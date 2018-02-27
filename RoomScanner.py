# RoomScanner Main Application Script

import sys

import tkinter as tk #tkinter is for the GUI.
import tkinter.filedialog as fdialog

class RoomScanner(tk.Frame):
    def __init__(self, master=None, debug=False):
        tk.Frame.__init__(self, master)

        #Debug mode?
        self.debug = debug

        self.grid()
        self.createView()
        self.focus()

    def createView(self):
        self.uploadButton = tk.Button(
            self,
            text='Open an Image Directory',
            command=self.selectImage
        )
        self.uploadButton.grid()

        self.quitButton = tk.Button(
            self,
            text='Quit',
            command=self.quitApplication
        )
        self.quitButton.grid()
    def selectImage(self):
        path = fdialog.askdirectory()

        self.text = path
        self.uploadButton.config(state='disabled')

    def quitApplication(self):
        # do any cleanup
        exit(0)

try:
    sys.argv.index('-debug')
    d = True
    print('debugmode true')
except ValueError:
    d = False

app = RoomScanner(debug=d)
app.master.title('RoomScanner')
app.mainloop()
