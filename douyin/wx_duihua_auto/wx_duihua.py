import time
from PIL import Image
from selenium import webdriver


def rand_username_face(browser):
    """
    随机头像和用户名
    :param browser:
    :return:
    """
    username_btn = browser.find_elements_by_class_name('btn-rand-username')
    face_btn = browser.find_elements_by_class_name('btn-rand-face')

    for i in range(len(username_btn)):
        time.sleep(1)
        username_btn[i].click()
        face_btn[i].click()


def screenshot_iphone(browser):
    js = "document.getElementsByClassName('i-body')[0].scrollTop=10000"
    browser.execute_script(js)
    iphone = browser.find_element_by_id('iphone')
    iphone.screenshot('rr.png')
    # print(iphone.size)
    # size = iphone.size
    # # browser.find_element_by_id('iphone').screenshot('rr.png')
    # browser.find_element_by_class_name('i-body').screenshot('rrr.png')
    # time.sleep(1)
    left = top = 0
    right = 376
    bottom = 668
    # right = size['width']
    # bottom = size['height']
    im = Image.open('rr.png')
    im_crop = im.crop((left, top, right, bottom))
    im_crop.save('rrr.png')


def main(browser):
    """
    生成文本对话
    :param browser:
    :return:
    """
    a_u_contents = browser.find_elements_by_xpath('//textarea[starts-with(@class, "a-u-content")]')
    user1 = a_u_contents[0]
    user2 = a_u_contents[1]
    add_content = browser.find_elements_by_xpath('//div[@class="a-u-dialog"]/a')
    add1 = add_content[0]
    add2 = add_content[1]
    with open('rr', 'r', encoding='utf8') as f:
        contents = f.read()
        contents = contents.split('\n')
        print(contents)
        for content in contents:
            time.sleep(1)
            key, value = content.split(':')
            if key == '0':
                print('user1')
                user1.clear()
                user1.send_keys(value)
                add1.click()
                is_del_duihua(browser)
                screenshot_iphone(browser)
            elif key == '1':
                print('user2')
                user2.clear()
                user2.send_keys(value)
                add2.click()
                is_del_duihua(browser)
                screenshot_iphone(browser)
            else:
                print('error user !!!')


def is_del_duihua(browser):
    nav_tabs = browser.find_elements_by_xpath('//ul[contains(@class, "nav-tabs")]/li')
    show_setting = nav_tabs[0]
    duihua_setting = nav_tabs[1]

    show_setting.click()
    time.sleep(1)
    browser.find_elements_by_name('i-b-nick1')[1].click()
    time.sleep(1)
    duihua_setting.click()
    time.sleep(1)


def _init(browser):
    top_name = browser.find_element_by_class_name('input-common')
    top_name.clear()
    top_name.send_keys('')

    nav_tabs = browser.find_elements_by_xpath('//ul[contains(@class, "nav-tabs")]/li')
    show_setting = nav_tabs[0]
    duihua_setting = nav_tabs[1]
    duihua_setting.click()

    # browser.find_element_by_xpath('//input[contains(@class, "clear-dialog")]').click()
    msg_del = browser.find_elements_by_xpath('//a[@class="msg-del"]')
    for i in msg_del:
        i.click()

    browser.find_element_by_class_name('a-u-dialog-master').click()


browser = webdriver.Chrome()
browser.get('http://127.0.0.1:8888/default.html')
browser.maximize_window()
_init(browser)
# rand_username_face(browser)
main(browser)
time.sleep(3)
browser.close()
