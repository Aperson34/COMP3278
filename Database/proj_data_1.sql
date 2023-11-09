INSERT INTO Student (student_id, email, name, birthday, password) VALUES ('1', "mail@mail.com", "Alix", "1970-01-01", "123");
INSERT INTO Student (student_id, email, name, birthday, password) VALUES ('2', "mail@mail.com", "Janice", "1970-01-01", "124");
INSERT INTO Student (student_id, email, name, birthday, password) VALUES ('3', "mail@mail.com", "Jeremy", "1970-01-01", "215");
INSERT INTO Student (student_id, email, name, birthday, password) VALUES ('4', "mail@mail.com", "Justin", "1970-01-01", "124");
INSERT INTO Student (student_id, email, name, birthday, password) VALUES ('5', "mail@mail.com", "Zay", "1970-01-01", "355");

INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("1", "01:02:03", "2023-11-02", "05:02:03", "2023-11-02");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("2", "01:02:04", "2023-11-02", "05:02:03", "2023-11-02");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("3", "01:02:05", "2023-11-02", "05:02:03", "2023-11-02");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("4", "01:02:06", "2023-11-02", "05:02:03", "2023-11-02");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("5", "01:02:07", "2023-11-02", "05:02:03", "2023-11-02");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("4", "11:22:33", "2023-11-03", "22:33:44", "2023-11-03");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("3", "12:34:56", "2023-11-04", "21:44:05", "2023-11-04");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("5", "07:14:23", "2023-11-06", "07:15:11", "2023-11-06");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("5", "21:21:21", "2023-11-06", "22:22:22", "2023-11-07");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("1", "01:02:03", "2023-11-06", "05:02:03", "2023-11-08");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("2", "01:02:03", "2023-11-06", "05:02:03", "2023-11-07");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("4", "01:02:03", "2023-11-07", "05:02:03", "2023-11-07");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("3", "01:02:03", "2023-11-08", "05:02:03", "2023-11-08");

INSERT INTO RecognitionModel (model_id, file_path, date_created, student_id) VALUES ("1", "C:\\Users\\admin\\Desktop\\DB_SYSTEM\\model1.txt", "2023-11-02", "1");
INSERT INTO RecognitionModel (model_id, file_path, date_created, student_id) VALUES ("2", "C:\\Users\\admin\\Desktop\\DB_SYSTEM\\model2.txt", "2023-11-02", "2");
INSERT INTO RecognitionModel (model_id, file_path, date_created, student_id) VALUES ("3", "C:\\Users\\admin\\Desktop\\DB_SYSTEM\\model3.txt", "2023-11-02", "3");
INSERT INTO RecognitionModel (model_id, file_path, date_created, student_id) VALUES ("4", "C:\\Users\\admin\\Desktop\\DB_SYSTEM\\model4.txt", "2023-11-02", "4");
INSERT INTO RecognitionModel (model_id, file_path, date_created, student_id) VALUES ("5", "C:\\Users\\admin\\Desktop\\DB_SYSTEM\\model5.txt", "2023-11-02", "5");

INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("1", "COMP3278", "1A", "2023", "Introduction to database management systems", "Hi");
INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("2", "COMP3278", "1B", "2023", "Introduction to database management systems", "Hi");
INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("3", "COMP3230", "1", "2022", "Principles of Operating Systems", "Hi2");
INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("4", "COMP3314", "2", "2023", "Machine Learning", "Hi3");
INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("5", "COMP3251", "1A", "2022", "Algorithm design", "Hi4");
INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("6", "COMP3252", "1A", "2022", "Algorithm design and analysis", "Hi4");

