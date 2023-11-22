import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime, date, timedelta
import mysql.connector #MySQL API Library
from mysql.connector import Error

class Backend(object):
  
  def __init__(self):
    super().__init__()
    self.mydb = mysql.connector.connect(host="localhost", user="root", password="Z@y8472279") #change the password
    self.mycursor = self.mydb.cursor()
    self.mycursor.execute("USE GROUP19ICMS;")

  def createicms(self):
    self.mycursor.execute("DROP DATABASE IF EXISTS GROUP19ICMS;")
    self.mycursor.execute("CREATE DATABASE GROUP19ICMS;")
    self.mycursor.execute("USE GROUP19ICMS;")
    self.executeSQL("../Database/proj_tables_1.sql")
    self.executeSQL("../Database/proj_data_1.sql")

  def executeSQL(self,filename):
    try:
      with open(filename, "r") as file:
        sql_script = file.read()
        statements = sql_script.split(';')
        for statement in statements:
          if statement.strip():
            self.mycursor.execute(statement)
            print("SQL script executed successfully")
    except Error as e:
      print("Error executing SQL script", e)
    self.mydb.commit()
  
  def sendemail(self,filename,stu_id,course_id):
    class_id = self.nearestClass(stu_id, course_id)[0]
    if class_id==0:
      return
    self.mycursor.execute(f"SELECT * from CourseClass, Courses WHERE CourseClass.course_id=Courses.course_id AND CourseClass.course_id = '{course_id}' AND CourseClass.class_id='{class_id}'") #input instructions
    myresult = self.mycursor.fetchall()
    self.mycursor.execute(f"SELECT email from Student WHERE student_id='{stu_id}'") #input instructions
    myresult1 = self.mycursor.fetchall()
    material_paths=[]
    for i in range(len(filename)):
      self.mycursor.execute(f"SELECT CM.file_path from CourseMaterial AS CM JOIN CourseClass AS CC WHERE CC.course_id = CM.course_id AND CC.class_id = CM.class_id AND CC.course_id = '{course_id}' AND CC.class_id = '{class_id}' AND CM.material_name = '{filename[i]}'")
      material_paths.append(self.mycursor.fetchall()[0][0])
    
    # Define email sender and receiver
    email_sender = 'dbmsgroup19@gmail.com'
    #google password: icmsicms1919
    email_password = 'gkma bvtw qbii wulg'
    email_receiver = myresult1[0][0]
    # Set the subject and body of the email
    subject = f"Please Find Your Course Information Attached - {myresult[0][9]}"
    body = f"Course Code: {myresult[0][9]}\nCourse Name: {myresult[0][12]}\nCourse Date: {myresult[0][2]}\nCourse Start Time: {myresult[0][3]}\nCourse End Time: {myresult[0][4]}\nClass Location: {myresult[0][5]}\nZoom Link: {myresult[0][6]}"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject

    em.set_content(body)

    # Add the attachment to the email
    for i in range(len(material_paths)):
      attachment_path = material_paths[i]
      with open(attachment_path, 'rb') as attachment:
          em.add_attachment(attachment.read(), maintype='application', subtype='octet-stream', filename=attachment_path)
    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


  def getCourseClassInfo(self,student_id, course_id):
    class_id = self.nearestClass(student_id,course_id)[0]
    self.mycursor.execute(f"SELECT * FROM CourseClass AS CC WHERE CC.course_id = '{course_id}' AND CC.class_id='{class_id}'") #input instructions
    myresult = self.mycursor.fetchall()
    return(myresult)

  def getCourseMaterial(self,student_id, course_id):   #for course_material.py line 43, e.g. getCourseMaterial(1)
    class_id = self.nearestClass(student_id,course_id)[0]
    self.mycursor.execute(f"SELECT CM.material_name FROM CourseMaterial AS CM WHERE CM.course_id='{course_id}' AND CM.class_id='{class_id}'") #input instructions
    myresult = self.mycursor.fetchall()
    return(myresult)

  def getCourseList(self,student_id,sem):  #for course_list.py line 48, e.g. getCourseList(1,2)
    filter = str(sem)+"%"
    self.mycursor.execute(f"SELECT courses.course_code,courses.course_name,courses.course_id from CourseTaken, Courses WHERE CourseTaken.course_id=Courses.course_id AND courses.class_code LIKE '{filter}' AND CourseTaken.student_id='{student_id}'") #input instructions
    myresult = self.mycursor.fetchall()
    return(myresult)

  def getCourseData(self,student_id, course_id):  #for course_info.py line 19, e.g. getCourseData(1,1)
    self.mycursor.execute(f"SELECT courses.course_code,courses.course_name,courses.t_message, CourseClass.class_venue, CourseClass.class_time,CourseClass.zoomlink,CourseClass.class_end_time,CourseClass.class_date from CourseTaken,CourseClass,courses WHERE CourseClass.course_id='{course_id}' AND CourseClass.course_id = Courses.course_id AND CourseTaken.course_id = CourseClass.course_id AND CourseTaken.student_id='{student_id}' ORDER BY CourseClass.class_date , CourseClass.class_time") #input instructions
    myresult = self.mycursor.fetchall()
    if (len(myresult) != 0):
      now = datetime.now()
      for i in myresult:
        if i[7]>now.date() or (i[7]==now.date() and (datetime.min + i[6]).time() > now.time()):
          return i
      return myresult[len(myresult)-1]



  def putLoginInfo(self,student_id, ctime, cdate):
    self.mycursor.execute("LOCK TABLES LoginBehaviour WRITE;")
    self.mycursor.execute(f"INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES (\"{student_id}\", \"{ctime}\", \"{cdate}\", \"00:00:00\", \"2000-01-01\");") #insert login data
    self.mycursor.execute("UNLOCK TABLES;")

  def putLogoutInfo(self,student_id, login_time, login_date, ctime, cdate):
    self.mycursor.execute("LOCK TABLES LoginBehaviour WRITE;")
    self.mycursor.execute(f"DELETE FROM LoginBehaviour WHERE student_id = \"{student_id}\" AND login_time = \"{login_time}\" AND login_date = \"{login_date}\";") #delete partial login record
    self.mycursor.execute(f"INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES (\"{student_id}\", \"{login_time}\", \"{login_date}\", \"{ctime}\", \"{cdate}\");") #insert login data
    self.mycursor.execute("UNLOCK TABLES;")

  def getStudentInfo(self,student_id):
    self.mycursor.execute(f"SELECT * FROM Student WHERE student_id = {student_id}")
    myresult = self.mycursor.fetchall()
    email = myresult[0][1]
    name = myresult[0][2]
    birthday = myresult[0][3]
    return (email, name, birthday)

  def checkLoginCredentials(self,username, password):
    
    self.mycursor.execute("SELECT username, pswd, student_id FROM LoginCredentials WHERE username = %s AND pswd = %s", (username, password))
    myresult = self.mycursor.fetchall()
    if len(myresult) != 0:
        return myresult[0][2]
    else:
        return "0000000000"

  def getCourseInfo(self,course_id):
    self.mycursor.execute(f"SELECT * FROM Courses WHERE course_id = {course_id}") 
    myresult = self.mycursor.fetchall()
    course_code = myresult[0][1]
    class_code = myresult[0][2]
    year_offered = myresult[0][3]
    coursename = myresult[0][4]
    t_message = myresult[0][5]
    return (course_code, class_code, year_offered, coursename, t_message)

  def getLoginBehaviour(self,student_id):
    self.mycursor.execute(f"SELECT * FROM LoginBehaviour WHERE student_id = '{student_id}' ORDER BY login_date DESC, login_time DESC")
    myresult = self.mycursor.fetchall()
    return myresult #(login_time, login_date, logout_time, logout_date)

  def getCourseTeacher(self,course_id):
    self.mycursor.execute(f"SELECT * FROM CourseTaught AS CT JOIN Teacher AS T WHERE CT.course_id = {course_id} AND CT.teacher_id = T.teacher_id")
    myresult = self.mycursor.fetchall()
    teacher_name = ()
    for row in myresult:
      teacher_name += row[3]
    return teacher_name


  def nearestClass(self,student_id, course_id):
    now = datetime.now()
    d_string = now.date()
    t_string = now.time()
    self.mycursor.execute(f"SELECT class_id FROM coursetaken,courseclass WHERE (courseclass.class_date > '{d_string}' OR (courseclass.class_time >= '{t_string}' AND courseclass.class_date = '{d_string}')) AND student_id = '{student_id}' AND coursetaken.course_id=courseclass.course_id AND coursetaken.course_id = '{course_id}' ORDER BY courseclass.class_date,courseclass.class_time")
    myresult = self.mycursor.fetchall()
    if (len(myresult) > 0):
      return(myresult[0])
    else:
      self.mycursor.execute(f"SELECT class_id FROM coursetaken,courseclass WHERE student_id = '{student_id}' AND coursetaken.course_id=courseclass.course_id AND coursetaken.course_id = '{course_id}' ORDER BY courseclass.class_date DESC, courseclass.class_time DESC")
      myresult = self.mycursor.fetchall()
      if (len(myresult) > 0):
        return(myresult[0])
      return((0,))

  
  def getLectureToday(self,student_id):
    now = datetime.now()
    d_string = now.strftime("%Y-%m-%d")
    self.mycursor.execute(f"SELECT * FROM CourseClass AS CC JOIN CourseTaken AS CT WHERE CC.course_id = CT.course_id AND student_id = '{student_id}' AND CC.class_date='{d_string}' ORDER BY CC.class_date ASC, CC.class_time ASC")
    myresult = self.mycursor.fetchall()
    return(myresult)
  def HaveClassIn1Hr(self,student_id):
    LectureToday= self.getLectureToday(student_id)
    for i in range(len(LectureToday)):
        if self.within1hr(LectureToday[i][2],LectureToday[i][3],LectureToday[i][4]):
            return LectureToday[i]
    return (0, 0, date(1997,1,1), timedelta(seconds=0), timedelta(seconds=0), "000", "", False, '0000000000', 0)

  def within1hr(self,date,starttime,endtime):
    now = datetime.now()
    if ((datetime.combine(date, datetime.min.time()) + starttime) <= now+timedelta(hours=1)) and ((datetime.combine(date, datetime.min.time()) + endtime) >= now): #startime < 1 hour from now and now is not yet endtime
      return True
    else:
      return False

  def checkClassWithin1Hr(self,student_id): 
    self.mycursor.execute(f"SELECT courseclass.class_date,courseclass.class_time,courseclass.class_end_time from courseclass,coursetaken WHERE courseclass.course_id=coursetaken.course_id AND coursetaken.student_id='{student_id}'")
    myresult = self.mycursor.fetchall()
    Ans = False
    for i in range(len(myresult)):
      Ans = Ans or self.within1hr(myresult[i][0],myresult[i][1],myresult[i][2])
    return(Ans)
    
  def getCourseTaken(self,student_id): 
    self.mycursor.execute(f"SELECT C.course_code, C.class_code, C.course_name FROM Courses AS C JOIN CourseTaken as CT WHERE CT.student_id = '{student_id}' and C.course_id = CT.course_id")
    myresult = self.mycursor.fetchall()
    return(myresult)

  def getLectureMaterialPath(self,course_id, class_id):
    self.mycursor.execute(f"SELECT CM.material_name FROM CourseMaterial AS CM WHERE CM.course_id = '{course_id}' and CM.class_id = '{class_id}'") #input instructions
    myresult = self.mycursor.fetchall()
    filepaths=[]
    for row in myresult:
      filepaths.append(row[0])
    return filepaths

  def getTimeTableDisplayData(self,student_id):
    today = date.today()
    weekday = today.weekday()
    sunday = today - timedelta(days=(weekday+1)%7)
    saturday = sunday + timedelta(days=6)
    self.mycursor.execute(f"SELECT C.course_id, C.course_code, C.course_name, CC.class_date, CC.class_time, CC.class_end_time FROM CourseClass AS CC JOIN CourseTaken AS CT JOIN Courses AS C WHERE CC.course_id = CT.course_id AND C.course_id = CC.course_id AND CT.student_id = '{student_id}' AND CC.class_date BETWEEN '{sunday}' AND '{saturday}' ORDER BY CC.class_date ASC, CC.class_time ASC")
    myresult = self.mycursor.fetchall()
    return myresult
