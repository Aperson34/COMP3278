INSERT INTO Student (student_id, email, s_name, birthday) VALUES ('3035788621', "alix@mail.com", "Alix Lee Ka Shing", "2001-10-30");
INSERT INTO Student (student_id, email, s_name, birthday) VALUES ('3035788622', "janice@connect.hku.hk", "Janice Lui", "2002-05-06");
INSERT INTO Student (student_id, email, s_name, birthday) VALUES ('3035788623', "jeremy123@outlook.com", "Jeremy Chan", "2003-07-14");
INSERT INTO Student (student_id, email, s_name, birthday) VALUES ('3035788624', "justin@gmail.com", "Justin NG", "1999-12-09");
INSERT INTO Student (student_id, email, s_name, birthday) VALUES ('3035788625', "zaychan@connect.hku.hk", "Chan Chin Hung", "2002-08-10");

INSERT INTO LoginCredentials (username, pswd, student_id) VALUES ("alix", "alix1030", "3035788621");
INSERT INTO LoginCredentials (username, pswd, student_id) VALUES ("janice", "jlui0506", "3035788622");
INSERT INTO LoginCredentials (username, pswd, student_id) VALUES ("jeremy123", "j123714", "3035788623");
INSERT INTO LoginCredentials (username, pswd, student_id) VALUES ("justin", "j1999", "3035788624");
INSERT INTO LoginCredentials (username, pswd, student_id) VALUES ("zaychan", "Z@yChan80", "3035788625");

INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("3035788621", "10:20:03", "2023-11-02", "12:02:03", "2023-11-02");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("3035788622", "13:12:04", "2023-11-13", "14:02:03", "2023-11-13");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("3035788623", "23:52:34", "2023-11-16", "00:01:03", "2023-11-17");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("3035788624", "05:04:06", "2023-10-24", "05:06:03", "2023-10-24");
INSERT INTO LoginBehaviour (student_id, login_time, login_date, logout_time, logout_date) VALUES ("3035788625", "23:02:07", "2023-11-16", "23:05:04", "2023-11-16");


INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("1", "COMP3278", "1A", "2023", "Introduction to database management systems", "Hi this is introduction to database management system subclass 1A");
INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("2", "COMP3278", "1B", "2023", "Introduction to database management systems", "Hi this is introduction to database management system subclass 1B");
INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("3", "COMP3230", "1A", "2022", "Principles of Operating Systems", "Hi2");
INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("4", "COMP3314", "2B", "2023", "Machine Learning", "Hi3");
INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("5", "COMP3251", "1A", "2022", "Algorithm design", "Hi4");
INSERT INTO Courses (course_id, course_code, class_id, year_offered, course_name, welcome_message) VALUES ("6", "COMP3252", "1A", "2022", "Algorithm design and analysis", "Hi4");

INSERT INTO CourseClass (course_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-01", "14:30:00", "16:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", False);
INSERT INTO CourseClass (course_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-05", "13:30:00", "15:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", False);
INSERT INTO CourseClass (course_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-07", "14:30:00", "16:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", False);
INSERT INTO CourseClass (course_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-12", "13:30:00", "15:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", False);
INSERT INTO CourseClass (course_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-14", "14:30:00", "16:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", True);
INSERT INTO CourseClass (course_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-19", "13:30:00", "15:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", False);
INSERT INTO CourseClass (course_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2023-09-21", "14:30:00", "16:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", True);

INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-01", "14:30:00", "intro", "C:\\Users\\admin\\Desktop\\COMP3278\\lec0.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-05", "13:30:00", "diagrams1", "C:\\Users\\admin\\Desktop\\COMP3278\\lec1.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-07", "14:30:00", "diagrams1", "C:\\Users\\admin\\Desktop\\COMP3278\\lec1.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-12", "13:30:00", "diagrams2", "C:\\Users\\admin\\Desktop\\COMP3278\\lec2.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-14", "14:30:00", "diagrams2", "C:\\Users\\admin\\Desktop\\COMP3278\\lec2.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-19", "13:30:00", "sql1", "C:\\Users\\admin\\Desktop\\COMP3278\\lec3.pdf");
INSERT INTO CourseMaterial (course_id, class_date, class_time, material_name, file_path) VALUES ("1", "2023-09-21", "14:30:00", "sql2", "C:\\Users\\admin\\Desktop\\COMP3278\\lec3.pdf");

INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788621", "1");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788622", "1");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788623", "1");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788624", "1");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788625", "1");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788621", "3");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788621", "4");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788621", "5");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788622", "2");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788623", "3");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788624", "4");
INSERT INTO ClassTaken (student_id, course_id) VALUES ("3035788625", "5");

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
  
INSERT INTO TeacherMessage (teacher_id, course_id, t_message, message_date, message_time) VALUES ("1", "1", "Hi", "2023-08-25", "13:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, t_message, message_date, message_time) VALUES ("2", "2", "Hi1", "2023-08-25", "14:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, t_message, message_date, message_time) VALUES ("3", "1", "Hi2", "2023-08-25", "15:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, t_message, message_date, message_time) VALUES ("4", "3", "Hi3", "2023-08-25", "16:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, t_message, message_date, message_time) VALUES ("5", "4", "Hi4", "2023-08-25", "17:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, t_message, message_date, message_time) VALUES ("6", "4", "Hi5", "2023-08-25", "18:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, t_message, message_date, message_time) VALUES ("7", "5", "Hi6", "2023-08-25", "19:30:00");
INSERT INTO TeacherMessage (teacher_id, course_id, t_message, message_date, message_time) VALUES ("8", "5", "E=mc2", "2023-11-01", "00:00:01");
INSERT INTO TeacherMessage (teacher_id, course_id, t_message, message_date, message_time) VALUES ("8", "6", "E=mc2", "2023-10-010", "00:00:01");
INSERT INTO TeacherMessage (teacher_id, course_id, t_message, message_date, message_time) VALUES ("9", "6", "Believe", "2023-11-17", "00:00:01");