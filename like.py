import tkinter as tk
import random

# Function to show a popup when clicking "Yes"
def show_popup():
    popup = tk.Toplevel(root)
    popup.title("❤️ Thank You! ❤️")
    popup.config(bg="#FFD700")  # Gold Background
    label = tk.Label(popup, text="You're Awesome! 😍", font=("Comic Sans MS", 14, "bold"), bg="#FFD700", fg="black")
    label.pack(padx=30, pady=30)

# Function to move the "No" button away smoothly
def move_button(event):
    x = random.randint(50, 300)
    y = random.randint(50, 300)
    no_button.place(x=x, y=y)

# Create main window
root = tk.Tk()
root.title("❤️ Do You Like Me? ❤️")
root.geometry("400x400")
root.config(bg="#FFB6C1")  # Light pink background

# Create the question label
question_label = tk.Label(root, text="Do you like me? 😊", font=("Comic Sans MS", 16, "bold"), bg="#FFB6C1", fg="black")
question_label.pack(pady=20)

# Create "Yes" button with styling
yes_button = tk.Button(root, text="Yes ❤️", command=show_popup, font=("Arial", 12, "bold"), bg="#32CD32", fg="white", width=10)
yes_button.pack(pady=10)

# Create "No" button with styling
no_button = tk.Button(root, text="No 💔", font=("Arial", 12, "bold"), bg="#FF4500", fg="white", width=10)
no_button.place(x=150, y=200)

# Bind "No" button to move on hover
no_button.bind("<Enter>", move_button)

# Run the Tkinter event loop
root.mainloop()
