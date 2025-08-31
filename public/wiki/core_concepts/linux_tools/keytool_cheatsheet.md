Here’s a **Linux `keytool` Cheat Sheet** with common commands and examples:

---


# Linux `keytool` Cheat Sheet

`keytool` is a Java-based command-line utility for managing **keystores**, **certificates**, and **cryptographic keys**. It is part of the Java Development Kit (JDK).

---

- [Linux `keytool` Cheat Sheet](#linux-keytool-cheat-sheet)
  - [**1. Common Commands**](#1-common-commands)
    - [**Generate a Keystore and Key Pair**](#generate-a-keystore-and-key-pair)
    - [**List Contents of a Keystore**](#list-contents-of-a-keystore)
    - [**Export a Certificate**](#export-a-certificate)
    - [**Import a Certificate into a Keystore**](#import-a-certificate-into-a-keystore)
    - [**Delete a Certificate or Key**](#delete-a-certificate-or-key)
    - [**Change Keystore Password**](#change-keystore-password)
    - [**Change Key Password**](#change-key-password)
    - [**Generate a Certificate Signing Request (CSR)**](#generate-a-certificate-signing-request-csr)
    - [**Import a CA-Signed Certificate**](#import-a-ca-signed-certificate)
    - [**Check Certificate Details**](#check-certificate-details)
    - [**Convert Keystore Format (JKS to PKCS12)**](#convert-keystore-format-jks-to-pkcs12)
    - [**List Trusted Certificates in a Keystore**](#list-trusted-certificates-in-a-keystore)
  - [**2. Common Options**](#2-common-options)
  - [**3. Tips**](#3-tips)


## **1. Common Commands**

### **Generate a Keystore and Key Pair**
```bash
keytool -genkeypair -alias mydomain -keyalg RSA -keysize 2048 -keystore keystore.jks -validity 365
```
- Creates a **keystore** (`keystore.jks`) with a **self-signed certificate**.
- Replace `mydomain` with your alias and set a password when prompted.

---

### **List Contents of a Keystore**
```bash
keytool -list -keystore keystore.jks
```
- Lists all entries in the keystore.
- Add `-v` for detailed output.

---

### **Export a Certificate**
```bash
keytool -exportcert -alias mydomain -keystore keystore.jks -file mydomain.crt
```
- Exports the certificate for `mydomain` to `mydomain.crt`.

---

### **Import a Certificate into a Keystore**
```bash
keytool -importcert -alias importedcert -keystore keystore.jks -file certificate.crt
```
- Imports a certificate (e.g., `certificate.crt`) into the keystore.

---

### **Delete a Certificate or Key**
```bash
keytool -delete -alias mydomain -keystore keystore.jks
```
- Removes the entry with the alias `mydomain`.

---

### **Change Keystore Password**
```bash
keytool -storepasswd -keystore keystore.jks
```
- Prompts for the **old** and **new** keystore passwords.

---

### **Change Key Password**
```bash
keytool -keypasswd -alias mydomain -keystore keystore.jks
```
- Changes the password for the key associated with `mydomain`.

---

### **Generate a Certificate Signing Request (CSR)**
```bash
keytool -certreq -alias mydomain -keystore keystore.jks -file mydomain.csr
```
- Creates a CSR (`mydomain.csr`) for submission to a Certificate Authority (CA).

---

### **Import a CA-Signed Certificate**
```bash
keytool -importcert -alias mydomain -keystore keystore.jks -file signed_cert.crt
```
- Imports a **signed certificate** (e.g., `signed_cert.crt`) into the keystore.

---

### **Check Certificate Details**
```bash
keytool -printcert -file mydomain.crt
```
- Displays details of a certificate file.

---

### **Convert Keystore Format (JKS to PKCS12)**
```bash
keytool -importkeystore -srckeystore keystore.jks -destkeystore keystore.p12 -deststoretype PKCS12
```
- Converts a JKS keystore to PKCS12 format.

---

### **List Trusted Certificates in a Keystore**
```bash
keytool -list -keystore $JAVA_HOME/lib/security/cacerts
```
- Lists trusted CA certificates in the default Java cacerts file.
- Default password: `changeit`.

---

## **2. Common Options**
| Option               | Description                                  |
|----------------------|----------------------------------------------|
| `-alias <alias>`     | Specifies the alias for the entry.           |
| `-keystore <file>`   | Specifies the keystore file.                 |
| `-storepass <pass>`  | Provides the keystore password.              |
| `-keypass <pass>`    | Provides the key password.                   |
| `-validity <days>`   | Sets the validity period (default: 90 days). |
| `-keyalg <alg>`      | Specifies the key algorithm (e.g., RSA).     |
| `-keysize <size>`    | Sets the key size (e.g., 2048).              |

---

## **3. Tips**
- **Default Keystore**: If no keystore is specified, `keytool` uses `$HOME/.keystore`.
- **Passwords**: Always protect keystores and keys with strong passwords.
- **Backup**: Always back up your keystore file.
