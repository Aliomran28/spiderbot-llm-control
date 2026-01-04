import json
import serial
import time
from robot_llm import ask_robot_llm

ser = serial.Serial("COM5", 115200, timeout=1)
time.sleep(2)

while True:
    user_text = input(">> ")
    response = ask_robot_llm(user_text)
    print("LLM:", response)

    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        print("⛔ Invalid JSON")
        continue

    cmd = data.get("cmd", "INVALID").strip().upper()

    if cmd == "FORWARD":
        ser.write(b'F')
        print("✅ FORWARD sent")
    elif cmd == "BACKWARD":
        ser.write(b'B')
        print("✅ BACKWARD sent")
    elif cmd == "LEFT":
        ser.write(b'L')
        print("✅ LEFT sent")
    elif cmd == "RIGHT":
        ser.write(b'R')
        print("✅ RIGHT sent")
    elif cmd == "STOP":
        ser.write(b'S')
        print("✅ STOP sent")
    else:
        print("⛔ Befehl ignoriert")
