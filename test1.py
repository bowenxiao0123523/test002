from selenium import webdriver

def get_tab_count():
    # 创建一个浏览器驱动实例
    driver = webdriver.Chrome()  
    tab_count = len(driver.window_handles)
    driver.quit()
    return tab_count

print(get_tab_count())
