# Create your views here.

import json
import jsonschema

from .circle import Circle, Point, check_point_in_circle

from django.http.response import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError, JsonResponse

schema_request = {
    "type": "object",
    "required": ["point", "circle"],
    "properties": {
        "point": {"type": "object",
                  "required": ["x", "y"],
                  "properties": {
                      "x": {
                         "type": "number"
                      },
                      "y": {
                          "type": "number"
                      }
                  }},
        "circle": {"type": "object",
                   "required": ["x", "y", "radius"],
                   "properties": {
                      "x": {
                         "type": "number"
                      },
                      "y": {
                          "type": "number"
                      },
                      "radius": {
                          "type": "number"
                      }
                   }},
    },
}

schema_response = {
    "type": "object",
    "required": ["point", "inside"],
    "properties": {
        "point": {"type": "object",
                  "required": ["x", "y"],
                  "properties": {
                      "x": {
                         "type": "number"
                      },
                      "y": {
                          "type": "number"
                      }
                  }},
        "inside": {"type": "boolean"},
    },
}


def in_circle(request):
    if request.method != "POST":
        return HttpResponseForbidden("POST only")

    try:
        request_decoded = json.loads(request.body.decode("utf-8") )
    except ValueError:
        return HttpResponseBadRequest("Malformed JSON")

    try:
        # validate JSON with jsonschema
        jsonschema.validate(request_decoded, schema_request)
    except jsonschema.ValidationError:
        return HttpResponseBadRequest("Schema validation failed")

    point_x, point_y = request_decoded["point"]["x"], request_decoded["point"]["y"]
    circle_x, circle_y = request_decoded["circle"]["x"], request_decoded["circle"]["y"]
    circle_radius = request_decoded["circle"]["radius"]

    point = Point(point_x, point_y)
    try:
        circle = Circle(circle_x, circle_y, circle_radius)
    except ValueError:
        return HttpResponseBadRequest("Negative radius")

    is_inside = check_point_in_circle(point, circle)

    response_dict = {"inside": is_inside, "point": {"x": point_x, "y": point_y}}

    try:
        # validate JSON with jsonschema, not really needed, buy hey, Alpha particle bug
        jsonschema.validate(response_dict, schema_response)
    except jsonschema.ValidationError:
        return HttpResponseServerError("Alpha particle bug happened")

    jsonschema.validate(response_dict, schema_response)

    response = JsonResponse(response_dict)

    return response
