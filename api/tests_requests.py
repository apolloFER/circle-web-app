import pytest

from .views import in_circle

from django.test.client import RequestFactory
from django.http.response import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse

rf = RequestFactory()


def test_get_request():
    request = rf.get('/api/')
    response = in_circle(request)
    assert isinstance(response, HttpResponseForbidden)


def test_malformed_json():
    body = b'{"a":1sfaoijo]f'
    request = rf.post('/api', data=body, content_type='application/json')
    response = in_circle(request)
    assert isinstance(response, HttpResponseBadRequest)


def test_wrong_json():
    body = b'{"point": {"xy": 1.0, "y": 2.0}, "circleaa": {"x": 1.1}}'
    request = rf.post('/api', data=body, content_type='application/json')
    response = in_circle(request)
    assert isinstance(response, HttpResponseBadRequest)


def test_post_request():
    body = b'{"point": {"x": 1.0, "y": 2.0}, "circle": {"x": 1.1, "y": 2.6, "radius": 4.2}}'
    request = rf.post('/api', data=body, content_type='application/json')
    response = in_circle(request)
    assert response.__class__ is JsonResponse


