#change the password & databasename
# delete all '#' in .sql file
import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime, date, timedelta
import mysql.connector #MySQL API Library
from mysql.connector import Error


mydb = mysql.connector.connect(host="localhost", user="root", password="Z@y8472279", database="Project") #change the password & database
mycursor = mydb.cursor()

def sendemail(filename):    #sendemail ('Hello.txt') will send the Hello.txt as attachment
    # Define email sender and receiver
    email_sender = 'dbmsgroup19@gmail.com'
    #google password: icmsicms1919
    email_password = 'gkma bvtw qbii wulg'
    email_receiver = 'justinyeung1096@gmail.com'

    # Set the subject and body of the email
    subject = 'Please Find Your Course Information Attached'
    body = """
    See title.
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject

    em.set_content(body)

    # Add the attachment to the email
    attachment_path = filename
    with open(attachment_path, 'rb') as attachment:
        em.add_attachment(attachment.read(), maintype='application', subtype='octet-stream', filename=attachment_path)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

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
#these should only be executed once for initialisation, better use another .py to handle


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

def getCourseInfo(course_id): #tested
  mycursor.execute(f"SELECT * FROM Courses WHERE course_id = {course_id}") #input instructions
  myresult = mycursor.fetchall()
  course_code = myresult[0][1]
  class_id = myresult[0][2]
  year_offered = myresult[0][3]
  coursename = myresult[0][4]
  welcome_message = myresult[0][5]
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


  
def getLectureToday(student_id): #tested with 1 record
  now = datetime.now()
  d_string = now.strftime("%Y-%m-%d")
  t_string = now.strftime("%H:%M:%S")
  mycursor.execute(f"SELECT * FROM CourseClass AS CC JOIN ClassTaken AS CT WHERE CC.course_id = CT.course_id AND student_id = '{student_id}' AND CC.class_date='{d_string}'") #input instructions
  myresult = mycursor.fetchall()
  return(myresult)

def HaveClassIn1Hr(LectureToday):
    for i in range(len(LectureToday)):
        if within1hr(LectureToday[i][1],LectureToday[i][2],LectureToday[i][3]):
            return LectureToday[i]
    return "" #need some dummy

def within1hr(date,starttime,endtime):
    now = datetime.now()
    if ((datetime.combine(date, datetime.min.time()) + starttime) <= now+timedelta(hours=1)) and ((datetime.combine(date, datetime.min.time()) + endtime) >= now): #startime < 1 hour from now and now is not yet endtime
        return True
    else:
        return False
    
def getCourseTaken(student_id): #untested
  mycursor.execute(f"SELECT C.course_code, C.class_id, C.course_name FROM Courses AS C JOIN CourseTaken as CT WHERE CT.student_id = '{student_id}' and C.course_id = CT.course_id") #input instructions
  myresult = mycursor.fetchall()
  return(myresult)

def getLectureMaterialPath(course_id, class_date, class_time): #untested
  mycursor.execute(f"SELECT CM.material_name FROM CourseMaterial AS CM WHERE CM.course_id = '{course_id}' and CM.class_date = '{class_date}' and CM.class_time = '{class_time}'") #input instructions
  myresult = mycursor.fetchall()
  filepaths=[]
  for row in myresult:
    filepaths.append(row[0])
  return filepaths