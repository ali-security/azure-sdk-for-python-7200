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

from .catalog_item import CatalogItem


class USqlProcedure(CatalogItem):
    """A Data Lake Analytics catalog U-SQL procedure item.

    :param compute_account_name: the name of the Data Lake Analytics account.
    :type compute_account_name: str
    :param version: the version of the catalog item.
    :type version: str
    :param database_name: the name of the database.
    :type database_name: str
    :param schema_name: the name of the schema associated with this procedure
     and database.
    :type schema_name: str
    :param name: the name of the procedure.
    :type name: str
    :param definition: the defined query of the procedure.
    :type definition: str
    """

    _attribute_map = {
        'compute_account_name': {'key': 'computeAccountName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'schema_name': {'key': 'schemaName', 'type': 'str'},
        'name': {'key': 'procName', 'type': 'str'},
        'definition': {'key': 'definition', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(USqlProcedure, self).__init__(**kwargs)
        self.database_name = kwargs.get('database_name', None)
        self.schema_name = kwargs.get('schema_name', None)
        self.name = kwargs.get('name', None)
        self.definition = kwargs.get('definition', None)
