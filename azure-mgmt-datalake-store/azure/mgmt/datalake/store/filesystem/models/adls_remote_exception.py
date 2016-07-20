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

from msrest.serialization import Model


class AdlsRemoteException(Model):
    """Data Lake Store filesystem exception based on the WebHDFS definition for
    RemoteExceptions.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar java_class_name: the full class package name for the exception
     thrown, such as 'java.lang.IllegalArgumentException'.
    :vartype java_class_name: str
    :ivar message: the message associated with the exception that was thrown,
     such as 'Invalid value for webhdfs parameter "permission":...'.
    :vartype message: str
    :param exception: Polymorphic Discriminator
    :type exception: str
    """ 

    _validation = {
        'java_class_name': {'readonly': True},
        'message': {'readonly': True},
        'exception': {'required': True},
    }

    _attribute_map = {
        'java_class_name': {'key': 'javaClassName', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'exception': {'key': 'exception', 'type': 'str'},
    }

    _subtype_map = {
        'exception': {'IllegalArgumentException': 'AdlsIllegalArgumentException', 'UnsupportedOperationException': 'AdlsUnsupportedOperationException', 'SecurityException': 'AdlsSecurityException', 'IOException': 'AdlsIOException', 'FileNotFoundException': 'AdlsFileNotFoundException', 'FileAlreadyExistsException': 'AdlsFileAlreadyExistsException', 'BadOffsetException': 'AdlsBadOffsetException', 'RuntimeException': 'AdlsRuntimeException', 'AccessControlException': 'AdlsAccessControlException'}
    }

    def __init__(self):
        self.java_class_name = None
        self.message = None
        self.exception = None
