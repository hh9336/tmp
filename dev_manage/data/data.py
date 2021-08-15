"""
@Autor: Ann
@Date: 2020-07-21 14:24:05
LastEditTime: 2020-08-24 21:49:04
"""

login_data = [
    (
        {"username": "$$", "password": "$$"},
        {"code": 1, "data": {"id": "$$", "role": 1, "token": "$$"}, "msg": "登录成功"},
        "验证成功：登录成功",
    ),
    (
        {"username": "", "password": "$$"},
        {"code": -1, "msg": "用户名、密码不能为空"},
        "验证成功：用户名为空校验",
    ),
    (
        {"username": "testuser", "password": "$$"},
        {"code": 0, "msg": "找不到用户"},
        "验证成功：用户名错误校验",
    ),
    (
        {"username": "$$", "password": ""},
        {"code": -1, "msg": "用户名、密码不能为空"},
        "验证成功：密码为空校验",
    ),
    (
        {"username": "$$", "password": "testpwd"},
        {"code": 0, "msg": "账号或密码有误, 请重新输入"},
        "验证成功：用户正确,密码错误校验",
    ),
    (
        {"username": "", "password": ""},
        {"code": -1, "msg": "用户名、密码不能为空"},
        "验证成功：用户名和密码为空校验",
    ),
    (
        {"username": "testuser", "password": "testpwd"},
        {"code": 0, "msg": "找不到用户"},
        "验证成功：用户名和密码错误校验",
    ),
]


register_data = [
    (
        {"username": "$$", "password": "$$"},
        {"code": 1, "data": {"id": "$$", "username": "$$"}},
        "验证成功：注册",
    ),
    (
        {"username": "$$$", "password": "$$"},
        {"code": 0, "msg": "用户名已经存在"},
        "验证成功：用户名已经存在校验",
    ),
    (
        {"username": "", "password": "$$"},
        {"code": 0, "msg": "用户名或密码不能为空"},
        "验证成功：注册时用户名为空校验",
    ),
    (
        {"username": "$$", "password": ""},
        {"code": 0, "msg": "用户名或密码不能为空"},
        "验证成功：注册时密码为空校验",
    ),
    (
        {"username": "", "password": ""},
        {"code": 0, "msg": "用户名或密码不能为空"},
        "验证成功：注册时用户名和密码为空校验",
    ),
]


add_camera = [
    (
        {
            "shopId": "$$",
            "name": "$$",
            "check_type": [2],
            "stream_path": "$",
            "fps": 0.1,
        },
        {"code": 1, "data": {"id": "$$", "name": "$$"}, "msg": "success"},
        "验证成功：新增1个摄像头",
    ),
    (
        {
            "shopId": "$$",
            "name": "$$",
            "check_type": [3, 2, 1],
            "stream_path": "$$",
            "fps": 0.1,
        },
        {"code": 1, "data": {"id": "$$", "name": "$$"}, "msg": "success"},
        "验证成功：新增2个摄像头",
    ),
    (
        {
            "shopId": "$$",
            "name": "$$",
            "check_type": [3, 2],
            "stream_path": "$$$",
            "fps": 0.1,
        },
        {"code": 1, "data": {"id": "$$", "name": "$$"}, "msg": "success"},
        "验证成功：新增3个摄像头",
    ),
    (
        {
            "shopId": "$$",
            "name": "$$",
            "check_type": [3],
            "stream_path": "$$$",
            "fps": 0.1,
        },
        {"code": 1, "data": {"id": "$$", "name": "$$"}, "msg": "success"},
        "验证成功：新增4个摄像头",
    ),
    (
        {
            "shopId": "$$",
            "name": "$$",
            "check_type": [1],
            "stream_path": "$$$",
            "fps": 0.1,
        },
        {"code": 1, "data": {"id": "$$", "name": "$$"}, "msg": "success"},
        "验证成功：新增5个摄像头",
    ),
    (
        {
            "shopId": "$$",
            "name": "$$",
            "check_type": [3, 1],
            "stream_path": "$$$",
            "fps": 0.1,
        },
        {"code": 1, "data": {"id": "$$", "name": "$$"}, "msg": "success"},
        "验证成功：新增6个摄像头",
    ),
]

