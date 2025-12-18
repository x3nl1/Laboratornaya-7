import sqlite3

def delete_record():
    connection = sqlite3.connect("students1.db")
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM students WHERE id = 2")
    connection.commit()
    
    cursor.execute("SELECT * FROM students")
    remaining = cursor.fetchall()
    
    connection.close()
    
    print("Оставшиеся студенты:", remaining)

if __name__ == "__main__":
    delete_record()
