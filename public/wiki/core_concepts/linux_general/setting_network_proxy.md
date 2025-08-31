### **Setting a System Proxy in `.bashrc`**

To configure a **system-wide proxy** for command-line tools (e.g., `curl`, `wget`, `apt`, `git`), you can add proxy settings to your `.bashrc` file. This ensures that all terminal sessions inherit the proxy configuration.

---

- [**1. Open `.bashrc`**](#1-open-bashrc)
- [**2. Add Proxy Settings**](#2-add-proxy-settings)
  - [**HTTP Proxy**](#http-proxy)
  - [**HTTPS Proxy**](#https-proxy)
  - [**FTP Proxy**](#ftp-proxy)
  - [**No Proxy for Local Addresses**](#no-proxy-for-local-addresses)
- [**3. Example Configuration**](#3-example-configuration)
- [**4. Save and Apply Changes**](#4-save-and-apply-changes)
- [**5. Verify Proxy Settings**](#5-verify-proxy-settings)
- [**6. Test the Proxy**](#6-test-the-proxy)
- [**7. Configure Proxy for Specific Tools**](#7-configure-proxy-for-specific-tools)
  - [**7.1. `apt` (Debian/Ubuntu)**](#71-apt-debianubuntu)
  - [**7.2. `git`**](#72-git)
  - [**7.3. `npm` (Node.js)**](#73-npm-nodejs)
  - [**7.4. `yum` (RHEL/CentOS)**](#74-yum-rhelcentos)
- [**8. Authentication (If Required)**](#8-authentication-if-required)
- [**9. Disable Proxy Temporarily**](#9-disable-proxy-temporarily)
- [**10. Permanent Proxy for All Users**](#10-permanent-proxy-for-all-users)
- [**11. Troubleshooting**](#11-troubleshooting)
- [**12. Example: Full `.bashrc` Proxy Configuration**](#12-example-full-bashrc-proxy-configuration)
- [**13. Notes**](#13-notes)


## **1. Open `.bashrc`**
Edit your `.bashrc` file in your home directory:
```bash
nano ~/.bashrc
```

---

## **2. Add Proxy Settings**
Add the following lines to the end of the file, replacing `proxy-server-ip` and `port` with your proxy server’s address and port (e.g., `192.168.1.100:8080`):

### **HTTP Proxy**
```bash
export http_proxy="http://proxy-server-ip:port"
export HTTP_PROXY="$http_proxy"
```

### **HTTPS Proxy**
```bash
export https_proxy="http://proxy-server-ip:port"
export HTTPS_PROXY="$https_proxy"
```

### **FTP Proxy**
```bash
export ftp_proxy="http://proxy-server-ip:port"
export FTP_PROXY="$ftp_proxy"
```

### **No Proxy for Local Addresses**
```bash
export no_proxy="localhost,127.0.0.1,192.168.0.0/16,10.0.0.0/8"
export NO_PROXY="$no_proxy"
```

---

## **3. Example Configuration**
```bash
# Proxy settings
export http_proxy="http://192.168.1.100:8080"
export HTTP_PROXY="$http_proxy"
export https_proxy="http://192.168.1.100:8080"
export HTTPS_PROXY="$https_proxy"
export ftp_proxy="http://192.168.1.100:8080"
export FTP_PROXY="$ftp_proxy"
export no_proxy="localhost,127.0.0.1,192.168.0.0/16,10.0.0.0/8"
export NO_PROXY="$no_proxy"
```

---

## **4. Save and Apply Changes**
1. Save the file (`Ctrl+O`, then `Enter` in `nano`).
2. Exit the editor (`Ctrl+X` in `nano`).
3. Reload `.bashrc` to apply the changes:
   ```bash
   source ~/.bashrc
   ```

---

## **5. Verify Proxy Settings**
Check if the environment variables are set:
```bash
env | grep -i proxy
```
Output should look like:
```
http_proxy=http://192.168.1.100:8080
HTTPS_PROXY=http://192.168.1.100:8080
no_proxy=localhost,127.0.0.1,192.168.0.0/16,10.0.0.0/8
```

---

## **6. Test the Proxy**
Test the proxy with `curl` or `wget`:
```bash
curl -I https://google.com
```
or
```bash
wget -qO- https://google.com
```

---

## **7. Configure Proxy for Specific Tools**

### **7.1. `apt` (Debian/Ubuntu)**
Create or edit `/etc/apt/apt.conf.d/proxy.conf`:
```bash
sudo nano /etc/apt/apt.conf.d/proxy.conf
```
Add:
```plaintext
Acquire::http::Proxy "http://proxy-server-ip:port";
Acquire::https::Proxy "http://proxy-server-ip:port";
```

---

### **7.2. `git`**
Configure Git to use the proxy:
```bash
git config --global http.proxy http://proxy-server-ip:port
git config --global https.proxy http://proxy-server-ip:port
```

---

### **7.3. `npm` (Node.js)**
Configure npm to use the proxy:
```bash
npm config set proxy http://proxy-server-ip:port
npm config set https-proxy http://proxy-server-ip:port
```

---

### **7.4. `yum` (RHEL/CentOS)**
Edit `/etc/yum.conf`:
```bash
sudo nano /etc/yum.conf
```
Add:
```plaintext
proxy=http://proxy-server-ip:port
```

---

## **8. Authentication (If Required)**
If your proxy requires authentication, include the username and password in the proxy URL:
```bash
export http_proxy="http://username:password@proxy-server-ip:port"
export https_proxy="http://username:password@proxy-server-ip:port"
```

---

## **9. Disable Proxy Temporarily**
To temporarily disable the proxy, unset the environment variables:
```bash
unset http_proxy HTTP_PROXY https_proxy HTTPS_PROXY ftp_proxy FTP_PROXY no_proxy NO_PROXY
```

---

## **10. Permanent Proxy for All Users**
To set the proxy system-wide (for all users), add the proxy settings to `/etc/environment`:
```bash
sudo nano /etc/environment
```
Add:
```plaintext
http_proxy="http://proxy-server-ip:port"
HTTP_PROXY="http://proxy-server-ip:port"
https_proxy="http://proxy-server-ip:port"
HTTPS_PROXY="http://proxy-server-ip:port"
ftp_proxy="http://proxy-server-ip:port"
FTP_PROXY="http://proxy-server-ip:port"
no_proxy="localhost,127.0.0.1,192.168.0.0/16,10.0.0.0/8"
NO_PROXY="localhost,127.0.0.1,192.168.0.0/16,10.0.0.0/8"
```

---

## **11. Troubleshooting**
- **Connection Refused**: Verify the proxy server is running and the port is open.
- **Authentication Failed**: Ensure the username and password are correct.
- **DNS Issues**: Add `use_proxy_dns=true` to the proxy URL if DNS resolution fails.
- **SSL/TLS Errors**: Use `https_proxy` for HTTPS traffic and ensure certificates are trusted.

---

## **12. Example: Full `.bashrc` Proxy Configuration**
```bash
# Proxy settings
export http_proxy="http://192.168.1.100:8080"
export HTTP_PROXY="$http_proxy"
export https_proxy="http://192.168.1.100:8080"
export HTTPS_PROXY="$https_proxy"
export ftp_proxy="http://192.168.1.100:8080"
export FTP_PROXY="$ftp_proxy"
export no_proxy="localhost,127.0.0.1,192.168.0.0/16,10.0.0.0/8"
export NO_PROXY="$no_proxy"

# Alias to toggle proxy
alias proxy-on='source ~/.bashrc'
alias proxy-off='unset http_proxy HTTP_PROXY https_proxy HTTPS_PROXY ftp_proxy FTP_PROXY no_proxy NO_PROXY'
```

---

## **13. Notes**
- Proxy settings in `.bashrc` only affect **command-line tools** and **terminal sessions**. GUI applications may require separate proxy configurations.
- For **systemd services**, configure proxies in the service’s environment file (e.g., `/etc/systemd/system/service-name.service.d/override.conf`).
- Use `export -p` to list all exported environment variables.