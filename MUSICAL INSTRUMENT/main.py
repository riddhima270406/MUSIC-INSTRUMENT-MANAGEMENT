import tkinter as tk
from tkinter import messagebox
import csv
import os
import io
import requests
from PIL import ImageTk, Image


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
8
window2 = tk.Toplevel()
window2.configure(bg="#D6C7B7")
window2.geometry("700x700")
window2.withdraw()

window3 = tk.Toplevel()
window3.configure(bg="#D6C7B7")
window3.geometry("700x700")
window3.withdraw()




def go_back(window1, W2, backG):
    window1.withdraw()
    W2.deiconify()
    backG.destroy()

def gBack():
    go_back(window1, W1, backG)

def pBack():
    go_back(window2, W1, backP)

def dBack():
    go_back(window3, W1, backD)


def on_click(W2, W1):
    W2.destroy()
    W1.deiconify()

def w1():
    on_click(W2, W1)

def w2():
    on_click(W2, W3)


# window1 (guitar) ELEMENTS
backG= tk.Button(window1, text="Back", command= gBack, bg="#D6C7B7", relief="flat", font=("Montserrat", 20))
backG.pack()

# window2 (piano) ELEMENTS
backP = tk.Button(window2, text="Back", command= pBack, bg="#D6C7B7", relief="flat", font=("Montserrat", 20))
backP.pack()

# window3 (drums) ELEMENTS
backD = tk.Button(window3, text="Back", command= dBack, bg="#D6C7B7", relief="flat", font=("Montserrat", 20))
backD.pack()


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
text_label = tk.Label(W1, text="Hello, World!", fg="#594030", bg="#D6C7B7")
text_label.pack()

img_path1 = ".\guitar\guitar_icon.png"  
img_g = tk.PhotoImage(file=img_path1)
img_g_button = tk.Button(W1, width=200, height=200, image=img_g, command=img_guitar, bg="#D6C7B7", relief="flat")
img_g_button.place(x=38, y=48)

img_path2 = ".\piano\piano_icon.png"  
img_p = tk.PhotoImage(file=img_path2)
img_p_button = tk.Button(W1, width=200, height=200, image=img_p, command=img_piano, bg="#D6C7B7", relief="flat")
img_p_button.place(x= 240, y=255)

img_path3 = ".\drums\drums_icon.png"  
img_d = tk.PhotoImage(file=img_path3)
img_d_button = tk.Button(W1, width=200, height=200, image=img_d, command=img_drums, bg="#D6C7B7", relief="flat")
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
            img = imgg.get()

            l =[i, t, n, p, img]

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
            imgL.place_forget()
            imgg.place_forget()
            imgg.delete(0, tk.END)
            ad1.place_forget()

    else:
        messagebox.showerror('ERROR', 'Please enter price properly.')


def Display():
    ll.destroy()
    disp.place_forget()
    for label in d_labels:
        label.destroy()

def img_url(image_url, il, x, y):
    response = requests.get(image_url)
    img_data = response.content
    img = Image.open(io.BytesIO(img_data))
    img = img.resize((x,y))  # Adjust the size as needed
    img_tk = ImageTk.PhotoImage(img)
    il.configure(image=img_tk)
    il.image = img_tk


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
            y = 'Id: '+x[0]+'\nName: '+x[1]+'\nType: '+x[2]+'\nPrice: ₹'+x[3]+'\n Image URL: '+x[4]
            im = tk.Label(W3)
            im.place(x= 300, y= 500)
            img_url(x[4], im, 300, 300)
            s = tk.Label(W3, text=y, font=("Montserrat", 15), foreground="black", bg="#D6C7B7")
            s.place(x=260, y=360)
            seaButton.destroy()
            sear.place(x=330, y=500)
    if search_id not in ids: 
        messagebox.showerror("ID DOESN'T EXIST", "There is no such id!")
    F.close()
    


def modify():
    pass


    
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

imgL= tk.Label(W3, text="Image URL: ", font=("Montserrat", 14), foreground="black", bg = "#D6C7B7")
imgg=tk.Entry(W3, width=17, font=("Montserrat", 14))

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
    imgL.place(x=230, y=420)
    imgg.place(x=340, y=420)
    ad1.place(x=330, y=450)



disp = tk.Button(W3, text="DONE", command=Display)
ll, d = None, None
d_labels = []
def displ():
    global ll, d, d_labels
    F = open('file.csv', 'r')
    l = csv.reader(F)
    j=350
    ll = tk.Label(W3, text="[ID, TYPE, NAME, PRICE, IMAGE URL]", font=("Montserrat", 14), foreground="black", bg="#D6C7B7")
    ll.place(x=230, y=280)
    for i, x in enumerate(l):
        y = x[0]+', '+x[1]+', '+x[2]+', '+x[3]+', '+x[4]
        z = str(i+1) +'. '+y
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

def mod():
    global id_input, id_modified, modifyId

    F = open('file.csv', 'r')
    A = open('t.csv', 'w', newline='')
    id_modified = tk.Label(W3, text="ID to be modified: ", font=("Montserrat", 14), foreground="black", bg = "#D6C7B7")
    id_input = tk.Entry(W3, width=20, font=("Montserrat", 14))
    modifyId = id_input.get()
    w = csv.writer(A)
    l = csv.reader(F)
    for r in l :
        if r[0] == modifyId:
            tyL.place(x=230, y= 330)
            type.place(x=285, y=330)
            nameL.place(x=230, y=360)
            name.place(x=295, y=360)
            prL.place(x=230, y= 390)
            price.place(x=285, y=390)
            imgL.place(x=230, y=420)
            imgg.place(x=340, y=420)
            t = [id_modified , type.get(), name.get(), price.get(), imgg.get()]
            w.writerow(t)
        else:
            w.writerow(r)
    F.close()
    A.close()
    os.remove('file.csv')
    os.rename('t.csv', 'file.csv')

#[id, name, price, img]
#search, accept, display, modify






W1.withdraw()
W2.withdraw()
# W3.withdraw()

W1.mainloop()