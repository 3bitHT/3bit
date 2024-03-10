# File: 3bit.py

class UserAuthentication:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, username_input, password_input):
        return username_input == self.username and password_input == self.password

def login():
    # Definizione delle credenziali di accesso
    username = "admin"
    password = "admin"

    auth = UserAuthentication(username, password)

    # Creazione della finestra di accesso
    access_window = tk.Tk()
    access_window.title("Accesso")
    access_window.geometry("300x150")

    # Label e Entry per nome utente
    label_username = tk.Label(access_window, text="Nome utente:")
    label_username.grid(row=0, column=0, padx=10, pady=5)
    entry_username = tk.Entry(access_window)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    # Label e Entry per password
    label_password = tk.Label(access_window, text="Password:")
    label_password.grid(row=1, column=0, padx=10, pady=5)
    entry_password = tk.Entry(access_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    # Funzione per controllare le credenziali
    def check_credentials():
        username_input = entry_username.get()
        password_input = entry_password.get()
        if auth.authenticate(username_input, password_input):
            access_window.destroy()  # Chiude la finestra di accesso
            import home  # Importa il modulo home.py
            home.start()  # Avvia la pagina home
        else:
            messagebox.showerror("Errore di accesso", "Nome utente o password errati.")

    # Pulsante per effettuare l'accesso
    button_login = tk.Button(access_window, text="Accedi", command=check_credentials)
    button_login.grid(row=2, columnspan=2, padx=10, pady=10)

    access_window.mainloop()

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import messagebox
    login()

