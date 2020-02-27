import time

from selenium import webdriver
import unittest

class Calculatortest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000/')
        #เขาสังเกตเห็นข้อความบนเว็บว่ามีคำว่า Calculator
        #เขาได้ลองใช้ app นี้โดยลองใส่ค่าลงไปแล้วกดปุ่ม  find value
        # เขาได้ใสเลข 3 และ เลข 5
        clear_history = self.browser.find_element_by_name('clear_history')
        clear_history.click()
        num1=self.browser.find_element_by_name('x')
        num1.send_keys(3)
        num2 = self.browser.find_element_by_name('y')
        num2.send_keys(5)

        #เขาได้เลือกเครื่องหมาย +
        select_operate_plus = self.browser.find_element_by_xpath("//input[@value='+']")
        select_operate_plus.click()
        #เขากดปุม   find value
        find_value_button = self.browser.find_element_by_name('find value')
        find_value_button.click()
        #เขาได้เห็นคำตอบที่แสดงออกมา
        result = self.browser.find_element_by_tag_name('body').text
        self.assertIn("8",result)
        #เขาลองใส่ผลลัพธ์ลองดูอีกรอบ
        #เขาได้ใสเลข 20 และ เลข 30
        num1 = self.browser.find_element_by_name('x')
        num1.send_keys(30)
        num2 = self.browser.find_element_by_name('y')
        num2.send_keys(20)
        # เขาได้เลือกเครื่องหมาย + - * / และกดปุ่ม find value อีกรอบ
        select_operate_plus = self.browser.find_element_by_xpath("//input[@value='+']")
        select_operate_plus.click()
        select_operate_minus = self.browser.find_element_by_xpath("//input[@value='-']")
        select_operate_minus.click()
        select_operate_minus = self.browser.find_element_by_xpath("//input[@value='*']")
        select_operate_minus.click()
        select_operate_minus = self.browser.find_element_by_xpath("//input[@value='/']")
        select_operate_minus.click()
        find_value_button = self.browser.find_element_by_name('find value')
        find_value_button.click()
        #เขาเห็นคำตอบที่ได้คือ 50 10 600 ตามลำดับ
        result = self.browser.find_element_by_tag_name('body').text
        self.assertIn("the result 30 + 20 is :50", result)
        self.assertIn("the result 30 - 20 is :10", result)
        self.assertIn("the result 30 * 20 is :600", result)
        self.assertIn("the result 30 / 20 is :1.5", result)
        time.sleep(2)
        #เขาได้เห็นหัวข้อชื่อว่า history
        history_head = self.browser.find_element_by_xpath("//h1[@name='history']").text
        self.assertIn("History",history_head)
        #เขาได้เจอกับประวัติที่เขาเคยทำการคิดคำนวณ
        result = self.browser.find_element_by_tag_name('body').text
        self.assertIn("the result 3+5 is :8",result)
        # เขาได้เห็นปุ่ม clear history และลองกด
        clear_history = self.browser.find_element_by_name('clear_history')
        clear_history.click()
        # เขาไม่เห็นประวัติการคิดคำนวณของเขาอีกแล้ว
        see=self.assertIn("the result 3+5 is :8", result)
        self.assertEqual(see,None)
        time.sleep(2)

if __name__ == '__main__':
    unittest.main(warnings='ignore')