"""
@Project : cd-auto-test-client.git
@File    : drivers.py
@IDE     : PyCharm
@Author  : geek mister
@Date    : 2024/1/5 13:53
@MyHome  : https://github.com/geekmister
@Desc    : driver manager, you can use this module do
            1. init driver manager;
            2. quit driver;
            3. instance all kinds of options.
"""


from selenium import webdriver


from utils.logger import logger


class DriverManager:
    """
    Browser driver manager...
    """

    # webdriver, what's private variable
    __webdriver = None

    def __init__(self, options=None, url=""):
        """

        Args:
            options(Options | None): driver options, contains ChromeOptions, FirefoxOptions, SafariOptions, IEOptions,
                EdgeOptions, that's no normal value is required.
            url(str): visit address, that's no normal value is required.
        """

        browser_name = options.capabilities["browserName"]
        logger.info("ready to init driver of browser name is %s", browser_name)

        if browser_name == "chrome":
            self.__webdriver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            self.__webdriver = webdriver.Firefox(options=options)
        elif browser_name == "ie":
            self.__webdriver = webdriver.Ie(options=options)
        elif browser_name == "safari":
            self.__webdriver = webdriver.Safari(options=options)
        elif browser_name == "edge":
            self.__webdriver = webdriver.Edge(options=options)
        else:
            logger.error("no match browser name")

    def quit(self):
        """
        quit driver
        Returns:
            None
        """

        self.__webdriver.quit()


class ChromeOptions(webdriver.ChromeOptions):
    """
    Overwriting ChromeOptions, the goal is extension to match self requirements
    """

    def __init__(self):
        webdriver.ChromeOptions.__init__(self=self)
        pass


class SafariOptions(webdriver.SafariOptions):
    """
    Overwriting SafariOptions, the goal is extension to match self requirements
    """

    def __init__(self):
        webdriver.SafariOptions.__init__(self=self)
        pass


class IEOptions(webdriver.IeOptions):
    """
    Overwriting IeOptions, the goal is extension to match self requirements
    """

    def __init__(self):
        webdriver.IeOptions.__init__(self=self)
        pass


class FirefoxOptions(webdriver.FirefoxOptions):
    """
    Overwriting FirefoxOptions, the goal is extension to match self requirements
    """

    def __init__(self):
        webdriver.FirefoxOptions.__init__(self=self)
        pass


class EdgeOptions(webdriver.EdgeOptions):
    """
    Overwriting EdgeOptions, the goal is extension to match self requirements
    """

    def __init__(self):
        webdriver.EdgeOptions.__init__(self=self)
        pass


if __name__ == "__main__":
    # the under code are test code
    driver_manager = DriverManager(ChromeOptions(), "https://www.baidu.com")

