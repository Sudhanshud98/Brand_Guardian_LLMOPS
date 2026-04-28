from azure.identity import DefaultAzureCredential

cred = DefaultAzureCredential()
token = cred.get_token("https://management.azure.com/.default")
print(token.token)