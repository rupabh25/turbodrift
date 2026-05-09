# 🚗 Turbo Drift

Turbo Drift is an AI-powered car price prediction web application developed using **Python, Streamlit, Scikit-learn, and SQLite**. The application predicts the estimated resale price of a car based on multiple vehicle parameters such as fuel type, kilometers driven, ownership history, transmission type, and car age.

---

## ✨ Features

* 🔐 Secure Login & Signup System
* 🔑 Password Hashing using Bcrypt
* 🧠 Machine Learning Based Car Price Prediction
* 📊 Interactive and Modern Streamlit UI
* 🗂 SQLite Database Integration
* 🚪 Session-Based Authentication & Logout System
* 📈 Dynamic Price Trend Visualization

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* SQLite3
* Bcrypt
* Joblib

---

## 📂 Project Structure

```bash
TurboDrift/
│
├── pages/
│   ├── 1_Predict_Price.py
│   └── 3_Car_Chatbot.py
│
├── app.py
├── auth.py
├── predict_price.py
├── train_model.py
├── car_data.csv
├── car_price_model.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/rupabh25/turbodrift.git
cd turbodrift
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run Application

```bash
python -m streamlit run app.py
```

---

## 🔒 Authentication System

Turbo Drift includes a secure authentication system using:

* SQLite Database
* Password Hashing with Bcrypt
* Session-Based Login Protection
* Logout Functionality

Passwords are securely hashed before being stored in the database.

---

## 📸 Screenshots

### 🔑 Login Page

*Add screenshot here*

### 🚘 Prediction Dashboard

*Add screenshot here*

### 💰 Predicted Price Output

*Add screenshot here*

---

## 🚀 Future Improvements

* 🤖 AI Chatbot Enhancements
* ☁️ Cloud Deployment
* 📱 Fully Responsive UI
* 📊 Real-Time Market Data Integration
* 👨‍💼 Admin Dashboard
* 📈 Better Analytics & Visualization

---

## 👨‍💻 Contributors

* Rupabh Shrivastava
* Samarth Pandya
* Rudra Patidar

---

## 📄 License

This project is developed for educational and learning purposes.
