# uTrade Solutions Campus Hiring 2026 – Mini Project

## Overview

This project is a simple command-line application built in Python that allows users to manage a collection of values. The application provides functionality to add, remove, view, and clear stored items through an interactive menu.

The purpose of this project is to demonstrate clean code structure, modular design, and proper handling of user input and edge cases.

---

## Project Structure

```
utrade-mini-project
│
├── src
│   └── main.py
│
├── tests
│
├── README.md
├── requirements.txt
└── .gitignore
```

**src/main.py**
Contains the main program logic including the application flow and data management classes.

**tests/**
Reserved for future automated test cases.

**requirements.txt**
Lists project dependencies (no external libraries are required for this project).

---

## Design Decisions

The program is designed using a modular approach and consists of two main components:

### Application Class

Responsible for handling user interaction.
It displays the menu, reads user choices, and calls the appropriate functions.

### DataManager Class

Responsible for managing the stored data.
It provides functions to:

* add new values
* remove existing values
* display stored values
* clear all values

Separating these responsibilities improves readability, maintainability, and makes the system easier to extend.

---

## Data Structures Used

### Python List

A Python list is used to store user-entered values.

Reasons for choosing a list:

* Efficient insertion using `append()`
* Easy removal using `remove()`
* Simple iteration for displaying stored values
* Suitable for small in-memory datasets

Given the limited scope of the assignment, a list provides a clean and efficient solution.

---

## Edge Cases Handled

The application includes validation to prevent common errors:

* Empty input values
* Duplicate entries
* Attempting to remove values that do not exist
* Viewing items when the list is empty
* Invalid menu selections

Handling these cases ensures the application remains stable and user-friendly.

---

## How to Build and Run

### 1. Clone the repository

```
git clone <repository-link>
cd utrade-mini-project
```

### 2. Run the application

```
python src/main.py
```

No external libraries are required.

---

## Example Usage

```
==== Mini Project Menu ====

1. Add Item
2. Remove Item
3. View Items
4. Clear All Items
5. Exit

Enter your choice: 1
Enter a value: apple
Value added successfully.

Enter your choice: 3

Stored Values:
1. apple
```

---

## Trade-offs

Due to the limited time available for the assignment:

* Data is stored only in memory and is not persisted after the program exits.
* No external libraries or frameworks were used.
* The application is implemented as a command-line interface rather than a graphical interface.

These decisions allowed focusing on clean code structure and core functionality.

---

## Known Limitations

* Data is not saved after the application closes.
* The application supports only a single user session.
* Automated tests are not yet implemented.

---

## Future Improvements

Possible improvements for future versions include:

* Adding persistent storage using files or a database
* Implementing automated unit tests
* Adding logging for better debugging
* Creating a REST API interface
* Supporting multiple users concurrently

---

## Author

Submitted as part of the **uTrade Solutions Campus Hiring 2026 – Mini Project Assignment**.