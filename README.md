# Proxima

A Eurorack module that measures the distance using a VL53L0X Time-of-Flight sensor and converts it into a Control Voltage (CV) for your modular system.
Control parameters easily with hand movements in the air.

⸻

# Installation
	1.	Install CircuitPython on the Pico
	2.	Download this repository
	3.	Copy Proxima_R2CV.py to the Pico
	4.	Copy the contents of the libs folder into the lib folder on the Pico:


## Features
	•	Distance range: 2 cm to 20 cm
	•	CV output: 0 V to 8 V
	•	Smooth values using a moving average filter

⸻

## Hardware Notes
	•	+5 V from Eurorack → VSYS (Pin 39) on Pico
	•	GND connected
	•	+12 V from Eurorack → Pin 8 of LM358 (Op-Amp power supply)
	•	GND connected

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

