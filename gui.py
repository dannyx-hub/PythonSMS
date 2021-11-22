from logging import error
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
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
        root.configure(bg="#3b3b39")
        root.resizable(width=False, height=False)

        #message box to set status

        self.GMessage_588=tk.Message(root)
        self.GMessage_588["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=16)
        self.GMessage_588["font"] = ft
        self.GMessage_588["fg"] = "#babab8"
        self.GMessage_588['bg'] = "#3b3b39"
        self.GMessage_588["justify"] = "center"
        self.GMessage_588["text"] = ""
        self.GMessage_588.place(x=0,y=360,width=598,height=137)

        #Entry to phone number

        self.GLineEdit_510=tk.Entry(root)
        self.GLineEdit_510["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_510["font"] = ft
        self.GLineEdit_510["fg"] = "#333333"
        self.GLineEdit_510["justify"] = "center"
        self.GLineEdit_510["text"] = ""
        self.GLineEdit_510['bg'] = "#858585"
        self.GLineEdit_510.place(x=160,y=110,width=290,height=40)

        #Entry to write message content

        self.GLineEdit_972=tk.Entry(root)
        self.GLineEdit_972["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_972["font"] = ft
        self.GLineEdit_972["fg"] = "#333333"
        self.GLineEdit_972["justify"] = "center"
        self.GLineEdit_972["text"] =  ""
        self.GLineEdit_972['bg'] = "#858585"
        self.GLineEdit_972.place(x=160,y=220,width=290,height=40)

        GLabel_949=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_949["font"] = ft
        GLabel_949["fg"] = "#babab8"
        GLabel_949["justify"] = "center"
        GLabel_949["text"] = "Phone Number"
        GLabel_949['bg'] = "#3b3b39"
        GLabel_949.place(x=170,y=60,width=270,height=25)

        GLabel_420=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_420["font"] = ft
        GLabel_420["fg"] = "#babab8"
        GLabel_420["justify"] = "center"
        GLabel_420["text"] = "Message"
        GLabel_420['bg'] = "#3b3b39"
        GLabel_420.place(x=170,y=180,width=270,height=25)

        GButton_108=tk.Button(root)
        GButton_108["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_108["font"] = ft
        GButton_108["fg"] = "#000000"
        GButton_108["justify"] = "center"
        GButton_108["text"] = "Send"
        GButton_108['bg'] = "#858585"
        GButton_108.place(x=100,y=290,width=96,height=71)
        GButton_108["command"] = self.GButton_108_command

        GButton_692=tk.Button(root)
        GButton_692["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_692["font"] = ft
        GButton_692["fg"] = "#000000"
        GButton_692["justify"] = "center"
        GButton_692["text"] = "Configuration"
        GButton_692['bg'] = "#858585"
        GButton_692.place(x=390,y=290,width=96,height=71)
        GButton_692["command"] = self.GButton_692_command

    def GButton_108_command(self):
        from adbgui import main
        self.number = self.GLineEdit_510.get()
        self.msg = self.GLineEdit_972.get()
        if len(self.number) != 0 and len(self.msg) != 0:
            try:
                self.adb = main(self.number,self.msg)
                self.GMessage_588.configure(text=f"{self.msg}. Message send successfull")
                tkinter.messagebox.showinfo(title="PythonSMS", message="message send successfull")
            except Exception as e:
                self.GMessage_588.configure(text="something gone wrong, check connection, config file and run again",color="red")
                tkinter.messagebox.showerror(title="PythonSMS", message=f"{e}")
        else:
            tkinter.messagebox.showinfo(title="PythonSMS", message="you must add number and message")
            self.GMessage_588.configure(text="something gone wrong, check connection, config file and run again")
    def GButton_692_command(self):
        import os
        os.popen("python configgui.py")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
