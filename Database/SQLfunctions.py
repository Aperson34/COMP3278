#for testing purposes
from Backend import *
temp = Backend()
temp.__init__()
temp.createicms()

now = datetime.now()
d_string = now.strftime("%Y-%m-%d")
temp.mycursor.execute(f"SELECT * FROM CourseClass AS CC JOIN CourseTaken AS CT WHERE CC.course_id = CT.course_id AND student_id = '3035788625' ORDER BY CC.class_date ASC, CC.class_time ASC") #input instructions
myresult = temp.mycursor.fetchall()
print(myresult)
for i in range(len(myresult)):
    print(i)
    print(type(myresult[i]))    
#return [(0, 0, "1997-01-01", timedelta(days=0), timedelta(days=0), "000", "", False)]

#(email,name,birthday) = getStudentInfo("3035788625")
#print(email, name, birthday)
#print(checkLoginCredentials("zaychan", "123"))
#print(HaveClassIn1Hr(getLectureToday("3035788625")))
