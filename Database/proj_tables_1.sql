

-- Create TABLE 'Student'
CREATE TABLE Student (
  student_id varchar(10) NOT NULL UNIQUE,
  email varchar(50) NOT NULL,
  s_name varchar(50) NOT NULL,
  birthday date NOT NULL,
  PRIMARY KEY (student_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create TABLE 'LoginCredentials'
CREATE TABLE LoginCredentials(
  username varchar(50) NOT NULL UNIQUE,
  pswd varchar(50) NOT NULL,
  student_id varchar(10) NOT NULL UNIQUE,
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  PRIMARY KEY (username)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- Create TABLE 'LoginBehaviour'
CREATE TABLE LoginBehaviour (
  student_id varchar(10) NOT NULL,
  login_time time NOT NULL,
  login_date date NOT NULL,
  logout_time time NOT NULL,
  logout_date date NOT NULL,
  PRIMARY KEY (student_id, login_time, login_date),
  FOREIGN KEY (student_id) REFERENCES Student(student_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- CREATE TABLE 'Courses'
CREATE TABLE Courses (
  course_id int NOT NULL UNIQUE,
  course_code varchar(8) NOT NULL,
  class_code varchar(2) NOT NULL,
  year_offered int NOT NULL,
  course_name varchar(50) NOT NULL,
  t_message varchar(1000),
  PRIMARY KEY (course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- CREATE TABLE 'CourseClass'
CREATE TABLE CourseClass (
  course_id int NOT NULL,
  class_id int NOT NULL,
  class_date date NOT NULL,
  class_time time NOT NULL,
  class_end_time time NOT NULL,
  class_venue varchar(10),
  zoomlink varchar(1000),
  is_tutorial boolean NOT NULL,
  PRIMARY KEY (course_id, class_id),
  FOREIGN KEY (course_id) REFERENCES Courses(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- CREATE TABLE 'CourseMaterial'
CREATE TABLE CourseMaterial (
  course_id int NOT NULL,
  class_id int NOT NULL,
  material_name varchar(50) NOT NULL,
  file_path varchar(100) NOT NULL,
  PRIMARY KEY (course_id, class_id, material_name),
  FOREIGN KEY (course_id, class_id) REFERENCES CourseClass(course_id, class_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- CREATE TABLE 'CourseTaken'
CREATE TABLE CourseTaken (
  student_id varchar(10) NOT NULL,
  course_id int NOT NULL,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (course_id) REFERENCES Courses(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- CREATE TABLE 'Teachers'
CREATE TABLE Teachers (
  teacher_id int NOT NULL UNIQUE,
  teacher_name varchar(80) NOT NULL,
  PRIMARY KEY (teacher_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- CREATE TABLE 'CourseTaught'
CREATE TABLE CourseTaught (
  teacher_id int NOT NULL,
  course_id int NOT NULL,
  PRIMARY KEY (teacher_id, course_id),
  FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id),
  FOREIGN KEY (course_id) REFERENCES Courses(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

