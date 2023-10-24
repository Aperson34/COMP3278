DROP TABLE IF EXISTS `Student`;

# Create TABLE 'Student'
CREATE TABLE `Student` (
  `student_id` int NOT NULL,
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `birthday` date NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


# Create TABLE 'LoginBehaviour'
CREATE TABLE `LoginBehaviour` (
  `login_time` time NOT NULL,
  `login_date` date NOT NULL,
  `logout_time` time NOT NULL,
  `logout_date` date NOT NULL,
  `student_id` int NOT NULL,
  PRIMARY KEY (`student_id`, `login_time`, `login_date`)
);

# CREATE TABLE 'RegconitionModel'
CREATE TABLE `RegconitionModel` (
  `model_id` int NOT NULL,
  `file_path` varchar(100) NOT NULL,
  `date_created` date NOT NULL,
  `student_id` int NOT NULL,
  PRIMARY KEY (`model_id`)
);

# CREATE TABLE 'Courses'
CREATE TABLE `Courses` (
  `course_id` varchar(8) NOT NULL,
  `class` varchar(2) NOT NULL,
  `year_offered` int NOT NULL,
  `course_name` varchar(50) NOT NULL,
  `welcome_message` varchar(1000) NOT NULL,
  PRIMARY KEY (`course_id`, `class`, `year_offered`)
);

#CREATE TABLE 'CourseClass'
CREATE TABLE `CourseClass` (
  `course_id` varchar(8) NOT NULL,
  `class` varchar(2) NOT NULL,
  `year_offered` int NOT NULL, 
  `class_date` date NOT NULL,
  `class_time` time NOT NULL,
  `class_venue` varchar(8) NOT NULL,
  `zoomlink` varchar(100) NOT NULL,
  PRIMARY KEY (`course_id`, `class`, `year_offered`, `class_date`, `class_time`)
);

# CREATE TABLE 'CourseMaterial'
CREATE TABLE `CourseMaterial` (
  `course_id` varchar(8) NOT NULL,
  `class` varchar(2) NOT NULL,
  `year_offered` int NOT NULL,
  `material_name` varchar(50),
  `file_path` varchar(100) NOT NULL,
  PRIMARY KEY (`course_id`, `class`, `year_offered`, `material_name`)
);

# CREATE TABLE 'ClassTaken'
CREATE TABLE `ClassTaken` (
  `student_id` int NOT NULL,
  `course_id` varchar(8) NOT NULL,
  `class` varchar(2) NOT NULL,
  `year_offered` int NOT NULL,
  PRIMARY KEY (`student_id`, `course_id`, `class`, `year_offered`)
);
