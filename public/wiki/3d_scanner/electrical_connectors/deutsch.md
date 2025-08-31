# Deutsch Connectors

Deutsch connectors are a family of rugged electrical connectors designed for harsh automotive, marine, and industrial environments. Originally developed by Deutsch (now part of TE Connectivity), these connectors are known for their reliability, weatherproof sealing, and resistance to vibration, corrosion, and extreme temperatures.

## Overview

Deutsch connectors feature:
- Sealed design with environmental protection (IP67/IP68 ratings)
- Positive locking mechanisms
- Color-coded housings for easy identification
- Wide temperature range operation (-55°C to +125°C)
- Vibration and shock resistance
- Multiple contact arrangements

## Connector Series

### DT Series (Deutsch Truck)
The most common series, widely used in automotive and heavy-duty applications.

### DTM Series (Deutsch Truck Miniature)
Compact version of the DT series for space-constrained applications.

### DTP Series (Deutsch Truck Panel Mount)
Panel-mount versions with threaded coupling nuts.

### DTHD Series (Deutsch Truck Heavy Duty)
High-current applications with larger contact sizes.

## Connector Specifications Chart

| Series | Shell Size | Pin Count | Pin Arrangement | Wire Gauge Range | Current Rating | Housing Color |
|--------|------------|-----------|-----------------|------------------|----------------|---------------|
| **DT Series** |
| DT04-2P | 04 | 2 | 2-pin | 20-12 AWG | 13A per pin | Black |
| DT04-3P | 04 | 3 | 3-pin | 20-12 AWG | 13A per pin | Black |
| DT04-4P | 04 | 4 | 4-pin | 20-12 AWG | 13A per pin | Black |
| DT04-6P | 04 | 6 | 6-pin | 20-12 AWG | 13A per pin | Black |
| DT04-8P | 04 | 8 | 8-pin | 20-12 AWG | 13A per pin | Black |
| DT04-12P | 04 | 12 | 12-pin | 20-12 AWG | 13A per pin | Black |
| DT06-2S | 06 | 2 | 2-socket | 20-12 AWG | 13A per pin | Gray |
| DT06-3S | 06 | 3 | 3-socket | 20-12 AWG | 13A per pin | Gray |
| DT06-4S | 06 | 4 | 4-socket | 20-12 AWG | 13A per pin | Gray |
| DT06-6S | 06 | 6 | 6-socket | 20-12 AWG | 13A per pin | Gray |
| DT06-8S | 06 | 8 | 8-socket | 20-12 AWG | 13A per pin | Gray |
| DT06-12S | 06 | 12 | 12-socket | 20-12 AWG | 13A per pin | Gray |
| **DTM Series** |
| DTM04-2P | 04 | 2 | 2-pin | 22-16 AWG | 7.5A per pin | Black |
| DTM04-3P | 04 | 3 | 3-pin | 22-16 AWG | 7.5A per pin | Black |
| DTM04-4P | 04 | 4 | 4-pin | 22-16 AWG | 7.5A per pin | Black |
| DTM04-6P | 04 | 6 | 6-pin | 22-16 AWG | 7.5A per pin | Black |
| DTM04-8P | 04 | 8 | 8-pin | 22-16 AWG | 7.5A per pin | Black |
| DTM04-12P | 04 | 12 | 12-pin | 22-16 AWG | 7.5A per pin | Black |
| DTM06-2S | 06 | 2 | 2-socket | 22-16 AWG | 7.5A per pin | Gray |
| DTM06-3S | 06 | 3 | 3-socket | 22-16 AWG | 7.5A per pin | Gray |
| DTM06-4S | 06 | 4 | 4-socket | 22-16 AWG | 7.5A per pin | Gray |
| DTM06-6S | 06 | 6 | 6-socket | 22-16 AWG | 7.5A per pin | Gray |
| DTM06-8S | 06 | 8 | 8-socket | 22-16 AWG | 7.5A per pin | Gray |
| DTM06-12S | 06 | 12 | 12-socket | 22-16 AWG | 7.5A per pin | Gray |
| **DTHD Series** |
| DTHD04-4P | 04 | 4 | 4-pin | 14-10 AWG | 25A per pin | Black |
| DTHD04-6P | 04 | 6 | 6-pin | 14-10 AWG | 25A per pin | Black |
| DTHD06-4S | 06 | 4 | 4-socket | 14-10 AWG | 25A per pin | Gray |
| DTHD06-6S | 06 | 6 | 6-socket | 14-10 AWG | 25A per pin | Gray |

