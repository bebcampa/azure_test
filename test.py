from azure.identity import ClientSecretCredential
from msgraph.core import GraphClient
import json

clientid= ""
clientsecret = ""
tenantid = ""


credentials=ClientSecretCredential(tenant_id=tenantid,client_id=clientid,client_secret=clientsecret) 
graph_client = GraphClient(credential=credentials)

users = graph_client.get('/users')
groups = graph_client._graph_url('https://graph.microsoft.com/v1.0/groups')


print(users.json())
print("------------")
