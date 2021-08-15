import json
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ruamel import yaml


class BasePage:
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator=None):
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def finds(self, by, locator=None):
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def set_implicitly_wait(self, second):
        self.driver.implicitly_wait(second)

    def wait_for_click(self, locator):
        # 显示等待
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_condition(self, condition):
        # 满足 condition 的显示等待
        WebDriverWait(self.driver, 10).until(condition)

    def update_init_date(self, yaml_path):
        t = time.time()
        time_update = int(round(t * 1000))
        with open(yaml_path, encoding="utf-8") as f:
            result = yaml.safe_load(f)
            time_old = result['init_time']['test_time']
            result = str(result)
            data = result.replace(str(time_old), str(time_update))
            update_val = eval(data)
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(update_val, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)

    def steps(self, path, name):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace('${' + key + '}', value)
        steps = json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "send_keys" == action:
                    img_path = eval(step["img_path"])
                    for i in img_path:
                        self.find(step["by"], step["locator"]).send_keys(i)
                if "double_click" == action:
                    double_click = self.find(step["by"], step["locator"])
                    ActionChains(self.driver).double_click(double_click).perform()
                if "control_a" == action:
                    self.find(step["by"], step["locator"]).send_keys(Keys.CONTROL, 'a')
                if "select_del_mark" == action:
                    canvas = self.find(step["by"], step["locator"])
                    start_position = eval(step['start_position'])
                    ActionChains(self.driver).move_to_element_with_offset(canvas, start_position[0],
                                                                          start_position[1]).click().perform()
                if "moved_right" == action:
                    canvas = self.find(step["by"], step["locator"])
                    position = step['position']
                    ActionChains(self.driver).move_to_element_with_offset(canvas, position[0],
                                                                          position[1]).perform()
                if "chains_rectangle" == action:
                    canvas = self.find(step["by"], step["locator"])
                    start_position = eval(step['start_position'])
                    end_position = eval(step['end_position'])
                    ActionChains(self.driver).move_to_element_with_offset(canvas, start_position[0],
                                                                          start_position[1]).click_and_hold(
                        on_element=None).move_by_offset(end_position[0], end_position[1]).release(
                        on_element=None).perform()
                if "chains_polygon" == action:
                    canvas = self.find(step["by"], step["locator"])
                    position1 = eval(step['position1'])
                    position2 = eval(step['position2'])
                    position3 = eval(step['position3'])
                    position4 = eval(step['position4'])
                    position5 = eval(step['position5'])
                    ActionChains(self.driver).move_to_element_with_offset(canvas, position1[0],
                                                                          position1[1]).click().move_by_offset(
                        position2[0], position2[1]).click().move_by_offset(position3[0],
                                                                           position3[1]).click().move_by_offset(
                        position4[0], position4[1]).click().move_by_offset(position5[0], position5[1]).click().perform()
                if "chains_parallelogram" == action:
                    canvas = self.find(step["by"], step["locator"])
                    position1 = eval(step['position1'])
                    position2 = eval(step['position2'])
                    position3 = eval(step['position3'])
                    ActionChains(self.driver).move_to_element_with_offset(canvas, position1[0],
                                                                          position1[1]).click().move_by_offset(
                        position2[0], position2[1]).click().move_by_offset(position3[0], position3[1]).click().perform()
                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0

    def back(self):
        self.driver.back()
