from rest_framework.status import HTTP_200_OK
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_user(api_client):
    """Тест создания пользователя"""
    url = reverse('user-register')
    user = {"first_name": "Егоа",
            "last_name": "Петров",
            "email": "example@example.ru",
            "password": "#2423t3wef3t335",
            "company": "Panasonic",
            "position": "Supeviser"
            }
    resp = api_client.post(url, user)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['Status'] == True


@pytest.mark.django_db
def test_add_contact(simple_user_client):
    """Тест добавления контактов пользователя"""
    url = reverse('user-contact')
    contact = {"city": "Zyyyyy","street": "Троицкий проспект","phone": "+79000555522" }
    resp = simple_user_client.post(url, contact)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['Status'] == True
