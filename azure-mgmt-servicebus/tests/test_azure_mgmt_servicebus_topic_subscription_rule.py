﻿# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
import unittest

import azure.mgmt.servicebus.models
from azure.mgmt.servicebus.models import SBNamespace,SBSku,SkuName,SBTopic,SBSubscription,Rule,Action,SqlFilter,FilterType,CorrelationFilter,SqlRuleAction
from azure.common.credentials import ServicePrincipalCredentials

from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer


class MgmtServiceBusTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtServiceBusTest, self).setUp()

        self.servicebus_client = self.create_mgmt_client(
            azure.mgmt.servicebus.ServiceBusManagementClient
        )

    @ResourceGroupPreparer()
    def test_sb_rule_curd(self, resource_group, location):
        # List all topic types
        resource_group_name = resource_group.name  # "ardsouza-resourcemovetest-group2"

        # Create a Namespace
        namespace_name = "testingpythontestcase"

        test = SBNamespace(location, {'tag1': 'value1', 'tag2': 'value2'}, SBSku(SkuName.standard))
        creatednamespace = self.servicebus_client.namespaces.create_or_update(resource_group_name, namespace_name, test)
        creatednamespace = creatednamespace.result()
        self.assertEqual(creatednamespace.name, namespace_name)


        # Create a Topic
        topic_name = "testingpythonsdktopic"
        createtopicresponse = self.servicebus_client.topics.create_or_update(resource_group_name, namespace_name,topic_name,SBTopic())
        self.assertEqual(createtopicresponse.name, topic_name)

        # Get the created Topic
        gettopicresponse = self.servicebus_client.topics.get(resource_group_name, namespace_name,topic_name)
        self.assertEqual(gettopicresponse.name, topic_name)

        # Create subscription
        subscription_name = "testingpythonsdksubscription"
        createsubscriptionresponse =self.servicebus_client.subscriptions.create_or_update(resource_group_name, namespace_name,topic_name,subscription_name,SBSubscription())
        self.assertEqual(createsubscriptionresponse.name, subscription_name)

        # Get created subscription
        getsubscriptionresponse = self.servicebus_client.subscriptions.get(resource_group_name,namespace_name, topic_name,subscription_name)
        self.assertEqual(getsubscriptionresponse.name, subscription_name)

        # create rule
        rule_name = "testingpythonsdkrule"
        createruleresponse = self.servicebus_client.rules.create_or_update(resource_group_name,namespace_name, topic_name,subscription_name,rule_name,Rule())
        self.assertEqual(createruleresponse.name, rule_name)

        # get create rule
        getruleresponse = self.servicebus_client.rules.get(resource_group_name, namespace_name,topic_name, subscription_name, rule_name)
        self.assertEqual(getruleresponse.name, rule_name)

        # get all rules
        getallrulesresponse = list(self.servicebus_client.rules.list_by_subscriptions(resource_group_name, namespace_name, topic_name,subscription_name))
        self.assertEqual(len(getallrulesresponse),1)

        # update create rule with filter and action
        strSqlExp = "myproperty='test'"
        ruleparameter = Rule(None,FilterType.sql_filter,SqlFilter(sql_expression=strSqlExp),None)
        createruleresponse = self.servicebus_client.rules.create_or_update(resource_group_name, namespace_name,topic_name, subscription_name, rule_name,ruleparameter)
        self.assertEqual(createruleresponse.name, rule_name)

        # Delete the created subscription
        self.servicebus_client.subscriptions.delete(resource_group_name, namespace_name, topic_name, subscription_name)

        # delete the Topic
        self.servicebus_client.topics.delete(resource_group_name, namespace_name, topic_name)

        # Delete the create namespace
        deletenamespace = self.servicebus_client.namespaces.delete(resource_group_name, namespace_name)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()