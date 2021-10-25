# Battery-Optimization-System
A battery optimization system for a drone system
This is a simple python app that can track the battery usage by a drone system based on measured current. The current expended is measured with an ACS 712 current sensor. The value is then collected with a raspberry pi 3 through an ADC system because the current sensor is analog while the Rpi is digital. The collected current values is then added throughout the duration of operation and is compared to the maximum supply of the battery used. This gives the estimated remaining battery life at every given time. The system is based on a simple python app with tkinter as the interface.
A future project will be to make a webserver interface.
