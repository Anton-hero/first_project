print("Hello from repository!")
# Импорт библиотек
from dotenv import load_dotenv
import os

def print_author():
    # Загружаем переменные из файла .env
    load_dotenv()
    
    # Читаем переменную AUTHOR
    author = os.getenv('AUTHOR')
    
    # Печатаем имя автора
    print(f"Автор проекта: {author}")

# Вызов функции для проверки
if __name__ == "__main__":
    print_author()
