from qcloud_cos import CosConfig, CosS3Client
import sys
import logging

import requests

from config import Config

class TencentCloudCOS:
    def __init__(self, secret_id, secret_key, region, bucket_name):
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.region = region
        self.bucket_name = bucket_name

        # 配置 COS 客户端
        self.config = CosConfig(Region=self.region, SecretId=self.secret_id, SecretKey=self.secret_key)
        self.client = CosS3Client(self.config)

    def upload_file(self, local_file_path, cos_file_key):
        """上传文件到 COS"""
        try:
            response = self.client.put_object(
                Bucket=self.bucket_name,
                Body=open(local_file_path, 'rb'),
                Key=cos_file_key,
                EnableMD5=False
            )
            logging.info(f"File uploaded successfully: {response['ETag']}")
            return response
        except Exception as e:
            logging.error(f"Failed to upload file: {str(e)}")
            return None

    def download_file(self, cos_file_key, local_file_path):
        """从 COS 下载文件"""
        try:
            response = self.client.get_object(
                Bucket=self.bucket_name,
                Key=cos_file_key
            )
            with open(local_file_path, 'wb') as f:
                f.write(response['Body'].get_raw_stream().read())
            logging.info(f"File downloaded successfully: {local_file_path}")
            return True
        except Exception as e:
            logging.error(f"Failed to download file: {str(e)}")
            return False

    def delete_file(self, cos_file_key):
        """从 COS 删除文件"""
        try:
            response = self.client.delete_object(
                Bucket=self.bucket_name,
                Key=cos_file_key
            )
            logging.info(f"File deleted successfully: {cos_file_key}")
            return response
        except Exception as e:
            logging.error(f"Failed to delete file: {str(e)}")
            return None

_instance = None

def get_origin_file_cos_instance(region = 'ap-guangzhou', bucket_name = 'original-research-1328064767'):
    global _instance
    if _instance is None:
        _instance = TencentCloudCOS(Config.COS_SECRET_ID, Config.COS_SECRET_KEY, 
                                    region, bucket_name )
    return _instance




# 使用示例
if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    secret_id = Config.COS_SECRET_ID
    secret_key = Config.COS_SECRET_KEY
    region = 'ap-guangzhou'
    bucket_name = 'original-research-1328064767'

    cos_tool = TencentCloudCOS(secret_id, secret_key, region, bucket_name)

    # 上传文件
    # res = cos_tool.upload_file('/Users/leefeng/Downloads/intensity-segments.pdf', '/Users/leefeng/Downloads/intensity-segments.pdf')

    # 下载文件
    cos_tool.download_file('/Users/leefeng/Downloads/intensity-segments.pdf', '/Users/leefeng/Downloads/test/intensity-segments.pdf')

    # 删除文件
    # cos_tool.delete_file('/Users/leefeng/Downloads/intensity-segments.pdf')


