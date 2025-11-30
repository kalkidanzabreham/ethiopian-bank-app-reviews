
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
│── data/
│ ├── raw/
│ ├── processed/
│ ├── sentiment/
│── src/
│ ├── preprocessing.py
│ ├── scraper.py
│── utils/
│ ├── config.py
│ ├── helper.py
│── README.md
```

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
