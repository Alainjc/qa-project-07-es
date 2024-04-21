import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""
    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    flash_button = (By.XPATH, "//div[@class='mode active']")
    taxi_button = (By.CSS_SELECTOR, "div[class='type active disabled'] img[class='type-icon']")
    order_flash_taxi = (By.XPATH, "//button[normalize-space()='Pedir un taxi']")
    comfort_button = (By.CSS_SELECTOR, "div[class='tcard-icon'] img[alt='Comfort']")
    comfort_button_selected = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]")
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_number_field = (By.XPATH, '//*[@id="phone"]')
    next_button_set_number_window = (By.CSS_SELECTOR, "div[class='section active'] button[type='submit']")
    sms_code_field = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/form/div[1]/div[1]/input")
    confirm_button_set_code_window = (By.XPATH, "//button[normalize-space()='Confirmar']")
    np_button_filled = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[1]/div")
    payment_method_button = (By.CLASS_NAME, "pp-text")
    add_new_card_button = (By.CSS_SELECTOR, "div[class='pp-row disabled'] div[class='pp-title']")
    add_card_number_field = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/form/div[1]/div[1]/div[2]/input")
    add_card_code_field = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    add_card_button = (By.CSS_SELECTOR, "div[class='pp-buttons'] button[type='submit']")
    added_card_check = (By.CSS_SELECTOR, ".pp-button.filled")
    close_button_payment_method_window = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/button")
    add_comment_field = (By.ID, "comment")
    blankets_scarves_button = (By.XPATH, "(//span[@class='slider round'])[1]")
    blankets_scarves_checkbox = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input")
    ice_cream_add_button = (By.XPATH, "//div[@class='r-group']//div[1]//div[1]//div[2]//div[1]//div[3]")
    ice_cream_counter = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]")
    order_taxi_button = (By.CLASS_NAME, "smart-button-main")
    order_taxi_progress = (By.XPATH, "//*[@id='root']/div/div[5]/div[2]/div[1]/div/div[3]")
    driver_name = (By.XPATH, "//*[@id='root']/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field))
        self.set_from(from_address)
        self.set_to(to_address)

    def click_flash_button(self):
        self.driver.find_element(*self.flash_button).click()

    def click_taxi_button(self):
        self.driver.find_element(*self.taxi_button).click()

    def click_order_taxi_button(self):
        #self.driver.find_element(*self.order_flash_taxi).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.order_flash_taxi))
        self.driver.find_element(*self.order_flash_taxi).click()

    def click_comfort_taxi_button(self):
        self.driver.find_element(*self.comfort_button).click()

    def order_comfort_taxi(self):
        self.click_flash_button()
        self.click_taxi_button()

        self.click_order_taxi_button()
        self.click_comfort_taxi_button()

    def get_comfort_taxi(self):
        return self.driver.find_element(*self.comfort_button_selected).is_displayed()

    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    def click_next_button_phone_field(self):
        self.driver.find_element(*self.next_button_set_number_window).click()

    def set_sms_code(self):
        self.driver.find_element(*self.sms_code_field).send_keys(retrieve_phone_code(self.driver))

    def click_confirm_button_code_field(self):
        self.driver.find_element(*self.confirm_button_set_code_window).click()

    def set_user_phone_number(self, number):
        self.click_phone_number_button()
        phone_number_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.phone_number_field))
        phone_number_input.send_keys(number)
        self.click_next_button_phone_field()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.sms_code_field))
        self.set_sms_code()
        self.click_confirm_button_code_field()

    def get_filled_phone_number(self):
        return self.driver.find_element(*self.np_button_filled).text

    def click_payment_method_button(self):
        payment_button = self.driver.find_element(*self.payment_method_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", payment_button)
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_new_card_button).click()

    def set_card_number_and_code(self, card_number, code):
        self.click_payment_method_button()
        self.click_add_card_button()
        self.driver.find_element(*self.add_card_number_field).send_keys(card_number)
        self.driver.find_element(*self.add_card_code_field).send_keys(code)
        tab_code_field = self.driver.find_element(*self.add_card_code_field)
        tab_code_field.send_keys(Keys.TAB)
        self.driver.find_element(*self.add_card_button).click()

    def click_on_close_button(self):
        self.driver.find_element(*self.close_button_payment_method_window).click()

    def get_added_card_checkmark(self):
        return self.driver.find_element(*self.added_card_check).is_displayed()

    def add_comment_to_driver(self, comment):
        comment_field = self.driver.find_element(*self.add_comment_field)
        self.driver.execute_script("arguments[0].scrollIntoView();", comment_field)
        comment_field.send_keys(comment)

    def get_comment_to_driver(self):
        return self.driver.find_element(*self.add_comment_field).get_property('value')

    def click_on_add_scarves_blankets_button(self):
        add_scarves_blankets = self.driver.find_element(*self.blankets_scarves_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", add_scarves_blankets)
        self.driver.find_element(*self.blankets_scarves_button).click()

    def get_scarves_blankets_active_button(self):
        return self.driver.find_element(*self.blankets_scarves_checkbox).is_selected()

    def click_on_add_ice_cream_button(self):
        add_ice_cream = self.driver.find_element(*self.ice_cream_add_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", add_ice_cream)
        add_ice_cream.click()
        add_ice_cream.click()

    def get_ice_cream_counter_value(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    def click_on_order_taxi(self):
        self.driver.find_element(*self.order_taxi_button).click()

    def order_progress(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.order_taxi_progress))

    def get_driver_name_displayed(self):
        return WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(self.driver_name))


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_comfort_fee(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.order_comfort_taxi()
        comfort_taxi = routes_page.get_comfort_taxi()
        assert comfort_taxi, "Comfort taxi NO está seleccionado"

    def test_set_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        user_phone_number = data.phone_number
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.order_comfort_taxi()
        routes_page.set_user_phone_number(user_phone_number)
        phone_number_added = routes_page.get_filled_phone_number()
        assert phone_number_added == user_phone_number

    def test_add_credit_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.order_comfort_taxi()
        routes_page.set_card_number_and_code(data.card_number, data.card_code)
        routes_page.click_on_close_button()
        added_card = routes_page.get_added_card_checkmark()
        assert added_card

    def test_add_driver_comment(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        driver_comment = data.message_for_driver
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.order_comfort_taxi()
        routes_page.add_comment_to_driver(driver_comment)
        assert routes_page.get_comment_to_driver() == driver_comment

    def test_order_scarves_blankets(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.order_comfort_taxi()
        routes_page.click_on_add_scarves_blankets_button()
        active_button = routes_page.get_scarves_blankets_active_button()
        assert active_button, "El botón NO está seleccionado"

    def test_order_ice_cream(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.order_comfort_taxi()
        routes_page.click_on_add_ice_cream_button()
        ice_cream_counter = routes_page.get_ice_cream_counter_value()
        assert '2' in ice_cream_counter, "El número 2 NO está presente en el contador"

    def test_order_taxi_button(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.order_comfort_taxi()
        routes_page.set_user_phone_number(data.phone_number)
        routes_page.add_comment_to_driver(data.message_for_driver)
        routes_page.click_on_order_taxi()
        order_progress = routes_page.order_progress()
        assert order_progress, "El elemento NO esta disponible"

    def test_driver_info(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.order_comfort_taxi()
        routes_page.set_user_phone_number(data.phone_number)
        routes_page.add_comment_to_driver(data.message_for_driver)
        routes_page.click_on_order_taxi()
        driver_name = routes_page.get_driver_name_displayed()
        assert driver_name, "El elemento no está disponible"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()