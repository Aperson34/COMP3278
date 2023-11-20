#for testing purposes
from Backend import *
createicms()
executeSQL("proj_tables_1.sql")
executeSQL("proj_data_1.sql")


#(email,name,birthday) = getStudentInfo("3035788625")
#print(email, name, birthday)
#print(checkLoginCredentials("zaychan", "123"))
#print(HaveClassIn1Hr(getLectureToday("3035788625")))
