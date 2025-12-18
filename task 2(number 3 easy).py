import sqlite3

def select_data():
    connection = sqlite3.connect("students1.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM students")
    all_students = cursor.fetchall()
    
    cursor.execute("SELECT name FROM students WHERE grade > 80")
    good_students = cursor.fetchall()
    
    connection.close()
    
    print("Все студенты:", all_students)
    print("Студенты с оценкой > 80:", good_students)

if __name__ == "__main__":
    select_data()
