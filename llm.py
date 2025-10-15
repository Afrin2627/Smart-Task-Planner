import google.generativeai as genai
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

PROMPT = """
You are an expert project manager helping a startup team plan efficiently.

Task: Convert the following goal into a clear, realistic, and motivating project plan.

Output format:
1️⃣ A short, motivating summary paragraph (2–3 sentences) explaining the overall strategy and focus.
2️⃣ Then, a detailed, structured task breakdown in valid JSON format.

The JSON array should follow this structure exactly:
[
  {"task": "Define MVP scope & success metrics", "duration": "1 day", "dependencies": []},
  {"task": "Set up GitHub repo & CI/CD pipeline", "duration": "1 day", "dependencies": ["Define MVP scope & success metrics"]}
]

Rules:
- The summary should sound natural, confident, and concise.
- The JSON should include realistic, actionable tasks with dependencies.
- Avoid vague or generic items (“Plan marketing strategy”, “Do QA”) — make them specific.

Goal:
"""



def extract_json(text: str):
    try:
        match = re.search(r'\[.*\]', text, re.S)
        if match:
            json_str = match.group(0)
            return json.loads(json_str)
        return None
    except Exception:
        return None

def generate_plan(goal):
    model = genai.GenerativeModel("models/gemini-2.5-flash")  # ✅ Updated model
    response = model.generate_content(PROMPT + goal)
    text = response.text.strip()
    plan = extract_json(text)
    if plan:
        return plan
    else:
        return [{"task": "Error generating plan", "duration": "—", "dependencies": []}]
