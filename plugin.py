import sys
import time
from datetime import datetime
from typing import Dict,Callable

def digital_clock():
    colores = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
    indice_color = 0
    
    try:
        while True:
            ahora = datetime.now()
            hora = ahora.strftime("%H:%M:%S")
            fecha = ahora.strftime("%d/%m/%Y")
            
            # Cambiar color cíclicamente
            color = colores[indice_color % len(colores)]
            indice_color += 1
            
            # Limpiar y mostrar
            sys.stdout.write("\033c")
            sys.stdout.write(f"""
{color}
╔════════════════════════════╗
║                            ║
║      \033[1mRELOJ DIGITAL\033[0m{color}    ║
║                            ║
║    ╔══════════════════╗    ║
║    ║                  ║    ║
║    ║   \033[97m{hora}\033[0m{color}   ║    ║
║    ║   \033[97m{fecha}\033[0m{color}  ║    ║
║    ║                  ║    ║
║    ╚══════════════════╝    ║
║                            ║
╚════════════════════════════╝
\033[0m""")
            sys.stdout.flush()
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\n\n⏱️  Reloj detenido")


def main():
    digital_clock()

def install():
    print("Digital-Clock")

def register_command() -> Dict[str, Callable]:
    return {
            "digital_clock": digital_clock
            }
digital_clock()
