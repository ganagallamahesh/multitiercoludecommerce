import React, { useState, useEffect } from 'react';
import ProductCard from '../components/ProductCard';
import Notification from '../components/Notification';
import { Search, Filter, Layers } from 'lucide-react';

export default function Catalog() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [category, setCategory] = useState('All');
  const [search, setSearch] = useState('');
  const [notification, setNotification] = useState('');
  const [dataSource, setDataSource] = useState('');

  const fetchProducts = async () => {
    setLoading(true);
    try {
      const queryParams = new URLSearchParams();
      if (category !== 'All') queryParams.append('category', category);
      if (search) queryParams.append('search', search);

      const response = await fetch(`/api/products?${queryParams.toString()}`);
      const data = await response.json();
      setProducts(data.products || []);
      setDataSource(data.source || 'REST API Tier');
    } catch (error) {
      console.error('Failed to fetch products:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, [category]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    fetchProducts();
  };

  return (
    <div>
      <Notification message={notification} onClose={() => setNotification('')} />

      <div className="catalog-header">
        <div className="catalog-title">
          <h1>Product Catalog</h1>
          <p>
            Connected to <strong>IaaS Backend REST API</strong> & <strong>PaaS MySQL Data Tier</strong>
          </p>
        </div>

        <form onSubmit={handleSearchSubmit} className="filters-bar">
          <div style={{ position: 'relative' }}>
            <input
              type="text"
              placeholder="Search products..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              style={{ paddingLeft: '2.4rem', width: '220px' }}
            />
            <Search
              size={16}
              color="var(--text-muted)"
              style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)' }}
            />
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Filter size={16} color="var(--text-muted)" />
            <select value={category} onChange={(e) => setCategory(e.target.value)}>
              <option value="All">All Categories</option>
              <option value="Electronics">Electronics</option>
              <option value="Furniture">Furniture</option>
              <option value="Accessories">Accessories</option>
            </select>
          </div>
        </form>
      </div>

      {/* Tier Info Banner */}
      <div
        style={{
          background: 'var(--bg-card)',
          border: '1px solid var(--border-color)',
          borderRadius: 'var(--radius-md)',
          padding: '0.85rem 1.25rem',
          marginBottom: '2rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          fontSize: '0.875rem'
        }}
      >
        <span style={{ color: 'var(--text-secondary)' }}>
          Showing <strong>{products.length}</strong> cloud platform items
        </span>
        <span style={{ color: 'var(--accent-primary)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
          <Layers size={14} /> Data Source: {dataSource}
        </span>
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', padding: '4rem 0', color: 'var(--text-secondary)' }}>
          <p>Loading Product Catalog from IaaS API...</p>
        </div>
      ) : products.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '4rem 0', color: 'var(--text-secondary)' }}>
          <p>No products matching your search criteria.</p>
        </div>
      ) : (
        <div className="product-grid">
          {products.map((product) => (
            <ProductCard
              key={product.id}
              product={product}
              onNotification={(msg) => setNotification(msg)}
            />
          ))}
        </div>
      )}
    </div>
  );
}
