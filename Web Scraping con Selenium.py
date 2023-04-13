from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = '/Users/frank/Downloads/chromedriver' #escribe tu ruta aqui


driver = webdriver.Chrome(path)

driver.get(website)


# Wait for the "All matches" button to be clickable
all_matches_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//label[@analytics-event="All matches"]'))
)

all_matches_button.click()

matches = EC.find_elements(By.TAG_NAME,'tr')
for match in matches:
    print(match.text)

