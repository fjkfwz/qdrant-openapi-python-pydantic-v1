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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conint

class OptimizersConfigDiff(BaseModel):
    """
    OptimizersConfigDiff
    """
    deleted_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The minimal fraction of deleted vectors in a segment, required to perform segment optimization")
    vacuum_min_vector_number: Optional[conint(strict=True, ge=0)] = Field(None, description="The minimal number of vectors in a segment, required to perform segment optimization")
    default_segment_number: Optional[conint(strict=True, ge=0)] = Field(None, description="Target amount of segments optimizer will try to keep. Real amount of segments may vary depending on multiple parameters: - Amount of stored points - Current write RPS  It is recommended to select default number of segments as a factor of the number of search threads, so that each segment would be handled evenly by one of the threads If `default_segment_number = 0`, will be automatically selected by the number of available CPUs")
    max_segment_size: Optional[conint(strict=True, ge=0)] = Field(None, description="Do not create segments larger this size (in kilobytes). Large segments might require disproportionately long indexation times, therefore it makes sense to limit the size of segments.  If indexation speed have more priority for your - make this parameter lower. If search speed is more important - make this parameter higher. Note: 1Kb = 1 vector of size 256")
    memmap_threshold: Optional[conint(strict=True, ge=0)] = Field(None, description="Maximum size (in kilobytes) of vectors to store in-memory per segment. Segments larger than this threshold will be stored as read-only memmaped file.  Memmap storage is disabled by default, to enable it, set this threshold to a reasonable value.  To disable memmap storage, set this to `0`.  Note: 1Kb = 1 vector of size 256")
    indexing_threshold: Optional[conint(strict=True, ge=0)] = Field(None, description="Maximum size (in kilobytes) of vectors allowed for plain index, exceeding this threshold will enable vector indexing  Default value is 20,000, based on <https://github.com/google-research/google-research/blob/master/scann/docs/algorithms.md>.  To disable vector indexing, set to `0`.  Note: 1kB = 1 vector of size 256.")
    flush_interval_sec: Optional[conint(strict=True, ge=0)] = Field(None, description="Minimum interval between forced flushes.")
    max_optimization_threads: Optional[conint(strict=True, ge=0)] = Field(None, description="Maximum available threads for optimization workers")
    __properties = ["deleted_threshold", "vacuum_min_vector_number", "default_segment_number", "max_segment_size", "memmap_threshold", "indexing_threshold", "flush_interval_sec", "max_optimization_threads"]

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
    def from_json(cls, json_str: str) -> OptimizersConfigDiff:
        """Create an instance of OptimizersConfigDiff from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if deleted_threshold (nullable) is None
        # and __fields_set__ contains the field
        if self.deleted_threshold is None and "deleted_threshold" in self.__fields_set__:
            _dict['deleted_threshold'] = None

        # set to None if vacuum_min_vector_number (nullable) is None
        # and __fields_set__ contains the field
        if self.vacuum_min_vector_number is None and "vacuum_min_vector_number" in self.__fields_set__:
            _dict['vacuum_min_vector_number'] = None

        # set to None if default_segment_number (nullable) is None
        # and __fields_set__ contains the field
        if self.default_segment_number is None and "default_segment_number" in self.__fields_set__:
            _dict['default_segment_number'] = None

        # set to None if max_segment_size (nullable) is None
        # and __fields_set__ contains the field
        if self.max_segment_size is None and "max_segment_size" in self.__fields_set__:
            _dict['max_segment_size'] = None

        # set to None if memmap_threshold (nullable) is None
        # and __fields_set__ contains the field
        if self.memmap_threshold is None and "memmap_threshold" in self.__fields_set__:
            _dict['memmap_threshold'] = None

        # set to None if indexing_threshold (nullable) is None
        # and __fields_set__ contains the field
        if self.indexing_threshold is None and "indexing_threshold" in self.__fields_set__:
            _dict['indexing_threshold'] = None

        # set to None if flush_interval_sec (nullable) is None
        # and __fields_set__ contains the field
        if self.flush_interval_sec is None and "flush_interval_sec" in self.__fields_set__:
            _dict['flush_interval_sec'] = None

        # set to None if max_optimization_threads (nullable) is None
        # and __fields_set__ contains the field
        if self.max_optimization_threads is None and "max_optimization_threads" in self.__fields_set__:
            _dict['max_optimization_threads'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OptimizersConfigDiff:
        """Create an instance of OptimizersConfigDiff from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OptimizersConfigDiff.parse_obj(obj)

        _obj = OptimizersConfigDiff.parse_obj({
            "deleted_threshold": obj.get("deleted_threshold"),
            "vacuum_min_vector_number": obj.get("vacuum_min_vector_number"),
            "default_segment_number": obj.get("default_segment_number"),
            "max_segment_size": obj.get("max_segment_size"),
            "memmap_threshold": obj.get("memmap_threshold"),
            "indexing_threshold": obj.get("indexing_threshold"),
            "flush_interval_sec": obj.get("flush_interval_sec"),
            "max_optimization_threads": obj.get("max_optimization_threads")
        })
        return _obj


