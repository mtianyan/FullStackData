#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
import json
# import sys

# if __name__ == '__main__':
#     # 将python对象test转换json对象
#     test = {"username":"测试","age":16}
#     print type(test)
#     python_to_json = json.dumps(test,ensure_ascii=False)
#     print python_to_json
#     print type(python_to_json)

#     # 将json对象转换成python对象
#     json_to_python = json.loads(python_to_json)
#     print type(json_to_python)
#     print json_to_python['username']

import json

data ={
    "showapi_res_code": 0,
    "showapi_res_error": "",
    "showapi_res_body": {
        "Result": "bjekdg",
        "ret_code": 0,
        "Id": "8d726a7e-7f7e-418a-8930-56fec272e1b0"
    }
}
json_str = json.dumps(data)
jsonobj = json.loads(json_str)
print jsonobj['showapi_res_body']['Result']