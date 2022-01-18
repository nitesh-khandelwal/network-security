from tkinter import *
class MyWindow:
    def __init__(self, win):
        #Encipher button will be created
        self.btn=Button(window, text="Encipher", bg='white',fg='blue')
        self.b1=Button(win, text='Encipher', command=self.plain_to_cipher)
        self.b1.place(x=100, y=250)
        
        #Decipher button will be created
        self.btn=Button(window, text="Decipher", bg='white',fg='blue')
        self.b1=Button(win, text='Decipher', command=self.cipher_to_plain)
        self.b1.place(x=400, y=250)
        
        #Label Plain text that can be seen above text box will be created
        self.lbl1=Label(window, text="PLAIN TEXT", fg='black', font=("Helvetica", 12))
        self.lbl1.place(x=60, y=50)
        
        #Label Cipher text that can be seen above 2nd text box will be created
        self.lbl2=Label(window, text="CIPHER TEXT", fg='black', font=("Helvetica", 12))
        self.lbl2.place(x=350, y=50)
        
        #First text box will be created
        self.txtfld1=Entry(window, text="Enter your text here", bd=5)
        self.txtfld1.place(x=60, y=80,width=200,height=100)
        
        #second text box will be created
        self.txtfld2=Entry(window, text="Result", bd=5)
        self.txtfld2.place(x=350, y=80,width=200,height=100)
        
        
    def plain_to_cipher(self):
        self.txtfld2.delete(0, 'end')#This will clear the text field containg plain text
        string=self.txtfld1.get()
        result=""
        for i in range(len(string)):
            char=string[i]
            b=ord(char) #ord function changes that char to its corresponding ASCII value
            #To change upper alphabetic characters
            if(char.isupper()):
                a=155-b
                result+=chr(a) #chr function changes ASCII value to its corresponding character
            #To change lower alphabetic characters 
            elif(char.islower()):
                a=219-b
                result+=chr(a)
            #To add other special characters as it is
            else:
                result+=chr(b)
        self.txtfld2.insert(END,result)
        
#Function to change Cipher text to plain text        
    def cipher_to_plain(self):
        self.txtfld1.delete(0,'end') #This will clear the text field containg plain text
        string=self.txtfld2.get()
        result=""
        for i in range(len(string)):
            char=string[i]
            b=ord(char)
            #To change upper alphabetic characters
            if(char.isupper()):
                a=155-b
                result+=chr(a)
            #To change lower alphabetic characters 
            elif(char.islower()):
                a=219-b
                result+=chr(a)
            #To add other special characters as it is
            else:
                result+=chr(b)
        self.txtfld1.insert(END,result)
                
        
        

window=Tk()
mywin=MyWindow(window)
window.title('Plain text <----> Cipher text') #Title of the window created
window.geometry("600x300+300+200") #Size of the window created
window.mainloop()