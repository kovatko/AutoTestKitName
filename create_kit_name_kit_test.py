import sender_stand_request
import data
import requests
import configuration


def get_new_user_token():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)


response_token = get_new_user_token()
data.auth_token["Authorization"] = "Bearer " + response_token.json()["authToken"]


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)
    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == name


#Тест №1 (Создание набора пользователя). Параметр = 1 символу.
def test_create_kit_1_letter_in_name_get_succes():
    positive_assert("А")


#Тест №2 (Создание набора пользователя). Параметр = 511 символов.
def test_create_kit_511_letter_in_name_get_succes():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


#Тест №3 (Создание набора пользователя). Параметр = 0 символов.
def test_create_kit_0_letter_in_name_get_error():
    negative_assert("")


#Тест №4 (Создание набора пользователя). Параметр = 512 символов.
def test_create_kit_512_letter_in_name_get_error():
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


#Тест №5 (Создание набора пользователя). Разрешены английские буквы.
def test_create_kit_en_letter_in_name_get_succes():
    positive_assert("QWErty")


#Тест №6 (Создание набора пользователя). Разрешены русские буквы.
def test_create_kit_ru_letter_in_name_get_succes():
    positive_assert("Мария")


#Тест №7 (Создание набора пользователя). Разрешены спецсимволы.
def test_create_kit_sc_letter_in_name_get_succes():
    positive_assert("\"№%@\",")


#Тест №8 (Создание набора пользователя). Разрешены пробелы.
def test_create_kit_space_letter_in_name_get_succes():
    positive_assert("Человек и КО ")


#Тест №9 (Создание набора пользователя). Разрешены цифры.
def test_create_kit_numbers_letter_in_name_get_succes():
    positive_assert("123")


#Тест №10 (Создание набора пользователя). Параметр не передан в запросе.
def test_create_kit_epmty_letter_in_name_get_error():
    kit_body = {}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)
    assert kit_response.status_code == 400

    # Тест №11 (Создание набора пользователя). Передан другой тип параметра.


def test_create_kit_another_parameter_get_error():
    kit_body = get_kit_body(123)
    negative_assert(kit_body)
