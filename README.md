# PasswordManager
A safe password manager using JSON type data to store and search through user credentials

![image](https://github.com/user-attachments/assets/0781848d-0594-49db-aaef-fa77706bb2e2)

This app uses Tkinter GUI in Python to show a clean, user-friendly interface.
In the main window, you'll see "search", "generate" and "add" button. "Search" button gets the text entered into the website entry and then searches for it in the data.json for matching entries, if finds one it will show the username/email and password created for that website.
Generate button generates you a strong random password (see generate_password() function in the main.py), and if you don't like the current password than you can reclick the button to generate a new password.
Add button will enter the new user credentials into the data.json file.

This app has built-in features for smoother user experience. For example, if you leave the entries blank then try to add the user credentials, then you will get an error saying you left the essential fields blank. 
It ships with an already generated data.json file, but if you want, you can delete it and let the app create one for you. Deleting the current data.json will not give you any errors as FileNotFoundError is already handled in the main.py's try except blocks. In a case where you might be searching for user credentials for a website you did not create before, app will present you a message box saying "Data Not Found". This KeyWordError is also handled with try-except blocks and will not force the app to unexpectedly crash.
Hopefully you will have a smooth and enjoyable experience with this app.
