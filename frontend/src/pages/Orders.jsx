import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { Package, Calendar, MapPin, CheckCircle } from 'lucide-react';

export default function Orders() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const { token } = useAuth();

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await fetch('/api/orders/my-orders', {
          headers: { Authorization: `Bearer ${token}` }
        });
        const data = await response.json();
        setOrders(data.orders || []);
      } catch (err) {
        console.error('Failed to load orders:', err);
      } finally {
        setLoading(false);
      }
    };

    if (token) fetchOrders();
  }, [token]);

  if (loading) {
    return <div style={{ textAlign: 'center', padding: '4rem 0' }}>Loading Order History...</div>;
  }

  return (
    <div>
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Order History</h1>
        <p style={{ color: 'var(--text-secondary)' }}>
          Retrieved from <strong>MySQL PaaS Data Tier</strong> via <strong>IaaS REST API</strong>
        </p>
      </div>

      {orders.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '4rem 1rem', background: 'var(--bg-card)', borderRadius: 'var(--radius-md)' }}>
          <Package size={48} color="var(--text-muted)" style={{ marginBottom: '1rem' }} />
          <h3 style={{ fontSize: '1.2rem', fontWeight: 700, marginBottom: '0.5rem' }}>No Orders Found</h3>
          <p style={{ color: 'var(--text-secondary)' }}>You haven't placed any orders yet.</p>
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          {orders.map((order) => (
            <div key={order.id} className="order-summary-card">
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem', borderBottom: '1px solid var(--border-color)', paddingBottom: '0.75rem' }}>
                <div>
                  <h3 style={{ fontSize: '1.1rem', fontWeight: 800, color: 'var(--text-primary)' }}>
                    Order #{order.id}
                  </h3>
                  <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                    <Calendar size={13} /> {new Date(order.created_at || Date.now()).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })}
                  </span>
                </div>

                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                  <span className="badge badge-paas" style={{ textTransform: 'uppercase' }}>
                    <CheckCircle size={12} /> {order.status}
                  </span>
                  <span style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--accent-primary)' }}>
                    ${Number(order.total_amount).toFixed(2)}
                  </span>
                </div>
              </div>

              <div style={{ fontSize: '0.875rem', color: 'var(--text-secondary)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <MapPin size={14} color="#38bdf8" /> <strong>Shipping Address:</strong> {order.shipping_address}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
