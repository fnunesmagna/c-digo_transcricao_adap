# 1 - Configuração credencial JSON
# 2 - Instanciando o objeto
# 3 - Informando o nome do áudio a ser transcrito do storage
#     gs://Bucket + nome do arquivo no storage
# 4 - Instaciando o objeto e aplicando a função RecognitionAudio ao audio específico
# 5 - Parametrização do Audio via API
#     Verificar a extensão do arquivo e analisar qual o ECONDING correto para aparametrização
# 6 - Reconhecendo a fala do audio


from urllib import response
from google.cloud import speech
import os
import io

# 1
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/nunesfi/Área de Trabalho/Magna/Projetos/DIPOL/Oitivas/scripts/credencial_json/dipol-sist-invest-dev-10dab1f88c35.json"
# 2
client = speech.SpeechClient()
# 3
gcs_uri = "gs://sp-app-oitiva-transcricao-dev/1180-Delegado.webm"
# 4
audio = speech.RecognitionAudio(uri = gcs_uri)

#5
config = speech.RecognitionConfig(
        encoding= speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
        sample_rate_hertz=48000,
        language_code="pt_BR",
        model = 'phone_call',
        use_enhanced = True,
        enableWordConfidence = True
    )

# 6
operation = client.long_running_recognize(config=config, audio=audio)
response = operation.result(timeout=10000)

for result in response.results:
    print(u"{}".format(result.alternatives[0].transcript))

frase = ''

palavras = frase.split(' ')
for palavra in palavras:
    print(palavra)