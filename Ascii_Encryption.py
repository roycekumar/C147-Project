from tkinter import *
root=Tk()
root.title("Encryption with Ascii Code")

root.geometry("400x400")
root.configure(background='light blue')

enter_word=Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label=Label(root,text="Name in Ascii : ",bg="#d9fefe",fg="black")
label1=Label(root,text="Encrypted Name : ",bg="#d9fefe",fg="black")
def asciiConverter():
    label['text']="Name in Ascii : "
    label1['text']="Encrypted Name : "
    input_word=enter_word.get()
    for letter in input_word:
        encrypted=ord(letter)-1
        label['text']+=str(ord(letter))+" "
        label1['text']+=chr(encrypted)
        
btn=Button(root,text="Display the Ascii Code and Encrypted value",command=asciiConverter,bg="#4169df",fg="white")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)
label1.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()