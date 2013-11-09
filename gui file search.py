# A GUI search program using TK
# Based on script by David Briddock
# http://davidbriddock.blogspot.com/2013/04/learn-python-gui-file-search-app.html

from Tkinter import *
import os


# initialise main window
def init(win):
    win.title("File Search")

    labelPath.grid(row=0, column=0, sticky="W")
    entryPath.grid(row=1, column=0)
    labelEnding.grid(row=2, column=0, sticky="W")
    entryEnding.grid(row=0, column=1)
    #btnSearch.grid(row=0, column=1, sticky="W")
    fileList.grid(row=1, column=1, rowspan=5)
    yscroll.grid(row=1, column=2, rowspan=5, sticky="NS")

    fileList.configure(yscrollcommand=yscroll.set)
    yscroll.configure(command=fileList.yview)
    # Replace this with radio buttons
    entryPath.insert(INSERT, "/home")
    entryEnding.insert(INSERT, "")


# find button callback
def search():
    # get start directory and file ending
    start_dir = entryPath.get()
    letter_number = entryEnding.get()

    # clear the listbox
    fileList.delete(0, END)

    # find matching file and fill listbox
    for file_name in os.listdir(start_dir):
        if letter_number in file_name:
            fileList.insert(END, start_dir + "\\" + file_name)

# create top-level window object
win = Tk()

# create widgets
# Replace this with radio buttons
labelPath = Label(win, text="Starting Path")
entryPath = Entry(win, width=12)
labelEnding = Label(win, text="File Ending")
entryEnding = Entry(win, width=12)
fileList = Listbox(win, width=80, height=20)
yscroll = Scrollbar(win, orient=VERTICAL)
#btnSearch = Button(win, text="Search", width=8, command=search)


def enter(event):  # makes search box search when you hit ENTER
    search()


entryEnding.bind('<Return>', enter)


# Testing the action of clicking a filename
# This prints the position number of the filename on the list.
def launch_file(e):
    test_result = fileList.curselection()
    print(fileList.get(test_result))
    os.startfile(fileList.get(test_result))
fileList.bind('<<ListboxSelect>>', launch_file)

# initialise and run main loop
entryEnding.focus_set()
init(win)
mainloop()
