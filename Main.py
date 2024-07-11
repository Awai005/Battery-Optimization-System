import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay
import RPi.GPIO as GPIO	# To use GPIO pins
# Start SPI connection
import Tkinter as tk
from Tkinter import*
import ttk
import threading
from threading import*
spi = spidev.SpiDev() # Created an object
spi.open(0,0)	

# Initializing LED pin as OUTPUT pin
#led_pin = 20
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(led_pin, GPIO.OUT) 

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
def Volts(data):
	volts = (data * 3.3) / float(1023)
	volts = round(volts, 2)
	return volts
def Current(data):
	volts = (data / 1024.0) * 5000 #(data * 3.3) / float(1023)
	volts = round(volts, 2)
	current = ((volts - 2500) / 100)
	return current

def read_sensor():
	output = analogInput(0) # Reading from CH0
	volt_out = Volts(output)
	current_out = Current(output)
	print("Voltage is   {}".format(volt_out))
	sleep(0.05)
	print("Current is   {}".format(current_out))
	print ('\n')
	sleep(2)
	return current_out
def current_reading():
	output = analogInput(0) # Reading from CH0
	current_out = Current(output)
	sleep(1)
	return current_out
def voltage_reading():
	output = analogInput(0) # Reading from CH0
	volt_out = Volts(output)
	sleep(1)
	return volt_out

def threading():
	t1 = Thread(target=read_sensor)
	#root = Tk()
	#volt_out = Volts(output)
	current_out = current_reading()
	volt_out = voltage_reading()
	var = tk.StringVar()
	var2 = tk.StringVar()
	lbl2.config(text = volt_out)
	lbl.config(text = str(round(current_out,4)))
	progress = current_out
	newprogress = current_out + progress
	t1.start()
	#print("progress   {}".format(newprogress))
	lbl.after(1000, threading)

#task = threading.Thread(target=read_sensor)#daemon=True)
#root = tk.Tk()
#root.geometry("400x400")
#var = tk.StringVar()
#lbl = tk.Label(root, textvariable = var, width=40, height=5, font=('consolas', 24, 'bold'))
#lbl.pack()
#b = Button(root, text ="touch me", command = threading)
#b.pack()
#task.start()
#root.mainloop
top = Tk() 
top.title("Battery Optimization System Test")
#top.geometry("200x100")
top.geometry("200x100") 
lbl3 = tk.Label(top, text ="Voltage in 'V'", width=30, height=3, font=('consolas', 24, 'bold'))
lbl3.pack()
lbl2 = tk.Button(top, width = 30, height=2, font=('consolas', 15))
lbl2.pack()
lbl4 = tk.Label(top, text ="Current in 'A'", width=30, height=2, font=('consolas', 24, 'bold'))
lbl4.pack()
lbl = tk.Button(top, width=30, height=2, font=('consolas', 15))
lbl.pack()
lbl5 = tk.Button(top, text ="tek motor", width = 7, height = 1, font=('consolas', 24, 'bold'))
lbl5.pack()
lbl6 = tk.Button(top, text ="cift motor", width = 7, height = 1, font=('consolas', 24, 'bold'))
lbl6.pack()
my_progress = ttk.Progressbar(top, orient=HORIZONTAL, length = 300, mode='determinate')
my_progress.pack(pady=10)
my_progress['value'] = 90


def bar():
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

  
threading() 
  
top.mainloop() 


