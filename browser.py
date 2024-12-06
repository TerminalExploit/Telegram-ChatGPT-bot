import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ChatGPTBrowser:
    def __init__(self, driver_path, chatgpt_url, proxy=None):
        """Подключаемся к браузеру с remote-debugging и дополнительными настройками для обхода капчи."""
        
        chrome_options = Options()
        chrome_options.debugger_address = "127.0.0.1:9222"  # Порт для подключения к открытому браузеру
        chrome_options.add_argument("--incognito")  # Инкогнито режим
        chrome_options.add_argument("--disable-extensions")  # Отключение расширений
        chrome_options.add_argument("--headless")  # Без графического интерфейса
        chrome_options.add_argument("--disable-gpu")  # Отключение GPU для предотвращения ошибок
        chrome_options.add_argument("--no-sandbox")  # Для Linux-систем, если не работает

        if proxy:
            chrome_options.add_argument(f'--proxy-server={proxy}')  # Прокси-сервер, если задан

        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get(chatgpt_url)
        
        print("Подключились к открытому окну Chrome.")
        print("Войдите в свою учетную запись ChatGPT и нажмите Enter в консоли.")
        input("Нажмите Enter после входа...")

    def send_message(self, message):
        """Отправляем сообщение в ChatGPT и получаем ответ."""
        try:
            input_box = self.driver.find_element(By.TAG_NAME, "textarea")
            input_box.send_keys(message)
            input_box.send_keys(Keys.ENTER)

            # Ждем появления ответа
            time.sleep(5)

            # Получаем последний ответ
            responses = self.driver.find_elements(By.CLASS_NAME, "text-base")
            return responses[-1].text if responses else "Ответ не найден."
        except Exception as e:
            return f"Ошибка при работе с браузером: {e}"

    def close(self):
        """Закрываем браузер."""
        self.driver.quit()