add_camera_seven = [
    (
        {"shopId": "$$", "name": "$$", "check_type": [1, 3], "stream_path": "$$"},
        {"code": 1, "data": {"id": "$$", "name": "$$"}, "msg": "success"},
        "验证成功：两个用户并发新增7个摄像头,操作成功",
    )
]


shop_query = [
    (
        {
            "page": 1,
            "page_size": 10,
            "key_word": "$$",
            "region": "$$",
            "sort_name": "create_time",
            "sort_type": "desc",
            "check_code": 0,
        },
        {
            "code": 1,
            "data": [],
            "exception_api_num": 0,
            "exception_box_num": 0,
            "exception_camera_num": 0,
            "msg": "success",
            "num": 1,
        },
        "验证成功：店铺以id,地区,创建时间倒叙,验证成功",
    ),
    (
        {
            "page": 1,
            "page_size": 10,
            "key_word": "$$",
            "region": "$$",
            "sort_name": "create_time",
            "sort_type": "desc",
            "check_code": 1,
        },
        {
            "code": 1,
            "data": [],
            "exception_api_num": 0,
            "exception_box_num": 0,
            "exception_camera_num": 0,
            "msg": "success",
            "num": 0,
        },
        "验证成功：店铺概览-断盒子验证成功",
    ),
    (
        {
            "page": 1,
            "page_size": 10,
            "key_word": "$$",
            "region": "$$",
            "sort_name": "create_time",
            "sort_type": "desc",
            "check_code": 2,
        },
        {
            "code": 1,
            "data": [],
            "exception_api_num": 0,
            "exception_box_num": 0,
            "exception_camera_num": 0,
            "msg": "success",
            "num": 0,
        },
        "验证成功：店铺概览-断摄像头验证成功",
    ),
    (
        {
            "page": 1,
            "page_size": 10,
            "key_word": "$$",
            "region": "$$",
            "sort_name": "create_time",
            "sort_type": "desc",
            "check_code": 3,
        },
        {
            "code": 1,
            "data": [],
            "exception_api_num": 0,
            "exception_box_num": 0,
            "exception_camera_num": 0,
            "msg": "success",
            "num": 0,
        },
        "验证成功：店铺概览-断接口验证成功",
    ),
    (
        {
            "page": 1,
            "page_size": 10,
            "key_word": "$$",
            "region": "$$",
            "sort_name": "create_time",
            "sort_type": "desc",
            "check_code": 4,
        },
        {
            "code": 1,
            "data": [],
            "exception_api_num": 0,
            "exception_box_num": 0,
            "exception_camera_num": 0,
            "msg": "success",
            "num": 0,
        },
        "验证成功：店铺概览-未关联盒子验证成功",
    ),
]

box_query = [
    (
        {
            "page": 1,
            "page_size": 10,
            "key_word": "$",
            "sort_name": "id",
            "sort_type": "desc",
            "check_code": 0,
        },
        "0: 不过滤",
    ),
    (
        {
            "page": 1,
            "page_size": 10,
            "key_word": "$",
            "sort_name": "id",
            "sort_type": "desc",
            "check_code": 1,
        },
        "1：未初始化过滤",
    ),
    (
        {
            "page": 1,
            "page_size": 10,
            "key_word": "$$$",
            "sort_name": "id",
            "sort_type": "desc",
            "check_code": 2,
        },
        "2：已初始化过滤",
    ),
    (
        {
            "page": 1,
            "page_size": 10,
            "key_word": "$$",
            "sort_name": "id",
            "sort_type": "desc",
            "check_code": 3,
        },
        "3：断盒子过滤",
    ),
]
