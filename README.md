# Bad Usb
## Description:
A bad usb device which uses an AtTiny85 to emulate a HID keyboard, run some powershell code to gain reversed TCP shell.

## DISCLAIMER!!!
This project is only for study purposes, DO NOT USE IT AGAINST THE LAW!!!
I don't take any responsibility for abused use!!!

## Requirements
1. A chip with USB port and AtTiny85 on it, DigiSpark made this kind of things and work well.
2. Arduino IDE with DigiSpark AVR add-on installed.
3. A target computer(you can use your own one).
4. A server which had python and flask preinstalled.

## How to use it:
1. Open the bad_usb.ino file with Arduino IDE, change the IP address to your server.
2. Flash it into your chip.
3. Run the bad_server.py on your computer, or deploy it to your server.
4. Plug your chip into target computer.
5. Open http://*yourserver*:80/index to gain a reversed TCP shell, where yourserver is localhost if you run it locally.

## What-ifs:
### 1. What if I don't have a chip?
#### Well... GO AND BUY ONE OR MAKE YOUR OWN ONE! You'll find it quite cheap on online shop. It's also very easy to build one.
#### See http://digistump.com/products/1 for more details.
### 2. Okay, I have one but I can't flash the program. What happened?
#### That's because you haven't got the right driver installed.
#### See http://digistump.com/wiki/digispark/tutorials/connecting
### 3. Riiiiiight... I don't have Python environment, what now?
<del>
#### Well... Use whatever programming language you have to create a TCP server and listen for 127.0.0.1:1234(by default).
#### Plenty of examples can be found on Google.
</del>
#### Install one, obviously.
### 4. Why does it have to connect target computer twice before my payload kick in?
#### You've asked an excellent question!
#### When you plug it in, the first thing is that the bootloader waits for the connection from Arduino IDE.
#### After waited for a while, it loads the V-USB module, disconnect itself and reconnect as a HID device, hence act like it was connecting twice.
#### In the future, I'll try to remove the bootloader and directly load the V-USB module.
### 5. I open the website as you told, but a 'No connection' showed in the textaera?
#### Make sure the payload worked properly on the target machine, since moden AVs and UAC blocks powershell from running, especially with param '-ep bypass' which is to bypass all the privillege check, and the param '-w hid' which is to run powershell windowless. You can modify the code to fit your situation.