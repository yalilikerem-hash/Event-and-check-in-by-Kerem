import random
from datetime import datetime
id = random.randint(10,812)

event_info = {
    "id":   id ,
    "name": "Kerem Yalılı",
    "location": "Nostalji Düğün Salonu",
    "start_date": datetime(8,16,2007) ,
    "end_date":  datetime(8,18,2007),
    "capacity": 500,
    "price": 100000               
}
   
def load_events():
