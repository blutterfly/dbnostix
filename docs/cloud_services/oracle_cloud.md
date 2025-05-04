Here is a concise summary of the article **"How I Set Up a Free Server That I’ll Never Have to Pay For" by Frost** from Medium, along with actionable **steps** and relevant **code blocks**:

---

## 🧾 Summary

Frost explains how to set up a **permanently free Linux server** using Oracle Cloud's "Always Free" tier, useful for hosting websites, running projects, or experimenting.

---

## ⚙️ How-To Guide

### ✅ Step 1: Sign Up on Oracle Cloud

1. Go to [https://signup.cloud.oracle.com](https://signup.cloud.oracle.com)
2. Fill in your details (name, email, and payment info — no charges apply for free tier).
3. Complete the signup and log in.

---

### ✅ Step 2: Create a Free Instance

1. In the Oracle Cloud dashboard:

   * Navigate to **Compute > Instances**
   * Click **"Create Instance"**
   * Enable the **"Always Free resources only"** option.

---

### ✅ Step 3: Save Your SSH Keys

* During instance creation, Oracle generates an SSH key pair.
* Download and save both the **public** and **private** keys to your system.

---

### ✅ Step 4: Connect to Your Server via SSH

Use this command in your terminal (adjust `<key-file-name>` and `your-public-ip` accordingly):

```bash
ssh -i <key-file-name> ubuntu@your-public-ip
```

> Example:

```bash
ssh -i ~/.ssh/oracle_free.pem ubuntu@132.145.75.23
```

---

## 💡 Use Cases

Once connected, you can:

* Host a website or web application
* Deploy and test code
* Run databases, backend services, or custom scripts

---


Here's a **Bash automation script** to streamline the setup of your Oracle Cloud free server, including SSH config and initial connection. This assumes you're manually creating the instance via the dashboard (Oracle doesn't support full automation of free-tier VM creation via CLI for new accounts).

---

## 🛠 `setup_oracle_free_server.sh`

```bash
#!/bin/bash

# Constants (Edit as needed)
KEY_NAME="oracle_free"
KEY_DIR="$HOME/.ssh"
KEY_PATH="$KEY_DIR/$KEY_NAME.pem"
USER="ubuntu"

# Prompt for public IP
read -p "Enter your Oracle public IP address: " PUBLIC_IP

# 1. Generate SSH Key (skip if you already downloaded it)
echo "Ensure your private key is saved as $KEY_PATH"
if [ ! -f "$KEY_PATH" ]; then
    echo "❌ Private key not found. Please download it from Oracle dashboard."
    exit 1
fi

# 2. Set correct permissions
chmod 400 "$KEY_PATH"
echo "✅ Key permissions set to 400"

# 3. Add to SSH config
SSH_CONFIG="$KEY_DIR/config"
if ! grep -q "$PUBLIC_IP" "$SSH_CONFIG" 2>/dev/null; then
    echo "🔧 Adding SSH config entry..."
    cat <<EOF >> "$SSH_CONFIG"

Host oracle-free
    HostName $PUBLIC_IP
    User $USER
    IdentityFile $KEY_PATH
    IdentitiesOnly yes
EOF
    echo "✅ SSH config updated."
else
    echo "ℹ️ SSH config for this IP already exists."
fi

# 4. Test SSH connection
echo "🌐 Connecting to Oracle server..."
ssh oracle-free
```

---

## 🔧 Instructions

1. Save this as `setup_oracle_free_server.sh`
2. Run it with:

   ```bash
   chmod +x setup_oracle_free_server.sh
   ./setup_oracle_free_server.sh
   ```
3. Follow the prompts.

---

Great — here's an **enhanced version** of the script that, once connected to your Oracle Free Tier server, automatically installs common development tools:

---

## 🔧 `setup_oracle_free_server.sh` (with auto-install)

```bash
#!/bin/bash

# Constants
KEY_NAME="oracle_free"
KEY_DIR="$HOME/.ssh"
KEY_PATH="$KEY_DIR/$KEY_NAME.pem"
USER="ubuntu"

# Prompt for public IP
read -p "Enter your Oracle public IP address: " PUBLIC_IP

# Step 1: Ensure private key exists
if [ ! -f "$KEY_PATH" ]; then
    echo "❌ Private key not found at $KEY_PATH. Please download it from Oracle and place it there."
    exit 1
fi

# Step 2: Set permissions
chmod 400 "$KEY_PATH"
echo "✅ Set permissions for key file"

# Step 3: Add SSH config for convenience
SSH_CONFIG="$KEY_DIR/config"
if ! grep -q "$PUBLIC_IP" "$SSH_CONFIG" 2>/dev/null; then
    echo "🔧 Updating SSH config..."
    cat <<EOF >> "$SSH_CONFIG"

Host oracle-free
    HostName $PUBLIC_IP
    User $USER
    IdentityFile $KEY_PATH
    IdentitiesOnly yes
EOF
    echo "✅ SSH config updated."
fi

# Step 4: Connect and install tools
echo "🚀 Connecting and installing packages..."

ssh oracle-free <<'EOF'
echo "🔧 Updating package index..."
sudo apt update -y

echo "📦 Installing common packages..."
sudo apt install -y nginx git ufw fail2ban htop curl

echo "🔥 Configuring UFW firewall..."
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw --force enable

echo "✅ Setup complete. Installed: nginx, git, ufw, fail2ban, htop, curl"
EOF
```

---

## ✅ What It Does

* **Checks key** and SSH config
* **Connects to the server via SSH**
* **Installs**:

  * `nginx` (web server)
  * `git` (version control)
  * `ufw` (firewall)
  * `fail2ban` (basic security)
  * `htop` (system monitor)
  * `curl` (network utility)
* **Enables firewall** and opens necessary ports

---

Perfect! Here’s the **final version** of your setup script — it not only installs essential packages but also creates a custom Nginx homepage with your name or project information.

---

## 🖥 `setup_oracle_free_server.sh` (Full Setup with Homepage)

```bash
#!/bin/bash

# Constants
KEY_NAME="oracle_free"
KEY_DIR="$HOME/.ssh"
KEY_PATH="$KEY_DIR/$KEY_NAME.pem"
USER="ubuntu"

# Prompt for public IP and homepage title
read -p "Enter your Oracle public IP address: " PUBLIC_IP
read -p "Enter a title for your homepage (e.g., 'Welcome to My Server'): " HOMEPAGE_TITLE
read -p "Enter a short description (e.g., 'Hosted on Oracle Cloud Free Tier'): " HOMEPAGE_DESC

# Step 1: Ensure private key exists
if [ ! -f "$KEY_PATH" ]; then
    echo "❌ Private key not found at $KEY_PATH. Please download it from Oracle and place it there."
    exit 1
fi

# Step 2: Set permissions
chmod 400 "$KEY_PATH"
echo "✅ Set permissions for key file"

# Step 3: Add SSH config
SSH_CONFIG="$KEY_DIR/config"
if ! grep -q "$PUBLIC_IP" "$SSH_CONFIG" 2>/dev/null; then
    echo "🔧 Adding SSH config entry..."
    cat <<EOF >> "$SSH_CONFIG"

Host oracle-free
    HostName $PUBLIC_IP
    User $USER
    IdentityFile $KEY_PATH
    IdentitiesOnly yes
EOF
    echo "✅ SSH config updated."
fi

# Step 4: Connect and set up server
echo "🚀 Connecting to server and configuring..."

ssh oracle-free <<EOF
echo "🔄 Updating packages..."
sudo apt update -y

echo "📦 Installing tools..."
sudo apt install -y nginx git ufw fail2ban htop curl

echo "🔥 Setting up UFW firewall..."
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw --force enable

echo "🌐 Creating custom Nginx homepage..."
sudo bash -c 'cat > /var/www/html/index.nginx-debian.html <<EOPAGE
<!DOCTYPE html>
<html>
<head>
    <title>$HOMEPAGE_TITLE</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 10%; }
        h1 { font-size: 2.5em; color: #333; }
        p { font-size: 1.2em; color: #666; }
    </style>
</head>
<body>
    <h1>$HOMEPAGE_TITLE</h1>
    <p>$HOMEPAGE_DESC</p>
</body>
</html>
EOPAGE'

sudo systemctl reload nginx
echo "✅ Setup complete! Visit http://$PUBLIC_IP"
EOF
```

---

## 🧪 Result

After you run this script:

* SSH is set up and secured.
* A firewall is configured with necessary rules.
* Your server has useful packages pre-installed.
* Your custom homepage is live at `http://<your-public-ip>`

---




