import tkinter as tk
from tkinter import messagebox
import csv
import os
from tkinter import font


j=0
n=None
s = None


W1 = tk.Tk()
W1.configure(bg="#D6C7B7")
W1.geometry("700x700")

W2 = tk.Tk()
W2.configure(bg="#D6C7B7") 
W2.geometry('700x700')

W3 = tk.Tk()
W3.configure(bg="#D6C7B7")
W3.geometry("700x700")
 
window1 = tk.Toplevel()
window1.configure(bg="#D6C7B7")
window1.geometry("700x700")
window1.withdraw()

window2 = tk.Toplevel()
window2.configure(bg="#D6C7B7")
window2.geometry("700x700")
window2.withdraw()

window3 = tk.Toplevel()
window3.configure(bg="#D6C7B7")
window3.geometry("700x700")
window3.withdraw()

WWW =tk.Tk()
WWW.configure(bg="#D6C7B7")
WWW.geometry("700x700")
WWW.withdraw()
bought = tk.Label(WWW, fg="#594030", font=("Ariel", 17, 'bold'), bg="#D6C7B7", text="ITEM BOUGHT!")
bought.place(x=220, y=300)


def go_back(window1, W2):
    window1.withdraw()
    W2.deiconify()
    

def gBack():
    go_back(window1, W1)

def pBack():
    go_back(window2, W1)

def dBack():
    go_back(window3, W1)


def on_click(W2, W1):
    W2.destroy()
    W1.deiconify()

def w1():
    on_click(W2, W1)

def w2():
    on_click(W2, W3)


F = open('file.csv', 'r')
i = csv.reader(F)

a,b,c = 1,1,1
gItems = []
pItems = []
dItems = []

for l in i:
    if l[1] == 'g' or l[1] == 'G':
        gItems.append((str(a)+'.   '+l[2]))
        a+=1

    elif l[1] == 'p' or l[1] == 'P':
        pItems.append((str(b)+'.   '+l[2]))
        NameP = tk.Label(window2, text=l[2])
        PriceP = tk.Label(window2, text=l[3])
        b+=1


    elif l[1] == 'd' or l[1] == 'G':
        dItems.append((str(c)+'.   '+l[2]))
        NameD = tk.Label(window3, text=l[2])
        PriceD = tk.Label(window3, text=l[3])
        c+=1

    
    
    

q=50

for gg in gItems:
    NameG = tk.Label(window1, text=gg, fg="#594030", font=("Ariel", 17, 'bold'), bg="#D6C7B7")
    NameG.place(x=100, y=100+q)
    q+=50

r=50

for pp in pItems:
    NameP = tk.Label(window2, text=pp, fg="#594030", font=("Ariel", 17, 'bold'), bg="#D6C7B7")
    NameP.place(x=100, y=100+r)
    r+=50

s=50

for dd in dItems:
    NameD = tk.Label(window3, text=dd, fg="#594030", font=("Ariel", 17, 'bold'), bg="#D6C7B7")
    NameD.place(x=100, y=100+s)
    s+=50


F.close()

def BuyGuitar():
    global gItems, GenterE
    GBuyItem = int(GenterE.get())
    
    if GBuyItem <= len(gItems):
        F = open('file.csv', 'r')
        A = open('temp.csv', 'w', newline='')
        R = csv.reader(F)
        W = csv.writer(A)

        for x in gItems:
            if int(x[0]) == GBuyItem:
                for r in R:
                    if x.split()[1] != r[2]:
                        W.writerow(r)

        F.close()
        A.close()
        os.remove('file.csv')
        os.rename('temp.csv','file.csv')
        window1.withdraw()
        window2.withdraw()
        window3.withdraw()
        WWW.deiconify()
    else:
       messagebox.showerror("Error", " Invalid Serial No OR Serial No Out Of Range!")

    

def BuyPiano():
    global pItems, PenterE
    PBuyItem = int(PenterE.get())

    if PBuyItem <= len(pItems):
        F = open('file.csv', 'r')
        A = open('temp.csv', 'w', newline='')
        R = csv.reader(F)
        W = csv.writer(A)

        for x in pItems:
            if int(x[0]) == PBuyItem:
                for r in R:
                    if x.split()[1] != r[2]:
                        W.writerow(r)

        F.close()
        A.close()
        os.remove('file.csv')
        os.rename('temp.csv','file.csv')
        window1.withdraw()
        window2.withdraw()
        window3.withdraw()
        
        WWW.deiconify()
    else:
       messagebox.showerror("Error", " Invalid Serial No OR Serial No Out Of Range!")


