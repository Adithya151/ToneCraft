<h1 align="center">✉️ ToneCraft — Smart Email Tone Corrector</h1>

<p align="center">
  ToneCraft is an NLP-based application that analyzes and corrects the tone of emails.<br>
  Built using <b>Python</b>, <b>Django</b>, <b>Scikit-learn</b>, and <b>NLP techniques</b>, it classifies email tone and rewrites messages into polite and professional versions.
</p>

---

## 🚀 Features

### 🔍 Email Tone Classification
- Classifies email tone as **Formal**, **Friendly**, or **Rude**
- Uses **TF-IDF Vectorization** with **Logistic Regression**

### 🧠 Text Preprocessing
- Tokenization and stopword removal  
- Text normalization for improved accuracy  

### ✍️ Tone Correction
- Automatically rewrites emails into **polite and professional** versions  

### 🖥️ Web-Based Frontend
- Built using **Django**, **HTML**, and **CSS**
- Clean and simple user interface for email input and results  

---

## 🛠️ Tech Stack

| **Layer**        | **Technology**                    |
|------------------|------------------------------------|
| **Frontend**     | HTML5, CSS3                        |
| **Backend**      | Django, Python                     |
| **ML Model**     | Support Vector Machine(95.8)       |
| **NLP**          | TF-IDF, NLTK                       |
| **Libraries**    | Scikit-learn, Pandas               |

---

## 📸 Application Preview

<p align="center">
  <img src="https://github.com/Adithya151/ToneCraft/blob/main/Screenshot%202025-12-24%20200534.png" width="600" alt="AutoCleanX Dashboard"/>
</p>

---

## 🔄 Workflow

1. User enters an email message  
2. Text is preprocessed using NLP techniques  
3. Model predicts the email tone  
4. System rewrites the email into a polite and professional version  
5. User reviews and copies the improved email  

---

## 📂 Folder Structure

```bash
ToneCraft/
├── manage.py
├── tonecraft/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css
│   ├── views.py
│   └── preprocessing.py
├── model/
│   ├── tone_classifier.pkl
│   └── vectorizer.pkl
├── requirements.txt
└── README.md
