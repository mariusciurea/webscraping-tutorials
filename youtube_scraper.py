from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)
driver.get("http://youtube.com/MariusCiurea1")

agree_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button')))
agree_button.click()

chn_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'style-scope ytd-channel-name')))
chn_subs = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#subscriber-count')))

video_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div')))
video_tab.click()
time.sleep(10)

print('Channel name: ', chn_name.text)
print('Channel subs: ', chn_subs.text)

height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    time.sleep(1.5)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == height:
        break
    height = new_height

video_details = driver.find_elements(By.ID, 'dismissible')
video_list = []
for detail in video_details:
    title = detail.find_element(By.ID, 'video-title')
    views = detail.find_element(By.ID, 'metadata-line')
    video_dict = {
        'title': title.text,
        'views': views.text.split('\n')[0],
        'date_posted': views.text.split('\n')[1]
    }
    video_list.append(video_dict)

df = pd.DataFrame(video_list)
print(df)