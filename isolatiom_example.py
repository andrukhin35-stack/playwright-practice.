# ФИО Андрей Андрюхин Иванович
# Дата: 2026-11-13
# время 22:51
# изоляция контекстов браузера
# Источник: https://playwright.dev/python/docs/browser-contexts
# запускает chromium и запускает два независимых контекста браузера
# каждый контекст имеет отдельные cookies и данные сайтов

from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()


    user_context = browser.new_context()
    admin_context = browser.new_context()

with sync_playwright() as playwright:
    run(playwright)
    # резульат запуска:
    # команда: python isolatiom-example.py
    # скрипт завершился без ошибок, код завершения -0
    