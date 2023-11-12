#change the password & databasename
# delete all '#' in .sql file
from datetime import datetime
import mysql.connector #MySQL API Library
from mysql.connector import Error


mydb = mysql.connector.connect(host="localhost", user="root", password="Z@y8472279", database="Project") #change the password & database
mycursor = mydb.cursor()


def executeSQL(filename):
    try:
          with open(filename, "r") as file:
              sql_script = file.read()
              mycursor.execute(sql_script, multi=True)
              print("SQL script executed successfully")
    except Error as e:
          print("Error executing SQL script", e)

def executeSQLdata(filename):
    try:
          with open(filename, "r") as file:
              sql_script = file.read()
              mycursor.execute(sql_script, multi=True)
              mydb.commit()
              print("SQL script executed successfully")
    except Error as e:
          print("Error executing data SQL script", e)
#executeSQL("proj_tables_1.sql")
#executeSQLdata("proj_data_1.sql")


def putLoginInfo(student_id, ctime, cdate):
    mycursor.execute(f"INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ({student_id}, {ctime}, {cdate}, 0, 0);") #insert login data

def putLogoutInfo(student_id, login_time, login_date, ctime, cdate):
    mycursor.execute(f"DELETE FROM LoginBehaviour WHERE student_id = {student_id} AND login_time = {login_time} AND login_date = {login_date};") #delete partial login record
    mycursor.execute(f"INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ({student_id}, {login_time}, {login_date}, {ctime}, {cdate});") #insert login data

def getStudentInfo(student_id): #tested
  mycursor.execute(f"SELECT * FROM Student WHERE student_id = {student_id}") #input instructions
  myresult = mycursor.fetchall()
  email = myresult[0][1]
  name = myresult[0][2]
  birthday = myresult[0][3]
  return (email, name, birthday)

def checkLoginCredentials(username, password): #tested
    query = f"SELECT username, pswd, student_id FROM LoginCredentials WHERE username = '{username}' AND pswd = '{password}'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if len(myresult) != 0:
        return myresult[0][2]
    else:
        return "0000000000"

def getCourseInfo(course_id):
  mycursor.execute(f"SELECT * FROM Course WHERE course_id = {course_id}") #input instructions
  myresult = mycursor.fetchall()
  course_code = myresult[0][2]
  class_id = myresult[0][3]
  year_offered = myresult[0][4]
  coursename = myresult[0][5]
  welcome_message = myresult[0][6]
  return (course_code, class_id, year_offered, coursename, welcome_message)

def getLoginBehaviour(student_id):
  mycursor.execute(f"SELECT * FROM LoginBehaviour WHERE student_id = {student_id}") #input instructions
  myresult = mycursor.fetchall()
  login_time = myresult[0][2]
  login_date = myresult[0][3]
  logout_time = myresult[0][4]
  logout_date = myresult[0][5]
  return (login_time, login_date, logout_time, logout_date)

def getCourseTeacher(course_id):
  mycursor.execute(f"SELECT * FROM CourseTaught AS CT JOIN Teacher AS T WHERE CT.course_id = {course_id} AND CT.teacher_id = T.teacher_id") #input instructions
  myresult = mycursor.fetchall()
  teacher_name = ()
  for row in myresult:
    teacher_name += row[3]
  return teacher_name


  
def getNextLecture(student_id):
  now = datetime.now()
  d_string = now.strftime("%Y-%m-%d")
  t_string = now.strftime("%H:%M:%S")
  print(d_string, t_string)
  mycursor.execute(f"") #input instructions
  myresult = mycursor.fetchall()