import keyboard
import serial
import time

print("Appuie sur une touche (CTRL+C pour arrêter)")

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

key_map = {
    "enter": "\n",  # Touche Entrée
    "backspace": "\b",  # Retour arrière
    "space": " ",  # Espace
    "tab": "\t",  # Tabulation
    "esc": "\x1b",  # Échappement
    "delete": "\x7f",  # Suppr
    
    # Chiffres et symboles
    "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0",
    "!": "!", "@": "@", "#": "#", "$": "$", "%": "%", "^": "^", "&": "&", "*": "*", "(": "(", ")": ")",
    "-": "-", "_": "_", "=": "=", "+": "+", "[": "[", "]": "]", "{": "{", "}": "}", "\\": "\\", "|": "|",
    ";": ";", ":": ":", "'": "'", "\"": "\"", ",": ",", "<": "<", ".": ".", ">": ">", "/": "/", "?": "?",
    
    # Lettres (min et maj)
    "a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h", "i": "i", "j": "j",
    "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t",
    "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z",
    "A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F", "G": "G", "H": "H", "I": "I", "J": "J",
    "K": "K", "L": "L", "M": "M", "N": "N", "O": "O", "P": "P", "Q": "Q", "R": "R", "S": "S", "T": "T",
    "U": "U", "V": "V", "W": "W", "X": "X", "Y": "Y", "Z": "Z",
    
    # Touches de fonction
    "f1": "\x3a", "f2": "\x3b", "f3": "\x3c", "f4": "\x3d", "f5": "\x3e", "f6": "\x3f", "f7": "\x40",
    "f8": "\x41", "f9": "\x42", "f10": "\x43", "f11": "\x44", "f12": "\x45",
    
    # Autres touches spéciales
    "caps lock": "\x39", "num lock": "\x53", "scroll lock": "\x47", "insert": "\x49", "home": "\x4a",
    "page up": "\x4b", "page down": "\x4e", "print screen": "\x46",
    
    # Touches fléchées
    "left": "\x50", "right": "\x4f", "up": "\x52", "down": "\x51"
}

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP:
        key_to_send = key_map.get(event.name, event.name)
        ser.write(key_to_send.encode())
        print(f"Touche envoyée : {key_to_send}")