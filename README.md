# Mon Key
# BLE Keyboard 

## Description

This project turns an ESP32 into a Bluetooth keyboard. The idea is simple: when you connect your computer to the ESP32 via Bluetooth, any key you press on your keyboard is sent to the ESP32, which then transmits it back over Bluetooth as if it were a real wireless keyboard.

To make it work, you need to:
1. Pair your ESP32 with your computer via Bluetooth
2. Start the Python script on your PC, which listens for key event
3. Open the Serial Monitor in Arduino IDE (this seems to be necessary for the communication between the ESP32 and the computer. without it, the ESP32 might not receive the keystrokes)

Once everything is set up, each key you type on your computer is forwarded to the ESP32 over serial, and the ESP32 then sends it as a Bluetooth HID input. This effectively makes your ESP32 act as a wireless keyboard.

## Depedencies

You need to use python3 and .ino code wich python will be a deamon script on your PC and .ino will be flashed in the ESP32. 

### Venv
If you are in 'Arch' or other distrib that don't accept pip install directly you will need venv to run the following, otherwise you don't need to use it. The installation with Arch is :
''' 
sudo pacman -S python-venv
'''

A venv environment is already installed in 'esp32/' so go to it with
'''
cd esp32
'''

And run
'''
source bin/activate
'''

### Python Dependencies
To install the required Python dependencies, if not go to 'esp32/BLE_Keyboard/' file with 
'''
cd esp32/BLE_Keyboard/
'''

And then simply run
'''
pip install -r requirements.txt
'''

### Arduino Libraries

For the ESP32 firmware, you need to install some Arduino libraries. There are two ways to do this, depending on your setup :

**Using Arduino IDE**
1. Open 'Arduino IDE'
2. Go to 'Sketch > Include Library > Manage Libraries'
3. Search for the required libraries wich is 'Arduino.h'
4. And install it

**Using PlatformIO**
1. Open your project in VS Code with PlatformIO installed
2. Open 'platformio.ini' and add the necessary libraries under the '[env]' section
3. If not go to 'esp32/' file and Run
'''
pio lib install
'''

## Launch

1. Flash the esp32 with 'BLE_Keyboard.ino' with Arduino-IDE or PlatformIO
2. When the ESP32 is flashed a Bluetooth access point will apear. Connect your computer to it
3. Start the python deamon program with
- Arch (or using venv)
'''
sudo env "PATH=$PATH" python3 BLE_Keyboard/Send_keystroke_ESP32.py
'''
- Else
'''
sudo python3 BLE_Keyboard/Send_keystroke_ESP32.py
'''
4. Here the Bluetooth keyboard should not be working (it wase the case for me) so you can open the 'serial monitor' with PlatformIO or Arduino-IDE

Here you can leave these windows in background and you should see that every key pressed, it will wait a bit a pressed it again without doing anything.