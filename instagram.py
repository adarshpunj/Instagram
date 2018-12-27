#This code was written by Adarsh Punj in December 2018
#follow_fans_of(page): string (Target Page username)
#unfollow_users: int (Number of users to be unfollowed)
#post() function is under development

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from pynotify import pynotify
from random import randint
from strings import string
import time
import requests
import os

driver = None

def sleep(x):
    time.sleep(x)

def configure_environment():
    global driver
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('disable-extensions')
    options.add_argument(string().user_agent)
    driver = webdriver.Chrome(string().chromedriver_path
    ,chrome_options=options)

def login():
    driver.get("https://www.instagram.com/accounts/login")
    login_credentials = driver.find_elements_by_css_selector(
    "._2hvTZ.pexuQ.zyHYP")

    login_credentials[0].send_keys(string().username)
    sleep(1)
    login_credentials[1].send_keys(string().password)
    sleep(1)
    click_login = driver.find_elements_by_css_selector(
    "._0mzm-.sqdOP.L3NKy")[1].click()
    sleep(3)
    pynotify("Instagram Bot","Logged into Instagram").push()

def post():
    driver.get("https://instagram.com/"+string().username)
    driver.find_element_by_css_selector(
    ".glyphsSpriteNew_post__outline__24__grey_9.u-__7").click().send_keys(
    '/Users/adarshpunj/Desktop/post.png')

def get_following_list():
    driver.get("https://www.instagram.com/"+string().username)
    following = driver.find_elements_by_css_selector(".-nal3")[2].click()
    sleep(5)
    first_scroll_timeout = time.time()+5
    total_scroll_timeout = time.time()+25

    driver.find_element_by_css_selector("._7UhW9.xLCgt.MMzan._0PwGv.fDxYl").click()

    while time.time()<first_scroll_timeout:
        ActionChains(driver).send_keys(Keys.DOWN).perform()
        sleep(0.1)

    driver.find_element_by_css_selector(".wFPL8").click()

    while time.time()<total_scroll_timeout:
        ActionChains(driver).send_keys(Keys.DOWN).perform()

def print_following_list():
    get_following_list()
    users = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
    for i in range(0,len(users)):
        print users[i].get_attribute('title')
    print "TOTAL FOLLOWERS: "+str(len(users))

def follow_fans_of(page):
    total_follows = 0
    pynotify("INSTAGRAM BOT","Targetting page @"+page).push()
    driver.get("https://www.instagram.com/"+page)
    driver.find_element_by_css_selector(".Nnq7C.weEfm").click()
    sleep(3)
    try:
        driver.find_element_by_css_selector("._0mzm-.sqdOP.yWX7d._8A5w5").click()
    except:
        pynotify("Instagram Bot"
        ,"Error while targetting user @"+page+". Unable to fetch likes list").push()
    time.sleep(3)
    follow_buttons = driver.find_elements_by_css_selector("._0mzm-.sqdOP.L3NKy")

    for button in range(0,len(follow_buttons)):
        if(follow_buttons[button].text=="Follow"):
            try:
                follow_buttons[button].click()
                pynotify("Instagram Bot","Followed a user").push()
                total_follows = total_follows+1
                sleep(randint(20,50))
            except:
                pynotify("Instagram Bot","Error while targetting user @"+page).push()
                break
    pynotify("Instagram Bot","Total Follows in the session: "+str(total_follows)).push()

def follow_users():
    for page in string().target_pages:
        try:
            follow_fans_of(page)
        except:
            follow_fans_of(string().target_pages[
            string().target_pages.index(page)+1])
        sleep(randint(30,40))

def unfollow_users(limit):
    get_following_list()
    users_unfollowed = 0
    unfollow_button = driver.find_elements_by_css_selector("._0mzm-.sqdOP.L3NKy._8A5w5")
    sleep(3)
    for i in range(1,len(unfollow_button)):
        sleep(randint(30,40))
        driver.execute_script("arguments[0].click();", unfollow_button[-i])
        sleep(1)
        confirm_unfollow_button = driver.find_element_by_css_selector(".aOOlW.-Cab_")
        confirm_unfollow_button.click()
        pynotify("Instagram Bot","Unfollowed a user").push()
        users_unfollowed = users_unfollowed+1
        if users_unfollowed == limit:
            os.system("say "+str(users_unfollowed)+"unfollowed. Aborting the function.")
            driver.get("https://instagram.com/")
            break

def retrieve_data_from_access_tool(data_name):
    data_list = []
    driver.get("https://www.instagram.com/accounts/access_tool/"+data_name)
    while True:
        try:
            driver.find_element_by_css_selector("._0mzm-.sqdOP.L3NKy").click()
            sleep(0.5)
        except:
            break
    try:
        element_list = driver.find_elements_by_class_name("-utLf")
        for element in element_list:
            data_list.append(element.text)
    except:
        pass
    return data_list

def get_summary():
    accounts_you_follow = retrieve_data_from_access_tool(
    "accounts_you_follow")
    accounts_following_you = retrieve_data_from_access_tool(
    "accounts_following_you")
    current_follow_requests = retrieve_data_from_access_tool(
    "current_follow_requests")

    print "ACCOUNTS YOU FOLLOW: "+len(accounts_you_follow)
    for accounts in accounts_you_follow:
        print accounts

    print '\n'
    print "ACCOUNTS FOLLOWING YOU:"+len(accounts_following_you)
    for accounts in accounts_following_you:
        print accounts

    print '\n'
    print "YOU BOTH FOLLOW EACH OTHER:"
    for accounts in accounts_following_you and accounts_you_follow:
        print accounts

    print '\n'
    print "ACCOUNTS THAT ARE NOT FOLLOWING YOU:"

    for accounts in accounts_you_follow:
        if accounts in accounts_following_you:
            pass
        else:
            print accounts
