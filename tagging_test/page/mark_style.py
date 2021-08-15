from selenium.webdriver.common.by import By

from mark_po.config.base_page import BasePage


class MarkStyle(BasePage):

    def click_add_template(self, condition_val):
        """
        新增模板
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.steps("page/mark_style.yaml", "click_add_template")

    def input_template_name(self, input_template_name):
        """
        输入模板名称
        :return:
        """
        self._params['template_name'] = input_template_name['template_name']
        self.steps("page/mark_style.yaml", "click_template_name")
        self.steps("page/mark_style.yaml", "control_a_template_name")
        self.steps("page/mark_style.yaml", "input_template_name")

    def select_mark_shape_rectangle(self):
        """
        选择标注形状为矩形
        :return:
        """
        self.steps("page/mark_style.yaml", "select_mark_shape_rectangle")

    def select_mark_shape_polygon(self):
        """
        选择标注形状为多边形
        :return:
        """
        self.steps("page/mark_style.yaml", "select_mark_shape_polygon")

    def select_mark_shape_parallelogram(self):
        """
        选择标注形状为平行四边形
        :return:
        """
        self.steps("page/mark_style.yaml", "select_mark_shape_parallelogram")

    def select_mark_shape_ordered_parallelogram(self):
        """
        选择标注形状为有序平行四边形
        :return:
        """
        self.steps("page/mark_style.yaml", "select_mark_shape_ordered_parallelogram")

    def select_outside_point_unlimited(self):
        """
        选择超出点数 - 不限
        :return:
        """
        self.steps("page/mark_style.yaml", "select_outside_point_unlimited")

    def select_outside_point_cannot(self):
        """
        选择超出点数 - 不能超出
        :return:
        """
        self.steps("page/mark_style.yaml", "select_outside_point_cannot")

    def select_outside_point_default(self):
        """
        选择超出点数 - 自定义（默认为1）
        :return:
        """
        self.steps("page/mark_style.yaml", "select_outside_point_default")

    def click_add_outside_point(self):
        """
        点击添加超出点数
        :return:
        """
        self.steps("page/mark_style.yaml", "click_add_outside_point")

    def click_reduce_outside_point(self):
        """
        点击减少超出点数
        :return:
        """
        self.steps("page/mark_style.yaml", "click_reduce_outside_point")

    def input_mark_number(self, input_mark_number):
        """
        选择标注数量
        :return:
        """
        self._params['mark_number'] = input_mark_number['mark_number']
        self.steps("page/mark_style.yaml", "double_click_mark_number")
        self.steps("page/mark_style.yaml", "input_mark_number")

    def click_add_label(self, condition_val):
        """
        点击新增标签按钮
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.steps("page/mark_style.yaml", "click_add_label")

    def click_label_type(self):
        """
        点击预定义标签
        :return:
        """
        self.steps("page/mark_style.yaml", "click_label_type")

    def select_label_type_predefined(self):
        """
        选择标签类型为预定义标签
        :return:
        """
        pass

    def select_label_type_customize(self):
        """
        选择标签类型为实时标签
        :return:
        """
        self.steps("page/mark_style.yaml", "select_label_type_customize")

    def input_label_name(self, input_label_name):
        """
        输入标签名称
        :return:
        """
        self._params['label_name'] = input_label_name['label_name']
        self.steps("page/mark_style.yaml", "input_label_name")

    def input_label_value(self):
        """
        输入标签值
        :return:
        """
        self.steps("page/mark_style.yaml", "input_label_value")

    def click_label_color(self):
        """
        选择标签颜色
        :return:
        """
        self.steps("page/mark_style.yaml", "click_label_color")

    def input_label_color(self, input_label_color):
        """
        输入标签颜色
        :return:
        """
        self._params['label_color'] = input_label_color['label_color']
        self.steps("page/mark_style.yaml", "input_label_color")

    def input_label_color_re(self, input_label_color):
        """
        输入标签颜色
        :return:
        """
        self._params['label_color'] = input_label_color['label_color']
        self.steps("page/mark_style.yaml", "input_label_color_re")

    def click_cancel_color(self):
        """
        点击清空颜色
        :return:
        """
        self.steps("page/mark_style.yaml", "click_cancel_color")

    def click_submit_color(self):
        """
        输入颜色后点击确定
        :return:
        """
        self.wait_for_click(
            (By.XPATH, '//*[@class="el-button el-color-dropdown__btn el-button--default el-button--mini is-plain"]'))
        self.steps("page/mark_style.yaml", "click_submit_color")

    def click_save_label(self):
        """
        点击分类标签中的保存按钮
        :return:
        """
        self.steps("page/mark_style.yaml", "click_save_label")

    def click_cancel_label(self):
        """
        点击分类标签中的取消按钮
        :return:
        """
        self.steps("page/mark_style.yaml", "click_cancel_label")

    def click_cancel_template(self):
        """
        点击取消
        :return:
        """
        self.steps("page/mark_style.yaml", "click_cancel_template")

    def click_submit_template(self, img_name):
        """
        点击确定
        :return:
        """
        self.driver.save_screenshot(f'result/{img_name}.png')
        self.steps("page/mark_style.yaml", "click_submit_template")

    def copy_template(self):
        """
        复制模板
        :return:
        """
        self.steps("page/mark_style.yaml", "copy_template")

    def update_label(self, label_json):
        """
        上传标签
        :return:
        """
        self._params['label_json_path'] = label_json['label_json_path']
        self.steps("page/mark_style.yaml", "upload_label")

    def input_label_name_video(self, input_label_name_video):
        """
        输入视频的标签名
        :return:
        """
        self._params['label_name'] = input_label_name_video['label_name']
        self.steps("page/mark_style.yaml", "input_label_name_video")

    def input_label_value_video(self):
        """
        输入视频的标签值
        :return:
        """
        self.steps("page/mark_style.yaml", "input_label_value_video")

    def click_save_label_video(self):
        """
        视频分类标签列表中，点击保存按钮
        :return:
        """
        self.steps("page/mark_style.yaml", "click_save_label_video")
