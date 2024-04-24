# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""
FILE: sample_all_operations.py
DESCRIPTION:
    These samples demonstrate sending, receiving, releasing, and acknowledging CloudEvents.
USAGE:
    python sample_all_operations.py
    Set the environment variables with your own values before running the sample:
    1) EVENTGRID_KEY - The access key of your eventgrid account.
    2) EVENTGRID_ENDPOINT - The namespace endpoint. Typically it exists in the format
    "https://<YOUR-NAMESPACE-NAME>.<REGION-NAME>.eventgrid.azure.net".
    3) EVENTGRID_TOPIC_NAME - The namespace topic name.
    4) EVENTGRID_EVENT_SUBSCRIPTION_NAME - The event subscription name.
"""
import os
import asyncio
from azure.core.credentials import AzureKeyCredential
from azure.eventgrid.models import *
from azure.core.messaging import CloudEvent
from azure.core.exceptions import HttpResponseError
from azure.eventgrid import EventGridClient

EVENTGRID_KEY: str = os.environ["EVENTGRID_KEY"]
EVENTGRID_ENDPOINT: str = os.environ["EVENTGRID_ENDPOINT"]
TOPIC_NAME: str = os.environ["EVENTGRID_TOPIC_NAME"]
EVENT_SUBSCRIPTION_NAME: str = os.environ["EVENTGRID_EVENT_SUBSCRIPTION_NAME"]


# Create a client
client = EventGridClient(EVENTGRID_ENDPOINT, AzureKeyCredential(EVENTGRID_KEY))


cloud_event_reject = CloudEvent(data="reject", source="https://example.com", type="example")
cloud_event_release = CloudEvent(data="release", source="https://example.com", type="example")
cloud_event_ack = CloudEvent(data="acknowledge", source="https://example.com", type="example")

# Publish a CloudEvent
try:
    client.send(topic_name=TOPIC_NAME, events=cloud_event_reject)
except HttpResponseError:
    raise

# Publish a list of CloudEvents
try:
    list_of_cloud_events = [cloud_event_release, cloud_event_ack]
    client.send(topic_name=TOPIC_NAME, events=list_of_cloud_events)
except HttpResponseError:
    raise

# Receive Published Cloud Events
try:
    receive_results = client.receive_cloud_events(
        topic_name=TOPIC_NAME,
        subscription_name=EVENT_SUBSCRIPTION_NAME,
        max_events=10,
        max_wait_time=10,
    )
except HttpResponseError:
    raise

# Iterate through the results and collect the lock tokens for events we want to release/acknowledge/reject:

release_events = []
acknowledge_events = []
reject_events = []

for detail in receive_results.value:
    data = detail.event.data
    broker_properties = detail.broker_properties
    if data == "release":
        release_events.append(broker_properties.lock_token)
    elif data == "acknowledge":
        acknowledge_events.append(broker_properties.lock_token)
    else:
        reject_events.append(broker_properties.lock_token)

# Release/Acknowledge/Reject events

if len(release_events) > 0:
    try:
        release_result = client.release_cloud_events(
            topic_name=TOPIC_NAME,
            subscription_name=EVENT_SUBSCRIPTION_NAME,
            lock_tokens=release_events,
        )
    except HttpResponseError:
        raise

    for succeeded_lock_token in release_result.succeeded_lock_tokens:
        print(f"Succeeded Lock Token:{succeeded_lock_token}")

if len(acknowledge_events) > 0:
    try:
        ack_result = client.acknowledge_cloud_events(
            topic_name=TOPIC_NAME,
            subscription_name=EVENT_SUBSCRIPTION_NAME,
            lock_tokens=acknowledge_events,
        )
    except HttpResponseError:
        raise

    for succeeded_lock_token in ack_result.succeeded_lock_tokens:
        print(f"Succeeded Lock Token:{succeeded_lock_token}")

if len(reject_events) > 0:
    try:
        reject_result = client.reject_cloud_events(
            topic_name=TOPIC_NAME,
            subscription_name=EVENT_SUBSCRIPTION_NAME,
            lock_tokens=reject_events,
        )
    except HttpResponseError:
        raise

    for succeeded_lock_token in reject_result.succeeded_lock_tokens:
        print(f"Succeeded Lock Token:{succeeded_lock_token}")
