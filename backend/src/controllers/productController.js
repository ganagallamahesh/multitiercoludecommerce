const db = require('../config/db');

// Fallback seed catalog for demonstration if DB is unseeded
const FALLBACK_PRODUCTS = [
  {
    id: 1,
    title: 'Cloud Tier High Performance Laptop',
    description: 'Next-gen Developer workstation with 32GB RAM, 1TB NVMe, optimized for cloud container orchestration.',
    price: 105999.00,
    stock: 25,
    category: 'Electronics',
    image_url: 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&q=80'
  },
  {
    id: 2,
    title: 'Noise-Canceling Wireless Headphones',
    description: 'Active noise reduction headphones with 30-hour battery life and multi-device connection.',
    price: 15990.00,
    stock: 40,
    category: 'Electronics',
    image_url: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&q=80'
  },
  {
    id: 3,
    title: 'Ergonomic Mesh Office Chair',
    description: 'Breathable lumbar support chair engineered for long coding sessions and remote workstation comfort.',
    price: 19999.00,
    stock: 15,
    category: 'Furniture',
    image_url: 'https://images.unsplash.com/photo-1580481072645-022f9a6d1261?w=800&q=80'
  },
  {
    id: 4,
    title: 'Ultra-Wide 4K Curved Monitor',
    description: '34-inch IPS display with 144Hz refresh rate, USB-C Power Delivery, and HDR 400 certification.',
    price: 39999.00,
    stock: 12,
    category: 'Electronics',
    image_url: 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800&q=80'
  },
  {
    id: 5,
    title: 'Wireless Mechanical Keyboard',
    description: 'Hot-swappable RGB mechanical keyboard with tactile switches and multi-device Bluetooth capability.',
    price: 9499.00,
    stock: 30,
    category: 'Accessories',
    image_url: 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&q=80'
  },
  {
    id: 6,
    title: 'Precision Ergonomic Gaming Mouse',
    description: 'Lightweight 26,000 DPI sensor mouse with customizable side buttons and braided ultra-flex cable.',
    price: 5499.00,
    stock: 50,
    category: 'Accessories',
    image_url: 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=800&q=80'
  }
];

// Get product catalog with search, filter, and pagination
exports.getAllProducts = async (req, res) => {
  try {
    const { category, search } = req.query;

    let query = 'SELECT * FROM products';
    const params = [];
    const conditions = [];

    if (category && category !== 'All') {
      conditions.push('category = ?');
      params.push(category);
    }

    if (search) {
      conditions.push('(title LIKE ? OR description LIKE ?)');
      params.push(`%${search}%`, `%${search}%`);
    }

    if (conditions.length > 0) {
      query += ' WHERE ' + conditions.join(' AND ');
    }

    query += ' ORDER BY id DESC';

    const [rows] = await db.query(query, params);
    
    if (rows && rows.length > 0) {
      return res.json({ products: rows, source: 'MySQL PaaS Tier' });
    }
    
    // If DB returned 0 rows or is unseeded, fallback gracefully
    let filteredFallback = FALLBACK_PRODUCTS;
    if (category && category !== 'All') {
      filteredFallback = filteredFallback.filter(p => p.category === category);
    }
    if (search) {
      filteredFallback = filteredFallback.filter(p => 
        p.title.toLowerCase().includes(search.toLowerCase()) || 
        p.description.toLowerCase().includes(search.toLowerCase())
      );
    }

    return res.json({ products: filteredFallback, source: 'Fallback Catalog' });
  } catch (error) {
    console.warn('DB Fetch failed, serving fallback products:', error.message);
    return res.json({ products: FALLBACK_PRODUCTS, source: 'Fallback Catalog (Offline DB)' });
  }
};

// Get single product by ID
exports.getProductById = async (req, res) => {
  try {
    const { id } = req.params;
    const [rows] = await db.query('SELECT * FROM products WHERE id = ?', [id]);

    if (rows.length > 0) {
      return res.json({ product: rows[0] });
    }

    const fallback = FALLBACK_PRODUCTS.find(p => p.id === parseInt(id));
    if (fallback) {
      return res.json({ product: fallback });
    }

    return res.status(404).json({ error: 'Product not found.' });
  } catch (error) {
    const fallback = FALLBACK_PRODUCTS.find(p => p.id === parseInt(req.params.id));
    if (fallback) return res.json({ product: fallback });
    res.status(500).json({ error: 'Failed to retrieve product details.', details: error.message });
  }
};
