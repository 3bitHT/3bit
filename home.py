# File: home.py
import tkinter as tk
from tkinter import PhotoImage
import subprocess

def open_modulo():
    subprocess.Popen(["python", "modulo.py"])

def start():
    # Creazione della finestra home
    home_window = tk.Tk()
    home_window.title("Home")
    home_window.geometry("800x600")  # Dimensioni della finestra
    home_window.configure(bg="yellow")  # Imposta lo sfondo giallo

    # Aggiunta del logo al centro
    logo_image = PhotoImage(file="logohome.png")  # Assicurati di avere un file "logohome.png" nella stessa directory
    logo_label = tk.Label(home_window, image=logo_image, bg="yellow")
    logo_label.image = logo_image
    logo_label.place(relx=0.5, rely=0.5, anchor="center")  # Posiziona il logo al centro

    # Aggiungi un pulsante per creare il modulo di identità
    button_create_identity = tk.Button(home_window, text="Crea Modulo di Identità", command=open_modulo)
    button_create_identity.place(relx=0.5, rely=0.8, anchor="center")

    home_window.mainloop()

if __name__ == "__main__":
    start()

