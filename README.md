# **Multi-Domain ChatBot** 🤖  

An AI-powered chatbot capable of handling conversations across multiple domains, including **General, Medical, Financial, and Legal** topics. Built using **LangChain**, **Google Generative AI (Gemini 1.5 Flash)**, and **Gradio** for an intuitive user experience.

---

## **🔹 Features** ✨
✔ Multi-domain support (**General, Medical, Financial, Legal**)  
✔ Intelligent responses via **Google Generative AI (Gemini 1.5 Flash)**  
✔ Interactive **Gradio** UI for seamless user interaction  
✔ Secure API key management using **environment variables**  
✔ Lightweight, efficient, and easy to deploy  

---

## **🛠 Installation & Setup** 🚀

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/multi-domain-chatbot.git
cd multi-domain-chatbot
```

### **2️⃣ Set Up Virtual Environment (Optional)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure API Key** 🔑  
#### **Option 1: Local Setup (For Development)**
Create a `.env` file in the project directory and add your API key:
```bash
GOOGLE_API_KEY=your_api_key_here
```

#### **Option 2: GitHub Actions (For Deployment)**
- Go to **GitHub Repository** → **Settings** → **Secrets and Variables** → **Actions**.
- Click **New Repository Secret**.
- Name it `GOOGLE_API_KEY` and paste your API key.

---

## **🚀 Usage**
Run the chatbot with:
```bash
python app.py
```
Then, open **[http://127.0.0.1:7862/](http://127.0.0.1:7862/)** in your browser and start chatting!

---

## **🎨 Preview**
![es](https://github.com/user-attachments/assets/d167affc-9863-45a9-9104-2e0b89eaaa5c)


---

## **🔗 Live Demo** 🌐
🚀 Try it out here: [Live Demo](https://multi-domain-chatbot.onrender.com)

---

## **📜 License**
**© 2024 AbuBakar Shahzad | All Rights Reserved**

