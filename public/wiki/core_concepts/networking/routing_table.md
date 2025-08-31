## Routing Table

- [Routing Table](#routing-table)
- [**1. What is a Routing Table?**](#1-what-is-a-routing-table)
- [**2. Components of a Routing Table Entry**](#2-components-of-a-routing-table-entry)
- [**3. How Routing Tables Are Generated**](#3-how-routing-tables-are-generated)
  - [**3.1. Directly Connected Networks**](#31-directly-connected-networks)
  - [**3.2. Static Routes**](#32-static-routes)
  - [**3.3. Dynamic Routes**](#33-dynamic-routes)
    - [**3.3.1. Routing Protocols**](#331-routing-protocols)
    - [**3.3.2. How Dynamic Routes Are Learned**](#332-how-dynamic-routes-are-learned)
    - [**3.3.3. Example: OSPF Route Learning**](#333-example-ospf-route-learning)
  - [**3.4. Default Route**](#34-default-route)
- [**4. Routing Table Generation: Step-by-Step**](#4-routing-table-generation-step-by-step)
  - [**4.1. Router Boot-Up**](#41-router-boot-up)
  - [**4.2. Example: Building a Routing Table**](#42-example-building-a-routing-table)
    - [**Network Topology**](#network-topology)
    - [**Routing Table for Router A (OSPF)**](#routing-table-for-router-a-ospf)
- [**5. How Routing Tables Are Used**](#5-how-routing-tables-are-used)
- [**6. Routing Table Examples**](#6-routing-table-examples)
  - [**6.1. Linux Routing Table**](#61-linux-routing-table)
  - [**6.2. Cisco Router Routing Table**](#62-cisco-router-routing-table)
- [**7. Dynamic Routing Protocols in Depth**](#7-dynamic-routing-protocols-in-depth)
  - [**7.1. OSPF (Open Shortest Path First)**](#71-ospf-open-shortest-path-first)
  - [**7.2. RIP (Routing Information Protocol)**](#72-rip-routing-information-protocol)
  - [**7.3. BGP (Border Gateway Protocol)**](#73-bgp-border-gateway-protocol)
- [**8. Advanced Routing Table Concepts**](#8-advanced-routing-table-concepts)
  - [**8.1. Administrative Distance**](#81-administrative-distance)
  - [**8.2. Route Redistribution**](#82-route-redistribution)
  - [**8.3. Policy-Based Routing**](#83-policy-based-routing)
- [**9. Routing Table Maintenance**](#9-routing-table-maintenance)
- [**10. Practical Example: Tracing a Packet**](#10-practical-example-tracing-a-packet)
  - [**Scenario**](#scenario)
- [**11. Tools to Inspect Routing Tables**](#11-tools-to-inspect-routing-tables)
- [**12. Summary: How Routing Tables Are Built**](#12-summary-how-routing-tables-are-built)


## **1. What is a Routing Table?**
A routing table is a **database** stored in a router or networked device that lists:
- **Destination networks** (where packets need to go).
- **Next hops** (the next device to forward the packet to).
- **Interfaces** (which physical or logical interface to use).
- **Metrics** (cost or priority of the route).
- **Route types** (directly connected, static, or dynamically learned).

---

## **2. Components of a Routing Table Entry**
Each entry in a routing table typically includes:



| Field               | Description                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------|
| **Destination Network** | The IP address of the destination network (e.g., `192.168.1.0/24`).                          |
| **Subnet Mask**     | Defines the network portion of the destination (e.g., `255.255.255.0` or `/24`).              |
| **Next Hop**         | The IP address of the next router or gateway (e.g., `10.0.0.1`).                               |
| **Interface**        | The outgoing interface (e.g., `eth0`, `GigabitEthernet0/1`).                                  |
| **Metric**           | The cost or priority of the route (e.g., `10` for OSPF, `1` for directly connected networks). |
| **Route Type**       | How the route was learned (e.g., connected, static, OSPF, BGP, RIP).                          |

---

## **3. How Routing Tables Are Generated**

### **3.1. Directly Connected Networks**
- **Definition**: Routes to networks that are **directly connected** to the router’s interfaces.
- **How It’s Added**:
  - When an interface is configured with an IP address and subnet mask, the router automatically adds a **directly connected route** to its routing table.
  - Example: If `eth0` is configured with `192.168.1.1/24`, the router adds a route for `192.168.1.0/24` via `eth0`.
- **Example Entry**:
  ```
  Destination: 192.168.1.0/24
  Next Hop: 0.0.0.0 (directly connected)
  Interface: eth0
  ```

---

### **3.2. Static Routes**
- **Definition**: Routes that are **manually configured** by a network administrator.
- **How It’s Added**:
  - Administrators use commands like `ip route` (Linux) or `route add` (Windows) to add static routes.
  - Example (Linux):
    ```bash
    ip route add 10.0.0.0/24 via 192.168.1.2 dev eth0
    ```
    This adds a route to `10.0.0.0/24` via the next hop `192.168.1.2` using interface `eth0`.
- **Use Cases**:
  - Small networks.
  - Routes to specific networks that don’t change often.
  - Backup routes.
- **Example Entry**:
  ```
  Destination: 10.0.0.0/24
  Next Hop: 192.168.1.2
  Interface: eth0
  ```

---

### **3.3. Dynamic Routes**
Dynamic routes are **automatically learned** and updated using **routing protocols**. These protocols allow routers to exchange routing information and adapt to network changes (e.g., link failures).

#### **3.3.1. Routing Protocols**
- **Interior Gateway Protocols (IGPs)**:
  - Used within a single **autonomous system (AS)**.
  - Examples: **OSPF (Open Shortest Path First)**, **RIP (Routing Information Protocol)**, **EIGRP (Enhanced Interior Gateway Routing Protocol)**.
- **Exterior Gateway Protocols (EGPs)**:
  - Used between different autonomous systems.
  - Example: **BGP (Border Gateway Protocol)**.

---

#### **3.3.2. How Dynamic Routes Are Learned**
1. **Neighbor Discovery**:
   - Routers using the same routing protocol discover each other by exchanging **hello packets**.
   - Example: OSPF routers send hello packets every 10 seconds to establish adjacencies.

2. **Link-State or Distance-Vector Updates**:
   - **Link-State Protocols (e.g., OSPF)**:
     - Routers exchange **Link-State Advertisements (LSAs)** to build a complete map of the network (topology database).
     - Each router runs the **Dijkstra algorithm** to calculate the shortest path to every network.
   - **Distance-Vector Protocols (e.g., RIP)**:
     - Routers share their **entire routing table** with neighbors.
     - Each router updates its table based on the **distance (hop count)** to each network.

3. **Best Path Selection**:
   - Routers use metrics like **hop count (RIP)**, **bandwidth (OSPF)**, or **path attributes (BGP)** to determine the best path.
   - Example: OSPF prefers paths with the lowest **cost** (inversely proportional to bandwidth).

4. **Routing Table Update**:
   - The best paths are added to the routing table.
   - Example OSPF entry:
     ```
     Destination: 172.16.0.0/16
     Next Hop: 192.168.2.2
     Interface: eth1
     Metric: 10
     ```

---

#### **3.3.3. Example: OSPF Route Learning**
1. **Router A** and **Router B** establish an OSPF adjacency.
2. **Router B** sends an LSA advertising network `172.16.0.0/16` with a cost of `10`.
3. **Router A** receives the LSA, runs Dijkstra’s algorithm, and adds the route to its routing table:
   ```
   Destination: 172.16.0.0/16
   Next Hop: 192.168.2.2 (Router B)
   Interface: eth1
   Metric: 10
   ```

---

### **3.4. Default Route**
- **Definition**: A route used when no other route matches the destination. Typically points to the **gateway of last resort** (e.g., ISP’s router).
- **How It’s Added**:
  - Manually configured as a static route:
    ```bash
    ip route add default via 192.168.1.1
    ```
  - Or learned dynamically (e.g., via DHCP or BGP).
- **Example Entry**:
  ```
  Destination: 0.0.0.0/0
  Next Hop: 192.168.1.1
  Interface: eth0
  ```

---

## **4. Routing Table Generation: Step-by-Step**

### **4.1. Router Boot-Up**
1. **Initialize Interfaces**:
   - The router loads configurations for its interfaces (e.g., `eth0`, `eth1`).
   - Directly connected routes are added to the routing table.
2. **Load Static Routes**:
   - Manually configured static routes are added.
3. **Establish Routing Protocol Adjacencies**:
   - The router sends hello packets to discover neighbors (e.g., OSPF or EIGRP neighbors).
4. **Exchange Routing Information**:
   - The router exchanges LSAs (OSPF) or routing tables (RIP) with neighbors.
5. **Run Path Selection Algorithms**:
   - The router calculates the best paths using Dijkstra (OSPF) or Bellman-Ford (RIP).
6. **Update Routing Table**:
   - Best paths are added to the routing table.
7. **Forward Packets**:
   - The router uses the routing table to forward incoming packets.

---

### **4.2. Example: Building a Routing Table**
#### **Network Topology**
```
[Router A] ---- [Router B] ---- [Router C]
   eth0: 192.168.1.1/24    eth0: 192.168.1.2/24
   eth1: 10.0.0.1/24       eth1: 10.0.0.2/24       eth0: 172.16.0.1/16
```
- **Router A** is connected to `192.168.1.0/24` and `10.0.0.0/24`.
- **Router B** is connected to `192.168.1.0/24`, `10.0.0.0/24`, and `172.16.0.0/16` (via Router C).
- **Router C** is connected to `172.16.0.0/16`.

#### **Routing Table for Router A (OSPF)**
1. **Directly Connected Routes**:
   ```
   192.168.1.0/24 via eth0
   10.0.0.0/24 via eth1
   ```
2. **OSPF Learned Route**:
   - Router B advertises `172.16.0.0/16` with a cost of `10`.
   - Router A adds:
     ```
     172.16.0.0/16 via 10.0.0.2 (Router B), eth1, cost 10
     ```

---

## **5. How Routing Tables Are Used**
When a router receives a packet:
1. **Extract Destination IP**: The router looks at the destination IP in the packet header.
2. **Longest Prefix Match**: The router searches its routing table for the **most specific match** (longest subnet mask) for the destination IP.
   - Example: A packet to `172.16.5.10` matches `172.16.0.0/16` in the routing table.
3. **Forward the Packet**:
   - If a match is found, the packet is forwarded to the **next hop** via the specified **interface**.
   - If no match is found, the packet is forwarded using the **default route** (if one exists).
   - If no default route exists, the packet is **dropped**.

---

## **6. Routing Table Examples**

### **6.1. Linux Routing Table**
View the routing table using:
```bash
ip route show
```
or
```bash
route -n
```
**Example Output**:
```
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    100    0        0 eth0
10.0.0.0        0.0.0.0         255.255.255.0   U     0      0        0 eth1
192.168.1.0     0.0.0.0         255.255.255.0   U     0      0        0 eth0
172.16.0.0      10.0.0.2        255.255.0.0     UG    10     0        0 eth1
```
- **`0.0.0.0`**: Default route via `192.168.1.1`.
- **`10.0.0.0/24`**: Directly connected via `eth1`.
- **`172.16.0.0/16`**: Learned via OSPF, next hop `10.0.0.2`.

---

### **6.2. Cisco Router Routing Table**
View the routing table using:
```bash
show ip route
```
**Example Output**:
```
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2

Gateway of last resort is 192.168.1.1 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 192.168.1.1
      10.0.0.0/24 is subnetted, 1 subnets
C        10.0.0.0 is directly connected, Ethernet1
C     192.168.1.0/24 is directly connected, Ethernet0
O     172.16.0.0/16 [110/10] via 10.0.0.2, 00:00:10, Ethernet1
```
- **`S*`**: Static default route via `192.168.1.1`.
- **`C`**: Directly connected routes.
- **`O`**: OSPF-learned route for `172.16.0.0/16`.

---

## **7. Dynamic Routing Protocols in Depth**

### **7.1. OSPF (Open Shortest Path First)**
- **Type**: Link-state protocol.
- **How It Works**:
  1. Routers exchange **LSAs** to build a **topology database**.
  2. Each router runs the **Dijkstra algorithm** to calculate the shortest path to every network.
  3. Routes are added to the routing table based on the lowest **cost** (e.g., `cost = 100Mbps / bandwidth`).
- **Example Metric**:
  - `10.0.0.0/24` via `eth1`, cost `10`.

---

### **7.2. RIP (Routing Information Protocol)**
- **Type**: Distance-vector protocol.
- **How It Works**:
  1. Routers share their **entire routing table** with neighbors every 30 seconds.
  2. Routes are selected based on the lowest **hop count** (maximum 15 hops).
  3. If a route’s hop count exceeds 15, it is considered unreachable.
- **Example Metric**:
  - `172.16.0.0/16` via `10.0.0.2`, hop count `2`.

---

### **7.3. BGP (Border Gateway Protocol)**
- **Type**: Path-vector protocol (used between autonomous systems).
- **How It Works**:
  1. Routers exchange **path attributes** (e.g., AS path, next hop) to determine the best route.
  2. BGP uses policies (e.g., prefer shorter AS paths) to select routes.
  3. BGP does not use traditional metrics like cost or hop count.
- **Example Route**:
  - `203.0.113.0/24` via `198.51.100.2`, AS path `65001 65002`.

---

## **8. Advanced Routing Table Concepts**

### **8.1. Administrative Distance**
- **Definition**: A measure of trustworthiness for routes from different sources.
- **Purpose**: If multiple routes exist for the same destination, the route with the **lowest administrative distance** is preferred.
- **Example Values**:
  - Directly connected: `0`
  - Static route: `1`
  - EIGRP: `90`
  - OSPF: `110`
  - RIP: `120`
  - BGP: `20` (external), `200` (internal)

---

### **8.2. Route Redistribution**
- **Definition**: The process of sharing routes between different routing protocols.
- **Example**: Redistributing OSPF routes into BGP:
  ```bash
  router bgp 65001
  redistribute ospf 1
  ```
- **Use Case**: Connecting an OSPF network to the internet via BGP.

---

### **8.3. Policy-Based Routing**
- **Definition**: Routing decisions based on **policies** (e.g., source IP, protocol) rather than just destination IP.
- **Example**: Route traffic from `192.168.1.0/24` via `ISP1` and traffic from `10.0.0.0/24` via `ISP2`.
- **Configuration (Linux)**:
  ```bash
  ip rule add from 192.168.1.0/24 lookup 100
  ip route add default via 198.51.100.1 dev eth0 table 100
  ```

---

## **9. Routing Table Maintenance**
- **Aging Out Routes**: Dynamic routes are removed if not refreshed (e.g., RIP routes time out after 180 seconds).
- **Link Failures**: If a link fails, routing protocols recalculate paths and update the routing table.
- **Manual Updates**: Administrators can manually add, remove, or modify routes.

---

## **10. Practical Example: Tracing a Packet**
### **Scenario**
- Your device (`192.168.1.10`) sends a packet to `203.0.113.5`.
- **Routing Table on Your Router**:
  ```
  0.0.0.0/0 via 198.51.100.1 (ISP)
  192.168.1.0/24 via eth0
  ```
- **Steps**:
  1. Your device sends the packet to the router (`192.168.1.1`).
  2. The router matches `203.0.113.5` to the default route (`0.0.0.0/0`).
  3. The router forwards the packet to `198.51.100.1` (ISP’s gateway).
  4. The ISP routes the packet toward `203.0.113.5` using BGP.

---

## **11. Tools to Inspect Routing Tables**
- **Linux/macOS**:
  ```bash
  ip route
  netstat -rn
  traceroute 203.0.113.5
  ```
- **Windows**:
  ```bash
  route print
  tracert 203.0.113.5
  ```
- **Cisco IOS**:
  ```bash
  show ip route
  show ip ospf database
  ```

---

## **12. Summary: How Routing Tables Are Built**
1. **Directly Connected Routes**: Added automatically for local interfaces.
2. **Static Routes**: Manually configured by administrators.
3. **Dynamic Routes**: Learned via routing protocols (OSPF, RIP, BGP).
4. **Default Route**: Used for destinations with no specific match.
5. **Best Path Selection**: Based on metrics, administrative distance, and policies.
6. **Forwarding**: Packets are forwarded using the longest prefix match.

---