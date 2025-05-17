import tkinter as tk
import requests

def fetch_pastebin_content():
    url = "https://pastebin.com/raw/RSAxyvQf"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        content = response.text
        text_area.delete(1.0, tk.END)  
        text_area.insert(tk.END, content)  
    except requests.exceptions.RequestException as e:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, f"Error fetching content: {e}")


root = tk.Tk()
root.title("SMTP VIP FOR FREE BY X7X1X TECHNOLOGY")


root.configure(bg='black')


text_area = tk.Text(root, wrap=tk.WORD, width=80, height=20, bg='black', fg='white')
text_area.pack(padx=10, pady=10)


fetch_button = tk.Button(root, text="CLAIM FOR FREE", command=fetch_pastebin_content, bg='black', fg='white')
fetch_button.pack(pady=5)


root.mainloop()

