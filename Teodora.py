################################################################################## IMPORT DELLE LIBRERIE ##################################################################
# Import delle librerie per creare la GUI
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk, ImageDraw  # Per la gestione delle immagini

# Import delle librerie per far funzionare il chatbot
import re
import random

# Import del modulo per generare codici UUID (codice identificativo delle chat salvate)
import uuid
import os

# Import del file in cui è contenuto il dizionario utile al mio bot
import rules

################################################################################## IMPORT DELLE LIBRERIE ##################################################################
# Definizione delle regole del chatbot attraverso dizionario
responses = rules.rules

# Creazione della lista delle risposte negative
rispostenegative = ["Scusami, non ho capito quello che mi hai chiesto. Potresti riformulare la domanda?", "Credo di non aver capito, puoi provare a cambiare la domanda?"]

# Crea una funzione per rispondere alle domande ricevute come input
def respond(user_input):
    for pattern, response_list in responses.items():
        if re.match(pattern, user_input):
            return random.choice(response_list)
    # Se non si trova un match impostiamo la risposta standard
    return random.choice(rispostenegative)

# Crea una funzione per gestire l'invio del messaggio nella GUI (Graphical User Interface)
def send_message():
    user_input = input_entry.get()
    if user_input.strip() != "":
        response = respond(user_input)
        add_message("Tu: " + user_input, "user")
        add_message("Teodora: " + response, "bot")
        input_entry.delete(0, tk.END)
        
        if user_input.strip().lower() == "chiudi":
            close_chat()
        
        # Aggiunge la riga alla lista di conversazione
        conversation.append(f"Tu: {user_input}\nTeodora: {response}\n\n")

# Crea una funzione per chiudere la finestra di dialogo
def close_chat():
    add_message("Me a veg, è stato un piacere parlare con te!", "bot")
    
    # Crea il percorso della sottocartella 'Chat'
    chat_folder = os.path.join("Chat")
    if not os.path.exists(chat_folder):
        os.makedirs(chat_folder)  # Crea la cartella se non esiste
    
    # Genera un UUID univoco per il nome del file
    filename = os.path.join(chat_folder, str(uuid.uuid4()) + ".txt")
    
    # Salva la conversazione su un file .txt
    with open(filename, "w") as file:
        file.writelines(conversation)
    
    root.after(3000, root.destroy)  # Chiude la finestra dopo 3 secondi

# Crea una funzione per aggiungere un messaggio nella chat con l'immagine dell'utente o del bot
def add_message(message, sender):
    chat_text.config(state=tk.NORMAL)
    message_frame = tk.Frame(chat_text, bg="white")

    img = user_img if sender == "user" else bot_img
    img_label = tk.Label(message_frame, image=img, bg="white")
    img_label.pack(side="left", padx=5, pady=5)

    text_label = tk.Label(message_frame, text=message, bg="white", font=font_style, justify=tk.LEFT, wraplength=chat_text.winfo_width() - 70)
    text_label.pack(side="left", padx=5, pady=5)
    
    chat_text.window_create(tk.END, window=message_frame)
    chat_text.insert(tk.END, "\n")
    chat_text.config(state=tk.DISABLED)
    chat_text.see(tk.END)

# Funzione per creare un'immagine circolare
def create_circle_image(image_path, size):
    image_path = os.path.join("Icons", image_path)
    image = Image.open(image_path).resize((size, size), Image.Resampling.LANCZOS).convert("RGBA")
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    result = Image.new("RGBA", (size, size))
    result.paste(image, (0, 0), mask=mask)
    return ImageTk.PhotoImage(result)

# Creazione della GUI
root = tk.Tk()
root.title("Informazioni turistiche Ravenna")

# Impostazione del font per il testo nella finestra di chat
font_style = ("Calibri", 12)

# Colore di sfondo per la finestra e i frame
background_color = "#FFFFFF"  # White

# Caricamento delle immagini per l'utente e il bot
user_img = create_circle_image("user.png", 50)
bot_img = create_circle_image("bot.png", 50)

# Creazione della chat
chat_frame = tk.Frame(root, bg=background_color)
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_text = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state=tk.DISABLED, font=font_style, bg="white")
chat_text.pack(fill=tk.BOTH, expand=True)

# Creazione del textbox dove l'utente digita le domande
input_frame = tk.Frame(root, bg=background_color)
input_frame.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

input_entry = tk.Entry(input_frame, font=font_style)
input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

send_button = tk.Button(input_frame, text="Invia", command=send_message, font=font_style, bg="#B5E2FF")  # Light blue
send_button.pack(side=tk.RIGHT)

# Collegamento del tasto "Invio" all'effettivo invio del messaggio
input_entry.bind("<Return>", lambda event: send_message())

# Creazione di un messaggio di benvenuto
add_message("Teodora: At salut, me a so Teodora. \nDai, mi ripresento! Ciao, sono Teodora, l’assistente virtuale del comune di Ravenna. Come posso esserti utile? Quando non hai più bisogno di me scrivimi 'Chiudi'.", "bot")

# Inizializza la lista di conversazione
conversation = []

# Aggiorna la dimensione del wrap length quando la finestra viene ridimensionata
def update_wrap_length(event):
    for window in chat_text.winfo_children():
        for widget in window.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(wraplength=chat_text.winfo_width() - 70)

chat_text.bind("<Configure>", update_wrap_length)

root.mainloop()
