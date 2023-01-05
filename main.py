# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# Change the channel name below (keep the quotation marks)
channel_name = "my_channel"

# Set necessary variables
site = f"https://www.twitch.tv/{channel_name}"
path_to_webdriver = "./msedgedriver"
vpn_extension = "./vpn.crx"
vpn_html = "chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/html/foreground.html"
sleep_time = 60*60    # 1 hour runtime

# Edgedriver Options
options = Options()
options.add_extension(vpn_extension)
driver_service = Service(executable_path=path_to_webdriver)
driver = webdriver.Edge(service=driver_service, options=options)

# Close the VPN installation window and load the VPN HTML
while True:
    if len(driver.window_handles) == 2:
        break
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.get(vpn_html)

# Navigate through the menu and connect to VPN
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@class="next"]')))
for i in range(2):
    driver.find_element(by="xpath", value='//button[@class="next"]').click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@id="mainBtn"]')))
driver.find_element(by="xpath", value='//div[@id="mainBtn"]').click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="connected"]')))

# Let the show begin
driver.get(site)
sleep(sleep_time)
