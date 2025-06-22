# ⚡ Energy Consumption Predictor (Gradio App)

This project is a machine learning-powered **web demo** that predicts a country's energy consumption score based on various environmental, economic, and industrial features. It uses **Gradio** to provide an interactive user interface for input and real-time prediction.

---

## 🧠 Model Overview

The model takes the following features as input:
- Per Capita Energy Use
- Renewable Energy Share
- Fossil Fuel Dependency
- Industrial Energy Use
- Household Energy Use
- Carbon Emissions
- Energy Price Index
- Country (One-hot encoded: Australia, Brazil, Canada, etc.)

It returns:
> 🔍 **Predicted Energy Consumption Score** — a numerical value representing energy usage behavior.

---



## 🧪 How to Use

1. Adjust the sliders for numeric values
2. Select the country using the dropdown
3. Click "Submit"
4. View the predicted energy consumption score instantly

---

## 📦 Folder Structure

gradio_app/
├── gradio_app.py # Gradio frontend + model loading
├── models/
│ └── energy_consumption.pkl # Trained XGBoost model
├── requirements.txt # Dependencies for Hugging Face Spaces

## 📦 Requirements

Install dependencies locally using:

```bash
pip install -r requirements.txt
