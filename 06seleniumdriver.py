from example import webdriver
from example.webdriver.chrome.service import Service
import time
# options
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')


url = 'https://csg.bet/'
service = Service()


driver = webdriver.Chrome(service=service, options=options)

try:
 driver.get(url=url)
 time.sleep(10)
except Exception as ex:
    print(ex)
finally:
 driver.close()
 driver.quit()

