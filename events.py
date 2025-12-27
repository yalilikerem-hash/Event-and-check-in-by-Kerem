def create_event(events, name, capacity, price):
    new_event = {
        "id": str(len(events) + 1),
        "name": name,
        "capacity": int(capacity),
        "price": float(price),
        "sessions": []
    }
    events.append(new_event)
    return new_event


def add_session(events, event_id, session_name):    
    for e in events:
        if e['id'] == event_id:
            e['sessions'].append(session_name)
            return True
    return False

    
