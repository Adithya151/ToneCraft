<h1 align="center">✉️ ToneCraft — Smart Email Tone Corrector</h1>

<p align="center">
  ToneCraft is an NLP-based application that analyzes and corrects the tone of emails.<br>
  Built using <b>Python</b>, <b>Scikit-learn</b>, and <b>NLP techniques</b>, it classifies email tone and rewrites messages into polite and professional versions.
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

### 🖥️ Interactive Frontend
- Built using **Streamlit**
- Real-time tone detection and rewriting  

---

## 🛠️ Tech Stack

| **Layer**    | **Technology**            |
|-------------|----------------------------|
| **Frontend** | Streamlit                  |
| **Backend**  | Python                     |
| **ML Model** | Suport Vector Machine(95.8)|
| **NLP**      | TF-IDF, NLTK               |
| **Libraries**| Scikit-learn, Pandas       |

---

## 📸 Application Preview

<p align="center">
  <img src="screenshots/frontend.png" width="600" alt="ToneCraft Frontend"/>
</p>

> 📌 Add your Streamlit UI screenshot inside a `screenshots/` folder and name it `frontend.png`.

---

## 🔄 Workflow

1. User enters an email message  
2. Text is preprocessed using NLP techniques  
3. Model predicts the email tone  
4. System rewrites the email into a polite and professional version  
5. User reviews and copies the improved email  

---

## 🎯 Use Cases

- Improving professional email communication  
- Corporate and HR email drafting  
- Academic and NLP learning projects  
- Soft skills and workplace communication enhancement  

---

## 📂 Folder Structure

```bash
ToneCraft/
├── app.py
├── model/
│   ├── tone_classifier.pkl
│   └── vectorizer.pkl
├── preprocessing.py
├── requirements.txt
└── README.md
