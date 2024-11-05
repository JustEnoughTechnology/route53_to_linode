import linode_api4
import boto3


client = linode_api4.LinodeClient(token='YOUR_API_TOKEN')

domains = client.domains.list()

domain_list = []
for domain in domains:
    domain_list.append(domain['domain'])

print (domain_list)

