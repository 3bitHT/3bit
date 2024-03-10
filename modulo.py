import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Dichiarazione delle variabili globali
entry_full_name = None
entry_birth_date = None
entry_birth_place = None
entry_gender = None
entry_address = None
label_photo = None
label_signature = None

def select_photo():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.svg")])
    if file_path:
        label_photo.config(text=file_path)

def select_signature():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.svg")])
    if file_path:
        label_signature.config(text=file_path)

def create_identity():
    global entry_full_name, entry_birth_date, entry_birth_place, entry_gender, entry_address, label_photo, label_signature
    
    # Recupera le informazioni inserite dall'utente
    full_name = entry_full_name.get()
    birth_date = entry_birth_date.get()
    birth_place = entry_birth_place.get()
    gender = entry_gender.get()
    address = entry_address.get()
    photo_path = label_photo.cget("text")
    signature_path = label_signature.cget("text")

    # Creazione della cartella UTENTI_SALVATI se non esiste
    if not os.path.exists("UTENTI_SALVATI"):
        os.makedirs("UTENTI_SALVATI")

    # Creazione della sottocartella con il nome completo dell'utente
    user_folder = os.path.join("UTENTI_SALVATI", full_name)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    # Salvataggio delle informazioni in un file
    file_path = os.path.join(user_folder, "info.txt")
    with open(file_path, "w") as file:
        file.write(f"Nome completo: {full_name}\n")
        file.write(f"Data di nascita: {birth_date}\n")
        file.write(f"Luogo di nascita: {birth_place}\n")
        file.write(f"Sesso: {gender}\n")
        file.write(f"Indirizzo di residenza: {address}\n")
        file.write(f"Percorso della foto: {photo_path}\n")
        file.write(f"Percorso della firma: {signature_path}\n")

    messagebox.showinfo("Modulo di Identità", "Le informazioni sono state salvate con successo.")

def start():
    global entry_full_name, entry_birth_date, entry_birth_place, entry_gender, entry_address, label_photo, label_signature

    # Creazione della finestra modulo di identità
    modulo_window = tk.Tk()
    modulo_window.title("Modulo di Identità")
    modulo_window.geometry("600x400")

    # Aggiunta dei campi per le informazioni
    label_full_name = tk.Label(modulo_window, text="Nome completo:")
    label_full_name.grid(row=0, column=0, padx=10, pady=5)
    entry_full_name = tk.Entry(modulo_window)
    entry_full_name.grid(row=0, column=1, padx=10, pady=5)

    label_birth_date = tk.Label(modulo_window, text="Data di nascita:")
    label_birth_date.grid(row=1, column=0, padx=10, pady=5)
    entry_birth_date = tk.Entry(modulo_window)
    entry_birth_date.grid(row=1, column=1, padx=10, pady=5)

    label_birth_place = tk.Label(modulo_window, text="Luogo di nascita:")
    label_birth_place.grid(row=2, column=0, padx=10, pady=5)
    entry_birth_place = tk.Entry(modulo_window)
    entry_birth_place.grid(row=2, column=1, padx=10, pady=5)

    label_gender = tk.Label(modulo_window, text="Sesso:")
    label_gender.grid(row=3, column=0, padx=10, pady=5)
    entry_gender = tk.Entry(modulo_window)
    entry_gender.grid(row=3, column=1, padx=10, pady=5)

    label_address = tk.Label(modulo_window, text="Indirizzo di residenza:")
    label_address.grid(row=4, column=0, padx=10, pady=5)
    entry_address = tk.Entry(modulo_window)
    entry_address.grid(row=4, column=1, padx=10, pady=5)

    # Pulsanti per selezionare la foto e la firma
    button_photo = tk.Button(modulo_window, text="Seleziona Foto", command=select_photo)
    button_photo.grid(row=5, column=0, padx=10, pady=5)

    button_signature = tk.Button(modulo_window, text="Seleziona Firma", command=select_signature)
    button_signature.grid(row=5, column=1, padx=10, pady=5)

    # Label per mostrare il percorso del file selezionato
    label_photo = tk.Label(modulo_window, text="")
    label_photo.grid(row=6, column=0, padx=10, pady=5)

    label_signature = tk.Label(modulo_window, text="")
    label_signature.grid(row=6, column=1, padx=10, pady=5)

    # Pulsante per creare il modulo di identità
    button_create_identity = tk.Button(modulo_window, text="Crea Modulo di Identità", command=create_identity)
    button_create_identity.grid(row=7, columnspan=2, padx=10, pady=10)

    modulo_window.mainloop()

if __name__ == "__main__":
    start()

