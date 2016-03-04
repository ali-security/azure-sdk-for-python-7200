# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Contact(Model):
    """
    Contact information for domain registration. If 'Domain Privacy' option is
    not selected then the contact information will be  be made publicly
    available through the Whois directories as per ICANN requirements.

    :param Address address_mailing: Mailing address
    :param str email: Email address
    :param str fax: Fax number
    :param str job_title: Job title
    :param str name_first: First name
    :param str name_last: Last name
    :param str name_middle: Middle name
    :param str organization: Organization
    :param str phone: Phone number
    """ 

    _attribute_map = {
        'address_mailing': {'key': 'addressMailing', 'type': 'Address'},
        'email': {'key': 'email', 'type': 'str'},
        'fax': {'key': 'fax', 'type': 'str'},
        'job_title': {'key': 'jobTitle', 'type': 'str'},
        'name_first': {'key': 'nameFirst', 'type': 'str'},
        'name_last': {'key': 'nameLast', 'type': 'str'},
        'name_middle': {'key': 'nameMiddle', 'type': 'str'},
        'organization': {'key': 'organization', 'type': 'str'},
        'phone': {'key': 'phone', 'type': 'str'},
    }

    def __init__(self, address_mailing=None, email=None, fax=None, job_title=None, name_first=None, name_last=None, name_middle=None, organization=None, phone=None, **kwargs):
        self.address_mailing = address_mailing
        self.email = email
        self.fax = fax
        self.job_title = job_title
        self.name_first = name_first
        self.name_last = name_last
        self.name_middle = name_middle
        self.organization = organization
        self.phone = phone
