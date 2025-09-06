import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Functionality
def show_message():
    messagebox.showinfo("Dashboard", "Button Clicked!")

def update_progress():
    value = progress["value"]
    if value < 100:
        progress["value"] += 10
        root.after(500, update_progress)  # updates every 0.5 sec

# Root Window
root = tk.Tk()
root.title("Random Tkinter Dashboard")
root.geometry("900x600")
root.config(bg="#f5f5f5")

# Top Frame (Title Bar)
top_frame = tk.Frame(root, bg="#4CAF50", height=60)
top_frame.pack(fill="x")

title_label = tk.Label(top_frame, text="📊 Dashboard", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white")
title_label.pack(pady=10)

# Left Navigation Panel
left_frame = tk.Frame(root, bg="#333", width=200)
left_frame.pack(fill="y", side="left")

nav_label = tk.Label(left_frame, text="Navigation", font=("Arial", 14, "bold"), bg="#333", fg="white")
nav_label.pack(pady=10)

btn1 = tk.Button(left_frame, text="Home", font=("Arial", 12), command=show_message)
btn1.pack(pady=10, fill="x")

btn2 = tk.Button(left_frame, text="Settings", font=("Arial", 12), command=show_message)
btn2.pack(pady=10, fill="x")

btn3 = tk.Button(left_frame, text="About", font=("Arial", 12), command=show_message)
btn3.pack(pady=10, fill="x")

# Main Content Area
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True, fill="both", side="left")

# Progress Bar Example
progress_label = tk.Label(main_frame, text="Progress", font=("Arial", 14), bg="white")
progress_label.pack(pady=10)

progress = ttk.Progressbar(main_frame, length=300, mode="determinate")
progress.pack(pady=10)
update_progress()

# Add a Chart (using Matplotlib)
fig, ax = plt.subplots(figsize=(4, 3))
ax.bar(["A", "B", "C", "D"], [10, 30, 20, 40], color="skyblue")
ax.set_title("Random Bar Chart")

canvas = FigureCanvasTkAgg(fig, master=main_frame)
canvas.draw()
canvas.get_tk_widget().pack(pady=20)

root.mainloop()
