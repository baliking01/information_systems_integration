from zeep import Client
import time
import random

wsdl_url = 'http://localhost:8000/?wsdl'
client = Client(wsdl_url)

colors = ['RED', 'GREEN', 'BLUE']

while True:
    color = random.choice(colors)
    response = client.service.process_color(color)
    print(f"Sent: {color}")
    time.sleep(1)