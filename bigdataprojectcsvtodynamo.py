import json
import csv
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    region = 'us-east-1'
    record_list = []
    try:
        s3 = boto3.client('s3')
        dynamodb = boto3.client('dynamodb', region_name = region)
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        csv_file = s3.get_object(Bucket = bucket, Key = key)
        
        record_list = csv_file['Body'].read().decode('utf-8').split('\n')
        
        csv_reader = csv.reader(record_list, delimiter = ',',quotechar = '"')
        
        for row in csv_reader:
            u_q = row[0]
            coolant = row[1]
            stator_winding = row[2]
            u_d = row[3]
            stator_tooth = row[4]
            motor_speed = row[5]
            i_d = row[6]
            i_q = row[7]
            pm = row[8]
            stator_yoke = row[9]
            ambient = row[10]
            torque = row[11]
            profile_id = row[12]
            id = row[13]
            
            add_to_db = dynamodb.put_item(TableName = 'pmsm_temperature', Item = {
                'u_q' : {'N': str(u_q)},
                'coolant' : {'N': str(coolant)},
                'stator_winding' : {'N': str(stator_winding)},
                'u_d' : {'N': str(u_d)},
                'stator_tooth' : {'N': str(stator_tooth)},
                'motor_speed' : {'N': str(motor_speed)},
                'i_d' : {'N': str(i_d)},
                'i_q' : {'N': str(i_q)},
                'pm' : {'N': str(pm)},
                'stator_yoke' : {'N': str(stator_yoke)},
                'ambient' : {'N': str(ambient)},
                'torque' : {'N': str(torque)},
                'profile_id' : {'N': str(profile_id)},
                'id' : {'N': str(id)},
                
            })
            

        
        
    except Exception as e:
        print(str(e))
    return {
        'statusCode': 200,
        'body': json.dumps('csv to dynamodb success')
    }
