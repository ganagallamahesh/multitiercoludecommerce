const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

dotenv.config();

const authRoutes = require('./routes/authRoutes');
const productRoutes = require('./routes/productRoutes');
const orderRoutes = require('./routes/orderRoutes');

const app = express();
const PORT = process.env.PORT || 5000;

// Enable CORS for Frontend PaaS application
app.use(cors());
app.use(express.json());

// API Request Logging
app.use((req, res, next) => {
  console.log(`[IaaS Backend VM] ${req.method} ${req.originalUrl}`);
  next();
});

// Cloud Tier Status Endpoint
app.get('/api/health', (req, res) => {
  res.json({
    status: 'healthy',
    tier: 'Application Tier (Backend)',
    cloud_service_model: 'Infrastructure as a Service (IaaS)',
    vm_environment: process.env.NODE_ENV || 'development',
    timestamp: new Date().toISOString()
  });
});

// Mount Tier Routes
app.use('/api/auth', authRoutes);
app.use('/api/products', productRoutes);
app.use('/api/orders', orderRoutes);

// Global 404
app.use((req, res) => {
  res.status(404).json({ error: 'API route not found on IaaS Backend Server.' });
});

// Global Error Handler
app.use((err, req, res, next) => {
  console.error('Unhandled Error:', err);
  res.status(500).json({ error: 'Internal Server Error on Application Tier.' });
});

app.listen(PORT, () => {
  console.log(`=======================================================`);
  console.log(` E-Commerce Application Tier [IaaS VM REST API Server]`);
  console.log(` Running on: http://localhost:${PORT}`);
  console.log(` Health Check: http://localhost:${PORT}/api/health`);
  console.log(`=======================================================`);
});
