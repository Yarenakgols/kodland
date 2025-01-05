import sqlite3

def create_db():
    connection = sqlite3.connect('exam.db')
    cursor = connection.cursor()

    # Sorular tablosunu oluştur
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
                        id INTEGER PRIMARY KEY,
                        question_text TEXT,
                        answer_A TEXT,
                        answer_B TEXT,
                        answer_C TEXT,
                        answer_D TEXT,
                        correct_answer TEXT)''')

    # Sonuçlar tablosunu oluştur
    cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        score INTEGER)''')

    connection.commit()
    connection.close()

# Veritabanını oluştur
create_db()
