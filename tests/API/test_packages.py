import subprocess
import json
import pytest

BASE_URL = "https://"


def run_curl(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return json.loads(result.stdout)


def test_create_package():
    command = [ ]

    response = run_curl(command)

    # Проверяем, что сервер вернул успешный ответ
    assert response is not None, "Ответ пустой!"
    assert "package" in response, "Ответ не содержит package!"
    assert response["package"]["adults_count"] == 1, "Количество взрослых не совпадает!"

    page = 'https://{}/{}}/'
    key_kind = 'id'
    if key_kind in response:
        print (f"{page}+{response[key_kind]}")

