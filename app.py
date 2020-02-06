import pymysql.cursors

# Connect to the database

connection = pymysql.connect(host='mrbartucz.com',

                             user='sc3460ze',

                             password='Jas4863009*',

                             db='sc3460ze_uni',

                             charset='utf8mb4',

                             cursorclass=pymysql.cursors.DictCursor)

#input_user=input("Search for Name:")

try:

    with connection.cursor() as cursor:

        # Select all Students
        sql = "SELECT * from sc3460ze_students"
        # Select student by searching with first name
        #sql = "SELECT * from sc3460ze_students where First_Name = '"+input_user+"'"
              
        # execute the SQL command

        cursor.execute(sql)
       

        # get the results

        for result in cursor:

            print (result)

    
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.

        # So you must commit to save your changes. 

        # connection.commit()  

finally:

    connection.close()


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3460)