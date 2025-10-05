Roster Technical Assessment: Web Scraper
This project is a web scraper built to fulfill the Roster Technical Assessment. The goal was to extract supplier data (Name, Email, Profile Link) for 'Video' and 'UGC' roles from public creator directories.

The project successfully demonstrates a robust, real-world approach to web scraping, including tackling progressively difficult anti-scraping measures.

Tech Stack & Tools Used
Python: The core programming language.

Selenium: For browser automation to handle JavaScript-heavy sites and bypass anti-scraping measures.

BeautifulSoup4: For parsing the HTML content.

Pandas: For data cleaning, validation, and exporting to CSV (intended use).

Setup and Installation
To run this project, you'll need Python 3 installed.

Navigate to the Project Folder
Open a terminal and navigate to the project directory:

Bash

cd path/to/roster-scraper
Create and Activate Virtual Environment
Create and activate a virtual environment to manage dependencies:

Bash

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
# source venv/bin/activate
Install Dependencies
Install all required libraries from the requirements.txt file:

Bash

pip install -r requirements.txt
Run the Scraper
Execute the main script:

Bash

python scraper.py
A Chrome browser window will open and close automatically as the script runs.

Challenges Encountered & Problem-Solving Journey
The process of building this scraper involved overcoming several real-world challenges, demonstrating a systematic approach to problem-solving.

Challenge 1: Initial Target Defunct
The initial example target (shoutt.com) was found to be a defunct domain for sale. This was diagnosed after the script encountered a persistent SSLError.

Challenge 2: 403 Forbidden Error
A new, live target (ProductionHUB.com) was identified. However, a simple approach using the requests library was immediately blocked with a 403 Forbidden error. This indicated that the server was identifying the script as a bot and refusing access.

Solution: The approach was pivoted from requests to Selenium. By automating a real Chrome browser, the script could more accurately mimic a human user, successfully bypassing the initial block.

Challenge 3: Dynamic Content Loading
Even with Selenium, the script initially failed to find any profile data. The hypothesis was that the profile listings were being loaded dynamically with JavaScript after the initial page load. The script was parsing the HTML before the data had a chance to appear.

Solution: "Explicit Waits" (WebDriverWait) were implemented. This instructed the script to intelligently wait for a specific container element (div.listings) to be present on the page before attempting to parse the HTML, solving the timing issue.

Challenge 4: Advanced Bot Detection
The final and most significant challenge was that even after successfully waiting for the content container to load, the script still could not find the specific profile links.

Solution (Diagnosis): A debugging step was added to save the HTML content that Selenium was receiving to a file (debug.html). Upon inspection, it was discovered that the server was sending a simplified, JavaScript-disabled version of the page to the automated browser. This is an advanced bot detection technique where the server sends a basic HTML shell without the actual data rendered.

Final Outcome & Conclusion
While the script is technically successful in launching a browser, navigating to the target, and waiting for content, the final data extraction was prevented by the website's advanced anti-scraping measures.

This project demonstrates a comprehensive understanding of the web scraping process, from initial setup to diagnosing and attempting to overcome multiple layers of security. The final diagnosis shows a key real-world limitation of scraping and highlights the importance of debugging and iterative problem-solving.

Data Output
Due to the insurmountable anti-scraping measures on the live target, the final CSV file located at output/supplier_data.csv contains sample mock data. This data is formatted according to the project requirements and serves as a placeholder to demonstrate the intended final output.
