"""
@Project : cd-auto-test-client.git
@File    : actions.py
@IDE     : PyCharm
@Author  : geek mister
@Date    : 2024/1/9 14:19
@MyHome  : https://github.com/geekmister
@Desc    : Development based on selenium actions mouse interface.
            1. Document link: https://www.selenium.dev/zh-cn/documentation/webdriver/actions_api/mouse/
            2. Alternate Button Clicks, There are a total of 5 defined buttons for a Mouse:
                0 — Left Button (the default)
                1 — Middle Button (currently unsupported)
                2 — Right Button
                3 — X1 (Back) Button
                4 — X2 (Forward) Button
"""


from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


class MouseAction:
    """
    Actions about mouse...
    """

    @staticmethod
    def press_left_and_hold(self, element, driver):
        """
        This method combines moving the mouse to the center of an element with pressing the left mouse button.
        This is useful for focusing a specific element.
        Args:
            self(MouseAction): instance
            element(WebElement): acting element
            driver(WebDriver): web driver

        Returns:
            None

        """

        ActionChains(driver).click_and_hold(on_element=element).perform()

    @staticmethod
    def click_left(self, element, driver):
        """
        This method combines moving to the center of an element with pressing and releasing the left mouse button.
        This is otherwise known as “clicking”
        Args:
            self(MouseAction): instance
            element(WebElement): acting element
            driver(WebDriver): web driver

        Returns:
            None
        """

        ActionChains(driver=driver).click(on_element=element).perform()

    @staticmethod
    def click_left_double(self, element, driver):
        """
        This method combines moving to the center of an element with pressing and releasing the left mouse button twice.
        Args:
            self(MouseAction): instance
            element(WebElement): acting element
            driver(WebDriver): web driver

        Returns:
            None
        """

        ActionChains(driver=driver).double_click(on_element=element).perform()

    @staticmethod
    def click_right(self, element, driver):
        """
        This method combines moving to the center of an element with pressing and releasing the right mouse button (button 2).
        This is otherwise known as “right-clicking”
        Args:
            self(MouseAction): instance
            element(WebElement): acting element
            driver(WebDriver): web driver

        Returns:
            None
        """

        ActionChains(driver=driver).click(on_element=element).perform()

    @staticmethod
    def click_back(self, driver):
        """
        There is no convenience method for this, it is just pressing and releasing mouse button 3
        Args:
            self(MouseAction): instance
            driver(WebDriver): web driver

        Returns:
            None
        """

        action = ActionBuilder(driver=driver)
        action.pointer_action.pointer_down(MouseButton.BACK)
        action.pointer_action.pointer_up(MouseButton.BACK)
        action.perform()

    @staticmethod
    def click_forward(self, driver):
        """
        There is no convenience method for this, it is just pressing and releasing mouse button 4
        Args:
            self(MouseAction): instance
            driver(WebDriver): web driver

        Returns:
            None
        """

        action = ActionBuilder(driver=driver)
        action.pointer_action.pointer_down(MouseButton.FORWARD)
        action.pointer_action.pointer_up(MouseButton.FORWARD)
        action.perform()

    @staticmethod
    def move_to_element(self, element, driver):
        """
        This method moves the mouse to the in-view center point of the element. This is otherwise known as “hovering.”
        Note that the element must be in the viewport or else the command will error
        Args:
            self(MouseAction): instance
            element(WebElement): acting element
            driver(WebDriver): web driver

        Returns:
            None
        """

        ActionChains(driver=driver).move_to_element(to_element=element).perform()

    @staticmethod
    def move_to_element_offset(self, element, driver, x_offset, y_offset):
        """
        This method moves the mouse to the in-view center point of the element, then moves by the provided offset.
        Args:
            self(MouseAction): instance
            element(WebElement): acting element
            driver(WebDriver): web driver
            x_offset(int): offset y
            y_offset(int): offset x

        Returns:
            None
        """

        ActionChains(driver=driver) \
            .move_to_element_with_offset(to_element=element, xoffset=x_offset, yoffset=y_offset).perform()

    @staticmethod
    def move_to_viewport_origin_offset(self, driver, x_offset, y_offset):
        """
        This method moves the mouse from the upper left corner of the current viewport by the provided offset.
        Args:
            self(MouseAction): instance
            driver(WebDriver): web driver
            x_offset(int): offset y
            y_offset(int): offset x

        Returns:
            None
        """

        action = ActionBuilder(driver)
        action.pointer_action.move_to_location(x=x_offset, y=y_offset)
        action.perform()

    @staticmethod
    def move_to_viewport_current_offset(self, driver, x_offset, y_offset):
        """
        This method moves the mouse from its current position by the offset provided by the user.
        If the mouse has not previously been moved, the position will be in the upper left corner of the viewport.
        Note that the pointer position does not change when the page is scrolled.
        Note that the first argument X specifies to move right when positive, while the second argument Y specifies to move down when positive.
        So moveByOffset(30, -10) moves right 30 and up 10 from the current mouse position.
        Args:
            self(MouseAction): instance
            driver(WebDriver): web driver
            x_offset(int): offset y
            y_offset(int): offset x

        Returns:
            None
        """

        ActionChains(driver=driver).move_by_offset(xoffset=x_offset, yoffset=y_offset).perform()

    @staticmethod
    def drag_drop_element(self, from_element, to_element, driver):
        """
        This method firstly performs a click-and-hold on the source element,
        moves to the location of the target element and then releases the mouse.
        Args:
            self(MouseAction): instance
            from_element(WebElement): acting from element
            to_element(WebElement): acting to element
            driver(WebDriver): web driver

        Returns:
            None
        """

        ActionChains(driver).drag_and_drop(from_element, to_element).perform()

    @staticmethod
    def drag_drop_element_by_offset(self, element, driver, x_start, y_start, x_end, y_end):
        """
        This method firstly performs a click-and-hold on the source element,
        moves to the given offset and then releases the mouse.
        Args:
            self(MouseAction): instance
            element(WebElement): acting element
            x_start(int): start point x
            y_start(int): start point y
            x_end(int): end point x
            y_end(int): end point y
            driver(WebDriver): web driver

        Returns:
            None
        """

        ActionChains(driver).drag_and_drop_by_offset(element, x_end - x_start, y_end - y_start).perform()


class Element:
    """
    Actions about element
    """

    @staticmethod
    def find_element(self, way, value):
        match way:
            case "class_name":
                pass
            case _:
                pass
        pass


