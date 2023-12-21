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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conint, conlist
from openapi_client.models.filter import Filter
from openapi_client.models.lookup_location import LookupLocation
from openapi_client.models.recommend_example import RecommendExample
from openapi_client.models.recommend_strategy import RecommendStrategy
from openapi_client.models.search_params import SearchParams
from openapi_client.models.shard_key_selector import ShardKeySelector
from openapi_client.models.with_payload_interface import WithPayloadInterface
from openapi_client.models.with_vector import WithVector

class RecommendRequest(BaseModel):
    """
    Recommendation request. Provides positive and negative examples of the vectors, which can be ids of points that are already stored in the collection, raw vectors, or even ids and vectors combined.  Service should look for the points which are closer to positive examples and at the same time further to negative examples. The concrete way of how to compare negative and positive distances is up to the `strategy` chosen.  # noqa: E501
    """
    shard_key: Optional[ShardKeySelector] = None
    positive: Optional[conlist(RecommendExample)] = Field(None, description="Look for vectors closest to those")
    negative: Optional[conlist(RecommendExample)] = Field(None, description="Try to avoid vectors like this")
    strategy: Optional[RecommendStrategy] = None
    filter: Optional[Filter] = None
    params: Optional[SearchParams] = None
    limit: conint(strict=True, ge=1) = Field(..., description="Max number of result to return")
    offset: Optional[conint(strict=True, ge=0)] = Field(None, description="Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues.")
    with_payload: Optional[WithPayloadInterface] = None
    with_vector: Optional[WithVector] = None
    score_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.")
    using: Optional[StrictStr] = None
    lookup_from: Optional[LookupLocation] = None
    __properties = ["shard_key", "positive", "negative", "strategy", "filter", "params", "limit", "offset", "with_payload", "with_vector", "score_threshold", "using", "lookup_from"]

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
    def from_json(cls, json_str: str) -> RecommendRequest:
        """Create an instance of RecommendRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of shard_key
        if self.shard_key:
            _dict['shard_key'] = self.shard_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in positive (list)
        _items = []
        if self.positive:
            for _item in self.positive:
                if _item:
                    _items.append(_item.to_dict())
            _dict['positive'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in negative (list)
        _items = []
        if self.negative:
            for _item in self.negative:
                if _item:
                    _items.append(_item.to_dict())
            _dict['negative'] = _items
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of params
        if self.params:
            _dict['params'] = self.params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of with_payload
        if self.with_payload:
            _dict['with_payload'] = self.with_payload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of with_vector
        if self.with_vector:
            _dict['with_vector'] = self.with_vector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lookup_from
        if self.lookup_from:
            _dict['lookup_from'] = self.lookup_from.to_dict()
        # set to None if shard_key (nullable) is None
        # and __fields_set__ contains the field
        if self.shard_key is None and "shard_key" in self.__fields_set__:
            _dict['shard_key'] = None

        # set to None if strategy (nullable) is None
        # and __fields_set__ contains the field
        if self.strategy is None and "strategy" in self.__fields_set__:
            _dict['strategy'] = None

        # set to None if filter (nullable) is None
        # and __fields_set__ contains the field
        if self.filter is None and "filter" in self.__fields_set__:
            _dict['filter'] = None

        # set to None if params (nullable) is None
        # and __fields_set__ contains the field
        if self.params is None and "params" in self.__fields_set__:
            _dict['params'] = None

        # set to None if offset (nullable) is None
        # and __fields_set__ contains the field
        if self.offset is None and "offset" in self.__fields_set__:
            _dict['offset'] = None

        # set to None if with_payload (nullable) is None
        # and __fields_set__ contains the field
        if self.with_payload is None and "with_payload" in self.__fields_set__:
            _dict['with_payload'] = None

        # set to None if with_vector (nullable) is None
        # and __fields_set__ contains the field
        if self.with_vector is None and "with_vector" in self.__fields_set__:
            _dict['with_vector'] = None

        # set to None if score_threshold (nullable) is None
        # and __fields_set__ contains the field
        if self.score_threshold is None and "score_threshold" in self.__fields_set__:
            _dict['score_threshold'] = None

        # set to None if lookup_from (nullable) is None
        # and __fields_set__ contains the field
        if self.lookup_from is None and "lookup_from" in self.__fields_set__:
            _dict['lookup_from'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RecommendRequest:
        """Create an instance of RecommendRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RecommendRequest.parse_obj(obj)

        _obj = RecommendRequest.parse_obj({
            "shard_key": ShardKeySelector.from_dict(obj.get("shard_key")) if obj.get("shard_key") is not None else None,
            "positive": [RecommendExample.from_dict(_item) for _item in obj.get("positive")] if obj.get("positive") is not None else None,
            "negative": [RecommendExample.from_dict(_item) for _item in obj.get("negative")] if obj.get("negative") is not None else None,
            "strategy": obj.get("strategy"),
            "filter": Filter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "params": SearchParams.from_dict(obj.get("params")) if obj.get("params") is not None else None,
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "with_payload": WithPayloadInterface.from_dict(obj.get("with_payload")) if obj.get("with_payload") is not None else None,
            "with_vector": WithVector.from_dict(obj.get("with_vector")) if obj.get("with_vector") is not None else None,
            "score_threshold": obj.get("score_threshold"),
            "using": obj.get("using"),
            "lookup_from": LookupLocation.from_dict(obj.get("lookup_from")) if obj.get("lookup_from") is not None else None
        })
        return _obj


