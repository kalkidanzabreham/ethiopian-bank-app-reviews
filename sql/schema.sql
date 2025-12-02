-- schema.sql

CREATE TABLE IF NOT EXISTS banks (
  bank_id SERIAL PRIMARY KEY,
  bank_code VARCHAR(16) UNIQUE NOT NULL,
  bank_name TEXT NOT NULL,
  app_id TEXT
);

CREATE TABLE IF NOT EXISTS reviews (
  review_id TEXT PRIMARY KEY,
  bank_id INTEGER NOT NULL REFERENCES banks(bank_id) ON DELETE CASCADE,
  review_text TEXT,
  rating SMALLINT,
  review_date DATE,
  review_year INT,
  review_month INT,
  user_name TEXT,
  thumbs_up INT,
  text_length INT,
  source TEXT,
  sentiment_label VARCHAR(16),
  sentiment_score FLOAT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_reviews_bank_id ON reviews(bank_id);
CREATE INDEX IF NOT EXISTS idx_reviews_review_date ON reviews(review_date);
CREATE INDEX IF NOT EXISTS idx_reviews_sentiment_score ON reviews(sentiment_score);
