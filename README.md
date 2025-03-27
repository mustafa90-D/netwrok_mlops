### Network Security Projects For Phising Data

Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = 788614365622.dkr.ecr.us-east-1.amazonaws.com/networkssecurity
ECR_REPOSITORY_NAME = networkssecurity


Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh


sudo sh get-docker.sh

sudo usermod -aG docker ubuntu


newgrp docker

# 🛡️ Network Security Threat Detection with MLOps

This project is a modular, production-ready **MLOps pipeline** for detecting network security threats such as phishing, anomalies, and malicious behaviors. It leverages a scalable architecture and integrates **ETL, model training, validation, prediction, logging, cloud sync, CI/CD**, and **MongoDB** for storing results or metadata.

---

## 📌 Project Goals

- Detect and classify threats in network data
- Enable automated training, validation, and prediction
- Follow **MLOps best practices** with modular architecture
- Make the system deployable and maintainable using CI/CD, logging, and configuration management

---

## 🗂️ Project Structure

```
MLOPS/
│
├── Artifacts/                     # Stores models, logs, and outputs
├── data_schema/                  # YAML schema for data validation
│   └── schema.yaml
├── logs/                         # Logs from all stages
├── Network_Data/                 # Raw CSV dataset
│   └── phishingData.csv
├── networksecurity/              # Main Python package
│   ├── cloud/                   # S3 Sync utility
│   ├── components/             # Ingestion, transformation, trainer
│   ├── constant/               # Constants
│   ├── entity/                 # Pydantic-based config and output schemas
│   ├── exception/              # Custom exception handling
│   ├── logging/                # Central logger
│   ├── pipeline/               # Training + Batch prediction scripts
│   ├── utils/                  # Helper methods (file ops, etc.)
│   └── main_utils/ml_utils/    # Metrics, estimators, model logic
├── prediction_output/           # Generated predictions
├── templates/                   # UI if any
├── valid_data/                  # Cleaned/validated data
├── .env                         # Environment config
├── Dockerfile                   # Container setup
├── push_data.py                 # Script to push to MongoDB
├── test_mongodb.py              # MongoDB testing
├── requirements.txt             # Python dependencies
├── setup.py                     # Installable module
├── main.py                      # Launch entry point
├── app.py                       # Streamlit or FastAPI app
└── README.md
```

---

## 🔄 MLOps Pipeline Stages

| Stage                  | Description |
|------------------------|-------------|
| `data_ingestion.py`    | Downloads and loads the raw phishing/network data |
| `data_validation.py`   | Validates CSV against `schema.yaml` |
| `data_transformation.py` | Prepares data for modeling |
| `model_trainer.py`     | Trains a classifier (e.g., RandomForest, XGBoost) |
| `batch_prediction.py`  | Makes predictions on unseen/new data |
| `s3_syncer.py`         | Sync artifacts with AWS S3 |
| `push_data.py`         | Pushes metadata or results to MongoDB |

---

## 🧪 Technologies Used

-📦 ML libraries (Scikit-learn, LightGBM, XGBoost)

☁️ Cloud tools (AWS S3)

🧠 Tracking (MLflow)

🧱 Infrastructure (Docker, CI/CD, MongoDB)

🖥️ Serving (Streamlit or FastAPI)

⚙️ Utilities (PyYAML, logging, GitHub Actions)

---

## ✅ CI/CD Integration

- **CI**: Code is linted, tested, and validated on every push via GitHub Actions
- **CD**: Artifacts can be deployed to cloud storage or app platforms

---

## 📊 MongoDB Integration

Prediction logs or performance metrics can be pushed to **MongoDB Atlas** or local instance using `push_data.py`.

You can easily switch or expand to any other NoSQL database with `pymongo`.

---

## 🚀 Future Work

- Add alert generation system
- Integrate with real-time network data APIs
- Improve model explainability with SHAP or LIME
- Enhance Streamlit/FastAPI dashboards

---

## 👨‍💻 Author

Made with ❤️ by Mustafa  
_“Built with modularity, powered by MLOps.”_

---