def BuyDrum():
    global dItems, DenterE
    DBuyItem = int(DenterE.get())

    if DBuyItem <= len(dItems):
        F = open('file.csv', 'r')
        A = open('temp.csv', 'w', newline='')
        R = csv.reader(F)
        W = csv.writer(A)

        for x in dItems:
            if int(x[0]) == DBuyItem:
                for r in R:
                    if x.split()[1] != r[2]:
                        W.writerow(r)

        F.close()
        A.close()
        os.remove('file.csv')
        os.rename('temp.csv','file.csv')
        window1.withdraw()
        window2.withdraw()
        window3.withdraw()
        
        WWW.deiconify()
    else:
       messagebox.showerror("Error", " Invalid Serial No OR Serial No Out Of Range!")

if len(gItems) != 0:
    Genter = tk.Label(window1, text="Enter the serial no. of the instrument you want to buy: ", font=("Ariel", 12, 'bold'), fg="#35231D",bg="#D6C7B7")
    Genter.place(x=100, y=q+150)
    GenterE = tk.Entry(window1, width=10, font=("Montserrat", 13, 'bold'))
    GenterE.place(y=q+150, x=520)

    buyG = tk.Button(window1, command=BuyGuitar, text='BUY', relief='raised', font=('Ariel', 14, 'bold'))
    buyG.place(y=220+q, x=330)
else:
    oopsG = tk.Label(window1, text="NO ITEMS AVAILABLE", fg="#594030", font=("Ariel", 20, 'bold'), bg="#D6C7B7")
    oopsG.place(x=220, y=300)

if len(pItems) != 0:
    Penter = tk.Label(window2, text="Enter the serial no. of the instrument you want to buy: ", font=("Ariel", 12, 'bold'), fg="#35231D",bg="#D6C7B7")
    Penter.place(x=100, y=r+150)
    PenterE = tk.Entry(window2, width=10, font=("Montserrat", 13, 'bold'))
    PenterE.place(y=r+150, x=520)
    buyP = tk.Button(window2, command=BuyPiano, text='BUY', relief='raised', font=('Ariel', 14, 'bold'))
    buyP.place(y=220+r, x=330)
else:
    oopsP = tk.Label(window2, text="NO ITEMS AVAILABLE", fg="#594030", font=("Ariel", 20, 'bold'), bg="#D6C7B7")
    oopsP.place(x=220, y=300)

if len(dItems) != 0:
    Denter = tk.Label(window3, text="Enter the serial no. of the instrument you want to buy: ", font=("Ariel", 12, 'bold'), fg="#35231D",bg="#D6C7B7")
    Denter.place(x=100, y=s+150)
    DenterE = tk.Entry(window3, width=10, font=("Montserrat", 13, 'bold'))
    DenterE.place(y=s+150, x=520)
    buyD = tk.Button(window3, command=BuyDrum, text='BUY', relief='raised', font=('Ariel', 14, 'bold'))
    buyD.place(y=220+s, x=330)
else:
    oopsD = tk.Label(window3, text="NO ITEMS AVAILABLE", fg="#594030", font=("Ariel", 20, 'bold'), bg="#D6C7B7")
    oopsD.place(x=220, y=300)

# window1 (guitar) ELEMENTS
backG= tk.Button(window1, text="Back", command= gBack, bg="#D6C7B7", relief="groove", font=("Montserrat", 13, 'bold'))
backG.place(x=620, y=20)

# window2 (piano) ELEMENTS
backP = tk.Button(window2, text="Back", command= pBack, bg="#D6C7B7", relief="groove", font=("Montserrat", 13, 'bold'))
backP.place(x=620, y=20)

# window3 (drums) ELEMENTS
backD = tk.Button(window3, text="Back", command= dBack, bg="#D6C7B7", relief="groove", font=("Montserrat", 13, 'bold'))
backD.place(x=620, y=20)


def img_guitar():
    global window1
    window1.deiconify()
    W1.withdraw()
    

def img_piano():
    global window2
    window2.deiconify()
    W1.withdraw()
    

def img_drums():
    global window3
    window3.deiconify()
    W1.withdraw()
    


# W1 (USER) ELEMENTS
t1 = tk.Label(W1, text="WELCOME TO", fg="#594030", bg="#D6C7B7", font=("Ariel", 17, 'bold'))
t1.place(x=410, y=80)
t2 = tk.Label(W1, text="♫ MUSICALLY STORE ♫ ", fg="#594030", bg="#D6C7B7", font=('Montserrat', 23, 'bold'))
t2.place(y=120, x=300)

b1 = tk.Label(W1, text="Click the instrument you are looking for.", fg="#594030", bg="#D6C7B7", font=("Ariel", 12, 'bold'))
b1.place(x=20, y=640)


g1 = tk.Label(W1, text="GUITARS", font=("Ariel", 13, 'italic', 'bold'), foreground="black", bg = "#D6C7B7")
g1.place(x=43, y=250)

