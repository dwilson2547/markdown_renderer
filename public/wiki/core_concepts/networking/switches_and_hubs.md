### **Network Switching vs. Hubs: Key Differences**

---

- [**Network Switching vs. Hubs: Key Differences**](#network-switching-vs-hubs-key-differences)
  - [**1. What is a Network Switch?**](#1-what-is-a-network-switch)
  - [**2. How Switches Work**](#2-how-switches-work)
  - [**3. What is a Network Hub?**](#3-what-is-a-network-hub)
  - [**4. Key Differences Between Switches and Hubs**](#4-key-differences-between-switches-and-hubs)
  - [**5. Why Switches Replaced Hubs**](#5-why-switches-replaced-hubs)
  - [**6. Practical Example**](#6-practical-example)
  - [**7. Modern Use Cases**](#7-modern-use-cases)
  - [**8. Types of Switches**](#8-types-of-switches)


#### **1. What is a Network Switch?**
- A **switch** is a **Layer 2 (Data Link Layer)** device that intelligently forwards data between devices in a **Local Area Network (LAN)**.
- It uses **MAC addresses** to determine where to send data, ensuring efficient and secure communication.

---

#### **2. How Switches Work**
- **MAC Address Learning**: Switches build a **MAC address table** by learning which devices are connected to which ports.
- **Frame Forwarding**: When a device sends data (e.g., an Ethernet frame), the switch checks the **destination MAC address** and forwards the frame **only to the correct port**.
- **Collision Domains**: Each port on a switch operates in its own **collision domain**, reducing network congestion.
- **Full-Duplex Communication**: Switches allow devices to **send and receive data simultaneously**, improving performance.

---

#### **3. What is a Network Hub?**
- A **hub** is a **Layer 1 (Physical Layer)** device that **broadcasts** all incoming data to **every connected device**.
- It does **not** use MAC addresses or make forwarding decisions.
- All devices connected to a hub share the **same collision domain**, leading to inefficiencies and congestion.

---

#### **4. Key Differences Between Switches and Hubs**



| Feature               | Switch                                      | Hub                                          |
|-----------------------|---------------------------------------------|---------------------------------------------|
| **Layer**             | Operates at **Layer 2 (Data Link)**         | Operates at **Layer 1 (Physical)**          |
| **Forwarding**        | Forwards data **only to the intended port** | **Broadcasts** data to **all ports**       |
| **Collision Domains** | Each port is its own collision domain       | All ports share **one collision domain**   |
| **Performance**       | Faster, more efficient                      | Slower, prone to collisions                |
| **Intelligence**      | Learns MAC addresses                        | No intelligence; just repeats signals      |
| **Duplex Mode**       | Supports **full-duplex** communication      | Only supports **half-duplex**               |
| **Security**          | More secure (data only sent to intended recipient) | Less secure (data broadcasted to all devices) |

---

#### **5. Why Switches Replaced Hubs**
- **Efficiency**: Switches reduce unnecessary traffic by sending data only where it’s needed.
- **Performance**: Switches support **full-duplex** communication, doubling bandwidth.
- **Scalability**: Switches handle more devices without degrading performance.
- **Security**: Switches isolate traffic, reducing the risk of eavesdropping.

---

#### **6. Practical Example**
- **Hub**: If Device A sends data to Device B, **all devices** (C, D, E) receive the data, even if it’s not for them.
- **Switch**: If Device A sends data to Device B, **only Device B** receives it.

---

#### **7. Modern Use Cases**
- **Switches**: Used in **all modern networks** (home, office, data centers).
- **Hubs**: Obsolete in most applications but may still be found in **legacy systems** or simple setups.

---

#### **8. Types of Switches**
- **Unmanaged Switches**: Plug-and-play, no configuration.
- **Managed Switches**: Allow advanced features like **VLANs, QoS, and monitoring**.
- **Smart Switches**: A middle ground with limited management features.

---