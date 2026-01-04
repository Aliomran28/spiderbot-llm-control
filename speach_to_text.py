import speech_recognition as sr
import sounddevice as sd

def listen_forever():
    recognizer = sr.Recognizer()

    fs = 16000          # Abtastrate
    duration = 5        # Aufnahme pro Durchlauf (Sekunden)

    print("🎤 Sprachsteuerung gestartet.")
    print("👉 Sprich einen Befehl (z. B. 'forward', 'right').")
    print("👉 Sage 'stop' oder 'aufhören', um zu beenden.\n")

    while True:
        print("🎙️ Aufnahme läuft...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()

        audio_data = sr.AudioData(audio.tobytes(), fs, 2)

        try:
            text = recognizer.recognize_google(audio_data, language="en-US")
            text = text.lower().strip()
            print("🗣️ Erkannt:", text)

            # 🛑 Stopp-Bedingung
            if text in ["stop", "aufhören", "exit", "quit"]:
                print("🛑 Sprachsteuerung beendet.")
                break

            # 👉 Hier später an LLM weiterleiten
            # z.B.: command = ask_robot_llm(text)

        except sr.UnknownValueError:
            print("⚠️ Sprache nicht verstanden.")
        except sr.RequestError as e:
            print("❌ Fehler beim Speech-Service:", e)

        print("-" * 40)

if __name__ == "__main__":
    listen_forever()
