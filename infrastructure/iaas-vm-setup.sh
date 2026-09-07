#!/bin/bash
# ==============================================================================
# IaaS Virtual Machine Provisioning & Bootstrap Script
# Multi-Tier Application Cloud Service Model Mapping (Application Tier)
# ==============================================================================

set -e

echo "=== [1/6] Updating System Packages ==="
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y curl git nginx ufw build-essential

echo "=== [2/6] Installing Node.js LTS Runtime ==="
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

echo "=== [3/6] Configuring Security Firewall (UFW) ==="
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw --force enable

echo "=== [4/6] Setting Up Application Directory & Repository ==="
sudo mkdir -p /var/www/ecommerce-backend
sudo chown -R $USER:$USER /var/www/ecommerce-backend

# Navigate and initialize environment
cd /var/www/ecommerce-backend

# Populate application systemd daemon script
sudo bash -c 'cat <<EOF > /etc/systemd/system/ecommerce-backend.service
[Unit]
Description=E-Commerce Backend REST API Daemon (IaaS VM Service)
After=network.target mysql.service

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/var/www/ecommerce-backend
ExecStart=/usr/bin/node src/server.js
Restart=always
RestartSec=5
Environment=NODE_ENV=production
Environment=PORT=5000

[Install]
WantedBy=multi-user.target
EOF'

echo "=== [5/6] Configuring Nginx Reverse Proxy ==="
sudo bash -c 'cat <<EOF > /etc/nginx/sites-available/ecommerce-api
server {
    listen 80;
    server_name _;

    location /api {
        proxy_pass http://127.0.0.1:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_cache_bypass \$http_upgrade;
    }
}
EOF'

sudo ln -sf /etc/nginx/sites-available/ecommerce-api /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx

echo "=== [6/6] Reloading Systemd & Starting Backend Daemon ==="
sudo systemctl daemon-reload
# sudo systemctl enable ecommerce-backend
# sudo systemctl start ecommerce-backend

echo "=== IaaS Virtual Machine Setup Completed Successfully ==="
