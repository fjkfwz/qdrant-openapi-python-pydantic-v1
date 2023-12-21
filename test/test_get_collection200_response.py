# coding: utf-8

"""
    Qdrant API

    API description for Qdrant vector search engine.  This document describes CRUD and search operations on collections of points (vectors with payload).  Qdrant supports any combinations of `should`, `must` and `must_not` conditions, which makes it possible to use in applications when object could not be described solely by vector. It could be location features, availability flags, and other custom properties businesses should take into account. ## Examples This examples cover the most basic use-cases - collection creation and basic vector search. ### Create collection First - let's create a collection with dot-production metric. ``` curl -X PUT 'http://localhost:6333/collections/test_collection' \\   -H 'Content-Type: application/json' \\   --data-raw '{     \"vectors\": {       \"size\": 4,       \"distance\": \"Dot\"     }   }'  ``` Expected response: ``` {     \"result\": true,     \"status\": \"ok\",     \"time\": 0.031095451 } ``` We can ensure that collection was created: ``` curl 'http://localhost:6333/collections/test_collection' ``` Expected response: ``` {   \"result\": {     \"status\": \"green\",     \"vectors_count\": 0,     \"segments_count\": 5,     \"disk_data_size\": 0,     \"ram_data_size\": 0,     \"config\": {       \"params\": {         \"vectors\": {           \"size\": 4,           \"distance\": \"Dot\"         }       },       \"hnsw_config\": {         \"m\": 16,         \"ef_construct\": 100,         \"full_scan_threshold\": 10000       },       \"optimizer_config\": {         \"deleted_threshold\": 0.2,         \"vacuum_min_vector_number\": 1000,         \"max_segment_number\": 5,         \"memmap_threshold\": 50000,         \"indexing_threshold\": 20000,         \"flush_interval_sec\": 1       },       \"wal_config\": {         \"wal_capacity_mb\": 32,         \"wal_segments_ahead\": 0       }     }   },   \"status\": \"ok\",   \"time\": 2.1199e-05 } ```  ### Add points Let's now add vectors with some payload: ``` curl -L -X PUT 'http://localhost:6333/collections/test_collection/points?wait=true' \\ -H 'Content-Type: application/json' \\ --data-raw '{   \"points\": [     {\"id\": 1, \"vector\": [0.05, 0.61, 0.76, 0.74], \"payload\": {\"city\": \"Berlin\"}},     {\"id\": 2, \"vector\": [0.19, 0.81, 0.75, 0.11], \"payload\": {\"city\": [\"Berlin\", \"London\"] }},     {\"id\": 3, \"vector\": [0.36, 0.55, 0.47, 0.94], \"payload\": {\"city\": [\"Berlin\", \"Moscow\"] }},     {\"id\": 4, \"vector\": [0.18, 0.01, 0.85, 0.80], \"payload\": {\"city\": [\"London\", \"Moscow\"] }},     {\"id\": 5, \"vector\": [0.24, 0.18, 0.22, 0.44], \"payload\": {\"count\": [0]}},     {\"id\": 6, \"vector\": [0.35, 0.08, 0.11, 0.44]}   ] }' ``` Expected response: ``` {     \"result\": {         \"operation_id\": 0,         \"status\": \"completed\"     },     \"status\": \"ok\",     \"time\": 0.000206061 } ``` ### Search with filtering Let's start with a basic request: ``` curl -L -X POST 'http://localhost:6333/collections/test_collection/points/search' \\ -H 'Content-Type: application/json' \\ --data-raw '{     \"vector\": [0.2,0.1,0.9,0.7],     \"top\": 3 }' ``` Expected response: ``` {     \"result\": [         { \"id\": 4, \"score\": 1.362, \"payload\": null, \"version\": 0 },         { \"id\": 1, \"score\": 1.273, \"payload\": null, \"version\": 0 },         { \"id\": 3, \"score\": 1.208, \"payload\": null, \"version\": 0 }     ],     \"status\": \"ok\",     \"time\": 0.000055785 } ``` But result is different if we add a filter: ``` curl -L -X POST 'http://localhost:6333/collections/test_collection/points/search' \\ -H 'Content-Type: application/json' \\ --data-raw '{     \"filter\": {         \"should\": [             {                 \"key\": \"city\",                 \"match\": {                     \"value\": \"London\"                 }             }         ]     },     \"vector\": [0.2, 0.1, 0.9, 0.7],     \"top\": 3 }' ``` Expected response: ``` {     \"result\": [         { \"id\": 4, \"score\": 1.362, \"payload\": null, \"version\": 0 },         { \"id\": 2, \"score\": 0.871, \"payload\": null, \"version\": 0 }     ],     \"status\": \"ok\",     \"time\": 0.000093972 } ``` 

    The version of the OpenAPI document: v1.7.x
    Contact: andrey@vasnetsov.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from qdrant_openapi.models.get_collection200_response import GetCollection200Response  # noqa: E501

class TestGetCollection200Response(unittest.TestCase):
    """GetCollection200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCollection200Response:
        """Test GetCollection200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCollection200Response`
        """
        model = GetCollection200Response()  # noqa: E501
        if include_optional:
            return GetCollection200Response(
                time = 1.337,
                status = '',
                result = qdrant_openapi.models.collection_info.CollectionInfo(
                    status = 'green', 
                    optimizer_status = null, 
                    vectors_count = 0, 
                    indexed_vectors_count = 0, 
                    points_count = 0, 
                    segments_count = 0, 
                    config = qdrant_openapi.models.collection_config.CollectionConfig(
                        params = qdrant_openapi.models.collection_params.CollectionParams(
                            vectors = null, 
                            shard_number = 1, 
                            sharding_method = 'auto', 
                            replication_factor = 1, 
                            write_consistency_factor = 1, 
                            read_fan_out_factor = 0, 
                            on_disk_payload = True, 
                            sparse_vectors = {
                                'key' : qdrant_openapi.models.sparse_vector_params.SparseVectorParams(
                                    index = qdrant_openapi.models.sparse_index_params.SparseIndexParams(
                                        full_scan_threshold = 0, 
                                        on_disk = True, ), )
                                }, ), 
                        hnsw_config = qdrant_openapi.models.hnsw_config.HnswConfig(
                            m = 0, 
                            ef_construct = 4, 
                            full_scan_threshold = 0, 
                            max_indexing_threads = 0, 
                            on_disk = True, 
                            payload_m = 0, ), 
                        optimizer_config = qdrant_openapi.models.optimizers_config.OptimizersConfig(
                            deleted_threshold = 0, 
                            vacuum_min_vector_number = 100, 
                            default_segment_number = 0, 
                            max_segment_size = 0, 
                            memmap_threshold = 0, 
                            indexing_threshold = 0, 
                            flush_interval_sec = 0, 
                            max_optimization_threads = 0, ), 
                        wal_config = qdrant_openapi.models.wal_config.WalConfig(
                            wal_capacity_mb = 1, 
                            wal_segments_ahead = 0, ), 
                        quantization_config = null, ), 
                    payload_schema = {
                        'key' : qdrant_openapi.models.payload_index_info.PayloadIndexInfo(
                            data_type = 'keyword', 
                            points = 0, )
                        }, )
            )
        else:
            return GetCollection200Response(
        )
        """

    def testGetCollection200Response(self):
        """Test GetCollection200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
