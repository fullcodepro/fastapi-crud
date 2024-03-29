# REST Server con Python & FastAPI

![https://amalgjose.files.wordpress.com/2021/02/fast_api_ppt.png](https://amalgjose.files.wordpress.com/2021/02/fast_api_ppt.png)

Configuración de entorno virtual con python:
Windows:
```bash
pip3 install virtualenv
```

Linux:
```
pip install virtualenv
```

Crear entorno virtual:
```bash
vitualenv env
```

Activar entorno virtual desde la terminal:
```bash
.\env\Scripts\activate
```

Desactivar entorno virtual desde la terminal:
```bash
.\env\Scripts\deactivate
```

![Entorno Activado](static/images/entorno-activado.jpg)


Instalación de dependencias en Linux - WSL
```bash
pip3 install -r requirements.txt
```

Instalación de dependencias en Windows
```bash
pip install -r requirements.txt
```

Crear archivo .env y configurar variable de entorno.

```bash
HUGGINGFACEHUB_API_TOKEN="YOUR_HUGGINGFACE_API_TOKEN"

REPO_ID="YOUR_REPO_MODEL_ID"
```

Inicializar servidor con:
```bash
uvicorn app:app --reload
```

Endpoint de ejemplo (GET):
```bash
http://localhost:8000/falcon?question=quien+fue+maradona
```