INSERT INTO CourseClass (course_id, class_date, class_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-01", "14:30:00", "Meng Wah Complex MWT1", "https://hku.zoom.us/rec/share/AXpuCAAJ_3nxGng3GDBvWYCAcTtRerCOI0rHpLyKCGV_YiM9Y-XYSGdVWDGx_Jg.lubxpz6SgAXZxmiv", "False");
INSERT INTO CourseClass (course_id, class_date, class_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-05", "13:30:00", "Meng Wah Complex MWT1", "https://hku.zoom.us/rec/share/AXpuCAAJ_3nxGng3GDBvWYCAcTtRerCOI0rHpLyKCGV_YiM9Y-XYSGdVWDGx_Jg.lubxpz6SgAXZxmiv", "False");
INSERT INTO CourseClass (course_id, class_date, class_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-07", "14:30:00", "Meng Wah Complex MWT1", "https://hku.zoom.us/rec/share/AXpuCAAJ_3nxGng3GDBvWYCAcTtRerCOI0rHpLyKCGV_YiM9Y-XYSGdVWDGx_Jg.lubxpz6SgAXZxmiv", "False");
INSERT INTO CourseClass (course_id, class_date, class_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-12", "13:30:00", "Meng Wah Complex MWT1", "https://hku.zoom.us/rec/share/AXpuCAAJ_3nxGng3GDBvWYCAcTtRerCOI0rHpLyKCGV_YiM9Y-XYSGdVWDGx_Jg.lubxpz6SgAXZxmiv", "False");
INSERT INTO CourseClass (course_id, class_date, class_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-14", "14:30:00", "Meng Wah Complex MWT1", "https://hku.zoom.us/rec/share/AXpuCAAJ_3nxGng3GDBvWYCAcTtRerCOI0rHpLyKCGV_YiM9Y-XYSGdVWDGx_Jg.lubxpz6SgAXZxmiv", "True");
INSERT INTO CourseClass (course_id, class_date, class_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-19", "13:30:00", "Meng Wah Complex MWT1", "https://hku.zoom.us/rec/share/AXpuCAAJ_3nxGng3GDBvWYCAcTtRerCOI0rHpLyKCGV_YiM9Y-XYSGdVWDGx_Jg.lubxpz6SgAXZxmiv", "False");
INSERT INTO CourseClass (course_id, class_date, class_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-21", "14:30:00", "Meng Wah Complex MWT1", "https://hku.zoom.us/rec/share/AXpuCAAJ_3nxGng3GDBvWYCAcTtRerCOI0rHpLyKCGV_YiM9Y-XYSGdVWDGx_Jg.lubxpz6SgAXZxmiv", "True");

INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-01", "14:30:00", "intro", "C:\\Users\\admin\\Desktop\\COMP3278\\lec0.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-05", "13:30:00", "diagrams1", "C:\\Users\\admin\\Desktop\\COMP3278\\lec1.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-07", "14:30:00", "diagrams1", "C:\\Users\\admin\\Desktop\\COMP3278\\lec1.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-12", "13:30:00", "diagrams2", "C:\\Users\\admin\\Desktop\\COMP3278\\lec2.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-14", "14:30:00", "diagrams2", "C:\\Users\\admin\\Desktop\\COMP3278\\lec2.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-19", "13:30:00", "sql1", "C:\\Users\\admin\\Desktop\\COMP3278\\lec3.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-21", "14:30:00", "sql2", "C:\\Users\\admin\\Desktop\\COMP3278\\lec3.pdf");

INSERT INTO ClassTaken (student_id, course_id) VALUES ("1", "1");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("2", "1");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3", "1");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("4", "1");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("5", "1");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("1", "3");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("1", "4");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("1", "5");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("2", "2");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3", "3");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("4", "4");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("5", "5");

INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("1", "Ping Luo");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("2", "Peter");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("3", "Sam");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("4", "Helen");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("5", "Yvonne");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("6", "Ken");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("7", "Eva");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("8", "Albert Einstein");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("9", "Jesus Christ");

INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("1", "1");
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("2", "2");
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("3", "1");
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("4", "3");
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("5", "4");
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("6", "4");
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("7", "5");
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("8", "5");
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("8", "6");
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("9", "6");
  
INSERT INTO TeacherMessage (teacher_id, course_id, message, message_date, message_time) VALUES ("1", "1", "Hi", "2023-08-25", "13:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, message, message_date, message_time) VALUES ("2", "2", "Hi1", "2023-08-25", "14:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, message, message_date, message_time) VALUES ("3", "1", "Hi2", "2023-08-25", "15:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, message, message_date, message_time) VALUES ("4", "3", "Hi3", "2023-08-25", "16:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, message, message_date, message_time) VALUES ("5", "4", "Hi4", "2023-08-25", "17:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, message, message_date, message_time) VALUES ("6", "4", "Hi5", "2023-08-25", "18:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, message, message_date, message_time) VALUES ("7", "5", "Hi6", "2023-08-25", "19:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, message, message_date, message_time) VALUES ("8", "5", "E=mc2", "1970-01-01", "00:00:01");
INSERT INTO TeacherMessage (teacher_id, course_id, message, message_date, message_time) VALUES ("8", "6", "E=mc2", "1970-01-01", "00:00:01");
INSERT INTO TeacherMessage (teacher_id, course_id, message, message_date, message_time) VALUES ("9", "6", "Believe", "1970-01-01", "00:00:01");