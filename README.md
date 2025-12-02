
# Ethiopian Banking App Review Analysis
A data-driven project that scrapes and analyzes user reviews from Google Play Store for major Ethiopian banking applications (BOA, CBE, Dashen).  
The project covers data collection, preprocessing, exploratory analysis, network-based insight extraction, and theme identification.

## 📌 Features
- Automated scraping of Google Play reviews  
- Cleaning and preprocessing of raw text  
- Sentiment classification (rule-based and model-assisted)  
- Exploratory Data Analysis (EDA)  
- User–theme bipartite network construction  
- Degree-based network statistics  
- Theme extraction per bank  
- Visual and statistical reporting  

## 🧰 Tech Stack
- Python 3.x  
- BeautifulSoup / requests  
- pandas, numpy  
- nltk, sklearn  
- networkx  
- matplotlib  

## 📂 Project Structure
```bash
project/
│── notebooks/
│ ├── preprocessing_EDA.ipynb
│ ├── sentiment.ipynb
│ ├── Themes.ipynb
│ └── Task4_Analysis.ipyn
│── data/
│ ├── raw/
│ ├── processed/
│ ├── sentiment/
│── src/
│ ├── preprocessing.py
│ ├── scraper.py
│ └── analysis.py 
├── sql/
│ └── schema.sql # PostgreSQL schema
│── utils/
│ ├── config.py
│ ├── helper.py
│── README.md
```

---

## **Task 1: Data Collection and Preprocessing**

- Scraped 400+ reviews per bank (1200 total) from Google Play Store.
- Preprocessed data:
  - Removed duplicates
  - Handled missing values
  - Normalized dates to YYYY-MM-DD
- Saved clean CSV: `data/processed/reviews_processed.csv`
- Git: Committed scripts in `task-1` branch with detailed commit messages.

---

## **Task 2: Sentiment and Thematic Analysis**

- Sentiment analysis using VADER for all reviews.
- Identified 3–5 key themes per bank:
  - **Performance Issues**
  - **Login / Access Issues**
  - **Transaction / Feature Issues**
  - **Positive Ease of Use**
- Saved outputs:
  - Sentiment scores: `data/sentiment/sentiment_scores.csv`
- Git: Committed scripts in `task-2` branch.

---

## **Task 3: PostgreSQL Database**

- Designed relational database schema (PostgreSQL) to store cleaned data.
- Tables:
  - `banks` (bank_id, bank_code, bank_name, app_id)
  - `reviews` (review_id, bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, source, ...)
- SQL schema file: `sql/schema.sql`
- Populated tables via Python scripts (psycopg2 / SQLAlchemy).
- Verified data integrity via SQL queries.

---

## **Task 4: Insights and Recommendations**

- Derived actionable insights from sentiment and themes.
- Top positive and negative words identified per bank.
- Key drivers and pain points:
  - **BOA:** Performance Issues, Login / Access Issues, Transaction / Feature Issues
  - **CBE:** Transaction / Feature Issues
  - **Dashen:** Performance Issues, Positive Ease of Use
- Suggested improvements per bank:
  - Optimize app performance
  - Improve login and transaction reliability
  - Enhance UI/UX and feature accessibility
- Visualizations (to be added in final report):
  - Sentiment distribution
  - Review length by bank
  - Top keywords per theme
- Git: Committed scripts and visualizations in `task-4` branch.

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
jupyter notebook
```
📝 Output

Cleaned datasets per bank

Visualizations for sentiment, frequency, and networks

Extracted themes per bank:
```bash
{
 'BOA': ['Performance Issues','Login / Access Issues','Transaction / Feature Issues'],
 'CBE': ['Transaction / Feature Issues'],
 'Dashen': ['Performance Issues','Positive Ease of Use']
}
```
📄 Author

Kalkidan Abreham
2025
