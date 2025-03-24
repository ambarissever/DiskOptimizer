import os
import psutil

# Disk kullanım bilgisi
def disk_usage():
    print("Disk Kullanım Bilgisi:")
    disk = psutil.disk_usage('/')
    print(f"Toplam Alan: {disk.total / (1024 ** 3):.2f} GB")
    print(f"Boş Alan: {disk.free / (1024 ** 3):.2f} GB")
    print(f"Kullanılan Alan: {disk.used / (1024 ** 3):.2f} GB")
    print(f"Yüzde Kullanım: {disk.percent}%\n")

# Dosya uzantılarını extensions.txt dosyasından okuma
def load_extensions(filename="extensions.txt"):
    try:
        with open(filename, 'r') as file:
            extensions = [line.strip() for line in file.readlines() if line.strip()]
        return extensions
    except Exception as e:
        print(f"Hata: Uzantılar dosyası okunurken bir sorun oluştu: {e}")
        return []

# Dosya türlerine göre gereksiz dosyaları temizleme
def delete_unnecessary_files(directory, extensions):
    print(f"Gereksiz dosyaları temizleme işlemi başlatılıyor...")
    files_deleted = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                file_path = os.path.join(dirpath, filename)
                try:
                    os.remove(file_path)
                    files_deleted += 1
                    print(f"Silindi: {file_path}")
                except Exception as e:
                    print(f"Hata: {e}")
    print(f"Toplam silinen dosya sayısı: {files_deleted}\n")

# Disk temizliği için gereksiz dosya uzantıları
def clean_disk(directory, extensions):
    confirmation = input(f"Silme işlemini başlatmadan önce emin misiniz? (Evet/Hayır): ").strip().lower()
    if confirmation == 'evet':
        delete_unnecessary_files(directory, extensions)
    else:
        print("Silme işlemi iptal edildi.\n")

# Ana menü
def main():
    print("Dosya ve Disk Yönetim Aracı")
    extensions = load_extensions()  # Uzantıları dosyadan yükle

    if not extensions:
        print("Uzantılar dosyasından veri alınamadı. Program sonlandırılıyor.")
        return

    while True:
        print("\nSeçenekler:")
        print("1. Disk kullanım bilgilerini görüntüle")
        print("2. Gereksiz dosyaları temizle")
        print("3. Çıkış")
        choice = input("Seçiminizi yapın (1/2/3): ")

        if choice == '1':
            disk_usage()
        elif choice == '2':
            directory = input("Temizlemek istediğiniz dizini girin: ")
            if os.path.isdir(directory):
                clean_disk(directory, extensions)
            else:
                print("Geçersiz dizin.")
        elif choice == '3':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek.")

if __name__ == "__main__":
    main()
