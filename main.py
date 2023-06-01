from tkinter import *

# window setup
my_window = Tk()


def window_setup():

    my_window.title("BMI Calculator")
    my_window.minsize(width=300, height=300)
    my_window.config(padx=50, pady=50)


# weight label setup
weight_label = Label(text="Enter Your Weight(kg)")


def weight_label_setup():

    weight_label.config(pady=10, padx=10)
    weight_label.pack()


weight_label_setup()

# weight entry setup
weight_entry = Entry(width=10)
weight_entry.pack()
weight_entry.focus()

# height label setup
height_label = Label(text="Enter Your Height(cm)")


def height_label_setup():

    height_label.config(pady=10, padx=10)
    height_label.pack()


height_label_setup()

# height entry setup
height_entry = Entry(width=10)
height_entry.pack()

# calculate button setup

calculate_button = Button(text="Calculate")
calculate_button.pack()

window_setup()


my_window.mainloop()
