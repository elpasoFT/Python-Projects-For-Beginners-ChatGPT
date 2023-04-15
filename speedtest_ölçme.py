import speedtest as st

speedtester = st.Speedtest()

print("İnternet hızı ölçülüyor...")

download_speed = speedtester.download() / 1000000
upload_speed = speedtester.upload() / 1000000

print(f"İndirme hızı: {download_speed:.2f} Mbps")
print(f"Yükleme hızı: {upload_speed:.2f} Mbps")
