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

### **Navigate to the Project Folder**
Open a terminal and navigate to the project directory:
```bash
cd path/to/roster-scraper

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
# source venv/bin/activate

#Install Dependencies
pip install -r requirements.txt

#Run the Scraper
python scraper.py
````

### **Final Outcome & Conclusion**

While the script is technically successful in launching a browser, navigating to the target, and waiting for content, the final data extraction was prevented by the website's advanced anti-scraping measures.
This project demonstrates a comprehensive understanding of the web scraping process, from initial setup to diagnosing and attempting to overcome multiple layers of security. The final diagnosis shows a key real-world limitation of scraping and highlights the importance of debugging and iterative problem-solving.
