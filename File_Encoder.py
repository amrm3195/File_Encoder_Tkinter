#Import the required Libraries
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import pyAesCrypt
import webbrowser
#Create an instance of Tkinter frame
loop= Tk()
#Set the geometry of Tkinter frame
loop.geometry("800x500")
#background color and text color
bgcol='#1B2631'
textcol='#FDFEFE'
#window title
loop.title(str("File Encoder"))
#sizable
loop.resizable(False,False)
#background color
loop.config(background=bgcol)
#icon
loop.iconbitmap("build\\icon.ico",)
################functins###############################################################################################################
#select files function
def selectfiles():
    finaltext.configure(text="")
    fr2=Frame(width=500,height=150,bg="#2E4053").place(relx=.5,rely=.45,anchor='center')
    destanse=0
    global more1
    global files
    files = filedialog.askopenfilenames()
    for file in files[0:7]:
        Label(fr2,text=file if len(file)<=85 else (file[0:85]+"..."),bg='#2E4053',fg=textcol,font=("helvetica",10)).place(x=150,y=150+destanse)
        destanse = destanse+20
    Button(fr2,text="Files\n"+str(len(files)),bg=bgcol,fg=textcol,font=("garamond",20),command=showfiles).place(x=690,y=175)
    if len(files)>7:
        more1=Label(fr2,text='more....',bg='#2E4053',fg=textcol,font=("helvetica",10))
        more1.focus_set()
        more1.place(x=150,y=295)
#encrypt function
def encrypt():
    global entery
    global confirm_button
    global show_button
    global showim
    global hideim
    hideim = PhotoImage(file="build\\close.png").subsample(20,20)
    showim = PhotoImage(file='build\\open.png').subsample(20,20)
    entery = Entry(loop, width=20, borderwidth=1,foreground="#17202A",font=('Arial',12,'bold'),show="●")
    entery.focus_set()
    entery.place(relx=.5,rely=.78,anchor="center")
    Label(loop,text=" Enter a password ",bg=bgcol,fg=textcol,font=("helvetica",10,'bold')).place(relx=.5,rely=.7,anchor='center')
    confirm_button = Button(loop, text="✓",bg='#148F77', fg=textcol,font=("helvetica",12,'bold'),command=confirm_encryption)
    confirm_button.focus_set()
    confirm_button.place(x=540,y=375)
    show_button=Button(loop,image=hideim,border=0,fg=textcol,bg=bgcol,font=("helvetica",12,'bold'),command=show)
    show_button.focus_set()
    show_button.place(x=500,y=375)
#decrypt function
def decrypt():
    global entery
    global confirm_button
    global show_button
    global showim
    global hideim
    hideim = PhotoImage(file="build\\close.png").subsample(20,20)
    showim = PhotoImage(file='build\\open.png').subsample(20,20)
    entery = Entry(loop, width=20, borderwidth=1,foreground="#17202A",font=('Arial',12,'bold'),show="●")
    entery.focus_set()
    entery.place(relx=.5,rely=.78,anchor="center")
    Label(loop,text="Enter the password",bg=bgcol,fg=textcol,font=("helvetica",10,'bold')).place(relx=.5,rely=.7,anchor='center')
    confirm_button = Button(loop, text="✓",bg='#148F77', fg=textcol,font=("helvetica",12,'bold'),command=confirm_decryption)
    confirm_button.focus_set()
    confirm_button.place(x=540,y=375)
    show_button=Button(loop,image=hideim,fg=textcol,bg=bgcol,border=0,font=("helvetica",12,'bold'),command=show)
    show_button.focus_set()
    show_button.place(x=500,y=375)
