import tkinter as tk
import calculator

root = tk.Tk()
root.configure(padx=10, pady=10)
root.resizable(height=False, width=False)

def no_result():
    noResultScreen = tk.Toplevel()
    noResultScreen.configure(padx=10, pady=10)

    label = tk.Label(noResultScreen, text='A feladatnak nincs megoldasa.')
    label.grid(row=0, column=0)

def not_number_error(e):
    errorScreen = tk.Toplevel()
    errorScreen.configure(padx=10, pady=10)

    label = tk.Label(errorScreen, text='Nem szam van valamelyik mezoben!')
    label.grid(row=0, column=0)

    error = tk.Label(errorScreen, text=e)
    error.grid(row=1, column=0)

def result_screen(x1, x2):
    resultScreen = tk.Toplevel()
    resultScreen.configure(padx=10, pady=10)
    resultScreen.geometry('150x60')
    resultScreen.resizable(height=False, width=False)

    x1Label = tk.Label(resultScreen, text='X1 = '+ str(x1))
    x1Label.grid(row=0, column=0)

    x2Label = tk.Label(resultScreen, text='X2 = '+ str(x2))
    x2Label.grid(row=1, column=0)

def accept(a, b, c):
    try:
        a=float(a.get())
        b=float(b.get())
        c=float(c.get())
        
        result = calculator.calculate(a,b,c)

        if result == False:
            no_result()
        else:
            print(type(result))
            x1 = result['x1']
            x2 = result['x2']
            result_screen(x1, x2)

    except ValueError as e:
        not_number_error(e)



title = tk.Label(root, text='2.Fok fuggveny megoldo')
title.grid(row=0, column=0, columnspan=2)

a_label = tk.Label(root, text='A: ')
a_label.grid(row=1, column=0, pady=5)

a_entry = tk.Entry(root)
a_entry.grid(row=1, column=1)

b_label = tk.Label(root, text='B: ')
b_label.grid(row=2, column=0, pady=5)

b_entry = tk.Entry(root)
b_entry.grid(row=2, column=1)

c_label = tk.Label(root, text='C: ')
c_label.grid(row=3, column=0, pady=5)

c_entry = tk.Entry(root)
c_entry.grid(row=3, column=1)

accept_button = tk.Button(root, text='Szamol', command=lambda:accept(a_entry,b_entry,c_entry))
accept_button.grid(row=4, column=0, columnspan=2)

root.mainloop()