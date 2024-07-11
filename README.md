# Battery Optimization System Test

This project demonstrates a battery optimization system using a Raspberry Pi, SPI communication, and a graphical interface created with Tkinter. The system reads voltage and current values from a sensor connected to an MCP3008 ADC and displays these values in a GUI.

## Features
- **SPI Communication**: Communicates with SPI devices using the `spidev` library.
- **Sensor Readings**: Reads analog values from an MCP3008 ADC and calculates voltage and current.
- **GUI Display**: Displays real-time voltage and current readings in a Tkinter-based GUI.
- **Multithreading**: Utilizes threading to update sensor readings without freezing the GUI.

## Requirements
- Python 3
- spidev
- numpy
- RPi.GPIO
- Tkinter
- ttk

## Code Explanation
The main script performs the following tasks:

- **Initialize SPI Connection**: Sets up the SPI connection to communicate with the MCP3008 ADC.
- **GPIO Setup**: Configures GPIO pins for LED output (commented out in the provided code).
- **Analog Data Reading**: Reads data from the MCP3008 ADC channels and converts it to voltage and current values.
- **Sensor Reading Functions**: Functions to read voltage and current values, and print them to the console.
- **Multithreading**: Uses threading to continuously update the sensor readings without freezing the GUI.
- **Tkinter GUI**: Sets up a Tkinter window with labels and buttons to display the voltage and current readings.

## Acknowledgment
This is a third year class project in Mechatronics System design.
