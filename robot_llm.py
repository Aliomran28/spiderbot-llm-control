import subprocess

def ask_robot_llm(user_input: str):
    prompt = f"""
You are a robot command interpreter.

Your task:
- Understand natural language commands.
- Ignore polite words, filler words, insults, and irrelevant text.
- Detect ONLY the robot movement intent.

Valid intents:
- FORWARD
- BACKWARD
- LEFT
- RIGHT
- STOP

Words / sentences that mean FORWARD:
- forward
- go forward
- please go forward
- move forward
- can you move forward
- forward dummy
move forward now
- go ahead      
move ahead
- ahead 
- proceed   

Words / sentences that mean BACKWARD:
- back
- go back
- move back
- backward
- go backward
- back please

Words / sentences that mean LEFT:
- left
- go left
- move left
- turn left

Words / sentences that mean RIGHT:
- right
- go right
- move right
- turn right

Rules:
- If intent is FORWARD output:
  {{"cmd":"FORWARD"}}
- If intent is BACKWARD output:
  {{"cmd":"BACKWARD"}}
- If intent is LEFT output:
  {{"cmd":"LEFT"}}
- If intent is RIGHT output:
  {{"cmd":"RIGHT"}}
- If intent is STOP output:
  {{"cmd":"STOP"}}
- Otherwise output:
  {{"cmd":"INVALID"}}

Output rules:
- Output ONLY valid JSON
- No explanations
- No extra text

User input: "{user_input}"
"""

    result = subprocess.run(
        ["ollama", "run", "gemma3:1b"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
