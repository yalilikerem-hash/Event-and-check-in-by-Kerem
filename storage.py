import json
import os

def load_state():
   
    if not os.path.exists('data'): os.makedirs('data')
    results = []
    for f in ['events.json', 'attendees.json', 'registrations.json']:
        path = os.path.join('data', f)
        if os.path.exists(path):
            with open(path, 'r') as file: results.append(json.load(file))
        else:
            results.append([])
    return results[0], results[1], results[2]

def save_state(events, attendees, regs):
    
    with open('data/events.json', 'w') as f: json.dump(events, f)
    with open('data/attendees.json', 'w') as f: json.dump(attendees, f)
    with open('data/registrations.json', 'w') as f: json.dump(regs, f)
