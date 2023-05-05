from tkinter import *

root = Tk()
root.geometry("800x800")
root.title("Profits for TX-CORP")


month = ("January","Feburary","March","April","May","June","July","August","September","October","November","December")

profit = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

label1 = Label(root, text = "Months - January, February, March, April, May, June, July, August, September, October, November, and December")
label2 = Label(root, text = "Profits  - 20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000")
label3 = Label(root)
label4 = Label(root)

def max1():
    max_profit = max(profit)
    max_profit_index = profit.index(max_profit)
    mxpm = month[max_profit_index]
    label3["text"]="Max profit was "+str(max_profit)+" in the month of "+str(mxpm)+"."

def min1():
    min_profit = min(profit)
    min_profit_index = profit.index(min_profit)
    mnpm = month[min_profit_index]
    label4["text"]="Lowest profit recorded was "+str(min_profit)+" in the month of "+str(mnpm)+"."
    
btn1 = Button(root, text = "Show Max Profit", command = max1)
btn2 = Button(root, text = "Show Min Profit", command = min1)
btn1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
btn2.place(relx = 0.5, rely = 0.8, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.3, anchor = CENTER)
label2.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label3.place(relx = 0.5, rely = 0.7, anchor = CENTER)
label4.place(relx = 0.5, rely = 0.9, anchor = CENTER)
root.mainloop()