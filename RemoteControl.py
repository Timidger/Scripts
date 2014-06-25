from selenium import selenium
import unittest, time, re

class RemoteControl(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://27715netclass.blackbaudondemand.com/")
        self.selenium.start()
    
    def test_remote_control(self):
        sel = self.selenium
        sel.open("/NetClassroom7/Forms/login.aspx?ReturnUrl=%2fNetClassroom7%2fdefault.aspx")
        sel.type("id=sid", "prestonc")
        sel.type("id=pin", "Harrison12")
        sel.click("id=btnLogin")
        sel.wait_for_page_to_load("30000")
        sel.click("id=mnuPerformanceIdsubMenuItem2")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
