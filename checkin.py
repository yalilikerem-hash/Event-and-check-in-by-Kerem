def check_in(regs, reg_id):
    for r in regs:
        if r['id'] == reg_id:
            if r['status'] == "Onaylı":
                r['checked_in'] = True
                return "Giriş Başarılı!"
            else:
                return "Hata: Bekleme listesindekiler giriş yapamaz."
    return "Kayıt bulunamadı."
  
