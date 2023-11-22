INSERT INTO Student (student_id, email, s_name, birthday) VALUES ("3035788621", "alix@mail.com", "Alix Lee Ka Shing", "2001-10-30");
INSERT INTO Student (student_id, email, s_name, birthday) VALUES ('3035788622', "janice@connect.hku.hk", "Janice Lui", "2002-05-06");
INSERT INTO Student (student_id, email, s_name, birthday) VALUES ('3035788623', "jeremy123@outlook.com", "Jeremy Chan", "2003-07-14");
INSERT INTO Student (student_id, email, s_name, birthday) VALUES ('3035788624', "justinyeung1096@gmail.com", "Justin Yeung", "2002-04-02");
INSERT INTO Student (student_id, email, s_name, birthday) VALUES ('3035788625', "zaychan80@gmail.com", "Chan Chin Hung", "2002-08-10");

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


INSERT INTO Courses (course_id, course_code, class_code, year_offered, course_name, t_message) VALUES ("1", "COMP3278", "1A", "2023", "Introduction to database management systems", "Hi this is introduction to database management system subclass 1A");
INSERT INTO Courses (course_id, course_code, class_code, year_offered, course_name, t_message) VALUES ("2", "COMP3278", "1B", "2023", "Introduction to database management systems", "Hi this is introduction to database management system subclass 1B");
INSERT INTO Courses (course_id, course_code, class_code, year_offered, course_name, t_message) VALUES ("3", "COMP3230", "1A", "2022", "Principles of Operating Systems", "Hi2");
INSERT INTO Courses (course_id, course_code, class_code, year_offered, course_name, t_message) VALUES ("4", "COMP3314", "2B", "2023", "Machine Learning", "Hi3");
INSERT INTO Courses (course_id, course_code, class_code, year_offered, course_name, t_message) VALUES ("5", "COMP3251", "1A", "2022", "Algorithm design", "Hi4");
INSERT INTO Courses (course_id, course_code, class_code, year_offered, course_name, t_message) VALUES ("6", "COMP3252", "1A", "2022", "Algorithm design and analysis", "Hi4");
INSERT INTO Courses (course_id, course_code, class_code, year_offered, course_name, t_message) VALUES ("7", "CAES9542", "1A", "2023", "Technical English for CS Students", "Learn English");
INSERT INTO Courses (course_id, course_code, class_code, year_offered, course_name, t_message) VALUES ("8", "COMP4801", "1A", "2023", "Final Year Project", "Hi666");
INSERT INTO Courses (course_id, course_code, class_code, year_offered, course_name, t_message) VALUES ("9", "COMP3353", "1A", "2023", "Bioinformatics", "Bioinformatics is just data science!");

INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "1", "2023-09-01", "14:30:00", "16:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "2", "2023-09-05", "13:30:00", "15:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "3", "2023-09-07", "14:30:00", "16:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "4", "2023-09-12", "13:30:00", "15:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "5", "2023-09-14", "14:30:00", "16:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", True);

INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("1", "7", "2023-11-22", "01:30:00", "02:20:00", "MWT1", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", True);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "1", "2023-09-04", "15:30:00", "17:20:00", "CPD-LG.07", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "2", "2023-09-07", "15:30:00", "16:20:00", "CPD-G.02", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "3", "2023-09-11", "15:30:00", "17:20:00", "CPD-LG.07", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "4", "2023-09-14", "15:30:00", "16:20:00", "CPD-G.02", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "5", "2023-09-18", "15:30:00", "17:20:00", "CPD-LG.07", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "6", "2023-09-21", "15:30:00", "16:20:00", "CPD-G.02", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "7", "2023-09-25", "15:30:00", "17:20:00", "CPD-LG.07", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "8", "2023-09-28", "15:30:00", "16:20:00", "CPD-G.02", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "9", "2023-10-05", "15:30:00", "16:20:00", "CPD-G.02", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "10", "2023-10-12", "15:30:00", "16:20:00", "CPD-G.02", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "11", "2023-10-26", "15:30:00", "16:20:00", "CPD-G.02", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "12", "2023-10-30", "15:30:00", "17:20:00", "CPD-LG.07", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "13", "2023-11-02", "15:30:00", "16:20:00", "CPD-G.02", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "14", "2023-11-09", "15:30:00", "16:20:00", "CPD-G.02", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "15", "2023-11-13", "15:30:00", "17:20:00", "CPD-LG.07", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "16", "2023-11-20", "15:30:00", "17:20:00", "CPD-LG.07", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "17", "2023-11-23", "15:30:00", "16:20:00", "CPD-G.02", "", False);
INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ("9", "18", "2023-11-27", "15:30:00", "17:20:00", "CPD-LG.07", "", False);

INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("1", "1", "intro", "../CourseMaterials/2023-24/COMP3278/lec01.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("1", "2", "diagrams1", "../CourseMaterials/2023-24/COMP3278/lec01.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("1", "3", "diagrams1", "../CourseMaterials/2023-24/COMP3278/lec01.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("1", "3", "diagrams2", "../CourseMaterials/2023-24/COMP3278/lec02.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("1", "4", "diagrams2", "../CourseMaterials/2023-24/COMP3278/lec02.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("1", "7", "sql1", "../CourseMaterials/2023-24/COMP3278/lec03.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("1", "7", "sql2", "../CourseMaterials/2023-24/COMP3278/lec04.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "1", "lecture 1", "../CourseMaterials/2023-24/COMP3353/lecture 1.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "2", "lecture 2", "../CourseMaterials/2023-24/COMP3353/lecture 2.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "3", "lecture 3", "../CourseMaterials/2023-24/COMP3353/lecture 3.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "4", "lecture 3", "../CourseMaterials/2023-24/COMP3353/lecture 3.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "4", "lecture 4", "../CourseMaterials/2023-24/COMP3353/lecture 4.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "5", "lecture 5", "../CourseMaterials/2023-24/COMP3353/lecture 5.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "5", "lecture 6", "../CourseMaterials/2023-24/COMP3353/lecture 6.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "6", "lecture 6", "../CourseMaterials/2023-24/COMP3353/lecture 6.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "7", "lecture 7", "../CourseMaterials/2023-24/COMP3353/lecture 7.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "8", "lecture 8", "../CourseMaterials/2023-24/COMP3353/lecture 8.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "8", "lecture 9", "../CourseMaterials/2023-24/COMP3353/lecture 9.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "10", "lecture 10", "../CourseMaterials/2023-24/COMP3353/lecture 10.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "11", "lecture 11", "../CourseMaterials/2023-24/COMP3353/lecture 11.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "12", "lecture 12", "../CourseMaterials/2023-24/COMP3353/lecture 12.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "13", "lecture 13", "../CourseMaterials/2023-24/COMP3353/lecture 13.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "14", "lecture 14", "../CourseMaterials/2023-24/COMP3353/lecture 14.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "15", "lecture 15", "../CourseMaterials/2023-24/COMP3353/lecture 15.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "16", "lecture 16", "../CourseMaterials/2023-24/COMP3353/lecture 16.pdf");
INSERT INTO CourseMaterial (course_id, class_id, material_name, file_path) VALUES ("9", "17", "lecture 17", "../CourseMaterials/2023-24/COMP3353/lecture 17.pdf");



INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788621", "1");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788622", "1");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788623", "1");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788624", "1");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788625", "1");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788621", "3");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788621", "4");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788621", "5");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788622", "2");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788623", "3");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788624", "4");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788625", "5");
INSERT INTO CourseTaken (student_id, course_id) VALUES ("3035788625", "9");

INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("1", "Ping Luo");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("2", "Peter");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("3", "Sam");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("4", "Helen");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("5", "Yvonne");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("6", "Ken");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("7", "Eva");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("8", "Albert Einstein");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("9", "Jesus Christ");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("10", "RB Luo");
INSERT INTO Teachers (teacher_id, teacher_name) VALUES ("11", "Yekai Zhou");

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
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("10", "9");
INSERT INTO CourseTaught (teacher_id, course_id) VALUES ("11", "9");
  
