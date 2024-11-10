import boto3
import os

def download_images_s3(files_to_download, bucket_name='dermamarker-v2', local_directory="all_images_short"):
    s3 = boto3.client('s3')

    downloaded_images = []

    for file_key in files_to_download:
        local_path = os.path.join(local_directory, os.path.basename(file_key))
        
        try:
            # Download the file from S3 to the local path
            s3.download_file(bucket_name, file_key, local_path)
            print(f"Downloaded: {file_key} to {local_path}")
            downloaded_images.append(local_path)
        except Exception as e:
            print(f"Error downloading {file_key}: {e}")

    return downloaded_images

def delete_local_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print(f"File not found: {file_path}")
