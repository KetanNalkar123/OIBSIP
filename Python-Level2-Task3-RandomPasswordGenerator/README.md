# Advanced Random Password Generator

## OASIS INFOBYTE - Python Programming Internship

### Task 3: Random Password Generator

An advanced desktop-based Random Password Generator developed using Python and Tkinter.

The application generates secure random passwords using Python's cryptographically secure `secrets` module. Users can customize password length, character types, ambiguous character exclusion, password strength, clipboard copying, and temporary generation history.

---

## Features

- Professional graphical user interface using Tkinter
- Custom password length from 4 to 64 characters
- Uppercase character selection
- Lowercase character selection
- Number selection
- Special character selection
- Secure password generation using Python `secrets`
- Guarantees selected character types are included
- Password strength indicator
- Weak, Medium and Strong classifications
- Copy password to clipboard
- Exclude ambiguous characters option
- Last 5 generated passwords
- Session-only password history
- Clear history functionality
- Input validation
- No password persistence

---

## Security

The application uses Python's `secrets` module instead of the standard `random` module.

The `secrets` module is designed for generating cryptographically strong random values and is more appropriate for password generation.

Generated password history is stored only in application memory during the current session.

Passwords are not written to a database or file.

---

## Password Character Types

The application supports:

### Uppercase

```text
A-Z