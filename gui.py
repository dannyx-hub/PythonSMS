import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("PythonSMS")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GLineEdit_220=tk.Entry(root)
        self.GLineEdit_220["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_220["font"] = ft
        self.GLineEdit_220["fg"] = "#333333"
        self.GLineEdit_220["justify"] = "center"
        # self.GLineEdit_220["text"] = "Entry"
        self.GLineEdit_220.place(x=0,y=80,width=358,height=35)
        # self.GLineEdit_220["show"] = "text"

        self.GLineEdit_3=tk.Entry(root)
        self.GLineEdit_3["borderwidth"] = "1px"
        self.GLineEdit_3["fg"] = "#333333"
        self.GLineEdit_3['justify'] = 'center'
        self.GLineEdit_3.place(x=0,y=150,width=357,height=38)



        GLabel_132=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_132["font"] = ft
        GLabel_132["fg"] = "#333333"
        GLabel_132["justify"] = "center"
        GLabel_132["text"] = "numer telefonu"
        GLabel_132.place(x=10,y=40,width=152,height=30)

        GLabel_484=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_484["font"] = ft
        GLabel_484["fg"] = "#333333"
        GLabel_484["justify"] = "center"
        GLabel_484["text"] = "tresc wiadomosci"
        GLabel_484.place(x=0,y=120,width=163,height=30)

        self.GMessage_236=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GMessage_236["font"] = ft
        self.GMessage_236["fg"] = "#333333"
        self.GMessage_236["justify"] = "center"
        self.GMessage_236["text"] = "Message"
        self.GMessage_236.place(x=120,y=360,width=355,height=113)

        GButton_899=tk.Button(root)
        GButton_899["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_899["font"] = ft
        GButton_899["fg"] = "#000000"
        GButton_899["justify"] = "center"
        GButton_899["text"] = "wyślij"
        GButton_899.place(x=170,y=220,width=239,height=70)
        GButton_899["command"] = self.GButton_899_command

    def GButton_899_command(self):
        from adbgui import main
        self.temp = self.GLineEdit_220.get()
        self.temp2 = self.GLineEdit_3.get()
        self.adb = main(self.temp,self.temp2)
        self.GMessage_236.set(self.adb)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
