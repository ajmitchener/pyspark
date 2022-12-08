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
  #get s3 object
  result = s3_client.get_object(Bucket=bucketName, Key=filename)
  #Read a text file line by line using splitlines object
  final_document_array = ""
  for line in result["Body"].read().splitlines():
      each_line = line.decode('utf-8')
      print("Input Line : ",each_line)
      if(each_line!=''): #dont process empty lines
          translated=translate_text(each_line, 'bn')
          print("After translation : ",translated)
          final_document_array+=translated
          final_document_array+='\n\n'
  s3_client.put_object(Body=final_document_array, Bucket='outputtranslateddoc', Key=file_name)
  print("Done")
