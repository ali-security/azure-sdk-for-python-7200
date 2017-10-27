# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class FaceOperations(object):
    """FaceOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def find_similar(
            self, face_id, face_list_id=None, face_ids=None, max_num_of_candidates_returned=20, mode="matchPerson", custom_headers=None, raw=False, **operation_config):
        """Given query face's faceId, find the similar-looking faces from a faceId
        array or a faceListId.

        :param face_id: FaceId of the query face. User needs to call Face -
         Detect first to get a valid faceId. Note that this faceId is not
         persisted and will expire 24 hours after the detection call
        :type face_id: str
        :param face_list_id: An existing user-specified unique candidate face
         list, created in Face List - Create a Face List. Face list contains a
         set of persistedFaceIds which are persisted and will never expire.
         Parameter faceListId and faceIds should not be provided at the same
         time
        :type face_list_id: str
        :param face_ids: An array of candidate faceIds. All of them are
         created by Face - Detect and the faceIds will expire 24 hours after
         the detection call.
        :type face_ids: list[str]
        :param max_num_of_candidates_returned: The number of top similar faces
         returned. The valid range is [1, 1000].
        :type max_num_of_candidates_returned: int
        :param mode: Similar face searching mode. It can be "matchPerson" or
         "matchFace". Possible values include: 'matchPerson', 'matchFace'
        :type mode: str or ~azure.cognitiveservices.vision.face.models.enum
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.cognitiveservices.vision.face.models.SimilarFaceResult] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.FindSimilarRequest(face_id=face_id, face_list_id=face_list_id, face_ids=face_ids, max_num_of_candidates_returned=max_num_of_candidates_returned, mode=mode)

        # Construct URL
        url = '/findsimilars'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'FindSimilarRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[SimilarFaceResult]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def group(
            self, face_ids, custom_headers=None, raw=False, **operation_config):
        """Divide candidate faces into groups based on face similarity.

        :param face_ids: Array of candidate faceId created by Face - Detect.
         The maximum is 1000 faces
        :type face_ids: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: GroupResponse or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.GroupResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.GroupRequest(face_ids=face_ids)

        # Construct URL
        url = '/group'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'GroupRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GroupResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def identify(
            self, person_group_id, face_ids, max_num_of_candidates_returned=1, confidence_threshold=None, custom_headers=None, raw=False, **operation_config):
        """Identify unknown faces from a person group.

        :param person_group_id: personGroupId of the target person group,
         created by PersonGroups.Create
        :type person_group_id: str
        :param face_ids: Array of candidate faceId created by Face - Detect.
        :type face_ids: list[str]
        :param max_num_of_candidates_returned: The number of top similar faces
         returned.
        :type max_num_of_candidates_returned: int
        :param confidence_threshold: Confidence threshold of identification,
         used to judge whether one face belong to one person.
        :type confidence_threshold: float
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.cognitiveservices.vision.face.models.IdentifyResultItem]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.IdentifyRequest(person_group_id=person_group_id, face_ids=face_ids, max_num_of_candidates_returned=max_num_of_candidates_returned, confidence_threshold=confidence_threshold)

        # Construct URL
        url = '/identify'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'IdentifyRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[IdentifyResultItem]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def verify(
            self, face_id, person_id, person_group_id, custom_headers=None, raw=False, **operation_config):
        """Verify whether two faces belong to a same person or whether one face
        belongs to a person.

        :param face_id: faceId the face, comes from Face - Detect
        :type face_id: str
        :param person_id: Specify a certain person in a person group. personId
         is created in Persons.Create.
        :type person_id: str
        :param person_group_id: Using existing personGroupId and personId for
         fast loading a specified person. personGroupId is created in Person
         Groups.Create.
        :type person_group_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VerifyResult or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.VerifyResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.VerifyRequest(face_id=face_id, person_id=person_id, person_group_id=person_group_id)

        # Construct URL
        url = '/verify'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'VerifyRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VerifyResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def detect(
            self, url, return_face_id=True, return_face_landmarks=False, return_face_attributes=None, custom_headers=None, raw=False, **operation_config):
        """Detect human faces in an image and returns face locations, and
        optionally with faceIds, landmarks, and attributes.

        :param url:
        :type url: str
        :param return_face_id: A value indicating whether the operation should
         return faceIds of detected faces.
        :type return_face_id: bool
        :param return_face_landmarks: A value indicating whether the operation
         should return landmarks of the detected faces.
        :type return_face_landmarks: bool
        :param return_face_attributes: Analyze and return the one or more
         specified face attributes in the comma-separated string like
         "returnFaceAttributes=age,gender". Supported face attributes include
         age, gender, headPose, smile, facialHair, glasses and emotion. Note
         that each face attribute analysis has additional computational and
         time cost.
        :type return_face_attributes: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~azure.cognitiveservices.vision.face.models.DetectedFace]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        image_url = models.ImageUrl(url=url)

        # Construct URL
        url = '/detect'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if return_face_id is not None:
            query_parameters['returnFaceId'] = self._serialize.query("return_face_id", return_face_id, 'bool')
        if return_face_landmarks is not None:
            query_parameters['returnFaceLandmarks'] = self._serialize.query("return_face_landmarks", return_face_landmarks, 'bool')
        if return_face_attributes is not None:
            query_parameters['returnFaceAttributes'] = self._serialize.query("return_face_attributes", return_face_attributes, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(image_url, 'ImageUrl')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[DetectedFace]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def detect_in_stream(
            self, image, return_face_id=True, return_face_landmarks=False, return_face_attributes=None, custom_headers=None, raw=False, callback=None, **operation_config):
        """Detect human faces in an image and returns face locations, and
        optionally with faceIds, landmarks, and attributes.

        :param image: An image stream.
        :type image: Generator
        :param return_face_id: A value indicating whether the operation should
         return faceIds of detected faces.
        :type return_face_id: bool
        :param return_face_landmarks: A value indicating whether the operation
         should return landmarks of the detected faces.
        :type return_face_landmarks: bool
        :param return_face_attributes: Analyze and return the one or more
         specified face attributes in the comma-separated string like
         "returnFaceAttributes=age,gender". Supported face attributes include
         age, gender, headPose, smile, facialHair, glasses and emotion. Note
         that each face attribute analysis has additional computational and
         time cost.
        :type return_face_attributes: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~azure.cognitiveservices.vision.face.models.DetectedFace]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = '/detect'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if return_face_id is not None:
            query_parameters['returnFaceId'] = self._serialize.query("return_face_id", return_face_id, 'bool')
        if return_face_landmarks is not None:
            query_parameters['returnFaceLandmarks'] = self._serialize.query("return_face_landmarks", return_face_landmarks, 'bool')
        if return_face_attributes is not None:
            query_parameters['returnFaceAttributes'] = self._serialize.query("return_face_attributes", return_face_attributes, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/octet-stream'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._client.stream_upload(image, callback)

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[DetectedFace]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
