import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os
# Load cleaned data
df = pd.read_csv("data/sentiment/sentiment_scores.csv")
# Load .env file
load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

# Step 1: Ensure banks exist
banks = df[['bank_code', 'bank_name']].drop_duplicates()

for _, row in banks.iterrows():
    cur.execute("""
        INSERT INTO banks (bank_code, bank_name)
        VALUES (%s, %s)
        ON CONFLICT (bank_code) DO NOTHING;
    """, (row['bank_code'], row['bank_name']))

conn.commit()

# Map bank codes → bank_id
cur.execute("SELECT bank_id, bank_code FROM banks;")
bank_map = {code: bank_id for bank_id, code in cur.fetchall()}

# Step 2: Insert reviews
for _, r in df.iterrows():
    cur.execute("""
        INSERT INTO reviews (
            review_id, bank_id, review_text, rating, review_date,
            review_year, review_month, user_name, thumbs_up, text_length,
            source, sentiment_label, sentiment_score
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (review_id) DO NOTHING;
    """, (
        r['review_id'],
        bank_map[r['bank_code']],
        r['review_text'],
        r['rating'],
        r['review_date'],
        r['review_year'],
        r['review_month'],
        r['user_name'],
        r['thumbs_up'],
        r['text_length'],
        r['source'],
        r['sentiment_label'],
        float(r['sentiment_score'])
    ))

conn.commit()
cur.close()
conn.close()

print("✔ Data inserted successfully!")
