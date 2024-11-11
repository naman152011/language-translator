# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:46:24 2024

@author: LENOVO
"""

from tkinter import Tk, Label, Text, Button, ttk
from googletrans import LANGUAGES

# Step 1: Convert LANGUAGES dictionary values to a list
languages_list = list(LANGUAGES.values())

# Initialize the main application window
root = Tk()
root.title("Language Translator")
root.geometry("600x400")
root.configure(bg="Light Blue")

# Step 2: Create the first combobox for the source language
source_lang_combobox = ttk.Combobox(root, state="readonly", values=languages_list, width=20)
source_lang_combobox.set("english")  # Step 4: Set default language
source_lang_combobox.place(x=115, y=50)

# Label for source language
source_label = Label(root, text="Enter Text:", bg="white", font=("Arial", 12, "bold"))
source_label.place(x=20, y=50)

# Step 5: Create label for output language
output_label = Label(root, text="Output", bg="white", font=("Arial", 12, "bold"))
output_label.place(x=340, y=50)

# Step 7: Create the second combobox for the destination language
dest_lang_combobox = ttk.Combobox(root, state="readonly", values=languages_list, width=20)
dest_lang_combobox.set("choose output language")  # Step 9: Set default prompt for destination language
dest_lang_combobox.place(x=400, y=50)

# Step 10: Create a textarea for the input text
input_textarea = Text(root, height=10, width=30, wrap="word", bg="white", font=("Arial", 10), bd=0, padx=10, pady=10)
input_textarea.place(x=100, y=100)

# Step 11: Create a textarea for the output text
output_textarea = Text(root, height=10, width=30, wrap="word", bg="white", font=("Arial", 10), bd=0, padx=10, pady=10)
output_textarea.place(x=300, y=100)

# Step 12: Define the function to handle translation
def translate_text():
    from googletrans import Translator
    translator = Translator()
    src_lang = source_lang_combobox.get()
    dest_lang = dest_lang_combobox.get()
    input_text = input_textarea.get("1.0", "end-1c")
    
    # Convert language names to codes for translation
    src_code = [k for k, v in LANGUAGES.items() if v == src_lang]
    dest_code = [k for k, v in LANGUAGES.items() if v == dest_lang]
    
    if src_code and dest_code and input_text:
        translation = translator.translate(input_text, src=src_code[0], dest=dest_code[0])
        output_textarea.delete("1.0", "end")
        output_textarea.insert("end", translation.text)

# Step 13: Create a button to trigger translation
translate_button = Button(root, text="Translate", font=("Arial", 12, "bold"), bg="blue", fg="white",
                          activebackground="lightblue", relief="flat", pady=5, command=translate_text)
translate_button.place(x=250, y=300)

# Run the Tkinter main loop
root.mainloop()
