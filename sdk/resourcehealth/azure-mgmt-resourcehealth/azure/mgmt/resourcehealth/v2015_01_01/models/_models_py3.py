# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class AvailabilityStatus(_serialization.Model):
    """availabilityStatus of a resource.

    :ivar id: Azure Resource Manager Identity for the availabilityStatuses resource.
    :vartype id: str
    :ivar name: current.
    :vartype name: str
    :ivar type: Microsoft.ResourceHealth/AvailabilityStatuses.
    :vartype type: str
    :ivar location: Azure Resource Manager geo location of the resource.
    :vartype location: str
    :ivar properties: Properties of availability state.
    :vartype properties: ~azure.mgmt.resourcehealth.v2015_01_01.models.AvailabilityStatusProperties
    """

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "properties": {"key": "properties", "type": "AvailabilityStatusProperties"},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        name: Optional[str] = None,
        type: Optional[str] = None,
        location: Optional[str] = None,
        properties: Optional["_models.AvailabilityStatusProperties"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword id: Azure Resource Manager Identity for the availabilityStatuses resource.
        :paramtype id: str
        :keyword name: current.
        :paramtype name: str
        :keyword type: Microsoft.ResourceHealth/AvailabilityStatuses.
        :paramtype type: str
        :keyword location: Azure Resource Manager geo location of the resource.
        :paramtype location: str
        :keyword properties: Properties of availability state.
        :paramtype properties:
         ~azure.mgmt.resourcehealth.v2015_01_01.models.AvailabilityStatusProperties
        """
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.properties = properties


class AvailabilityStatusListResult(_serialization.Model):
    """The List availabilityStatus operation response.

    All required parameters must be populated in order to send to Azure.

    :ivar value: The list of availabilityStatuses. Required.
    :vartype value: list[~azure.mgmt.resourcehealth.v2015_01_01.models.AvailabilityStatus]
    :ivar next_link: The URI to fetch the next page of availabilityStatuses. Call ListNext() with
     this URI to fetch the next page of availabilityStatuses.
    :vartype next_link: str
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[AvailabilityStatus]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: List["_models.AvailabilityStatus"], next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: The list of availabilityStatuses. Required.
        :paramtype value: list[~azure.mgmt.resourcehealth.v2015_01_01.models.AvailabilityStatus]
        :keyword next_link: The URI to fetch the next page of availabilityStatuses. Call ListNext()
         with this URI to fetch the next page of availabilityStatuses.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class AvailabilityStatusProperties(_serialization.Model):  # pylint: disable=too-many-instance-attributes
    """Properties of availability state.

    :ivar availability_state: Availability status of the resource. Known values are: "Available",
     "Unavailable", and "Unknown".
    :vartype availability_state: str or
     ~azure.mgmt.resourcehealth.v2015_01_01.models.AvailabilityStateValues
    :ivar summary: Summary description of the availability state.
    :vartype summary: str
    :ivar detailed_status: Details of the availability status.
    :vartype detailed_status: str
    :ivar reason_type: When the resource's availabilityState is Unavailable, it describes where the
     health impacting event was originated. Examples are planned, unplanned, user initiated or an
     outage etc.
    :vartype reason_type: str
    :ivar root_cause_attribution_time: When the resource's availabilityState is Unavailable, it
     provides the Timestamp for when the health impacting event was received.
    :vartype root_cause_attribution_time: ~datetime.datetime
    :ivar resolution_eta: When the resource's availabilityState is Unavailable and the reasonType
     is not User Initiated, it provides the date and time for when the issue is expected to be
     resolved.
    :vartype resolution_eta: ~datetime.datetime
    :ivar occured_time: Timestamp for when last change in health status occurred.
    :vartype occured_time: ~datetime.datetime
    :ivar reason_chronicity: Chronicity of the availability transition. Known values are:
     "Transient" and "Persistent".
    :vartype reason_chronicity: str or
     ~azure.mgmt.resourcehealth.v2015_01_01.models.ReasonChronicityTypes
    :ivar reported_time: Timestamp for when the health was last checked.
    :vartype reported_time: ~datetime.datetime
    :ivar is_arm_resource: flag to show if child resource need detail health.
    :vartype is_arm_resource: bool
    :ivar recently_resolved_state: An annotation describing a change in the availabilityState to
     Available from Unavailable with a reasonType of type Unplanned.
    :vartype recently_resolved_state:
     ~azure.mgmt.resourcehealth.v2015_01_01.models.AvailabilityStatusPropertiesRecentlyResolvedState
    :ivar recommended_actions: Lists actions the user can take based on the current
     availabilityState of the resource.
    :vartype recommended_actions:
     list[~azure.mgmt.resourcehealth.v2015_01_01.models.RecommendedAction]
    :ivar service_impacting_events: Lists the service impacting events that may be affecting the
     health of the resource.
    :vartype service_impacting_events:
     list[~azure.mgmt.resourcehealth.v2015_01_01.models.ServiceImpactingEvent]
    """

    _attribute_map = {
        "availability_state": {"key": "availabilityState", "type": "str"},
        "summary": {"key": "summary", "type": "str"},
        "detailed_status": {"key": "detailedStatus", "type": "str"},
        "reason_type": {"key": "reasonType", "type": "str"},
        "root_cause_attribution_time": {"key": "rootCauseAttributionTime", "type": "iso-8601"},
        "resolution_eta": {"key": "resolutionETA", "type": "iso-8601"},
        "occured_time": {"key": "occuredTime", "type": "iso-8601"},
        "reason_chronicity": {"key": "reasonChronicity", "type": "str"},
        "reported_time": {"key": "reportedTime", "type": "iso-8601"},
        "is_arm_resource": {"key": "isArmResource", "type": "bool"},
        "recently_resolved_state": {
            "key": "recentlyResolvedState",
            "type": "AvailabilityStatusPropertiesRecentlyResolvedState",
        },
        "recommended_actions": {"key": "recommendedActions", "type": "[RecommendedAction]"},
        "service_impacting_events": {"key": "serviceImpactingEvents", "type": "[ServiceImpactingEvent]"},
    }

    def __init__(
        self,
        *,
        availability_state: Optional[Union[str, "_models.AvailabilityStateValues"]] = None,
        summary: Optional[str] = None,
        detailed_status: Optional[str] = None,
        reason_type: Optional[str] = None,
        root_cause_attribution_time: Optional[datetime.datetime] = None,
        resolution_eta: Optional[datetime.datetime] = None,
        occured_time: Optional[datetime.datetime] = None,
        reason_chronicity: Optional[Union[str, "_models.ReasonChronicityTypes"]] = None,
        reported_time: Optional[datetime.datetime] = None,
        is_arm_resource: Optional[bool] = None,
        recently_resolved_state: Optional["_models.AvailabilityStatusPropertiesRecentlyResolvedState"] = None,
        recommended_actions: Optional[List["_models.RecommendedAction"]] = None,
        service_impacting_events: Optional[List["_models.ServiceImpactingEvent"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword availability_state: Availability status of the resource. Known values are:
         "Available", "Unavailable", and "Unknown".
        :paramtype availability_state: str or
         ~azure.mgmt.resourcehealth.v2015_01_01.models.AvailabilityStateValues
        :keyword summary: Summary description of the availability state.
        :paramtype summary: str
        :keyword detailed_status: Details of the availability status.
        :paramtype detailed_status: str
        :keyword reason_type: When the resource's availabilityState is Unavailable, it describes where
         the health impacting event was originated. Examples are planned, unplanned, user initiated or
         an outage etc.
        :paramtype reason_type: str
        :keyword root_cause_attribution_time: When the resource's availabilityState is Unavailable, it
         provides the Timestamp for when the health impacting event was received.
        :paramtype root_cause_attribution_time: ~datetime.datetime
        :keyword resolution_eta: When the resource's availabilityState is Unavailable and the
         reasonType is not User Initiated, it provides the date and time for when the issue is expected
         to be resolved.
        :paramtype resolution_eta: ~datetime.datetime
        :keyword occured_time: Timestamp for when last change in health status occurred.
        :paramtype occured_time: ~datetime.datetime
        :keyword reason_chronicity: Chronicity of the availability transition. Known values are:
         "Transient" and "Persistent".
        :paramtype reason_chronicity: str or
         ~azure.mgmt.resourcehealth.v2015_01_01.models.ReasonChronicityTypes
        :keyword reported_time: Timestamp for when the health was last checked.
        :paramtype reported_time: ~datetime.datetime
        :keyword is_arm_resource: flag to show if child resource need detail health.
        :paramtype is_arm_resource: bool
        :keyword recently_resolved_state: An annotation describing a change in the availabilityState to
         Available from Unavailable with a reasonType of type Unplanned.
        :paramtype recently_resolved_state:
         ~azure.mgmt.resourcehealth.v2015_01_01.models.AvailabilityStatusPropertiesRecentlyResolvedState
        :keyword recommended_actions: Lists actions the user can take based on the current
         availabilityState of the resource.
        :paramtype recommended_actions:
         list[~azure.mgmt.resourcehealth.v2015_01_01.models.RecommendedAction]
        :keyword service_impacting_events: Lists the service impacting events that may be affecting the
         health of the resource.
        :paramtype service_impacting_events:
         list[~azure.mgmt.resourcehealth.v2015_01_01.models.ServiceImpactingEvent]
        """
        super().__init__(**kwargs)
        self.availability_state = availability_state
        self.summary = summary
        self.detailed_status = detailed_status
        self.reason_type = reason_type
        self.root_cause_attribution_time = root_cause_attribution_time
        self.resolution_eta = resolution_eta
        self.occured_time = occured_time
        self.reason_chronicity = reason_chronicity
        self.reported_time = reported_time
        self.is_arm_resource = is_arm_resource
        self.recently_resolved_state = recently_resolved_state
        self.recommended_actions = recommended_actions
        self.service_impacting_events = service_impacting_events


class AvailabilityStatusPropertiesRecentlyResolvedState(_serialization.Model):
    """An annotation describing a change in the availabilityState to Available from Unavailable with a
    reasonType of type Unplanned.

    :ivar unavailable_occurred_time: Timestamp for when the availabilityState changed to
     Unavailable.
    :vartype unavailable_occurred_time: ~datetime.datetime
    :ivar resolved_time: Timestamp when the availabilityState changes to Available.
    :vartype resolved_time: ~datetime.datetime
    :ivar unavailability_summary: Brief description of cause of the resource becoming unavailable.
    :vartype unavailability_summary: str
    """

    _attribute_map = {
        "unavailable_occurred_time": {"key": "unavailableOccurredTime", "type": "iso-8601"},
        "resolved_time": {"key": "resolvedTime", "type": "iso-8601"},
        "unavailability_summary": {"key": "unavailabilitySummary", "type": "str"},
    }

    def __init__(
        self,
        *,
        unavailable_occurred_time: Optional[datetime.datetime] = None,
        resolved_time: Optional[datetime.datetime] = None,
        unavailability_summary: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword unavailable_occurred_time: Timestamp for when the availabilityState changed to
         Unavailable.
        :paramtype unavailable_occurred_time: ~datetime.datetime
        :keyword resolved_time: Timestamp when the availabilityState changes to Available.
        :paramtype resolved_time: ~datetime.datetime
        :keyword unavailability_summary: Brief description of cause of the resource becoming
         unavailable.
        :paramtype unavailability_summary: str
        """
        super().__init__(**kwargs)
        self.unavailable_occurred_time = unavailable_occurred_time
        self.resolved_time = resolved_time
        self.unavailability_summary = unavailability_summary


class ErrorResponse(_serialization.Model):
    """Error details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar details: The error details.
    :vartype details: str
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "details": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "details": {"key": "details", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None


class Operation(_serialization.Model):
    """Operation available in the resourcehealth resource provider.

    :ivar name: Name of the operation.
    :vartype name: str
    :ivar display: Properties of the operation.
    :vartype display: ~azure.mgmt.resourcehealth.v2015_01_01.models.OperationDisplay
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "display": {"key": "display", "type": "OperationDisplay"},
    }

    def __init__(
        self, *, name: Optional[str] = None, display: Optional["_models.OperationDisplay"] = None, **kwargs: Any
    ) -> None:
        """
        :keyword name: Name of the operation.
        :paramtype name: str
        :keyword display: Properties of the operation.
        :paramtype display: ~azure.mgmt.resourcehealth.v2015_01_01.models.OperationDisplay
        """
        super().__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(_serialization.Model):
    """Properties of the operation.

    :ivar provider: Provider name.
    :vartype provider: str
    :ivar resource: Resource name.
    :vartype resource: str
    :ivar operation: Operation name.
    :vartype operation: str
    :ivar description: Description of the operation.
    :vartype description: str
    """

    _attribute_map = {
        "provider": {"key": "provider", "type": "str"},
        "resource": {"key": "resource", "type": "str"},
        "operation": {"key": "operation", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword provider: Provider name.
        :paramtype provider: str
        :keyword resource: Resource name.
        :paramtype resource: str
        :keyword operation: Operation name.
        :paramtype operation: str
        :keyword description: Description of the operation.
        :paramtype description: str
        """
        super().__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationListResult(_serialization.Model):
    """Lists the operations response.

    All required parameters must be populated in order to send to Azure.

    :ivar value: List of operations available in the resourcehealth resource provider. Required.
    :vartype value: list[~azure.mgmt.resourcehealth.v2015_01_01.models.Operation]
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Operation]"},
    }

    def __init__(self, *, value: List["_models.Operation"], **kwargs: Any) -> None:
        """
        :keyword value: List of operations available in the resourcehealth resource provider. Required.
        :paramtype value: list[~azure.mgmt.resourcehealth.v2015_01_01.models.Operation]
        """
        super().__init__(**kwargs)
        self.value = value


class RecommendedAction(_serialization.Model):
    """Lists actions the user can take based on the current availabilityState of the resource.

    :ivar action: Recommended action.
    :vartype action: str
    :ivar action_url: Link to the action.
    :vartype action_url: str
    :ivar action_url_text: Substring of action, it describes which text should host the action url.
    :vartype action_url_text: str
    """

    _attribute_map = {
        "action": {"key": "action", "type": "str"},
        "action_url": {"key": "actionUrl", "type": "str"},
        "action_url_text": {"key": "actionUrlText", "type": "str"},
    }

    def __init__(
        self,
        *,
        action: Optional[str] = None,
        action_url: Optional[str] = None,
        action_url_text: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword action: Recommended action.
        :paramtype action: str
        :keyword action_url: Link to the action.
        :paramtype action_url: str
        :keyword action_url_text: Substring of action, it describes which text should host the action
         url.
        :paramtype action_url_text: str
        """
        super().__init__(**kwargs)
        self.action = action
        self.action_url = action_url
        self.action_url_text = action_url_text


class ServiceImpactingEvent(_serialization.Model):
    """Lists the service impacting events that may be affecting the health of the resource.

    :ivar event_start_time: Timestamp for when the event started.
    :vartype event_start_time: ~datetime.datetime
    :ivar event_status_last_modified_time: Timestamp for when event was submitted/detected.
    :vartype event_status_last_modified_time: ~datetime.datetime
    :ivar correlation_id: Correlation id for the event.
    :vartype correlation_id: str
    :ivar status: Status of the service impacting event.
    :vartype status: ~azure.mgmt.resourcehealth.v2015_01_01.models.ServiceImpactingEventStatus
    :ivar incident_properties: Properties of the service impacting event.
    :vartype incident_properties:
     ~azure.mgmt.resourcehealth.v2015_01_01.models.ServiceImpactingEventIncidentProperties
    """

    _attribute_map = {
        "event_start_time": {"key": "eventStartTime", "type": "iso-8601"},
        "event_status_last_modified_time": {"key": "eventStatusLastModifiedTime", "type": "iso-8601"},
        "correlation_id": {"key": "correlationId", "type": "str"},
        "status": {"key": "status", "type": "ServiceImpactingEventStatus"},
        "incident_properties": {"key": "incidentProperties", "type": "ServiceImpactingEventIncidentProperties"},
    }

    def __init__(
        self,
        *,
        event_start_time: Optional[datetime.datetime] = None,
        event_status_last_modified_time: Optional[datetime.datetime] = None,
        correlation_id: Optional[str] = None,
        status: Optional["_models.ServiceImpactingEventStatus"] = None,
        incident_properties: Optional["_models.ServiceImpactingEventIncidentProperties"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword event_start_time: Timestamp for when the event started.
        :paramtype event_start_time: ~datetime.datetime
        :keyword event_status_last_modified_time: Timestamp for when event was submitted/detected.
        :paramtype event_status_last_modified_time: ~datetime.datetime
        :keyword correlation_id: Correlation id for the event.
        :paramtype correlation_id: str
        :keyword status: Status of the service impacting event.
        :paramtype status: ~azure.mgmt.resourcehealth.v2015_01_01.models.ServiceImpactingEventStatus
        :keyword incident_properties: Properties of the service impacting event.
        :paramtype incident_properties:
         ~azure.mgmt.resourcehealth.v2015_01_01.models.ServiceImpactingEventIncidentProperties
        """
        super().__init__(**kwargs)
        self.event_start_time = event_start_time
        self.event_status_last_modified_time = event_status_last_modified_time
        self.correlation_id = correlation_id
        self.status = status
        self.incident_properties = incident_properties


class ServiceImpactingEventIncidentProperties(_serialization.Model):
    """Properties of the service impacting event.

    :ivar title: Title of the incident.
    :vartype title: str
    :ivar service: Service impacted by the event.
    :vartype service: str
    :ivar region: Region impacted by the event.
    :vartype region: str
    :ivar incident_type: Type of Event.
    :vartype incident_type: str
    """

    _attribute_map = {
        "title": {"key": "title", "type": "str"},
        "service": {"key": "service", "type": "str"},
        "region": {"key": "region", "type": "str"},
        "incident_type": {"key": "incidentType", "type": "str"},
    }

    def __init__(
        self,
        *,
        title: Optional[str] = None,
        service: Optional[str] = None,
        region: Optional[str] = None,
        incident_type: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword title: Title of the incident.
        :paramtype title: str
        :keyword service: Service impacted by the event.
        :paramtype service: str
        :keyword region: Region impacted by the event.
        :paramtype region: str
        :keyword incident_type: Type of Event.
        :paramtype incident_type: str
        """
        super().__init__(**kwargs)
        self.title = title
        self.service = service
        self.region = region
        self.incident_type = incident_type


class ServiceImpactingEventStatus(_serialization.Model):
    """Status of the service impacting event.

    :ivar value: Current status of the event.
    :vartype value: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "str"},
    }

    def __init__(self, *, value: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword value: Current status of the event.
        :paramtype value: str
        """
        super().__init__(**kwargs)
        self.value = value
