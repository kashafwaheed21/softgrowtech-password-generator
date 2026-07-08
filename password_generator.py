import customtkinter as ctk
import random
import string
import pyperclip
from tkinter import messagebox

# ---------------- Appearance ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- Window ----------------
app = ctk.CTk()
app.title("🔐 Secure Password Generator Pro")
app.geometry("700x780")
app.resizable(False, False)

# ---------------- Title ----------------
title = ctk.CTkLabel(
    app,
    text="🔐 Secure Password Generator Pro",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

subtitle = ctk.CTkLabel(
    app,
    text="Generate strong and secure passwords instantly",
    font=("Arial", 14)
)
subtitle.pack()

# ---------------- Password Length ----------------
length_label = ctk.CTkLabel(
    app,
    text="Password Length",
    font=("Arial", 18)
)
length_label.pack(pady=(25,5))

length_slider = ctk.CTkSlider(
    app,
    from_=8,
    to=32,
    number_of_steps=24
)
length_slider.set(16)
length_slider.pack(fill="x", padx=60)

length_value = ctk.CTkLabel(
    app,
    text="16 Characters",
    font=("Arial",16)
)
length_value.pack(pady=8)

def update_slider(value):
    length_value.configure(text=f"{int(value)} Characters")

length_slider.configure(command=update_slider)

# ---------------- Checkboxes ----------------
checkbox_frame = ctk.CTkFrame(app)
checkbox_frame.pack(pady=20)

uppercase = ctk.BooleanVar(value=True)
lowercase = ctk.BooleanVar(value=True)
numbers = ctk.BooleanVar(value=True)
symbols = ctk.BooleanVar(value=True)

ctk.CTkCheckBox(
    checkbox_frame,
    text="Uppercase Letters",
    variable=uppercase
).grid(row=0,column=0,padx=20,pady=10)

ctk.CTkCheckBox(
    checkbox_frame,
    text="Lowercase Letters",
    variable=lowercase
).grid(row=0,column=1,padx=20,pady=10)

ctk.CTkCheckBox(
    checkbox_frame,
    text="Numbers",
    variable=numbers
).grid(row=1,column=0,padx=20,pady=10)

ctk.CTkCheckBox(
    checkbox_frame,
    text="Symbols",
    variable=symbols
).grid(row=1,column=1,padx=20,pady=10)

# ---------------- Password Box ----------------
password_entry = ctk.CTkEntry(
    app,
    width=500,
    height=45,
    font=("Consolas",18)
)
password_entry.pack(pady=20)

def generate_password():

    password_entry.configure(state="normal")

    characters = ""

    if uppercase.get():
        characters += string.ascii_uppercase

    if lowercase.get():
        characters += string.ascii_lowercase

    if numbers.get():
        characters += string.digits

    if symbols.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showwarning(
            "Selection Required",
            "Please select at least one character type."
        )
        return

    length = int(length_slider.get())

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    # Make the entry editable
    password_entry.configure(state="normal")

    # Remove the old password
    password_entry.delete(0, "end")

    # Insert the new password
    password_entry.insert(0, password)

   # Lock the entry so it can't be edited accidentally
    password_entry.configure(state="readonly")

    history_box.insert("end", password + "\n")
    check_strength(password)

def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    pyperclip.copy(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength.configure(
            text="🔴 Weak • Improve by using more character types"
        )

    elif score <= 4:
        strength.configure(
            text="🟡 Medium • Good, but could be stronger"
        )

    else:
        strength.configure(
            text="🟢 Strong • Excellent password!"
        )
def clear_history():
    history_box.delete("1.0", "end")
# ---------------- Buttons ----------------
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

generate_btn = ctk.CTkButton(
    button_frame,
    text="🔐 Generate Password",
    width=180,
    height=40,
    command=generate_password
)
generate_btn.grid(row=0, column=0, padx=10)

copy_btn = ctk.CTkButton(
    button_frame,
    text="📋 Copy Password",
    width=150,
    height=40,
    command=copy_password
)
copy_btn.grid(row=0, column=1, padx=10)

clear_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Clear History",
    width=150,
    height=40,
    command=clear_history
)
clear_btn.grid(row=0, column=2, padx=10)

# ---------------- Password Strength ----------------
strength_title = ctk.CTkLabel(
    app,
    text="🔐 Password Strength",
    font=("Arial", 18, "bold")
)
strength_title.pack(pady=(20, 5))

strength = ctk.CTkLabel(
    app,
    text="⚪ Not Generated Yet",
    font=("Arial", 16)
)
strength.pack(pady=(0, 15))

# ---------------- History ----------------
history_label = ctk.CTkLabel(
    app,
    text="Password History",
    font=("Arial",18,"bold")
)
history_label.pack()

history_box = ctk.CTkTextbox(
    app,
    width=500,
    height=100
)
history_box.pack(pady=10)

footer = ctk.CTkLabel(
    app,
    text="Developed by Kashaf Waheed | SoftGrowTech Python Internship",
    font=("Arial", 12)
)
footer.pack(pady=(5, 10))

app.mainloop()