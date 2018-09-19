import json
import boto3

def lambda_handler(event, context):
    region = "us-east-1"
    ec2 = boto3.resource('ec2', region_name=region)
    client = boto3.client('ec2', region_name=region)
    vFilter = [{'Name':'tag:Name', 'Values':['DevelopmentVPC']}]
    vpcs = list(ec2.vpcs.filter(Filters=vFilter))
    vIds = []
    instances = ec2.instances.all()
    for vpc in vpcs:
    	for tag in vpc.tags:
    	    if tag["Value"] == "DevelopmentVPC":
    		vIds.append(vpc.vpc_id)
    print vIds
    
    for instance in instances:
        print "instance iter"
    	vols = instance.volumes.all()
    	if instance.vpc_id in vIds:
    		print instance.tags
    		for v in vols:
    		    print "vols iter"
    		    v.create_snapshot(Description = instance.instance_id)
    print "Collecting snapshots"
    ss=ec2.snapshots.filter(Filters=[{'Name': 'owner-id', 'Values': ['896917285996']}])
    print "Snapshots collected"
    for snap in ss:
        snap.wait_until_completed()
    print "snap done"
    
    for instance in instances:
            vols = instance.volumes.all()
            if instance.vpc_id in vIds:
                if 'NAT' not in [t['Value'] for t in instance.tags]:
                    instance.terminate()

                        