from selenium import webdriver
from selenium.webdriver.common.by import By

from dis_webhook import webhook_embed

import schedule
import time

url = "https://www.quikfixlaptopkeys.com/?product=asus-rog-flow-x16-gv601-keyboard-key-replacement-kit"
driver = webdriver.Chrome()
counter = 1

def send_webhook_msg(title, msg):
    webhook_embed(title, msg)
    return

def item_stock_checker():
    global counter
    try:
        #print("Opening page")
        driver.get(url)

        #print("Checking Page title")
        assert "ASUS ROG Flow X16 GV601 Replacement" in driver.title
        #print("Title found")

        #print("Finding black button image")
        black_img_button = driver.find_element(By.CSS_SELECTOR, 'div[data-value="key-color-black"]')

        if black_img_button:
            #print("Image Found")
            black_img_button.click()

            #print("Find Dropdown menu")
            drop_down_elem = driver.find_element(By.CSS_SELECTOR, 'select[data-attribute_name="attribute_pa_key"]')
            drop_down_elem.click()

            #print("Find \"e\" option")
            e_option_elem = driver.find_element(By.CSS_SELECTOR, 'option[value="key-e"]')
            e_option_elem.click()
            drop_down_elem.click() # close dropdown

            #print("Check if item in stock")
            check_stock = driver.find_element(By.CSS_SELECTOR, 'button[class="single_add_to_cart_button button alt wp-element-button disabled wc-variation-is-unavailable"]')

            if check_stock:
                #print("Find item stock info")
                button_text = check_stock.text
                print(button_text)
                instock = True if "Out" not in button_text else False
                if instock:
                    title = ''
                    msg = f"{counter}🟢: IN STOCK!"
                    send_webhook_msg(title, msg)
                else:
                    title = ''
                    msg = f"{counter}🔴: Not in stock"
                    send_webhook_msg(title, msg)

                counter += 1
        else:
            print("Image not found")
    except Exception as e:
        print("/n/n")
        send_webhook_msg("**CODE ERROR**", str(e))
        exit()

def main():
    schedule.every(10).minutes.do(item_stock_checker)
    item_stock_checker()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()