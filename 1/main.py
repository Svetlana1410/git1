import matplotlib.pyplot as plt
from openpyxl import load_workbook
from tkinter import *  
cities = []
temperatures = []

def clicked():
    a = txt.get()
    wb = load_workbook(a)
    sheet = wb['Second']
    
    counter = 1
    counterTemp = 1
    while sheet['A' + str(counter)].value != None:
        cities.append(sheet['A' + str(counter)].value)
        counter += 1
    while sheet['B' + str(counterTemp)].value != None:
        temperatures.append(sheet['B' + str(counterTemp)].value)
        counterTemp += 1
    lb2.grid(column=1, row=1)
    btn1.grid(column=0, row=2)
    btn2.grid(column=2, row=2)

def clicked1():
    plt.bar(cities, temperatures)
    plt.show()

def clicked2():
    print(cities)
    print(temperatures)

    
window = Tk()  
window.title("Excell")
window.geometry('400x250')
lbl = Label(window, text="Введите название файла")  
lbl.grid(column=0, row=0)
lb2 = Label(window, text="Файл открыт!")
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)
btn = Button(window, text="Открыть файл", command=clicked) 
btn.grid(column=2, row=0)
btn1 = Button(window, text="Построить график", command=clicked1) 
btn2 = Button(window, text="Вывести данные", command=clicked2) 
window.mainloop()







