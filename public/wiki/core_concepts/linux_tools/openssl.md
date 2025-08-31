Here’s a **Linux `openssl` Cheat Sheet** with common commands and practical examples:

---

# Linux `openssl` Cheat Sheet

`openssl` is a versatile command-line tool for **SSL/TLS certificates**, **keys**, and **cryptographic operations**.

---

- [Linux `openssl` Cheat Sheet](#linux-openssl-cheat-sheet)
  - [**1. Key and Certificate Management**](#1-key-and-certificate-management)
    - [**Generate a Private Key**](#generate-a-private-key)
    - [**Generate a Self-Signed Certificate**](#generate-a-self-signed-certificate)
    - [**Generate a Certificate Signing Request (CSR)**](#generate-a-certificate-signing-request-csr)
    - [**Check Certificate Details**](#check-certificate-details)
    - [**Check CSR Details**](#check-csr-details)
    - [**Check Private Key Details**](#check-private-key-details)
    - [**Convert Private Key Formats**](#convert-private-key-formats)
      - [**PEM to DER**](#pem-to-der)
      - [**DER to PEM**](#der-to-pem)
    - [**Convert Certificate Formats**](#convert-certificate-formats)
      - [**PEM to DER**](#pem-to-der-1)
      - [**DER to PEM**](#der-to-pem-1)
    - [**Convert PKCS#12 (.p12) to PEM**](#convert-pkcs12-p12-to-pem)
    - [**Convert PEM to PKCS#12 (.p12)**](#convert-pem-to-pkcs12-p12)
  - [**2. Encryption and Decryption**](#2-encryption-and-decryption)
    - [**Encrypt a File**](#encrypt-a-file)
    - [**Decrypt a File**](#decrypt-a-file)
  - [**3. Hashing**](#3-hashing)
    - [**Generate a Hash**](#generate-a-hash)
    - [**Verify a Hash**](#verify-a-hash)
  - [**4. SSL/TLS Testing**](#4-ssltls-testing)
    - [**Test a Remote SSL Server**](#test-a-remote-ssl-server)
    - [**Check Certificate Expiry**](#check-certificate-expiry)
  - [**5. Common Options**](#5-common-options)
  - [**6. Tips**](#6-tips)


## **1. Key and Certificate Management**

### **Generate a Private Key**
```bash
openssl genpkey -algorithm RSA -out private.key -pkeyopt rsa_keygen_bits:2048
```
- Creates a **2048-bit RSA private key** (`private.key`).

---

### **Generate a Self-Signed Certificate**
```bash
openssl req -x509 -newkey rsa:2048 -keyout private.key -out cert.crt -days 365 -nodes
```
- Creates a **self-signed certificate** (`cert.crt`) and private key (`private.key`) valid for 365 days.
- `-nodes`: Skips password protection.

---

### **Generate a Certificate Signing Request (CSR)**
```bash
openssl req -new -key private.key -out request.csr
```
- Generates a CSR (`request.csr`) using an existing private key.

---

### **Check Certificate Details**
```bash
openssl x509 -in cert.crt -text -noout
```
- Displays detailed information about a certificate (`cert.crt`).

---

### **Check CSR Details**
```bash
openssl req -in request.csr -text -noout
```
- Displays details of a CSR (`request.csr`).

---

### **Check Private Key Details**
```bash
openssl rsa -in private.key -text -noout
```
- Displays details of a private key (`private.key`).

---

### **Convert Private Key Formats**
#### **PEM to DER**
```bash
openssl rsa -in private.key -outform DER -out private.der
```

#### **DER to PEM**
```bash
openssl rsa -inform DER -in private.der -out private.pem
```

---

### **Convert Certificate Formats**
#### **PEM to DER**
```bash
openssl x509 -in cert.crt -outform DER -out cert.der
```

#### **DER to PEM**
```bash
openssl x509 -inform DER -in cert.der -out cert.pem
```

---

### **Convert PKCS#12 (.p12) to PEM**
```bash
openssl pkcs12 -in cert.p12 -out cert.pem -nodes
```
- Extracts certificates and private keys from a `.p12` file.

---

### **Convert PEM to PKCS#12 (.p12)**
```bash
openssl pkcs12 -export -out cert.p12 -inkey private.key -in cert.crt
```
- Combines a private key and certificate into a `.p12` file.

---

## **2. Encryption and Decryption**

### **Encrypt a File**
```bash
openssl enc -aes-256-cbc -salt -in file.txt -out file.enc
```
- Encrypts `file.txt` using **AES-256-CBC** and outputs `file.enc`.

---

### **Decrypt a File**
```bash
openssl enc -d -aes-256-cbc -in file.enc -out file.txt
```
- Decrypts `file.enc` back to `file.txt`.

---

## **3. Hashing**

### **Generate a Hash**
```bash
openssl dgst -sha256 file.txt
```
- Computes the **SHA-256 hash** of `file.txt`.

---

### **Verify a Hash**
```bash
openssl dgst -sha256 -verify public.key -signature file.sig file.txt
```
- Verifies a signature (`file.sig`) using a public key.

---

## **4. SSL/TLS Testing**

### **Test a Remote SSL Server**
```bash
openssl s_client -connect example.com:443 -servername example.com
```
- Connects to `example.com` on port 443 and displays the SSL certificate.

---

### **Check Certificate Expiry**
```bash
openssl x509 -enddate -noout -in cert.crt
```
- Shows the expiry date of `cert.crt`.

---

## **5. Common Options**
| Option               | Description                                  |
|----------------------|----------------------------------------------|
| `-in <file>`         | Input file.                                  |
| `-out <file>`        | Output file.                                 |
| `-text`              | Output in human-readable format.             |
| `-noout`             | Do not output the encoded version.           |
| `-nodes`             | Skip password protection.                    |
| `-days <n>`          | Set certificate validity in days.            |
| `-sha256`            | Use SHA-256 for hashing.                     |

---

## **6. Tips**
- **Backup Keys**: Always back up private keys securely.
- **Permissions**: Restrict access to private keys (`chmod 400 private.key`).
- **Passwords**: Use strong passwords for private keys and keystores.
