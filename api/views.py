import json

from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

token = '6d82549b48a8b079f618ee9c51a6dfb59c7e2196'


class TaskList(APIView):
    parser_classes = (JSONParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        dict_res = \
            {"features":
                [
                    {
                        "type": "Feature",
                        "properties": {
                            "id": "5380748",
                            "gid": "gn:locality:5380748",
                            "layer": "locality",
                            "source": "gn",
                            "name": "Palo Alto",
                            "country_a": "USA",
                            "country": "United States",
                            "region": "California",
                            "region_a": "CA",
                            "county": "Santa Clara County",
                            "locality": "Palo Alto",
                            "confidence": 0.956,
                            "label": "Palo Alto, Santa Clara County, CA"
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [
                                -122.14302,
                                37.44188
                            ]
                        }
                    },
                    {
                        "type": "Feature",
                        "properties": {
                            "id": "5345032",
                            "gid": "gn:locality:5345032",
                            "layer": "locality",
                            "source": "gn",
                            "name": "East Palo Alto",
                            "country_a": "USA",
                            "country": "United States",
                            "region": "California",
                            "region_a": "CA",
                            "county": "San Mateo County",
                            "locality": "East Palo Alto",
                            "confidence": 0.889,
                            "label": "East Palo Alto, San Mateo County, CA"
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [
                                -122.14108,
                                37.46883
                            ]
                        }
                    },
                    {
                        "type": "Feature",
                        "properties": {
                            "id": "4870630",
                            "gid": "gn:county:4870630",
                            "layer": "county",
                            "source": "gn",
                            "name": "Palo Alto County",
                            "country_a": "USA",
                            "country": "United States",
                            "region": "Iowa",
                            "region_a": "IA",
                            "county": "Palo Alto County",
                            "confidence": 0.882,
                            "label": "Palo Alto County, IA"
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [
                                -94.67814,
                                43.08206
                            ]
                        }
                    },
                ]
            }

        data = json.dumps(dict_res)

        return Response(data)
