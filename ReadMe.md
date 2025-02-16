## Problem Statement: Travel&Go - A Smart Travel Guide and Language Translator

## Introduction:
Welcome to Travel&Go! This app enhances your travel experience by providing multilingual guidance, real-time translations, and AI-powered travel utilities.

## Technologies Used:
- **Frontend:** Flutter (Dart)
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **AI Tools:** Automatic Language Identification, Speech-to-Text, and Text-to-Speech models.

## Key Features:
### 1. **Travel Guide with Language Preferences**
- **Multilingual Travel Content:** Get tourist information in your preferred language.
- **City & Landmark Information:** Explore historical sites, attractions, and must-visit places.
- **Transport Guidance:** Learn about public transport, taxis, and the best travel routes.
- **Local Cuisine & Restaurants:** Get restaurant recommendations based on reviews.
- **Emergency Assistance:** Auto-translate emergency phrases for quick help.
- **Offline Mode:** Downloadable city guides for offline access.

### 2. **Voice-Based Language Communicator**
- **Real-Time Speech-to-Text Conversion:** Recognizes and transcribes speech instantly.
- **Language Detection:** Identifies the spoken language automatically.
- **Instant Text Translation:** Supports multiple language translations in real-time.
- **Speech Synthesis:** Reads out translated text with proper pronunciation.
- **Offline Mode:** Supports limited language translations without an internet connection.

### 3. **Enhanced Travel Utilities**
- **Weather Forecasting:** Provides real-time weather updates for your destination.
- **Currency Converter:** Displays live exchange rates and allows offline conversions.
- **Travel Expense Manager:** Tracks expenses and budgets during trips.
- **Local Event Recommendations:** Suggests concerts, festivals, and events in the area.

### 4. **Smart Language Detection Mechanism**
- **Location-Based Detection:** Uses GPS to suggest the most spoken language in the region.
- **AI-Based Language Identification:** Uses AI models to detect spoken language in real-time.
- **User-Assisted Selection:** If detection fails, users can manually select the language.

## Installation
Follow these steps to set up the project in your local environment.

### **Prerequisites**
- Android Studio installed
- Flutter SDK installed
- VS Code installed
- Python 3.12.2 installed
- Git installed
- PostgreSQL installed

### **1. Clone the Repository**
```bash
git clone https://github.com/sangeetanandanvishal04/Travel-Go.git
```

### **Backend Setup in VS Code**
#### **2. Create and Activate a Virtual Environment**
```bash
python3 -m venv venv
```
- **For Windows:** `venv\Scripts\activate`
- **For macOS/Linux:** `source venv/bin/activate`

#### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **4. Set Up PostgreSQL Database**
Create a PostgreSQL database and update the `.env` file with:
```env
DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_PASSWORD = "YOUR_DATABASE_PASSWORD"
DATABASE_NAME = "YOUR_DATABASE_NAME"
DATABASE_USERNAME = "YOUR_DATABASE_USERNAME"
SECRET_KEY = 09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 300
```

#### **5. Set Up SMTP Email Configuration**
Update `.env` file with your email credentials:
```env
EMAIL = "YOUR_EMAIL"
SMTP_PASSWORD = "YOUR_SMTP_PASSWORD"
```

**Steps to get SMTP Password:**
1. Go to Google Account Settings → Security.
2. Navigate to "Signing in to other sites."
3. Generate an App Password for email authentication.

### **Frontend Setup in Android Studio**
Find the frontend code and setup instructions at:
- [Frontend Code](https://github.com/sangeetanandanvishal04/Travel-Go.git)

### **9. Run the Application**
Start the FastAPI Server:
```bash
uvicorn FastAPI.main:app --reload
```
Run the Flutter app inside Android Studio.

---
Enjoy a seamless travel experience with **Travel&Go!**