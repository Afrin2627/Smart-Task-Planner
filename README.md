# Smart Task Planner

An **AI-powered task planning app** that generates optimized task plans based on your goals using OpenAI API.  
Designed to help users **organize tasks efficiently** and increase productivity.

![image_alt](https://github.com/Afrin2627/Smart-Task-Planner/blob/c5b09ed58d0a7b491b0d26608ab8b8f9546735f1/img.png)


🖼️ Demo

https://github.com/user-attachments/assets/855deb19-dc39-424a-ac5c-67aa8156e27b

---

## 🌟 Features
- Generate intelligent task plans for any goal.
- Prioritize tasks automatically based on importance and time.
- Web-based interface using **Flask**.
- Clean and user-friendly frontend with HTML/CSS.
- Optional audio or system notifications for task reminders.

---

## 🛠️ Technologies Used
- **Backend:** Python, Flask, OpenAI API
- **Frontend:** HTML, CSS, JavaScript
- **Environment Management:** `.env` file for API keys
- **Version Control:** Git & GitHub

---

## 📁 Folder Structure
Smart-Task-Planner/
│
├── backend/
│ ├── app.py # Flask application
│ ├── requirements.txt # Python dependencies
│
├── frontend/
│ ├── index.html # Frontend page
│
├── images/ # Screenshots / GIFs
│
├── .gitignore
└── README.md

yaml
Copy code

---

## ⚡ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Afrin2627/Smart-Task-Planner.git
Navigate to backend

bash
Copy code
cd Smart-Task-Planner/backend
Install dependencies

bash
Copy code
pip install -r requirements.txt
Create a .env file in the backend/ folder:

ini
Copy code
OPENAI_API_KEY=your_openai_api_key_here
Run the Flask app

bash
Copy code
python app.py
Open in your browser
Go to http://127.0.0.1:5000 to use the app.




📝 Usage Instructions
Open the app in your browser.

Enter your goal in the input field.

Click Generate Plan.

The AI generates a smart, prioritized task list.

Optionally, save the plan for reference.

⚠️ Important Notes
API key is not included in this repo for security reasons.
Create your own .env file as shown in setup instructions.

Make sure Python 3.x is installed.

For large goals, generating plans may take a few seconds.

👨‍💻 Future Enhancements
Multi-language support for international users.

Mobile-friendly interface.

Integration with calendar apps (Google Calendar / Outlook).

Notifications and reminders for tasks.

📂 License
This project is open source and available under the MIT License.

Made with ❤️ by Afrin2627
