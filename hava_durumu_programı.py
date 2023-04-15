import tkinter as tk
import requests
import json

api_key = "65ba8cbcbecb44df337bd8b4810a9a52"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = ""

# Hava durumu verilerini alma fonksiyonu
def get_weather():
    # Girilen şehir adını al
    city_name = city_entry.get()

    # API isteği
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    # Verileri kontrol etme
    if data["cod"] != "404":
        if "weather" in data:
            weather = data["weather"]
            main = data["main"]
            temperature = main["temp"]
            humidity = main["humidity"]
            pressure = main["pressure"]
            description = weather[0]["description"]
            # Hava durumu verilerini ekrana yazdırma
            result_label.config(text=f"Hava durumu: {description}\nSıcaklık: {temperature}°C\nNem: {humidity}%\nBasınç: {pressure}hPa")
        else:
            result_label.config(text="Hava durumu verisi bulunamadı!")
    else:
        result_label.config(text="Hava durumu bilgisi bulunamadı!")

# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Hava Durumu")

# Şehir seçimi için giriş kutusu ve butonu
city_entry = tk.Entry(root, width=20, font=("Arial", 14))
city_entry.pack(pady=10)

get_weather_button = tk.Button(root, text="Hava Durumu Bilgisi Al", font=("Arial", 14), command=get_weather)
get_weather_button.pack()

# Hava durumu sonuçlarının görüntüleneceği etiket
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
