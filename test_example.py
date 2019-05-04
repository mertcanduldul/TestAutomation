from webdriver import *
import time

class TestAmazonExample(WebDriverBase):
    HOME_CATEGORY_LOCATOR = (By.CSS_SELECTOR, "#desktop-top .as-title-block-left")
    SEARCH_BOX_LOCATOR = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON_LOCATOR = (By.CLASS_NAME, "nav-search-submit")
    PRODUCTS_NAME_LOCATOR=(By.CSS_SELECTOR,"img[data-image-index='2']")
    ADD_PRODUCT=(By.ID,"add-to-cart-button")
    ADD_WISHLIST=(By.ID,"add-to-wishlist-button-submit")
    USERNAME=(By.ID,"ap_email")
    PASSWORD=(By.ID,"ap_password")
    LOGINBUTTON=(By.ID,"signInSubmit")
    VIEWLIST=(By.CSS_SELECTOR,"a[id='WLHUC_viewlist']")
    DELETE_ITEM=(By.CSS_SELECTOR,"input[aria-labelledby='a-autoid-7-announce']")

        
    def __init__(self):
        super().__init__()
        self.init_driver()
        self.driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&switch_account=")
        self.login("USERNAME","PASSWORD")
        self.test_category()
        self.test_search_product("samsung")
        self.product_click()
        self.addwish_click()
        self.view_wishlist_click()
        self.delete_item()
        self.driver.quit()
        
    def login(self,username,password):
        x=self.get_element(self.USERNAME)
        x.send_keys(username)
        y=self.get_element(self.PASSWORD)
        y.send_keys(password)
        self.get_element(self.LOGINBUTTON).click()


    def test_search_product(self, product_name):
        search_box = self.get_element(self.SEARCH_BOX_LOCATOR)
        search_box.send_keys(product_name)
        self.get_element(self.SEARCH_BUTTON_LOCATOR).click()

    def product_click(self):
        self.get_element(self.PRODUCTS_NAME_LOCATOR).click()

    def addwish_click(self):
        self.get_element(self.ADD_WISHLIST).click()
        time.sleep(5)
    
    def view_wishlist_click(self):
        self.get_element(self.VIEWLIST).click()

    def delete_item(self):
        self.get_element(self.DELETE_ITEM).click()
        time.sleep(100)
        
    def test_category(self):
        first_category = self.get_element(self.HOME_CATEGORY_LOCATOR)
        #assert first_category.text == "Amazon'u keşfet"

if __name__ == "__main__":
    TestAmazonExample()