import platform
import psutil
import GPUtil
import multiprocessing
import cpuinfo
import shutil

# İşletim Sistemi Bilgileri
print(f"İşletim Sistemi: {platform.system()}")
print(f"İşletim Sistemi Sürümü: {platform.release()}")
print(f"İşletim Sistemi Mimarisi: {platform.machine()}")

# İşlemci Bilgileri
print(f"İşlemci Sayısı: {multiprocessing.cpu_count()}")

cpu_info = cpuinfo.get_cpu_info()
print(f"İşlemci Adı: {cpu_info['brand_raw']}")
print(f"İşlemci Türü: {cpu_info['arch']}")

# Bellek Bilgileri
mem = psutil.virtual_memory()
print(f"Toplam Bellek: {mem.total/1024**3:.2f} GB")
print(f"Kullanılan Bellek: {mem.used/1024**3:.2f} GB")
print(f"Boş Bellek: {mem.available/1024**3:.2f} GB")

# Depolama Birimi Bilgileri
total, used, free = shutil.disk_usage("/")
print(f"Toplam Depolama: {total/1024**3:.2f} GB")
print(f"Kullanılan Depolama: {used/1024**3:.2f} GB")
print(f"Boş Depolama: {free/1024**3:.2f} GB")

# Ekran Kartı Bilgileri
gpus = GPUtil.getGPUs()
for gpu in gpus:
    print(f"GPU Marka: {gpu.name}")
    print(f"Bellek Miktarı: {gpu.memoryTotal:.2f} GB")
    print(f"Kullanılan Bellek: {gpu.memoryUsed:.2f} GB")
    print(f"Boş Bellek: {gpu.memoryFree:.2f} GB")
    print(f"GPU Yükü: {gpu.load*100:.2f} %")

# Windows Lisans Bilgileri
if platform.system() == "Windows":
    import winreg
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion") as key:
        print(f"Windows Sürümü: {winreg.QueryValueEx(key, 'ProductName')[0]}")
        print(f"Windows Lisansı: {winreg.QueryValueEx(key, 'DigitalProductId')[0].hex()}")
