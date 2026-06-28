import os
import boto3
from dotenv import load_dotenv

# .env ファイルから秘密の情報を読み込む
load_dotenv()

# .env からキーなどを取り出す
access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION")
bucket_name = os.getenv("S3_BUCKET_NAME")

# S3に接続する係を用意する
s3 = boto3.client(
    "s3",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region,
)

# S3に置くファイルの中身を用意する
content = "今日の運勢は大吉！クロード部長より"

# S3にファイルを置く（アップロード）
s3.put_object(
    Bucket=bucket_name,
    Key="fortune-from-code.txt",
    Body=content,
)

print("S3へのアップロードが完了しました！")
print(f"バケット名: {bucket_name}")
print("ファイル名: fortune-from-code.txt")