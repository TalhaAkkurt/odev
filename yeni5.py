import tkinter as tk 

menu = tk.Tk()
menu.title("selam")
menu.geometry("800x600")

yazi=tk.Label(text="araba markası")
yazi.place(x=10 , y=10)

x= tk.StringVar()
giris=tk.Entry(textvariable=x)
giris.place(x=100 , y=10)

yazi2=tk.Label(text="Kaç cc")
yazi2.place(x=10 , y=30)

y= tk.StringVar()
giris=tk.Entry(textvariable=y)
giris.place(x=100 , y=30)


yazi3=tk.Label(text="Kaç yaşında")
yazi3.place(x=10 , y=50)

z= tk.StringVar()
giris=tk.Entry(textvariable=z)
giris.place(x=100 , y=50)

mtv=150

def vergi():
    if(y<=1000 and z<5):
        print(mtv +1750)
    elif(y<=1600 and z<5):
        print(mtv+1850)
    elif(y<=2000 and z<5):
        print(mtv+1950)
    elif (y<=1000 and z<10):
        print(mtv +1250)
    elif(y<=1600 and z<10):
        print(mtv+1350)
    elif(y<=2000 and z<10):
        print(mtv+1450)
    elif (y<=1000 and z<15):
        print(mtv+750)
    elif(y<=1600 and z<15):
        print(mtv+850)
    elif(y<=2000 and z<15):
        print(mtv+950)

if(x=="seat" and y==2000 and z<5):
    yazı4 = tk.Label(text="Vergi almıyom senden 5 para etmez")
    yazı4.place(x=200, y=200)
elif(x=="mersedes" and y==2000 and z<5):
    print(mtv*1)
elif(x=="bmv" and y==2000 and z<5):
    print(mtv*1)    

buton=tk.Button(command=vergi, text="Hesapla")
buton.place(x=400, y=300)







menu.mainloop()