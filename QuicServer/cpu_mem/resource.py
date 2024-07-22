import time 
import psutil 
from psutil import cpu_percent, virtual_memory

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = ' ' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    
    with open('cpu_info.txt', 'a') as file:
        file.write(f"{str(cpu_usage)}\n")
        file.close()

    mem_percent = (mem_usage / 100.0)
    mem_bar = ' ' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    
    with open('mem_info.txt', 'a') as file:
        file.write(f"{str(mem_usage)}\n")
        file.close()

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}% ", end="")

    print()

    print(f"\rMEM Usage: |{mem_bar}| {mem_usage:.2f}% ", end="")
    print()

iter = 200
count = 1
while count <= iter:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 50)
    time.sleep(1)
    count = count + 1
