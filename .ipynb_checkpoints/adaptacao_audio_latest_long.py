#Adaptação de áudio para transcrição
from google.cloud import speech_v1p1beta1 as speech
import os

# Credencial JSON
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/nunesfi/Área de Trabalho/Magna/Projetos/DIPOL/Oitivas/scripts/credencial_json/dipol-sist-invest-dev-10dab1f88c35.json'

# Instanciando o objeto 
adaptation_client = speech.AdaptationClient()

# Recurso/local em que a classe customizada será criada
parent = f"projects/dipol-sist-invest-dev/locations/global"

# Criação Custom class
adaptation_client.create_custom_class(
   {
        "parent": parent,
        "custom_class_id": "CustomID-21",
        "custom_class": {
            "items": [
                {"value": "dia"},
                {"value": "quente"},
                {"value": "aguardar"},
                {"value": "minuto"},
                {"value": "minutos"},
                {"value": "oitiva"},
                {"value": "oitivas"},
                {"value": "cronometro"},
                {"value": "cronometrado"},
                {"value": "um"},
                {"value": "hoje"}
            ]
        },
    }
)

# Nome da classe customizada, deixando o ID como nome do recurso
custom_class_name = (f"projects/dipol-sist-invest-dev/locations/global/customClasses/CustomID-21")

# Criação do Phrase_set
phrase_set_response = adaptation_client.create_phrase_set(
    {
        "parent": parent,
        "phrase_set_id": "PhraseSet-Teste18",
        "phrase_set": {
            "boost": 20,
            "phrases": [
                {"value": custom_class_name}
            ],
        },
    }
)

phrase_set_name = phrase_set_response.name

#Incluindo a adaptação na Transcrição de áudio
speech_adaptation = speech.SpeechAdaptation(phrase_set_references=[phrase_set_name])

# Parametrização do Audio via API
config = speech.RecognitionConfig(
    encoding = speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
    sample_rate_hertz = 48000,
    language_code = "pt_BR",
    model = "latest_long",
    adaptation = speech_adaptation,
)

client = speech.SpeechClient()

#bucket
gcs_uri = "gs://sp-app-oitiva-transcricao-dev/73_Delegado43.webm"

audio = speech.RecognitionAudio(uri= gcs_uri)

# 6 - Reconhecendo a fala do audio
operation = client.long_running_recognize(config=config, audio=audio)
response = operation.result(timeout=10000)

for result in response.results:
    print(u"{}".format(result.alternatives[0].transcript))
