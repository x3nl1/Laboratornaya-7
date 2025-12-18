import sqlite3

def create_database():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            grade INTEGER
        )
    """)
    
    test_students = [
        (1, "Иван Петров", 85),
        (2, "Мария Сидорова", 92),
        (3, "Алексей Иванов", 78)
    ]
    
    cursor.executemany(
        "INSERT OR IGNORE INTO students VALUES (?, ?, ?)",
        test_students
    )
    
    connection.commit()
    connection.close()
    
    print("База данных и таблица созданы")

if __name__ == "__main__":
    create_database()
