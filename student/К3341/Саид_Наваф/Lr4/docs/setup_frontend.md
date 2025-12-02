# Установка фронтенда

Путь к фронтенду в репозитории:
students/К3341/Саид_Наваф/laboratory_work_4/frontend/

Требования:
- Node.js (рекомендуется LTS), npm
- Backend (Django) должен быть запущен и доступен (см. ЛР3)

Шаги установки (локально):
1. Перейти в папку фронтенда:
```bash
cd students/К3341/Саид_Наваф/laboratory_work_4/frontend
```
2. Установить зависимости:
```bash
npm install
```
3. Создать .env в корне frontend:
```
VITE_API_URL=http://127.0.0.1:8000
```
4. Запустить dev сервер:
```bash
npm run dev
```
По умолчанию Vite откроет адрес, например: http://localhost:5173

Если нужно собрать продакшен‑бандл:
```bash
npm run build
```
Статический бандл окажется в папке `dist/`.