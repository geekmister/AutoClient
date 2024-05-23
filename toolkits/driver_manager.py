"""
@Author  : Geekmister
@Date    : 2024/05/23 16:25
@MyHome  : https://github.com/geekmister
@Desc    : 
    Webdriver manager, it's a tool to manage webdriver.
"""


from selenium import webdriver

from utils.logger import logger


def get_webdriver(options=None):
    """
    Desc:
        Get webdriver instance.
    Args:
        options(Any | None): Webdriver options.
    Return:
        Webdriver(Webdriver | None): Webdriver instance.
    """

    browser_name = options.capabilities["browserName"]
    logger.info("ready to init driver of browser name is %s", browser_name)

    if browser_name == "chrome":
        return webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        return webdriver.Firefox(options=options)
    elif browser_name == "ie":
        return webdriver.Ie(options=options)
    elif browser_name == "safari":
        return webdriver.Safari(options=options)
    elif browser_name == "edge":
        return webdriver.Edge(options=options)
    else:
        logger.error("no match browser name")
        return None
        

def webdriver_close(webdriver):
    """
    Desc:
        Webdriver close.
    Args:
        webdriver(Webdriver): Webdriver instance.
    Return:
        None
    """

    webdriver.close()
    logger.info("Webdriver closed!")


def webdriver_quit(webdriver):
    """
    Desc:
        Webdriver quit.
    Args:
        webdriver(Webdriver): Webdriver instance.
    Return:
        None
    """

    webdriver.quit()
    logger.info("Webdriver quited!")


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