
#firefox --new-tab "https://en.savefrom.net/1-youtube-video-downloader-384/"





    # Finding the search field by id
input = driver.find_element_by_id("sf_url")
     
    # Sending input text to search field
input.send_keys("Python")
     
    # Pressing enter to search input text
input.send_keys(Keys.ENTER)
sleep(10)
input()