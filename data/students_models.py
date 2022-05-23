from db import get_db

def check_login(username):

    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT username, password FROM tbl_users WHERE username = ?"
    cursor.execute(query, [username])
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    result.append(dict(zip(columns, cursor.fetchone()))) #konversi ke dictionary
        
    return result
    # Using a while loop
    #cursor.execute("SELECT * FROM tbl_users")
    #row = cursor.fetchone()
    #while row is not None:
       # print(row)
      #  row = cursor.fetchone()

# Using the cursor as iterator
    #cursor.execute("SELECT * FROM tbl_users")
   # for row in cursor:
        #print(row)

# ambil semua data students
def get_students():
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT id, nim, nama, jurusan, alamat FROM tbl_students"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #konversi ke dictionary
        
    return result

# ambil data students berdasarkan id
def get_students_by_id(id):
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT id, nim, nama, jurusan, alamat FROM tbl_students WHERE id = ?"
    cursor.execute(query, [id])
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    result.append(dict(zip(columns, cursor.fetchone()))) #konversi ke dictionary
        
    return result

# menambahkan data students
def insert_students(nim, nama, jurusan, alamat):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO tbl_students(nim, nama, jurusan, alamat) VALUES (?,?,?,?)"
    cursor.execute(query, [nim, nama, jurusan, alamat])
    db.commit()
    return True
    

# mengubah data students
def update_students(id, nim, nama, jurusan, alamat):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE tbl_students SET nim = ?, nama = ?, jurusan = ?, alamat = ? WHERE id = ?"
    cursor.execute(query, [nim, nama, jurusan, alamat, id])
    db.commit()
    return True

# menghapus data students
def delete_students(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM tbl_students WHERE id = ?"
    cursor.execute(query, [id])
    db.commit()
    return True
