from behave_webdriver.steps import *  # ignore
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import the Select class
import time

@given('I open the url "{url}"')
def step_go_to_url(context, url):
    context.behave_driver.get(url)
    time.sleep(2)

@when('I click on the "{selector}" and switch the value to "{value}"')
def step_click_on_select_and_enter_value(context, selector, value):
    s= context.behave_driver.find_element(By.ID, selector)
    select = Select(s)
    select.select_by_value(value)

@when('I click on the "{textId}" and enter "{value}"')
def step_to_enter_text_into_text_box(context, textId, value):
    text_area = context.behave_driver.find_element(By.ID, textId)
    text_area.clear()
    text_area.send_keys(value)

@when('I click "{btnId}" button')
def step_to_click_btn(context, btnId):
    btn = context.behave_driver.find_element(By.ID, btnId)
    btn.click()
    time.sleep(3)
@then('I should see "{value}" in the "{div}"')
def step_to_verify(context, value, div):
    div_container = context.behave_driver.find_element(By.ID, div)
    p = div_container.find_element(By.TAG_NAME, "p")
    assert p.text == value, f"Expected '{value}', but got '{p.text}'"






