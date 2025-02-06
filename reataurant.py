from tkinter import *
import time
import calc_function
import random

root = Tk()
root.geometry("1400x700")
root.title("Restaurant Payment System")

top = Frame(root,width=1400,height=50)
top.pack(side=TOP)
frame1 = Frame(root,width=900,height=650)
frame1.pack(side=LEFT)
frame2 = Frame(root,width=400,height=650)
frame2.pack(side=RIGHT)

app_title = Label(top,font=('arial',30,'bold'),text="RESTAURANT PAYMENT SYSTEM")
app_title.grid(row=0,column=0)

localtime = time.asctime(time.localtime(time.time()))
app_time = Label(top,font=('arial',20),text=localtime)
app_time.grid(row = 1 , column=0)

calc_function.calculator(frame2)

fries= StringVar()
larggefries=StringVar()
burger=StringVar()
fillet=StringVar()
cheeseburger=StringVar()
drinks=StringVar()
order_no=StringVar()
cost=StringVar()
service_charge=StringVar()
tax=StringVar()
subtotal=StringVar()
total=StringVar()

price_list ={"fries":2.5,"largefries":3.5,"burger":5.5,"filet":4.5,"cburger":6.0,"drinks":2.0}

def bill():
    x = str(random.randint(10000, 99999))
    order_no.set(x)

    # Get item counts from user input
    count_of_fries = int(fries.get())
    count_of_lfries = int(largefries.get())  
    count_of_burger = int(burger.get())
    count_of_filet = int(fillet.get())  
    count_of_chesse = int(cheeseburger.get())  
    count_of_drinks = int(drinks.get())

    # Calculate individual costs correctly
    cost_of_fries = count_of_fries * price_list['fries']
    cost_of_lfries = count_of_lfries * price_list['largefries']  
    cost_of_burger = count_of_burger * price_list['burger']
    cost_of_filet = count_of_filet * price_list['filet']  
    cost_of_chesse = count_of_chesse * price_list['cburger']
    cost_of_drinks = count_of_drinks * price_list['drinks']

    # Compute total cost before tax
    cost_of_meal_value = cost_of_fries + cost_of_lfries + cost_of_burger + cost_of_filet + cost_of_chesse + cost_of_drinks

    # Compute tax and service charge
    tax_value = cost_of_meal_value * 0.1  # 10% tax
    service_charge_value = cost_of_meal_value * 0.125  # 12.5% service charge

    # Compute final total
    total_cost_value = cost_of_meal_value + tax_value + service_charge_value  

    # Convert to formatted strings
    cost_of_meal = "Rs " + str('%.2f' % cost_of_meal_value)
    paid_tax = "Rs " + str('%.2f' % tax_value)
    service_charge = "Rs " + str('%.2f' % service_charge_value)
    overall_cost = "Rs " + str('%.2f' % total_cost_value)

    # Set values to respective fields
    cost.set(cost_of_meal)
    tax.set(paid_tax)
    service_charge.set(service_charge)
    subtotal.set(cost_of_meal)
    total.set(overall_cost)


lblfries =Label(frame1,font=('arial',16,"bold"),text="Fries")
lblfries.grid(row=0,column=0)

txtfries = Entry(frame1,font=('arial',16,'bold'), textvariable=fries,bd=6,bg="white",justify="right")
txtfries.grid(row=0,column=1)

lbllargefries =Label(frame1,font=('arial',16,"bold"),text="largefries")
lbllargefries.grid(row=1,column=0)

txtlargefries = Entry(frame1,font=('arial',16,'bold'), textvariable=larggefries,bd=6,bg="white",justify="right")
txtlargefries.grid(row=1,column=1)

lblburger =Label(frame1,font=('arial',16,"bold"),text="burger")
lblburger.grid(row=2,column=0)

txtburger = Entry(frame1,font=('arial',16,'bold'), textvariable=lblburger,bd=6,bg="white",justify="right")
txtburger.grid(row=2,column=1)

