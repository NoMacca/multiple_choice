import tkinter
from tkinter import filedialog
from tkinter import *



tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

folder_path = filedialog.askdirectory()

print(folder_path)

file_path= filedialog.askopenfilename()

print(file_path)

def get_file_path():
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
    l1 = Label(window, text = "File path: " + file_path).pack()

window = tkinter.Tk()
# Creating a button to search the file
b1 = Button(window, text = "Open File", command = get_file_path).pack()
window.mainloop()
