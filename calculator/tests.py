from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import resolve

from calculator import views
from calculator.models import Calculate

from calculator.views import home
class test_open_webpage(TestCase):
    #ทดสอบว่าเข้าหน้าหลักได้หรือไม่
    def test_start_page(self):
        start = resolve('/')
        self.assertEqual(start.func,home)
class Unittest(TestCase):
    #เช็คว่าใช้ templates ถูกต้องหรือไม่
    def test_used_home_template(self):
        respone = self.client.get('/')
        self.assertTemplateUsed(respone,'calculator/home.html')
    #เช็คว่าข้อมุลประวัติการใช้งานในตอนเริ่มใช้มีหรือไม่
    def test_check_history_when_start(self):
        self.client.get('/')
        self.assertEqual(Calculate.objects.count(),0)
    #ทดสอบฟังค์ชันคิดคำนวณ + - * / ใน views
    def test_function_calculate(self):
        result_plus = views.calculating(10,20,"+")
        self.assertEqual(10+20,result_plus)
        result_minus = views.calculating(30,10,'-')
        self.assertEqual(30-10,result_minus)
        result_multiple=views.calculating(45,3,'*')
        self.assertEqual(45*3,result_multiple)
        result_divide=views.calculating(10,5,'/')
        self.assertEqual(10/5,result_divide)
    #ทำการทดสอบว่าคำนวณได้หรือไม่ และโชว์ว่ามีผลลัพธ์หรือไม่
    def test_user_can_calculate_and_show_result_in_history(self):
        request = self.client.post('/',{'x':1,'y':2,'operate_list':['+'],'find value':'1'})
        respone = request.content.decode('utf8')
        self.assertIn('the result 1 + 2 is :3',str(respone))
        self.client.get('/')
        self.assertEqual(Calculate.objects.count(), 1)
    #คำนวณได้หลายค่าพร้อมกันและโชว์ในประวัติการใช้งาน
    def test_user_can_calculate_and_show_result_in_history_mutiple_thing(self):
        request = self.client.post('/', {'x': 10, 'y': 20, 'operate_list': ['+','-','*','/'], 'find value': '1'})
        respone = request.content.decode('utf8')
        self.assertIn('the result 10 + 20 is :30', str(respone))
        self.assertIn('the result 10 - 20 is :-10', str(respone))
        self.assertIn('the result 10 * 20 is :200', str(respone))
        self.assertIn('the result 10 / 20 is :0.5', str(respone))
        self.client.get('/')
        self.assertEqual(Calculate.objects.count(),4)
    #ทดสอบปุ่ม clear history
    def test_user_delete_all_history(self):
        request = self.client.post('/', {'x': 10, 'y': 20, 'operate_list': ['+', '-', '*', '/'], 'find value': '1'})
        respone = request.content.decode('utf8')
        self.assertIn('the result 10 + 20 is :30', str(respone))
        self.assertIn('the result 10 - 20 is :-10', str(respone))
        self.assertIn('the result 10 * 20 is :200', str(respone))
        self.assertIn('the result 10 / 20 is :0.5', str(respone))
        self.client.get('/')
        self.assertEqual(Calculate.objects.count(), 4)
        self.client.post('/',{"clear_history":'1'})
        self.assertEqual(Calculate.objects.count(), 0)

