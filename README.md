

A minimal Streamlit app to predict prices for Cars, Houses, and Laptops using pre-trained machine learning models.

## Features
- Predict car, house, and laptop prices with a simple UI
- Fast, one-page app (no images, minimal design)
- Dark theme enabled by default

## Requirements
- Python 3.7+
- See `requirements.txt` for Python dependencies

## Setup & Local Run
1. Clone this repository or download the project files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run Predictions.py
   ```
4. The app will open in your browser at `http://localhost:8501`

## Deployment (Streamlit Community Cloud)
1. Push your project to a public GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Sign in with GitHub and click “New app”.
4. Select your repo, branch, and set the main file as `Predictions.py`.
5. Click “Deploy”.

**Make sure all required files (models, CSVs, etc.) are in the repo!**

## Project Structure
- `Predictions.py` — Main Streamlit app
- `cars_notebook.py`, `banglore_home_prices_final.py` — Model logic
- `df.pkl`, `pipe.pkl`, `locations.csv`, `quikr_car.csv`, `bengaluru_house_prices.csv` — Data/model files
- `.streamlit/config.toml` — Dark theme config
- `requirements.txt` — Python dependencies

## License
See [LICENSE](LICENSE).
