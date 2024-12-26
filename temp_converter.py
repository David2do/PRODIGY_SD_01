import tkinter as tk
from tkinter import messagebox

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_fahrenheit(celsius):
    return 1.8 * celsius + 32

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * (5 / 9) + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 1.8 + 32

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def converter():
    value = entry_value.get()
    temp_unit = selected_unit.get()

    if not value.replace('.', '', 1).isdigit():
        messagebox.showerror("Invalid value", "Please enter a valid number")
        return

    value = float(value)

    if temp_unit == '°C':
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        result_label.config(text=f"{value}°C is equivalent to {f:.2f}°F and {k:.2f}K")
    elif temp_unit == '°F':
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        result_label.config(text=f"{value}°F is equivalent to {c:.2f}°C and {k:.2f}K")
    elif temp_unit == 'K':
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        result_label.config(text=f"{value}K is equivalent to {c:.2f}°C and {f:.2f}°F")
    else:
        messagebox.showerror("Error", "Invalid unit of measurement")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Input for temperature value
label_value = tk.Label(root, text="Enter the temperature value:")
label_value.pack()

entry_value = tk.Entry(root)
entry_value.pack()

# Dropdown menu for temperature unit selection
label_unit = tk.Label(root, text="Select the unit (°C, °F, K):")
label_unit.pack()

# Dropdown options
options = ["°C", "°F", "K"]
selected_unit = tk.StringVar()
selected_unit.set(options[0])  # Default value

unit_menu = tk.OptionMenu(root, selected_unit, *options)
unit_menu.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=converter)
convert_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
