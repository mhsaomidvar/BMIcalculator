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

result = StringVar()


def calculate():
    try:
        w = int(weight_entry.get())
        h = int(height_entry.get())
        BMI = w / ((h/100)**2)
        print(BMI)

        if BMI < 18.5:
            result.set("Underweight")
            print("Underweight")
        elif 18.5 <= BMI < 25:
            result.set("Normal")
            print("Normal")
        elif 25 <= BMI < 30:
            result.set("Overweight")
            print("Overweight")
        elif 30 <= BMI < 40:
            result.set("Obese")
            print("Obese")
        elif 40 <= BMI :
            result.set("Morbidly obese")
            print("Morbidly Obese")
    except:
        result.set("check your entry.")
        print("check your entry.")


# calculate button setup


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.config(bg="white")
calculate_button.pack()


# result label setup

result_label = Label(textvariable=result, font=["Arial", 11, "normal"])
result_label.config(padx=10, pady=10)
result_label.pack()


window_setup()
my_window.mainloop()
