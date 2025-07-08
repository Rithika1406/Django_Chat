# 💬 Django Real-Time Chat App

A secure, real-time chat application built with **Django 5.2**, **Channels**, and **WebSockets**. Users can create/join private chat rooms using a room name and passcode. All messages are saved to the database and streamed live to connected users using Django Channels.

---

## 🚀 Features

- 🔐 User authentication (login/logout)
- 🏠 Home page redirects to chat flow
- 💬 Create or Join password-protected chat rooms
- 📡 Real-time WebSocket-based chat
- 🧠 Messages stored in database (with timestamps)
- 📄 Chat history loads for each room (last 50 messages)
- ✅ Clean Django structure with Channels integration

---

## 📁 Project Structure

```

DjangoChat/
├── DjangoChat/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── routing.py
├── chatapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── consumers.py
│   ├── routing.py
│   ├── templates/
│   │   └── chat/
│   │       ├── join\_room.html
│   │       ├── create\_room.html
│   │       ├── chat\_room.html
│   │       └── login.html
│   └── static/
│       └── chatapp/
│           └── chat.js (if used)
├── db.sqlite3
├── manage.py
└── requirements.txt

````

---

## 🛠️ Installation & Setup

### 1. 🔃 Clone the repository

```bash
https://github.com/Rithika1406/Django_Chat

cd django-chat-app
````

### 2. 📦 Create virtual environment & activate

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. 🧰 Install dependencies

```bash
pip install -r requirements.txt
```

### 4. 🔧 Apply migrations

```bash
python manage.py migrate
```

### 5. 👤 Create a superuser

```bash
python manage.py createsuperuser
```

### 6. ▶️ Run the server

```bash
python manage.py runserver
```

> By default, the app uses `InMemoryChannelLayer`. For production, switch to Redis in `settings.py`.

---

## 🧪 Tech Stack

| Layer     | Tech                     |
| --------- | ------------------------ |
| Backend   | Django 5.2               |
| Real-time | Channels 4.1, WebSockets |
| Server    | Daphne (ASGI)            |
| Auth      | Django Auth              |
| Database  | SQLite (default)         |
| Frontend  | HTML + JS (Optional)     |
| Styling   | CSS (optional)           |

---

## 🌐 WebSocket URL Pattern

```
/ws/chat/<room_name>/
```

Handled by:

* `chatapp/routing.py`
* `chatapp/consumers.py`

---

## 🧾 Sample .env for Production (Optional)

```env
DEBUG=False
SECRET_KEY=your-secure-key
ALLOWED_HOSTS=yourdomain.com,localhost,127.0.0.1
```

---

## ✅ To Do

* [ ] Add Redis support via `channels_redis`
* [ ] Style the UI with Bootstrap or Tailwind
* [ ] Add emojis or markdown support in chat
* [ ] Add chat notifications
* [ ] Dockerize for deployment
