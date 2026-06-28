import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://en.wikipedia.org/wiki/List_of_largest_biomedical_companies_by_revenue'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
tables = soup.find_all("table")
table = soup.find_all("table")[0]
rows = table.find_all("tr")

# Get column names from header row
column_names = [th.get_text(strip=True) for th in rows[0].find_all("th")]
column_names = [re.sub(r'\[.*?\]', '', col).strip() for col in column_names]
print("Columns:", column_names)

# Get data rows
data = []
for row in rows[1:]: # Skip header row
    cols = row.find_all("td")
    if cols:
        cleaned = [re.sub(r'\[.*?\]', '', col.get_text(strip=True)).strip() for col in cols]
        data.append(cleaned)

# Create DataFrame with column names
df = pd.DataFrame(data, columns=column_names)

# Convert year columns to numeric
year_columns = ['2025', '2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016']
for col in year_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

print(df.head())

# Save cleaned CSV
df.to_csv("biomedical_companies_cleaned.csv", index=False)
print("Saved cleaned CSV!")
