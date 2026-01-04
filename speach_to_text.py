import serial
import time
import speech_recognition as sr

# ================= SERIAL =================
PORT = "COM5"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)
print("✅ ESP32 verbunden")

# ================= SPEECH =================
recognizer = sr.Recognizer()
mic = sr.Microphone()

# ================= COMMAND MAPPING =================
def map_command(text: str):
    text = text.lower()

    if "forward" in text or "move" in text or "go" in text:
        return b"F"
    if "back" in text or "backward" in text:
        return b"B"
    if "left" in text:
        return b"L"
    if "right" in text:
        return b"R"
    if "stop" in text:
        return b"S"

    return None

print("🎤 Sag: forward / back / left / right / stop")

# ================= MAIN LOOP =================
while True:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎧 Höre zu...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("🗣️ Gesagt:", text)

        cmd = map_command(text)
        if cmd:
            ser.write(cmd)
            print("➡️ Gesendet:", cmd)
        else:
            print("⚠️ Kein gültiger Befehl erkannt")

    except sr.UnknownValueError:
        print("❌ Sprache nicht verstanden")
    except sr.RequestError as e:
        print("❌ Speech API Fehler:", e)
