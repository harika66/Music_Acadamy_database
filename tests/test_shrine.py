import requests
import json
import jsonpath

# def test_add_student():    
#     url = "http://shrine_fastapi:80/user"
# #    user = {"data" : { "std_name": "Pranav1111", "course_name": "guitar", "batch": "string", "tch_name": "string", "fees": 0 }}


#     file = open("/test/add_student.json",'r',encoding='utf-8')
#     json_input = file.read()
#     request_json = json.loads(json_input)
#     print(request_json)
#     response = requests.post(url,request_json)
#     print(response.request.url)
#     print(response.request.headers)
#     print(response.request.body)
#     assert response.status_code == 200    


def test_get_all_students():
    url = "http://shrine_fastapi:80/students"
    response = requests.get(url)
    assert response.status_code == 200
