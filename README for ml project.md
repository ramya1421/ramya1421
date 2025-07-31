# 🌍 Smart Disaster Response System 🚨

A multi-modal AI/ML solution that leverages satellite imagery and social media text data to detect and respond to natural disasters in real-time. Integrated with Amazon Web Services for scalable, cloud-native deployment.

---

## ✅ Problem Statement

Natural disasters like floods, earthquakes, and wildfires often cause communication breakdowns. Early and accurate damage detection from both **satellite images** and **social media reports** can greatly improve rescue and response efforts.

---

## 🔧 Features

- 🔎 **Satellite Image Analysis** using AWS Rekognition
- 🧠 **Text Sentiment/NLP Analysis** on social media posts using AWS Comprehend
- 🚨 **Real-time Alerts** via AWS SNS
- 📊 **Scalable AWS Infrastructure** (S3, Lambda, SageMaker-ready)
- 🗺️ (Optional) Location-based heatmaps using AWS Location Services

---

## 🧱 Architecture Diagram

```
[Social Media Input]     [Satellite Imagery]
         ↓                       ↓
 AWS Comprehend        AWS Rekognition
         ↓                       ↓
     Text Tags            Image Labels
         ↘                 ↙
           [Disaster Detection Engine]
                        ↓
                  AWS SNS Alerts
                        ↓
            [First Responders / Dashboard]
```

---

## 🛠️ Tech Stack

| Component           | Tool / Service             |
|---------------------|----------------------------|
| Language            | Python 3.8+                |
| Cloud Platform      | AWS                        |
| Image Analysis      | AWS Rekognition            |
| Text Analysis       | AWS Comprehend             |
| Storage             | AWS S3                     |
| Notifications       | AWS SNS                    |
| Optional Hosting    | AWS Lambda, EC2            |
| Visualization       | Amazon QuickSight (Optional)|

---

## 📂 Folder Structure

```
📁 disaster-response-system/
├── main.py                   # Main pipeline script
├── sample_satellite_image.jpg
├── requirements.txt
├── README.md
└── utils/
    └── helper_functions.py   # Modular components (optional)
```

---

## 🚀 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/disaster-response-system.git
cd disaster-response-system
```

### 2. Set up environment

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure AWS

- Set your AWS credentials:
```bash
aws configure
```
- Update the following variables in `main.py`:
  - `S3_BUCKET`
  - `SNS_TOPIC_ARN`
  - AWS Region (`us-east-1` recommended)

### 4. Run the application

```bash
python main.py
```

---

## 🔁 Sample Input

### Tweets:
```
"Floods have destroyed all roads in Chennai. No power or food."
"Need help in Delhi, earthquake tremors just hit us."
```

### Image:
A satellite image showing water-logged regions (sample provided).

---

## 📈 Possible Enhancements

- 🛰️ Integrate with **real satellite feeds** (e.g., NASA FIRMS, Sentinel)
- 📍 Add **geotagging** with AWS Location Services
- 🤖 Train custom models on AWS SageMaker
- 📊 Build real-time dashboards with Streamlit or Amazon QuickSight

---

## 🛡️ Ethical Use

This project should be used **only for humanitarian purposes**, such as early disaster detection and relief coordination.

---

## 📜 License

MIT License © 2025 [RAMYA VARSHINI]
