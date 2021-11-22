import tkinter as tk

def createNewWindow(self):
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "insert path to adb")
    self.GLineEdit_510=tk.Entry(newWindow)
    self.GLineEdit_510["borderwidth"] = "1px"
    self.GLineEdit_510["fg"] = "#333333"
    self.GLineEdit_510["justify"] = "center"
    self.GLineEdit_510["text"] = "please enter your phone number"
    self.GLineEdit_510.place(x=160,y=110,width=290,height=40)
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    self.GLineEdit_510.pack()
    buttonExample.pack()
def safetoconfig(self):
    self.GLineEdit_510.get()
    return
app = tk.Tk()
buttonExample = tk.Button(app, 
              text="Create new window",
              command=safetoconfig)
buttonExample.pack()

app.mainloop()