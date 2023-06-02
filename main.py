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


# calculate and error check function


def calculate():
    while True:
        try:
            w = int(weight_entry.get())
            h = int(height_entry.get())
            BMI = w / ((h/100)**2)
            print(BMI)

            if 18.5 <= BMI < 25:
                print("Normal")
            elif 25 <= BMI < 30:
                print("Overweight")
            elif 30 <= BMI < 40:
                print("Obese")
            elif 40 <= BMI :
                print("Morbidly Obese")

            break

        except:
            print("please check your entry.")
            break


# calculate button setup

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.config(bg="white")
calculate_button.pack()


window_setup()
my_window.mainloop()
