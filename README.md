# WordOps Website Backup to Amazon S3
This repository contains a Python script that automates the backup process for WordOps websites and their respective MySQL databases to Amazon S3. It allows you to schedule regular backups, ensuring that your website data is safely stored and easily accessible. The script is designed to be easy to configure and can be set up to run automatically via cron, providing a reliable and secure solution for your website backup needs.

## Prerequisites
Before you begin, ensure you have the following prerequisites installed on your system:

Python 3.6 or higher
Boto3 (AWS SDK for Python)
You can install Boto3 using pip:

```bash
pip install boto3

An Amazon S3 bucket to store the backups
AWS CLI configured with the necessary AWS access and secret keys
Configuration
Clone the repository to your local system:
bash
Copy code
git clone https://github.com/yourusername/wordops-s3-backup.git
Open the autobackup.py file in your favorite text editor.

Replace the s3_bucket_name variable with the name of your Amazon S3 bucket.

Update the websites list with the necessary information about your WordOps websites, including the local folder path, database name, database user, and database password.

```python
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
Save and close the autobackup.py file.
Usage
To run the backup script manually, navigate to the directory containing the autobackup.py file and run the following command:

```bash
python3 autobackup.py
To schedule the script to run automatically using cron, open your crontab configuration file:

```bash
crontab -e
Add the following line to the file, replacing /path/to/your/autobackup.py with the actual path to the autobackup.py file on your system:

```bash
0 0,12 * * * /usr/bin/python3 /path/to/your/autobackup.py
This will run the backup script twice a day, at 00:00 and 12:00.

Save the file and exit the editor. The script will now run automatically at the specified times, backing up your WordOps websites and their MySQL databases to Amazon S3.