#confirm encryption button
def confirm_encryption():
    global successful
    global unsuccessful
    finaltext.configure(text="Encrypting...")
    successful = []
    unsuccessful = []
    all = []
    fr3 = Frame(width=500,height=150,bg="#2E4053").place(relx=.5,rely=.45,anchor='center')
    destanse = 0
    password = entery.get()
    for file in files:
        try:
            pyAesCrypt.encryptFile(file, file+".enc", password)
            os.remove(file)
            all.append(file)
            successful.append(file)
        except:
            all.append(file)
            unsuccessful.append(file)
    for file in all[0:7]:
        if file in successful:
            Label(fr3,text=file if len(file)<=50 else (file[0:50]+"...")+" ➤ Encrypted Successfully",bg='#2E4053',fg="#229954",font=("helvetica",10)).place(x=150,y=150+destanse)
            destanse = destanse+20
        elif file in unsuccessful:
            Label(fr3,text=file if len(file)<=42 else (file[0:42]+"...")+" ➤ Did not Encrypted Successfully",bg='#2E4053',fg="#CB4335",font=("helvetica",10)).place(x=150,y=150+destanse)
            destanse = destanse+20
        confirm_button.destroy()
        if len(all)>7:
            more1.destroy()
            more2=Label(fr2,text='more....',bg='#2E4053',fg=textcol,font=("helvetica",10)).place(x=150,y=295)
            successful_button=Button(loop,text="Successful: "+str(len(successful)),bg="#145A32",width=13,fg=textcol,font=("helvetica",12,'bold'),command=showfiles_successful)
            successful_button.focus_set()
            successful_button.place(relx=.91,rely=.6,anchor="center")
            unsuccessful_button=Button(loop,text="Unsuccessful: "+str(len(unsuccessful)),bg="#78281F",width=13,fg=textcol,font=("helvetica",12,'bold'),command=showfiles_unsuccessful)
            unsuccessful_button.focus_set()
            unsuccessful_button.place(relx=.91,rely=.7,anchor="center")
    try:
        successful_buttton.destroy()
    except:
        pass
    try:
        unsuccessful_button.destroy()
    except:
        pass
    #final text
    finaltext.configure(text="Done!")
#confirm decryption button
def confirm_decryption():
    global successful
    global unsuccessful
    finaltext.configure(text="Encrypting...")
    successful = []
    unsuccessful = []
    all = []
    fr3 = Frame(width=500,height=150,bg="#2E4053").place(relx=.5,rely=.45,anchor='center')
    destanse = 0
    password = entery.get()
    for file in files:
        try:
            pyAesCrypt.decryptFile(file, os.path.splitext(file)[0], password)
            os.remove(file)
            all.append(file)
            successful.append(file)
        except:
            all.append(file)
            unsuccessful.append(file)
    for file in all[0:7]:
        if file in successful:
            Label(fr3,text=file if len(file)<=50 else (file[0:50]+"...")+" ➤ Decrypted Successfully",bg='#2E4053',fg="#229954",font=("helvetica",10)).place(x=150,y=150+destanse)
            destanse = destanse+20
        elif file in unsuccessful:
            Label(fr3,text=file if len(file)<=42 else (file[0:42]+"...")+" ➤ Did not Decrypted Successfully",bg='#2E4053',fg="#CB4335",font=("helvetica",10)).place(x=150,y=150+destanse)
            destanse = destanse+20
        confirm_button.destroy()
        if len(all)>7:
            more1.destroy()
            more2=Label(fr2,text='more....',bg='#2E4053',fg=textcol,font=("helvetica",10)).place(x=150,y=295)
            successful_button=Button(loop,text="Successful: "+str(len(successful)),bg="#145A32",width=13,fg=textcol,font=("helvetica",12,'bold'),command=showfiles_successful)
            successful_button.focus_set()
            successful_button.place(relx=.91,rely=.6,anchor="center")
            unsuccessful_button=Button(loop,text="Unsuccessful: "+str(len(unsuccessful)),bg="#78281F",width=13,fg=textcol,font=("helvetica",12,'bold'),command=showfiles_unsuccessful)
            unsuccessful_button.focus_set()
            unsuccessful_button.place(relx=.91,rely=.7,anchor="center")
    try:
        successful_buttton.destroy()
    except:
        pass
    try:
        unsuccessful_button.destroy()
    except:
        pass
    #final text
    finaltext.configure(text="Done!")
