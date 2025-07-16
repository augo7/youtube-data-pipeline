# 🚀 YouTube Data Pipeline: Scalable ETL with Python & BigQuery

This project demonstrates a robust and modular ETL (Extract, Transform, Load) pipeline designed to ingest, process, and analyze selected YouTube channel data at scale. Leveraging the YouTube Data API, Python’s powerful data manipulation libraries, and Google BigQuery’s cloud analytics platform, this pipeline embodies real-world data engineering best practices.

By integrating secure API management, reusable code architecture, and cloud data warehousing, this project provides a strong foundation for complex data workflows and insightful analytics.

---

## 🔍 Project Highlights

- **API Integration & Data Extraction:** Programmatically retrieves dynamic, multi-channel YouTube statistics, handling API rate limits and data pagination with reliability.

- **Data Transformation:** Applies clean, efficient data processing using Pandas to convert raw JSON responses into analysis-ready tabular datasets.

- **Cloud Data Warehousing:** Seamlessly loads transformed data into BigQuery, enabling high-performance querying and scalable storage.

- **Security & Best Practices:** Implements environment variable management via `.env` files and `python-dotenv` to safeguard sensitive API credentials.

- **Analytical Insight:** Supports downstream SQL-based analytics, such as engagement scoring and channel performance ranking, driving actionable business insights.

---

## 🛠️ Technologies & Tools

| Technology           | Purpose                                  |
|----------------------|------------------------------------------|
| Python               | Core language for scripting & processing |
| Pandas               | Data wrangling and transformation        |
| YouTube Data API     | Reliable extraction of YouTube metrics   |
| Google BigQuery      | Cloud-scale data storage and analytics   |
| dotenv + `.env` file | Secure and configurable secret management|
| Git & GitHub         | Version control and collaborative workflow|

---

## 📂 Project Structure

- `API_key.py` — Efficient extraction of YouTube channel data using secure API calls

- `pandas_processing.py` — Clean and transform raw data into structured formats using Pandas

- `BigQuery_load.py` — Automated ingestion of processed data into BigQuery tables

- `.env` — Secure storage of API keys (excluded from version control)

- `.gitignore` — Protects sensitive files and unnecessary artifacts from being pushed

- `README.md` — Project documentation and usage guidelines

---

##  How to Use This Project

1. Clone the repository to your local machine.

2. Configure your API key securely by adding it to a `.env` file:

   ```ini
   YOUTUBE_API_KEY=your_actual_api_key
Install dependencies (Pandas, python-dotenv, google-cloud-bigquery) using:

bash
Copy
Edit
pip install -r requirements.txt
Run the pipeline sequentially:

bash
Copy
Edit
python API_key.py
python pandas_processing.py
python BigQuery_load.py
Analyze the data with BigQuery SQL to generate insights such as engagement rates, subscriber growth, and content performance.

🚀 Future Enhancements
Automate the pipeline with orchestration tools like Apache Airflow or Google Cloud Functions to enable scheduled, continuous data updates.

Expand dataset granularity by including video-level metrics and user engagement data.

Integrate with BI tools such as Looker Studio or Tableau for dynamic, visual dashboards.

Implement robust logging, error handling, and testing frameworks for production readiness.


👨‍💻 About Me
I am a passionate Computer Science student attending Texas State University, actively building expertise in data analytics and engineering. This project reflects my hands-on experience with APIs, data transformation, cloud platforms, and secure coding practices — foundational skills essential for modern data-driven organizations.
