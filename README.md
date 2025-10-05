# **Web Scraper**

The goal was to extract supplier data (Name, Email, Profile Link) for 'Video' and 'UGC' roles from public creator directories.

The project successfully demonstrates a robust, real-world approach to web scraping, including tackling progressively difficult anti-scraping measures.

---
## **Tech Stack & Tools Used**

* **Python**: The core programming language.
* **Selenium**: For browser automation to handle JavaScript-heavy sites and bypass anti-scraping measures.
* **BeautifulSoup4**: For parsing the HTML content.
* **Pandas**: For data cleaning, validation, and exporting to CSV (intended use).

---
## **Setup and Installation**

To run this project, you'll need Python 3 installed.

### **1. Navigate to the Project Folder**
Open a terminal and navigate to the project directory:
```bash
cd path/to/roster-scraper

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
# source venv/bin/activate
