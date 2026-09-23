-- ==============================================================================
-- MySQL Seed Data Script
-- Multi-Tier Application Cloud Service Model Mapping (Data Tier - PaaS)
-- ==============================================================================

USE ecommerce_db;

-- Clear existing data for clean setup
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE order_items;
TRUNCATE TABLE orders;
TRUNCATE TABLE products;
TRUNCATE TABLE users;
SET FOREIGN_KEY_CHECKS = 1;

-- Seed Default Demo User (Password: password123)
-- bcrypt hash for 'password123': $2b$10$wN9Q7i9N2Z5.FhVv6.Gz4OqP9yG/r0N6A2o8n3G6W6P3n
INSERT INTO users (id, name, email, password_hash, role) VALUES
(1, 'Cloud Architect Demo User', 'user@cloudmapping.com', '$2b$10$wN9Q7i9N2Z5.FhVv6.Gz4OqP9yG/r0N6A2o8n3G6W6P3n', 'customer'),
(2, 'System Administrator', 'admin@cloudmapping.com', '$2b$10$wN9Q7i9N2Z5.FhVv6.Gz4OqP9yG/r0N6A2o8n3G6W6P3n', 'admin');

-- Seed E-Commerce Catalog Products (Image URLs mapped to Cloud Storage S3/GCS buckets)
INSERT INTO products (id, title, description, price, stock, category, image_url) VALUES
(1, 'Cloud Tier High Performance Laptop', 'Next-gen Developer workstation with 32GB RAM, 1TB NVMe, optimized for cloud container orchestration.', 105999.00, 25, 'Electronics', 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&q=80'),
(2, 'Noise-Canceling Wireless Headphones', 'Active noise reduction headphones with 30-hour battery life and multi-device connection.', 15990.00, 40, 'Electronics', 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&q=80'),
(3, 'Ergonomic Mesh Office Chair', 'Breathable lumbar support chair engineered for long coding sessions and remote workstation comfort.', 19999.00, 15, 'Furniture', 'https://images.unsplash.com/photo-1580481072645-022f9a6d1261?w=800&q=80'),
(4, 'Ultra-Wide 4K Curved Monitor', '34-inch IPS display with 144Hz refresh rate, USB-C Power Delivery, and HDR 400 certification.', 39999.00, 12, 'Electronics', 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800&q=80'),
(5, 'Wireless Mechanical Keyboard', 'Hot-swappable RGB mechanical keyboard with tactile switches and multi-device Bluetooth capability.', 9499.00, 30, 'Accessories', 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&q=80'),
(6, 'Precision Ergonomic Gaming Mouse', 'Lightweight 26,000 DPI sensor mouse with customizable side buttons and braided ultra-flex cable.', 5499.00, 50, 'Accessories', 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=800&q=80');

-- Seed Initial Demo Order
INSERT INTO orders (id, user_id, total_amount, status, shipping_address) VALUES
(1, 1, 121989.00, 'delivered', '742 Cloud Avenue, Tech City, Bengaluru, KA 560001');

INSERT INTO order_items (id, order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 1, 105999.00),
(2, 1, 2, 1, 15990.00);
