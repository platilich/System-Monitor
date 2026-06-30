from rich.console import Console
from rich.table import Table
from rich.text import Text

import psutil
import time
import os





#################### функции ####################

def get_cpu():
    return f'{psutil.cpu_percent(interval=1)} %'



def get_ram():
    return f'{psutil.virtual_memory().percent} %'


def get_disk():
    disk = psutil.disk_usage("/")
    used_gb = round(disk.used / (1024 ** 3))
    total_gb = round(disk.total / (1024 ** 3))

    return f'{used_gb}/{total_gb} GB'



def get_temp():
    try:
        temps = psutil.sensors_temperatures()


        return f'{temps} °C'

    except Exception as e:
        return f'{55}°C'




#################### основной код ####################


def main():


    console = Console(record=True)



    table = Table(title=Text('System Monitor', style='bold'), style='dark_green')

    table.add_column('CPU', justify='center', width=10)
    table.add_column('RAM', justify='center', width=10)
    table.add_column('Disk', justify='center', width=10)
    table.add_column('Temp', justify='center', width=10)



    cpu = str(get_cpu())
    ram = str(get_ram())
    disk = str(get_disk())
    temp = str(get_temp())

    table.add_row(cpu, ram, disk, temp)

    os.system('clear')



    console.print(table)



if __name__ == '__main__':
    while True:
        main()
        time.sleep(2)