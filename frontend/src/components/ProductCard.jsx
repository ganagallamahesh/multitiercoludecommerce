import React from 'react';
import { useCart } from '../context/CartContext';
import { ShoppingCart, Check } from 'lucide-react';

export default function ProductCard({ product, onNotification }) {
  const { addToCart, cart } = useCart();
  const isInCart = cart.some((item) => item.id === product.id);

  const handleAdd = () => {
    addToCart(product);
    if (onNotification) {
      onNotification(`Added "${product.title}" to shopping cart!`);
    }
  };

  return (
    <div className="product-card">
      <div className="product-image-container">
        <img
          src={product.image_url}
          alt={product.title}
          className="product-image"
          loading="lazy"
        />
        <span className="category-tag">{product.category}</span>
      </div>

      <div className="product-details">
        <h3 className="product-title">{product.title}</h3>
        <p className="product-description">{product.description}</p>

        <div className="product-footer">
          <div>
            <span className="product-price">₹{Number(product.price).toLocaleString('en-IN', { minimumFractionDigits: 2 })}</span>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              Stock: {product.stock} units
            </div>
          </div>

          <button
            onClick={handleAdd}
            className={`btn ${isInCart ? 'btn-outline' : 'btn-primary'}`}
            style={{ padding: '0.5rem 0.85rem' }}
          >
            {isInCart ? <Check size={16} /> : <ShoppingCart size={16} />}
            {isInCart ? 'In Cart' : 'Add to Cart'}
          </button>
        </div>
      </div>
    </div>
  );
}
