🧠 Smart Task Planner: AI-Powered Goal Breakdown & Timeline Generator
⭐ Project Vision: Turning Ambition into Action

This project transforms high-level user goals into structured, time-bound action plans using LLM reasoning.
It intelligently analyzes your objective — whether it’s “Launch a product in 2 weeks” or “Prepare for a data science interview” —
and outputs a detailed, dependency-aware project plan with visual task timelines (bar graphs).

🛠️ Technical Architecture & Stack
Component	Technology	Purpose
🧩 Backend API	Flask (Python)	Handles requests, processes user input
🤖 LLM Engine	Google Gemini 1.5 Flash	Performs task reasoning & timeline generation
🎨 Frontend/UI	HTML, CSS, JavaScript	Interactive interface for user input & visualization
📊 Visualization	Chart.js (Bar Graphs)	Displays task timelines & dependencies
🔐 Environment	.env	Stores API keys securely
⚙️ Architectural Flow

Goal Input → User enters a project goal (e.g., “Build an app in 10 days”).

Processing Layer (Flask) → Sends the input to Gemini via the backend.

LLM Reasoning → The model generates a structured plan with dependencies & durations.

Visualization Layer → Tasks and timelines are displayed using interactive bar charts.

🧠 LLM Prompting Strategy

“Break down this goal into actionable tasks with suggested deadlines and dependencies.”

The prompt is designed to make the LLM output structured, concise, and logically sequenced tasks.
This ensures clarity, efficient execution, and visually appealing task timelines.

🧩 Scope of Work

✅ Input:
User-provided goal text (e.g., “Launch a product in 2 weeks”)

✅ Output:

Detailed Task Breakdown

Dependencies & Timelines

Visual Bar Graphs (Timeline Representation)

✅ Frontend:
Elegant web interface with interactive visualization

✅ Backend:
Flask API integrated with Google Gemini API for reasoning and plan generation

🚀 Final Deliverables
Deliverable	Status
🧠 AI-Generated Project Plans	✅ Working
📊 Visual Task Timeline	✅ Implemented
💻 Flask API	✅ Live locally
🎨 Frontend UI	✅ Interactive
📦 GitHub Repo + README	✅ Completed
✅ Evaluation Focus
Metric	Description
Task Completeness	Goal fully broken down into logical subtasks
Timeline Logic	Dependencies and durations make realistic sense
LLM Reasoning	Proper use of Gemini’s structured thinking
Code Quality	Modular Flask design with clear separation of logic
Visualization	Intuitive bar chart display for users
⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/Afrin2627/Smart-Task-Planner.git
cd Smart-Task-Planner

2️⃣ Create Virtual Environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment

Create a .env file in the root directory:

GEMINI_API_KEY=your_api_key_here

5️⃣ Run the Application
python app.py


Open your browser → http://127.0.0.1:5000

🎯 Example Run — “Launch a New Mobile App in 1 Month”

Here’s how Smart Task Planner transforms a high-level goal into a structured, time-bound project plan using AI reasoning.

🧩 Input Goal

“Launch a new mobile app in 1 month”

🤖 AI-Generated Project Plan

The system intelligently breaks down the goal into clear, sequential tasks with:

Defined phases and subtasks

Estimated durations (in days)

Logical dependencies between steps

Visual timeline representation for progress tracking



Highlights:

Clearly shows key project stages — Design, Backend Setup, Testing, App Store Launch, etc.

Estimates realistic durations for each stage to fit within 1 month.

Provides an intuitive timeline overview to help plan execution efficiently.

💡 Behind the Scenes — LLM Reasoning

The AI prompt used:

“Break down this goal into actionable tasks with suggested deadlines and dependencies.”

Using this, the Gemini 1.5 Flash model interprets the goal contextually — generating well-structured, sequential tasks with logical flow and timeline accuracy.

🧠 Insight

The Smart Task Planner acts like your AI-powered project manager — turning ambitious ideas into executable plans, backed by structured logic and clear visualization.

🏁 Conclusion

This project showcases end-to-end AI reasoning — from understanding user intent to delivering a realistic, visually guided plan.
It’s a demonstration of how LLMs + visualization can revolutionize goal management, planning, and execution.



🧰 Technologies Used

Frontend: HTML, CSS, JS

Backend: Flask

AI Model: Google Gemini 1.5 Flash

Visualization: Chart.js

Version Control: Git & GitHub


💡 Future Enhancements

✅ Add database support for saving task plans

✅ Allow plan export (PDF/Excel)

✅ Integrate real-time collaboration via socket-based UI
