import speech_recognition as sr

###### Configuracoes #####
with open('rosie-pyhton-assistente-386123-4b482ef2b8d0.json') as credenciais_google:
    credenciais_google = credenciais_google.read()
def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        print("aguardando o comando:")
        audio = microfone.listen(source)
    try:
        print(microfone.recognize_google_cloud(audio, credentials_json=credenciais_google, language='pt_BR'))
    except sr.UnknownValueError:
        print("erro_retorno_api")
    except sr.RequestError as e:
        print("nao escutei muito bem; {0}" .format(e))

monitora_audio()
