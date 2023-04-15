import os
import docx
import pytesseract
from PIL import Image

# özelleştirilmiş girdi klasörü yolu
girdi_klasoru = r"C:\Users\elpasoft\Desktop\girdi_klasoru"

# Tesseract OCR'nin yüklü olduğundan emin olun
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\elpasoft\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Çıktı Word dosyası
doc = docx.Document()

# Girdi klasöründeki tüm görüntü dosyalarını işle
for dosya in os.listdir(girdi_klasoru):
    if dosya.endswith(".png") or dosya.endswith(".jpg") or dosya.endswith(".jpeg"):
        dosya_yolu = os.path.join(girdi_klasoru, dosya)
        image = Image.open(dosya_yolu)
        text = pytesseract.image_to_string(image, lang='tur')
        doc.add_paragraph(text)

# Sonuç Word dosyasını kaydet
doc.save("çıktı_dosyası.docx")
