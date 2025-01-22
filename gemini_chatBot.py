
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Çevresel değişkenleri yükle
load_dotenv()

# API anahtarını al
API = os.getenv("API_KEY")
if not API:
    print("API anahtarınız .env dosyasından alınamadı!")
    exit()

# API'yi yapılandır
genai.configure(api_key=API)

# Modeli başlat
model = genai.GenerativeModel("gemini-1.5-flash")

# Sohbet döngüsü
isExit = False
while not isExit:
    text = input("Mesajınızı Yazın: ")
    
    # Çıkış komutu
    if text.lower() == "exit":
        isExit = True
        print("Çıkış Yapıldı...")
        break
    else:
        try:
            # Modelden yanıt almak için
            response = model.generate_content(text)
            print(response.text)
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
