"""Generating CloudFormation template.""" 
 
from troposphere import ( 
    GetAZs, 
    Output, 
    Parameter, 
    Ref, 
    Select, 
    Sub, 
    Tags, 
    Template, 
    GetAtt 
) 
 
from troposphere.ec2 import ( 
    VPC, 
    InternetGateway, 
    NetworkAcl, 
    NetworkAclEntry, 
    Route, 
    RouteTable, 
    Subnet, 
    SubnetNetworkAclAssociation, 
    SubnetRouteTableAssociation, 
    VPCGatewayAttachment, 
    EIP, 
    NatGateway, 
) 
 
t = Template() 
 
t.add_description("Effective DevOps in AWS: VPC, public and private subnets") 
