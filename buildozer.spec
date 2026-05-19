[app]

# Название приложения
title = Calculator

# Package название (используется как имя APK)
package.name = calculator

# Domain (обратный домен для уникальности)
package.domain = org.myapp

# Версия приложения
version = 1.0

# Главный файл приложения
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Требуемые библиотеки
requirements = python3,kivy,kivymd

# Ориентация (portrait, landscape, sensor)
orientation = portrait

# Полный экран
fullscreen = 0

# Иконка приложения (опционально)
icon.filename = %(source.dir)s/data/icon.png

# Точка входа в приложение
main.py = main.py

[buildozer]

# Логирование
log_level = 2

# Предупреждения
warn_on_root = 1

# Версия Android API
android.api = 31

# Минимальная версия Android API
android.minapi = 21

# Версия NDK
android.ndk = 25b

# Приватные хранилища
android.private_storage = True

# Разрешения
android.permissions = INTERNET

# Возможности
android.features = 

# Архитектуры
android.archs = arm64-v8a,armeabi-v7a

# Метаданные
android.meta_data = 

# Классы Java (если используются)
android.add_src = 

# Класс Activity
android.activity_class_name = PythonActivity

# Сервисы
android.services = 

# Broadcast receivers
android.receivers = 

# Content providers
android.providers = 

# Bootstrap (вид приложения)
p4a.bootstrap = sdl2

# Gradle dependencies
android.gradle_dependencies = 

# Java classes (дополнительные JAR файлы)
android.add_libs_armeabi_v7a = 
android.add_libs_arm64_v8a = 

# Использовать https для скачивания
android.accept_sdk_license = True
