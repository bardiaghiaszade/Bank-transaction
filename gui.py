
import tkinter as tk
from tkinter import messagebox, simpledialog
import logic


def update_balances(*args):
    sender = sender_var.get()
    receiver = receiver_var.get()

    sender_balance = logic.get_balance(sender) if sender else None
    receiver_balance = logic.get_balance(receiver) if receiver else None

    if sender_balance is not None:
        sender_balance_label.config(
            text=f"Balance: {sender_balance:.2f} credits"
        )
    else:
        sender_balance_label.config(text="Balance: -")

    if receiver_balance is not None:
        receiver_balance_label.config(
            text=f"Balance: {receiver_balance:.2f} credits"
        )
    else:
        receiver_balance_label.config(text="Balance: -")


def refresh_users():
    users = logic.get_users()

    for variable, menu in (
        (sender_var, sender_menu),
        (receiver_var, receiver_menu)
    ):
        current_user = variable.get()

        menu.delete(0, "end")

        for user in users:
            menu.add_command(
                label=user,
                command=lambda value=user, var=variable: (
                    var.set(value),
                    update_balances()
                )
            )

        if current_user in users:
            variable.set(current_user)
        elif users:
            variable.set(users[0])
        else:
            variable.set("")

    update_balances()


def do_transfer():
    sender = sender_var.get()
    receiver = receiver_var.get()

    if not sender or not receiver:
        messagebox.showerror("Error", "Please select both users")
        return

    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid amount")
        return

    result = logic.transfer(sender, receiver, amount)

    if result == "Success":
        messagebox.showinfo("Success", "Transfer completed!")
        amount_entry.delete(0, tk.END)
        update_balances()
    else:
        messagebox.showerror("Error", result)


def add_new_user():
    name = simpledialog.askstring(
        "Add User",
        "Enter the new user's name:"
    )

    if name is None:
        return

    result = logic.add_user(name)

    if result == "Success":
        messagebox.showinfo(
            "Success",
            f"User {name.strip()} added with 100 credits!"
        )
        refresh_users()
    else:
        messagebox.showerror("Error", result)


# --- GUI ---
root = tk.Tk()
root.title("Bank System")
root.geometry("380x350")

users = logic.get_users()

sender_var = tk.StringVar(root)
receiver_var = tk.StringVar(root)

sender_var.set(users[0] if users else "")
receiver_var.set(users[0] if users else "")

tk.Label(root, text="Sender").pack()

sender_menu_widget = tk.OptionMenu(root, sender_var, "")
sender_menu_widget.pack()
sender_menu = sender_menu_widget["menu"]

sender_balance_label = tk.Label(root, text="Balance: -")
sender_balance_label.pack()

tk.Label(root, text="Receiver").pack()

receiver_menu_widget = tk.OptionMenu(root, receiver_var, "")
receiver_menu_widget.pack()
receiver_menu = receiver_menu_widget["menu"]

receiver_balance_label = tk.Label(root, text="Balance: -")
receiver_balance_label.pack()

tk.Label(root, text="Amount").pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(
    root,
    text="Transfer",
    command=do_transfer
).pack(pady=5)

tk.Button(
    root,
    text="Add User",
    command=add_new_user
).pack(pady=5)

refresh_users()

root.mainloop()
