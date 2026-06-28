# CodeAlpha_WebScraping
A Codealpha -Data analytics Project task focusing on how to scrap websites
# 🕷️ Biomedical Companies Web Scraping

A Python-based web scraping project that collects revenue data of the world's largest biomedical companies from Wikipedia, cleans the data, and saves it as a structured CSV file for further analysis.

---


## 📌 About

This project scrapes the **List of Largest Biomedical Companies by Revenue** from Wikipedia using Python. It extracts company names, countries, stock exchange listings, and annual revenue figures from 2016 to 2025. The raw data is cleaned to remove Wikipedia footnotes and special characters, then saved as a clean CSV file ready for analysis.

**Data Source:** [Wikipedia — List of Largest Biomedical Companies by Revenue](https://en.wikipedia.org/wiki/List_of_largest_biomedical_companies_by_revenue)

---

## 🛠️ Technologies Used

| Library | Purpose |
|---|---|
| `Python 3.14` | Programming language |
| `requests` | Sending HTTP requests to fetch web pages |
| `BeautifulSoup4` | Parsing and extracting HTML content |
| `pandas` | Data manipulation and CSV export |
| `re` | Cleaning footnotes and special characters |

---

## 📁 Project Structure

```
biomedical-webscraping/
├── Task I_Web Scraping.py              # Main scraping script
├── biomedical_companies_cleaned.csv    # Cleaned output data
├── requirements.txt                    # Required libraries
└── README.md                           # Project documentation
```

```
---

## ⚠️ Important Notes

- Always check a website's `robots.txt` before scraping
- A **User-Agent header** is required to access Wikipedia programmatically
- Add `time.sleep()` between requests to avoid overloading servers
- This project is for **educational and research purposes only**
- Respect the website's **Terms of Service**

---

## 📝 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---
