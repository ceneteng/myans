#!/usr/bin/python

import boto3

regions = ['us-east-1']

invfile = open("inventory/ansible-nodes", "r+")
invcur = invfile.readlines()
invnew = []
terminated = []

invfile.seek(0)
for item in regions:
    ec2 = boto3.resource('ec2',region_name=item)
    print("Listing instances in " + item)
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['terminated']}])
    for instance in instances:
        terminated.append(instance.id)

for line in invcur:
    if any(s in line for s in terminated):
        continue
    else:
        invfile.write(line)


invfile.truncate()
invfile.close()