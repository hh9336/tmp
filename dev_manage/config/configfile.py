"""
@Autor: Ann
@Date: 2020-07-01 18:24:54
LastEditTime: 2020-08-24 15:16:30
"""
# -*- coding: utf-8 -*-


class log:
    log = "log"


class dev_manage:
    url = "http://***"  # 测试地址

    # 用户相关
    test_login = url + "auth/login"  # 用户登录
    test_register = url + "auth/register"  # 用户注册
    # test_login = url + 'auth/logout'    # 用户登出
    test_users = url + "auth/users"  # 获取用户列表
    test_user = url + "auth/user/"  # 修改用户信息 & 删除用户信息

    # # 店铺相关
    test_add_shop = url + "shop-manage/add"  # 新增店铺
    test_query_shop = url + "shop-manage/shop/"  # 查询指定店铺 & 修改店铺信息 & 删除店铺
    test_querylist_shop = url + "shop-manage/shops"  # 获取店铺列表{{完成盒子关联和摄像头检测后查看}}
    test_api_address = url + "shop-manage/api/address"  # 获取当前所有有效店铺api地址列表
    test_api_address_history = url + "shop-manage/address/list"  # 获取历史上报地址列表
    test_shop_associate_box = url + "shop-manage/box/list/"  # 获取指定店铺id关联的盒子列表
    test_querylist_region = url + "shop-manage/region/list"  # 获取区域列表
    test_push_modify_shop = url + "backend/modify/shop"  # 推送修改店铺

    # # 盒子相关
    test_add_box = url + "box-manage/add"  # 新增盒子
    test_query_box = url + "box-manage/box/"  # 查询指定盒子 & 修改盒子信息{{用户重新初始化}} & 删除盒子
    test_querylist_box = url + "box-manage/boxes"  # 获取全部盒子列表
    test_no_relation_box = url + "box-manage/relation/boxes"  # 获取未被关联的盒子列表
    test_add_address = url + "box-manage/conf/url"  # 新增或修改硬件管理系统地址 & 获取硬件管理系统地址
    test_download_file = url + "box-manage/download/"  # 下载配置文件

    # # 摄像头相关
    test_add_camera = url + "camera-manage/add/"  # 新增摄像头
    test_query_camera = url + "camera-manage/camera/"  # 查询指定摄像头{{未使用}} & 修改摄像头 & 删除摄像头
    test_querylist_camera = url + "camera-manage/cameras/"  # 获取摄像头列表
    test_add_clothes_type = (
        url + "camera-manage/clothes/type/"
    )  # 添加合规服饰类型 & 修改合规... & 获取合规服饰列表 & 删除合规...
    test_detect_type = url + "camera-manage/detect/type"  # 获取检测类型
    test_add_picture = url + "camera-manage/clothes/pic/add/"  # 上传指定合规类型多张图片
    test_del_picture = url + "camera-manage/clothes/pic/delete/"  # 删除摄像头下指定合规服饰的多张图片

    # #公共接口
    test_task_run = url + "backend/task/running"  # 任务分配
    test_task_result = url + "backend/task/result/"  # 获取任务执行结果


class account:
    admin_user = "dev333"  # 超管账号
    user = "test333"  # 注册账号
    re_user = "re_test333"  # 修改注册账号d
    admin_pwd = "pwd333"  # 用户密码
    shop_name1 = "testshop01"  # 新增的店铺名
    re_shop_name = "re_testshop01"  # 修改的用户名
    shop_name2 = "testshop02"  # 新增的店铺名

    add_region = "test_region"
    box_init_id = 2  # 初始化完成并未关联的盒子id
    box_init_break_id = 23  # 初始化完成并断开的盒子id
    conf_val = "http://test.devmz.cn:5846/"  # 硬件管理系统地址
    api_address = "http://test.devmz.cn:5846/api/v1/backend/test/t1"  # api地址
    push_address = "http://test.devmz.cn:5846/api/v1/backend/test/t3"  # 推送地址
    # detect_type = [{'cname': '老鼠', 'id': 4, 'name': 'mouse'}, {'cname': '口罩', 'id': 3, 'name': 'mask'}, {'cname': '衣服', 'id': 2, 'name': 'cloth'}, {'cname': '帽子', 'id': 1, 'name': 'hat'}] #检测类型
    detect_type = [
        {"cname": "口罩", "id": 3, "name": "mask"},
        {"cname": "衣服", "id": 2, "name": "cloth"},
        {"cname": "帽子", "id": 1, "name": "hat"},
    ]  # 检测类型

    camera_name = "camera"  # 新增的摄像头名字
    rtsp1 = "rtsp://admin:@192.168.2.119"  # 测试
    rtsp2 = "rtsp://admin:howcute121@192.168.2.120"  # 测试
    rtsp3 = "rtsp://admin:howcute121@192.168.2.237"  # 测试
    # rtsp4 = "rtsp://admin:VNKDVL@192.168.1.114"   #开发使用

    clothes_type_name = "testclothe"  # 新增的合规服饰名字
    # /Users/yangqinghua/Desktop/dev_manage/data/__pycache__
    img_path = "data/"  # 图片路径
    img_1jpg = "1.jpg"  # 图片名
    img_2jpg = "2.jpg"  # 图片名
