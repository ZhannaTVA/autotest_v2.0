# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

try:
    driver.get(sbis_site)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Проверить отображение четырех вкладок')
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-link--hover')
    assert len(tabs) == 4, 'Неверное кол-во вкладок'

    print('Проверить текст и видимость кнопки Контакты')
    button_txt = 'Контакты'
    contacts_btn = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    assert contacts_btn.text == button_txt, 'Неверный текст кнопки'
    assert contacts_btn.is_displayed(), 'Кнопка не отображается'

    print('Перейти на страницу Контакты')
    contacts_btn.click()

    print('Проверить адрес страницы')
    assert 'https://sbis.ru/contacts' in driver.current_url

    print('Проверить атрибут и видимость баннера Тензор')
    banner_title = 'tensor.ru'
    banner_btn = driver.find_element(By.CSS_SELECTOR, '[href="https://tensor.ru/"]')
    assert banner_btn.get_attribute('title') == banner_title, 'Неверный тултип баннера'

    print('Клик по баннеру')
    banner_btn.click()
    driver.switch_to.window(driver.window_handles[1])

    print('Найти блок с новостью "Сила в людях" и линк')
    strength_block = driver.find_element(By.XPATH, '//p[. = "Сила в людях"]')

    print('Найти линк "Подробнее" и кликнуть')
    about_link = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text > a[href="/about"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", about_link)
    about_link.click()

    print('Проверить адрес сайта и заголовок страницы (https://tensor.ru/about)')
    about_site = 'https://tensor.ru/about'
    about_title = 'О компании | Тензор — IT-компания'
    assert driver.current_url == about_site, 'Неверный адрес сайта'
    assert driver.title == about_title, 'Неверный заголовок сайта'
finally:
    driver.quit()
