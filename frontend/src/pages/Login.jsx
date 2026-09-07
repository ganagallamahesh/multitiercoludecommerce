import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { LogIn, Lock, Mail, Server } from 'lucide-react';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { loginUser } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Authentication failed.');
      }

      loginUser(data.user, data.token);
      navigate('/');
    } catch (err) {
      // Fallback auth for local demo testing if API is unreachable
      if (email === 'user@cloudmapping.com' && password === 'password123') {
        const demoUser = { id: 1, name: 'Cloud Architect Demo User', email, role: 'customer' };
        loginUser(demoUser, 'demo_jwt_token_12345');
        navigate('/');
        return;
      }
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-card">
      <div className="auth-header">
        <div style={{ display: 'inline-flex', padding: '0.65rem', background: 'var(--accent-light)', borderRadius: 'var(--radius-full)', marginBottom: '0.75rem' }}>
          <LogIn size={24} color="#38bdf8" />
        </div>
        <h2>User Login</h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem' }}>
          Authentication handled via <strong>IaaS REST API (JWT)</strong>
        </p>
      </div>

      {error && (
        <div
          style={{
            background: 'rgba(239, 68, 68, 0.15)',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            color: 'var(--danger)',
            padding: '0.75rem 1rem',
            borderRadius: 'var(--radius-sm)',
            fontSize: '0.875rem',
            marginBottom: '1.25rem'
          }}
        >
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Email Address</label>
          <div style={{ position: 'relative' }}>
            <input
              type="email"
              required
              placeholder="user@cloudmapping.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              style={{ paddingLeft: '2.5rem' }}
            />
            <Mail size={16} color="var(--text-muted)" style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)' }} />
          </div>
        </div>

        <div className="form-group">
          <label>Password</label>
          <div style={{ position: 'relative' }}>
            <input
              type="password"
              required
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={{ paddingLeft: '2.5rem' }}
            />
            <Lock size={16} color="var(--text-muted)" style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)' }} />
          </div>
        </div>

        <button
          type="submit"
          className="btn btn-primary"
          style={{ width: '100%', marginTop: '1rem', padding: '0.75rem' }}
          disabled={loading}
        >
          {loading ? 'Authenticating with IaaS Backend...' : 'Sign In'}
        </button>
      </form>

      <div style={{ marginTop: '1.5rem', textAlign: 'center', fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
        Demo Credentials: <code style={{ color: 'var(--accent-primary)', background: 'var(--bg-secondary)', padding: '0.15rem 0.4rem', borderRadius: '4px' }}>user@cloudmapping.com</code> / <code style={{ color: 'var(--accent-primary)', background: 'var(--bg-secondary)', padding: '0.15rem 0.4rem', borderRadius: '4px' }}>password123</code>
      </div>

      <div style={{ marginTop: '1rem', textAlign: 'center', fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
        Don't have an account? <Link to="/register" style={{ color: 'var(--accent-primary)', fontWeight: 600 }}>Register Now</Link>
      </div>
    </div>
  );
}
