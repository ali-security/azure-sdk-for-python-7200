# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

"""
FILE: sample_analyze_orchestration_app_luis_response_async.py

DESCRIPTION:
    This sample demonstrates how to analyze user query using an orchestration project.
    In this sample, orchestration project's top intent will map to a LUIS project.

    For more info about how to setup a CLU orchestration project, see the README.

USAGE:
    python sample_analyze_orchestration_app_luis_response_async.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_CLU_ENDPOINT                       - endpoint for your CLU resource.
    2) AZURE_CLU_KEY                            - API key for your CLU resource.
    3) AZURE_CLU_ORCHESTRATION_PROJECT_NAME     - project name for your CLU orchestration project.
    4) AZURE_CLU_ORCHESTRATION_DEPLOYMENT_NAME  - deployment name for your CLU orchestration project.
"""

import asyncio

async def sample_analyze_orchestration_app_luis_response_async():
    # [START analyze_orchestration_app_luis_response_async]
    # import libraries
    import os
    from azure.core.credentials import AzureKeyCredential

    from azure.ai.language.conversations.aio import ConversationAnalysisClient
    from azure.ai.language.conversations.models import (
        CustomConversationalTask,
        ConversationAnalysisOptions,
        CustomConversationTaskParameters,
        TextConversationItem
    )

    # get secrets
    clu_endpoint = os.environ["AZURE_CLU_ENDPOINT"]
    clu_key = os.environ["AZURE_CLU_KEY"]
    project_name = os.environ["AZURE_CLU_ORCHESTRATION_PROJECT_NAME"]
    deployment_name = os.environ["AZURE_CLU_ORCHESTRATION_DEPLOYMENT_NAME"]

    # analyze query
    client = ConversationAnalysisClient(clu_endpoint, AzureKeyCredential(clu_key))
    async with client:
        query = "Reserve a table for 2 at the Italian restaurant"
        result = await client.analyze_conversation(
                task=CustomConversationalTask(
                    analysis_input=ConversationAnalysisOptions(
                        conversation_item=TextConversationItem(
                            text=query
                        )
                    ),
                    parameters=CustomConversationTaskParameters(
                        project_name=project_name,
                        deployment_name=deployment_name
                    )
                )
            )

        # view result
        print("query: {}".format(result.results.query))
        print("project kind: {}\n".format(result.results.prediction.project_kind))

        # top intent
        top_intent = result.results.prediction.top_intent
        print("top intent: {}".format(top_intent))
        top_intent_object = result.results.prediction.intents[top_intent]
        print("confidence score: {}".format(top_intent_object.confidence))
        print("project kind: {}".format(top_intent_object.target_kind))

        if top_intent_object.target_kind == "luis":
            print("\nluis response:")
            luis_response = top_intent_object.result["prediction"]
            print("top intent: {}".format(luis_response["topIntent"]))
            print("\nentities:")
            for entity in luis_response["entities"]:
                print("\n{}".format(entity))

    # [END analyze_orchestration_app_luis_response_async]


async def main():
    await sample_analyze_orchestration_app_luis_response_async()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())