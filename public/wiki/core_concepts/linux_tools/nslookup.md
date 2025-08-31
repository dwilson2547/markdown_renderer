Here’s a **comprehensive `nslookup` cheat sheet** with common commands and practical examples:

---

### **`nslookup` Cheat Sheet**
`nslookup` is a command-line tool for querying **DNS (Domain Name System)** records to troubleshoot domain and network issues.

---

- [**`nslookup` Cheat Sheet**](#nslookup-cheat-sheet)
- [**1. Basic Syntax**](#1-basic-syntax)
- [**2. Common Options**](#2-common-options)
- [**3. Basic Queries**](#3-basic-queries)
  - [**3.1. Lookup a Domain**](#31-lookup-a-domain)
  - [**3.2. Query a Specific DNS Server**](#32-query-a-specific-dns-server)
  - [**3.3. Reverse DNS Lookup (PTR Record)**](#33-reverse-dns-lookup-ptr-record)
- [**4. Query Specific DNS Record Types**](#4-query-specific-dns-record-types)
  - [**4.1. A Record (IPv4 Address)**](#41-a-record-ipv4-address)
  - [**4.2. AAAA Record (IPv6 Address)**](#42-aaaa-record-ipv6-address)
  - [**4.3. MX Record (Mail Server)**](#43-mx-record-mail-server)
  - [**4.4. TXT Record**](#44-txt-record)
  - [**4.5. CNAME Record (Alias)**](#45-cname-record-alias)
  - [**4.6. NS Record (Name Servers)**](#46-ns-record-name-servers)
  - [**4.7. SOA Record (Start of Authority)**](#47-soa-record-start-of-authority)
- [**5. Interactive Mode**](#5-interactive-mode)
- [**6. Debug Mode**](#6-debug-mode)
- [**7. Common Use Cases**](#7-common-use-cases)
- [**8. Practical Examples**](#8-practical-examples)
  - [**8.1. Check DNS Propagation**](#81-check-dns-propagation)
  - [**8.2. Verify SPF Records**](#82-verify-spf-records)
  - [**8.3. Troubleshoot Email Delivery**](#83-troubleshoot-email-delivery)
  - [**8.4. Find Authoritative Name Servers**](#84-find-authoritative-name-servers)
  - [**8.5. Check for DNS Spoofing**](#85-check-for-dns-spoofing)
- [**9. Tips and Tricks**](#9-tips-and-tricks)
- [**10. Comparison with `dig`**](#10-comparison-with-dig)


### **1. Basic Syntax**
```bash
nslookup [options] [domain] [dns-server]
```

---

### **2. Common Options**

| Option | Description                          |
|--------|--------------------------------------|
| `-type=X` | Query specific DNS record type (e.g., `A`, `MX`, `TXT`). |
| `-debug`  | Enable debug mode for detailed output. |
| `-vc`     | Disable search list (use only the specified DNS server). |

---

### **3. Basic Queries**

#### **3.1. Lookup a Domain**
```bash
nslookup example.com
```
**Example**:
```bash
nslookup google.com
```
- Returns the **A record** (IPv4 address) for `google.com`.

---

#### **3.2. Query a Specific DNS Server**
```bash
nslookup example.com 8.8.8.8
```
**Example**:
```bash
nslookup github.com 1.1.1.1
```
- Queries `github.com` using Cloudflare’s DNS server (`1.1.1.1`).

---

#### **3.3. Reverse DNS Lookup (PTR Record)**
```bash
nslookup 8.8.8.8
```
**Example**:
```bash
nslookup 142.250.190.46
```
- Returns the domain name associated with the IP `142.250.190.46`.

---

### **4. Query Specific DNS Record Types**

#### **4.1. A Record (IPv4 Address)**
```bash
nslookup -type=A example.com
```
**Example**:
```bash
nslookup -type=A github.com
```
- Returns the IPv4 address for `github.com`.

---

#### **4.2. AAAA Record (IPv6 Address)**
```bash
nslookup -type=AAAA example.com
```
**Example**:
```bash
nslookup -type=AAAA google.com
```
- Returns the IPv6 address for `google.com`.

---

#### **4.3. MX Record (Mail Server)**
```bash
nslookup -type=MX example.com
```
**Example**:
```bash
nslookup -type=MX gmail.com
```
- Returns the mail servers for `gmail.com`.

---

#### **4.4. TXT Record**
```bash
nslookup -type=TXT example.com
```
**Example**:
```bash
nslookup -type=TXT google.com
```
- Returns TXT records (e.g., SPF, DKIM) for `google.com`.

---

#### **4.5. CNAME Record (Alias)**
```bash
nslookup -type=CNAME www.example.com
```
**Example**:
```bash
nslookup -type=CNAME www.github.com
```
- Returns the canonical name (alias) for `www.github.com`.

---

#### **4.6. NS Record (Name Servers)**
```bash
nslookup -type=NS example.com
```
**Example**:
```bash
nslookup -type=NS google.com
```
- Returns the authoritative name servers for `google.com`.

---

#### **4.7. SOA Record (Start of Authority)**
```bash
nslookup -type=SOA example.com
```
**Example**:
```bash
nslookup -type=SOA example.com
```
- Returns the SOA record, which contains administrative information about the domain.

---

### **5. Interactive Mode**
Start `nslookup` in interactive mode for multiple queries:
```bash
nslookup
```
**Example Session**:
```bash
> set type=MX
> gmail.com
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
gmail.com       mail exchanger = 5 gmail-smtp-in.l.google.com.
gmail.com       mail exchanger = 10 alt1.gmail-smtp-in.l.google.com.
...
> exit
```

---

### **6. Debug Mode**
Enable debug mode for detailed output:
```bash
nslookup -debug example.com
```
**Example**:
```bash
nslookup -debug google.com
```
- Shows the step-by-step DNS resolution process.

---

### **7. Common Use Cases**

| Task                                      | Command                                      |
|-------------------------------------------|----------------------------------------------|
| Lookup a domain’s IP                     | `nslookup example.com`                       |
| Query a specific DNS server              | `nslookup example.com 8.8.8.8`              |
| Reverse DNS lookup                       | `nslookup 8.8.8.8`                           |
| Query MX records                          | `nslookup -type=MX example.com`              |
| Query TXT records                         | `nslookup -type=TXT example.com`             |
| Query CNAME records                       | `nslookup -type=CNAME www.example.com`       |
| Query NS records                          | `nslookup -type=NS example.com`              |
| Query SOA records                         | `nslookup -type=SOA example.com`             |
| Interactive mode                          | `nslookup`                                   |
| Debug mode                                | `nslookup -debug example.com`               |

---

### **8. Practical Examples**

#### **8.1. Check DNS Propagation**
```bash
nslookup example.com 8.8.8.8
nslookup example.com 1.1.1.1
```
- Queries multiple DNS servers to verify DNS propagation.

---

#### **8.2. Verify SPF Records**
```bash
nslookup -type=TXT example.com | grep "v=spf1"
```
- Checks the SPF record for `example.com`.

---

#### **8.3. Troubleshoot Email Delivery**
```bash
nslookup -type=MX gmail.com
```
- Verifies the mail servers for `gmail.com`.

---

#### **8.4. Find Authoritative Name Servers**
```bash
nslookup -type=NS example.com
```
- Lists the authoritative name servers for `example.com`.

---

#### **8.5. Check for DNS Spoofing**
```bash
nslookup example.com
nslookup example.com 8.8.8.8
nslookup example.com 1.1.1.1
```
- Compares results from different DNS servers to detect inconsistencies.

---

### **9. Tips and Tricks**
- **Use `dig` for Advanced Queries**: While `nslookup` is user-friendly, `dig` provides more detailed and flexible DNS queries.
  ```bash
  dig example.com MX
  ```
- **Check Local DNS Cache**: Use `ipconfig /flushdns` (Windows) or `sudo systemd-resolve --flush-caches` (Linux) to clear the DNS cache if results seem stale.
- **Query Specific DNS Servers**: Use public DNS servers like `8.8.8.8` (Google) or `1.1.1.1` (Cloudflare) to bypass local DNS issues.
- **Scripting**: Combine `nslookup` with shell scripting for automated DNS checks:
  ```bash
  for domain in google.com github.com example.com; do
    nslookup $domain
  done
  ```

---

### **10. Comparison with `dig`**
| Feature               | `nslookup`                          | `dig`                                |
|-----------------------|-------------------------------------|--------------------------------------|
| **Ease of Use**       | User-friendly, interactive mode     | More complex, detailed output        |
| **Output Format**     | Simple, human-readable              | Verbose, structured                 |
| **Query Types**       | Supports basic types                | Supports all DNS record types        |
| **Debugging**         | Limited (`-debug`)                  | Advanced (`+trace`, `+stats`)        |
| **Scripting**         | Less flexible                       | Highly flexible                      |

**Example with `dig`**:
```bash
dig example.com MX
```

---