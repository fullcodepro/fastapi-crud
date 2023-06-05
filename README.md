# REST Server con Python & FastAPI

![https://amalgjose.files.wordpress.com/2021/02/fast_api_ppt.png](https://amalgjose.files.wordpress.com/2021/02/fast_api_ppt.png)

Instalación de dependencias en Linux - WSL
```bash
pip3 install -r requirements.txt
```

Instalación de dependencias en Windows
```bash
pip install -r requirements.txt
```

Inicializar servidor con:
```bash
uvicorn app:app --reload
```

Endopoint
```bash
http://localhost:8000/falcon?question=quien+fue+maradona
```