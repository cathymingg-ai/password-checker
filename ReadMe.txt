Password Validity Checker
======================================

OVERVIEW
The Password Validity Checker is a beginner-friendly Python project that validates passwords based on specific security criteria. It features a graphical user interface (GUI) created with Tkinter, making it easy to use and visually appealing. This project is ideal for anyone starting in Python programming and cybersecurity.

FEATURES
Validates passwords based on:
Minimum length of 8 characters.
At least one lowercase letter.
At least one uppercase letter.
At least one digit.
At least one special character (@, $, _, &, !, %).
GUI with user-friendly design.
"Show/Hide Password" toggle for better usability.
Clear error messages displayed for invalid passwords.

PREREQUISITES
To run this project, ensure you have the following installed on your system:
Python 3.6 or higher
Tkinter (usually included with Python)
If Tkinter is not installed, you can install it based on your Linux distribution:

For Ubuntu/Debian:
    > sudo apt install python3-tk

For Fedora:
    > sudo dnf install python3-tkinter

For Arch Linux:
    > sudo pacman -S tk

HOW TO RUN
1. Clone or download this repository to your local machine.
2. Save the password_checker_gui.py file in a directory of your choice.
3. Open a terminal and navigate to the directory where the file is saved.
4. Run the script with the following command: python3 password_checker_gui.py
5. The GUI will launch with the title "This is your basic password validity checker."

HOW TO USE
1. Enter a password in the provided text field.
2. Click "Check Password" to validate it.
3. If the password is invalid, an error message will explain why. Adjust your password accordingly.
4. Use the "Show Password" toggle button to view or hide the entered password.

VALIDATION ALGORITHM: BASIC USE CASE
This project demonstrates the importance of password security and teaches:
1. How to implement basic password validation rules.
2. Building a GUI with Tkinter.
3. Providing meaningful feedback to users.

SCREENSHOTS
GUI on launch: Shows the password input field, "Show Password" toggle, and "Check Password" button.
Validation result: Displays a pop-up message indicating whether the password is valid or explaining why it is invalid.

FUTURE ENHANCEMENTS
Add a password strength indicator (e.g., weak, medium, strong).
Allow users to customize validation criteria.
Add support for saving or exporting validation results.
Improve GUI aesthetics with advanced themes.

LICENSE
This project is open-source and free to use for learning and development purposes. Contributions are welcome!
======================================