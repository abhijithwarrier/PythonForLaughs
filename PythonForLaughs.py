# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO GENERATE ONE-LINE JOKES FOR PROGRAMMERS USING pyjokes LIBRARY
#
# Python supports creation of random jokes using one of its libraries. Pyjokes is a python
# library that is used to create one-line jokes for programmers. You can get funny one-liner,
# mostly related to programming. This is a fun python library. It returns a random joke from
# the given category in the given language.
#
# The module can be installed using the command - pip install pyjokes

# Importing necessary packages
import pyjokes
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Making the lists of languages and categories.
langList = ['en', 'de', 'es', 'gl', 'it', 'eu']
categList = ['neutral', 'chuck', 'all']

# Defining CreateWidgets() to create necessary widgets for the GUI
def CreateWidgets():
    langLabel = Label(root, text="LANGUAGES : ", bg="darkolivegreen")
    langLabel.grid(row=1, column=0, padx=5, pady=5)
    root.langCombo = ttk.Combobox(root, width=15, values=langList)
    root.langCombo.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    root.langCombo.set("SELECT LANGUAGE")

    categLabel = Label(root, text="CATEGORIES : ", bg="darkolivegreen")
    categLabel.grid(row=1, column=2, padx=5, pady=8)
    root.categCombo = ttk.Combobox(root, width=15, values=categList, exportselection=False)
    root.categCombo.grid(row=2, column=2, columnspan=2, padx=5, pady=8)
    root.categCombo.set("SELECT CATEGORY")

    jokeButton = Button(root, text="MAKE ME LAUGH", width=15, command=getJoke)
    jokeButton.grid(row=3, column=0, columnspan=4, padx=5, pady=8)
    root.jokeText = Text(root, width=50, height=10, bg="snow3", wrap="word")
    root.jokeText.grid(row=4, column=0, columnspan=4, padx=5, pady=5)
    root.jokeText.config(state=DISABLED)

# Defining getJoke() function for displaying jokes based on Language and Category
def getJoke():
    # Fetching & storing user-inputs in resepective variables
    i_Language = root.langCombo.get()
    i_Category = root.categCombo.get()
    try:
        # Generating joke using the get_joke() method of the pyjokes Library.
        # The method takes language and category as the parameters
        joke = pyjokes.get_joke(language=i_Language, category=i_Category)
        # Enabling the Text Widget by setting the state to NORMAL
        root.jokeText.config(state=NORMAL)
        # Clearing the contents of the Text Widget
        root.jokeText.delete(0.0, END)
        # Printing the generated joke in the Text Widget
        root.jokeText.insert(0.0, joke)
        # Disabling the Text Widget by setting the state to DISABLED
        root.jokeText.config(state=DISABLED)
    except Exception as e:
        messagebox.showerror("ERROR", e)

# Creating object of tk class
root = tk.Tk()

# Setting title, background color & size of tkinter window
# & disabling the resizing property
root.geometry("370x290")
root.resizable(False, False)
root.title("PythonForLaughs")
root.config(bg = "darkolivegreen")

# Creating tkinter variables
language = StringVar()
category = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
