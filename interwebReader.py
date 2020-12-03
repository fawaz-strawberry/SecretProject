from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select   # class for selecting elements from list
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

from webdriver_manager.chrome import ChromeDriverManager

import cv2
import numpy as np
import pyautogui

import random

from PIL import Image

import keyboard

import torch
import time

link = "https://bitbucket.org/"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get(link)

SCREEN_SIZE = (1920, 1080)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
driver.find_element_by_tag_name('html').screenshot('web_screenshot.png')

driver.save_screenshot("pageImage.png")
main_im = Image.open('pageImage.png')

## FIND ALL INPUT TAG ELEMENTS

elements = driver.find_elements_by_tag_name("input")
i = 0
for element in elements:
    location = element.location
    size = element.size
    

    # crop image
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']
    try:
        im = main_im.crop((int(x), int(y), int(width), int(height)))
        im.save('element' + str(i) + '.png')
        i += 1

        color = (255, 0, 0)
        thickness = 2
        image = cv2.imread("pageImage.png")
        image = cv2.rectangle(image, (int(x), int(y)), (int(width), int(height)), color, thickness)

        cv2.imwrite('pageImage.png', image)

    except:
        print("Couldn't Save certain element: " + str(i) + " skipping")
        i += 1



## FIND ALL A TAG ELEMENTS


elements = driver.find_elements_by_tag_name("a")
for element in elements:
    location = element.location
    size = element.size

    # crop image
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']
    try:
        im = main_im.crop((int(x), int(y), int(width), int(height)))
        im.save('element' + str(i) + '.png')
        i += 1

        color = (0, 255, 0)
        thickness = 2
        image = cv2.imread("pageImage.png")
        image = cv2.rectangle(image, (int(x), int(y)), (int(width), int(height)), color, thickness)

        cv2.imwrite('pageImage.png', image)

    except:
        print("Couldn't Save certain element: " + str(i) + " skipping")
        i += 1


elements = driver.find_elements_by_tag_name("img")
for element in elements:
    location = element.location
    size = element.size

    # crop image
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']
    try:
        im = main_im.crop((int(x), int(y), int(width), int(height)))
        im.save('element' + str(i) + '.png')
        i += 1

        color = (0, 0, 255)
        thickness = 2
        image = cv2.imread("pageImage.png")
        image = cv2.rectangle(image, (int(x), int(y)), (int(width), int(height)), color, thickness)

        cv2.imwrite('pageImage.png', image)

    except:
        print("Couldn't Save certain element: " + str(i) + " skipping")
        i += 1

driver.quit()