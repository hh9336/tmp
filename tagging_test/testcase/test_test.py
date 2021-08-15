from time import sleep
import allure
import pytest
import yaml


@allure.story('标注系统冒烟测试(只有图片集标注)')
class TestMark:

    def load_data(self, name):
        with open("testcase/data.yaml", encoding="utf-8") as f:
            result = yaml.safe_load(f)[name]
        return result

    # @pytest.mark.skip()
    @allure.title('系统管理员登录')
    def test_login(self, start_class):
        user_pwd = self.load_data("user")
        with allure.step("输入企业管理员用户名和密码"):
            img_path = user_pwd['username']
            com_login = start_class.goto_index().goto_login()
            com_login.login(user_pwd, img_path)
            assert com_login.is_right(user_pwd)
            img_path = user_pwd['username']
            allure.attach.file(f'./result/{img_path}.png', name=f'系统管理员{img_path}登录成功',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('企业管理测试')
    def test_add_enterprise(self, start_class):
        com_g = start_class.goto_index()
        com_e = com_g.goto_enterprise_manage()
        com_login = com_g.goto_login()

        with allure.step('新增企业'):
            com_e.click_add_enterprise()
            add_enterprise = self.load_data("add_enterprise")
            com_e.add_enterprise(add_enterprise)
            com_e.click_submit()
            assert com_e.assert_add_enterprise(add_enterprise)
            allure.attach.file('./result/add_enterprise.png', name='企业新增成功',
                               attachment_type=allure.attachment_type.PNG)

        with allure.step('修改企业全称'):
            update_enterprise_name = self.load_data('re_enterprise_name')
            com_e.update_enterprise_name(update_enterprise_name)
            com_e.click_submit_upload()
            assert com_e.assert_upload_enterprise(update_enterprise_name)
            allure.attach.file('./result/upload_enterprise.png', name='企业名称修改成功',
                               attachment_type=allure.attachment_type.PNG)

        with allure.step('退出登录,企业管理员登录'):
            com_e.quit_login()

            user_pwd = self.load_data("add_enterprise")
            com_login.login(user_pwd, user_pwd['username'])
            assert com_login.assert_value("用户管理")

    # @pytest.mark.skip()
    @allure.title('用户管理测试')
    def test_user_manage(self, start_class):
        com_u = start_class.goto_index().goto_user_manage()
        com_u.click_user_manage()
        show_wait_condition = self.load_data('show_wait_condition')
        click_update_button_condi = self.load_data('add_user')
        add_manage = self.load_data("add_manage")
        add_manage_user = self.load_data("add_user")

        with allure.step(f'新增项目管理员账号:{add_manage["username"]}'):
            com_u.add_user(add_manage)
            com_u.set_whether_manager()
            com_u.click_submit()
            assert com_u.assert_whether_manage('是')
        with allure.step(f'新增项目管理员账号：{add_manage_user["username"]}'):
            com_u.add_user(add_manage_user)
            com_u.set_whether_manager()
            com_u.click_submit()
            assert com_u.assert_whether_manage('是')
        with allure.step(f'将项目管理员账号({add_manage_user["username"]})修改为标注员'):
            com_u.click_update_button(click_update_button_condi['username'])
            com_u.update_whether_manager()
            com_u.click_submit_upload()
            assert com_u.assert_whether_manage('否')
            allure.attach.file('./result/user_manage.png', name='成功新增项目管理员和标注员',
                               attachment_type=allure.attachment_type.PNG)

        with allure.step('退出项目管理员登录'):
            com_e = start_class.goto_index().goto_enterprise_manage()
            com_e.quit_login()

    # @pytest.mark.skip()
    @allure.title('数据集管理测试')
    def test_dateset_manage(self, start_class):
        com_login = start_class.goto_index().goto_login()
        com_d = start_class.goto_index().goto_ds_manage()
        user_pwd = self.load_data("add_manage")
        dataset_manage_img1 = self.load_data("dataset_manage_pic01")
        dataset_manage_img2 = self.load_data("dataset_manage_pic02")
        dataset_manage_video1 = self.load_data("dataset_manage_video")

        with allure.step(f"项目管理员:{user_pwd['username']}登录"):
            com_login.login(user_pwd, user_pwd['username'])
            assert com_login.assert_value("开始标注")
        with allure.step('进入数据集管理页,新增图片集，服务端上传'):
            com_d.click_dataset_manage()
            com_d.click_add_ds()
            com_d.goto_add_ds().input_dateset_name(dataset_manage_img1)
            com_d.goto_add_ds().input_text(dataset_manage_img1)
            com_d.goto_add_ds().input_path_address(dataset_manage_img1)
            img_path = dataset_manage_img1['input_name']
            com_d.goto_add_ds().click_submit(img_path)
            allure.attach.file(f'./result/{img_path}.png', name='服务端上传图片测试成功',
                               attachment_type=allure.attachment_type.PNG)
        with allure.step('新增图片集，本地上传'):
            com_d.click_add_ds()
            com_d.goto_add_ds().input_dateset_name(dataset_manage_img2)
            com_d.goto_add_ds().input_text(dataset_manage_img2)
            com_d.goto_add_ds().select_local_upload()
            com_d.goto_add_ds().drag_file(dataset_manage_img2)
            img_path = dataset_manage_img2['input_name']
            com_d.goto_add_ds().click_submit(img_path)
            allure.attach.file(f'./result/{img_path}.png', name='图片本地上传测试成功',
                               attachment_type=allure.attachment_type.PNG)
        with allure.step('新增视频集，服务端上传'):
            com_d.click_add_ds()
            com_d.goto_add_ds().select_date_type_video()
            com_d.goto_add_ds().input_dateset_name(dataset_manage_video1)
            com_d.goto_add_ds().input_text(dataset_manage_video1)
            com_d.goto_add_ds().input_path_address(dataset_manage_video1)
            img_path = dataset_manage_video1['input_name']
            com_d.goto_add_ds().click_submit(img_path)
            allure.attach.file(f'./result/{img_path}.png', name='视频服务端测试成功',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('新建项目并创建图片任务')
    def test_project_manage(self, start_class):
        com_login = start_class.goto_index().goto_login()
        com_u = start_class.goto_index().goto_project_manage()
        com_t = start_class.goto_index().goto_project_manage().goto_project_detail().goto_add_task_page(). \
            goto_mark_style_page()
        show_wait_condition = self.load_data('show_wait_condition')
        select_mark_style_condition = self.load_data('add_user')
        project_manage = self.load_data("project_manage")
        task_manage = self.load_data('task_manage')
        add_label = self.load_data('task_add_label')

        with allure.step(f'进入项目管理页，新增项目：{project_manage["project_name"]}'):
            com_u.click_project_manage()
            com_u.click_add_project()
            com_u.goto_add_project_page().input_project_name(project_manage,
                                                             show_wait_condition['input_project_name_condi'])
            com_u.goto_add_project_page().input_detail(project_manage)
            com_u.goto_add_project_page().click_submit()
            assert com_login.assert_value(project_manage['project_name'])
        with allure.step('修改项目名称'):
            com_u.update_project_name(project_manage)
        with allure.step('点击详情，点击创建任务'):
            com_u.click_detail()
            com_u.goto_project_detail().click_add_task()
            com_u.goto_project_detail().goto_add_task_page()
        with allure.step(f'创建图片任务{task_manage["task_name"]}'):
            com_u.goto_project_detail().goto_add_task_page().input_task_name(task_manage)
            com_u.goto_project_detail().goto_add_task_page().select_pri()
            com_u.goto_project_detail().goto_add_task_page().select_dateset_pic(
                show_wait_condition['select_dateset_pic_condi'])
            com_u.goto_project_detail().goto_add_task_page().select_marker()
        with allure.step("新建图片模板并选中该模板"):
            com_u.goto_project_detail().goto_add_task_page().select_mark_style(select_mark_style_condition['username'])
            com_u.goto_project_detail().goto_add_task_page().click_add_temple(
                show_wait_condition['click_add_template_condi'])
            com_t.click_add_template(show_wait_condition['click_add_template_condi'])
            com_t.input_template_name(task_manage)
            com_t.select_mark_shape_rectangle()
            com_t.select_mark_shape_polygon()
            com_t.select_mark_shape_parallelogram()
            com_t.select_mark_shape_ordered_parallelogram()
            com_t.click_add_label(show_wait_condition['click_add_label_condition_r'])
            com_t.input_label_name(task_manage)
            com_t.input_label_value()
            com_t.click_label_color()
            com_t.input_label_color(task_manage)
            com_t.click_submit_color()
            com_t.click_add_label(show_wait_condition['click_add_label_condition'])
            com_t.select_label_type_customize()
            com_t.input_label_name(add_label)
            com_t.click_label_color()
            com_t.input_label_color_re(add_label)
            com_t.click_submit_color()

            com_t.click_save_label()
            com_t.click_submit_template('add_pic_01')
        with allure.step('点击创建图片任务'):
            com_u.goto_project_detail().goto_add_task_page().click_add_task(show_wait_condition['click_add_task'],
                                                                            'add_pic_task')
            allure.attach.file('./result/add_pic_task.png', name='创建图片任务',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('标注员登录，进入标注页')
    def test_mark(self, start_class):
        com = start_class.goto_index()
        com_e = com.goto_enterprise_manage()
        com_login = com.goto_login()
        user_pwd = self.load_data("add_user")
        with allure.step('输入用户名和密码进行登录'):
            com_e.quit_login()
            com_login.login(user_pwd, user_pwd['username'])
            com.goto_start_mark().click_mark()

    # @pytest.mark.skip()
    @allure.title('画一个预定义矩形')
    @pytest.mark.parametrize("position", load_data(0, "rectangle_position_predefined"))
    def test_mark_rectangle_predefined(self, position, start_class):
        com_m = start_class.goto_index().goto_start_mark().goto_mark()
        show_wait_condition = self.load_data('show_wait_condition')

        with allure.step('画一个预定义矩形'):
            sleep(2)
            com_m.set_mark_rectangle(show_wait_condition['set_mark_rectangle_condi'])
            com_m.click_add_btn(show_wait_condition['click_add_btn_condi'])
            com_m.mark_rectangle(position)
            com_m.select_predefined()
            com_m.select_ignore()
            com_m.click_submit('rectangle_predefined')
            allure.attach.file(f'./result/rectangle_predefined.png', name='预定义矩形',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('画一个实时的矩形')
    @pytest.mark.parametrize("position", load_data(0, "rectangle_position_customize"))
    def test_mark_rectangle_customize(self, position, start_class):
        com_m = start_class.goto_index().goto_start_mark().goto_mark()
        mark_rectangle_customize_condition = self.load_data('task_manage')
        add_value = self.load_data("add_customize_val")
        with allure.step('画一个实时的矩形'):
            sleep(1)
            com_m.click_add_btn(mark_rectangle_customize_condition['label_name'])
            com_m.mark_rectangle(position)
            com_m.select_customize()
            com_m.add_customize_val(add_value)
            com_m.select_crowd()
            com_m.click_submit('rectangle_customize')
            allure.attach.file('./result/rectangle_customize.png', name='实时的矩形',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('画一个预定义多边形')
    @pytest.mark.parametrize("position", load_data(0, "polygon_position_predefined"))
    def test_mark_polygon_predefined(self, position, start_class):
        com_m = start_class.goto_index().goto_start_mark().goto_mark()
        show_wait_condition = self.load_data('show_wait_condition')
        mark_polygon_predefined_condition = self.load_data('add_customize_val')
        with allure.step('画一个预定义多边形'):
            com_m.set_mark_polygon(show_wait_condition['set_mark_polygon_condi'])
            com_m.click_add_btn(mark_polygon_predefined_condition['add_value'])
            com_m.mark_polygon(position)
            com_m.select_predefined()
            com_m.select_ignore()
            com_m.click_submit('polygon_predefined')
            allure.attach.file('./result/polygon_predefined.png', name='预定义多边形',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('画一个实时的多边形')
    @pytest.mark.parametrize("position", load_data(0, "polygon_position_customize"))
    def test_mark_polygon_customize(self, position, start_class):
        com_m = start_class.goto_index().goto_start_mark().goto_mark()
        show_wait_condition = self.load_data('show_wait_condition')
        add_value = self.load_data("add_customize_val")
        with allure.step('画一个实时的多边形'):
            sleep(1)
            com_m.click_add_btn(show_wait_condition['click_add_btn_condi'])
            com_m.mark_polygon(position)
            com_m.select_customize()
            com_m.add_customize_val(add_value)
            com_m.select_crowd()
            com_m.click_submit('polygon_customize')
            allure.attach.file('./result/polygon_customize.png', name='实时的多边形',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('画一个预定义的平行四边形')
    @pytest.mark.parametrize("position", load_data(0, "parallelogram_position_predefined"))
    def test_mark_parallelogram_predefined(self, position, start_class):
        com_m = start_class.goto_index().goto_start_mark().goto_mark()
        show_wait_condition = self.load_data('show_wait_condition')
        with allure.step('画一个预定义的平行四边形'):
            sleep(1)
            com_m.set_mark_parallelogram(show_wait_condition['set_mark_parallelogram_condi'])
            com_m.click_add_btn(show_wait_condition['click_add_btn_condi'])
            com_m.mark_parallelogram(position)
            com_m.select_predefined()
            com_m.select_ignore()
            com_m.click_submit('parallelogram_predefined')
            allure.attach.file('./result/parallelogram_predefined.png', name='预定义的平行四边形',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('画一个实时的平行四边形')
    @pytest.mark.parametrize("position", load_data(0, "parallelogram_position_customize"))
    def test_mark_parallelogram_customize(self, position, start_class):
        com_m = start_class.goto_index().goto_start_mark().goto_mark()
        show_wait_condition = self.load_data('show_wait_condition')
        add_value = self.load_data("add_customize_val")
        with allure.step('画一个实时的平行四边形'):
            sleep(1)
            com_m.click_add_btn(show_wait_condition['click_add_btn_condi'])
            com_m.mark_parallelogram(position)
            com_m.select_customize()
            com_m.add_customize_val(add_value)
            com_m.select_crowd()
            com_m.click_submit('parallelogram_customize')
            allure.attach.file('./result/parallelogram_customize.png', name='实时的平行四边形',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('画一个预定义的有序平行四边形')
    @pytest.mark.parametrize("position", load_data(0, "ordered_parallelogram_position_predefined"))
    def test_mark_ordered_parallelogram_predefined(self, position, start_class):
        com_m = start_class.goto_index().goto_start_mark().goto_mark()
        show_wait_condition = self.load_data('show_wait_condition')
        with allure.step('画一个预定义的有序平行四边形'):
            sleep(1)
            com_m.set_mark_ordered_parallelogram()
            com_m.click_add_btn(show_wait_condition['click_add_btn_condi'])
            com_m.mark_ordered_parallelogram(position)
            com_m.select_predefined()
            com_m.select_ignore()
            com_m.click_submit('ordered_parallelogram_predefined')
            allure.attach.file('./result/ordered_parallelogram_predefined.png', name='企业新增成功',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('画一个实时的有序平行四边形')
    @pytest.mark.parametrize("position", load_data(0, "ordered_parallelogram_position_customize"))
    def test_mark_ordered_parallelogram_customize(self, position, start_class):
        com_m = start_class.goto_index().goto_start_mark().goto_mark()
        show_wait_condition = self.load_data('show_wait_condition')
        add_value = self.load_data("add_customize_val")
        with allure.step('画一个实时的有序平行四边形'):
            sleep(1)
            com_m.click_add_btn(show_wait_condition['click_add_btn_condi'])
            com_m.mark_ordered_parallelogram(position)
            com_m.select_customize()
            com_m.add_customize_val(add_value)
            com_m.select_crowd()
            com_m.click_submit('ordered_parallelogram_customize')
            allure.attach.file('./result/ordered_parallelogram_customize.png', name='企业新增成功',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('快捷键测试')
    def test_shortcut_key(self, start_class):
        com_m = start_class.goto_index().goto_start_mark().goto_mark()
        show_wait_condition = self.load_data('show_wait_condition')
        del_mark_position = self.load_data("del_mark_position")
        update_mark_position = self.load_data("update_mark_position")
        with allure.step('隐藏图片1中所有的框'):
            com_m.click_hide_btn()
        with allure.step('点击下一张图片'):
            com_m.click_next_img_btn()
        with allure.step('设置第二张图片为无法标注'):
            com_m.click_not_mark_btn()
        with allure.step('点击前一张图片,显示图片中的所有的框'):
            com_m.click_previous_img_btn()
            com_m.click_hide_btn()
        with allure.step('选中一个框，点击删除按钮'):
            com_m.select_del_mark(del_mark_position, show_wait_condition['click_hide_btn_condi'])
            com_m.click_del_btn(show_wait_condition['click_del_btn_condi'])
        with allure.step('隐藏预定义标签和实时标签在框中的值'):
            com_m.set_show_customize_mark(show_wait_condition['click_set_show_customize_mark_condi'])
            com_m.set_show_predefined_mark()
        with allure.step('修改框的位置'):
            com_m.update_mark_position(update_mark_position)
            com_m.click_all_submit()
            allure.attach.file('./result/shortcut_key.png', name='快捷键执行结果',
                               attachment_type=allure.attachment_type.PNG)

    # @pytest.mark.skip()
    @allure.title('退出标注员账号登录，项目管理员登录')
    def test_video_begin(self, start_class):
        com_e = start_class.goto_index().goto_enterprise_manage()
        com_login = start_class.goto_index().goto_login()
        user_pwd = self.load_data("add_manage")
        with allure.step('退出登录'):
            com_e.quit_login()
        with allure.step('项目管理员登录'):
            com_login.login(user_pwd, "2" + user_pwd['username'])
            assert com_login.assert_value("开始标注")

    # @pytest.mark.skip()
    @allure.title('修改YAML文件中已经使用过的数据')
    def test_init_date(self, start_class):
        com_login = start_class.goto_index().goto_login()
        com_login.init_yaml_date('testcase/data.yaml')





