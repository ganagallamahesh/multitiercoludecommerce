const mysql = require('mysql2/promise');
const dotenv = require('dotenv');

dotenv.config();

const pool = mysql.createPool({
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT || '3306'),
  user: process.env.DB_USER || 'ecommerce_user',
  password: process.env.DB_PASSWORD || 'ecommerce_pass',
  database: process.env.DB_NAME || 'ecommerce_db',
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
  connectTimeout: 10000
});

// Test connection on module initialize
pool.getConnection()
  .then((conn) => {
    console.log(`[PaaS MySQL Data Tier] Connection established successfully to DB: ${process.env.DB_NAME || 'ecommerce_db'}`);
    conn.release();
  })
  .catch((err) => {
    console.warn(`[PaaS MySQL Data Tier Warning] Database connection pending/offline: ${err.message}`);
  });

module.exports = pool;
