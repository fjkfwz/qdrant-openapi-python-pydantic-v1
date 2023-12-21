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

from openapi_client.models.replica_set_telemetry import ReplicaSetTelemetry  # noqa: E501

class TestReplicaSetTelemetry(unittest.TestCase):
    """ReplicaSetTelemetry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReplicaSetTelemetry:
        """Test ReplicaSetTelemetry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReplicaSetTelemetry`
        """
        model = ReplicaSetTelemetry()  # noqa: E501
        if include_optional:
            return ReplicaSetTelemetry(
                id = 0,
                local = openapi_client.models.local_shard_telemetry.LocalShardTelemetry(
                    variant_name = '', 
                    segments = [
                        openapi_client.models.segment_telemetry.SegmentTelemetry(
                            info = openapi_client.models.segment_info.SegmentInfo(
                                segment_type = 'plain', 
                                num_vectors = 0, 
                                num_points = 0, 
                                num_indexed_vectors = 0, 
                                num_deleted_vectors = 0, 
                                ram_usage_bytes = 0, 
                                disk_usage_bytes = 0, 
                                is_appendable = True, 
                                index_schema = {
                                    'key' : openapi_client.models.payload_index_info.PayloadIndexInfo(
                                        data_type = 'keyword', 
                                        params = openapi_client.models.text_index_params.TextIndexParams(
                                            type = 'text', 
                                            tokenizer = 'prefix', 
                                            min_token_len = 0, 
                                            max_token_len = 0, 
                                            lowercase = True, ), 
                                        points = 0, )
                                    }, 
                                vector_data = {
                                    'key' : openapi_client.models.vector_data_info.VectorDataInfo(
                                        num_vectors = 0, 
                                        num_indexed_vectors = 0, 
                                        num_deleted_vectors = 0, )
                                    }, ), 
                            config = openapi_client.models.segment_config.SegmentConfig(
                                sparse_vector_data = {
                                    'key' : openapi_client.models.sparse_vector_data_config.SparseVectorDataConfig(
                                        index = openapi_client.models.sparse_index_config.SparseIndexConfig(
                                            full_scan_threshold = 0, 
                                            index_type = null, ), )
                                    }, 
                                payload_storage_type = null, ), 
                            vector_index_searches = [
                                openapi_client.models.vector_index_searches_telemetry.VectorIndexSearchesTelemetry(
                                    index_name = '', 
                                    unfiltered_plain = openapi_client.models.operation_duration_statistics.OperationDurationStatistics(
                                        count = 0, 
                                        fail_count = 0, 
                                        avg_duration_micros = 1.337, 
                                        min_duration_micros = 1.337, 
                                        max_duration_micros = 1.337, 
                                        last_responded = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                    unfiltered_hnsw = openapi_client.models.operation_duration_statistics.OperationDurationStatistics(
                                        count = 0, 
                                        fail_count = 0, 
                                        avg_duration_micros = 1.337, 
                                        min_duration_micros = 1.337, 
                                        max_duration_micros = 1.337, 
                                        last_responded = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                    unfiltered_sparse = , 
                                    filtered_plain = , 
                                    filtered_small_cardinality = , 
                                    filtered_large_cardinality = , 
                                    filtered_exact = , 
                                    filtered_sparse = , 
                                    unfiltered_exact = , )
                                ], 
                            payload_field_indices = [
                                openapi_client.models.payload_index_telemetry.PayloadIndexTelemetry(
                                    field_name = '', 
                                    points_values_count = 0, 
                                    points_count = 0, 
                                    histogram_bucket_size = 0, )
                                ], )
                        ], 
                    optimizations = openapi_client.models.optimizer_telemetry.OptimizerTelemetry(
                        status = null, 
                        optimizations = , 
                        log = [
                            openapi_client.models.tracker_telemetry.TrackerTelemetry(
                                name = '', 
                                segment_ids = [
                                    0
                                    ], 
                                status = null, 
                                start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], ), ),
                remote = [
                    openapi_client.models.remote_shard_telemetry.RemoteShardTelemetry(
                        shard_id = 0, 
                        peer_id = 0, 
                        searches = openapi_client.models.operation_duration_statistics.OperationDurationStatistics(
                            count = 0, 
                            fail_count = 0, 
                            avg_duration_micros = 1.337, 
                            min_duration_micros = 1.337, 
                            max_duration_micros = 1.337, 
                            last_responded = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        updates = openapi_client.models.operation_duration_statistics.OperationDurationStatistics(
                            count = 0, 
                            fail_count = 0, 
                            avg_duration_micros = 1.337, 
                            min_duration_micros = 1.337, 
                            max_duration_micros = 1.337, 
                            last_responded = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ],
                replicate_states = {
                    'key' : 'Active'
                    }
            )
        else:
            return ReplicaSetTelemetry(
                id = 0,
                remote = [
                    openapi_client.models.remote_shard_telemetry.RemoteShardTelemetry(
                        shard_id = 0, 
                        peer_id = 0, 
                        searches = openapi_client.models.operation_duration_statistics.OperationDurationStatistics(
                            count = 0, 
                            fail_count = 0, 
                            avg_duration_micros = 1.337, 
                            min_duration_micros = 1.337, 
                            max_duration_micros = 1.337, 
                            last_responded = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        updates = openapi_client.models.operation_duration_statistics.OperationDurationStatistics(
                            count = 0, 
                            fail_count = 0, 
                            avg_duration_micros = 1.337, 
                            min_duration_micros = 1.337, 
                            max_duration_micros = 1.337, 
                            last_responded = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ],
                replicate_states = {
                    'key' : 'Active'
                    },
        )
        """

    def testReplicaSetTelemetry(self):
        """Test ReplicaSetTelemetry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
