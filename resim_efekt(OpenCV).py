import cv2
import numpy as np

# Resmi yükle
img = cv2.imread('simple.jpg')

# Boyutunu al
height, width, channels = img.shape

# Gri tonlamalı hale getir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Kara kalem efekti uygula ve PNG dosyası kaydet
sketch = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 15)
cv2.imwrite('result1.png', sketch)

# Siyah beyaz efekti uygula ve PNG dosyası kaydet
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('result2.png', gray)

# Yağlı boya efekti uygula ve PNG dosyası kaydet
oil = cv2.xphoto.oilPainting(img, 7, 1)
cv2.imwrite('result3.png', oil)

# Çizgi film karakteri efekti uygula ve PNG dosyası kaydet
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
color = cv2.bilateralFilter(img, 9, 300, 300)
cartoon = cv2.bitwise_and(color, color, mask=edges)
cv2.imwrite('result4.png', cartoon)

# Karikatür efekti uygula ve PNG dosyası kaydet
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
color = cv2.bilateralFilter(img, 9, 300, 300)
cartoon = cv2.bitwise_and(color, color, mask=edges)
kernel = np.ones((3, 3), np.uint8)
cartoon = cv2.erode(cartoon, kernel, iterations=1)
cartoon = cv2.dilate(cartoon, kernel, iterations=1)
cv2.imwrite('result5.png', cartoon)

# Orjinal resmi göster veya kaydet
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

