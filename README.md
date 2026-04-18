# Retail-Sales-Forecasting-Inventory-Optimization
Multi-product retail sales forecasting and inventory optimization system using Machine Learning (Random Forest) with an interactive Streamlit dashboard for demand prediction and supply chain decision-making.

# 🛒 Retail Sales Forecasting & Inventory Optimization System

## 📌 Overview
This project simulates a real-world retail analytics system that forecasts product demand and optimizes inventory decisions using machine learning and statistical methods.

It supports **multi-product (multi-SKU) forecasting** and provides **inventory recommendations** such as safety stock and reorder points through an interactive dashboard.

---

## 🚀 Features

- 📊 Multi-product sales simulation
- 🤖 Machine Learning forecasting (Random Forest)
- 📈 Time-series feature engineering (lag features)
- 📦 Inventory optimization:
  - Safety Stock
  - Reorder Point
- 🛠 Interactive Streamlit dashboard
- 📥 Downloadable reports (CSV)

---

## 🧠 Business Problem

Retail businesses often face:
- Overstock → high holding cost
- Stockouts → lost sales

This system helps:
- Predict future demand
- Optimize stock levels
- Improve supply chain efficiency

---

## 🏗️ Project Architecture
Data Generation → Preprocessing → Feature Engineering → ML Model → Forecast → Inventory Optimization → Dashboard


---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn (Random Forest)
- Matplotlib
- Streamlit

---

## 📂 Project Structure
Retail-Sales-Forecasting/
│
├── app/
│ └── dashboard.py
├── src/
│ ├── data_generator.py
│ ├── preprocessing.py
│ ├── forecasting.py
│ ├── inventory.py
│
├── data/
├── outputs/
├── images/
├── main.py
├── requirements.txt
└── README.md

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd Retail-Sales-Forecasting
2. Install dependencies
pip install -r requirements.txt
3. Run pipeline
python main.py
4. Launch dashboard
streamlit run app/dashboard.py


📊 Dashboard Features
Select number of products
Adjust lead time & service level
View product-wise forecasts
Analyze inventory recommendations


📦 Inventory Formulas Used

Safety Stock:

Z × σ × √Lead Time

Reorder Point:

(Avg Demand × Lead Time) + Safety Stock


📸 Sample Outputs
Sales vs Forecast graphs
Product-wise inventory table
Downloadable reports


🎯 Future Improvements
Multi-store support
Real dataset integration
Advanced forecasting (ARIMA, Prophet)
Deployment on cloud

👩‍💻 Author

Ishwari Belhekar.
