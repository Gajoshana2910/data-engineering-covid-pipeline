# 🚀 COVID-19 Data Pipeline  

## 📖 Project Overview  
This project is an **end-to-end Data Engineering pipeline** that extracts COVID-19 data from an API, cleans and transforms it, and loads it into a **PostgreSQL database**. The pipeline is **automated using Apache Airflow** and can be deployed using **Docker**.  

## 📌 Tech Stack  
- **Python** → For scripting the ETL process  
- **Pandas** → Data transformation & cleaning  
- **Requests** → API calls for data extraction  
- **PostgreSQL** → Data storage  
- **Apache Airflow** → Workflow orchestration  
- **Docker** → Containerization for easy deployment  

```md
## 🏗️ Project Structure  

data-engineering-covid-pipeline/
│── dags/                     # Airflow DAGs
│   ├── covid_pipeline.py
│── scripts/                  # ETL Scripts
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│── docker-compose.yml        # Docker setup
│── requirements.txt          # Python dependencies
│── README.md                 # Project Documentation


## 🛠️ Steps to Run the Project

🔽 1️⃣ Clone the Repository  

git clone https://github.com/your-username/data-engineering-covid-pipeline.git
cd data-engineering-covid-pipeline

📦 2️⃣ Install Dependencies

pip install -r requirements.txt

🐘 3️⃣ Set Up PostgreSQL

(If using local PostgreSQL, create a database)

CREATE DATABASE covid_db;

🐳 4️⃣ Run Docker (If Using Airflow & PostgreSQL)

docker-compose up -d

🔄 5️⃣ Run ETL Scripts Manually

python scripts/extract.py   # Extract data from API
python scripts/transform.py # Transform & clean data
python scripts/load.py      # Load into PostgreSQL

⚡ 6️⃣ Schedule Pipeline with Apache Airflow

1. Open http://localhost:8080/
2. Log in (Username: airflow, Password: airflow)
3. Enable the covid_pipeline DAG
4. Click "Trigger DAG" to run the pipeline

📊 7️⃣ Verify Data in PostgreSQL

SELECT * FROM covid_stats LIMIT 10;

🚀 Future Enhancements

- ✅ Add Power BI / Jupyter Notebook for data visualization
- ✅ Deploy the pipeline on Azure Data Factory
- ✅ Store data in Snowflake instead of PostgreSQL

## 📜 License

This project is licensed under the **MIT License** - see the  
👉 [LICENSE](https://github.com/Gajoshana2910/data-engineering-covid-pipeline/blob/main/LICENSE) file for details.  

## 👨‍💻 Developed by

👉 [Gajalakshmi A K](https://github.com/Gajoshana2910)
