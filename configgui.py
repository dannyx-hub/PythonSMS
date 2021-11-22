import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox 
from tkinter import filedialog
from config import JSONimport

class App:
    def __init__(self, root):
        #setting title
        root.title("PythonSMS")
        #setting window size
        width=382
        height=235
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.configure(bg="#3b3b39")
        root.resizable(width=False, height=False)
        config = JSONimport()
        print(config)

        GLabel_460=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_460["font"] = ft
        GLabel_460["fg"] = "#babab8"
        GLabel_460["justify"] = "center"
        GLabel_460["text"] = "ADB path:"
        GLabel_460['bg'] = "#3b3b39"
        GLabel_460.place(x=100,y=20,width=165,height=30)

        # self.GLineEdit_765=tk.Entry(root)
        # self.GLineEdit_765["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times',size=10)
        # self.GLineEdit_765["font"] = ft
        # self.GLineEdit_765["fg"] = "#babab8"
        # self.GLineEdit_765["justify"] = "center"
        # self.GLineEdit_765["text"] = "Entry"
        # self.GLineEdit_765['bg'] = "#3b3b39"
        # self.GLineEdit_765.place(x=50,y=70,width=276,height=30)
        GLabel_461=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_461["font"] = ft
        GLabel_461["fg"] = "#babab8"
        GLabel_461["justify"] = "center"
        GLabel_461["text"] = config
        GLabel_461['bg'] = "#3b3b39"
        GLabel_461.place(x=50,y=70,width=276,height=30)


        # self.GMessage_588=tk.Message(root)
        # self.GMessage_588["anchor"] = "center"
        # ft = tkFont.Font(family='Times',size=10)
        # self.GMessage_588["font"] = ft
        # self.GMessage_588["fg"] = "#babab8"
        # self.GMessage_588['bg'] = "#3b3b39"
        # # self.GMessage_588["justify"] = "center"
        # self.GMessage_588["text"] = config
        # self.GMessage_588.place(x=50,y=70,width=276,height=30)


        GButton_508=tk.Button(root)
        GButton_508["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_508["font"] = ft
        GButton_508["fg"] = "#000000"
        GButton_508["justify"] = "center"
        GButton_508["text"] = "Change"
        GButton_508.place(x=130,y=150,width=116,height=43)
        GButton_508["command"] = self.GButton_508_command

    def GButton_508_command(self):
        import json
        import sys
        select=filedialog.askdirectory()
        tkinter.messagebox.showinfo(title="PythonSMS", message=select)
        with open("config.json","w") as configfile:
            self.data = {
            "path":f"{select}"
            }
            json.dump(self.data,configfile)
            tkinter.messagebox.showinfo(title="PythonSMS", message="ADB path updated")
        sys.exit(1)

        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
