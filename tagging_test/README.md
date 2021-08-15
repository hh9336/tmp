#### Init
 ```
 - PyYAML
 - pytest
 - selenium
 - allure
 - ruamel.yaml
```
 
 
#### 运行方式
    - 运行：pytest testcase/ -s -q --alluredir=./result
    - 生成报告：allure generate ./result -o ./report/ --clean