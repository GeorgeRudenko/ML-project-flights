# ✈️ Flight Stress-Test Simulator: ML-Powered Operational Resilience

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Marimo](https://img.shields.io/badge/Marimo-0.10+-orange)
![LightGBM](https://img.shields.io/badge/LightGBM-4.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-orange)

**Interactive Stress Testing for Flight Operations using Real-time ML Predictions**

*Academic Project • Business Intelligence • December 2025*
</div>

---

## 📊 Dataset Information

### Original Dataset
- **Source:** [Kaggle: Flight Delay and Cancellation Data (2024)](https://www.kaggle.com/datasets/nalisha/flight-delay-and-cancellation-data-1-million-2024)
- **Description:** Contains ~1 million flight records for 2024 with delay and cancellation information
- **Files used in project:**
  - `flight_data_2024.csv` - **Subset of original data** (sampled for demonstration)
  - `flight_data_processed.csv` - Preprocessed version with feature engineering
- **Original Size:** ~1 GB (full dataset)
- **Project Size:** ~300 MB (sampled subset), ~150 MB (processed)
- **Records in project:** Approximately 50,000 flight records (representative sample)

### Data Processing Pipeline
1. **Data Sampling** - Random sample of 50,000 records from original 1M dataset
2. **Missing Value Treatment** - Median imputation for numerical features
3. **Feature Engineering** - Created critical features:
   - `hourly_avg_delay`: Average delay per hour
   - `origin_avg_delay`: Average delay per origin airport
   - `day_of_week_encoded`: Cyclical encoding
4. **Categorical Encoding** - Label encoding for airports, carriers
5. **Train-Test Split** - 80/20 stratified split preserving temporal order
6. **Output** - Processed dataset ready for ML modeling

*⚠️ Note: Dataset files are not included in this repository. Download from Kaggle link above and place in project root.*

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/GeorgeRudenko/ML-project-flights.git
cd ML-project-flights

# Install dependencies
pip install -r requirements.txt

# Launch application
marimo run hw_simple_new.py
```

## 👤 Author
**George Rudenko** © 2025
