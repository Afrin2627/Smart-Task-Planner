from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
import os
import json
import re
from dotenv import load_dotenv

app = Flask(__name__, static_folder="templates", static_url_path="")

# ✅ Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_json(text):
    """Extract JSON-like list even if inside code fences or markdown."""
    text = text.replace("```json", "").replace("```", "").strip()
    match = re.search(r'\[.*\]', text, re.S)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            # Fallback: try to recover pseudo-JSON (lines starting with task names)
            items = []
            for block in re.split(r"\n\s*\n", match.group(0)):
                task_match = re.search(r"([A-Za-z].+?)\n", block)
                duration_match = re.search(r"🕒 Duration:\s*(.*)", block)
                dep_match = re.search(r"🔗 Dependencies:\s*(.*)", block)
                if task_match:
                    items.append({
                        "task": task_match.group(1).strip(),
                        "duration": duration_match.group(1).strip() if duration_match else "—",
                        "dependencies": [d.strip() for d in dep_match.group(1).split(",")] if dep_match else []
                    })
            return items
    return []

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    goal = data.get("goal", "")

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")

        prompt = f"""
        You are a senior project strategist.

        Task:
        1️⃣ Write a short motivational summary paragraph about the project goal.
        2️⃣ Then output a JSON array of tasks. Each task must have:
            - "task"
            - "duration"
            - "dependencies" (array)

        Goal: {goal}

        Example output:
        <summary paragraph>

        [
          {{"task": "Define MVP Scope", "duration": "1 day", "dependencies": []}},
          {{"task": "Build core app features", "duration": "5 days", "dependencies": ["Define MVP Scope"]}}
        ]
        """

        response = model.generate_content(prompt)
        text = response.text.strip()

        # Split summary and JSON
        summary = re.sub(r"```json.*", "", text, flags=re.S).strip()
        plan = extract_json(text)

        if not plan:
            plan = [{"task": "⚠️ Could not parse plan correctly.", "duration": "—", "dependencies": []}]

        return jsonify({
            "summary": summary,
            "plan": plan
        })

    except Exception as e:
        return jsonify({
            "summary": "",
            "plan": [{"task": f"Error: {str(e)}", "duration": "—", "dependencies": []}]
        })

if __name__ == "__main__":
    app.run(debug=True)
