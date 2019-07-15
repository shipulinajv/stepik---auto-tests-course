from selenium import webdriver

link = "https://www.degreesymbol.net/"
browser = webdriver.Chrome()
browser.get(link)

link = browser.find_element_by_link_text("» Degree symbol examples")
link.click()