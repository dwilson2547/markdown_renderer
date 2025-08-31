# OSI Model: The 7-Layer Networking Framework

<custom-element data-json="%7B%22type%22%3A%22table-metadata%22%2C%22attributes%22%3A%7B%22title%22%3A%22OSI%20Model%20Layers%22%7D%7D" />

- [OSI Model: The 7-Layer Networking Framework](#osi-model-the-7-layer-networking-framework)
  - [**1. Overview**](#1-overview)
  - [**2. Layer Breakdown**](#2-layer-breakdown)
    - [**Layer 7: Application**](#layer-7-application)
    - [**Layer 6: Presentation**](#layer-6-presentation)
    - [**Layer 5: Session**](#layer-5-session)
    - [**Layer 4: Transport**](#layer-4-transport)
    - [**Layer 3: Network**](#layer-3-network)
    - [**Layer 2: Data Link**](#layer-2-data-link)
    - [**Layer 1: Physical**](#layer-1-physical)
  - [**3. Why the OSI Model Matters**](#3-why-the-osi-model-matters)
  - [**4. OSI Model vs. TCP/IP Model**](#4-osi-model-vs-tcpip-model)
  - [**5. Common Misconceptions**](#5-common-misconceptions)
  - [**6. Further Reading**](#6-further-reading)


| Layer Number | Layer Name         | Key Function                                                                 | Protocols/Examples                                                                 |
|--------------|--------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| 7            | **Application**    | User interfaces, network services, and application support                  | [HTTP](http.md), [FTP](ftp.md), [SMTP](smtp.md), [DNS](dns.md), [SSH](../linux_general/ssh.md)                                                         |
| 6            | **Presentation**   | Data translation, encryption, compression, and formatting                  | [SSL/TLS](ssl_tls.md), JPEG, MPEG, ASCII                                                       |
| 5            | **Session**        | Manages sessions/connections between applications                            | NetBIOS, RPC, SIP, PPTP                                                           |
| 4            | **Transport**      | End-to-end communication, data segmentation, and error recovery             | TCP, UDP, SCTP, DCCP                                                              |
| 3            | **Network**        | Logical addressing, routing, and path determination                          | IP, ICMP, OSPF, BGP, IPsec                                                        |
| 2            | **Data Link**      | Framing, physical addressing (MAC), and error detection                      | Ethernet, PPP, Wi-Fi (802.11), VLAN, [MAC addresses](mac_addresses.md)                               |
| 1            | **Physical**       | Transmission of raw bit streams over physical media                         | Ethernet cables, fiber optics, Wi-Fi radio waves, USB, Bluetooth                 |

---

## **1. Overview**
The **Open Systems Interconnection (OSI) model** is a conceptual framework used to standardize network communication. It divides networking into **7 layers**, each with specific functions, to ensure interoperability and modular design.

---

## **2. Layer Breakdown**

### **Layer 7: Application**
- **Purpose**: Provides network services directly to end-users or applications.
- **Examples**: Web browsing ([HTTP](http.md)), email ([SMTP](smtp.md)), file transfer ([FTP](ftp.md)).
- **Key Concept**: User interaction with the network.

### **Layer 6: Presentation**
- **Purpose**: Translates, encrypts, and compresses data for the application layer.
- **Examples**: [SSL/TLS](ssl_tls.md) for encryption, JPEG/MPEG for multimedia.
- **Key Concept**: Data formatting and security.

### **Layer 5: Session**
- **Purpose**: Manages sessions between applications (e.g., setup, maintenance, teardown).
- **Examples**: NetBIOS for file sharing, SIP for VoIP.
- **Key Concept**: Session control and synchronization.

### **Layer 4: Transport**
- **Purpose**: Ensures end-to-end communication, including error recovery and flow control.
- **Examples**: TCP (reliable), UDP (fast, connectionless).
- **Key Concept**: Data segmentation and reassembly.

### **Layer 3: Network**
- **Purpose**: Handles logical addressing (IP) and routing between networks.
- **Examples**: IP, [routers](routers.md), [ICMP](icmp.md) (ping).
- **Key Concept**: Path determination and forwarding.

### **Layer 2: Data Link**
- **Purpose**: Manages physical addressing (MAC) and framing for local network communication.
- **Examples**: Ethernet, [switches](switches_and_hubs.md), Wi-Fi.
- **Key Concept**: Framing and error detection (e.g., CRC).

### **Layer 1: Physical**
- **Purpose**: Transmits raw bit streams over physical media.
- **Examples**: Cables (Ethernet, fiber), radio waves (Wi-Fi), USB.
- **Key Concept**: Signal transmission and hardware.

---

## **3. Why the OSI Model Matters**
- **Standardization**: Ensures compatibility between different vendors' hardware/software.
- **Troubleshooting**: Isolates issues to specific layers (e.g., a "physical" layer issue vs. an "application" layer issue).
- **Modularity**: Allows updates to one layer without affecting others.

---

## **4. OSI Model vs. TCP/IP Model**
| Feature          | OSI Model               | TCP/IP Model          |
|------------------|-------------------------|-----------------------|
| **Layers**       | 7                       | 4                     |
| **Flexibility**  | Theoretical, generic    | Practical, simplified |
| **Usage**        | Educational, reference  | Real-world networks   |

---

## **5. Common Misconceptions**
- **Myth**: The OSI model is used directly in real networks.
  **Reality**: The **TCP/IP model** is more widely implemented, but OSI is a critical reference.
- **Myth**: All layers are equally important in practice.
  **Reality**: Layers 1-4 are most critical for networking; layers 5-7 are often abstracted in modern applications.

---

## **6. Further Reading**
- [IETF RFCs](https://www.ietf.org/rfc.html) (TCP/IP standards)
- [OSI Model on Wikipedia](https://en.wikipedia.org/wiki/OSI_model)
- [Cisco Networking Academy](https://www.netacad.com/)
