import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Set password if you use one
    database="user_db"
)

def create_user(username, email, password):
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    val = (username, email, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print("✅ User registered successfully!")

def main():
    print("=== Sign Up Form ===")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    create_user(username, email, password)

if __name__ == "__main__":
    main()
