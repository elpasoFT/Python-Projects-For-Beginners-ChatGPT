import requests
import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self):
        self.url = 'https://openexchangerates.org/api/latest.json'
        self.api_key = '5c198a1e92c74d0aa08691bfb3442401'
        self.currencies = self.get_currencies()
        self.currency_countries = self.get_currency_countries()
        
        self.app = tk.Tk()
        self.app.title('Para Birimi Dönüştürücü')
        self.app.geometry('400x200')
        
        self.from_label = ttk.Label(self.app, text='Dönüştürülecek Para Birimi:')
        self.from_label.pack()
        
        self.from_currency = ttk.Combobox(self.app, values=[f'{currency} ({self.currency_countries[currency]})' for currency in self.currencies])
        self.from_currency.pack()
        self.from_currency.current(0)
        
        self.to_label = ttk.Label(self.app, text='Alınacak Para Birimi:')
        self.to_label.pack()
        
        self.to_currency = ttk.Combobox(self.app, values=[f'{currency} ({self.currency_countries[currency]})' for currency in self.currencies])
        self.to_currency.pack()
        self.to_currency.current(0)
        
        self.amount_label = ttk.Label(self.app, text='Miktar:')
        self.amount_label.pack()
        
        self.amount = ttk.Entry(self.app)
        self.amount.pack()
        
        self.convert_button = ttk.Button(self.app, text='Dönüştür', command=self.convert)
        self.convert_button.pack()
        
        self.result_label = ttk.Label(self.app, text='')
        self.result_label.pack()
        
        self.app.mainloop()
    
    def get_currencies(self):
        response = requests.get(f'{self.url}?app_id={self.api_key}')
        data = response.json()
        currencies = list(data['rates'].keys())
        currencies.append(data['base'])
        currencies.sort()
        return currencies
    
    def get_currency_countries(self):
        response = requests.get('https://openexchangerates.org/api/currencies.json')
        data = response.json()
        return data
    
    def convert(self):
        from_curr = self.from_currency.get().split()[0]
        to_curr = self.to_currency.get().split()[0]
        amount = float(self.amount.get())
        
        response = requests.get(f'{self.url}?app_id={self.api_key}&base={from_curr}')
        data = response.json()
        rate = data['rates'][to_curr]
        
        result = amount * rate
        self.result_label.config(text=f'{amount:.2f} {from_curr} ({self.currency_countries[from_curr]}) = {result:.2f} {to_curr} ({self.currency_countries[to_curr]})')

if __name__ == '__main__':
    converter = CurrencyConverter()
