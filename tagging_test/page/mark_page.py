from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from mark_po.config.base_page import BasePage


class MarkPage(BasePage):

    def set_mark_rectangle(self, condition_val):
        """
        设置标注形状为矩形
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)

        self.steps("page/mark_page.yaml", "set_mark_rectangle")

    def set_mark_polygon(self, condition_val):
        """
        设置标注形状为多边形
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.steps("page/mark_page.yaml", "set_mark_polygon")

    def set_mark_parallelogram(self, condition_val):
        """
        设置标注形状为平行四边形
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)

        self.steps("page/mark_page.yaml", "set_mark_parallelogram")

    def set_mark_ordered_parallelogram(self):
        """
        设置标注形状为有序平行四边形
        :return:
        """
        self.steps("page/mark_page.yaml", "set_mark_ordered_parallelogram")

    def mark_rectangle(self, position):
        """
        画一个预定义的矩形
        :return:
        """
        self._params["start_position"] = str(position['start_position'])
        self._params["end_position"] = str(position['end_position'])
        self.steps("page/mark_page.yaml", "mark_rectangle")

    def mark_polygon(self, position):
        """
        画一个预定义的多边形
        :return:
        """
        self._params["position1"] = str(position['position1'])
        self._params["position2"] = str(position['position2'])
        self._params["position3"] = str(position['position3'])
        self._params["position4"] = str(position['position4'])
        self._params["position5"] = str(position['position5'])
        self.steps("page/mark_page.yaml", "mark_polygon")

    def mark_parallelogram(self, position):
        """
        画一个预定义的平行四边形
        :return:
        """
        self._params["position1"] = str(position['position1'])
        self._params["position2"] = str(position['position2'])
        self._params["position3"] = str(position['position3'])
        self.steps("page/mark_page.yaml", "mark_parallelogram")

    def mark_ordered_parallelogram(self, position):
        """
        画一个预定义的有序平行四边形
        :return:
        """
        self._params["position1"] = str(position['position1'])
        self._params["position2"] = str(position['position2'])
        self._params["position3"] = str(position['position3'])
        self.steps("page/mark_page.yaml", "mark_ordered_parallelogram")

    def select_predefined(self):
        """
        新增一个框后，选择标签为预定义标签
        :return:
        """
        self.steps("page/mark_page.yaml", "select_predefined")

    def select_customize(self):
        """
        新增一个框后，选择标签为实时标签
        :return:
        """
        self.steps("page/mark_page.yaml", "select_customize")

    def select_predefined_val(self):
        """
        选择预定义标签属性
        :return:
        """
        pass

    def add_customize_val(self, add_value):
        """
        添加实时标签的值
        :return:
        """
        self._params["add_customize_val"] = str(add_value['add_value'])
        self.steps("page/mark_page.yaml", "add_customize_val")

    def select_ignore(self):
        """
        选择副属性选择忽略
        :return:
        """
        self.steps("page/mark_page.yaml", "select_ignore")

    def select_crowd(self):
        """
        选择副属性密集
        :return:
        """
        self.steps("page/mark_page.yaml", "select_crowd")

    def click_cancel(self):
        """
        新增框或修改框时点击取消
        :return:
        """
        self.steps("page/mark_page.yaml", "click_cancel")

    def click_submit(self, img_name):
        """
        新增框或修改框时点击确定
        :return:
        """
        self.steps("page/mark_page.yaml", "click_submit")
        self.driver.save_screenshot(f'result/{img_name}.png')

    def double_click(self, double_click):
        """
        双击
        :return:
        """
        self._params["double_click"] = double_click
        self.steps("page/mark_page.yaml", "double_click")

    def update_object_id(self, update_value):
        """
        修改框的对象ID
        :return:
        """
        self._params["update_object_id_val"] = str(update_value["updata_value"])
        self.steps("page/mark_page.yaml", "update_object_id")

    def update_mark_position(self, position):
        """
        修改框的位置
        :return:
        """
        self._params["start_position"] = str(position['start_position'])
        self._params["end_position"] = str(position['end_position'])
        self.steps("page/mark_page.yaml", "mark_rectangle")

    def click_all_cancel(self):
        """
        全部取消
        :return:
        """
        self.steps("page/mark_page.yaml", "click_all_cancel")

    def click_all_submit(self):
        """
        点击全部保存
        :return:
        """
        self.steps("page/mark_page.yaml", "click_all_submit")
        self.driver.save_screenshot('result/shortcut_key.png')

    def set_show_predefined_mark(self):
        """
        设置显示预定义标签的框
        :return:
        """
        self.steps("page/mark_page.yaml", "set_show_predefined_mark")

    def set_show_customize_mark(self, condition_val):
        """
        设置显示实时标签的框
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)

        self.steps("page/mark_page.yaml", "set_show_customize_mark")

    def click_add_btn(self, condition_val):
        """
        点击新增按钮Q
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)

        self.steps("page/mark_page.yaml", "click_add_btn")

    def select_del_mark(self, position, condition_val):
        """
        选择需要删除的框
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)

        self._params["start_position"] = str(position['start_position'])
        self.steps("page/mark_page.yaml", "select_del_mark")

    def click_del_btn(self, condition_val):
        """
        点击删除按钮
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)

        self.steps("page/mark_page.yaml", "click_del_btn")

    def click_previous_img_btn(self):
        """
        点击上一张
        :return:
        """
        self.wait_for_click((By.XPATH, "//*[@class='quick-btn-list']//button[3]"))
        self.steps("page/mark_page.yaml", "click_previous_img_btn")

    def click_next_img_btn(self):
        """
        点击下一张
        :return:
        """
        self.steps("page/mark_page.yaml", "click_next_img_btn")

    def click_hide_btn(self):
        """
        点击下一张
        :return:
        """
        self.wait_for_click((By.XPATH, "//*[@class='quick-btn-list']//button[5]"))
        self.steps("page/mark_page.yaml", "click_hide_btn")

    def click_reset_img_btn(self):
        """
        点击重置
        :return:
        """
        self.steps("page/mark_page.yaml", "click_reset_img_btn")

    def click_not_mark_btn(self):
        """
        在图片标注页，点击无法标注按钮
        :return:
        """
        self.wait_for_click((By.XPATH, "//*[@class='quick-btn-list']//button[7]"))
        self.steps("page/mark_page.yaml", "click_not_mark_btn")

    def moved_right(self):
        """
        鼠标移动至右侧，调出标注索引页
        :return:
        """
        self.steps("page/mark_page.yaml", "moved_right")

    def click_enter_not_mark_pic(self):
        """
        点击进入没有标注的图片
        :return:
        """
        self.steps("page/mark_page.yaml", "click_enter_not_mark_pic")

    def click_previous_page(self):
        """
        点击上一页
        :return:
        """
        self.steps("page/mark_page.yaml", "click_previous_page")

    def click_next_page(self):
        """
        点击下一页
        :return:
        """
        self.steps("page/mark_page.yaml", "click_next_page")

    def click_object_id(self):
        """
        点击对象ID，需要传入对象ID的xpath
        :return:
        """
        self.steps("page/mark_page.yaml", "click_object_id")

    def click_attribute(self):
        """
        点击属性，需要传入属性的Xpath
        :return:
        """
        self.steps("page/mark_page.yaml", "click_attribute")

    def click_play(self, condition_val):
        """
        点击播放
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.steps("page/mark_page.yaml", "click_play")

    def click_begin_or_end(self):
        """
        点击开始或结束标记
        :return:
        """
        self.steps("page/mark_page.yaml", "click_begin_or_end")

    def click_previous_video(self, condition_val):
        """
        点击上一个视频
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.steps("page/mark_page.yaml", "click_previous_video")

    def click_next_video(self):
        """
        点击下一个视频
        :return:
        """
        self.steps("page/mark_page.yaml", "click_next_video")

    def click_return(self):
        """
        点击快退
        :return:
        """
        self.steps("page/mark_page.yaml", "click_return")

    def click_forward(self):
        """
        点击快进
        :return: 
        """
        self.steps("page/mark_page.yaml", "click_forward")

    def click_not_mark_btn_video(self):
        """
        在视频标注页，点击无法标注按钮
        :return:
        """
        self.wait_for_click((By.XPATH, '//*[@class="quick-btn-list"]/button[7]'))
        self.steps("page/mark_page.yaml", "click_not_mark_btn_video")

    def update_video_label(self, condition_val):
        """
        更新视频的标签
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_update_video_label")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_update_video_label")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.steps("page/mark_page.yaml", "update_video_label")

    def click_del_label(self, condition_val):
        """
        点击删除标注结果
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.set_implicitly_wait(3)
        self.steps("page/mark_page.yaml", "click_del_label")

    def click_del_label_submit(self, condition_val):
        """
        点击删除标注结果确认按钮
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.steps("page/mark_page.yaml", "click_del_label_submit")
        self.driver.save_screenshot('result/task_video.png')

    def click_add_step_len(self):
        """
        点击新增步长
        :return:
        """
        self.steps("page/mark_page.yaml", "click_add_step_len")
