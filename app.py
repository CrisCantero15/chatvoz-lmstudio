# Proyecto 1: Aplicación de Voz para Interactuar con la API de LLM Studio u Ollama en Local

# Descripción: Esta aplicación permite enviar un prompt y recibir la respuesta mediante comandos de voz, en vez de texto. Se utilizarán bibliotecas de Python para reconocimiento de voz (por ejemplo, SpeechRecognition) y para síntesis de voz (por ejemplo, pyttsx3). El flujo consiste en:

# 1. Capturar la voz del usuario y convertirla a texto.
# 2. Enviar ese texto a la API de LLM Studio u Ollama (en local).
# 3. Recibir la respuesta en formato de texto y reproducirla mediante voz.

import speech_recognition as sr
import pyttsx3 as p
import requests
import os

os.system("cls" if os.name == "nt" else "clear")

# Inicializar el reconocedor de voz
r = sr.Recognizer()

# Inicializar el sintetizador de voz
engine = p.init()

def record_voice():
    """ Inicia micrófono y captura el audio con el mensaje transmitido por el usuario. """
    
    try:
        with sr.Microphone() as source:
            print("Grabando...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5)
            print("Audio capturado. Procesando tu mensaje...")
    except OSError:
        print("No se encontró un micrófono disponible")
        return None
    except sr.WaitTimeoutError:
        print("No se capturó audio en el tiempo esperado (timeout)")
        return None
    except Exception as e:
        print("Un error inesperado ocurrió: ", e)
        return None
    
    try:
        text = r.recognize_google(audio, language="es-ES")
        return text
    except sr.UnknownValueError:
        print("No se entendió el audio, repite el proceso.")
        return None
    except sr.RequestError as e:
        print("Error con el servicio de reconocimiento: ", e)
        return None

def get_response(text):
    """ Se envía, con el mensaje recibido por voz, un prompt a la API de LMStudio para generar una respuesta inteligente. """
    
    # URL con el endpoint donde realizar la petición (puerto 1234)
    URL = "http://localhost:1234/v1/chat/completions"
    
    # Modelo cargado en LM Studio de manera local (sustituir por el que se crea conveniente)
    MODEL = "deepseek/deepseek-r1-0528-qwen3-8b"

    payload = {
        "model": MODEL,
        "messages": [
            { "role": "system", "content": "Eres un asistente de voz amigable y conversacional. Responde únicamente a la pregunta del usuario de manera natural y coloquial, como si estuvieras hablando cara a cara. No analices, no expliques, no agregues contexto adicional; solo da una respuesta breve y directa." },
            { "role": "user", "content": "Responde brevemente: " + text }
        ],
        "temperature": 0.3,
        "max_tokens": -1, # Número ilimitado de tokens
        "stream": False # La API espera a generar toda la respuesta completa y luego la envía de una sola vez
    }

    try:
        response = requests.post(URL, json=payload)
        response.raise_for_status()
        data = response.json()
        message = data["choices"][0]["message"]["content"]
        return message
    except requests.RequestException as e:
        print("Error al realizar la petición a la API de LM Studio: ", e)
        return None

def play_response(message):
    """ Reproduce la respuesta al mensaje del usuario, utilizando un sintetizador de voz. """
    
    engine.say(message)
    engine.runAndWait()

def main():
    
    print("Bienvenido a tu chatbot de voz, donde podrás realizar la consulta que creas conveniente.")
    
    # Obtener el mensaje del usuario a travéz del reconocedor de voz
    user_message = record_voice()
    if not user_message:
        print("No se pudo capturar ningún mensaje. Saliendo...")
        return
    
    # Obtener la respuesta de la API generada con el prompt enviado a travéz del audio generado
    print("Formulando pregunta al asistente de voz...")
    lmstudio_response = get_response(user_message)
    if not lmstudio_response:
        print("No se pudo obtener respuesta de la API de LM Studio. Saliendo...")
        return
    
    # Pasar la respuesta por el sintetizador de voz para generar un audio como output para el usuario
    print("El asistente de voz está respondiendo...")
    play_response(lmstudio_response)

if __name__ == "__main__":
    main()