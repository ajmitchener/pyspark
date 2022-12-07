import json
import boto3

s3_client = boto3.client(service_name='s3')
translate = boto3.client(service_name='translate')

def translate_text(text, lang_code):
  result = translate.translate_text(
    Text=text,
    SourceLanguageCode='auto'
    TargetLanguageCode='lang_code'
  )
  return result['TranslatedText']

def lambda_handler(event, context):
  filename  = event['Records'][0]['s3']['object']['key']  
  bucket    = event['Records'][0]['s3']['bucket']['name']
  outfile = "s3://<bucket>/{}".format(filename)
  
  print("Event details : ", event)
  print("Input Filename : ", filename)
