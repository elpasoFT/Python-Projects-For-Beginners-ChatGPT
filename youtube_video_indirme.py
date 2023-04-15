import tkinter as tk
from tkinter import messagebox
import youtube_dl
import os


def download():
    url = entry.get()
    path = os.path.join(os.path.expanduser('~'), 'Desktop', 'indirilen_dosyalar')
    if not os.path.exists(path):
        os.mkdir(path)
    ydl_opts = {
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
    }

    # Format seçeneklerini ve en yüksek kaliteyi belirlemek için bir sözlük
    format_options = {
        'video': ['-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'],
        'audio': ['-x', '--audio-format', 'mp3']
    }

    # Kullanıcının seçtiği format ve kaliteyi ydl_opts sözlüğüne ekleyin
    if var.get() == 'video':
        ydl_opts['format'] = format_options['video'] + ['--merge-output-format', 'mp4']
    elif var.get() == 'audio':
        ydl_opts['format'] = format_options['audio']
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            messagebox.showinfo("Başarılı", "Dosya başarıyla indirildi!")
        except:
            messagebox.showerror("Başarısız", "Dosya indirilemedi.")


# arayüz oluşturma
root = tk.Tk()
root.title("Video/Audio İndirme Programı")
root.geometry("400x250")

# URL girilecek alan
url_label = tk.Label(root, text="İndirilecek video/ses dosyasının URL'sini girin:")
url_label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

# format ve kalite seçenekleri için radyo düğmeleri
options_frame = tk.Frame(root)
options_frame.pack()

var = tk.StringVar()
var.set('video')

video_rb = tk.Radiobutton(options_frame, text="Video", variable=var, value="video")
video_rb.pack(side=tk.LEFT)

audio_rb = tk.Radiobutton(options_frame, text="Ses", variable=var, value="audio")
audio_rb.pack(side=tk.LEFT)

# video formatı seçenekleri için seçenek menüsü
format_label = tk.Label(root, text="Video formatını seçin:")
format_label.pack()

formats = {
    'mp4': 'mp4',
    'webm': 'webm',
    'flv': 'flv',
    '3gp': '3gp',
    'avi': 'avi'
}

format_menu = tk.OptionMenu(root, tk.StringVar(), *formats.keys())
format_menu.pack()

# indirme butonu
download_button = tk.Button(root, text="İndir", command=download)
download_button.pack()

root.mainloop()
