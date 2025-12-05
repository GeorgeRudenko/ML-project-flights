# Создаём новый README с правильным порядком
cat > README.md << "EOF"
# ✈️ Flight Weather Impact Simulator: ML-Powered Delay Prediction

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Marimo](https://img.shields.io/badge/Marimo-0.10+-orange)
![LightGBM](https://img.shields.io/badge/LightGBM-4.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-orange)

**Real-time Weather Impact Simulation on Flight Arrival Times**

*Academic Project • Operational Analytics • December 2025*
</div>

---

## 🎮 Live Demo Interface

### Interactive Controls
\`\`\`python
# Marimo UI Components
airport_selector = mo.ui.dropdown(options=["JFK", "LAX", "ORD", ...])
weather_slider = mo.ui.slider(start=1.0, stop=3.0, step=0.1, value=1.5)
\`\`\`

| Control | Function | Range |
|---------|----------|-------|
| **Airport Selector** | Choose departure airport | All major US airports |
| **Weather Severity** | Simulate weather impact | 1.0x (Normal) to 3.0x (Storm) |

### Real-time Visualization
- **Comparative horizontal bar chart** showing:
  - 🟢 **Baseline**: Flight duration under normal conditions (Severity = 1.0)
  - 🔴 **Forecast**: Predicted duration with selected Weather Severity Factor
- **Dynamic Updates**: Instant recalculation on slider movement

---

## 📥 Download Prepared Data

### 🚀 Direct Download Link
**Access preprocessed dataset files here:**  
🔗 **[Google Drive: Flight Data for ML Project](https://drive.google.com/drive/folders/1piC9bHKQW2Fphi6pShXYybbxSZFKCMLp?usp=drive_link)**

### 📁 Available Files:
| File | Size | Description |
|------|------|-------------|
| \`flight_data_2024.csv\` | ~15 MB | Sampled subset from original Kaggle dataset |
| \`flight_data_processed.csv\` | ~8 MB | Preprocessed with feature engineering |

### 📍 File Placement:
\`\`\`
Your project folder/
├── flight_data_2024.csv      ← Download from Google Drive
├── flight_data_processed.csv ← Download from Google Drive
├── hw_simple_new.py
├── requirements.txt
└── ... (other project files)
\`\`\`

---

## 🚀 Quick Start

\`\`\`bash
# 1. Clone and install
git clone https://github.com/GeorgeRudenko/ML-project-flights.git
cd ML-project-flights
pip install -r requirements.txt

# 2. Download data from Google Drive link above
# 3. Place CSV files in project folder (see placement diagram)

# 4. Launch simulator
marimo run hw_simple_new.py

# 5. Open browser: http://localhost:8088
\`\`\`

---

## 📊 Dataset Information

### Original Dataset
- **Source:** [Kaggle: Flight Delay and Cancellation Data (2024)](https://www.kaggle.com/datasets/nalisha/flight-delay-and-cancellation-data-1-million-2024)

### Weather Simulation Logic
The model doesn't use actual weather data. Instead, it **simulates weather impact** by:
1. Taking historical delay averages for an airport
2. Applying **Severity Multiplier** (1.0x to 3.0x)
3. Predicting how arrival time changes with increased delays

---

## 🎯 How to Use
1. **Select Airport** from dropdown (e.g., "JFK")
2. **Adjust Weather Severity** slider
   - 1.0 = Normal conditions
   - 2.0 = Bad weather
   - 3.0 = Storm conditions
3. **Observe** predicted delay in real-time
4. **Compare** baseline vs adjusted arrival times

---

## 📁 Project Structure
\`\`\`
hw_simple_new.py          # Main application with interactive UI
requirements.txt          # Python dependencies
*.ipynb                  # Analysis notebooks
LICENSE, README.md       # Documentation
\`\`\`

---

## 👤 Author
**George Rudenko** © 2025 | Academic Project | Machine Learning Applications

---

### 🔄 Full Reproduction (Optional):
For complete reproducibility:
1. Original source: [Kaggle Dataset](https://www.kaggle.com/datasets/nalisha/flight-delay-and-cancellation-data-1-million-2024)
2. Run \`eda.ipynb\` → creates sampled dataset
3. Run \`model.ipynb\` → applies feature engineering

*Note: Google Drive files are provided for convenience to avoid downloading 1GB+ of raw data.*
EOF
