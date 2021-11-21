from selenium import webdriver
import datetime
import time


def main():
    print('this message is from main function')

    driver = webdriver.Chrome()
    # 窗口最大化显示
    driver.maximize_window()
    driver.get("https://www.taobao.com/")
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("亲，请登录").click()
    time.sleep(30)


if __name__ == '__main__':
    main()
