from azure.identity import ClientSecretCredential
from msgraph.core import GraphClient
import json

clientid= "67f62bc8-c664-4e63-9d44-128673cdc0c2"
clientsecret = "5Ld8Q~.e5FpnjO50cpOn1vKdFaNXXbS6Gh_Aaa6Y"
tenantid = "e849ddc8-20b6-406a-aded-d8e20d57e4f0"


credentials=ClientSecretCredential(tenant_id=tenantid,client_id=clientid,client_secret=clientsecret) 
graph_client = GraphClient(credential=credentials)

users = graph_client.get('/users')
groups = graph_client._graph_url('https://graph.microsoft.com/v1.0/groups')


print(users.json())
print("------------")
