import os
import subprocess
import boto3
from datetime import datetime

def backup_wordops_website_to_s3(bucket_name, local_folder, db_name, db_user, db_password):
    s3_client = boto3.client('s3')
    site_name = local_folder.split('/')[-2]
    backup_filename = f'{site_name}_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.tar.gz'
    temp_folder = '/tmp'
    backup_filepath = os.path.join(temp_folder, backup_filename)

    # MySQL veritabanı yedeğini alın
    mysql_backup_filename = f'{site_name}_mysql_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.sql'
    mysql_backup_filepath = os.path.join(temp_folder, mysql_backup_filename)
    subprocess.run(['mysqldump', '-u', db_user, f'-p{db_password}', db_name, '-r', mysql_backup_filepath], check=True)

    # Yedek dosyasını oluşturun (web sitesi dosyaları ve MySQL veritabanı yedeğini dahil edin)
    subprocess.run(['tar', 'czf', backup_filepath, '-C', local_folder, '.', '-C', temp_folder, mysql_backup_filename], check=True)

    # MySQL veritabanı yedeğini silin
    os.remove(mysql_backup_filepath)

    with open(backup_filepath, 'rb') as backup_file:
        s3_client.upload_fileobj(backup_file, bucket_name, backup_filename)

    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=site_name)

    if 'Contents' in response:
        objects = sorted(response['Contents'], key=lambda obj: obj['LastModified'])

        while len(objects) > 10:
            s3_client.delete_object(Bucket=bucket_name, Key=objects[0]['Key'])
            objects.pop(0)

    print(f'Yedek başarıyla {bucket_name} S3 bucketına yüklendi: {backup_filename}')

if __name__ == '__main__':
    s3_bucket_name = 's3_bucket_name'
    websites = [
        {
            'local_folder': '/var/www/example.com/htdocs',
            'db_name': 'example_db',
            'db_user': 'root',
            'db_password': 'your_database_password'
        },
        {
            'local_folder': '/var/www/anotherexample.com/htdocs',
            'db_name': 'anotherexample_db',
            'db_user': 'root',
            'db_password': 'your_database_password'
        }
    ]
    for website in websites:
        backup_wordops_website_to_s3(
            s3_bucket_name,
            website['local_folder'],
            website['db_name'],
            website['db_user'],
            website['db_password']
        )
