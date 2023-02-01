# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE.txt in the project root for
# license information.
# -------------------------------------------------------------------------
from datetime import timedelta
from unittest import mock

from azure.monitor.query import MetricsQueryClient, MetricAggregationType, Metric
from devtools_testutils import AzureRecordedTestCase


METRIC_NAME = "Event"


class TestMetricsClient(AzureRecordedTestCase):

    def test_metrics_auth(self, recorded_test, monitor_info):
        client = self.create_client_from_credential(MetricsQueryClient, self.get_credential(MetricsQueryClient))
        response = client.query_resource(
            monitor_info['metrics_resource_id'],
            metric_names=[METRIC_NAME],
            timespan=timedelta(days=1),
            aggregations=[MetricAggregationType.COUNT]
            )
        assert response
        assert response.metrics

    def test_metrics_granularity(self, recorded_test, monitor_info):
        client = self.create_client_from_credential(MetricsQueryClient, self.get_credential(MetricsQueryClient))
        response = client.query_resource(
            monitor_info['metrics_resource_id'],
            metric_names=[METRIC_NAME],
            timespan=timedelta(days=1),
            granularity=timedelta(minutes=5),
            aggregations=[MetricAggregationType.COUNT]
            )
        assert response
        assert response.granularity == timedelta(minutes=5)

    def test_metrics_filter(self, recorded_test, monitor_info):
        client = self.create_client_from_credential(MetricsQueryClient, self.get_credential(MetricsQueryClient))
        response = client.query_resource(
            monitor_info['metrics_resource_id'],
            metric_names=[METRIC_NAME],
            timespan=timedelta(days=1),
            granularity=timedelta(minutes=5),
            filter="Source eq '*'",
            aggregations=[MetricAggregationType.COUNT]
            )
        assert response
        metric = response.metrics[METRIC_NAME]
        for t in metric.timeseries:
            assert t.metadata_values is not None

    def test_metrics_list(self, recorded_test, monitor_info):
        client = self.create_client_from_credential(MetricsQueryClient, self.get_credential(MetricsQueryClient))
        response = client.query_resource(
            monitor_info['metrics_resource_id'],
            metric_names=[METRIC_NAME],
            timespan=timedelta(days=1),
            granularity=timedelta(minutes=5),
            aggregations=[MetricAggregationType.COUNT]
            )
        assert response
        metrics = response.metrics
        assert len(metrics) == 1
        assert metrics[0].__class__ == Metric
        assert metrics[METRIC_NAME].__class__ == Metric
        assert metrics[METRIC_NAME] == metrics[0]

    def test_metrics_list_with_commas(self):
        """Commas in metric names should be encoded as %2."""

        with mock.patch("azure.monitor.query._generated.metrics.operations.MetricsOperations.list") as mock_list:
            mock_list.return_value = {"foo": "bar"}
            client = self.create_client_from_credential(MetricsQueryClient, self.get_credential(MetricsQueryClient))
            client.query_resource(
                "resource",
                metric_names=["metric1,metric2", "foo,test,test"],
                timespan=timedelta(days=1),
                granularity=timedelta(minutes=5),
                aggregations=[MetricAggregationType.COUNT]
            )

        assert "metricnames" in mock_list.call_args[1]
        assert mock_list.call_args[1]['metricnames'] == "metric1%2metric2,foo%2test%2test"


    def test_metrics_namespaces(self, recorded_test, monitor_info):
        client = self.create_client_from_credential(MetricsQueryClient, self.get_credential(MetricsQueryClient))

        response = client.list_metric_namespaces(monitor_info['metrics_resource_id'])

        assert response is not None
        for item in response:
            assert item

    def test_metrics_definitions(self, recorded_test, monitor_info):
        client = self.create_client_from_credential(MetricsQueryClient, self.get_credential(MetricsQueryClient))
        response = client.list_metric_definitions(
            monitor_info['metrics_resource_id'], namespace='Microsoft.OperationalInsights/workspaces')

        assert response is not None
        for item in response:
            assert item
