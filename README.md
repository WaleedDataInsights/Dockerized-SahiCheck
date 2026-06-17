# SahiCheck: AI-Powered Fake News, Phishing, and Fraud Detection

**Group ID:** F25DS011
**Course:** Tools & Techniques
**Developer:** Waleed Zahid (L1F21BSDS0051)


---

## Project Overview

SahiCheck is a cybersecurity awareness application developed to help users identify fake news, phishing links, and suspicious fraud-related content. The system allows users to submit text, URLs, or transaction-related information and receive a prediction result with a confidence score.

The main purpose of this project is to demonstrate how modern software tools and deployment techniques can be used to build and deploy a real-world application.

### Main Features

* Fake News Detection
* Phishing Detection
* Fraud Detection
* Prediction Confidence Scores
* FastAPI REST API
* PostgreSQL Database Support
* MongoDB Database Support
* Docker-Based Deployment

---

## Tools and Techniques Used

| Tool / Technology | Usage                        |
| ----------------- | ---------------------------- |
| Python            | Backend Development          |
| FastAPI           | REST API Development         |
| PostgreSQL        | Structured Data Storage      |
| MongoDB           | Unstructured Data Storage    |
| Docker            | Application Containerization |
| GitHub            | Version Control              |
| CSV Datasets      | Data Source                  |
| Uvicorn           | API Server                   |

---

## Tools Not Used

### KNIME

KNIME was not used because data preprocessing and handling were performed using Python libraries.

### Apache Airflow

Airflow was not required because the project performs real-time predictions instead of scheduled batch processing.

### n8n

n8n was not used because prediction results are generated directly through the FastAPI backend.

### Streamlit

A dedicated dashboard was not required for this implementation because the focus of the project was backend deployment and containerization.

---

## Project Structure

01_Project_Report/

03_Source_Code/

04_Data/

05_deployment_guide/

08_Docker_Deployment/

09_Survey_and_Requirement_Collection/

10_Outputs_and_Results/

11_Contribution_and_Evidence/

---

## Running the Application

### Install Dependencies

pip install -r requirements.txt

### Start Backend

uvicorn app:app --reload

### Open API Documentation

http://localhost:8000/docs

---

## Expected Output

The system accepts user inputs and returns:

* Detection Result
* Prediction Type
* Confidence Score

Examples:

* Fake News Detection
* Phishing Detection
* Fraud Detection

---

## Author

Waleed Zahid

BS Data Science

University of Central Punjab
