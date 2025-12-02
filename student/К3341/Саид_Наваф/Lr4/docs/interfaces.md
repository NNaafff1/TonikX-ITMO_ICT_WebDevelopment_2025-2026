# Описание интерфейсов (компоненты и маршруты)

Маршруты (router):
- `/owners` — список владельцев (Owners.vue). Вызов: GET `/api/owners/`
- `/owners/:id` — детальная страница владельца (OwnerDetail.vue). Вызов: GET `/api/owners/<id>/`
- `/login` — страница входа (Login.vue). Вызов: POST `/api/token/` (Django SimpleJWT)
- `/register` — регистрация (Register.vue). Вызов: POST `/auth/users/` (Djoser)

Краткие примеры запросов (axios):
- Получить список владельцев:
```js
const res = await api.get('/api/owners/');
```
- Получить владельца по id:
```js
const res = await api.get(`/api/owners/${id}/`);
```
- Вход (получаем access token):
```js
const res = await api.post('/api/token/', { username, password });
// сохранить res.data.access в localStorage и установить заголовок Authorization
```

Аутентификация:
- После получения токена сохранить `access` в localStorage и добавить в axios default header:
  `Authorization: Bearer <token>`

UI:
- Простая кастомная CSS‑тема в `src/assets/main.css` (без зависимостей).