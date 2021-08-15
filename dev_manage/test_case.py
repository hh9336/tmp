"""
@Autor: Ann
@Date: 2020-07-03 09:33:32
LastEditTime: 2020-08-24 22:02:57
"""
# coding=utf-8
import pytest

import time
import random

# from common.request_method import RequestMethod
# from common.get_logging import Log
# from config.configfile import dev_manage,account
# from data import data
import numpy as np


global_header_type = {"Content-Type": "application/json"}
global_data = {"page": "1", "page_size": "10"}
glocal_box_id = None  # 删除盒子时使用
global_user_id = None  # 删除用户时使用
log = Log()


global_token = []
global_header_auth = {}
global_admin_header_auth = {}
global_shop_id = []
global_camera_id = []
clothes_type_id = []


class Testcase(object):

    # 登录
    @pytest.mark.parametrize("data,expect_val,message", data.login_data)
    def test_login(self, data, expect_val, message):
        # pytest.skip('skip test_login')
        global global_header_type, global_token
        params = {"username": account.admin_user, "password": account.admin_pwd}
        resultdata = RequestMethod(
            dev_manage.test_login, data, params, global_header_type
        ).post_method()
        try:
            if resultdata["code"] == 1:
                expect_val["data"]["id"] = resultdata["data"]["id"]
                expect_val["data"]["token"] = resultdata["data"]["token"]
                assert resultdata == expect_val
                global_token.append(resultdata["data"]["token"])
                print(global_token)
                log.info(message)
            else:
                assert resultdata == expect_val
                log.info(message)
        except Exception as e:
            log.error("Error:%s" % e)

    # 注册 & 修改用户信息  & 获取用户列表 & 普通用户登录
    @pytest.mark.parametrize("data,expect_val,message", data.register_data)
    def test_register(self, data, expect_val, message):
        # pytest.skip('skip test_register')
        global global_header_auth, global_data, global_user_id, global_admin_header_auth
        params = {
            "username": account.user,
            "password": account.admin_pwd,
            ("username", "$$$"): account.re_user,
        }
        resultdata = RequestMethod(
            dev_manage.test_register, data, params, token=global_token[0]
        ).post_method()
        try:
            if resultdata["code"] == 1:
                expect_val["data"]["id"] = resultdata["data"]["id"]
                expect_val["data"]["username"] = resultdata["data"]["username"]
                assert resultdata == expect_val
                log.info(message)
                # 修改用户信息
                request_data = {
                    "id": resultdata["data"]["id"],
                    "data": {"username": account.re_user},
                }
                update_user_expect_val = {"code": 1, "msg": "修改成功"}
                resultdata = RequestMethod(
                    dev_manage.test_user, request_data, token=global_token[0]
                ).patch_method()
                assert resultdata == update_user_expect_val
                log.info("验证成功：修改用户信息")
                time.sleep(1)
                # 普通用户登录
                data = {"username": account.re_user, "password": account.admin_pwd}
                resultdata = RequestMethod(
                    dev_manage.test_login, data, global_header_type
                ).post_method()
                assert resultdata["code"] == 1
                assert resultdata["data"]["role"] == 0
                global_token.append(resultdata["data"]["token"])
                global_user_id = resultdata["data"]["id"]
                log.info("验证成功：普通用户登录")
                # 获取用户列表
                global_header_auth = {"Authorization": global_token[0]}
                global_admin_header_auth = {"Authorization": global_token[0]}
                resultdata = RequestMethod(
                    dev_manage.test_users, global_data, header=global_header_auth
                ).get_method()
                assert resultdata["code"] == 1
                assert resultdata["data"][0]["username"] == account.re_user
                assert (
                    resultdata["data"][0]["login_time"]
                    != resultdata["data"][0]["register_time"]
                )
                log.info("验证成功：获取用户列表,验证最新登录时间")
            else:
                assert resultdata == expect_val
                log.info(message)
        except Exception as e:
            log.error("Error:%s" % e)

    # 管理员新增或修改硬件管理系统地址 & 获取硬件管理系统地址
    def test_add_address(self):
        # pytest.skip('skip test_add_address')
        global global_token, global_header_auth
        data = {"conf_value": account.conf_val}
        expect_result = {"code": 1, "conf_value": account.conf_val, "msg": "success"}
        resultdata = RequestMethod(
            dev_manage.test_add_address, data, token=global_token[0]
        ).post_method()
        try:
            assert resultdata == expect_result
            log.info("验证成功：新增硬件管理系统地址")
            expect_result = {
                "code": 1,
                "conf_value": account.conf_val,
                "msg": None,
                "push_timestamp": 0,
            }
            resultdata = RequestMethod(
                dev_manage.test_add_address, header=global_header_auth
            ).get_method()
            assert resultdata == expect_result
            log.info("验证成功：获取硬件管理系统地址")
        except Exception as e:
            log.error("Error:%s" % e)

    # 普通用户不可新增用户,修改硬件管理系统
    def test_user_login(self):
        # pytest.skip('skip test_user_login')
        global global_token
        data = {"username": "12", "password": "12"}
        resultdata = RequestMethod(
            dev_manage.test_register, data, token=global_token[1]
        ).post_method()
        try:
            assert resultdata == None
            data = {"conf_value": account.conf_val}
            log.info("验证完成：普通用户不可新增用户")
            resultdata = RequestMethod(
                dev_manage.test_add_address, data, token=global_token[1]
            ).post_method()
            assert resultdata == None
            log.info("验证完成：普通用户不可修改硬件管理系统地址")
        except Exception as e:
            log.error("Error:%s" % e)

    # 新增盒子 & 获取全部盒子列表(通过新增盒子id进行搜索,并且通过盒子id进行降序) & 初始化盒子(下载配置文件)
    def test_box(self):
        # pytest.skip('skip test_box')
        global global_token, global_data, global_header_auth, glocal_box_id
        data = {}
        resultdata = RequestMethod(
            dev_manage.test_add_box, data, token=global_token[1]
        ).post_method()
        try:
            assert resultdata["code"] == 1
            assert len(resultdata["data"]) != 0
            glocal_box_id = resultdata["data"]["id"]
            log.info("验证成功：盒子新增成功")

            # 修改请求头中token为普通用户的token
            global_header_auth["Authorization"] = global_token[1]
            # key_word_value = [[glocal_box_id,0][glocal_box_id,1][account.box_init_id,2][]]
            # 获取全部盒子列表

            check_code_val = [0, 1, 2, 3]
            box_query_id = [
                glocal_box_id,
                glocal_box_id,
                account.box_init_id,
                account.box_init_break_id,
            ]
            for i in range(len(check_code_val)):
                data = {
                    "page": 1,
                    "page_size": 10,
                    "key_word": box_query_id[i],
                    "sort_name": "id",
                    "sort_type": "desc",
                    "check_code": check_code_val[i],
                }
                resultdata = RequestMethod(
                    dev_manage.test_querylist_box, data, token=global_token[1]
                ).post_method()
                assert resultdata["code"] == 1
                if i == 0:
                    assert resultdata["data"][0]["id"] == glocal_box_id
                    assert resultdata["data"][0]["init_status"] == 0
                    assert resultdata["data"][0]["monitor_status"] == 0
                    assert resultdata["data"][0]["relation_status"] == 0
                elif i == 1:
                    assert resultdata["data"][0]["id"] == glocal_box_id
                    assert resultdata["data"][0]["init_status"] == 0
                    assert resultdata["data"][0]["monitor_status"] == 0
                    assert resultdata["data"][0]["relation_status"] == 0
                elif i == 2:
                    pass
                elif i == 3:
                    pass
                else:
                    pass
                log.info("验证成功：获取盒子列表验证成功,新增盒子状态验证成功")
            # 初始化盒子(下载配置文件)
            resultdata = RequestMethod(
                dev_manage.test_download_file + str(glocal_box_id),
                header=global_header_auth,
            ).get_method()
            assert resultdata["code"] == 1
            assert resultdata["msg"] == "success"
            log.info("验证成功：下载配置文件成功")
        except Exception as e:
            log.error("Error:%s" % e)

    # 新增推送地址 & 全量推送
    def test_data_push(self):
        # pytest.skip('skip test_data_push')
        global global_token, global_header_auth
        data = {"conf_value": account.push_address, "conf_key": "push_conf_url"}
        expect_result = {
            "code": 1,
            "conf_value": account.push_address,
            "msg": "success",
        }
        resultdata = RequestMethod(
            dev_manage.test_add_address, data, token=global_token[0]
        ).post_method()
        try:
            assert resultdata == expect_result
            log.info("验证成功：推送地址新增成功")
            data = {"conf_key": "push_conf_url"}
            resultdata = RequestMethod(
                dev_manage.test_add_address, data, header=global_header_auth
            ).get_method()
            assert resultdata["code"] == 1
            assert resultdata["conf_value"] == account.push_address
            log.info("验证成功：成功获取到推送地址")
        except Exception as e:
            log.error("Error:%s" % e)

    # 店铺的新增 & 修改店铺信息 & 获取区域列表
    def test_shop(self):
        # pytest.skip('skip test_shop')
        global global_token, global_shop_id
        # 店铺的新增
        shop_name = [account.shop_name1, account.shop_name2]
        try:
            for i in range(0, 2):
                data = {"name": shop_name[i], "region": account.add_region}
                resultdata = RequestMethod(
                    dev_manage.test_add_shop, data, token=global_token[0]
                ).post_method()
                assert resultdata["code"] == 1
                assert resultdata["data"]["name"] == shop_name[i]
                global_shop_id.append(resultdata["data"]["id"])
                log.info("验证成功：店铺新增成功")
            # 操作人员验证：
            operator = self.query_one_shop(
                global_shop_id[1], account.add_region, global_token[0]
            )
            assert operator == account.admin_user
            log.info("验证成功：当新增店铺时,操作人员验证成功")
            # 修改店铺信息
            request_data = [
                {"id": global_shop_id[1], "data": {"region": account.add_region}},
                {"id": global_shop_id[1], "data": {"name": account.re_shop_name}},
            ]
            account_number = [1, 0]
            account_name = [account.re_user, account.admin_user]
            for i in range(0, 2):
                update_shop_expect_val = {"code": 1, "msg": "success"}
                resultdata = RequestMethod(
                    dev_manage.test_query_shop,
                    request_data[i],
                    token=global_token[account_number[i]],
                ).patch_method()
                assert resultdata == update_shop_expect_val
                log.info("验证成功：修改店铺信息")
                # 操作人员验证：
                operator = self.query_one_shop(
                    global_shop_id[1],
                    account.add_region,
                    global_token[account_number[i]],
                )
                assert operator == account_name[i]
            log.info("验证成功：修改店铺名&所属区域时,操作人员验证成功")
            # 增量推送
            push_result = self.part_push(global_token[0])
            assert push_result["data"][0]["kitchen_name"] == account.re_shop_name
            log.info("验证成功：修改店铺名,操作人员验证成功")
            # 获取区域列表
            resultdata = RequestMethod(
                dev_manage.test_querylist_region, header=global_header_auth
            ).get_method()
            for i in range(0, len(resultdata["data"])):
                if resultdata["data"][i]["name"] == account.add_region:
                    log.info("验证成功：区域列表查询正确")
                else:
                    pass
        except Exception as e:
            log.error("Error:%s" % e)

    # 新增推送地址 & 全量推送
    def test_all_push(self):
        # pytest.skip('skip test_data_push')
        global global_token, global_header_auth
        try:
            # 全量推送
            data1 = {"full": 1}
            resultdata = RequestMethod(
                dev_manage.test_push_modify_shop, data1, token=global_token[0]
            ).post_method()
            assert resultdata["code"] == 1
            assert len(resultdata["data"]) != 0
            log.info("验证成功：全量推送")
        except Exception as e:
            log.error("Error:%s" % e)

    # 获取检测类型 & 获取可关联的盒子列表
    def test_other_info(self):
        # pytest.skip('skip test_other_info')
        global global_data, global_header_auth
        resultdata = RequestMethod(
            dev_manage.test_detect_type, header=global_header_auth
        ).get_method()
        try:
            # 获取检测类型
            expect_result = {"code": 1, "data": account.detect_type, "msg": "success"}
            assert resultdata == expect_result
            # 获取可关联的盒子
            resultdata = RequestMethod(
                dev_manage.test_no_relation_box, header=global_header_auth
            ).get_method()
            assert resultdata["code"] == 1
            assert len(resultdata["data"]) != 0
            if account.box_init_id in resultdata["data"]:
                log.info("验证成功：待关联的盒子可进行绑定")
            else:
                log.error("失败：请检查配置文件中的盒子是否正常或初始化完成并处于未关联状态")
        except Exception as e:
            log.error("Error:%s" % e)

    # 新增6个摄像头
    @pytest.mark.parametrize("data,expect_val,message", data.add_camera)
    def test_camera(self, data, expect_val, message):
        # pytest.skip('skip test_camera')
        global global_shop_id, global_token
        params = {
            "shopId": global_shop_id[1],
            "name": account.camera_name + str(random.randint(0, 20)),
            ("stream_path", "$"): account.rtsp1,
            "stream_path": account.rtsp2,
            ("stream_path", "$$$"): account.rtsp3,
        }
        resultdata = RequestMethod(
            dev_manage.test_add_camera + str(global_shop_id[1]),
            data,
            params,
            token=global_token[1],
        ).post_method()
        try:
            if resultdata["code"] == 1:
                assert resultdata["msg"] == "success"
                assert len(resultdata["data"]) != 0
                global_camera_id.append(resultdata["data"]["id"])
                log.info(message)
            else:
                log.info("失败：新增摄像头失败,请排查")
        except Exception as e:
            log.error("Error:%s" % e)

    # 测试摄像头并发操作 - (一个店铺只可新增7个摄像头) & 查询指定摄像头 & 摄像头的编辑 & 摄像头列表查询(摄像头当前状态判断)
    @pytest.mark.parametrize("data,expect_val,message", data.add_camera_seven)
    def test_camera_seven(self, data, expect_val, message):
        # pytest.skip('skip test_camera_seven')
        global global_shop_id, global_camera_id, global_token, global_data, global_header_auth

        # 操作人员验证：
        operator = self.query_one_shop(
            global_shop_id[1], account.add_region, global_token[1]
        )
        assert operator == account.re_user
        log.info("验证成功：新增摄像头,操作人员验证成功")

        params = {
            "shopId": global_shop_id[1],
            "name": account.camera_name + str(random.randint(0, 20)),
            "stream_path": account.rtsp2,
        }
        user_resultdata = RequestMethod(
            dev_manage.test_add_camera + str(global_shop_id[1]),
            data,
            params,
            token=global_token[1],
        ).post_method()
        admin_resultdata = RequestMethod(
            dev_manage.test_add_camera + str(global_shop_id[1]),
            data,
            params,
            token=global_token[0],
        ).post_method()

        try:
            admin_expect_result = {"code": 0, "data": {}, "msg": "店铺摄像头已添加至最大值"}
            assert user_resultdata["code"] == 1
            assert user_resultdata["msg"] == "success"
            global_camera_id.append(user_resultdata["data"]["id"])
            assert admin_resultdata == admin_expect_result
            log.info(message)
            # 查询指定摄像头
            resultdata = RequestMethod(
                dev_manage.test_query_camera
                + str(global_shop_id[1])
                + "/"
                + str(global_camera_id[6]),
                header=global_header_auth,
            ).get_method()
            assert resultdata["code"] == 1
            # 摄像头编辑
            data = [
                {
                    "id": str(global_shop_id[1]) + "/" + str(global_camera_id[0]),
                    "data": {"name": account.camera_name + "666"},
                },
                {
                    "id": str(global_shop_id[1]) + "/" + str(global_camera_id[0]),
                    "data": {"fps": 0.1},
                },
                {
                    "id": str(global_shop_id[1]) + "/" + str(global_camera_id[0]),
                    "data": {"stream_path": account.rtsp1},
                },
                {
                    "id": str(global_shop_id[1]) + "/" + str(global_camera_id[0]),
                    "data": {"check_type": [1, 2]},
                },
            ]
            account_number = [0, 1, 0, 1]
            account_name = [
                account.admin_user,
                account.re_user,
                account.admin_user,
                account.re_user,
            ]
            for i in range(0, 4):
                resultdata = RequestMethod(
                    dev_manage.test_query_camera,
                    data[i],
                    token=global_token[account_number[i]],
                ).patch_method()
                expect_result = {"code": 1, "msg": "success"}
                assert resultdata == expect_result
                log.info("验证成功：摄像头编辑成功")
                # 操作人员验证：
                operator = self.query_one_shop(
                    global_shop_id[1],
                    account.add_region,
                    global_token[account_number[i]],
                )
                assert operator == account_name[i]
                log.info("验证成功：当修改摄像头,操作人员验证成功")
                # 增量推送验证
                push_result = self.part_push(global_token[0])
                if i == 0:
                    assert (
                        push_result["data"][0]["camera_list"][6]["camera_name"]
                        == account.camera_name + "666"
                    )
                elif i == 1:
                    assert push_result["data"][0]["camera_list"][6]["fps"] == 0.1
                elif i == 2:
                    assert (
                        push_result["data"][0]["camera_list"][6]["stream_path"]
                        == account.rtsp1
                    )
                elif i == 3:
                    assert push_result["data"][0]["camera_list"][6]["task_type"] == [
                        "hat",
                        "cloth",
                    ]
                else:
                    log.error("失败：请排查")
            log.info("验证成功:修改摄像头名 and fps and rtsp and 检测类型,操作人员校验")
            log.info("验证成功:修改摄像头名 and fps and rtsp and 检测类型,增量校验")
            # 摄像头列表查询(摄像头当前状态判断)
            resultdata = RequestMethod(
                dev_manage.test_querylist_camera + str(global_shop_id[1]),
                global_data,
                header=global_header_auth,
            ).get_method()
            assert resultdata["code"] == 1
            assert resultdata["num"] == 7
            assert resultdata["data"][0]["stream_path"] == account.rtsp2
            assert resultdata["data"][0]["monitor_status"] == 2  # 待检测
            log.info("验证成功：摄像头列表查询(摄像头当前状态判断)")
        except Exception as e:
            log.error("Error:%s" % e)

    # 获取指定店铺id关联的盒子列表 & 查询指定盒子 & 店铺关联盒子(多用户盒子关联) & 获取店铺关联的盒子列表 & 查询指定盒子(状态监控) & 获取店铺关联盒子列表 & 获取店铺列表
    def test_box_conn_shop(self):
        # pytest.skip('skip test_box_conn_shop')
        global global_shop_id, global_header_auth, global_token
        # 获取指定店铺id关联的盒子列表
        expect_val = {
            "code": 1,
            "data": {"bound": [], "normal": []},
            "msg": "success",
        }  # bound - 关联中  normal - 已关联
        resultdata = RequestMethod(
            dev_manage.test_shop_associate_box + str(global_shop_id[1]),
            header=global_header_auth,
        ).get_method()
        assert resultdata == expect_val
        log.info("验证成功：店铺%s当前状态下没有关联中和已关联的盒子" % global_shop_id[1])
        # 查询指定盒子
        resultdata = RequestMethod(
            dev_manage.test_query_box + str(account.box_init_id),
            header=global_header_auth,
        ).get_method()
        try:
            if (
                resultdata["data"]["init_status"] == 1
                and resultdata["data"]["monitor_status"] == 1
                and resultdata["data"]["relation_status"] == 0
            ):
                log.info("验证成功：盒子%s处于初始化完成,并且正常,可关联店铺" % account.box_init_id)

                # 店铺关联盒子 -(普通用户) - 关联成功后需要监控盒子的状态和店铺的状态
                data = {
                    "box": account.box_init_id,
                    "shop": global_shop_id[1],
                    "task_code": 20007,
                }
                resultdata = RequestMethod(
                    dev_manage.test_task_run, data, token=global_token[0]
                ).post_method()
                assert resultdata["code"] == 1
                assert resultdata["msg"] == "success"
                # 多用户关联盒子 - (超管)
                resultdata = RequestMethod(
                    dev_manage.test_task_run, data, token=global_token[1]
                ).post_method()
                expect_val = {"code": 0, "msg": "店铺已关联盒子请刷新界面"}
                assert resultdata == expect_val
                # 操作人员验证：
                operator = self.query_one_shop(
                    global_shop_id[1], account.add_region, global_token[0]
                )
                assert operator == account.admin_user
                log.info("验证成功:关联盒子时,操作人员校验")
                # 获取店铺关联盒子列表
                expect_val = {
                    "code": 1,
                    "data": {"bound": [account.box_init_id], "normal": []},
                    "msg": "success",
                }
                resultdata = RequestMethod(
                    dev_manage.test_shop_associate_box + str(global_shop_id[1]),
                    header=global_header_auth,
                ).get_method()
                assert resultdata == expect_val
                # 查询指定盒子,进行关联状态监控
                execute = True
                while execute == True:
                    resultdata = RequestMethod(
                        dev_manage.test_query_box + str(account.box_init_id),
                        header=global_header_auth,
                    ).get_method()
                    if (
                        resultdata["data"]["init_status"] == 1
                        and resultdata["data"]["monitor_status"] == 1
                    ):
                        if resultdata["data"]["relation_status"] == 2:
                            log.info(
                                "验证中:盒子%s正在关联店铺%s中,请等候"
                                % (account.box_init_id, global_shop_id[1])
                            )
                            time.sleep(5)
                            continue
                        elif resultdata["data"]["relation_status"] == 1:
                            # time.sleep(3)
                            # 获取店铺关联盒子列表
                            expect_val = {
                                "code": 1,
                                "data": {"bound": [], "normal": [account.box_init_id]},
                                "msg": "success",
                            }
                            resultdata = RequestMethod(
                                dev_manage.test_shop_associate_box
                                + str(global_shop_id[1]),
                                header=global_header_auth,
                            ).get_method()
                            assert resultdata == expect_val
                            # 获取店铺列表,进行监控状态校验
                            data = {
                                "page": 1,
                                "page_size": 10,
                                "sort_type": "desc",
                                "check_code": 0,
                            }
                            resultdata = RequestMethod(
                                dev_manage.test_querylist_shop,
                                data,
                                token=global_token[1],
                            ).post_method()
                            for i in range(0, len(resultdata["data"])):
                                if resultdata["data"][i]["id"] == global_shop_id[1]:
                                    assert (
                                        resultdata["data"][i]["monitor_info"][
                                            "api_status"
                                        ]
                                        == 2
                                    )
                                    assert (
                                        resultdata["data"][i]["monitor_info"][
                                            "api_time"
                                        ]
                                        == "-1"
                                    )
                                    # assert resultdata['data'][i]['monitor_info']["camera_status"] == 1
                                    assert (
                                        resultdata["data"][i]["monitor_info"][
                                            "monitor_code"
                                        ]
                                        == 1
                                    )
                                    log.info("验证成功：店铺列表监控状态正常")
                                else:
                                    pass
                            log.info(
                                "验证成功: 盒子%s关联店铺%s成功"
                                % (account.box_init_id, global_shop_id[1])
                            )
                            break
                        else:
                            log.error(
                                "失败：盒子%s关联店铺%s过程中出现其他异常,请检查"
                                % (account.box_init_id, global_shop_id[1])
                            )
                            break
                    else:
                        log.error("失败：在关联过程中盒子状态异常,请检查")
                        break
            else:
                log.error("失败：待关联的盒子%s状态异常,无法进行关联，请检查" % account.box_init_id)
        except Exception as e:
            log.error("Error:%s" % e)

    # 添加合规服饰类型(三个摄像头下分别添加2种服饰类型) & 获取合规服饰列表 & 修改合规服饰类型(验证不可修改相同的服饰名和新增)
    def test_add_clothes_type(self):
        # pytest.skip('skip test_add_clothes_type')
        global global_shop_id, global_camera_id, global_header_auth, global_token, clothes_type_id
        try:
            expect_result = {"code": 1, "msg": "操作成功"}
            for i in range(0, 3):
                for j in range(0, 2):
                    data = {"name": account.clothes_type_name + str(j)}
                    resultdata = RequestMethod(
                        dev_manage.test_add_clothes_type
                        + str(global_shop_id[1])
                        + "/"
                        + str(global_camera_id[i]),
                        data,
                        token=global_token[1],
                    ).post_method()
                    assert resultdata["code"] == 1
                    assert resultdata["msg"] == "操作成功"
                    clothes_type_id.append(resultdata["cloth_type_id"])
            log.info("验证成功: 成功在三个摄像头下分别新增2个服装类型")
            # 操作人员验证：
            operator = self.query_one_shop(
                global_shop_id[1], account.add_region, global_token[1]
            )
            assert operator == account.re_user
            log.info("验证成功:新增合规服饰时,操作人员校验")
        except Exception as e:
            log.error("Error:%s" % e)
        try:
            # 获取合规服饰列表
            resultdata = RequestMethod(
                dev_manage.test_add_clothes_type
                + str(global_shop_id[1])
                + "/"
                + str(global_camera_id[0]),
                header=global_header_auth,
            ).get_method()
            assert resultdata["code"] == 1
            assert len(resultdata["data"]) == 2
            cloth_id = resultdata["data"][0]["id"]
            cloth_name = resultdata["data"][0]["name"]
            log.info("验证成功: 成功验证获取合规服饰列表")
            # 验证不可新增相同的服饰名
            data = {"name": cloth_name}
            expect_result = {"code": 0, "msg": "该合规类型已存在"}
            resultdata = RequestMethod(
                dev_manage.test_add_clothes_type
                + str(global_shop_id[1])
                + "/"
                + str(global_camera_id[0]),
                data,
                token=global_token[1],
            ).post_method()
            assert resultdata == expect_result
            log.info("验证成功: 验证不可新增相同的服饰名")
            # 修改同名合规服饰类型 & 修改合合规服饰名称
            data_cloth_name = [cloth_name, cloth_name + "y"]
            expect_result1 = {"code": 0, "msg": "修改失败,合规服饰类型名已经存在"}
            expect_result2 = {"code": 1, "msg": "操作成功"}
            for i in range(0, 2):
                data = {
                    "id": str(global_shop_id[1]) + "/" + str(global_camera_id[0]),
                    "data": {"clothes_type_id": cloth_id, "name": data_cloth_name[i]},
                }
                resultdata = RequestMethod(
                    dev_manage.test_add_clothes_type, data, token=global_token[1]
                ).patch_method()
                if i == 0:
                    assert resultdata == expect_result1
                    log.info("验证成功: 不可修改为同名合规服饰类型")
                elif i == 1:
                    assert resultdata == expect_result2
                    log.info("验证成功: 修改合合规服饰名称成功")
                else:
                    log.error("失败：修改合规服饰的验证失败,请检查")
        except Exception as e:
            log.error("Error:%s" % e)

    # 将每个摄像头下的第一个合规服饰上传两张图片(?)
    def test_add_picture(self):
        # pytest.skip('skip test_add_picture')
        global global_shop_id, global_camera_id, clothes_type_id, global_header_auth, global_token
        try:
            header = {
                # "Content-Type": "application/x-www-form-urlencoded", # 不可添加
                "Authorization": global_token[0]
            }
            # 对数组进行拆分，拆分成五维数组
            cycle_cloth_type_id = np.array(clothes_type_id)
            cycle_clothes_type_id = cycle_cloth_type_id.reshape((3, 2))
            for i in range(0, len(cycle_clothes_type_id)):
                data = {
                    "file_parameter": [
                        '{"size": 12367, "timestamp": 1081681636001}',
                        '{"size": 12345, "timestamp": 1081681636221}',
                    ],
                    "add_img_cloth_type_id": [
                        account.img_path + account.img_1jpg,
                        account.img_path + account.img_1jpg,
                    ],
                }
                expect_result = {"code": 1, "msg": "操作成功"}
                resultdata = RequestMethod(
                    dev_manage.test_add_picture
                    + str(global_shop_id[1])
                    + "/"
                    + str(global_camera_id[i])
                    + "/"
                    + str(cycle_clothes_type_id[i][0]),
                    data,
                    header=header,
                ).post_file_method()
                assert resultdata == expect_result
                log.info("验证成功：为摄像头%s下的合规服饰上传2张" % global_camera_id[i])
            # 操作人员验证：
            operator = self.query_one_shop(
                global_shop_id[1], account.add_region, global_token[0]
            )
            assert operator == account.admin_user
            log.info("验证成功:合规服饰图片上传时,操作人员校验")
        except Exception as e:
            log.error("Error:%s" % e)

    # 新增api地址 & 获取所有的API地址 & 获取历史上报地址列表 & API进行检测 & 获取任务执行结果 & 店铺列表进行监控 & 应用到盒子
    def test_api_check(self):
        # pytest.skip('skip test_api_check')
        global global_token, global_header_auth, global_shop_id
        try:
            # 新增api地址
            request_data = {
                "id": global_shop_id[1],
                "data": {"api_addr": account.api_address},
            }
            expect_val = {"code": 1, "msg": "success"}
            resultdata = RequestMethod(
                dev_manage.test_query_shop, request_data, token=global_token[1]
            ).patch_method()
            assert resultdata == expect_val
            log.info("验证成功：新增api地址")
            # 获取所有的API地址
            resultdata = RequestMethod(
                dev_manage.test_api_address, global_data, header=global_header_auth
            ).get_method()
            assert resultdata["code"] == 1
            assert len(resultdata["data"]) != 0
            if account.api_address in resultdata["data"]:
                log.info("验证成功: 获取到最新的API地址列表")
            else:
                log.error("失败: 获取的API地址列表中无新增的API地址")
            # 操作人员验证：
            operator = self.query_one_shop(
                global_shop_id[1], account.add_region, global_token[1]
            )
            assert operator == account.re_user
            log.info("验证成功：当新增 and 修改API地址,操作人员验证成功")
            # 增量推送验证
            push_result = self.part_push(global_token[0])
            assert push_result["data"][0]["api"] == account.api_address
            log.info("验证成功：修改API地址,增量推送验证成功")

            # 获取历史上报地址列表
            resultdata = RequestMethod(
                dev_manage.test_api_address_history, header=global_header_auth
            ).get_method()
            for i in range(0, len(resultdata["data"])):
                if resultdata["data"][i] == account.api_address:
                    log.info("验证成功：成功获取历史上报地址列表")
                else:
                    pass
            # 拉取配置(20001)
            data = {"box": account.box_init_id, "task_code": 20001}
            resultdata = RequestMethod(
                dev_manage.test_task_run, data, token=global_token[1]
            ).post_method()
            assert resultdata["code"] == 1
            assert resultdata["msg"] == "success"
            # API检测
            data = {"box": account.box_init_id, "mark": 1, "task_code": 20004}
            resultdata = RequestMethod(
                dev_manage.test_task_run, data, token=global_token[1]
            ).post_method()
            assert resultdata["code"] == 1
            assert resultdata["msg"] == "success"
            task_id = resultdata["task_id"]
            # 获取任务执行结果
            execute = True
            while execute == True:
                resultdata = RequestMethod(
                    dev_manage.test_task_result + str(task_id),
                    header=global_header_auth,
                ).get_method()
                # result_info = eval(resultdata['data']['info'])
                if (
                    resultdata["data"]["info"] == "执行中"
                    and resultdata["data"]["result"] == 0
                ):
                    log.info("检测中：API在检测中,请等待")
                    time.sleep(6)
                    continue
                elif resultdata["data"]["result"] == 1:
                    result_info = eval(resultdata["data"]["info"])
                    assert result_info["message"] == "success"
                    data = {
                        "page": 1,
                        "page_size": 10,
                        "sort_type": "desc",
                        "check_code": 0,
                    }
                    resultdata = RequestMethod(
                        dev_manage.test_querylist_shop, data, token=global_token[1]
                    ).post_method()
                    for i in range(0, len(resultdata["data"])):
                        if resultdata["data"][i]["id"] == global_shop_id[1]:
                            assert (
                                resultdata["data"][i]["monitor_info"]["api_status"] == 1
                            )
                            assert (
                                resultdata["data"][i]["monitor_info"]["api_time"] != -1
                            )
                            # assert resultdata['data'][i]['monitor_info']["camera_status"] == 0
                            assert (
                                resultdata["data"][i]["monitor_info"]["monitor_code"]
                                == 1
                            )
                            log.info("验证成功：店铺列表监控状态正常")
                        else:
                            pass
                    log.info("验证完成：API检测成功")
                    break
                elif resultdata["data"]["result"] == -1:
                    data = {
                        "page": 1,
                        "page_size": 10,
                        "sort_type": "desc",
                        "check_code": 0,
                    }
                    resultdata = RequestMethod(
                        dev_manage.test_querylist_shop, data, token=global_token[1]
                    ).post_method()
                    for i in range(0, len(resultdata["data"])):
                        if resultdata["data"][i]["id"] == global_shop_id[1]:
                            assert (
                                resultdata["data"][i]["monitor_info"]["api_status"] == 0
                            )
                            assert (
                                resultdata["data"][i]["monitor_info"]["api_time"] != -1
                            )
                            # assert resultdata['data'][i]['monitor_info']["camera_status"] == 0
                            assert (
                                resultdata["data"][i]["monitor_info"]["monitor_code"]
                                == 1
                            )
                            log.info("验证成功：店铺列表监控状态正常")
                        else:
                            pass
                    log.info("验证完成：API检测失败")
                    break
                else:
                    log.error("失败：在进行API检测的过程中,出现异常,请检查")
                    break

            # 应用到盒子
            data = {
                "box": account.box_init_id,
                "mark": 1,
                "task_code": 20005,
                "shop": global_shop_id[1],
            }
            resultdata = RequestMethod(
                dev_manage.test_task_run, data, token=global_token[0]
            ).post_method()
            assert resultdata["code"] == 1
            assert resultdata["msg"] == "success"
            while execute == True:
                resultdata = RequestMethod(
                    dev_manage.test_task_result + str(task_id),
                    header=global_header_auth,
                ).get_method()
                if (
                    resultdata["data"]["info"] == "执行中"
                    and resultdata["data"]["result"] == 0
                ):
                    log.info("检测中：上报结果类型应用到盒子中,请等待")
                    time.sleep(6)
                    continue
                elif resultdata["data"]["result"] == 1:
                    result_info = eval(resultdata["data"]["info"])
                    assert result_info["message"] == "success"
                    log.info("验证完成：成功应用到盒子")
                    break
                elif resultdata["data"]["result"] == -1:
                    data = {
                        "page": 1,
                        "page_size": 10,
                        "sort_type": "desc",
                        "check_code": 0,
                    }
                    log.info("验证完成：应用到盒子失败")
                    break
                else:
                    log.error("失败：在应用到盒子的过程中,出现异常,请检查")
                    break
            # 操作人员验证：
            operator = self.query_one_shop(
                global_shop_id[1], account.add_region, global_token[0]
            )
            assert operator == account.admin_user
            log.info("验证成功：上报类型应用到盒子,操作人员验证成功")
        except Exception as e:
            log.error("Error:%s" % e)

    # 摄像头状态(店铺列表)检测 & 摄像头抓拍检测 & 触发20001(拉取配置) & 拉取合规服饰(20003)
    def test_camera_check(self):
        # pytest.skip('skip test_camera_check')
        global global_shop_id, global_camera_id, global_data, global_header_auth, global_token
        # 摄像头状态(店铺列表)检测
        try:
            execute = True
            while execute == True:
                end = 0
                resultdata = RequestMethod(
                    dev_manage.test_querylist_camera + str(global_shop_id[1]),
                    global_data,
                    header=global_header_auth,
                ).get_method()
                execute = False
                for i in range(0, 7):
                    if (resultdata["data"][i]["monitor_status"]) == 1:
                        log.info("摄像头状态验证中：摄像头%s状态正常" % resultdata["data"][i]["id"])
                        end = end + 1
                        if end == 7:
                            log.info("验证成功：摄像头状态全部正常")
                            # 店铺列表检测
                            data = {
                                "page": 1,
                                "page_size": 10,
                                "sort_type": "desc",
                                "check_code": 0,
                            }
                            resultdata = RequestMethod(
                                dev_manage.test_querylist_shop,
                                data,
                                token=global_token[1],
                            ).post_method()
                            for j in range(0, len(resultdata["data"])):
                                if resultdata["data"][j]["id"] == global_shop_id[1]:
                                    assert (
                                        resultdata["data"][j]["monitor_info"][
                                            "camera_status"
                                        ]
                                        == 1
                                    )
                                    log.info("验证成功：店铺列表监控状态正常")
                                else:
                                    pass
                            execute = False
                    elif (resultdata["data"][i]["monitor_status"]) == 0:
                        log.warning("摄像头%s状态断开,请检查" % i)
                        time.sleep(5)
                    elif (resultdata["data"][i]["monitor_status"]) == 3:
                        log.warning("摄像头%s检测中" % i)
                        time.sleep(2)
                    else:
                        log.error("失败：摄像头状态查询失败,请检查")
                        execute = False
        except Exception as e:
            log.error("Error:%s" % e)
        try:
            # 摄像头抓拍检测
            task_id = []
            for i in range(0, 3):
                rtsp = [account.rtsp1, account.rtsp2, account.rtsp3]
                data = {
                    "box": account.box_init_id,
                    "camera": global_camera_id[i],
                    "mark": rtsp[i],
                    "task_code": 20002,
                }
                resultdata = RequestMethod(
                    dev_manage.test_task_run, data, token=global_token[1]
                ).post_method()
                assert resultdata["code"] == 1
                assert resultdata["msg"] == "success"
                task_id.append(resultdata["task_id"])
            log.info("验证成功：摄像头检测任务已发起")
            # 任务查询：
            for i in range(0, len(task_id)):
                execute = True
                while execute == True:
                    resultdata = RequestMethod(
                        dev_manage.test_task_result + str(task_id[i]),
                        header=global_header_auth,
                    ).get_method()
                    if (
                        resultdata["data"]["info"] == "执行中"
                        and resultdata["data"]["result"] == 0
                    ):
                        log.info("检测中：抓拍检测中,请等待")
                        time.sleep(5)
                        continue
                    elif (
                        resultdata["data"]["info"] == "success"
                        and resultdata["data"]["result"] == 1
                    ):
                        log.info("验证完成：RTSP(%s)抓拍完成" % rtsp[i])
                        break
                    else:
                        log.info("失败：RTSP(%s)抓拍异常,请检查" % rtsp[i])
                        break

            # 拉取配置(20001)
            data = {"box": account.box_init_id, "task_code": 20001}
            resultdata = RequestMethod(
                dev_manage.test_task_run, data, token=global_token[1]
            ).post_method()
            assert resultdata["code"] == 1
            assert resultdata["msg"] == "success"
            time.sleep(5)
            # 拉取合规服饰(20003)
            data = {"box": account.box_init_id, "task_code": 20003}
            resultdata = RequestMethod(
                dev_manage.test_task_run, data, token=global_token[1]
            ).post_method()
            assert resultdata["code"] == 1
            assert resultdata["msg"] == "success"
        except Exception as e:
            log.error("Error:%s" % e)

    # 查询指定店铺
    def test_shop_monitoring(self):
        # pytest.skip('skip test_shop_monitoring')
        global global_shop_id
        try:
            resultdata = RequestMethod(
                dev_manage.test_query_shop + str(global_shop_id[1]),
                header=global_header_auth,
            ).get_method()
            assert resultdata["code"] == 1
            assert resultdata["data"]["api_addr"] == account.api_address
            assert resultdata["data"]["box_apply_status"] == 1
            assert resultdata["data"]["init_api_status"] == 1
            assert resultdata["data"]["init_camera_status"] == 1
            assert resultdata["data"]["init_cloth_status"] == 1
            assert resultdata["data"]["monitor_info"]["api_status"] == 1
            assert resultdata["data"]["monitor_info"]["camera_status"] == 1
            assert resultdata["data"]["monitor_info"]["monitor_code"] == 1
            assert resultdata["data"]["relation_box_status"] == 1
            log.info("验证成功:店铺部署成功")
        except Exception as e:
            log.error("Error:%s" % e)

    # 店铺概览模糊查询
    @pytest.mark.parametrize("data,expect_val,message", data.shop_query)
    def test_shop_query(self, data, expect_val, message):
        # pytest.skip('skip test_shop_query')
        try:
            # 店铺概览模糊查询
            params = {"key_word": global_shop_id[1], "region": account.add_region}
            resultdata = RequestMethod(
                dev_manage.test_querylist_shop, data, params, token=global_token[1]
            ).post_method()
            if resultdata["num"] == 1:
                assert len(resultdata["data"]) == 1
                log.info(message)
            elif resultdata["num"] == 0:
                assert resultdata == expect_val
                log.info(message)
            else:
                log.error("模糊查询异常，请排查")
        except Exception as e:
            log.error("Error:%s" % e)

    # 删除店铺,删除盒子,店铺中解绑盒子,删除店铺,删除合规服饰,删除摄像头下指定一张合规服饰,删除摄像头,删除店铺,重新初始化盒子,查询盒子状态,删除盒子,修改硬件管理系统地址,删除普通用户,普通用户登录
    def test_del(self):
        # pytest.skip('skip test_del')
        global global_shop_id, glocal_box_id, global_camera_id, global_header_auth, global_user_id
        try:
            # 删除店铺
            expect_val = {"code": 0, "msg": "店铺下有盒子未解绑,不能删除该店铺"}
            resultdata = RequestMethod(
                dev_manage.test_query_shop + str(global_shop_id[1]),
                header=global_header_auth,
            ).del_method()
            assert resultdata == expect_val
            log.info("验证完成：当店铺下存在盒子时,店铺不允许删除")
            # 删除盒子
            expect_val = {"code": 0, "msg": "盒子未解绑店铺不能删除"}
            resultdata = RequestMethod(
                dev_manage.test_query_box + str(account.box_init_id),
                header=global_header_auth,
            ).del_method()
            assert resultdata == expect_val
            log.info("验证完成：当盒子关联店铺时,盒子无法被删除")
            # 店铺中解绑盒子
            data = {
                "box": account.box_init_id,
                "shop": global_shop_id[1],
                "task_code": 20006,
            }
            resultdata = RequestMethod(
                dev_manage.test_task_run, data, token=global_token[1]
            ).post_method()
            assert resultdata["code"] == 1
            assert resultdata["msg"] == "success"
            log.info("验证完成：下发解绑盒子任务,店铺解绑了盒子")
            # 操作人员验证：
            operator = self.query_one_shop(
                global_shop_id[1], account.add_region, global_token[1]
            )
            assert operator == account.re_user
            log.info("验证成功：解绑盒子,操作人员验证成功")
            # 监控状态查询
            data = {"page": 1, "page_size": 10, "sort_type": "desc", "check_code": 0}
            resultdata = RequestMethod(
                dev_manage.test_querylist_shop, data, token=global_token[1]
            ).post_method()
            for i in range(0, len(resultdata["data"])):
                if resultdata["data"][i]["id"] == global_shop_id[1]:
                    assert resultdata["data"][i]["monitor_info"]["api_status"] == 2
                    assert resultdata["data"][i]["monitor_info"]["api_time"] == "-1"
                    assert resultdata["data"][i]["monitor_info"]["camera_status"] == -1
                    assert resultdata["data"][i]["monitor_info"]["monitor_code"] == -1
                    log.info("验证成功：店铺列表监控状态正常")
                else:
                    pass
            log.info("验证完成：店铺解绑盒子后,盒子状态【未关联】,摄像头/接口【待检测】")
            # 删除店铺
            expect_val = {"code": 0, "msg": "店铺下存在摄像头,不能删除该店铺"}
            resultdata = RequestMethod(
                dev_manage.test_query_shop + str(global_shop_id[1]),
                header=global_header_auth,
            ).del_method()
            assert resultdata == expect_val
            log.info("验证完成：当店铺下存在摄像头时,店铺不可被删除")
        except Exception as e:
            log.error("Error:%s" % e)
        try:
            img_id = []
            # 合规服饰查询,获取到合规服饰id和pic_id
            for i in range(0, len(global_camera_id)):
                resultdata = RequestMethod(
                    dev_manage.test_add_clothes_type
                    + str(global_shop_id[1])
                    + "/"
                    + str(global_camera_id[i]),
                    header=global_header_auth,
                ).get_method()
                if len(resultdata["data"]) > 0:
                    for j in range(0, len(resultdata["data"])):
                        if len(resultdata["data"][j]["src"]) != 0:
                            for k in range(len(resultdata["data"][j]["src"])):
                                img_id.append(resultdata["data"][j]["src"][k]["pic_id"])
                            # 删除摄像头下指定一张合规服饰
                            data = {"pic_id_list": img_id}
                            expect_val = {"code": 1, "msg": "操作成功"}
                            resultdata_pic = RequestMethod(
                                dev_manage.test_del_picture
                                + str(global_shop_id[1])
                                + "/"
                                + str(global_camera_id[i]),
                                data,
                                token=global_token[1],
                            ).del_method()
                            assert resultdata_pic == expect_val
                            # 删除合规服饰
                            expect_val = {"code": 1, "msg": "操作成功"}
                            data = {"clothes_type_id": resultdata["data"][k]["id"]}
                            resultdata_cloth = RequestMethod(
                                dev_manage.test_add_clothes_type
                                + str(global_shop_id[1])
                                + "/"
                                + str(global_camera_id[i]),
                                data,
                                token=global_token[1],
                            ).del_method()
                            assert resultdata_cloth == expect_val
                            # 操作人员验证：
                            operator = self.query_one_shop(
                                global_shop_id[1], account.add_region, global_token[1]
                            )
                            assert operator == account.re_user
                        else:
                            # 删除合规服饰
                            expect_val = {"code": 1, "msg": "操作成功"}
                            data = {"clothes_type_id": resultdata["data"][j]["id"]}
                            resultdata_cloth = RequestMethod(
                                dev_manage.test_add_clothes_type
                                + str(global_shop_id[1])
                                + "/"
                                + str(global_camera_id[i]),
                                data,
                                token=global_token[0],
                            ).del_method()
                            assert resultdata_cloth == expect_val
                            # 操作人员验证：
                            operator = self.query_one_shop(
                                global_shop_id[1], account.add_region, global_token[0]
                            )
                            assert operator == account.admin_user
                    log.info("验证成功：删除合规服饰,操作人员验证成功")
                    log.info("验证成功: 成功删除摄像头%s下合规服饰以及合规服饰下的图片集" % global_camera_id[i])
                    # 删除摄像头
                    expect_val = {"code": 1, "msg": "success"}
                    resultdata_camera = RequestMethod(
                        dev_manage.test_query_camera
                        + str(global_shop_id[1])
                        + "/"
                        + str(global_camera_id[i]),
                        header=global_admin_header_auth,
                    ).del_method()
                    assert resultdata_camera == expect_val
                    log.info("验证完成：成功删除摄像头%s" % global_camera_id[i])
                else:
                    # 删除摄像头
                    expect_val = {"code": 1, "msg": "success"}
                    resultdata_camera = RequestMethod(
                        dev_manage.test_query_camera
                        + str(global_shop_id[1])
                        + "/"
                        + str(global_camera_id[i]),
                        header=global_admin_header_auth,
                    ).del_method()
                    assert resultdata_camera == expect_val
                    log.info("验证完成：成功删除摄像头%s" % global_camera_id[i])

            # 操作人员验证：
            operator = self.query_one_shop(
                global_shop_id[1], account.add_region, global_token[0]
            )
            assert operator == account.admin_user
            log.info("验证成功：删除摄像头,操作人员验证成功")
            # 增量推送
            push_result = self.part_push(global_token[0])
            assert push_result["data"][0]["camera_list"][0]["delete"] == 1
            log.info("验证成功：删除摄像头,增量推送验证成功")
            # 删除店铺
            expect_val = {"code": 1, "msg": "success"}
            for i in range(0, len(global_shop_id)):
                resultdata = RequestMethod(
                    dev_manage.test_query_shop + str(global_shop_id[i]),
                    header=global_header_auth,
                ).del_method()
                assert resultdata == expect_val
                log.info("验证完成：成功删除新增店铺%s" % global_shop_id[i])
            # 增量推送
            push_result = self.part_push(global_token[0])
            assert push_result["data"][0]["delete"] == 1
            log.info("验证成功：删除店铺,增量推送验证成功")
            # 重新初始化盒子
            data = {"init_status": 0, "relation_status": 0, "shop": 0, "name": 12}
            data = {
                "id": account.box_init_id,
                "data": {
                    "init_status": 0,
                    "relation_status": 0,
                    "shop": 0,
                    "name": None,
                },
            }
            resultdata = RequestMethod(
                dev_manage.test_query_box, data, token=global_token[1]
            ).patch_method()
            expect_result = {"code": 1, "msg": "success"}
            assert resultdata == expect_result
            log.info("验证完成：重新初始化盒子%s成功" % account.box_init_id)
            # 查询盒子状态
            data = {
                "page": 1,
                "page_size": 10,
                "key_word": glocal_box_id,
                "sort_name": "id",
                "sort_type": "desc",
            }
            resultdata = RequestMethod(
                dev_manage.test_querylist_box, data, token=global_token[1]
            ).post_method()
            for i in range(len(resultdata["data"])):
                if resultdata["data"][i]["id"] == account.box_init_id:
                    assert resultdata["data"][0]["init_status"] == 0
                    assert resultdata["data"][0]["monitor_status"] == 0
                    assert resultdata["data"][0]["relation_status"] == 0
                    log.info("验证成功：盒子%s未初始化" % account.box_init_id)
                else:
                    pass
            # 删除盒子
            expect_val = {"code": 1, "msg": "success"}
            resultdata = RequestMethod(
                dev_manage.test_query_box + str(glocal_box_id),
                header=global_header_auth,
            ).del_method()
            assert resultdata == expect_val
            log.info("验证完成：成功删除新增盒子")
            # 删除普通用户
            expect_val = {"code": 1, "msg": "删除成功"}
            resultdata = RequestMethod(
                dev_manage.test_user + str(global_user_id),
                header=global_admin_header_auth,
            ).del_method()
            assert resultdata == expect_val
            log.info("验证完成：成功删除新增用户")
            # 普通用户登录
            data = {"username": account.re_user, "password": account.admin_pwd}
            expect_val = {"code": 0, "msg": "找不到用户"}
            resultdata = RequestMethod(
                dev_manage.test_login, data, global_header_type
            ).post_method()
            assert resultdata == expect_val
            log.info("验证完成：被删除用户不可再次登录")
        except Exception as e:
            log.error("Error:%s" % e)

    # 增量推送
    def part_push(self, token):
        data = {"full": 0}
        resultdata = RequestMethod(
            dev_manage.test_push_modify_shop, data, token=token
        ).post_method()
        return resultdata

    # 操作人员查询
    def query_one_shop(self, shop_id, region, token):
        # 店铺概览模糊查询
        data = {
            "page": 1,
            "page_size": 10,
            "key_word": shop_id,
            "region": region,
            "sort_type": "desc",
            "check_code": 0,
        }
        resultdata = RequestMethod(
            dev_manage.test_querylist_shop, data, token=token
        ).post_method()
        return resultdata["data"][0]["operate_user"]


if __name__ == "__main__":
    pytest.main(["-s"])
