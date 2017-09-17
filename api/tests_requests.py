import json
import jsonschema

from .views import in_circle, schema_response

from django.test.client import RequestFactory
from django.http.response import HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError

rf = RequestFactory()

# Pytest module for testing requests to the API


# test if GET request fails
def test_get_request():
    request = rf.get('/api/')
    response = in_circle(request)
    assert isinstance(response, HttpResponseForbidden)


# test if malformed JSON fails
def test_malformed_json():
    body = b'{"a":1sfaoijo]f'
    request = rf.post('/api', data=body, content_type='application/json')
    response = in_circle(request)
    assert isinstance(response, HttpResponseBadRequest)


# test if request schema validation works
def test_wrong_json():
    body = b'{"point": {"xy": 1.0, "y": 2.0}, "circleaa": {"x": 1.1}}'
    request = rf.post('/api', data=body, content_type='application/json')
    response = in_circle(request)
    assert isinstance(response, HttpResponseBadRequest)


# test if response schema validates, should happen NEVER
def test_not_alpha_particle():
    body = b'{"point": {"x": 1.0, "y": 2.0}, "circle": {"x": 1.1, "y": 2.6, "radius": 4.2}}'
    request = rf.post('/api', data=body, content_type='application/json')
    response = in_circle(request)
    assert not isinstance(response, HttpResponseServerError)


# test when radius is negative
# P.S. no need to test if locations are negative, since in geometry they can be
def test_negative_radius():
    body = b'{"point": {"x": 1.0, "y": 2.0}, "circle": {"x": 1.1, "y": 2.6, "radius": -4.2}}'
    request = rf.post('/api', data=body, content_type='application/json')
    response = in_circle(request)
    assert isinstance(response, HttpResponseBadRequest)


# test if response schema validates in a normal request
def test_validate_schema():
    body = b'{"point": {"x": 1.0, "y": 2.0}, "circle": {"x": 1.1, "y": 2.6, "radius": 4.2}}'
    request = rf.post('/api', data=body, content_type='application/json')
    response = in_circle(request)
    jsonschema.validate(json.loads(response.content.decode("utf-8")), schema_response)


# test when point is within circle
def test_calculation_true():
    body = b'{"point": {"x": 1.0, "y": 2.0}, "circle": {"x": 1.1, "y": 2.6, "radius": 4.2}}'
    request = rf.post('/api', data=body, content_type='application/json')
    response = in_circle(request)
    response_dict = json.loads(response.content.decode("utf-8"))
    jsonschema.validate(response_dict, schema_response)
    assert response_dict["inside"]


# test when point is not within circle
def test_calculation_false():
    body = b'{"point": {"x": 1.0, "y": 2.0}, "circle": {"x": 1.1, "y": 2.6, "radius": 0.2}}'
    request = rf.post('/api', data=body, content_type='application/json')
    response = in_circle(request)
    response_dict = json.loads(response.content.decode("utf-8"))
    jsonschema.validate(response_dict, schema_response)
    assert not response_dict["inside"]
