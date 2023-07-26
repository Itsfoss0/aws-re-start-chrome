import boto3

 

def lambda_handler(event, context):

    source_bucket_name = 'my-source-bucket-nzuki'
    destination_bucket_name = 'my-destination-bucket-nzuki'

 

    # Initialize the Boto3 S3 client
    s3_client = boto3.client('s3')

 

    try:
        # List all objects in the source bucket
        response = s3_client.list_objects_v2(Bucket=source_bucket_name)

 

        if 'Contents' in response:
            for obj in response['Contents']:
                source_key = obj['Key']

 

                # Prepare the source and destination objects for the copy operation
                copy_source = {'Bucket': source_bucket_name, 'Key': source_key}

 

                # Copy the object from the source to the destination bucket with the same key
                s3_client.copy_object(Bucket=destination_bucket_name, CopySource=copy_source, Key=source_key)
                print(f"Successfully copied object: s3://{source_bucket_name}/{source_key} to s3://{destination_bucket_name}/{source_key}")

 

        else:
            print("Source bucket is empty. Nothing to copy.")
    except Exception as e:
        print(f"Error copying objects: {e}")
        raise e
