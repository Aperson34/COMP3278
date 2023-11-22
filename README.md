# COMP3278
User Menu for ICMS

Before using the ICMS:
First, go to Backend.py. In __init__ method of the class Backend, replace the default password with the corresponding password to your local mySQL server.
Next, in cmd, run the command "python initDatabase" to initialise the database to be used by ICMS.
Then, navigate to /COMP3278/GUI and run the command "python mainlayout.py" to start using the ICMS.

Login to the ICMS:
At login page, you could enter the correct username and password to login to the system.
On the other hand, you may click the button with a face icon to switch to the face recognition login page. Click the slider and wait for a few seconds to turn on the camera. If the system recognise your face, it will automatically login to the system. If you changed your mind, click 'Return to Login' to login with username and password.

Using the ICMS:
Right after login, if you have a class within one hour or there's a class you need to attend currently, the information of that class and the corresponding course will be displayed. In the case that there is currently a class, as well as a class in 1-hour time, information of the class closest to the current time (i.e. the current class), will be display.

On the right is information of the class, while on the left is the list of lecture materials to be used in the class. Click 'Get Material', then in the next page check the checkbox of the materials you need and click 'Send to Email'. You should get the materials sent to your email recorded in the database.

If you have no class in the next hour, your timetable for the week is displayed instead.

Click the icon with 3 bars on the left-upper corner of the screen, a sidebar will be shown with several options. Click 'Timetable' to view your lectures in this week.

Click 'Profile' to check you personal information as well as the login behaviour. Note that current login session will have logout date and time displayed as '2000-01-01 00:00:00'.

Click 'Course List' to see the list of courses you enrolled in this academic year. Click on those courses will redirect you to page similar to that displayed if you have class within 1 hour. Information about the course as well as the closest next class, or the previous class if there is no next class, will be displayed. You can get materials of that class from that course as well.

Finally, in the sidebar, click 'Logout' to logout from the ICMS. Your logout date and time will be recorded and can be seen during next login session.