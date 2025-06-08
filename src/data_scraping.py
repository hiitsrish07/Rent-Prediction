#webdriver is what lets selenium interact with browsers selenium> webdriver>chrome
from selenium import webdriver
#By lets you find elements in the browser eg By.ID
from selenium.webdriver.common.by import By
import time
import pandas as pd

#Chrome, Edge, Opera are built on the base/source code chromium . ChromeOptions enables you to interact with these browsers in a 
#centralized way. If you do not use ChromeOptions, selenium will launch chrome browser in default mode you wont beable to customize 
#anything 
opt = webdriver.ChromeOptions()
#Adding argument here is basicall passing CLI commands to your ChromeOptions saying I want my browser to launch headless(without UI) and without any extensions
# opt.add_argument("--headless")
opt.add_argument("--disable-extensions")

#Launch the chrome browser with the opt mentioned above 
driver = webdriver.Chrome(options=opt)
driver.get("https://www.nobroker.in/property/rent/Pune/pune?searchParam=W3sibGF0IjoxOC41NTc3NDQ2LCJsb24iOjczLjkxMjQ2NzQsInBsYWNlSWQiOiJDaElKaVNGeWVzWEF3anNScmN5RkZzUHlzTkUiLCJwbGFjZU5hbWUiOiJQdW5lIn1d&radius=2.0&sharedAccomodation=0&city=pune&locality=Pune")
time.sleep(5)

titles, rents, bhks, furnishings, areas = [], [], [], [], []

listings = driver.find_elements(By.TAG_NAME, 'article')[:10]

for listing in listings:
    title = listing.find_element(By.TAG_NAME, 'h2').text
    full_rent_text = listing.find_element(By.ID, "minimumRent").text
    rent = full_rent_text.split('+')[0].strip()
    bhk = listing.find_element(By.CSS_SELECTOR, "div.font-semibold.whitespace-nowrap").text
    # furnishing = listing.find_element(By.CSS_SELECTOR, "span.flex.justify-center").text




    titles.append(title)
    rents.append(rent)
    bhks.append(bhk)
    # furnishings.append(furnishing)

driver.quit()

# Create DataFrame
df = pd.DataFrame({
    'title': titles,
    'rent' : rents,
    'bhk'  : bhks
    # 'Furnishing' : furnishings
})

# Save to CSV
df.to_csv("pune_rent_listings.csv", index=False)
print("Saved 10 listings to pune_rent_listings.csv")
