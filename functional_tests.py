# from pyvirtualdisplay import Display
from selenium import webdriver

# display = Display(visible=0, size=(1024, 768))
# display.start()

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'overlord' in browser.title