lblcheeseburger =Label(frame1,font=('arial',16,"bold"),text="cheeseburger")
lblcheeseburger.grid(row=3,column=0)

txtcheeseburger = Entry(frame1,font=('arial',16,'bold'), textvariable=lblcheeseburger,bd=6,bg="white",justify="right")
txtcheeseburger.grid(row=3,column=1)

lblfillet =Label(frame1,font=('arial',16,"bold"),text="Fillet")
lblfillet.grid(row=4,column=0)

txtfillet = Entry(frame1,font=('arial',16,'bold'), textvariable=fries,bd=6,bg="white",justify="right")
txtfillet.grid(row=4,column=1)

lbldrinks =Label(frame1,font=('arial',16,"bold"),text="drinks")
lbldrinks.grid(row=5,column=0)

txtdrinks = Entry(frame1,font=('arial',16,'bold'), textvariable=fries,bd=6,bg="white",justify="right")
txtdrinks.grid(row=5,column=1)

lblorder =Label(frame1,font=('arial',16,"bold"),text="order",fg="steel blue")
lblorder.grid(row=0,column=2)

txtorder = Entry(frame1,font=('arial',16,'bold'), textvariable=order_no,bd=6,bg="white",justify="right")
txtorder.grid(row=0,column=3)

lblcost =Label(frame1,font=('arial',16,"bold"),text="cost",fg="steel blue")
lblcost.grid(row=1,column=2)

txtcost = Entry(frame1,font=('arial',16,'bold'), textvariable=cost,bd=6,bg="white",justify="right")
txtcost.grid(row=1,column=3)

lblservicecharge =Label(frame1,font=('arial',16,"bold"),text="service charge",fg="steel blue")
lblservicecharge.grid(row=2,column=2)

txtservicecharge = Entry(frame1,font=('arial',16,'bold'), textvariable=service_charge,bd=6,bg="white",justify="right")
txtservicecharge.grid(row=2,column=3)

lbltax =Label(frame1,font=('arial',16,"bold"),text="tax",fg="steel blue")
lbltax.grid(row=3,column=2)

txttax = Entry(frame1,font=('arial',16,'bold'), textvariable=tax,bd=6,bg="white",justify="right")
txttax.grid(row=3,column=3)

lblsubtotal =Label(frame1,font=('arial',16,"bold"),text="subtotal",fg="steel blue")
lblsubtotal.grid(row=4,column=2)

txtsubtotal = Entry(frame1,font=('arial',16,'bold'), textvariable=subtotal,bd=6,bg="white",justify="right")
txtsubtotal.grid(row=4,column=3)

lbltotal =Label(frame1,font=('arial',16,"bold"),text="total",fg="steel blue")
lbltotal.grid(row=5,column=2)

txttotal = Entry(frame1,font=('arial',16,'bold'), textvariable=total,bd=6,bg="white",justify="right")
txttotal.grid(row=5,column=3)

lbltotal = Label(frame1,text="-",fg="white")
lbltotal.grid(row=6,columnspan=4)

btnprice = Button(frame1,padx=16,pady=8,bd=10,fg="black",font=('arial',16,'bold'),width =10,text="PRICE",bg = "Powder blue")
btnprice.grid(row=7,column=0)

btntotal = Button(frame1,padx=16,pady=8,bd=10,fg="black",font=('arial',16,'bold'),width =10,text="TOTAL",bg = "Powder blue",command=bill)
btntotal.grid(row=7,column=1)

btnreset = Button(frame1,padx=16,pady=8,bd=10,fg="black",font=('arial',16,'bold'),width =10,text="RESET",bg = "Powder blue")
btnreset.grid(row=7,column=2)

btnexit = Button(frame1,padx=16,pady=8,bd=10,fg="black",font=('arial',16,'bold'),width =10,text="EXIT",bg = "Powder blue")
btnexit.grid(row=7,column=3)

root.mainloop()