import json
#import python library
import boto3

def lambda_handler(event, context):
    
    # conenct to DynamoDB resource
    
    client = boto3.resource('dynamodb', region_name = 'us-east-1')
    
    #Creating the visitor count and incrementing it when somebody visits
    #Stored in our visitorCount table
    
    #Create a DynamoDB client to visitor_count table 
    table = client.Table('visitor_count')
    
    #update attribute (visitor_count), updates visitor_count for index.html
    response = table.update_item(
        Key={
            'path': 'index.html'
        }, 
        AttributeUpdates={
            'visitor_count':{ 
                'Value' : 1, 
                'Action': 'ADD'
            }
        }
        )
    # get visitor_count from the visitor_count table for index.html 
    
    response = table.get_item(
        Key={
            'path':'index.html'
        }
        )
    #We want to print to debug so we can see both the item and the visitor count printed on seperate lines when we look on cloudwatch's log groups
    # we will assign it to a variable so we only call it when we want to
    visitor_count = (response['Item']['visitor_count'])
        
    
    return {
        'statusCode': 200,
        'headers':{
            'Access-Control-Allow-Origin': '*'
        },
        'body': visitor_count
    }
