import tkinter as tk 
import tkinter.font as tkFont
from adbgui import main

class App:
    global tn, mg
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

        tel=tk.Entry(root)
        tel["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        tel["font"] = ft
        tel["fg"] = "#333333"
        tel["justify"] = "center"
        tel["text"] = "Entry"
        tel.place(x=60,y=70,width=460,height=30)
        tel["show"] = "text"
        global tn  
        tn = tel.get()
        
        msg=tk.Entry(root)
        msg["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        msg["font"] = ft
        msg["fg"] = "#333333"
        msg["justify"] = "center"
        msg["text"] = "Entry"
        msg["relief"] = "flat"
        msg.place(x=60,y=160,width=464,height=138)
        msg["show"] = "text"
        global mg
        mg = msg.get()
        
        
        button=tk.Button(root)
        button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        button["font"] = ft
        button["fg"] = "#000000"
        button["justify"] = "center"
        button["text"] = "Button"
        button.place(x=180,y=340,width=199,height=65)
        button["command"] = self.button_command

        GMessage_956=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_956["font"] = ft
        GMessage_956["fg"] = "#333333"
        GMessage_956["justify"] = "center"
        GMessage_956["text"] = "Message"
        GMessage_956.place(x=130,y=450,width=298,height=35)

    def button_command(self):
        print(mg)
        # self.GMessage_956.set(main(tel,msg))
    def main(self):
        self.GMessage_956.set("test")

if __name__ == "__main__":
    from adb import main
    root = tk.Tk()
    app = App(root)
    root.mainloop()
