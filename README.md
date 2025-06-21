# News Summary Web App

A full-stack web application that allows users to upload news articles (PDFs/images) and receive AI-generated summaries. Built using React (frontend), Flask (backend), and MongoDB (for storing summaries per user).

---

## Features

- User Authentication (Sign In / Sign Up)
- Upload PDFs or Images
- Extracts text using OCR and summarizes it using AI (BART model)
- Saves summaries in MongoDB per user
- View history of previous summaries

---

## Tech Stack

- Frontend: React, Tailwind CSS, React Router
- Backend: Flask, Transformers, pdf2image, pytesseract
- Database: MongoDB (via PyMongo)
- AI Model: `sshleifer/distilbart-cnn-12-6` from HuggingFace

---

## Project Structure

news-summary-project/
├── news-summary-backend/
│ ├── app.py
│ ├── utils/
│ ├── requirements.txt
│ └── .env ← MongoDB connection string here
├── news-summary-frontend/
│ ├── src/
│ ├── public/
│ ├── package.json
│ └── tailwind.config.js
├── .gitignore
└── README.md

yaml
Copy
Edit

---

## Local Setup Instructions

### 1. Clone the Repo

bash
git clone https://github.com/Sweedallewis19/news-summary.git
cd news-summary
2. Backend Setup
bash
Copy
Edit
cd news-summary-backend
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
Create a .env file:

env
Copy
Edit
MONGO_URI=mongodb://localhost:27017/news-summary
Also install Poppler for Windows and add it to PATH for pdf2image.

Run the backend:

bash
Copy
Edit
python app.py
3. Frontend Setup
bash
Copy
Edit
cd ../news-summary-frontend
npm install
npm start

Testing
Open your browser and go to http://localhost:3000
Sign in with any email
Upload a .pdf, .jpg, or .png
View summary and summary history

