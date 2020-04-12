from tkinter import *
import math

def BMICalculator(event):
    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    labelBMI.configure(text = "Your BMI is :"+str(BMI))
    if BMI >= 30.0:
        labelWeightStatus.configure(text = "Your are Obese",fg = "red", bg = "blue")
    elif BMI >= 25.0:
        labelWeightStatus.configure(text="Your are Fat",fg = "orange",bg = "blue")
    elif BMI >= 23.0:
        labelWeightStatus.configure(text="Your are Overweight",fg = "orange",bg = "blue")
    elif BMI >= 18.6:
        labelWeightStatus.configure(text="Your are Normal or Healthy Weight",fg = "yellow",bg = "blue")
    else:
        labelWeightStatus.configure(text="Your are Underweight",fg = "red", bg = "blue")

BMIWindow = Tk()
labelHeight = Label(BMIWindow,text="Height (c.m.)").grid(row=0,column=0)
textBoxHeight = Entry(BMIWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(BMIWindow,text="Weight (kg)").grid(row=1,column=0)
textBoxWeight = Entry(BMIWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(BMIWindow,text="Calculate BMI")
calculateButton.bind('<Button-1>',BMICalculator)
calculateButton.grid(row=2,column=0)
labelBMI = Label(BMIWindow,text = "Result")
labelBMI.grid(row=2,column=1)
labelWeightStatus = Label(BMIWindow,text = "Your Weight Status",font = ("Helvetica",16))
labelWeightStatus.grid(row=3,column=0)
mainloop()