#help button function
def i():
    global enexplain
    global arexplain
    global infotext
    global extext
    global arbutton
    loop2 = Tk()
    loop2.geometry("450x280")
    loop2.config(background=bgcol)
    loop2.title("Info")
    loop2.iconbitmap("build\\info.ico")
    loop2.resizable(False,False)
    fr3 = Frame(loop2,width=430,height=170,bg='#2C3E50').place(relx=.5,rely=.32,anchor="center")
    enexplain = "This program was made by Amr Mohamed\n\nIf you have any suggestions about my programme contact me\n\nThank you for using my programme"
    arexplain = "هذا البرنامج من إعداد عمرو محمد\n\nإذا كان لديك أي اقتراحات حول برنامجي اتصل بي\n\nشكرا لك على استخدام برنامجي"
    infotext = Label(loop2, text="INFO!",bg="#2C3E50",fg=textcol,font=('helvetica',17,"bold"))
    infotext.focus_set()
    infotext.place(relx=.5,rely=.1,anchor="center")
    extext = Label(loop2, text=enexplain,bg="#2C3E50",fg=textcol,font=('helvetica',12))
    extext.focus_set()
    extext.place(relx=.5,rely=.35,anchor="center")
    arbutton = Button(loop2,text="EN",font=("helvetica",10,"bold"),bg="#B3B6B7",fg="#0E6251",command=changetoar)
    arbutton.focus_set()
    arbutton.place(x=380,y=20)
    Label(loop2,text="Whatsapp: +201021949449\nTwitter: amrm3195\nInstagram: amrm3195\nGithub: amrm3195",bg="#2C3E50",fg=textcol,font=('helvetica',12)).place(relx=.5,rely=.83,anchor="center")
    #-----
    loop2.mainloop()
#change to ar
def changetoar():
    infotext.configure(text="!معلومات",font=('helvetica',19,"bold"))
    extext.configure(text=arexplain,font=('helvetica',13))
    arbutton.configure(text="AR",fg="#78281F",command=changetoen)
#change to en
def changetoen():
    infotext.configure(text="INFO!",font=('helvetica',17,"bold"))
    extext.configure(text=enexplain,font=('helvetica',12))
    arbutton.configure(text="EN",fg="#0E6251",command=changetoar)
#showfiles button function
def showfiles():
    showfilestk = Tk()
    showfilestk.title("Files Selected")
    showfilestk.iconbitmap("build\\documents.ico")
    showfilestk.geometry("300x400")
    showfilestk.resizable(False,False)
    showfilestk.config(background=bgcol)
    destanse = 0
    showfileslist = Listbox(showfilestk,bg="#2E4053",fg="white",width=43,height=23)
    for file in files:
        showfileslist.insert(destanse,str(destanse+1)+': '+file)
        destanse+=1
    showfileslist.place(relx=.5,rely=.5,anchor="center")
#show successful files
def showfiles_successful():
    showfilestk_successful = Tk()
    showfilestk_successful.title("Successful files")
    showfilestk_successful.iconbitmap("build\\accept.ico")
    showfilestk_successful.geometry("300x400")
    showfilestk_successful.resizable(False,False)
    showfilestk_successful.config(background=bgcol)
    destanse = 0
    showfileslist = Listbox(showfilestk_successful,bg="#2E4053",fg="#229954",width=43,height=23)
    for file in successful:
        showfileslist.insert(destanse,str(destanse+1)+': '+file)
        destanse+=1
    showfileslist.place(relx=.5,rely=.5,anchor="center")
#show unsuccessful files
def showfiles_unsuccessful():
    showfilestk_unsuccessful = Tk()
    showfilestk_unsuccessful.title("Unsuccessful files")
    showfilestk_unsuccessful.iconbitmap("build\\cross.ico")
    showfilestk_unsuccessful.geometry("300x400")
    showfilestk_unsuccessful.resizable(False,False)
    showfilestk_unsuccessful.config(background=bgcol)
    destanse = 0
    showfileslist = Listbox(showfilestk_unsuccessful,bg="#2E4053",fg="#CB4335",width=43,height=23)
    for file in unsuccessful:
        showfileslist.insert(destanse,str(destanse+1)+': '+file)
        destanse+=1
    showfileslist.place(relx=.5,rely=.5,anchor="center")
