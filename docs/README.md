# GEN AI Interviewer

## 📚 Project Overview
This project is a full-stack application that simulates a **voice-based AI interviewer** with real-time video, audio transcription, and dynamic question generation using GPT-4.

## 🎯 Key Features
- **Live Video/Audio:** Use LiveKit to create a seamless video/audio interface.
- **Speech-to-Text (STT) & Text-to-Speech (TTS):** Deepgram or OpenAI Whisper for transcriptions and voice output.
- **Dynamic Questioning:** GPT-4 generates follow-up questions based on responses.
- **Local Storage:** CV, JD, transcripts, and results stored in JSON files.

## 📂 Project Folder Structure
```
/gen-ai-interviewer
├── /backend
│   ├── /api
│   │   ├── interview.py       # Core interview logic (LLM, STT, TTS orchestration)
│   │   ├── livekit.py         # LiveKit API integration for video sessions
│   │   ├── storage.py         # Store and retrieve data locally (JSON handler)
│   │   └── __init__.py
│   ├── app.py                 # Flask/FastAPI backend entry point
│   └── requirements.txt       # Backend dependencies
├── /frontend
│   ├── /admin
│   │   ├── /components
│   │   ├── /pages
│   │   ├── AdminDashboard.jsx # Admin to upload CV, JD, and prompt
│   │   └── Results.jsx        # View candidate results
│   ├── /candidate
│   │   ├── /components
│   │   ├── /pages
│   │   └── InterviewRoom.jsx  # Candidate video/audio interface with LiveKit
│   ├── App.js                 # Main frontend file
│   └── package.json           # Frontend dependencies
├── /config
│   ├── config.json            # API keys, endpoints, and environment config
│   └── .env                   # Environment variables (optional)
├── /data
│   ├── transcripts.json       # Store interview transcripts
│   ├── results.json           # Store candidate results
│   └── prompts.json           # Store system prompts
├── /docs
│   └── README.md              # Setup instructions & usage guide
└── /scripts
    └── demo_script.py         # Optional demo automation script
```

## 🚀 Quick Setup
1. **Clone the Repo:**
```bash
git clone https://github.com/ritamnandy11/gen-ai-interviewer.git
```

2. **Navigate to Project:**
```bash
cd gen-ai-interviewer
```

3. **Install Backend Dependencies:**
```bash
cd backend
pip install -r requirements.txt
```

4. **Install Frontend Dependencies:**
```bash
cd ../frontend
npm install
```

## 🔥 Usage
- **Admin:** Upload CV, JD, and system prompt.
- **Candidate:** Join interview session, speak, and hear AI questions.
- **Results:** View candidate’s performance and rating at the end.

## ⚡️ API Keys & Config
- Add required API keys in `/config/config.json` or `.env` file.
- Configure LiveKit, Deepgram, and GPT-4 endpoints properly.

## 📖 Documentation
- Detailed documentation and demo scripts in the `/docs` folder.

---

## 🤝 Contribution Guidelines
Contributions are welcome! Feel free to fork and submit PRs.
