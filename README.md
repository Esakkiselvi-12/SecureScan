# 🔐 SecureScan – Web Vulnerability Scanner

SecureScan is a beginner-friendly web-based vulnerability scanning application developed for educational and academic purposes.  
It helps users understand how basic reconnaissance techniques such as open port scanning and server header analysis work in cybersecurity.

---

## 🚀 Features

- 🌐 Scan any website URL or IP address
- 🔍 Detect commonly open network ports
- 🧠 Identify server technology via HTTP headers
- 🖥️ Clean, responsive web interface
- 📄 Simple vulnerability result display
- 📬 Contact page for feedback
- 🎓 Safe & educational – no aggressive penetration testing

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Socket
- Requests

### Frontend
- HTML5
- CSS3
- JavaScript

### Deployment
- GitHub (Source Control)
- Render (Cloud Hosting)

---

## 📁 Project Structure

SecureScan/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── contact.html
│
├── static/
│   ├── style.css
│
├── README.md

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the Repository
git clone https://github.com/your-username/SecureScan.git  
cd SecureScan

---

### 2️⃣ Create Virtual Environment (Optional)
python -m venv venv  
venv\Scripts\activate  
source venv/bin/activate

---

### 3️⃣ Install Dependencies
pip install -r requirements.txt

---

### 4️⃣ Run the Application
python app.py

---

### 5️⃣ Open Browser
http://127.0.0.1:5000

---

## 🌍 Deployment on Render

### 1️⃣ requirements.txt
flask  
requests

---

### 2️⃣ Push to GitHub
git add .  
git commit -m "Initial SecureScan deployment"  
git push origin main

---

### 3️⃣ Render Deployment Steps

1. Go to https://render.com  
2. Click **New → Web Service**  
3. Connect your GitHub repository  
4. Configure:

Runtime: Python  
Build Command: pip install -r requirements.txt  
Start Command: python app.py  

5. Click **Deploy**

---

## ⚠️ Disclaimer

SecureScan is intended only for educational and learning purposes.  
Scan only websites that you own or have permission to test.  
Unauthorized scanning may be illegal.

---

## 👨‍💻 Author

Esakkiselvi M
Cybersecurity & Web Development Learner

---

## 📬 Contact

Use the Contact page in the application to send feedback or queries.

---

## ⭐ Support

If you like this project, please give a ⭐ to the repository.
