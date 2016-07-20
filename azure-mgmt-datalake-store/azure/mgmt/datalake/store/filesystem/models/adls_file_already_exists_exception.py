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

from .adls_remote_exception import AdlsRemoteException


class AdlsFileAlreadyExistsException(AdlsRemoteException):
    """A WebHDFS exception thrown indicating the file or folder already exists.
    Thrown when a 403 error response code is returned (forbidden).

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

    def __init__(self):
        super(AdlsFileAlreadyExistsException, self).__init__()
        self.exception = 'FileAlreadyExistsException'
