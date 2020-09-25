import sys
from selenium import webdriver

url = sys.argv[1]
name = sys.argv[2]

print(f"Creating screenshot from {url}")
print(f"Creating screenshot with name: {name}")
print("wait until done message is shown")

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)

driver.get(url)
height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(("1440"), (height))  # May need manual adjustment


driver.save_screenshot(f"/Users/Remco/Sites/screenshots_websites/{name}.png")


driver.close()
print("Screenshot Done")
