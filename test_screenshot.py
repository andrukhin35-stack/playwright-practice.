# ФИО: Андрюхин Андрей Иванович
# Дата: 2026-11-10
# Время: 
# Тема: сохранение скриншота страницы.
# Источник: https://playwright.dev/python/docs/screenshots
# Описание: открываю главную страницу Playwright и сохраняю
# изображение её видимой области в файл screenshot.png.
# из документации взята строка page.screenshot().
# Для запуска через pytest добавлены импорт, функция и открытие сайта.

from playwright.sync_api import Page


def test_homepage_screenshot(page: Page):
    # Открываю сайт, который нужно сфотографировать.
    page.goto("https://playwright.dev/")

    # Сохраняю изображение видимой области страницы.
    page.screenshot(path="screenshot.png")