p1 = tk.Label(W1, text="PIANOS", font=("Helvetica", 13, 'italic', 'bold'), foreground="black", bg = "#D6C7B7")
p1.place(x=243, y=460)

d1 = tk.Label(W1, text="DRUMS", font=("Helvetica", 13, 'italic', 'bold'), foreground="black", bg = "#D6C7B7")
d1.place(x=455, y=660)

img_path1 = ".\guitar\guitar_icon.png"  
img_g = tk.PhotoImage(file=img_path1)
img_g_button = tk.Button(W1, width=200, height=200, image=img_g, command=img_guitar, bg="#D6C7B7", relief="groove")
img_g_button.place(x=38, y=48)

img_path2 = ".\piano\piano_icon.png"  
img_p = tk.PhotoImage(file=img_path2)
img_p_button = tk.Button(W1, width=200, height=200, image=img_p, command=img_piano, bg="#D6C7B7", relief="groove")
img_p_button.place(x= 240, y=255)

img_path3 = ".\drums\drums_icon.png"  
img_d = tk.PhotoImage(file=img_path3)
img_d_button = tk.Button(W1, width=200, height=200, image=img_d, command=img_drums, bg="#D6C7B7", relief="groove")
img_d_button.place(x=450, y=455)

    






# W2 (STARTING) ELEMENTS
user = tk.Button(W2, text="USER", command= w1, bg="#D6C7B7", relief="flat", font=("Montserrat", 20))
user.pack()
admin = tk.Button(W2, text="ADMIN", command= w2, bg="#D6C7B7", relief="flat", font=("Montserrat", 20))
admin.pack()








def menuEntry():
    if validateMenu(m.get()):
        if n == 1:
            addItem()

        if n == 2:
            displ()

        if n == 3:
            search()

        if n == 4:
            mod()
        
    else:
        messagebox.showerror('ERROR', 'Please enter number from the menu.')

def validateMenu(entry_text):
    if entry_text.isdigit() and int(entry_text) in range(1, 5): 
        global n 
        n = int(m.get()) 
        return True
    elif entry_text == "": 
        return True
    else:
        return False    
    


def validate_integer(entry_text):
    if entry_text.isdigit():  
        return True
    elif entry_text == "": 
        return True
    else:
        return False 



def AddingItems():

    if validate_integer(price.get()):
        if price.get():
            F = open("file.csv", 'a', newline='')
            w = csv.writer(F)

            i = idd.get()
            t = type.get()
            n = name.get()
            p = price.get()

            l =[i, t, n, p]

            w.writerow(l)
            F.close()

            idL.place_forget()
            idd.place_forget()
            idd.delete(0, tk.END)
            tyL.place_forget()
            type.place_forget()
            type.delete(0, tk.END)
            name.place_forget()
            nameL.place_forget()
            name.delete(0, tk.END)
            prL.place_forget()
            price.place_forget()
            price.delete(0, tk.END)
            ad1.place_forget()

    else:
        messagebox.showerror('ERROR', 'Please enter price properly.')


def Display():
    ll.destroy()
    disp.place_forget()
    for label in d_labels:
        label.destroy()


def SEARCH():
    sear.place_forget()
    s.destroy()
    seaID.destroy()
    sId.destroy()

def search_by_id():
    global s
    search_id = seaID.get()

    F = open('file.csv', 'r')
    l = csv.reader(F)
    ids=[]
    for x in l:
        ids.append(x[0])
        if x[0] == search_id:
            y = 'Id: '+x[0]+'\nName: '+x[1]+'\nType: '+x[2]+'\nPrice: ₹'+x[3]
            s = tk.Label(W3, text=y, font=("Montserrat", 15), foreground="black", bg="#D6C7B7")
            s.place(x=260, y=360)
            seaButton.destroy()
            sear.place(x=330, y=500)
    if search_id not in ids: 
        messagebox.showerror("ID DOESN'T EXIST", "There is no such id!")
    F.close()
    


def modify():
    F = open('file.csv', 'r')
    A = open('t.csv', 'w', newline='')
    w = csv.writer(A)
    l = csv.reader(F)
    for r in l :
        if r[0] == id_input.get():
            t = [id_input.get() , type.get(), name.get(), price.get()]
            w.writerow(t)
        else:
            w.writerow(r)
    F.close()
    A.close()
    os.remove('file.csv')
    os.rename('t.csv', 'file.csv')

    idL.place_forget()
    idd.place_forget()
    idd.delete(0, tk.END)
    tyL.place_forget()
    type.place_forget()
    type.delete(0, tk.END)
    name.place_forget()
    nameL.place_forget()
    name.delete(0, tk.END)
    prL.place_forget()
    price.place_forget()
    price.delete(0, tk.END)
    id_modified.place_forget()
    id_input.place_forget()
    id_input.delete(0, tk.END)
    modd.place_forget()




    
