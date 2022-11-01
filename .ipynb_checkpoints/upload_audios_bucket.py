from google.cloud import storage
import os

#Credencial JSON
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/nunesfi/Área de Trabalho/Magna/Projetos/DIPOL/Oitivas/scripts/credencial_json/dipol-sist-invest-dev-10dab1f88c35.json"

#Bucket Google Storage
bucket_name = "sp-app-oitiva-transcricao-dev"

# realizar upload de todos os áudios ao bucket

count = 0
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
for root, dirs, files in os.walk('/home/nunesfi/Área de Trabalho/Magna/Projetos/DIPOL/Oitivas/audios_dev_homol/Dev/Oitivas_Ambiente_DEV-20220902T130242Z-001/SP15/upload_audios_bucket'):
    for name in files:
        count += 1
        new_file = name[:-5] + str(count) + '.webm'
        source_file_name = root + "/" + new_file
        blob = bucket.blob(new_file)
        blob.upload_from_filename(root + "/" + name)

#teste