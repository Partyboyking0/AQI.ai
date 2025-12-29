🐍 Conda Environment Setup
1️⃣ Create Environment

conda create -n aqi python=3.10
conda activate aqi

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣Run app
uvicorn app:app --reload 

Now in different terminal:
4️⃣ Run ui
streamlit run ui.py