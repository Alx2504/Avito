from Task_2.base.base_class import Base
import os

def test_check(driver):
    base = Base(driver)

    driver.get("https://www.avito.ru/avito-care/eco-impact")

    current_dir = base.get_current_dir()

    base.scroll_to_elem('//h2[@class="desktop-item-title-LkZqW"]')
    base.get_screenshot_by_elem('//div[@class="desktop-impact-items-F7T6E"]', current_dir)
