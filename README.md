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
```python
# Marimo UI Components
airport_selector = mo.ui.dropdown(options=["JFK", "LAX", "ORD", ...])
weather_slider = mo.ui.slider(start=1.0, stop=3.0, step=0.1, value=1.5)
```

| Control | Function | Range |
|---------|----------|-------|
| **Airport Selector** | Choose departure airport | All major US airports |
| **Weather Severity** | Simulate weather impact | 1.0x (Normal) to 3.0x (Storm) |

### Real-time Visualization
- **Green Bar**: Baseline arrival time (Severity = 1.0)
- **Red Bar**: Adjusted prediction with weather impact
- **Delta Display**: `+X minutes` delay warning
- **Dynamic Updates**: Instant recalculation on slider movement

---

## 📊 Dataset Information

### Original Dataset
- **Source:** [Kaggle: Flight Delay and Cancellation Data (2024)](https://www.kaggle.com/datasets/nalisha/flight-delay-and-cancellation-data-1-million-2024)
- **Files used:**
  - `flight_data_2024.csv` - Sampled subset (50K records)
  - `flight_data_processed.csv` - With `origin_avg_delay`, `hourly_avg_delay` features

### Weather Simulation Logic
The model doesn't use actual weather data. Instead, it **simulates weather impact** by:
1. Taking historical delay averages for an airport
2. Applying **Severity Multiplier** (1.0x to 3.0x)
3. Predicting how arrival time changes with increased delays

---

## 🚀 Quick Start

```bash
# 1. Clone and install
git clone https://github.com/GeorgeRudenko/ML-project-flights.git
cd ML-project-flights
pip install -r requirements.txt

# 2. Launch simulator
marimo run hw_simple_new.py

# 3. Open browser: http://localhost:8088
```

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
```
hw_simple_new.py          # Main application with interactive UI
requirements.txt          # Python dependencies
*.ipynb                  # Analysis notebooks
LICENSE, README.md       # Documentation
```

## 👤 Author
**George Rudenko** © 2025 | Academic Project | Machine Learning Applications
