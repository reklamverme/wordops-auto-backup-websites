# WordOps Website Backup to Amazon S3

This repository contains a Python script that automates the backup process for WordOps websites and their respective MySQL databases to Amazon S3. It allows you to schedule regular backups, ensuring that your website data is safely stored and easily accessible. The script is designed to be easy to configure and can be set up to run automatically via cron, providing a reliable and secure solution for your website backup needs.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

1. Python 3.6 or higher
2. [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (AWS SDK for Python)

You can install Boto3 using pip:

```bash
pip install boto3
