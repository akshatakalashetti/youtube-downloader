from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome(ChromeDriverManager().install())
#opening link 
driver.get("https://en.savefrom.net/1-youtube-video-downloader-384/")
driver.close
#searching search bar with path
search_bar = driver.find_element_by_xpath('//*[@id="sf_url"]')
enter_link= input("Enter the youtube link you want to download")
search_bar.send_keys(enter_link)
#clicking submit button
submit_button  = driver.find_element_by_id("sf_submit").click() 
#waiting  to search
sleep(5)

print("downloading....")
#clicking download button
elements = driver.find_element_by_xpath('//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a').click()
print("video downloaded....")

