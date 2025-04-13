import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Bucket and file details
bucket_name = 'knowledge-v1'
file_content = 'Chao 1 lan nua'
s3_key = '460f021a-1427-4e04-ad89-05e5a959712f.png'  
def upload(bucket_name, s3_key, file_content):

    # Upload the string as a file
    s3.put_object(Bucket=bucket_name, Key=s3_key, Body=file_content)
    print(f"File '{s3_key}' uploaded to '{bucket_name}'")

def get(bucket_name, s3_key,local_path):
    """
    Download a file from an S3 bucket.

    :param bucket_name: Name of the S3 bucket
    :param s3_key: The key (path) of the file to download
    :return: The content of the downloaded file
    """
    # Download the file
    response = s3.get_object(Bucket=bucket_name, Key=s3_key)
    s3.download_file(bucket_name, s3_key, local_path)
    print("Download complete!")
def delete(bucket_name, s3_key):
    """
    Delete a file from an S3 bucket.
    :param bucket_name: Name of the S3 bucket
    :param s3_key: The key (path) of the file to delete
    """
    # Delete the file
    s3.delete_object(Bucket=bucket_name, Key=s3_key)
    print(f"File '{s3_key}' deleted from '{bucket_name}'")
def list_objects(bucket_name):
    """
    List all objects in an S3 bucket.
    :param bucket_name: Name of the S3 bucket
    :return: List of object keys in the bucket
    """
    # List objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        return [obj['Key'] for obj in response['Contents']]
    else:
        return []
def main():
    # # Upload a file
    # upload(bucket_name, s3_key, file_content)

    # List objects in the bucket
    objects = list_objects(bucket_name)
    print("Objects in bucket:", objects)

    # Download the file
    get(bucket_name, s3_key,'/Users/thanhtainguyen/Desktop/team9/realshit/kk.png')

    # # Delete the file
    # delete(bucket_name, s3_key)
if __name__ == "__main__":
    main()