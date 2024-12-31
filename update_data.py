import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd
import sys

# Отримуємо шлях до файлу ключа з аргументів командного рядка
cred_file = sys.argv[1]

# Ініціалізація Firebase
cred = credentials.Certificate(cred_file)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://metals-f6eb0-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Приклад даних для завантаження
data = {'name': ['John', 'Jane', 'Tom'],
        'age': [25, 28, 30],
        'city': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Конвертуємо DataFrame у словник
data_dict = df.to_dict(orient='records')

# Завантажуємо дані у Firebase
ref = db.reference('/')
ref.set(data_dict)
