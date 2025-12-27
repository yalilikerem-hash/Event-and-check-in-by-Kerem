
import storage, events, registration, checkin

def main():
    
    E, A, R = storage.load_state()

    while True:
        print("\n1-Etkinlik Ekle  2-Kayıt Ol  3-Giriş Yap (Check-in)  4-Listele  5-Çıkış")
        islem = input("İşlem seçin: ")

        if islem == "1":
            n = input("Ad: "); c = input("Kapasite: "); p = input("Fiyat: ")
            events.create_event(E, n, c, p)
            print("Etkinlik eklendi.")

        elif islem == "2":
            eid = input("Etkinlik ID: "); mail = input("E-posta: ")
            print(registration.register(R, E, eid, mail))

        elif islem == "3":
            rid = input("Kayıt ID: ")
            print(checkin.check_in(R, rid))

        elif islem == "4":
            print("\n--- ETKİNLİKLER ---")
            for e in E: print(f"ID: {e['id']} | {e['name']} | Kapasite: {e['capacity']}")
            print("\n--- KAYITLAR ---")
            for r in R: print(f"ID: {r['id']} | Etkinlik: {r['event_id']} | Durum: {r['status']} | Giriş: {r['checked_in']}")

        elif islem == "5":
            storage.save_state(E, A, R) 
            print("Veriler kaydedildi. Çıkılıyor...")
            break

if __name__ == "__main__":
    main()
