# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep
from selenium.common.exceptions import *

driver = webdriver.Chrome()
driver.maximize_window()
auth_link = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
contacts_link = 'https://fix-online.sbis.ru/page/dialogs'
user_login = 'arobelidze'
user_password = 'SMJ123'
recipient_name = 'Аробелидзе Жанна'
message_text = 'Автотест сообщение самому себе'

try:
    driver.get(auth_link)
    sleep(1)
    print('Авторизоваться на сайте https://fix-online.sbis.ru/')
    login = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    password.send_keys(user_password, Keys.ENTER)

    print('Перейти в реестр Контакты')
    sleep(2)
    driver.get(contacts_link)
    sleep(2)

    print('Отправить сообщение самому себе')
    driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]').click()
    sleep(2)
    assert driver.find_element(By.CSS_SELECTOR, '[class="controls-StackTemplate-content"]').is_displayed(), 'Меню выбора сотрудника не отображается'
    recipient = driver.find_element(By.CSS_SELECTOR, '[class="controls-StackTemplate-content"] [inputmode="text"]')
    recipient.send_keys(recipient_name)
    assert recipient.get_attribute('value') == recipient_name, 'Введен неверный поиск'
    sleep(2)
    recipient = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    assert recipient.get_attribute('title') == recipient_name, 'Неверное значение поиска'
    recipient.click()
    sleep(2)
    input_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    input_message.send_keys(message_text)
    assert input_message.text == message_text, 'Неверно набрано сообщение'
    driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]').click()
    sleep(2)

    print('Убедиться, что сообщение появилось в реестре')
    message = driver.find_element(By.XPATH, '//div[@data-qa="item"]//p[. = "{}"]'.format(message_text))
    assert message.is_displayed(), 'Сообщение не отображается в реестре'

    print('Удалить это сообщение и убедиться, что удалили')
    action_chains = ActionChains(driver)
    action_chains.context_click(message).perform()
    sleep(2)
    delete_btn = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    delete_btn.click()
    sleep(2)
    try:
        message_after_delete = driver.find_element(By.XPATH, '//div[@data-qa="item"]//p[. = "{}"]'.format(message_text))
    except NoSuchElementException:
        print("Сообщение успешно удалено")
    else:
        raise Exception('Сообщение не было удалено!')
finally:
    driver.quit()
