def register(regs, events, event_id, email):
   
    event = next((e for e in events if e['id'] == event_id), None)
    if not event: return "Etkinlik bulunamadı!"

    confirmed_count = len([r for r in regs if r['event_id'] == event_id and r['status'] == 'Onaylı'])
    
    status = "Onaylı" if confirmed_count < event['capacity'] else "Bekleme Listesi"
    
    new_reg = {
        "id": str(len(regs) + 100),
        "event_id": event_id,
        "email": email,
        "status": status,
        "checked_in": False
    }
  
    regs.append(new_reg)
    return f"Kayıt Tamamlandı! Durum: {status}"
