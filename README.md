# Bank Transaction System

A simple desktop banking simulation built with Python, Tkinter, and SQLite. The application lets you select users, view their balances, transfer credits between users, and add new users with an initial balance of 100 credits.

> **Note:** This is an educational project, not real banking software. It does not provide authentication, authorization, encryption, or production-grade financial controls.

## Features

- **View user balances:** The current balance is displayed for the selected sender and receiver.
- **Transfer credits:** Transfer a specified amount from one user to another.
- **Add users:** Create a new user from the GUI. New users start with **100 credits**.
- **Persistent storage:** User information and balances are stored in an SQLite database.
- **Input validation:** The application rejects invalid amounts, non-positive transfers, transfers to the same user, transfers to unknown users, and transfers that exceed the sender's balance.
- **Duplicate-name check:** A new user cannot be added if a user with the same name already exists, ignoring letter case.
- **Simple desktop interface:** The interface is built with Python's standard `tkinter` library.

## Requirements

- Python 3
- Tkinter (usually included with standard Python installations)
- SQLite support (included with Python)

No third-party Python packages are required.

## Project Structure

```text
Bank-transaction/
├── gui.py          # Tkinter user interface and button actions
├── logic.py        # Database queries, user creation, and transfer logic
├── database.db     # SQLite database containing the people table
├── README.md       # Project documentation
└── .gitignore      # Files excluded from Git
```

## Getting Started

### 1. Get the project

Clone the repository or download the project files and extract them.

```bash
git clone https://github.com/bardiaghiaszade/Bank-transaction.git
cd Bank-transaction
```

If you downloaded a ZIP file instead, open a terminal in the extracted project directory.

### 2. Check the database

The application expects `database.db` to be in the same directory as `logic.py`. The database must contain a `people` table with these columns:

| Column | Purpose |
|---|---|
| `id` | User identifier |
| `name` | User's name |
| `money` | User's balance in credits |

The supplied database includes example users. Keep a backup before changing or replacing it.

### 3. Run the application

From the project directory, run:

```bash
python gui.py
```

On Windows, this may also work:

```powershell
py .\gui.py
```

A window titled **Bank System** should open.

## How to Use

### View balances

1. Choose a user from the **Sender** dropdown.
2. The sender's current balance appears underneath the dropdown.
3. Choose a user from the **Receiver** dropdown.
4. The receiver's current balance appears underneath that dropdown.

### Transfer credits

1. Select the sender and receiver.
2. Enter the amount in the **Amount** field.
3. Click **Transfer**.
4. If the transfer succeeds, a confirmation message appears and both displayed balances are refreshed.

A transfer is rejected if the amount is invalid, zero or negative, the sender and receiver are the same, either user cannot be found, or the sender does not have enough credits.

### Add a user

1. Click **Add User**.
2. Enter the new user's name.
3. On success, the user is saved to the database with an initial balance of **100 credits** and becomes available in the dropdown menus.

Names cannot be empty, and duplicate names are rejected without regard to letter case.

## Implementation Notes

- `gui.py` creates the Tkinter window, dropdown menus, balance labels, amount input, and action buttons.
- `logic.py` contains the database operations:
  - `get_users()` returns user names.
  - `get_balance(name)` returns a user's current balance.
  - `add_user(name)` inserts a user with 100 credits.
  - `transfer(sender, receiver, amount)` validates and performs a transfer.
- SQLite changes are committed after a user is added or a transfer is completed.
- The database path is resolved relative to `logic.py`, so the application does not depend on the terminal's current working directory.

## Limitations

- There is no login system or access control; anyone who can run the application can use its actions.
- Balances are stored as floating-point values, which are not ideal for real financial calculations.
- The database table must already exist; the application does not
