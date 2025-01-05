from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Veritabanına bağlanarak en yüksek puanı al
def get_high_score():
    connection = sqlite3.connect('exam.db')
    cursor = connection.cursor()
    cursor.execute('SELECT MAX(score) FROM results')
    high_score = cursor.fetchone()[0]  # En yüksek puanı al
    connection.close()
    return high_score or 0  # Eğer sonuç yoksa 0 döndür

# Ana sayfa
@app.route('/')
def index():
    # Veritabanına bağlan
    connection = sqlite3.connect('exam.db')
    cursor = connection.cursor()

    # Soruları al
    cursor.execute('SELECT * FROM questions')
    questions = cursor.fetchall()

    connection.close()

    # En yüksek puanı al
    high_score = get_high_score()

    # Soruları HTML şablonuna gönder
    return render_template('index.html', questions=questions, high_score=high_score)

# Sonuçları gönderme
@app.route('/submit', methods=['POST'])
def submit():
    # Kullanıcının adını al
    user_name = request.form['name']
    
    score = 0
    # Soruları kontrol et
    for question_id in request.form:
        if question_id != 'name':  # 'name' parametresi sorulara dahil edilmemeli
            answer = request.form[question_id]
            # Veritabanına bağlan
            connection = sqlite3.connect('exam.db')
            cursor = connection.cursor()
            cursor.execute('SELECT correct_answer FROM questions WHERE id = ?', (question_id,))
            correct_answer = cursor.fetchone()[0]
            connection.close()

            # Cevap doğruysa puan artır
            if answer == correct_answer:
                score += 1

    # En yüksek puanı veritabanına kaydet
    connection = sqlite3.connect('exam.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO results (name, score) VALUES (?, ?)', (user_name, score))
    connection.commit()
    connection.close()

    # En yüksek puanı al
    high_score = get_high_score()

    # Sonuçları HTML şablonuna gönder
    return render_template('result.html', score=score, user_name=user_name, high_score=high_score)

if __name__ == '__main__':
    app.run(debug=True)
