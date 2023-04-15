import qrcode

url = "https://www.youtube.com/shorts/AwOO50It9DY"  # QR kodu oluşturmak için kullanılacak URL
img = qrcode.make(url)  # QR kodu görüntüsünü oluştur

# QR kodunu bir görüntü dosyası olarak kaydeder ve py dosyasının bulunduğu klasöre atar
img.save("qrcode.png")
