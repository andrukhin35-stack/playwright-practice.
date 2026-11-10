# ФИО: Андрюхин Андрей Иванович
# Дата: 2026-11-10
# Время: 17:27
# Тема: сохранение скриншота страницы.
# Источник: https://playwright.dev/python/docs/screenshots
# описание: открываю сайт Playwright и сохраняю два изображения:
# видимую область страницы и страницу целиком.
# изменение: добавил второй вызов screenshot с full_page=True
# и отдельным именем файла screenshot_full.png.
# зачем: чтобы сохранить содержимое ниже видимой области
# и сравнить обычный скриншот с полным.

from playwright.sync_api import Page


def test_homepage_screenshot(page: Page):
    # открывает главную страницу сайта.
    page.goto("https://playwright.dev/")

    # сохраняет только видимую область.
    page.screenshot(path="screenshot.png")
    # сохраняет всю страницу, включая область ниже экрана.
    page.screenshot(path="screenshot_full.png", full_page=True)
    #