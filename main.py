import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

urllib3.disable_warnings()

window = tk.Tk()
window.geometry("600x500")
window.title("Pokemon Finder GUI")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="Pokemon Finder")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

import ssl

def load_pokemon():
    pokemon_name = text_id_name.get()  # Get the text entered by the user
    pokemon = pypokedex.get(name=pokemon_name)

    # Create a custom urllib3 PoolManager with SSL context set to None
    http = urllib3.PoolManager(cert_reqs='CERT_NONE', ssl_context=None)

    response = http.request("GET", pokemon.sprites.front.get("default"), retries=False)
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=f"Type: {', '.join(pokemon.types)}")

label_id_name = tk.Label(window, text="ID or NAME")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Entry(window)  # Change Label to Entry
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="LOAD POKEMON", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop()
