import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useCart } from '../context/CartContext';
import { Trash2, Plus, Minus, ArrowRight, ShoppingBag } from 'lucide-react';

export default function Cart() {
  const { cart, updateQuantity, removeFromCart, cartTotal, clearCart } = useCart();
  const navigate = useNavigate();

  if (cart.length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '4rem 1rem' }}>
        <div style={{ display: 'inline-flex', padding: '1rem', background: 'var(--bg-card)', borderRadius: 'var(--radius-full)', marginBottom: '1.25rem' }}>
          <ShoppingBag size={48} color="var(--text-muted)" />
        </div>
        <h2 style={{ fontSize: '1.5rem', fontWeight: 800, marginBottom: '0.5rem' }}>Your Cart is Empty</h2>
        <p style={{ color: 'var(--text-secondary)', marginBottom: '1.5rem' }}>
          Explore our cloud hardware catalog and add items to your shopping cart.
        </p>
        <Link to="/" className="btn btn-primary">
          Browse Product Catalog
        </Link>
      </div>
    );
  }

  return (
    <div>
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Shopping Cart</h1>
        <p style={{ color: 'var(--text-secondary)' }}>Review selected cloud platform items before checkout</p>
      </div>

      <div className="cart-layout">
        <div className="cart-items-list">
          {cart.map((item) => (
            <div key={item.id} className="cart-item">
              <img src={item.image_url} alt={item.title} className="cart-item-img" />
              
              <div className="cart-item-info">
                <h4 className="cart-item-title">{item.title}</h4>
                <div className="cart-item-price">${Number(item.price).toFixed(2)} each</div>
              </div>

              <div className="quantity-controls">
                <button onClick={() => updateQuantity(item.id, -1)} className="quantity-btn">
                  <Minus size={14} />
                </button>
                <span style={{ padding: '0 0.5rem', fontWeight: 700, fontSize: '0.9rem' }}>{item.quantity}</span>
                <button onClick={() => updateQuantity(item.id, 1)} className="quantity-btn">
                  <Plus size={14} />
                </button>
              </div>

              <div style={{ fontWeight: 800, width: '90px', textAlign: 'right' }}>
                ${(item.price * item.quantity).toFixed(2)}
              </div>

              <button onClick={() => removeFromCart(item.id)} className="btn btn-danger" style={{ padding: '0.4rem' }}>
                <Trash2 size={16} />
              </button>
            </div>
          ))}

          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '1rem' }}>
            <button onClick={clearCart} className="btn btn-outline" style={{ fontSize: '0.85rem' }}>
              Clear Cart
            </button>
            <Link to="/" className="nav-link" style={{ fontSize: '0.9rem' }}>
              ← Continue Shopping
            </Link>
          </div>
        </div>

        <div className="order-summary-card">
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800, marginBottom: '1.25rem' }}>Order Summary</h3>
          
          <div className="summary-row">
            <span>Subtotal ({cart.reduce((s, i) => s + i.quantity, 0)} items)</span>
            <span>${cartTotal.toFixed(2)}</span>
          </div>
          <div className="summary-row">
            <span>Cloud Delivery (PaaS Express)</span>
            <span style={{ color: 'var(--success)', fontWeight: 600 }}>FREE</span>
          </div>
          <div className="summary-row">
            <span>Estimated Tax</span>
            <span>$0.00</span>
          </div>

          <div className="summary-total">
            <span>Total</span>
            <span style={{ color: 'var(--accent-primary)' }}>${cartTotal.toFixed(2)}</span>
          </div>

          <button
            onClick={() => navigate('/checkout')}
            className="btn btn-primary"
            style={{ width: '100%', marginTop: '1.5rem', padding: '0.85rem' }}
          >
            Proceed to Checkout <ArrowRight size={16} />
          </button>
        </div>
      </div>
    </div>
  );
}
