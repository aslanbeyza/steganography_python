# Metni görsele gömer
# encode.py

from PIL import Image
import os
from utils.helpers import char_to_binary, split_into_triplets

def encode_message(image_path, message, output_path):
    # Mesajı kontrol et
    if not message:
        raise ValueError("Mesaj boş olamaz!")
    
    # Bitiş işareti ekle
    message += '###'
    
    try:
        # Binary mesajı oluştur
        binary_message = ''.join([char_to_binary(c) for c in message])
        print(f"🔢 Gömülecek bit sayısı: {len(binary_message)}")
        
        # Görseli yükle
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Görsel bulunamadı: {image_path}")
            
        img = Image.open(image_path).convert('RGB')  # RGB moduna çevir
        pixels = list(img.getdata())  # Piksel verilerini liste olarak al
        width, height = img.size
        
        # Mesajın sığabileceği maksimum piksel sayısını kontrol et
        max_bits = width * height * 3
        if len(binary_message) > max_bits:
            raise ValueError(f"Mesaj çok uzun! Maksimum {max_bits//8} karakter sığabilir.")
        
        # Binary'i 3 bitlik parçalar halinde böl
        triplets = split_into_triplets(binary_message)
        new_pixels = []
        
        idx = 0
        # Piksel piksel gezer, RGB değerlerinin son bitlerine veri gömer
        for i, (r, g, b) in enumerate(pixels):
            if idx < len(triplets):
                t = triplets[idx]
                # Son bitleri değiştir
                r = (r & ~1) | int(t[0])
                g = (g & ~1) | int(t[1])
                b = (b & ~1) | int(t[2])
                idx += 1
            new_pixels.append((r, g, b))
        
        # Yeni görsel oluştur
        new_img = Image.new('RGB', (width, height))
        new_img.putdata(new_pixels)
        
        # PNG formatında kaydet (kayıpsız sıkıştırma)
        output_path = output_path.rsplit('.', 1)[0] + '.png'
        new_img.save(output_path, 'PNG')
        return True
        
    except Exception as e:
        raise ValueError(f"Mesaj gömülürken hata oluştu: {str(e)}")

if __name__ == "__main__":
    try:
        message = input("Gizlenecek mesajı girin: ")
        image_path = input("Kaynak görsel dosyasının adını girin (örn: image.jpg): ")
        output_path = input("Çıktı görsel dosyasının adını girin (örn: encoded_image.png): ")
        
        if encode_message(image_path, message, output_path):
            print(f"✅ Mesaj başarıyla '{output_path}' içerisine gizlendi.")
    except Exception as e:
        print(f"❌ Hata: {str(e)}")
