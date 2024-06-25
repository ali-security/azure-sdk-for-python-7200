# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest
import functools
from devtools_testutils.aio import recorded_by_proxy_async
from azure.ai.formrecognizer._generated.models import AnalyzeResultOperation
from azure.ai.formrecognizer.aio import DocumentAnalysisClient
from azure.ai.formrecognizer import AnalyzeResult, AnalysisFeature
from preparers import FormRecognizerPreparer
from asynctestcase import AsyncFormRecognizerTest
from preparers import GlobalClientPreparerAsync as _GlobalClientPreparer
from conftest import skip_flaky_test


DocumentAnalysisClientPreparer = functools.partial(_GlobalClientPreparer, DocumentAnalysisClient)


class TestDACAnalyzeReadAsync(AsyncFormRecognizerTest):

    @pytest.mark.live_test_only
    @skip_flaky_test
    @FormRecognizerPreparer()
    @DocumentAnalysisClientPreparer()
    @recorded_by_proxy_async
    async def test_document_read_url_features_formulas(self, client):
        async with client:
            poller = await client.begin_analyze_document_from_url("prebuilt-read", self.formula_url_jpg, features=[AnalysisFeature.FORMULAS])
            result = await poller.result()
        assert len(result.pages) > 0
        assert len(result.pages[0].formulas) == 2
        assert result.pages[0].formulas[0].kind == "inline"
        assert result.pages[0].formulas[0].value
        assert result.pages[0].formulas[0].polygon
        assert result.pages[0].formulas[0].span
        assert result.pages[0].formulas[0].confidence is not None
        assert result.pages[0].formulas[1].kind == "display"
        assert result.pages[0].formulas[1].value
        assert result.pages[0].formulas[1].polygon
        assert result.pages[0].formulas[1].span
        assert result.pages[0].formulas[1].confidence is not None

    @skip_flaky_test
    @FormRecognizerPreparer()
    @DocumentAnalysisClientPreparer()
    @recorded_by_proxy_async
    async def test_document_read_stream_languages(self, client):
        with open(self.invoice_pdf, "rb") as fd:
            document = fd.read()

        responses = []

        def callback(raw_response, _, headers):
            analyze_result = client._deserialize(AnalyzeResultOperation, raw_response)
            extracted_document = AnalyzeResult._from_generated(analyze_result.analyze_result)
            responses.append(analyze_result)
            responses.append(extracted_document)

        async with client:
            poller = await client.begin_analyze_document("prebuilt-read", document, features=[AnalysisFeature.LANGUAGES], cls=callback)
            result = await poller.result()
        raw_analyze_result = responses[0].analyze_result
        returned_model = responses[1]

        # Check AnalyzeResult
        assert returned_model.model_id == raw_analyze_result.model_id
        assert returned_model.api_version == raw_analyze_result.api_version
        assert returned_model.content == raw_analyze_result.content
        
        self.assertDocumentPagesTransformCorrect(returned_model.pages, raw_analyze_result.pages)
        self.assertDocumentStylesTransformCorrect(returned_model.styles, raw_analyze_result.styles)

        # check that detected languages are returned
        assert len(returned_model.languages) > 0
        self.assertDocumentLanguagesTransformCorrect(returned_model.languages, raw_analyze_result.languages)
        # check page range
        assert len(raw_analyze_result.pages) == len(returned_model.pages)

        self.assertDocumentParagraphsTransformCorrect(returned_model.paragraphs, raw_analyze_result.paragraphs)


    @pytest.mark.live_test_only
    @skip_flaky_test
    @FormRecognizerPreparer()
    @DocumentAnalysisClientPreparer()
    async def test_document_read_stream_html(self, **kwargs):
        client = kwargs.get("client")

        with open(self.html_file, "rb") as fd:
            document = fd.read()

        responses = []

        def callback(raw_response, _, headers):
            analyze_result = client._deserialize(AnalyzeResultOperation, raw_response)
            extracted_document = AnalyzeResult._from_generated(analyze_result.analyze_result)
            responses.append(analyze_result)
            responses.append(extracted_document)

        async with client:
            poller = await client.begin_analyze_document("prebuilt-read", document, cls=callback)
            result = await poller.result()
        raw_analyze_result = responses[0].analyze_result
        returned_model = responses[1]

        # Check AnalyzeResult
        assert returned_model.model_id == raw_analyze_result.model_id
        assert returned_model.api_version == raw_analyze_result.api_version
        assert returned_model.content == raw_analyze_result.content

        self.assertDocumentPagesTransformCorrect(returned_model.pages, raw_analyze_result.pages)
        self.assertDocumentStylesTransformCorrect(returned_model.styles, raw_analyze_result.styles)

        # check page range
        assert len(raw_analyze_result.pages) == len(returned_model.pages)

        self.assertDocumentParagraphsTransformCorrect(returned_model.paragraphs, raw_analyze_result.paragraphs)

    @pytest.mark.live_test_only
    @skip_flaky_test
    @FormRecognizerPreparer()
    @DocumentAnalysisClientPreparer()
    async def test_document_read_stream_spreadsheet(self, **kwargs):
        client = kwargs.get("client")

        with open(self.spreadsheet, "rb") as fd:
            document = fd.read()

        responses = []

        def callback(raw_response, _, headers):
            analyze_result = client._deserialize(AnalyzeResultOperation, raw_response)
            extracted_document = AnalyzeResult._from_generated(analyze_result.analyze_result)
            responses.append(analyze_result)
            responses.append(extracted_document)

        async with client:
            poller = await client.begin_analyze_document("prebuilt-read", document, cls=callback)
            result = await poller.result()
        raw_analyze_result = responses[0].analyze_result
        returned_model = responses[1]

        # Check AnalyzeResult
        assert returned_model.model_id == raw_analyze_result.model_id
        assert returned_model.api_version == raw_analyze_result.api_version
        assert returned_model.content == raw_analyze_result.content

        self.assertDocumentPagesTransformCorrect(returned_model.pages, raw_analyze_result.pages)
        self.assertDocumentStylesTransformCorrect(returned_model.styles, raw_analyze_result.styles)

        # check page range
        assert len(raw_analyze_result.pages) == len(returned_model.pages)
