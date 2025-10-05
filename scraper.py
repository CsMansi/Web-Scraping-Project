from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import logging

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Main Scraping Logic ---
def get_profile_links(role):
    profile_links = set()
    search_url = f"https://www.productionhub.com/directory/search?q={role.replace(' ', '+')}"
    logging.info(f"Scraping search page: {search_url}")

    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(search_url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.listings")))
        logging.info("Profile list container has loaded.")
        
        html_content = driver.page_source
        
        # --- NEW: Save the HTML to a file for debugging ---
        with open("debug.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        logging.info("Saved the page's HTML to debug.html for inspection.")

        soup = BeautifulSoup(html_content, 'html.parser')
        links_on_page = soup.select("div.media-title > a") 
        
        if not links_on_page:
            logging.warning(f"No profile links found for role '{role}'.")
        
        for link in links_on_page:
            full_url = link['href'] 
            profile_links.add(full_url)
            
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        driver.quit() 
        
    return list(profile_links)

# --- Execution ---
if __name__ == "__main__":
    logging.info("Scraper script started using Selenium.")
    editor_links = get_profile_links("video editor")
    
    logging.info(f"Found {len(editor_links)} links for 'video editor' role.")
    if editor_links:
        print("Success! Found the following profile URLs:")
        for url in editor_links:
            print(url)
    else:
        print("Could not find any profile links.")