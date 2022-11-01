from google.cloud import speech
from google.cloud import storage
import io
import os

# Credencial JSON
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/nunesfi/Área de Trabalho/Magna/Projetos/DIPOL/Oitivas/scripts/credencial_json/dipol-sist-invest-dev-10dab1f88c35.json"

client = speech.SpeechClient()

# Listar audios do bucket
bucket_name = 'sp-app-oitiva-transcricao-dev'
client = storage.Client()
bucket = client.get_bucket(bucket_name)
blobs = list(client.list_blobs(bucket, fields="items(name)"))

for blob in blobs:
    print(blob)
    #teste