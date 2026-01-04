import speech_recognition as sr

recognizer = sr.Recognizer()

# Robotik-optimierte Parameter
recognizer.energy_threshold = 300
recognizer.pause_threshold = 1.5
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.8

print("🎤 Sprachsteuerung bereit")

with sr.Microphone(sample_rate=16000) as source:
    print("🔇 Kalibriere Umgebungsgeräusche (NICHT sprechen!)")
    recognizer.adjust_for_ambient_noise(source, duration=1.5)
    print(f"✅ Energy Threshold: {recognizer.energy_threshold}")

    while True:
        try:
            print("🎙️ Sprich jetzt...")
            audio = recognizer.listen(
                source,
                timeout=7,
                phrase_time_limit=8
            )

            text = recognizer.recognize_google(audio, language="en-US")
            text = text.lower().strip()
            print("🗣️ Erkannt:", text)

        except sr.WaitTimeoutError:
            print("⏳ Keine Sprache gehört")
        except sr.UnknownValueError:
            print("⚠️ Sprache unverständlich")
        except sr.RequestError as e:
            print("❌ Google Speech Fehler:", e)

        print("-" * 40)
