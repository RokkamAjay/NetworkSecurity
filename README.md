### Network Security ML Project For Phising Data
# 🛡️ Network Security ML Project

An end-to-end Machine Learning project for detecting potentially malicious/phishing-related network data. The project demonstrates a complete ML workflow, starting from data ingestion and validation to model training, evaluation, and prediction through a FastAPI application.

## 📌 Project Overview

The goal of this project is to build a Machine Learning pipeline that can analyze network/security-related data and classify new records based on patterns learned from historical data.

The project follows a modular and production-oriented ML architecture that includes:

* Data Ingestion
* Data Validation
* Data Transformation
* Machine Learning Model Training
* Model Evaluation
* Model Saving
* Prediction
* FastAPI API
* MongoDB
* MLflow experiment tracking
* Docker support

> **Note:** This project is an ML-based classification system and should be considered a prototype/learning implementation rather than a complete production cybersecurity solution.

---

## 🎯 Problem Statement

Network and security systems can generate a large amount of data. Manually analyzing every record can be difficult and time-consuming.

This project explores how Machine Learning can be used to learn patterns from historical security-related data and generate predictions for new data.

### Objective

Build an end-to-end ML application that can:

1. Read and process security-related data.
2. Validate the input data.
3. Transform the data into a format suitable for Machine Learning.
4. Train and evaluate multiple ML classification algorithms.
5. Select and save a suitable trained model.
6. Accept new CSV data through an API.
7. Generate predictions for the new records.

---

## 🏗️ Project Architecture

```text
                    Network Security ML Project

                         Input Dataset
                              │
                              ▼
                     ┌─────────────────┐
                     │ Data Ingestion  │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ Data Validation │
                     └────────┬────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Data Transformation│
                    └─────────┬────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Model Training   │
                    └─────────┬────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Model Evaluation │
                    └─────────┬────────┘
                              │
                              ▼
                       Saved Model
                              │
                  ┌───────────┴───────────┐
                  │                       │
                  ▼                       ▼
              MLflow                 FastAPI
           Experiment Tracking       Prediction API
                                          │
                                          ▼
                                    New CSV Data
                                          │
                                          ▼
                                      Prediction
                                          │
                                          ▼
                                  prediction_output
```

---

## 🔄 Machine Learning Workflow

### 1. Data Ingestion

The project first obtains the required dataset and prepares it for the ML pipeline.

The ingestion stage is responsible for bringing the raw data into the project workflow.

### 2. Data Validation

The input dataset is checked against the expected data structure/schema.

This helps identify problems such as:

* Missing columns
* Unexpected columns
* Incorrect data structure
* Invalid input data

### 3. Data Transformation

The data is prepared before being provided to the Machine Learning algorithms.

This stage can include operations such as:

* Handling missing values
* Encoding categorical data
* Scaling numerical features
* Preparing features for model training

The preprocessing object is saved so that the **same transformations can be applied to new prediction data**.

### 4. Model Training

Multiple classification algorithms are trained and evaluated.

The project includes models such as:

* Logistic Regression
* K-Nearest Neighbors
* Decision Tree
* AdaBoost
* Gradient Boosting
* Random Forest

The models are evaluated to identify a suitable model for the dataset.

### 5. Model Evaluation

The trained models are evaluated using classification metrics.

Examples include:

* Accuracy
* Precision
* F1 Score

The evaluation results help compare the performance of the trained models.

### 6. Model Saving

The trained model and preprocessing object are saved as serialized files.

```text
final_model/
│
├── model.pkl
└── preprocessor.pkl
```

These files can later be loaded by the prediction application.

---

# 🚀 Prediction Workflow

Once the model has been trained, new data can be provided to the prediction API.

```text
New CSV
   ↓
FastAPI
   ↓
Pandas DataFrame
   ↓
Saved Preprocessor
   ↓
Trained ML Model
   ↓
Prediction
   ↓
Output CSV
```

The prediction result is stored in:

```text
prediction_output/output.csv
```

---

# 🌐 FastAPI

FastAPI is used to expose the Machine Learning pipeline through HTTP endpoints.

### Available Endpoints

### `/train`

Starts the training pipeline.

```text
/train
   ↓
Training Pipeline
   ↓
Data Processing
   ↓
Model Training
   ↓
Model Evaluation
```

### `/predict`

Accepts new CSV data and generates predictions using the saved model.

```text
/predict
   ↓
CSV Input
   ↓
Preprocessing
   ↓
ML Model
   ↓
Prediction
```

