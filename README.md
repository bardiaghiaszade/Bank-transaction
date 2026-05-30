# Simple Banking System

A small banking application built with Python, SQLite, and Tkinter.

The application allows users to transfer money between people stored in an SQLite database through a graphical user interface.

## Features

- View users stored in the database
- Select sender and receiver from dropdown menus
- Transfer money between accounts
- Automatic balance updates in SQLite
- Error handling for:
  - Invalid amounts
  - Missing users
  - Insufficient funds

## Project Structure

```text
transaction/
│
├── after.db      # SQLite database
├── logic.py      # Database and transaction logic
├── gui.py        # Tkinter graphical interface
└── README.md
```

## Database Structure

Database: `after.db`

Table: `people`

| Column | Type |
|----------|----------|
| id | INTEGER PRIMARY KEY |
| name | TEXT |
| money | REAL |

Example:

| id | name | money |
|----|------|--------|
| 1 | Alice | 1000 |
| 2 | Bob | 500 |
| 3 | Charlie | 750 |

## Requirements

- Python 3.10+ (or newer)
- Tkinter (usually included with Python)
- SQLite3 (included with Python)

## Installation

Clone or download the project.

Place the files in the same directory:

```text
after.db
logic.py
gui.py
```

## Running the Application

Open a terminal in the project folder:

```bash
cd path/to/project
```

Run:

```bash
python gui.py
```

A window will open where you can:

1. Select a sender.
2. Select a receiver.
3. Enter an amount.
4. Click **Transfer**.

## How It Works

### logic.py

Contains all database operations:

- Retrieve users from the database
- Validate transfers
- Update balances

### gui.py

Contains the Tkinter interface:

- Dropdown menus for sender and receiver
- Amount input field
- Transfer button
- Success and error messages

## Example Workflow

1. Alice has 1000.
2. Bob has 500.
3. Transfer 200 from Alice to Bob.

Result:

| Name | Balance |
|--------|--------|
| Alice | 800 |
| Bob | 700 |

## Future Improvements

- Transaction history
- Account creation
- Account deletion
- Login system
- Balance display
- Modern UI design
- Export transaction logs

## License

This project is open-source and intended for educational purposes.