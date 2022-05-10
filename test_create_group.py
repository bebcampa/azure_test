from azure.mgmt.managementgroups import ManagementGroupsAPI
from azure.common.credentials import get_azure_cli_credentials
from azure.common.client_factorya import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient

def createmanagementgroup( strName ):
    subsClient = get_client_from_cli_profile(SubscriptionClient)
    subsRaw = []
    for sub in subsClient.subscriptions.list():
        subsRaw.append(sub.as_dict())
    subsList = []
    for sub in subsRaw:
        subsList.append(sub.get('subscription_id'))

    mgClient = get_client_from_cli_profile(ManagementGroupsAPI)
    mg_request = {'name': strName, 'display_name': strName}

    mg = mgClient.management_groups.create_or_update(group_id=strName,create_management_group_request=mg_request)

    print(mg)

createmanagementgroup("MyNewMG")