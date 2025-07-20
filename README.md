# Proxima

A Eurorack module that measures the distance using a VL53L0X Time-of-Flight sensor and converts it into a Control Voltage (CV) for your modular system.
Control parameters easily with hand movements in the air.

⸻

# Installation
1.	Install CircuitPython on the Pico
2.	Download this repository
3.	"Proxima_R2CV.py" to the Pico
4.  Rename "Proxima_R2CV.py" to "code.py" to start the program automatically after connecting the power supply.
5.	Copy the contents of the circuit_pytho_libs folder into the lib folder on the Pico

____

## Features
•	Distance range: 2 cm to 20 cm

•	CV output: 0 V to 8 V

•	Smooth values using a moving average filter

⸻

## Schematics for:
•	Complete wiring

•	LM358 amplifier circuit

•	Low-pass filter

are located in the schematics/ folder.

⸻

### Estimated Cost
The module can be built from inexpensive components. Approximate prices:

•	Raspberry Pi Pico: 5–6 €

•	LM358 Op-Amp: 0.50 €

•	MCP4725 (12-bit DAC): 3–4 €

•	VL53L0X ToF sensor: 4–5 €

•	Resistors and capacitors: 1-2 €

•	Jumper wires and connectors: 1–2 €

Total: about 15–20 € (depending on supplier and shipping).

# text-based complete scheme

### 1. Pico:
VSYS (Pin 39) to +5v Eurorack

GND (Pin 38) to GND Eurorack

SDA (Pin 6) to SDA from Tof Sensor and DAC

SCL (Pin 7) to SCL from Tof Sensor and DAC

+3.3v (Pin 36) to VCC from Tof Sensor and DAC

### 2. DAC (MCP4725) and Tof Sensor (VL53L0X)
GND from Tof Sensor and DAC to GND (Pin 3)

### 3. low-pass filter
Output from DAC through 10kOhm Resistor to branching point A

branching point A through 100nF Capasitor to GND

branching point A to LM358 (Pin 3)

### 4. Op-Amp (LM358)
LM358 (Pin 4) to GND

LM358 (Pin 8) to +12v Eurorack

LM358 (Pin 2) to branching point B

branching point B through 10kOhm Resistor to GND

branching point B though 10kOhm Resistor and 4.7kOhm Resistor to branching point C

LM358 (Pin 1) to branching point C

branching point C to Output in CV

## !Make sure that all grounds are connected to each other.!