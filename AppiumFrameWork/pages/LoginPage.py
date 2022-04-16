from AppiumFrameWork.base.BasePage import BasePage
import AppiumFrameWork.utilities.CustomLogger as cl


class LoginPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _loginbutton ="com.code2lead.kwad:id/Login" # id
    _enterEmail ="3" # index
    _enterPassword ="Enter Password" # text
    _clickloginButton ="com.code2lead.kwad:id/Btn3" # id
    _wrongCredentials = "Wrong Credentials" # text
    _pageTitle ="Enter Admin" # text
    _enterText ="com.code2lead.kwad:id/Edt_admin" # id
    _submitButton ="SUBMIT" # text


    def clickLoginBotton(self):
        self.clickElement(self._loginbutton,"id")


    def enterEmail(self):
        self.sendText("admin@gmail.com",self._enterEmail,"index")


    def enterPassword(self):
        self.sendText("admin123",self._enterPassword,"text")


    def enterPassword2(self):
        self.sendText("admin1234",self._enterPassword,"text")


    def clickOnLoginB(self):
        self.clickElement(self._clickloginButton,"id")


    def verifyAdminScreen(self):
        adminScreen = self.isDisplayed(self._pageTitle,"text")
        assert adminScreen == True


    def enterText(self):
        self.sendText("Code2Lead",self._enterText,"id")


    def clickOnSubmit(self):
        self.clickElement(self._submitButton,"text")

