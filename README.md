# 🤖 Telegram Translator Bot

یک ربات تلگرام ساده، سریع و کاربردی برای **ترجمه خودکار بین فارسی و انگلیسی** با رابط کاربری دکمه‌ای و ذخیره تنظیمات زبان هر کاربر.

---

## ✨ امکانات

* 🔁 ترجمه دوطرفه **فارسی ⇄ انگلیسی**
* 🌐 تشخیص خودکار زبان متن ارسالی
* 🗣️ ترجمه هم‌زمان برای زبان‌های نامشخص
* 🌍 پشتیبانی از چند زبان (FA / EN)
* 💾 ذخیره زبان انتخابی هر کاربر در دیتابیس
* 🎛️ دکمه‌های تعاملی (Inline Keyboard)
* ⚡ سرعت بالا و استفاده آسان

---

## 🧠 تکنولوژی‌های استفاده‌شده

* Python 🐍
* pyTelegramBotAPI (TeleBot)
* deep-translator (GoogleTranslator)
* SQLite
* python-dotenv

---

## 📝 پیام‌ها و متن‌های ربات (FA / EN)

ربات از فایل متنی جداگانه برای مدیریت پیام‌ها استفاده می‌کند که به‌صورت دو زبانه پیاده‌سازی شده است.

### 🇮🇷 فارسی

* پیام خوش‌آمدگویی
* راهنمای استفاده
* درباره ربات و سازنده
* انتخاب زبان ربات

### 🇬🇧 English

* Welcome message
* Help & instructions
* About the bot & creator
* Language selection

این ساختار باعث می‌شود اضافه‌کردن زبان‌های جدید در آینده بسیار ساده باشد ✅

---

## 📌 دستورات ربات

| دستور        | توضیح                   |
| ------------ | ----------------------- |
| `/start`     | شروع ربات و انتخاب زبان |
| `/help`      | راهنمای استفاده         |
| `/about`     | درباره ربات             |
| `/languages` | تغییر زبان ربات         |

---

## 🚀 نصب و اجرا

### 1️⃣ نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

### 2️⃣ تنظیم توکن ربات

یک فایل `.env` بسازید و توکن ربات تلگرام را داخل آن قرار دهید:

```env
TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

### 3️⃣ اجرای ربات

```bash
python bot.py
```

---

## 🗄️ دیتابیس

* دیتابیس کاربران به‌صورت خودکار ساخته می‌شود
* زبان انتخابی هر کاربر ذخیره می‌شود
* در اجرای بعدی، ربات زبان قبلی کاربر را تشخیص می‌دهد

---

## 👨‍💻 درباره سازنده

**Alireza Tashani**
Web & Telegram Bot Developer 💻🤖

🛠️ مهارت‌ها:

* توسعه وب (Backend) 🌐
* توسعه ربات‌های تلگرام 🤖
* بهینه‌سازی تجربه کاربری و عملکرد 🚀

📬 راه‌های ارتباطی:

* ✉️ Email: **[alirezatd80@gmail.com](mailto:alirezatd80@gmail.com)**
* 🐙 GitHub: **[https://github.com/alirezatp80](https://github.com/alirezatp80)**

---

## 🌟 نکات پایانی

* ربات زبان متن را **به‌صورت خودکار تشخیص می‌دهد** 🤖
* مناسب استفاده روزمره، یادگیری زبان و ترجمه سریع
* کد ساده و قابل توسعه برای افزودن زبان‌های جدید

✨ اگر پیشنهادی برای بهبود ربات دارید، خوشحال می‌شوم در GitHub با من در میان بگذارید!

---

# 🌍 Telegram Translator Bot (English Version)

A simple, fast, and practical Telegram bot for **automatic Persian ⇄ English translation**, featuring interactive buttons and per-user language settings.

---

## ✨ Features

* 🔁 Two-way translation **Persian ⇄ English**
* 🌐 Automatic language detection
* 🗣️ Dual translation for unknown languages
* 🌍 Multi-language bot interface (FA / EN)
* 💾 Saves each user's selected language in database
* 🎛️ Inline keyboard buttons
* ⚡ Fast, lightweight, and easy to use

---

## 🧠 Technologies Used

* Python 🐍
* pyTelegramBotAPI (TeleBot)
* deep-translator (GoogleTranslator)
* SQLite
* python-dotenv

---

## 📝 Bot Texts & Messages (FA / EN)

The bot uses a separate text file to manage all messages in a bilingual structure.

### 🇮🇷 Persian

* Welcome message
* Help instructions
* About the bot & creator
* Language selection

### 🇬🇧 English

* Welcome message
* Help instructions
* About the bot & creator
* Language selection

This structure makes it very easy to add new languages in the future ✅

---

## 📌 Bot Commands

| Command      | Description                     |
| ------------ | ------------------------------- |
| `/start`     | Start the bot & choose language |
| `/help`      | Show help message               |
| `/about`     | About the bot                   |
| `/languages` | Change bot language             |

---

## 🚀 Installation & Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Set bot token

Create a `.env` file and put your Telegram bot token inside:

```env
TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

### 3️⃣ Run the bot

```bash
python bot.py
```

---

## 🗄️ Database

* User database is created automatically
* Each user's selected language is stored
* Bot remembers user preferences on next runs

---

## 👨‍💻 About the Creator

**Alireza Tashani**
Web & Telegram Bot Developer 💻🤖

🛠️ Skills:

* Backend web development 🌐
* Telegram bot development 🤖
* Performance & UX optimization 🚀

📬 Contact:

* ✉️ Email: **[alirezatd80@gmail.com](mailto:alirezatd80@gmail.com)**
* 🐙 GitHub: **[https://github.com/alirezatp80](https://github.com/alirezatp80)**

---

## 🌟 Final Notes

* Bot automatically detects text language 🤖
* Perfect for daily use, learning languages, and quick translations
* Clean and extensible codebase

✨ Feel free to contribute or share your ideas on GitHub!
