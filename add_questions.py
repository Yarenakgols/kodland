import sqlite3

def add_questions():
    connection = sqlite3.connect('exam.db')
    cursor = connection.cursor()

    # Soruları ekle
    cursor.execute('INSERT INTO questions (question_text, answer_A, answer_B, answer_C, answer_D, correct_answer) VALUES (?, ?, ?, ?, ?, ?)',
                   ('Python nedir?', 'Programlama dili', 'Bir oyun', 'Bir araç', 'Bir yemek', 'A'))
    cursor.execute('INSERT INTO questions (question_text, answer_A, answer_B, answer_C, answer_D, correct_answer) VALUES (?, ?, ?, ?, ?, ?)',
                   ('Flask nedir?', 'Bir programlama dili', 'Bir veritabanı', 'Bir web framework\'ü', 'Bir oyun motoru', 'C'))
    cursor.execute('INSERT INTO questions (question_text, answer_A, answer_B, answer_C, answer_D, correct_answer) VALUES (?, ?, ?, ?, ?, ?)',
                   ('SQLite nedir?', 'Bir veritabanı yönetim sistemi', 'Bir oyun motoru', 'Bir dil', 'Bir yazılım aracı', 'A'))
    
    connection.commit()
    connection.close()

# Soruları veritabanına ekleyin
add_questions()