---

# 📊 MLflow

MLflow is used for Machine Learning experiment tracking.

It helps track information related to different model-training experiments, such as:

* Model performance
* Metrics
* Parameters
* Experiment runs

This is useful when multiple Machine Learning algorithms need to be compared.

---

# 🗄️ MongoDB

MongoDB is used as a database component in the project.

It provides a way to store and retrieve project data during the data ingestion workflow.

The application uses a MongoDB connection configured through an environment variable.

---

# 🐳 Docker

The project includes Docker support to make the application easier to package and run in a consistent environment.

Docker can package:

```text
Python
+
Required Libraries
+
Application Code
+
Configuration
```

into a containerized application.

---

# 🛠️ Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming language |
| Pandas       | Data processing      |
| NumPy        | Numerical operations |
| Scikit-learn | Machine Learning     |
| FastAPI      | Prediction API       |
| MongoDB      | Data storage         |
| MLflow       | Experiment tracking  |
| Docker       | Containerization     |
| Git          | Version control      |
| GitHub       | Source code hosting  |

---

# 📁 Project Structure

```text
NetworkSecurity/
│
├── data_schema/
│
├── Network_Data/
│
├── networksecurity/
│   ├── components/
│   ├── constant/
│   ├── entity/
│   ├── exception/
│   ├── logging/
│   ├── pipeline/
│   └── utils/
│
├── final_model/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── prediction_output/
│
├── app.py
├── main.py
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/RokkamAjay/NetworkSecurity.git
```

### 2. Navigate to the project

```bash
cd NetworkSecurity
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Run the training pipeline

```bash
python main.py
```

This executes the ML training workflow.

## Run the FastAPI application

```bash
uvicorn app:app --reload
```

The API can then be accessed locally through:

```text
http://127.0.0.1:8000
```

FastAPI also provides interactive API documentation through:

```text
/docs
```

---

# 📥 Input Format

The current prediction implementation is designed to work with **CSV data containing the features expected by the trained model**.

Example workflow:

```text
CSV File
   ↓
Upload to /predict
   ↓
DataFrame
   ↓
Preprocessing
   ↓
Model
   ↓
Prediction
```

> The model cannot accept arbitrary files such as PDFs or unrelated JSON files. The input must contain the features and structure expected by the trained model.

---

# 📤 Output

The prediction results are generated and stored as:

```text
prediction_output/output.csv
```

The output contains the input records along with the generated prediction.

---

# 📈 Key Features

* End-to-end Machine Learning pipeline
* Modular project architecture
* Data ingestion and validation
* Data preprocessing
* Multiple ML classification algorithms
* Model evaluation
* Model persistence
* FastAPI prediction API
* MLflow experiment tracking
* MongoDB integration
* Docker support
* Git/GitHub version control

---

# 💡 What I Learned From This Project

Through this project, I worked with and gained practical exposure to:

* Building an end-to-end Machine Learning pipeline
* Organizing ML projects into reusable components
* Data preprocessing and validation
* Training multiple classification models
* Evaluating Machine Learning models
* Saving and loading trained models
* Creating prediction APIs using FastAPI
* Experiment tracking using MLflow
* Working with MongoDB
* Containerizing applications using Docker
* Debugging and integrating different components of an ML application

---

# 🔮 Future Improvements

Possible improvements include:

* Add authentication for the prediction API
* Improve input validation and error handling
* Add automated model retraining
* Add CI/CD integration
* Deploy the API to a cloud platform
* Add monitoring for model performance
* Add a web-based dashboard for prediction results
* Support additional structured input formats such as JSON after implementing appropriate validation and conversion

---

# 👨‍💻 Author

**Ajay Rokkam**

B.Tech – Computer Science and Engineering (Data Science)

GitHub:
https://github.com/RokkamAjay

LinkedIn:
https://www.linkedin.com/in/rokkam-ajay-852a6b329/

---

## ⭐ Project Summary

This project demonstrates how Machine Learning can be integrated into a complete application rather than being limited to model training alone.

The complete workflow is:

```text
Data
 ↓
Ingestion
 ↓
Validation
 ↓
Transformation
 ↓
Model Training
 ↓
Evaluation
 ↓
Model Saving
 ↓
FastAPI
 ↓
New CSV Data
 ↓
Prediction
```

The project provides practical exposure to **Machine Learning, backend APIs, databases, experiment tracking, containerization, and software project structure**.
