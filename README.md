# arduino_proto

## Useful links

### Projects etc
https://realpython.com/arduino-python/

### Resistors
https://www.wikihow.com/Identify-Resistors
https://www.calculator.net/resistor-calculator.html

### WSL for Arduino with Python
https://learn.microsoft.com/en-us/windows/wsl/connect-usb#attach-a-usb-device
https://github.com/dorssel/usbipd-win
https://devicetests.com/fix-permission-denied-error-usb-devices-ubuntu

#### Connect the board to WSL for execution with Python
```shell
# PowerShell as admin
usbipd wsl list
usbipd wsl attach --busid <BUS ID>

# Ubuntu WSL
ll /dev/
# identify the device, usually as follows
sudo chmod a+rw /dev/ttyACM0
```