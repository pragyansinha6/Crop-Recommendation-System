# 🌍 AgroGuide — Smart Crop Recommender

> An interactive web app that recommends the best crop to grow based on your soil nutrients and local climate conditions.

---

## 📌 What It Does

AgroGuide takes 7 input parameters from the user — soil nutrients and weather data — and instantly recommends the most suitable crop from a library of 17 crops. If no crop matches, it advises consulting a local agronomist.



## 🌾 Supported Crops

| | | |
|---|---|---|
| 🌾 Rice | 🌾 Wheat | 🌽 Maize |
| 🥔 Potato | 🎋 Sugarcane | 🌱 Soybean |
| ☁️ Cotton | 🍌 Banana | 🍅 Tomato |
| 🧅 Onion | 🌶️ Chilli | 🍠 Sweet Potato |
| ☕ Coffee | 🍵 Tea | 🥜 Groundnut |
| 🌻 Sunflower | 🍇 Grapes | |

---

## 📥 Input Parameters

| Parameter | Unit | Range |
|-----------|------|-------|
| Nitrogen (N) | mg/kg | 0 – 200 |
| Phosphorus (P) | mg/kg | 0 – 150 |
| Potassium / Potash (K) | mg/kg | 0 – 200 |
| Temperature | °C | 0 – 50 |
| Humidity | % | 0 – 100 |
| Soil pH | — | 0 – 14 |
| Rainfall | mm | 0 – 300 |

---

## ⚙️ How It Works

1. **Input** — User adjusts sliders for soil and climate conditions
2. **Rule Engine** — A priority-ordered `if/elif` function matches the inputs against agronomic requirements for each crop
3. **Output** — The matched crop is displayed in a colour-coded result panel:
   - 🟢 **Green** — confident crop match
   - 🟠 **Orange** — unusual conditions, expert consultation advised

### Sidebar Shortcut
Click any crop button in the sidebar to **auto-fill the sliders** with that crop's ideal growing conditions. Fine-tune from there and hit **Recommend**.

---

## 🚀 Backend

### Prerequisites

- Python 3.9 or later
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/agroguide.git
cd agroguide

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

### requirements.txt

```
streamlit
```

---

## 📁 Project Structure

```
agroguide/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ☁️ Deployment (Streamlit Community Cloud)

1. Push the project to a **public GitHub repository**
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
3. Click **New app** → select your repo, branch (`main`), and entry file (`app.py`)
4. Click **Deploy** — your app will be live at `https://your-app.streamlit.app`

---

## DIRECT LINK
Click here to get your perfect recommendation - https://agroguide-ps.streamlit.app/

---

## 🛠️ Built With

| Tool | Purpose |
|------|---------|
| [Python](https://python.org) | Core programming language |
| [Streamlit](https://streamlit.io) | Web UI framework |
| HTML / CSS (inline) | Custom styling and layout |

---

## 🌱 Future Improvements

- [ ] Add a machine learning model trained on real crop datasets
- [ ] Support multilingual UI for regional farmers
- [ ] Include fertiliser dosage recommendations
- [ ] Add a map view for region-based suggestions
- [ ] Export results as a PDF report

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- Crop parameter thresholds based on publicly available agronomic reference guides
- Built using [Streamlit](https://streamlit.io)

---

<p align="center">
  <i>AgroGuide — Empowering farmers with smart, data-driven crop decisions 🌍</i>
</p>

