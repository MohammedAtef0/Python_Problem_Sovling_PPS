import tkinter
import tkinter.messagebox
class CurrencyConverter:
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()
        #write a title on the main window widget
        self.main_window.title("Currency Converter")
        #create a frame for converting from dollar to egp
        self.TopFrame = tkinter.Frame(self.main_window)
        #create a frame for converting from kwd to egp
        self.MiddleFrame = tkinter.Frame(self.main_window)
        #create a bottom frame for converting from egp to dollar
        self.BottomFrame = tkinter.Frame(self.main_window)
        #creating three lables for each frame for telling the user which Currency to convert
        self.label1 = tkinter.Label(self.TopFrame, text = 'From Dollar to EGP' ,borderwidth= 2 , relief= 'raised')
        self.label2 = tkinter.Label(self.MiddleFrame, text='From KWD to EGP' , borderwidth=3 , relief='sunken')
        self.label3 = tkinter.Label(self.BottomFrame, text='From EGP to Dollar' , borderwidth=3 , relief='sunken')
        #use the pack method with its arguments to make make the labels visible
        self.label1.pack(side='left' , ipadx=50 , ipady=50)
        self.label2.pack(side='left' , ipadx=50 , ipady=50)
        self.label3.pack(side='left' , ipadx=50, ipady=50)
        self.TopFrame.pack()
        self.MiddleFrame.pack()
        self.BottomFrame.pack()
        #creating text areas to take inputs from the user
        self.D_Entry = tkinter.Entry(self.TopFrame, width=15)
        self.D_Entry.pack(side='top')
        self.KWD_Entry = tkinter.Entry(self.MiddleFrame, width=15)
        self.KWD_Entry.pack(side='top')
        self.EGP_Entry = tkinter.Entry(self.BottomFrame, width=15)
        self.EGP_Entry.pack(side='top')
        #creating the convert button and the exit button
        self.D_Button = tkinter.Button(self.TopFrame,text='Convert!', command=self.DollarToEgp)
        self.Exit_Button = tkinter.Button(self.TopFrame,text='Exit!',command=self.TopFrame.destroy)
        self.D_Button.pack()
        self.Exit_Button.pack()
        #----------------------------
        self.KWD_Button = tkinter.Button(self.MiddleFrame, text='Convert!', command=self.KWDToEgp)
        self.Exit_Button = tkinter.Button(self.MiddleFrame, text='Exit!', command=self.MiddleFrame.destroy)
        self.KWD_Button.pack()
        self.Exit_Button.pack()
        #---------------------------
        self.EGP_Button = tkinter.Button(self.BottomFrame, text='Convert!', command=self.EGPToDollar)
        self.Exit_Button = tkinter.Button(self.BottomFrame, text='Exit!', command=self.BottomFrame.destroy)
        self.EGP_Button.pack()
        self.Exit_Button.pack()
        #Calling the main loop method for doing the main frame of the GUI
        tkinter.mainloop()
    def DollarToEgp(self):
        Dollar = float(self.D_Entry.get()) * 27.68
        print(Dollar)
        tkinter.messagebox.showinfo('From EGP to Dollar', Dollar)
    def KWDToEgp(self):
        KWD = float(self.KWD_Entry.get()) * 90.49
        print(KWD)
        tkinter.messagebox.showinfo('From EGP to Dollar', KWD)
    def EGPToDollar(self):
        EGP = round(float(self.EGP_Entry.get()) * 0.036 , 2)
        print(EGP)
        tkinter.messagebox.showinfo('From EGP to Dollar' , EGP)
#make an instance from the Currency Converter class 
CC = CurrencyConverter()
