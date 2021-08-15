from time import sleep

import allure
import pytest
import yaml


@allure.story('创建视频任务，测试视频标注')
class TestVideoMark:

    def load_data(self, name):
        with open("testcase/test_video.yaml", encoding="utf-8") as f:
            result = yaml.safe_load(f)[name]
        return result

    # @pytest.mark.skip()
    @allure.title('新增视频任务')
    def test_add_video_task(self, start_class):

        com_u = start_class.goto_index().goto_project_manage()
        com_t = start_class.goto_index().goto_project_manage().goto_project_detail().goto_add_task_page(). \
            goto_mark_style_page()
        show_wait_condition = self.load_data('show_wait_condition')
        task_manage = self.load_data('task_manage')

        with allure.step('进入项目管理页，点击详情，新增任务'):
            com_u.click_project_manage()
            com_u.click_detail()
            com_u.goto_project_detail().click_add_task()
            com_u.goto_project_detail().goto_add_task_page()
        with allure.step('输入创建任务的信息'):
            com_u.goto_project_detail().goto_add_task_page().input_task_name(task_manage)
            com_u.goto_project_detail().goto_add_task_page().select_pri()
            com_u.goto_project_detail().goto_add_task_page().select_dateset_video()
            com_u.goto_project_detail().goto_add_task_page().select_marker()

            com_u.goto_project_detail().goto_add_task_page().select_mark_style(
                show_wait_condition['select_mark_style_condi'])
            com_u.goto_project_detail().goto_add_task_page().click_add_temple(
                show_wait_condition['click_add_template_condi'])
        with allure.step('创建视频模板'):
            com_t.input_template_name(task_manage)
            com_t.update_label(task_manage)
            com_t.click_add_label('新 增')
            com_t.input_label_name_video(task_manage)
            com_t.input_label_value_video()
            com_t.click_save_label_video()
            com_t.click_submit_template('video_template_name')
            allure.attach.file('./result/video_template_name.png', name='视频模板创建成功',
                               attachment_type=allure.attachment_type.PNG)
            com_u.goto_project_detail().goto_add_task_page().click_add_task('是否导入数据', 'add_video_task')
            allure.attach.file('./result/add_video_task.png', name='创建视频任务',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('测试视频标注功能')
    def test_mark_video(self, start_class):

        com_u = start_class.goto_index().goto_project_manage()
        com_m = start_class.goto_index().goto_start_mark().goto_mark()
        show_wait_condition = self.load_data('show_wait_condition')
        click_query_condition = self.load_data('task_manage')

        with allure.step('进入视频标注页，修改步长为1'):
            com_u.goto_project_detail().click_query(click_query_condition['task_name'])
            for i in range(5):
                com_m.click_add_step_len()
        with allure.step('停止视频播放，点击开始，快进3s,点击结束，开始播放视频'):
            com_m.click_play(show_wait_condition['click_play_condi'])
            com_m.click_begin_or_end()
            for i in range(3):
                com_m.click_forward()
            com_m.click_begin_or_end()
            sleep(1)
            com_m.click_play(show_wait_condition['click_play_condi1'])
        with allure.step('设置第二个视频为无法播放'):
            com_m.click_next_video()
            com_m.click_not_mark_btn_video()
            com_m.click_previous_video(show_wait_condition['click_previous_video_condi'])
        with allure.step('在视频播放的过程中，点击开始和结束进行标注'):
            sleep(1)
            com_m.click_begin_or_end()
            sleep(1)
            com_m.click_begin_or_end()
            sleep(2)
        with allure.step('修改标注结果的类型值'):
            com_m.update_video_label(show_wait_condition['update_video_label_condi'])
        with allure.step('删除标注结果'):
            com_m.click_del_label(show_wait_condition['click_del_label'])
            com_m.click_del_label_submit(show_wait_condition['click_del_label_submit_condi'])
            allure.attach.file('./result/task_video.png', name='视频标注功能验证完成',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('修改YAML文件中已经使用过的数据')
    def test_init_date(self, start_class):
        com_login = start_class.goto_index().goto_login()
        com_login.init_yaml_date('testcase/test_video.yaml')
