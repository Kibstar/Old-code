from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://www.amazon.co.uk')
searchElem = browser.find_element_by_css_selector('#twotabsearchtextbox')
searchElem.click()
searchElem.send_keys('Canon 77D')
searchElem.submit()