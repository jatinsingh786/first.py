import unittest
from selenium import webdriver
import time

path = '/home/jatin/Downloads/chromedriver'

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()


    def test_tabc(self):

        driver = self.driver
        driver.get('https://www.toolsqa.com/automation-practice-form/')


        a = driver.find_element_by_css_selector('div.wpb_wrapper > h1').text
        self.assertEqual(a,'Practice Automation Form')

        time.sleep(3)
        driver.find_element_by_partial_link_text('Partial').click()
        time.sleep(3)

        driver.find_element_by_link_text('Link Test')
        time.sleep(3)

        driver.find_element_by_name('firstname').send_keys('Krishna')





       #send keys to last name
        driver.find_element_by_name('lastname').send_keys('kriti')
        time.sleep(3)


        #select sex as male
        driver.find_element_by_id('sex-0').click()
        time.sleep(3)

        #select years of experience as 5
        driver.find_element_by_id('exp-4').click()
        time.sleep(3)


        #send date as 12/12/12
        driver.find_element_by_css_selector('#datepicker').send_keys('12/12/12')
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()