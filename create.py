#!/usr/bin/python
import time, sys, os
from dotenv import load_dotenv
from selenium import webdriver
load_dotenv()
path = os.getenv("FILEPATH")
email = os.getenv("EMAIL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
ghost = webdriver.Firefox()
ghost.maximize_window()
ghost.get('https://github.com/login')

def create():
    repoName = str(sys.argv[1])
    os.makedirs(path + repoName)
    py_btn = ghost.find_elements_by_xpath("//*[@id='login_field']")[0]
    py_btn.send_keys(email)
    py_btn = ghost.find_elements_by_xpath("//*[@id='password']")[0]
    py_btn.send_keys(password)
    py_btn = ghost.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[14]")
    py_btn.click()
    ghost.get('https://github.com/new')
    py_btn = ghost.find_elements_by_xpath("//*[@id='repository_name']")[0]
    py_btn.send_keys(repoName)
    py_btn = ghost.find_elements_by_xpath("/html/body/div[4]/main/div/form/div[6]/button")[0]
    py_btn.submit()
    time.sleep(5)
    ghost.close()

if __name__ == "__main__":
    create()
