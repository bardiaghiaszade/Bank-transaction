import tkinter as tk
from tkinter import messagebox
import logic


def do_transfer():
    sender = sender_var.get()
    receiver = receiver_var.get()

    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid amount")
        return

    result = logic.transfer(sender, receiver, amount)

    if result == "Success":
        messagebox.showinfo("Success", "Transfer completed!")
    else:
        messagebox.showerror("Error", result)


# --- GUI ---
root = tk.Tk()
root.title("Bank System")
root.geometry("350x250")

users = logic.get_users()

tk.Label(root, text="Sender").pack()
sender_var = tk.StringVar(root)
sender_var.set(users[0] if users else "")
tk.OptionMenu(root, sender_var, *users).pack()

tk.Label(root, text="Receiver").pack()
receiver_var = tk.StringVar(root)
receiver_var.set(users[0] if users else "")
tk.OptionMenu(root, receiver_var, *users).pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Transfer", command=do_transfer).pack(pady=10)

root.mainloop()