# mcp4725: DAC (Range: 0 - 4095, corresponds to 0 - 3.3V)
# vl53l0x: TOF Sensor

import board
import busio
import time
import adafruit_mcp4725
import adafruit_vl53l0x

MIN_CV = 0
MAX_CV = 8

# Maximale Länge der FIFO-Queue
# Nur ungerade Zahlen nehmen, damit die Berechnung funktioniert!
QUEUE_SIZE = 4

fifo_queue = [0] * QUEUE_SIZE

def add_to_fifo(val):
    fifo_queue.append(val)
    if len(fifo_queue) > QUEUE_SIZE:
        fifo_queue.pop(0)


i2c = busio.I2C(board.GP5, board.GP4)

dac = adafruit_mcp4725.MCP4725(i2c, address=0x60)
tof = adafruit_vl53l0x.VL53L0X(i2c, address=0x29)

def mean(values):
    clean = [v for v in values if isinstance(v, (int, float))]
    return sum(clean) / len(clean) if clean else MIN_CV

def median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n == 0:
        return 0
    elif n % 2 == 1:
        return sorted_vals[n // 2]
    else:
        mid1 = sorted_vals[n // 2 - 1]
        mid2 = sorted_vals[n // 2]
        return (mid1 + mid2) / 2

def measure_distance():
    dist = tof.range
    return dist if dist > 0 else None

def distance_to_cv(distance_mm):
    if distance_mm is None or distance_mm > 200:  # über 20cm
        return MIN_CV  # minimaler CV-Wert
    elif distance_mm < 20:  # unter 2cm nicht definiert, hier min 2cm setzen
        distance_mm = 20
    # linear von 20cm=0.01V bis 2cm=8V
    # 20cm=200mm, 2cm=20mm
    voltage = MIN_CV + (MAX_CV - MIN_CV) * (200 - distance_mm) / (200 - 20)
    return max(MIN_CV, min(MAX_CV, voltage))


def distance_to_normalized_dac(distance_mm):
    if distance_mm is None or distance_mm > 200:  # über 20cm
        # Vermeide 0, da MCP4725-Library bei exakt 0 eine AssertionError wirft
        return MIN_CV
    elif distance_mm < 20:  # unter 2cm nicht definiert, hier min 2cm setzen
        distance_mm = 20
    # linear von 20cm=0.01V bis 2cm=8V
    # 20cm=200mm, 2cm=20mm
    dac.norm = (200 - distance_mm) / (200 - 20)
    return max(MIN_CV, min(1, dac.norm))

try:
    current_dac_value = 0

    while True:
        distance = measure_distance()
        add_to_fifo(distance)

        #dac_norm = distance_to_normalized_dac(distance)
        dist_mean = mean(fifo_queue)
        #dist_median = median(fifo_queue)
        dac_norm_mean = distance_to_normalized_dac(dist_mean)
        #dac_norm_median = distance_to_normalized_dac(dist_median)

        #print(f"Entfernung: {distance if distance is not None else 'N/A'} mm; FIFO: {fifo_queue}; mean_dist: {dist_mean:.2f}; median_dist: {dist_median:.2f}; DAC.norm.mean Wert: {dac_norm_mean:.2f}; DAC.norm.median Wert: {dac_norm_median:.2f}")

        # Setze den DAC Wert (normalisiert von 0 bis 1 = 3.3V)
        #dac.normalized_value = dac_norm
        dac.normalized_value = dac_norm_mean
        #dac.normalized_value = dac_norm_median
        
        # ca. TODO Hz Update für glatte Übergänge
        time.sleep(0.0001)  

except KeyboardInterrupt:
    print("\nProgramm beendet")
    dac.value = 0

