# Lab 3: Mini Instagram Clone

خطوات التشغيل كاملة من CMD (Windows) أو Terminal (Mac/Linux).

## 1) فك الضغط وادخل المجلد
```
cd mini_instagram
```

## 2) أنشئ بيئة افتراضية (اختياري لكن مستحسن)
Windows CMD:
```
python -m venv venv
venv\Scripts\activate
```
Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

## 3) ثبّت المكتبات
```
pip install -r requirements.txt
```

## 4) أنشئ ملفات الترحيل (migrations) وطبّقها
```
python manage.py makemigrations
python manage.py migrate
```

## 5) (اختياري) أنشئ حساب أدمن لتتحكم بالمنشورات من /admin
```
python manage.py createsuperuser
```

## 6) شغّل السيرفر
```
python manage.py runserver
```
افتح المتصفح على: http://127.0.0.1:8000/

## 7) اختبار متطلبات الـ Exit Ticket
- ارفع صورة jpg أو png مع username ووصف -> لازم تظهر في الفيد.
- جرّب ترفع ملف .txt أو .pdf -> لازم يترفض برسالة خطأ.
- اضغط زر Like -> لازم العداد يزيد بواحد فورًا.
- شغّل الأمر التالي وتأكد إن feed.css نسخ داخل مجلد STATIC_ROOT (staticfiles/css/feed.css):
```
python manage.py collectstatic
```

## هيكل المشروع
```
mini_instagram/
├── manage.py
├── requirements.txt
├── mini_instagram/        # إعدادات المشروع (settings, urls)
├── feed/                  # التطبيق (Post model, views, urls, admin)
│   └── templates/feed/feed.html
├── static/css/feed.css    # تنسيق الفيد (Requirement 8)
└── media/posts/           # مكان تخزين الصور المرفوعة (Requirement 2)
```
