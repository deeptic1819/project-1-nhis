from tkinter import *

# Create the main window
root = Tk()
root.title("Python Calculator")
root.geometry("350x325+400+200")

# Global variable to store the current math expression
expression = ""

# Function to update the expression variable
def update_expression(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the math expression
def evaluate_expression():
    global expression
    try:
        result = eval(expression)
        equation.set(result)
        expression = str(result)
    except Exception as e:
        equation.set("Error")
        expression = ""

# Function to clear the expression
def clear_expression():
    global expression
    expression = ""
    equation.set("")

# Create the entry field for displaying the math expression
equation = StringVar()
entry_field = Entry(root, textvariable=equation,justify="right",font=("arial",20,'bold'),bd=20,bg="grey")
entry_field.grid(row=0,columnspan=4)

# Create the number buttons
button_1 = Button(root, text="1",height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"),command=lambda: update_expression(1))
button_1.grid(row=1, column=0)
button_2 = Button(root, text="2", height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"),command=lambda: update_expression(2))
button_2.grid(row=1, column=1)
button_3 = Button(root, text="3",height=2,width=6,bg='skyblue', font=("Verdana",14,"bold"),command=lambda: update_expression(3))
button_3.grid(row=1, column=2)

button_4 = Button(root, text="4",height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"), command=lambda: update_expression(4))
button_4.grid(row=2, column=0)
button_5 = Button(root, text="5", height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"),command=lambda: update_expression(5))
button_5.grid(row=2, column=1)
button_6 = Button(root, text="6",height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"), command=lambda: update_expression(6))
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"),command=lambda: update_expression(7))
button_7.grid(row=3, column=0)
button_8 = Button(root, text="8", height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"),command=lambda: update_expression(8))
button_8.grid(row=3, column=1)
button_9 = Button(root, text="9",height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"), command=lambda: update_expression(9))
button_9.grid(row=3, column=2)

button_0 = Button(root, text="0",height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"), command=lambda: update_expression(0))
button_0.grid(row=4, column=0)

# Create the operator buttons
button_add = Button(root, text="+",height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"), command=lambda: update_expression("+"))
button_add.grid(row=1, column=3)

button_subtract = Button(root, text="-", height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"),command=lambda: update_expression("-"))
button_subtract.grid(row=2, column=3)

button_multiply = Button(root, text="*", height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"),command=lambda: update_expression("*"))
button_multiply.grid(row=3, column=3)

button_divide = Button(root, text="/",height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"), command=lambda: update_expression("/"))
button_divide.grid(row=4, column=3)

button_equal = Button(root, text="=",height=2,width=6,bg='skyblue', font=("Verdana",14,"bold"),command=evaluate_expression)
button_equal.grid(row=4, column=2)

button_clear = Button(root, text="C",height=2,width=6,bg='skyblue',font=("Verdana",14,"bold"), command=clear_expression)
button_clear.grid(row=4, column=1)

# Start the GUI event loop

root.mainloop()



