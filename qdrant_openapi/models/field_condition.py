# coding: utf-8

"""
    Qdrant API

    API description for Qdrant vector search engine.  This document describes CRUD and search operations on collections of points (vectors with payload).  Qdrant supports any combinations of `should`, `must` and `must_not` conditions, which makes it possible to use in applications when object could not be described solely by vector. It could be location features, availability flags, and other custom properties businesses should take into account. ## Examples This examples cover the most basic use-cases - collection creation and basic vector search. ### Create collection First - let's create a collection with dot-production metric. ``` curl -X PUT 'http://localhost:6333/collections/test_collection' \\   -H 'Content-Type: application/json' \\   --data-raw '{     \"vectors\": {       \"size\": 4,       \"distance\": \"Dot\"     }   }'  ``` Expected response: ``` {     \"result\": true,     \"status\": \"ok\",     \"time\": 0.031095451 } ``` We can ensure that collection was created: ``` curl 'http://localhost:6333/collections/test_collection' ``` Expected response: ``` {   \"result\": {     \"status\": \"green\",     \"vectors_count\": 0,     \"segments_count\": 5,     \"disk_data_size\": 0,     \"ram_data_size\": 0,     \"config\": {       \"params\": {         \"vectors\": {           \"size\": 4,           \"distance\": \"Dot\"         }       },       \"hnsw_config\": {         \"m\": 16,         \"ef_construct\": 100,         \"full_scan_threshold\": 10000       },       \"optimizer_config\": {         \"deleted_threshold\": 0.2,         \"vacuum_min_vector_number\": 1000,         \"max_segment_number\": 5,         \"memmap_threshold\": 50000,         \"indexing_threshold\": 20000,         \"flush_interval_sec\": 1       },       \"wal_config\": {         \"wal_capacity_mb\": 32,         \"wal_segments_ahead\": 0       }     }   },   \"status\": \"ok\",   \"time\": 2.1199e-05 } ```  ### Add points Let's now add vectors with some payload: ``` curl -L -X PUT 'http://localhost:6333/collections/test_collection/points?wait=true' \\ -H 'Content-Type: application/json' \\ --data-raw '{   \"points\": [     {\"id\": 1, \"vector\": [0.05, 0.61, 0.76, 0.74], \"payload\": {\"city\": \"Berlin\"}},     {\"id\": 2, \"vector\": [0.19, 0.81, 0.75, 0.11], \"payload\": {\"city\": [\"Berlin\", \"London\"] }},     {\"id\": 3, \"vector\": [0.36, 0.55, 0.47, 0.94], \"payload\": {\"city\": [\"Berlin\", \"Moscow\"] }},     {\"id\": 4, \"vector\": [0.18, 0.01, 0.85, 0.80], \"payload\": {\"city\": [\"London\", \"Moscow\"] }},     {\"id\": 5, \"vector\": [0.24, 0.18, 0.22, 0.44], \"payload\": {\"count\": [0]}},     {\"id\": 6, \"vector\": [0.35, 0.08, 0.11, 0.44]}   ] }' ``` Expected response: ``` {     \"result\": {         \"operation_id\": 0,         \"status\": \"completed\"     },     \"status\": \"ok\",     \"time\": 0.000206061 } ``` ### Search with filtering Let's start with a basic request: ``` curl -L -X POST 'http://localhost:6333/collections/test_collection/points/search' \\ -H 'Content-Type: application/json' \\ --data-raw '{     \"vector\": [0.2,0.1,0.9,0.7],     \"top\": 3 }' ``` Expected response: ``` {     \"result\": [         { \"id\": 4, \"score\": 1.362, \"payload\": null, \"version\": 0 },         { \"id\": 1, \"score\": 1.273, \"payload\": null, \"version\": 0 },         { \"id\": 3, \"score\": 1.208, \"payload\": null, \"version\": 0 }     ],     \"status\": \"ok\",     \"time\": 0.000055785 } ``` But result is different if we add a filter: ``` curl -L -X POST 'http://localhost:6333/collections/test_collection/points/search' \\ -H 'Content-Type: application/json' \\ --data-raw '{     \"filter\": {         \"should\": [             {                 \"key\": \"city\",                 \"match\": {                     \"value\": \"London\"                 }             }         ]     },     \"vector\": [0.2, 0.1, 0.9, 0.7],     \"top\": 3 }' ``` Expected response: ``` {     \"result\": [         { \"id\": 4, \"score\": 1.362, \"payload\": null, \"version\": 0 },         { \"id\": 2, \"score\": 0.871, \"payload\": null, \"version\": 0 }     ],     \"status\": \"ok\",     \"time\": 0.000093972 } ``` 

    The version of the OpenAPI document: v1.7.x
    Contact: andrey@vasnetsov.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from qdrant_openapi.models.geo_bounding_box import GeoBoundingBox
from qdrant_openapi.models.geo_polygon import GeoPolygon
from qdrant_openapi.models.geo_radius import GeoRadius
from qdrant_openapi.models.match import Match
from qdrant_openapi.models.range import Range
from qdrant_openapi.models.values_count import ValuesCount

class FieldCondition(BaseModel):
    """
    All possible payload filtering conditions  # noqa: E501
    """
    key: StrictStr = Field(..., description="Payload key")
    match: Optional[Match] = None
    range: Optional[Range] = None
    geo_bounding_box: Optional[GeoBoundingBox] = None
    geo_radius: Optional[GeoRadius] = None
    geo_polygon: Optional[GeoPolygon] = None
    values_count: Optional[ValuesCount] = None
    __properties = ["key", "match", "range", "geo_bounding_box", "geo_radius", "geo_polygon", "values_count"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FieldCondition:
        """Create an instance of FieldCondition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of match
        if self.match:
            _dict['match'] = self.match.to_dict()
        # override the default output from pydantic by calling `to_dict()` of range
        if self.range:
            _dict['range'] = self.range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geo_bounding_box
        if self.geo_bounding_box:
            _dict['geo_bounding_box'] = self.geo_bounding_box.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geo_radius
        if self.geo_radius:
            _dict['geo_radius'] = self.geo_radius.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geo_polygon
        if self.geo_polygon:
            _dict['geo_polygon'] = self.geo_polygon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of values_count
        if self.values_count:
            _dict['values_count'] = self.values_count.to_dict()
        # set to None if match (nullable) is None
        # and __fields_set__ contains the field
        if self.match is None and "match" in self.__fields_set__:
            _dict['match'] = None

        # set to None if range (nullable) is None
        # and __fields_set__ contains the field
        if self.range is None and "range" in self.__fields_set__:
            _dict['range'] = None

        # set to None if geo_bounding_box (nullable) is None
        # and __fields_set__ contains the field
        if self.geo_bounding_box is None and "geo_bounding_box" in self.__fields_set__:
            _dict['geo_bounding_box'] = None

        # set to None if geo_radius (nullable) is None
        # and __fields_set__ contains the field
        if self.geo_radius is None and "geo_radius" in self.__fields_set__:
            _dict['geo_radius'] = None

        # set to None if geo_polygon (nullable) is None
        # and __fields_set__ contains the field
        if self.geo_polygon is None and "geo_polygon" in self.__fields_set__:
            _dict['geo_polygon'] = None

        # set to None if values_count (nullable) is None
        # and __fields_set__ contains the field
        if self.values_count is None and "values_count" in self.__fields_set__:
            _dict['values_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FieldCondition:
        """Create an instance of FieldCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FieldCondition.parse_obj(obj)

        _obj = FieldCondition.parse_obj({
            "key": obj.get("key"),
            "match": Match.from_dict(obj.get("match")) if obj.get("match") is not None else None,
            "range": Range.from_dict(obj.get("range")) if obj.get("range") is not None else None,
            "geo_bounding_box": GeoBoundingBox.from_dict(obj.get("geo_bounding_box")) if obj.get("geo_bounding_box") is not None else None,
            "geo_radius": GeoRadius.from_dict(obj.get("geo_radius")) if obj.get("geo_radius") is not None else None,
            "geo_polygon": GeoPolygon.from_dict(obj.get("geo_polygon")) if obj.get("geo_polygon") is not None else None,
            "values_count": ValuesCount.from_dict(obj.get("values_count")) if obj.get("values_count") is not None else None
        })
        return _obj


