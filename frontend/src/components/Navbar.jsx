import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useCart } from '../context/CartContext';
import { ShoppingBag, User, LogOut, Package, Cloud, Server, Database } from 'lucide-react';

export default function Navbar() {
  const { user, logoutUser } = useAuth();
  const { cartItemCount } = useCart();
  const navigate = useNavigate();

  const handleLogout = () => {
    logoutUser();
    navigate('/login');
  };

  return (
    <>
      {/* Cloud Service Model Tier Header */}
      <div className="cloud-tier-banner">
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Cloud size={16} color="#38bdf8" />
          <span><strong>Architecture Mapping:</strong> 3-Tier E-Commerce Cloud Platform</span>
        </div>
        <div className="cloud-badges">
          <span className="badge badge-paas">
            <Cloud size={12} /> Presentation: PaaS
          </span>
          <span className="badge badge-iaas">
            <Server size={12} /> Application: IaaS (VM)
          </span>
          <span className="badge badge-paas">
            <Database size={12} /> Database: PaaS (MySQL)
          </span>
        </div>
      </div>

      {/* Main App Navbar */}
      <nav className="navbar">
        <div className="navbar-content">
          <Link to="/" className="brand-logo">
            <Cloud color="#38bdf8" size={28} />
            Cloud<span>Mart</span>
          </Link>

          <div className="nav-links">
            <Link to="/" className="nav-link">Catalog</Link>

            <Link to="/cart" className="nav-link cart-icon-badge">
              <ShoppingBag size={20} />
              <span>Cart</span>
              {cartItemCount > 0 && <span className="cart-count">{cartItemCount}</span>}
            </Link>

            {user ? (
              <>
                <Link to="/orders" className="nav-link">
                  <Package size={18} /> Orders
                </Link>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                  <span style={{ fontSize: '0.875rem', color: 'var(--text-secondary)', fontWeight: 600 }}>
                    Hi, {user.name}
                  </span>
                  <button onClick={handleLogout} className="btn btn-outline" style={{ padding: '0.4rem 0.8rem', fontSize: '0.8rem' }}>
                    <LogOut size={14} /> Logout
                  </button>
                </div>
              </>
            ) : (
              <div style={{ display: 'flex', gap: '0.75rem' }}>
                <Link to="/login" className="btn btn-outline" style={{ padding: '0.45rem 1rem' }}>
                  Sign In
                </Link>
                <Link to="/register" className="btn btn-primary" style={{ padding: '0.45rem 1rem' }}>
                  Register
                </Link>
              </div>
            )}
          </div>
        </div>
      </nav>
    </>
  );
}
