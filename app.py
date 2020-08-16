import time

from PIL import Image
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Developer
# Hikmat Ullah
# me@hikmatu.com


def url_pages(initial_page, final_page):
    paginas = []
    book = f"https://bookshelf.vitalsource.com/#/books/<Course>/cfi/0!/4/4@0.00:55.2"
    for page in range(initial_page, final_page+1):
        url = f"https://bookshelf.vitalsource.com/#/books/<Course>/cfi/{page}!/4/4@0.00:55.2"



        paginas.append(url)

    return paginas


def login(driver, email, password):
    url =  f"https://bookshelf.vitalsource.com/#/user/signin"

    driver.get(url)

    time.sleep(10)
    btn_cookies=driver.find_element_by_xpath('//button/div/div[text()="Save"]')

    btn_cookies.click()

    time.sleep(20)
    username = driver.find_element_by_id("email-field")
    password = driver.find_element_by_id("password-field")

    time.sleep(5)
    username.send_keys(email)
    password.send_keys(password)
    password.send_keys(Keys.ENTER)

    time.sleep(5)


def save_screenshot(driver, length, width, file_name):
    driver.set_window_size(length, width)
    img_binary = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(img_binary))

    im_new = crop_center(img, length-100, width-200)

    im_new.save(file_name, quality=95)
    print(f"{file_name} Saved!")


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height-30) // 2))


def open_url(email, password, list_url_pages, course_title, length, width,initial_page):
    option = Options()
    option.headless = True
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Firefox(options=option)

    driver.maximize_window()
    login(driver, email, password)

    for page in range(0, len(list_url_pages)):
        page_for_file_name=(page+initial_page)

        driver.get(list_url_pages[page])
        time.sleep(6)
        save_screenshot(driver, length, width, f'{course_title}_{page_for_file_name}.png')


def main():
    #  Entradas de dados:
    print("\nDOWNLOAD IMAGES FROM PAGES OF VITALSOURCE LIBRARY")
    print("Before you do, read or README to avoid mistakes!\n")
    print("- Developed as a web-scraping study, I recommend that you do not commercialize or keep unauthorized copies of books")
    print("-> I have verified a limit of accesses, I bet this limit is necessary to preencher a captcha (I have not yet managed to break it (pois é do Google xD)\n")

    continue = 'YES'

    if continue == "YES":
        print("\n-> INFORMATION <-")
        email = 'email'
        password = 'password'
        course_title = 'courseTitle'
        initial_page = 0

        print(
            "\nI RECOMMEND TESTING THE RESOLUTIONS BEFORE PRINTING ALL PAGES! \ N "
            "THEREFORE, INSERT A QUANTITY LESS THAN 15 FOR TESTS")
        total_pages = 133
        final_page = (initial_page + total_pages)

        print("\nPAGES HAVE DIFFERENT RESOLUTIONS TO DEPEND ON THE BOOK, PERFORM TESTS OR CHECK THROUGH HTML")
        print(
            "-> RESOLUÇÕES <-:\n"
            "[1] 800 x 1065\n"
            "[2] 1600 x 2131\n"
            "[3] 2000 x 2664\n"
            "[4] 2000 x 2888\n")

        res = 4

        length, width = 0, 0
        if res == 1:
            length, width = 800, 1065
        elif res == 2:
            length, width = 1600, 2130
        elif res == 3:
            length, width = 2000, 2664
        elif res == 4:
            length, width = 2000, 2888


        list_url_pages = url_pages(initial_page, final_page)

        open_url(email, password, list_url_pages, course_title, length, width,initial_page)
    
    else:
        print('READ THE README!')
    

main()
