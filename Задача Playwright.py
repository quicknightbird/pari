#Условие: Написать тест, который открывает веб-страницу https://playwright.dev/, проверяет, что она существует, и что заголовок страницы соответствует ожидаемому значению.
#Ожидаемый результат: Тест, успешно проходящий проверку заголовка.

#При переходе на веб-страницу ожидаем заголовок Fast and reliable end-to-end testing for modern web apps | Playwright, так как <title>Fast and reliable end-to-end testing for modern web apps | Playwright</title>

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module") #Используем фикстуру для того, чтобы убрать дублирования
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        yield page
        browser.close()


def test_page_title_exists(page):
    page_title = page.title()
    assert page_title, "Title пустой"


def test_page_title_is_correct(page):
    expected_title = "Fast and reliable end-to-end testing for modern web apps | Playwright"
    page_title = page.title()
    assert page_title == expected_title, f"Ожидаемая '{expected_title}', но получаем '{page_title}'"
