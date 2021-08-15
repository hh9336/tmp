"""
@Autor: Ann
@Date: 2020-07-09 11:13:00
LastEditTime: 2020-08-20 20:27:22
"""
import json
import requests


class RequestMethod(object):
    def __init__(self, url: str, data=None, param=None, header=None, token=None):
        self._data = data
        self._param = param
        self._url = url
        self._header = header
        self._token = token

    def post_method(self):
        params_header_data = self.common()
        result = requests.post(
            url=self._url,
            headers=params_header_data[0],
            data=json.dumps(params_header_data[1]).encode("utf-8"),
        )
        return result.json()

    # def post_file_method(self):
    #     params_header_data = self.common()
    #     files = {"file":open(params_header_data[1], "rb")}
    #     result = requests.post(url=self._url,headers=params_header_data[0], files=files)
    #     return result.json()

    def post_file_method(self):
        params_header_data = self.common()
        data = {"file_parameter": params_header_data[1]["file_parameter"]}
        files = [
            (
                "files",
                (
                    params_header_data[1]["add_img_cloth_type_id"][0],
                    open(
                        params_header_data[1]["add_img_cloth_type_id"][0], "rb"
                    ).read(),
                ),
            ),
            (
                "files",
                (
                    params_header_data[1]["add_img_cloth_type_id"][1],
                    open(
                        params_header_data[1]["add_img_cloth_type_id"][1], "rb"
                    ).read(),
                ),
            ),
        ]
        result = requests.post(
            url=self._url, headers=params_header_data[0], data=data, files=files
        )
        return result.json()

    def get_method(self):
        params_header_data = self.common()
        if params_header_data[1]:
            result = requests.get(
                url=self._url,
                headers=params_header_data[0],
                params=params_header_data[1],
            )
        else:
            result = requests.get(url=self._url, headers=params_header_data[0])
        return result.json()

    def patch_method(self):
        header_data = self.common()
        result = requests.patch(
            url=self._url + str(self._data["id"]),
            headers=header_data[0],
            data=json.dumps(self._data["data"]).encode("utf-8"),
        )
        return result.json()

    def del_method(self):
        header_data = self.common()
        if header_data[1]:
            result = requests.delete(
                url=self._url,
                headers=header_data[0],
                data=json.dumps(header_data[1]).encode("utf-8"),
            )
        else:
            result = requests.delete(url=self._url, headers=self._header)
        return result.json()

    def common(self):

        if self._header == None:
            header = {"Content-Type": "application/json", "Authorization": self._token}
        else:
            header = self._header

        if self._param:
            for param_key, param_value in self._param.items():
                if type(param_key) == tuple:
                    param_name = param_key[0]
                    param_placeholder = param_key[1]
                else:
                    param_name = param_key
                    param_placeholder = "$$"
                if (
                    param_name in list(self._data.keys())
                    and self._data[param_name] == param_placeholder
                ):
                    self._data[param_name] = param_value

        return header, self._data
