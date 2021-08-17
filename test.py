from selenium import webdriver
import os
import time
from getpass import getpass
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.manager import DriverManager
from webdriver_manager.opera import OperaDriverManager


def login(subject):
    email='#email'		#Replace with Email here
    password='#Password'	#Replace with Password here
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1, 
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.geolocation": 2
    })

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
    driver.get('https://meet.google.com')

    bot=driver
    if subject=='dccn':
        ur='cn2m6mzbfj'
    elif subject=='iwt':
        ur='hoa7qyb4kf'
    elif subject=='toc':
        ur='b7svmgx5pz'
    elif subject=='os':
        ur='d7indqnwfa'
    elif subject=='se':
        ur='dcojwkdy3e'
    elif subject=='ice':
        ur='dvfkjwlihk'
    elif subject=='robo':
        ur='aphwkts6vm'
    elif subject=='lab':
        ur='error'
    else:
        ur=subject

    bot.find_element_by_xpath(
		'//span[@class="cta-wrapper"]/a').click()
    time.sleep(2)

    bot.find_element_by_xpath(
        '//div[@class="Xb9hP"]/input').send_keys(email)
    time.sleep(4)

    bot.find_element_by_xpath(
        '//div[@class="VfPpkd-dgl2Hf-ppHlrf-sM5MNb"]/button').click()
    time.sleep(4)

    bot.find_element_by_xpath(
        '//div[@class="Xb9hP"]/input').send_keys(password)
    time.sleep(4)

    bot.find_element_by_xpath(
        '//div[@class="VfPpkd-dgl2Hf-ppHlrf-sM5MNb"]/button').click()
    time.sleep(4)
    
    bot.find_element_by_xpath(
        '//label[@class="VfPpkd-fmcmS-yrriRe VfPpkd-fmcmS-yrriRe-OWXEXe-mWPk3d VfPpkd-ksKsZd-mWPk3d VfPpkd-fmcmS-yrriRe-OWXEXe-di8rgd-V67aGc VfPpkd-fmcmS-yrriRe-OWXEXe-INsAgc VfPpkd-fmcmS-yrriRe-OWXEXe-SfQLQb-M1Soyc-Bz112c cfWmIb orScbe h7XSnb"]/input').send_keys(ur)
    time.sleep(4)

    bot.find_element_by_xpath(
        '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d cjtUbb"]').click()
    time.sleep(4)
    #closing camera
    bot.find_element_by_xpath(
        '//div[@class="GOH7Zb"]/div/div').click()
    time.sleep(4)
    #closing mic
    bot.find_element_by_xpath(
        '//div[@class="dP0OSd"]/div/div').click()
    time.sleep(4)
    #clicking join button
    bot.find_element_by_xpath(
        '//div[@class="XCoPyb"]/div').click()
    time.sleep(4)
    enter_username = WebDriverWait(bot, 20).until(
	expected_conditions.presence_of_element_located((By.NAME, 'username')))
    enter_username.send_keys(email)
    enter_password = WebDriverWait(bot, 20).until(
	expected_conditions.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(password)
    enter_password.send_keys(Keys.RETURN)
    time.sleep(10)


sub=str(input('Enter the subject: (or any custom meet url:) '))
#driver=webdriver.Chrome(ChromeDriverManager().install())
#driver.close()
login(sub)