## Pin Layout Diagrams

### 2-Pin Configuration
```
 1   2
 o   o
```

### 3-Pin Configuration
```
   1
   o
2  o  o 3
```

### 4-Pin Configuration
```
1 o   o 2
   \ /
    X
   / \
4 o   o 3
```

### 6-Pin Configuration
```
  1 o   o 2
     \ /
3 o   X   o 6
     / \
  4 o   o 5
```

### 8-Pin Configuration
```
1 o       o 2
   o     o
3    o o    6
   o     o
4 o       o 5
     8 7
```

### 12-Pin Configuration
```
    1 o   o 2
  12 o o o o 3
       | |
  11 o | | o 4
       | |
  10 o o o o 5
    9 o   o 6
        8 7
```

## Part Number Nomenclature

Deutsch connector part numbers follow a specific format:

**DT[M][HD]SS-NNX[-YYYY]**

- **DT**: Deutsch Truck series identifier
- **M**: (Optional) Miniature version
- **HD**: (Optional) Heavy Duty version  
- **SS**: Shell size (04, 06, etc.)
- **NN**: Number of positions
- **X**: P = Pin/Plug, S = Socket/Receptacle
- **YYYY**: (Optional) Additional specifications

### Examples:
- `DT04-4P` = DT series, size 04, 4-pin plug
- `DT06-6S` = DT series, size 06, 6-socket receptacle
- `DTM04-2P` = DTM series, size 04, 2-pin plug

## Contact Types and Sizes

| Contact Size | Wire Gauge | Current Rating | Contact Material |
|--------------|------------|----------------|------------------|
| Size 16 | 20-16 AWG | 13A | Gold-plated copper alloy |
| Size 12 | 16-12 AWG | 25A | Gold-plated copper alloy |
| Size 16 (DTM) | 22-16 AWG | 7.5A | Gold-plated copper alloy |

## Installation Notes

### Crimping
- Use proper Deutsch crimping tools (e.g., HDT-48-00, M22520/5-01)
- Follow manufacturer's crimp specifications
- Inspect crimps for proper formation and retention

### Assembly
1. Insert crimped contacts into connector housing
2. Ensure contacts are fully seated and locked
3. Apply dielectric grease to mating surfaces
4. Install wedge or position assurance device
5. Mate connectors with firm, straight motion
6. Verify positive lock engagement

### Environmental Sealing
- IP67 rating when properly mated
- Use appropriate cable seals and grommets
- Apply dielectric grease for corrosion protection
- Ensure proper strain relief on cables

## Applications

### Automotive
- Engine management systems
- Lighting circuits
- Transmission controls
- ABS/traction control
- HVAC systems

### Marine
- Navigation equipment
- Bilge pump controls
- Engine instrumentation
- Lighting systems

### Industrial
- Heavy machinery
- Agricultural equipment
- Construction vehicles
- Mining equipment
- Rail applications

## Related Standards

- SAE J1128: Low Voltage Primary Cable
- SAE J1939: Heavy Duty Vehicle Network
- IEC 60529: IP Rating classifications
- ISO 8092: Road vehicles - Connectors

## Maintenance

### Inspection
- Check for corrosion, damage, or contamination
- Verify proper contact retention
- Test continuity and resistance
- Inspect cable strain relief

### Cleaning
- Use isopropyl alcohol for cleaning contacts
- Apply fresh dielectric grease after cleaning
- Replace seals if damaged or deteriorated

### Storage
- Store in original packaging when possible
- Keep in dry, temperature-controlled environment
- Protect contacts from contamination