import tkinter as tk
from tkinter import messagebox
from googletrans import Translator

translator = Translator()

# Function to translate text
def translate_text():
    input_text = text_input.get("1.0", "end-1c")
    target_language = language_input.get()

    if not input_text.strip():
        messagebox.showerror("Error", "Please enter text to translate.")
        return

    try:
        translation = translator.translate(input_text, dest=target_language)
        result_text.delete("1.0", "end")
        result_text.insert("1.0", translation.text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x400")

# Label for input text
input_label = tk.Label(root, text="Enter text to translate:")
input_label.pack(pady=10)

# Text input area
text_input = tk.Text(root, height=10, width=70)
text_input.pack(pady=10)

# Entry for target language
language_label = tk.Label(root, text="Enter target language (e.g., 'fr' for French):")
language_label.pack(pady=5)
language_input = tk.Entry(root)
language_input.pack(pady=5)

# Button to translate text
translate_button = tk.Button(root, text="Translate Text", command=translate_text)
translate_button.pack(pady=10)

# Text area for translation output
result_text = tk.Text(root, height=10, width=70)
result_text.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
