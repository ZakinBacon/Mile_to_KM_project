from tkinter import *

window = Tk()

window.title("Mile to KM Project")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def miles_to_km():
    km = input.get()  # Gets info from input
    km = int(km) * 1.609344  # calulation for Miles to KM
    starting_km["text"] = km  # Replace the text ok KM


# Creates the Label for is equal to
is_equal_to = Label(text="Is equal to", font=("Arial", 24, "bold"))
is_equal_to.grid(column=0, row=1)
# Creates the Label for KM
starting_km = Label(text="0", font=("Arial", 24, "bold"))
starting_km.grid(column=1, row=1)
# Creates the Label for miles
miles = Label(text="miles", font=("Arial", 24, "bold"))
miles.grid(column=2, row=0)
# Creates the Label for KM
km = Label(text="KM", font=("Arial", 24, "bold"))
km.grid(column=2, row=1)
# Creates the input area for the user to put in the miles
input = Entry(width=10)
input.grid(column=1, row=0)
# Creates the button to calculate the miles to KM
button2 = Button(text="Calculate", command=miles_to_km)
button2.grid(column=1, row=2)

window.mainloop()
