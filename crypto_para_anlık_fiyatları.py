import tkinter as tk
import requests
import json

api_key = "CMC APİ-KEY"  #buraya coinmarketcap tan aldığınız api anahtarınızı girmeniz gerekiyor.

def get_data(symbol):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": api_key
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    return data["data"][symbol]

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Crypto Para Anlık Fiyat")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Kripto Para Fiyatları")
        self.title_label.pack()

        self.input_frame = tk.Frame(self)
        self.input_frame.pack()

        self.input_label = tk.Label(self.input_frame, text="Sembol: ")
        self.input_label.pack(side=tk.LEFT)

        self.input_entry = tk.Entry(self.input_frame)
        self.input_entry.pack(side=tk.LEFT)

        self.input_button = tk.Button(self.input_frame, text="Göster", command=self.show_data)
        self.input_button.pack(side=tk.LEFT)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def show_data(self):
        symbol = self.input_entry.get().upper()
        data = get_data(symbol)

        name = data["name"]
        symbol = data["symbol"]
        price = data["quote"]["USD"]["price"]
        volume = data["quote"]["USD"]["volume_24h"]
        market_cap = data["quote"]["USD"]["market_cap"]

        text = f"{name} ({symbol}): {price:.2f} USD | Hacim: {volume:.2f} USD | Piyasa Değeri: {market_cap:.2f} USD"
        self.result_label.config(text=text)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
