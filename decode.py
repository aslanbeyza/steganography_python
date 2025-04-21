# Görselden gizli mesajı çözer
# decode.py

from PIL import Image
import os
from utils.helpers import binary_to_char

def decode_message(image_path):
    # Görseli kontrol et
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Görsel bulunamadı: {image_path}")
    
    try:
        # Gömülü görseli yükle
        img = Image.open(image_path).convert('RGB')
        pixels = list(img.getdata())
        
        binary_data = ""
        message = ""
        end_marker = "###"
        
        # Her pikselin RGB değerlerinin son bitlerini topla
        for r, g, b in pixels:
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
            
            # Her 8 bit tamamlandığında karaktere çevir
            while len(binary_data) >= 8:
                # 8 bitlik grubu al
                byte = binary_data[:8]
                binary_data = binary_data[8:]
                
                try:
                    # Binary'i karaktere çevir
                    char = binary_to_char(byte)
                    message += char
                    
                    # Bitiş işaretini kontrol et
                    if message.endswith(end_marker):
                        return message[:-3]  # Bitiş işaretini çıkar
                except:
                    continue
        
        # Bitiş işareti bulunamadıysa veya mesaj boşsa
        if not message or end_marker not in message:
            raise ValueError("Görselde gizli mesaj bulunamadı veya mesaj bozuk!")
            
        return message.split(end_marker)[0]
        
    except Exception as e:
        raise ValueError(f"Mesaj çözülürken hata oluştu: {str(e)}")

if __name__ == "__main__":
    try:
        image_path = input("Gizli mesaj içeren görsel dosyasının adını girin (örn: encoded_image.png): ")
        message = decode_message(image_path)
        if message:
            print("✅ Çözülen mesaj:", message)
        else:
            print("❌ Mesaj bulunamadı!")
    except Exception as e:
        print(f"❌ Hata: {str(e)}")
