# Password_Strength_Tester
Demonstrated strength testing of a password using Python language and GUI.

Here’s an in-depth explanation of the code:

### Library used:

I've used the *Tkinter* library for GUI and *re* for string pattern matching purposes.

### Function to Check Password Strength:
def check_password_strength(password)

This function checks several criteria such as length, lowercase letters, uppercase letters, digits, and special characters. Then it sums the boolean values of the requirements (True counts as 1, False counts as 0) to get a score. Based on the score, it categorizes the password as "Weak", "Medium", "Strong", or "Very Strong". After that, it returns the password strength and the dictionary containing the criteria results.

### Function to Update Password Strength Display
def update_password_strength(event=None)

This function updates the password strength label and criteria display in the GUI. It retrieves the password entered by the user and calls `check_password_strength` to evaluate the password and get the strength and criteria results, also updates the strength label with the password strength and changes its color based on the strength level. After this, it also updates the color of each criterion label to green if the criterion is met and red if it is not.

### Created and Set Up the GUI

- **Main Window**: Creates the main window (`root`) with the title "Password Strength Tester".
- **Password Entry**: Adds a label prompting the user to enter a password and an entry widget (`password_entry`) where the user types their password. The `show="*"` parameter hides the actual characters typed.
- **Event Binding**: Binds the `<KeyRelease>` event to the `update_password_strength` function, ensuring that the password strength is evaluated and displayed every time the user types a key.
- **Strength Label**: Adds a label (`strength_label`) to display the password strength.
- **Criteria Labels**: Adds labels for each password strength criterion, which will change color based on whether the criteria are met.
- **Event Loop**: Starts the GUI event loop with `root.mainloop()`, making the window responsive and interactive.