# W3 (ADMIN) ELEMENTS
text_list = ["MENU(Enter the number to perform the task)", "1. Add Instruments", "2. Display list of Instruments", "3. Search for an instrument (id)", "4. Modify Instrument details"]

for i, text in enumerate(text_list):
    label = tk.Label(W3, text=text, font=("Montserrat", 17), foreground="black", bg="#D6C7B7")
    j += 30
    label.place(x=30, y=int(j))
    print('\n')

mL= tk.Label(W3, text="Number from the menu: ", font=("Montserrat", 14), foreground="black", bg = "#D6C7B7")
mL.place(x=30, y=200)
m=tk.Entry(W3, width=40, font=("Montserrat", 14))
m.place(x=240, y=200)


process = tk.Button(W3, text="ENTER", command=menuEntry)
process.place(x=330, y=240)


idL= tk.Label(W3, text="ID: ", font=("Montserrat", 14), foreground="black", bg = "#D6C7B7")
idd=tk.Entry(W3, width=24, font=("Montserrat", 14))


tyL= tk.Label(W3, text="Type: ", font=("Montserrat", 14), foreground="black", bg = "#D6C7B7")
type=tk.Entry(W3, width=22, font=("Montserrat", 14))

nameL= tk.Label(W3, text="Name: ", font=("Montserrat", 14), foreground="black", bg = "#D6C7B7")
name=tk.Entry(W3, width=21, font=("Montserrat", 14))

prL= tk.Label(W3, text="Price: ", font=("Montserrat", 14), foreground="black", bg = "#D6C7B7")
price=tk.Entry(W3, width=22, font=("Montserrat", 14))


ad1 = tk.Button(W3, text="ADD", command=AddingItems)

def addItem():
    idL.place(x=230, y=300)
    idd.place(x=265, y=300)
    tyL.place(x=230, y= 330)
    type.place(x=285, y=330)
    nameL.place(x=230, y=360)
    name.place(x=295, y=360)
    prL.place(x=230, y= 390)
    price.place(x=285, y=390)
    ad1.place(x=330, y=450)



disp = tk.Button(W3, text="DONE", command=Display)
ll, d = None, None
d_labels = []
def displ():
    global ll, d, d_labels
    F = open('file.csv', 'r')
    l = csv.reader(F)
    j=350
    ll = tk.Label(W3, text="[ID, TYPE, NAME, PRICE]", font=("Montserrat", 14), foreground="black", bg="#D6C7B7")
    ll.place(x=230, y=280)
    for i, x in enumerate(l):
        y = x[0]+',  '+x[1]+',  '+x[2]+',  '+x[3]
        z = str(i+1) +'.  '+y
        d = tk.Label(W3, text=z, font=("Montserrat", 14), foreground="black", bg="#D6C7B7")
        d.place(x=240, y=j)    
        d_labels.append(d)
        j+=30
    disp.place(x=330, y=j+30)
    F.close()
    


seaButton, sId, seaID = None, None, None

sear = tk.Button(W3, text="DONE", command=SEARCH)
def search():
    global seaButton, seaID, sId
    seaButton = tk.Button(W3, text="Search by ID", command=search_by_id)
    sId= tk.Label(W3, text="Enter ID: ", font=("Montserrat", 14), foreground="black", bg = "#D6C7B7")
    seaID=tk.Entry(W3, width=24, font=("Montserrat", 14))
    sId.place(x=210, y=300)
    seaID.place(x=290, y=300)
    seaButton.place(x=330, y=390)

    
id_modified, id_input, modifyId = None, None, None
modd = tk.Button(W3, text="MODIFY", command=modify)

id_modified = tk.Label(W3, text="ID to be modified: ", font=("Montserrat", 14), foreground="black", bg = "#D6C7B7")
id_input = tk.Entry(W3, width=20, font=("Montserrat", 14))

def mod():
    global id_input, id_modified, modifyId
    
    id_modified.place(x=230, y=300)
    id_input.place(x=390, y=300)

    idL.place(x=230, y=300)
    idd.place(x=265, y=300)
    tyL.place(x=230, y= 330)
    type.place(x=285, y=330)
    nameL.place(x=230, y=360)
    name.place(x=295, y=360)
    prL.place(x=230, y= 390)
    price.place(x=285, y=390)
   
    
    modd.place(x=330, y=450)

    

#[id, name, price]
#search, accept, display, modify




#USER







W1.withdraw()
# W2.withdraw()
W3.withdraw()

W1.mainloop()
