const db = require('../config/db');

// In-memory fallback order store if DB connection is unavailable
const MEMORY_ORDERS = [];

// Create new order (Checkout Processing)
exports.createOrder = async (req, res) => {
  const userId = req.user.id;
  const { items, shippingAddress, totalAmount } = req.body;

  if (!items || !Array.isArray(items) || items.length === 0) {
    return res.status(400).json({ error: 'Order must contain at least one product item.' });
  }

  if (!shippingAddress) {
    return res.status(400).json({ error: 'Shipping address is required.' });
  }

  let connection;
  try {
    connection = await db.getConnection();
    await connection.beginTransaction();

    // Insert main order record into PaaS MySQL DB
    const [orderResult] = await connection.query(
      'INSERT INTO orders (user_id, total_amount, status, shipping_address) VALUES (?, ?, ?, ?)',
      [userId, totalAmount, 'paid', shippingAddress]
    );

    const orderId = orderResult.insertId;

    // Insert order items
    for (const item of items) {
      await connection.query(
        'INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?)',
        [orderId, item.id || item.product_id, item.quantity, item.price]
      );

      // Decrement product stock
      await connection.query(
        'UPDATE products SET stock = GREATEST(0, stock - ?) WHERE id = ?',
        [item.quantity, item.id || item.product_id]
      );
    }

    await connection.commit();
    connection.release();

    return res.status(201).json({
      message: 'Order processed successfully!',
      orderId,
      totalAmount,
      status: 'paid',
      tier: 'Application IaaS Engine -> MySQL PaaS Tier'
    });
  } catch (error) {
    if (connection) {
      await connection.rollback();
      connection.release();
    }
    console.warn('DB Transaction error during order placement, using memory fallback:', error.message);

    // Fallback order generation for dev mode
    const fallbackOrderId = Date.now();
    const newOrder = {
      id: fallbackOrderId,
      user_id: userId,
      total_amount: totalAmount,
      status: 'paid',
      shipping_address: shippingAddress,
      created_at: new Date().toISOString(),
      items
    };
    MEMORY_ORDERS.unshift(newOrder);

    return res.status(201).json({
      message: 'Order processed successfully (Dev Mode)',
      orderId: fallbackOrderId,
      totalAmount,
      status: 'paid'
    });
  }
};

// Get current user's order history
exports.getUserOrders = async (req, res) => {
  const userId = req.user.id;

  try {
    const [orders] = await db.query(
      `SELECT o.id, o.total_amount, o.status, o.shipping_address, o.created_at,
              COUNT(oi.id) as item_count
       FROM orders o
       LEFT JOIN order_items oi ON o.id = oi.order_id
       WHERE o.user_id = ?
       GROUP BY o.id
       ORDER BY o.created_at DESC`,
      [userId]
    );

    if (orders.length > 0) {
      return res.json({ orders });
    }

    const userMemoryOrders = MEMORY_ORDERS.filter(o => o.user_id === userId);
    return res.json({ orders: userMemoryOrders });
  } catch (error) {
    const userMemoryOrders = MEMORY_ORDERS.filter(o => o.user_id === userId);
    return res.json({ orders: userMemoryOrders });
  }
};
