# Bad Usb
## Description:
A bad usb device which uses an AtTiny85 to emulate a HID keyboard, run some powershell code.

## How to use it:
1. Modify the payload to fit your situation.
2. Flash it into your chip.
3. Run the bad_server.py(if you don't have Python environment, it's fine. Read the What-ifs section below).
4. Plug your chip into target computer and wait for some magic to happen.

## What-ifs:
### 1. What if I don't have a chip?
	Well... GO AND BUY ONE OR MAKE YOUR OWN ONE! You'll find it quite cheap on online shop. It's also very easy to build one.
	See http://digistump.com/products/1 for more details.
### 2. Okay, I have one but I can't flash the program. What happened?
	That's because you haven't got the right driver installed.
	See http://digistump.com/wiki/digispark/tutorials/connecting
### 3. Riiiiiight... I don't have Python environment, what now?
	Well... Use whatever programming language you have to create a TCP server and listen for 127.0.0.1:1234(by default).
	Plenty of examples can be found on Google.
### 4. Why does it have to connect my computer twice before my payload finally start to work?
	You've asked an excellent question!
	When you plug it in, the first thing is the bootloader waits for the connection from Arduino IDE. If there's no connection, then run your sketch.
	In your sketch, it loads the V-USB module, disconnect itself and reconnect as a HID device, hence act like it connected twice.
	In the future, I'll try to remove the bootloader and directly load the V-USB module and so on.