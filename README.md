# Chatbot de Voz con LM Studio (Local)

## Descripción

Esta aplicación permite interactuar con un modelo de lenguaje local (LM Studio u Ollama) mediante **voz** en lugar de texto. El flujo de la aplicación es:

1. Captura la voz del usuario y la convierte a texto.  
2. Envía el texto al modelo local para generar una respuesta inteligente.  
3. Reproduce la respuesta mediante síntesis de voz.

Se utilizan las siguientes bibliotecas de Python:

- `speech_recognition` para reconocimiento de voz.  
- `pyttsx3` para síntesis de voz.  
- `requests` para interactuar con la API de LM Studio.  
- `pyaudio` para el manejo del micrófono.  

---

## Requisitos

- Python 3.12+  
- LM Studio instalado y corriendo en local (por ejemplo, en `http://localhost:1234`)  
- Entorno virtual con las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

---

## Instalación y Ejecución

1. Clona o descarga el proyecto:

```bash
git clone <URL_DEL_PROYECTO>
cd chatvoz-lmstudio
```

2. Crea un entorno virtual

```bash
python -m venv env
```

3. Activa el entorno virtual:

- Windows:

```bash
env\Scripts\activate
```

- Linux / macOS:

```bash
source env/bin/activate
```

4. Instala las dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

5. Ejecuta el script principal:

```bash
python app.py
```

---

## Uso

1. Asegúrate de que LM Studio esté corriendo en local.
2. Al ejecutar app.py, el programa iniciará y mostrará:

```bash
Bienvenido a tu chatbot de voz, donde podrás realizar la consulta que creas conveniente.
```

3. Habla por el micrófono y espera a que el asistente de voz responda.
4. El asistente leerá la respuesta generada por el modelo mediante voz.

---

## Configuración de LM Studio

* Puerto por defecto: 1234.
* Endpoint utilizado: /v1/chat/completions.
* Modelo local recomendado: deepseek/deepseek-r1-0528-qwen3-8b.
* System prompt usado:

```bash
Eres un asistente de voz amigable que responde únicamente a preguntas de manera natural y coloquial, como en una conversación cara a cara con el usuario. No analices ni expliques el mensaje, solo responde.
```

---

## Manejo de errores

* Si no se detecta micrófono, el programa mostrará:

```bash
No se encontró un micrófono disponible
```

* Si no se entiende el audio:

```bash
No se entendió el audio, repite el proceso.
```

* Si falla la petición a LM Studio:

```bash
Error al realizar la petición a la API de LM Studio: <detalle del error>
```

---

## Licencia

Este proyecto es un ejercicio académico y no tiene fines comerciales. Usar bajo la licencia de tu institución educativa.

---

## Autor

Cristian Cantero López