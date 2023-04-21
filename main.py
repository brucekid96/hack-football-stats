from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

driver.get("https://www.flashscore.com/football/europe/champions-league/")

wait = WebDriverWait(driver,10)


matches = wait.until(EC.presence_of_element_located((By.ID,"live-table")))

teams = matches.find_elements(By.CLASS_NAME,"event__participant")


team_names = []


for team in teams:
    team_name = team.text
    

    if team_name:


     team_names.append(team_name)


print(team_names)


driver.close()