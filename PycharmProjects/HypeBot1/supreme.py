from selenium import webdriver
from time import sleep

type = input()
name = input()
browser = webdriver.Chrome(executable_path='/Users/ryangould/PycharmProjects/HypeBot1/chromedriver')
browser.set_window_size(900,900)
browser.set_window_position(0,0)
sleep(1)
browser.get("https://www.supremenewyork.com/shop")

elems = browser.find_elements_by_xpath("//a[@href]")
elems = elems[3:]
products = []

#creates list of product URLS
for elem in elems:
    x = str(elem.get_attribute("href"))
    if x.find(type): #adds products to list if they match product type
        products.append(elem.get_attribute("href"))

y = 0;
for x in products:
    y = y+1
    browser.get(products[y])
    pname = browser.find_element_by_class_name('protect').text
    #iterates through URLS until correct product is found
    if pname == name:
        break
#click add to cart
python_button = browser.find_elements_by_xpath('//*[@id="add-remove-buttons"]/input')[0]
python_button.click()

#checkout
button2 = browser.find_elements_by_xpath('//*[@id="cart"]/a[2]')[0]
button2.click()
sleep(1)

#enter shipping information
fieldbox = browser.find_element_by_xpath('//*[@id="cart-address"]')
fieldbox.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys('Ryan Gould')
fieldbox.find_element_by_xpath('//*[@id="order_email"]').send_keys('gouldr@wit.edu')
fieldbox.find_element_by_xpath('//*[@id="order_tel"]').send_keys('207-752-6067')
fieldbox.find_element_by_xpath('//*[@id="bo"]').send_keys('98 calumet street')
fieldbox.find_element_by_xpath('//*[@id="oba3"]').send_keys('2')
fieldbox.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys('02120')
fieldbox.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys('Boston')

#Enter payment information
fieldbox2 = browser.find_element_by_xpath('//*[@id="cart-cc"]/fieldset')
fieldbox2.find_element_by_xpath('//*[@id="nnaerb"]').send_keys('Credit Card #')
fieldbox2.find_element_by_xpath('//*[@id="credit_card_month"]/option[text()="08"]').click()
fieldbox2.find_element_by_xpath('//*[@id="credit_card_year"]/option[text()="2020"]').click()
fieldbox2.find_element_by_xpath('//*[@id="orcer"]').send_keys('611')
fieldbox2.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()

#process payment
cartFooter = browser.find_element_by_xpath('//*[@id="cart-footer"]')
cartFooter.find_element_by_xpath('//*[@id="pay"]/input').click()

sleep(20)
browser.close()