#show password
def show():
    entery.configure(show="")
    show_button.config(command=hide,image=showim)
#hide password
def hide():
    entery.configure(show="●")
    show_button.config(command=show,image=hideim)
#######################################################################################################################################
##dark frame
fr1=Frame(width=1300,height=51,bg="#17202A").place(x=0,y=0)
#black frame
dframe = Frame(width=10,height=51,bg="#080B0F").place(x=0,y=0)
#frame Title
Label(fr1,text="File Encoder",bg='#17202A',fg='white',font=('Georgia',25)).place(x=10,y=3)
#frame photo
photo1 = PhotoImage(file="build\\photo.png").subsample(11,11)
Label(fr1, image=photo1,bg='#17202A').place(x=205, y=0)
##
#photo2
photo2 = PhotoImage(file='build\\photo2.png').subsample(3,3)
Label(loop, image=photo2,bg=bgcol).place(relx=.5, rely=.191, anchor="center")
#text: choose your files
Label(loop, text="Select files:",bg=bgcol,fg=textcol,font=('helvetica',14)).place(x=20, y=160)
#files frame
fr2=Frame(width=500,height=150,bg="#2E4053").place(relx=.5,rely=.45,anchor='center')
#select files button
Button(loop,text='Select',bg='#626567',fg=textcol,font=("helvetica",12,'bold'),command=selectfiles).place(x=42,y=200)
#encrypt button
Button(loop, text="Encrypt",bg='#626567',fg=textcol,font=("helvetica",15,'bold'),command=encrypt).place(relx=.25,rely=.635)
#decrypt button
Button(loop, text="Decrypt",bg='#626567',fg=textcol,font=("helvetica",15,'bold'),command=decrypt).place(relx=.64,rely=.635)
#help button
Button(fr1, text="!",bg='#212F3C',fg=textcol,width=2,font=("helvetica",12,'bold'),command=i).place(x=760,y=10)
#facebook
facebook = PhotoImage(file = "build\\facebook.png").subsample(20,20)
Button(loop,image=facebook,bg=bgcol,border=0,command=lambda:webbrowser.open("https://www.facebook.com/profile.php?id=100071782627971")).place(relx=.95,rely=.92)
#insta
insta = PhotoImage(file = "build\\insta.png").subsample(20,20)
Button(loop,image=insta,bg=bgcol,border=0,command=lambda:webbrowser.open("https://www.instagram.com/amrm3195/")).place(relx=.9,rely=.92)
#twitter
twitter = PhotoImage(file = "build\\twitter.png").subsample(20,20)
Button(loop,image=twitter,bg=bgcol,border=0,command=lambda:webbrowser.open("https://twitter.com/amrm3195")).place(relx=.85,rely=.92)
#whatsapp
whatsapp = PhotoImage(file = "build\\whatsapp.png").subsample(20,20)
Button(loop,image=whatsapp,bg=bgcol,border=0,command=lambda:webbrowser.open("https://wa.me/qr/CSJRQ6W4V56YM1")).place(relx=.8,rely=.92)
#github
github = PhotoImage(file = "build\\github.png").subsample(20,20)
Button(loop,image=github,bg=bgcol,border=0,command=lambda:webbrowser.open("https://github.com/amrm3195")).place(relx=.75,rely=.92)
#final text
finaltext = Label(loop,text="",bg=bgcol,fg=textcol,font=("helvetica",12,'bold'))
finaltext.focus_set()
finaltext.place(relx=.5,rely=.9,anchor="center")
#my name
Label(loop, text="Made by\nAmr Mohamed",bg=bgcol,fg=textcol,font=("Brush Script MT",20)).place(relx=.1,rely=.90,anchor="center")
#version
Label(loop, text="v1.1.4",bg=bgcol,fg=textcol,font=("Arial Narrow",15,"bold")).place(relx=.7,rely=.95,anchor="center")

loop.mainloop()