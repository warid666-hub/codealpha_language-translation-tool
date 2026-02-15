# translation_tool_futuristic.py

from googletrans import Translator
from gtts import gTTS
import tkinter as tk
from tkinter import ttk, messagebox
import os


translator = Translator()

languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Urdu": "ur",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Italian": "it",
    "Russian": "ru",
    "Portuguese": "pt"
}



def translate_text():
    src_code = languages.get(source_lang.get())
    dest_code = languages.get(target_lang.get())
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to translate")
        return
    try:
        translated = translator.translate(text, src=src_code, dest=dest_code)
        output_text.config(state='normal')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
        output_text.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed!\n{str(e)}")

def copy_text():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")

def speak_text():
    text = output_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "No text to speak!")
        return
    try:
        tts = gTTS(text=text, lang=languages.get(target_lang.get()))
        tts.save("output.mp3")
        os.system("start output.mp3")
    except Exception as e:
        messagebox.showerror("Error", f"TTS failed!\n{str(e)}")

def swap_languages():
    src = source_lang.get()
    tgt = target_lang.get()
    source_lang.set(tgt)
    target_lang.set(src)
    input_content = input_text.get("1.0", tk.END).strip()
    output_content = output_text.get("1.0", tk.END).strip()
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, output_content)
    output_text.config(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, input_content)
    output_text.config(state='disabled')



root = tk.Tk()
root.title("⚡ Futuristic AI Translator")
root.geometry("900x700")
root.configure(bg="#0f111a")
root.state('zoomed')


TITLE_FONT = ("Consolas", 28, "bold")
LABEL_FONT = ("Consolas", 14, "bold")
TEXT_FONT = ("Consolas", 14)
BTN_FONT = ("Consolas", 12, "bold")


tk.Label(root, text="⚡ AI Language Translator", font=TITLE_FONT, bg="#0f111a", fg="#00ffea").pack(pady=20)


input_frame = tk.Frame(root, bg="#1c1f2b", bd=3, relief="ridge")
input_frame.pack(pady=15, padx=30, fill="both")
tk.Label(input_frame, text="Enter Text:", font=LABEL_FONT, bg="#1c1f2b", fg="#00ffea").pack(anchor="w", padx=10, pady=5)
input_text = tk.Text(input_frame, height=8, font=TEXT_FONT, bg="#10121c", fg="#00ffea", insertbackground="#00ffea")
input_text.pack(padx=10, pady=5, fill="both", expand=True)


lang_frame = tk.Frame(root, bg="#0f111a")
lang_frame.pack(pady=10)

tk.Label(lang_frame, text="Source Language:", font=LABEL_FONT, bg="#0f111a", fg="#00ffea").grid(row=0, column=0, padx=10)
source_lang = ttk.Combobox(lang_frame, values=list(languages.keys()), font=TEXT_FONT, width=20)
source_lang.grid(row=0, column=1, padx=10)
source_lang.set("English")

tk.Label(lang_frame, text="Target Language:", font=LABEL_FONT, bg="#0f111a", fg="#00ffea").grid(row=0, column=2, padx=10)
target_lang = ttk.Combobox(lang_frame, values=list(languages.keys()), font=TEXT_FONT, width=20)
target_lang.grid(row=0, column=3, padx=10)
target_lang.set("Spanish")

tk.Button(lang_frame, text="🔄 Swap", command=swap_languages, font=BTN_FONT, bg="#00ffea", fg="#0f111a", activebackground="#00ffea", activeforeground="#0f111a").grid(row=0, column=4, padx=15)


btn_frame = tk.Frame(root, bg="#0f111a")
btn_frame.pack(pady=15)
def on_hover(e): e.widget['bg'] = '#00ffea'; e.widget['fg'] = '#0f111a'
def off_hover(e): e.widget['bg'] = '#1c1f2b'; e.widget['fg'] = '#00ffea'

translate_btn = tk.Button(btn_frame, text="Translate", command=translate_text, font=BTN_FONT, bg="#1c1f2b", fg="#00ffea", width=15)
translate_btn.grid(row=0, column=0, padx=10)
translate_btn.bind("<Enter>", on_hover)
translate_btn.bind("<Leave>", off_hover)

copy_btn = tk.Button(btn_frame, text="Copy", command=copy_text, font=BTN_FONT, bg="#1c1f2b", fg="#00ffea", width=15)
copy_btn.grid(row=0, column=1, padx=10)
copy_btn.bind("<Enter>", on_hover)
copy_btn.bind("<Leave>", off_hover)

speak_btn = tk.Button(btn_frame, text="Speak", command=speak_text, font=BTN_FONT, bg="#1c1f2b", fg="#00ffea", width=15)
speak_btn.grid(row=0, column=2, padx=10)
speak_btn.bind("<Enter>", on_hover)
speak_btn.bind("<Leave>", off_hover)


output_frame = tk.Frame(root, bg="#1c1f2b", bd=3, relief="ridge")
output_frame.pack(pady=15, padx=30, fill="both")
tk.Label(output_frame, text="Translated Text:", font=LABEL_FONT, bg="#1c1f2b", fg="#00ffea").pack(anchor="w", padx=10, pady=5)
output_text = tk.Text(output_frame, height=8, font=TEXT_FONT, bg="#10121c", fg="#00ffea", state='disabled', insertbackground="#00ffea")
output_text.pack(padx=10, pady=5, fill="both", expand=True)

root.mainloop()
