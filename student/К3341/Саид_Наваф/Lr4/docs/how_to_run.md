# Как запускать сервер + фронтенд (коротко)

1) Backend (Django):
- Убедиться, что виртуenv активирован.
- Установить зависимости и миграции:
```bash
pip install -r requirements.txt
python manage.py migrate
# Опционально: создать суперадмина
python manage.py createsuperuser
```
- Заполнить тестовые данные:
```bash
python populate_lab3_practice3_1.py
```
- Запустить:
```bash
python manage.py runserver
```

2) Frontend (Vue):
```bash
cd students/К3341/Саид_Наваф/laboratory_work_4/frontend
npm install
npm run dev
```

3) Открыть:
- Фронтенд: http://localhost:5173
- Swagger (backend): http://127.0.0.1:8000/api/docs/swagger/
- Admin: http://127.0.0.1:8000/admin/

4) Подготовка сборки (опционально):
```bash
cd frontend
npm run build
# затем можно разместить dist/ в любом статическом хостинге
```