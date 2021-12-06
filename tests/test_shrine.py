import requests
import json
import jsonpath
import names

def test_add_student():
    url = "http://shrine_fastapi:80/user/"
    headers = {'content-type': 'application/json'}
    user = { "std_name": "", "course_name": "guitar", "batch": "string", "tch_name": "string", "fees": 0 }
    user["std_name"] = names.get_full_name()
    print( "Name : ", user["std_name"] )

    response = requests.post(url,data=json.dumps(user), headers = headers)
    print(response.request.url)
    print(response.request.headers)
    print(response.request.body)
    assert response.status_code == 200



def test_get_all_students():
    url = "http://shrine_fastapi:80/students"
    response = requests.get(url)
    assert response.status_code == 200