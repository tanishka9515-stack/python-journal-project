import tkinter as tk
from tkinter import messagebox
import datetime

# Create the main diary window and hide it until login
root = tk.Tk()
root.withdraw()  # Hide diary window until password is correct

# Password check function
def check_password():
    if password_entry.get() == "PASSWORDS":  # Replace with your own password
        login_window.destroy()
        root.deiconify()  # Show the diary window
    else:
        messagebox.showerror("Access Denied", "Wrong password!")

# Create login window
login_window = tk.Tk()
login_window.title("Diary Login 🛡️")
login_window.geometry("300x150")
login_window.configure(bg="#1e1e1e")

tk.Label(login_window, text="Enter Password", fg="white", bg="#1e1e1e", font=("Helvetica", 12)).pack(pady=10)
password_entry = tk.Entry(login_window, show="*", width=25, bg="#2e2e2e", fg="white", insertbackground="white")
password_entry.pack(pady=5)
tk.Button(login_window, text="Login", command=check_password, bg="#444", fg="white").pack(pady=10)

# Diary save function
def save_entry():
    entry = text_box.get("1.0", tk.END).strip()
    if entry:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open("diary.txt", "a") as file:
                file.write(f"{timestamp} | Mood: {mood_var.get()}\n{entry}\n\n")
            messagebox.showinfo("Saved", "Your entry has been saved 🖤")
            text_box.delete("1.0", tk.END)
        except PermissionError:
            messagebox.showerror("Permission Denied", "Cannot write to 'diary.txt'. Please check file permissions or try a different location.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")
    else:
        messagebox.showwarning("Empty", "Please write something before saving.")

# Diary GUI setup
root.title("My Journal Entries 🖤")
root.geometry("500x400")
root.configure(bg="#1e1e1e")  # Dark background

title = tk.Label(root, text="📝 Write Your Thoughts", fg="white", bg="#1e1e1e", font=("Helvetica", 16))
title.pack(pady=10)

# Mood selection
mood_var = tk.StringVar(value="😊")  # Default mood
tk.Label(root, text="How are you feeling?", fg="white", bg="#1e1e1e", font=("Helvetica", 12)).pack()
tk.OptionMenu(root, mood_var, "😊", "😢", "😠", "😴", "😎", "🤯", "❤️").pack(pady=5)
text_box = tk.Text(root, height=15, width=50, bg="#2e2e2e", fg="white", insertbackground="white")
text_box.pack(pady=10)

save_btn = tk.Button(root, text="💾 Save Entry", command=save_entry, bg="#444", fg="white")
save_btn.pack(pady=10)

# Start the GUI loop
root.mainloop()