import os
import sys
import time
import webbrowser
import threading
from server import app

def open_browser():
    time.sleep(1.2)
    url = "http://127.0.0.1:5000"
    print(f"[*] Opening RUNNN at {url}")
    webbrowser.open(url)

if __name__ == '__main__':
    print("==================================================================")
    print("             RUNNN - A Horror Game Where The Rules Change         ")
    print("           Faithful Recreation of abho & Vystel's Masterpiece     ")
    print("==================================================================")
    print("  Controls: WASD / Arrows = Move | Shift = Run")
    print("  Space / E = Interact / Pick Up / Fuel Furnace / Eat Carrot")
    print("  Left Click / F = Throw Rock | TAB = View Rules | P = Pause")
    print("==================================================================")
    
    # Launch browser in a background thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Start Flask Server
    try:
        app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
    except KeyboardInterrupt:
        print("\n[!] Game server terminated.")
