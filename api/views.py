# Create your views here.

import json
import jsonschema

from django.http.response import HttpResponseBadRequest, HttpResponseForbidden, JsonResponse

schema = {
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

def in_circle(request):
    if request.method != "POST":
        return HttpResponseForbidden("POST only")

    try:
        request_decoded = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Malformed JSON")

    # VALIDATE REQUEST JSON

    try:
        jsonschema.validate(request_decoded, schema)
    except jsonschema.ValidationError:
        return HttpResponseBadRequest("Schema validation failed")

    response = JsonResponse(data={"a": 1})

    return response