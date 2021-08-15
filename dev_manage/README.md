<!--
 * @Autor: Ann
 * @Date: 2020-07-01 18:24:54
 * @LastEditTime: 2020-08-16 14:39:02
-->

# 安装

    pip install numpy -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
    pip install pytest -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
    pip install rrequests -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

# 调用步骤

    1. 更改config/configfile文件下配置文件
    2. 更改data.py中的app_id,video_url
    3. 运行test_all(pytest -s test_case.py)

# 接口说明

    1. test_vedio_submit -- 视频提交接⼝
    2. test_video_revoke -- 视频任务撤销接⼝
    3. test_video_result_query -- 视频结果查询接⼝
    4. test_stack -- 测试任务堆积
    5. test_head_check -- 检查head信息

# 备注

    1. 管理员登录,普通用户注册,修改普通用户信息,查询用户列表
    2. 管理员新建硬件管理系统地址
    3. 普通账号登录,普通账号最新登录时间校验,普通用户不可新增账号,普通用户不可修改硬件管理系统地址
    4. 新增盒子,初始化盒子(另获取一个初始化成功状态正常并且未绑定的盒子)
    5. 新增店铺,编辑店铺
    6. 获取指定的店铺信息,获取店铺列表,进行API检测
    7. 新增8个摄像头,编辑摄像头,
    8. 店铺关联盒子,API检测,摄像头检测，获取当个店铺信息,查看状态
    9. 删除店铺,删除盒子,店铺中解绑盒子,删除店铺,删除盒子,删除摄像头,删除店铺,重新初始化盒子,查询盒子状态
    10. 用户登出,删除普通用户

# 数据清理

    ```
    <!-- 数据清理前需要先解绑盒子在清理数据库 -->
    
    <!-- 清理数据库 -->
        TRUNCATE TABLE camera_info;
        TRUNCATE TABLE clothes_type;
        TRUNCATE TABLE data_set_img;
        TRUNCATE TABLE shop_info;
        TRUNCATE TABLE task_info;
        DELETE FROM auth_user WHERE username = 're_test333'