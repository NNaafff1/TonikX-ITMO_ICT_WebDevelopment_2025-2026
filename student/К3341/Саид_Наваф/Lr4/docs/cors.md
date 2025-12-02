# CORS (настройка Cross-Origin Resource Sharing)

Чтобы фронтенд на http://localhost:5173 мог обращаться к Django backend (http://127.0.0.1:8000) — на сервере настроен пакет `django-cors-headers`.

Краткая сводка настроек в `settings.py`:
```python
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE

CORS_ALLOWED_ORIGINS = [
  "http://localhost:5173",
  "http://127.0.0.1:5173",
]
from corsheaders.defaults import default_headers
CORS_ALLOW_HEADERS = list(default_headers) + ["authorization"]
# Для dev можно временно: CORS_ALLOW_ALL_ORIGINS = True
```

Как проверить:
- Откройте DevTools → Network. При запросе к `/api/owners/` в разделе Response Headers должен быть `Access-Control-Allow-Origin: http://localhost:5173`.
- Curl: пример проверки preflight:
```bash
curl -i -X OPTIONS "http://127.0.0.1:8000/api/owners/" -H "Origin: http://localhost:5173" -H "Access-Control-Request-Method: GET"
```