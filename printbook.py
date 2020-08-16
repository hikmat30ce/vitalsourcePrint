import argparse
import time
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# Developer
# Hikmat Ullah
# me@hikmatu.com


parser = argparse.ArgumentParser(description='Book printing started.....')
parser.add_argument('--course', required=True, type=str,
                    help='this is the course string in vitalsource url, example https://bookshelf.vitalsource.com/#/books/<Course>/cfi/0!/4/4@0.00:55.2')
parser.add_argument('--loginurl', default='https://bookshelf.vitalsource.com/#/user/signin', type=str,
                    help='this is login url for vital source, is it provided by default, if in future changed, please provide it here')
parser.add_argument('--email', required=True, type=str, help='Vitalsource account email address')
parser.add_argument('--password', required=True, type=str, help='Vitalsource account password')
parser.add_argument('--title', required=True, type=str, help='Book title')
parser.add_argument('--total_pages', required=True, type=int, help='Total pages in vitalsource')
parser.add_argument('--initial_page', default=0, type=int,
                    help='this param is required in case you want to print the book to pring from some page. default is 0')
parser.add_argument('--resolution', default=4, type=int, help='Resolution of the image captured from book page')
args = parser.parse_args()


def url_pages(initial_page, final_page):
    pages = []
    for page in range(initial_page, final_page + 1):
        url = f"https://bookshelf.vitalsource.com/#/books/{args.course}/cfi/{page}!/4/4@0.00:55.2"
        pages.append(url)
    return pages


def login(driver, email, password):
    url = f"{args.loginurl}"

    driver.get(url)
    time.sleep(10)
    btn_cookies = driver.find_element_by_xpath('//button/div/div[text()="Save"]')
    btn_cookies.click()

    time.sleep(20)
    usernameelement = driver.find_element_by_id("email-field")
    passwordelement = driver.find_element_by_id("password-field")

    time.sleep(5)
    usernameelement.send_keys(email)
    passwordelement.send_keys(password)
    passwordelement.send_keys(Keys.ENTER)
    time.sleep(5)


def save_screenshot(driver, length, width, file_name):
    driver.set_window_size(length, width)
    img_binary = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(img_binary))

    im_new = crop_center(img, length - 100, width - 200)

    im_new.save(file_name, quality=95)
    print(f"{file_name} Saved!")


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height - 30) // 2))


def open_url(email, password, list_url_pages, course_title, length, width, initial_page):
    option = Options()
    option.headless = True
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Firefox(options=option)

    driver.maximize_window()
    login(driver, email, password)

    for page in range(0, len(list_url_pages)):
        page_for_file_name = (page + initial_page)

        driver.get(list_url_pages[page])
        time.sleep(6)
        save_screenshot(driver, length, width, f'{course_title}_{page_for_file_name}.png')


res = args.resolution
length, width = 0, 0
if res == 1:
    length, width = 800, 1065
elif res == 2:
    length, width = 1600, 2130
elif res == 3:
    length, width = 2000, 2664
elif res == 4:
    length, width = 2000, 2888
list_url_pages = url_pages(args.initial_page, (args.initial_page + args.total_pages))

open_url(args.email, args.password, list_url_pages, args.title, length, width, args.initial_page)
