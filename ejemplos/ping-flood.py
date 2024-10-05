import os
import time

direccion = "192.168.0.18"
pings = 1000000
tamano = 1000
wait = 0.01

for _ in range(pings):
    os.system(f"ping -c 1 {direccion} -s {tamano}")
    time.sleep(wait)