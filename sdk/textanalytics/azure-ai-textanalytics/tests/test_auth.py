# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest
from testcase import TextAnalyticsTest, TextAnalyticsPreparer, get_textanalytics_client
from devtools_testutils import get_credential
from azure.ai.textanalytics import TextAnalyticsClient, AnalyzeSentimentAction
import os


class TestAuth(TextAnalyticsTest):

    @pytest.mark.live_test_only
    @TextAnalyticsPreparer()
    def test_active_directory_auth(self, **kwargs):
        text_analytics_endpoint_suffix = os.environ.get("TEXTANALYTICS_ENDPOINT_SUFFIX",".cognitiveservices.azure.com")
        credential_scopes = ["https://{}/.default".format(text_analytics_endpoint_suffix[1:])]
        text_analytics = get_textanalytics_client(credential_scopes=credential_scopes)

        docs = [{"id": "1", "text": "I should take my cat to the veterinarian."},
                {"id": "2", "text": "Este es un document escrito en Español."},
                {"id": "3", "text": "猫は幸せ"},
                {"id": "4", "text": "Fahrt nach Stuttgart und dann zum Hotel zu Fu."}]

        response = text_analytics.detect_language(docs)

    @pytest.mark.live_test_only
    @TextAnalyticsPreparer()
    def test_analyze_active_directory_auth(self, **kwargs):
        text_analytics_endpoint_suffix = os.environ.get("TEXTANALYTICS_ENDPOINT_SUFFIX",".cognitiveservices.azure.com")
        credential_scopes = ["https://{}/.default".format(text_analytics_endpoint_suffix[1:])]
        text_analytics = get_textanalytics_client(credential_scopes=credential_scopes)

        docs = ["Microsoft was founded by Bill Gates and Paul Allen."]

        response = text_analytics.begin_analyze_actions(
            docs,
            actions=[AnalyzeSentimentAction()],
        ).result()

        pages = list(response)

    @TextAnalyticsPreparer()
    def test_empty_credentials(self, **kwargs):
        textanalytics_test_endpoint = "https://fakeendpoint.cognitiveservices.azure.com/"
        with pytest.raises(TypeError):
            text_analytics = TextAnalyticsClient(textanalytics_test_endpoint, "")

    @TextAnalyticsPreparer()
    def test_bad_type_for_credentials(self, **kwargs):
        textanalytics_test_endpoint = "https://fakeendpoint.cognitiveservices.azure.com/"
        with pytest.raises(TypeError):
            text_analytics = TextAnalyticsClient(textanalytics_test_endpoint, [])

    @TextAnalyticsPreparer()
    def test_none_credentials(self, **kwargs):
        textanalytics_test_endpoint = "https://fakeendpoint.cognitiveservices.azure.com/"
        with pytest.raises(ValueError):
            text_analytics = TextAnalyticsClient(textanalytics_test_endpoint, None)

    @TextAnalyticsPreparer()
    def test_none_endpoint(self, **kwargs):
        with pytest.raises(ValueError):
            text_analytics = TextAnalyticsClient(None, get_credential())
