import mysql.connector #MySQL API Library


mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="databasename") #change the password & database


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM admin") #input instructions

myresult = mycursor.fetchall() #get results
for x in myresult:
  print(x)  #a tuple of each row's element

def getStudentInfo(student_id):
  mycursor.execute(f"SELECT * FROM Student WHERE student_id = {student_id}") #input instructions
  myresult = mycursor.fetchall()
  email = myresult[2]
  name = myresult[3]
  birthday = myresult[4]
  return (email, name, birthday)

def getCourseInfo(course_id):
  mycursor.execute(f"SELECT * FROM Course WHERE course_id = {course_id}") #input instructions
  myresult = mycursor.fetchall()
  course_code = myresult[2]
  class_id = myresult[3]
  year_offered = myresult[4]
  coursename = myresult[5]
  welcome_message = myresult[6]
  return (course_code, class_id, year_offered, coursename, welcome_message)

def getLoginBehaviour(student_id):
  mycursor.execute(f"SELECT * FROM LoginBehaviour WHERE student_id = {student_id}") #input instructions
  myresult = mycursor.fetchall()
  login_time = myresult[2]
  login_date = myresult[3]
  logout_time = myresult[4]
  logout_date = myresult[5]
  return (login_time, login_date, logout_time, logout_date)

def getCourseTeacher(course_id):
  mycursor.execute(f"SELECT * FROM CourseTaught AS CT JOIN Teacher AS T WHERE CT.course_id = {course_id} AND CT.teacher_id = T.teacher_id") #input instructions
  myresult = mycursor.fetchall()
  teacher_name = ()
  for row in myresult:
    teacher_name += row[3]
  return teacher_name
