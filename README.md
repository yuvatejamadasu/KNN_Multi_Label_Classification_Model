# 🌸 KNN Multi-Class Classification – Iris Flower Prediction

## 📌 Project Overview

This project implements a **K-Nearest Neighbors (KNN) Multi-Class Classification Model** using the famous Iris Flower Dataset.

The application predicts the species of an Iris flower based on four input features: Sepal Length, Sepal Width, Petal Length, and Petal Width.

The trained Machine Learning model is integrated with a Flask web application, allowing users to enter flower measurements and get real-time predictions through a user-friendly interface.

## 🎯 Project Objectives

* Build a KNN classification model using the Iris dataset.
* Understand and implement the K-Nearest Neighbors algorithm.
* Predict Iris flower species using four numerical input features.
* Integrate the trained ML model with Flask.
* Develop an interactive web interface using HTML and CSS.
* Deploy the Machine Learning application using Render.

## 🌼 Iris Dataset

The Iris dataset contains 150 observations and 4 independent features.

**Input Features:**

1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)

**Target Classes:**

* Iris Setosa
* Iris Versicolor
* Iris Virginica

## 🛠️ Technologies Used

| Technology    | Purpose              |
| ------------- | -------------------- |
| Python        | Programming Language |
| NumPy         | Numerical Operations |
| Pandas        | Data Manipulation    |
| Scikit-learn  | Machine Learning     |
| KNN Algorithm | Classification       |
| Flask         | Backend Development  |
| HTML5         | Web Page Structure   |
| CSS3          | Web Page Styling     |
| Pickle        | Model Serialization  |
| Git & GitHub  | Version Control      |
| Render        | Cloud Deployment     |

## 📂 Project Structure

```text
KNN_Multi_Label_Classification_Data/
│
├── templates/
│   └── index.html
│
├── app.py
├── main.py
├── KNN_Multi_label_Classification_Explanation.py
├── KNN_Multi_level_Classification_Model.pkl
├── IRIS - IRIS.csv
├── requirements.txt
├── Procfile
└── README.md
```

## ⚙️ How It Works

1. The Iris dataset is loaded and processed using Pandas.
2. The KNN classification algorithm is trained using the dataset.
3. The trained model is saved as a Pickle file.
4. Flask loads the saved Machine Learning model.
5. Users enter four flower measurements through the web interface.
6. The input values are submitted to Flask using the POST method.
7. The application passes the input values to the trained KNN model.
8. The model predicts the Iris flower species.
9. The predicted result is displayed on the webpage.

## 🚀 Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/yuvatejamadasu/KNN_Multi_Label_Classification_Model.git
```

### Step 2: Navigate to the Project Folder

```bash
cd KNN_Multi_Label_Classification_Model
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Flask Application

```bash
python app.py
```

### Step 7: Open in Browser

```text
http://127.0.0.1:5000/
```

## 🌐 Deployment

This application is deployed using **Render**.

Deployment Configuration:

* Build Command:

```bash
pip install -r requirements.txt
```

* Start Command:

```bash
gunicorn app:app
```

## 📊 Machine Learning Algorithm

**K-Nearest Neighbors (KNN)** is a supervised Machine Learning algorithm used for classification and regression tasks.

In this project, KNN is used to classify Iris flowers into three different species based on their measurements.

The algorithm identifies the nearest data points and predicts the class based on the neighboring observations.

## 👨‍💻 Developed By

**M. Yuva Teja**

Machine Learning & Python Developer

GitHub: https://github.com/yuvatejamadasu

---

⭐ If you find this project useful, don't forget to give it a star on GitHub!

**Thank you for visiting my project!**
