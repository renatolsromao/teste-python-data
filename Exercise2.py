import boto3
import os
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIAVDFFZZLLBUNHFTN3'
SECRET_KEY = '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'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

uploaded = upload_to_aws('C:/Users/' + os.getlogin() + '/Desktop/openLib.json', 'rlsr-teste-python-data', 'Exercise2_Python_Teste')