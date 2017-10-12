import boto3

session = boto3.Session(profile_name='dev')
s3 = session.resource('s3')
s3client = session.client('s3')

for bucket in s3.buckets.all():
  print(bucket.name)
  response = s3client.delete_bucket(
    Bucket=bucket.name
  )
  print(response)
