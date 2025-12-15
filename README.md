# Smart Steve Commander v1

A custom mechanical macropad designed to control the "Smart Steve" personal automation assistant. It features a rotary encoder for volume/media control, an OLED screen for system status, and 8 mechanical keys for shortcuts.

Designed using KiCad and Fusion 360.

## Features
* **MCU:** Seeed XIAO RP2040
* **Inputs:** 8x MX-Style Mechanical Switches + 1x EC11 Rotary Encoder
* **Display:** 0.91" OLED I2C Display
* **Lighting:** 1x SK6812 (Neopixel) RGB LED for status indication
* **Case:** 3D Printed Sandwich Case

## Project Structure
* `/CAD`: Contains the complete 3D assembly (.STEP)
* `/PCB`: KiCad source files
* `/Firmware`: CircuitPython/KMK placeholder

## Bill of Materials (BOM)

| Component | Quantity | Description |
| :--- | :--- | :--- |
| Seeed XIAO RP2040 | 1 | Microcontroller |
| Cherry MX Style Switch | 8 | Mechanical Keys |
| Keycaps | 8 | 1U Keycaps |
| EC11 Rotary Encoder | 1 | Encoder with Push Button |
| 0.91" OLED Display | 1 | I2C 128x32 Display |
| SK6812 / WS2812B | 1 | RGB LED (5050 package) |
| 1N4148 Diodes | 9 | Through-hole diodes |
| 3D Printed Case | 1 | PLA/PETG |

## Gallery

### 3D Assembly
<img width="1518" height="966" alt="image" src="https://github.com/user-attachments/assets/262cc9a8-d6bd-48d6-9d67-e4a16fae2f9f" />


### PCB Layout
<img width="982" height="847" alt="image" src="https://github.com/user-attachments/assets/06166287-eb32-4ed2-ac6a-8830f578c204" />


### Schematic
<img width="830" height="587" alt="image" src="https://github.com/user-attachments/assets/67f401fb-b596-4992-8aa5-8e49458d18d8" />


### Case Assembly (Cross Section)
<img width="1514" height="974" alt="image" src="https://github.com/user-attachments/assets/5407dda6-96ae-4029-9367-83ad7d32fd38" />
