from flask import Flask, render_template, request, redirect, url_for
import boto3
from botocore.exceptions import NoCredentialsError

app = Flask(__name__)

# AWS S3 configuration
AWS_ACCESS_KEY_ID = 'AKIAXNVPZHOV3NRDTL4U'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'ap-south-1'
S3_BUCKET_NAME = 'flaskuploads3'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=AKIAXNVPZHOV3NRDTL4U,
                  aws_secret_access_key=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, region_name=ap-south-1)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        file_type = file.content_type

        # Validate file type (you may customize this based on your requirements)
        if file_type not in ['image/jpeg', 'image/png', 'application/pdf']:
            return "Invalid file type. Only JPEG, PNG, and PDF files are allowed."

        # Upload the file to S3
        s3.upload_fileobj(file, S3_BUCKET_NAME, file.filename)

        return f"File '{file.filename}' uploaded successfully."

    except NoCredentialsError:
        return "Credentials not available or incorrect."


if __name__ == "__main__":
    app.run(debug=True)

