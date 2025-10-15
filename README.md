🚀 Smart Task Planner





🧠 Objective

Break user goals into actionable tasks with timelines, dependencies, and summaries — powered by AI reasoning (LLM).

🧩 Scope of Work

✅ Input:
User enters a goal (e.g., “Launch a product in 2 weeks”)

✅ Output:

Detailed task breakdown

Dependencies between tasks

Estimated timelines & durations

Beautiful bar graph visualization of project flow

✅ Frontend:

Clean and interactive web interface built with HTML, CSS, and JavaScript

Displays both text-based and visual plan output

✅ Backend:

Flask API processes user input and interacts with Gemini LLM to generate structured plans

⚙️ Technical Expectations

🧩 Backend API: Built using Flask

🤖 LLM: Google Gemini 1.5 Flash for reasoning and task generation

📊 Visualization: Task timelines displayed using bar charts for clarity

🧠 LLM Usage Guidance

The system uses prompting to guide the LLM into structured reasoning:

“Break down this goal into actionable tasks with suggested deadlines and dependencies.”

The response is parsed as JSON and rendered visually in the frontend.

📦 Deliverables

✅ GitHub Repository (this project)

✅ README.md (includes all project details)

✅ Demo Video (to be added after recording)

🧪 Evaluation Focus
Criteria	Description
Task Completeness	Full breakdown of goal into subtasks
Timeline Logic	Tasks ordered by duration and dependencies
LLM Reasoning	Uses structured prompting and AI planning
Code & API Design	Clean, modular Flask + Frontend integration
Visualization	Interactive bar graph showing task flow
🏗️ Project Structure
smart-task-planner/
│
├── app.py                # Flask backend
├── llm.py                # Gemini API integration logic
├── templates/
│   └── index.html        # Frontend UI
├── requirements.txt      # Dependencies
├── test_request.py       # Local testing script
├── list_models.py        # Model listing for Gemini API
└── .env                  # Environment variables (API keys)

🧰 Technologies Used

Frontend: HTML, CSS, JS

Backend: Flask (Python)

AI: Google Gemini 1.5 Flash

Visualization: Chart.js / D3.js (Bar Graphs)

Version Control: Git & GitHub

🚀 How to Run Locally

Clone the repo

git clone https://github.com/Afrin2627/Smart-Task-Planner.git
cd Smart-Task-Planner


Install dependencies

pip install -r requirements.txt


Set up your Gemini API key in .env:

GEMINI_API_KEY=your_api_key_here


Run the Flask app

python app.py


Open your browser and go to:
👉 http://127.0.0.1:5000


💡 Example Prompt & Output

Input:

“Build a mobile app for food delivery in 3 weeks”

AI Output (LLM Reasoning):

Task: Design UI – 3 days

Task: Build Backend – 5 days

Task: API Integration – 4 days

Task: Testing & Launch – 5 days

(Displayed in bar chart + text summary)
