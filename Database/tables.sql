DROP TABLE IF EXISTS `Student`;

# Create TABLE 'Student'
CREATE TABLE `Student` (
  `student_id` int NOT NULL,
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `birthday` date NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


# Create TABLE 'LoginBehaviour'
CREATE TABLE `LoginBehaviour` (
  `student_id` int NOT NULL,
  `login_time` time NOT NULL,
  `login_date` date NOT NULL,
  `logout_time` time NOT NULL,
  `logout_date` date NOT NULL,
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
  `course_id` int NOT NULL,
  `course_code` varchar(8) NOT NULL,
  `class_id` varchar(2) NOT NULL,
  `year_offered` int NOT NULL,
  `course_name` varchar(50) NOT NULL,
  `welcome_message` varchar(1000),
  PRIMARY KEY (`course_id`)
);

#CREATE TABLE 'CourseClass'
CREATE TABLE `CourseClass` (
  `course_id` int NOT NULL,
  `class_date` date NOT NULL,
  `class_time` time NOT NULL,
  `class_venue` varchar(8),
  `zoomlink` varchar(100),
  `is_tutorial` boolean NOT NULL,
  PRIMARY KEY (`course_id`, `class_date`, `class_time`)
);

# CREATE TABLE 'CourseMaterial'
CREATE TABLE `CourseMaterial` (
  `course_id` int NOT NULL,
  `class_date` date NOT NULL,
  `class_time` time NOT NULL,
  `material_name` varchar(50) NOT NULL,
  `file_path` varchar(100) NOT NULL,
  PRIMARY KEY (`course_id`, `material_name`, `class_date`, `class_time`)
);

# CREATE TABLE 'ClassTaken'
CREATE TABLE `ClassTaken` (
  `student_id` int NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`student_id`, `course_id`)
);

# CREATE TABLE 'Teachers'
CREATE TABLE `Teachers` (
  `teacher_id` int NOT NULL,
  `teacher_name` varchar(80) NOT NULL,
  PRIMARY KEY (`teacher_id`)
);

# CREATE TABLE 'CourseTaught'
CREATE TABLE `CourseTaught` (
  `teacher_id` int NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`teacher_id`, `course_id`)
);

#CREATE TABLE 'TeacherMessage'
CREATE TABLE `TeacherMessage` (
  `teacher_id` int NOT NULL,
  `course_id` int NOT NULL,
  `message` varchar(1000) NOT NULL;
  `message_date` date NOT NULL,
  `message_time` time NOT NULL,
  PRIMARY KEY (`teacher_id`, `course_id`, `message_date`, `message_time`)
);
