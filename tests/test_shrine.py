import requests
import json
import jsonpath
import names

def test_add_student():
    url = "http://shrine_fastapi:80/user/"
    headers = {'content-type': 'application/json'}
    user = { "is_student": "true", "is_teacher": "false", "name": "", "email": "ab@gmail.com", "phone": "9999999999" }
    user["name"] = names.get_full_name()
    print( "Name : ", user["name"] )

    response = requests.post(url,data=json.dumps(user), headers = headers)
    print(response.request.url)
    print(response.request.headers)
    print(response.request.body)
    assert response.status_code == 200

def test_duplicate_names():
    url = "http://shrine_fastapi:80/user/"
    headers = {'content-type': 'application/json'}
    user = { "is_student": "true", "is_teacher": "false", "name": "", "email": "ab@gmail.com", "phone": "9999999999" }
    user["name"] = names.get_full_name()
    print( "Name : ", user["name"] )

    response = requests.post(url,data=json.dumps(user), headers = headers)
    response = requests.post(url,data=json.dumps(user), headers = headers)
    print(response.request.url)
    print(response.request.headers)
    print(response.request.body)
    assert response.status_code == 400

def test_get_all_students():
    url = "http://shrine_fastapi:80/students"
    response = requests.get(url)
    assert response.status_code == 200

def test_check_email_no_tld():#No top level domain
    url = "http://shrine_fastapi:80/user/"
    headers = {'content-type': 'application/json'}
    user = { "is_student": "true", "is_teacher": "false", "name": "", "email": "ab@gmail", "phone": "9999999999" }
    user["name"] = names.get_full_name()
    print( "Name : ", user["name"] )

    response = requests.post(url,data=json.dumps(user), headers = headers)
    assert response.status_code == 400

def test_check_email_no_domain():
    url = "http://shrine_fastapi:80/user/"
    headers = {'content-type': 'application/json'}
    user = { "is_student": "true", "is_teacher": "false", "name": "", "email": "ab@.in", "phone": "9999999999" }
    user["name"] = names.get_full_name()
    print( "Name : ", user["name"] )

    response = requests.post(url,data=json.dumps(user), headers = headers)
    assert response.status_code == 400

def test_check_phone_short_number():
    url = "http://shrine_fastapi:80/user/"
    headers = {'content-type': 'application/json'}
    user = { "is_student": "true", "is_teacher": "false", "name": "", "email": "ab@gmail.com", "phone": "99999" }
    user["name"] = names.get_full_name()
    print( "Name : ", user["name"] )

    response = requests.post(url,data=json.dumps(user), headers = headers)
    assert response.status_code == 400

def test_check_phone_long_number():
    url = "http://shrine_fastapi:80/user/"
    headers = {'content-type': 'application/json'}
    user = { "is_student": "true", "is_teacher": "false", "name": "", "email": "ab@gmail.com", "phone": "999999999999999" }
    user["name"] = names.get_full_name()
    print( "Name : ", user["name"] )

    response = requests.post(url,data=json.dumps(user), headers = headers)
    assert response.status_code == 400

def test_check_phone_wrong_country_code():
    url = "http://shrine_fastapi:80/user/"
    headers = {'content-type': 'application/json'}
    user = { "is_student": "true", "is_teacher": "false", "name": "", "email": "ab@gmail.com", "phone": "+92 9999999999" }
    user["name"] = names.get_full_name()
    print( "Name : ", user["name"] )

    response = requests.post(url,data=json.dumps(user), headers = headers)
    assert response.status_code == 400

