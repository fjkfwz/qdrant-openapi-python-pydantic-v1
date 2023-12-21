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


from typing import Dict, Optional
from pydantic import BaseModel, Field
from openapi_client.models.collection_params_diff import CollectionParamsDiff
from openapi_client.models.hnsw_config_diff import HnswConfigDiff
from openapi_client.models.optimizers_config_diff import OptimizersConfigDiff
from openapi_client.models.quantization_config_diff import QuantizationConfigDiff
from openapi_client.models.sparse_vector_params import SparseVectorParams
from openapi_client.models.vector_params_diff import VectorParamsDiff

class UpdateCollection(BaseModel):
    """
    Operation for updating parameters of the existing collection  # noqa: E501
    """
    vectors: Optional[Dict[str, VectorParamsDiff]] = Field(None, description="Vector update params for multiple vectors  { \"vector_name\": { \"hnsw_config\": { \"m\": 8 } } }")
    optimizers_config: Optional[OptimizersConfigDiff] = None
    params: Optional[CollectionParamsDiff] = None
    hnsw_config: Optional[HnswConfigDiff] = None
    quantization_config: Optional[QuantizationConfigDiff] = None
    sparse_vectors: Optional[Dict[str, SparseVectorParams]] = None
    __properties = ["vectors", "optimizers_config", "params", "hnsw_config", "quantization_config", "sparse_vectors"]

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
    def from_json(cls, json_str: str) -> UpdateCollection:
        """Create an instance of UpdateCollection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in vectors (dict)
        _field_dict = {}
        if self.vectors:
            for _key in self.vectors:
                if self.vectors[_key]:
                    _field_dict[_key] = self.vectors[_key].to_dict()
            _dict['vectors'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of optimizers_config
        if self.optimizers_config:
            _dict['optimizers_config'] = self.optimizers_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of params
        if self.params:
            _dict['params'] = self.params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hnsw_config
        if self.hnsw_config:
            _dict['hnsw_config'] = self.hnsw_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quantization_config
        if self.quantization_config:
            _dict['quantization_config'] = self.quantization_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in sparse_vectors (dict)
        _field_dict = {}
        if self.sparse_vectors:
            for _key in self.sparse_vectors:
                if self.sparse_vectors[_key]:
                    _field_dict[_key] = self.sparse_vectors[_key].to_dict()
            _dict['sparse_vectors'] = _field_dict
        # set to None if optimizers_config (nullable) is None
        # and __fields_set__ contains the field
        if self.optimizers_config is None and "optimizers_config" in self.__fields_set__:
            _dict['optimizers_config'] = None

        # set to None if params (nullable) is None
        # and __fields_set__ contains the field
        if self.params is None and "params" in self.__fields_set__:
            _dict['params'] = None

        # set to None if hnsw_config (nullable) is None
        # and __fields_set__ contains the field
        if self.hnsw_config is None and "hnsw_config" in self.__fields_set__:
            _dict['hnsw_config'] = None

        # set to None if quantization_config (nullable) is None
        # and __fields_set__ contains the field
        if self.quantization_config is None and "quantization_config" in self.__fields_set__:
            _dict['quantization_config'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateCollection:
        """Create an instance of UpdateCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateCollection.parse_obj(obj)

        _obj = UpdateCollection.parse_obj({
            "vectors": dict(
                (_k, VectorParamsDiff.from_dict(_v))
                for _k, _v in obj.get("vectors").items()
            )
            if obj.get("vectors") is not None
            else None,
            "optimizers_config": OptimizersConfigDiff.from_dict(obj.get("optimizers_config")) if obj.get("optimizers_config") is not None else None,
            "params": CollectionParamsDiff.from_dict(obj.get("params")) if obj.get("params") is not None else None,
            "hnsw_config": HnswConfigDiff.from_dict(obj.get("hnsw_config")) if obj.get("hnsw_config") is not None else None,
            "quantization_config": QuantizationConfigDiff.from_dict(obj.get("quantization_config")) if obj.get("quantization_config") is not None else None,
            "sparse_vectors": dict(
                (_k, SparseVectorParams.from_dict(_v))
                for _k, _v in obj.get("sparse_vectors").items()
            )
            if obj.get("sparse_vectors") is not None
            else None
        })
        return _obj

