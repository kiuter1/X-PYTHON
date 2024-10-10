import tkinter
from tkinter import messagebox


def check_temperature():
    try:
        temperature = float(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")
    if temperature <= 0:
        result_label.config(text="A cold, isn’t it?.")
    elif temperature > 0 and temperature < 10:
        result_label.config(text="Cool.")
    else:
        result_label.config(text="Nice weather we’re having..")

window = tkinter.Tk()
window.title("Temperature Checker")

label = tkinter.Label(window, text="Enter temperature:")
label.pack()

entry = tkinter.Entry(window)
entry.pack()

button = tkinter.Button(window, text="Check Temperature", command=check_temperature)
button.pack()

result_label = tkinter.Label(window)
result_label.pack()

window.mainloop()