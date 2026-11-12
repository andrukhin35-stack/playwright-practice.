# ФИО Андрей Андрюхин Иванович
# Дата : 12-11-2026
# Время запуска: 17:04
# Тема: запуск браузера через библеотеку playwright
# Источник  https://playwright.dev/python/docs/library
# описание : запускает playwright и браузер Chromium
# запускает страницу, открывает playwright.dev
# выводит загаловок страницы в терминал и закрывает браузер

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    browser.close()