# student_sorter
Sorts students into courses based off of their preferences.

To use:
1. Change the data in the text files to match your needs
    - each line of courses.txt should be formatted: 'course maxstudents'
        - maxstudents is the total number of students allowed in the course for all periods
    
    - each line of periods.txt should be formatted: 'periodnum  course1  course2  course3'
        - additional courses may be added
        - make sure each course is seperated by a tab
        - easy to copy and paste from google sheets
    
    - each line of students.txt should be formatted: 'studentname   request1    request2    request3'
        - additional requests may be added
        - make sure each request is seperated by a tab
        - easy to copy and paste from google sheets

2. Run main.py
    - as of now, there is no algorithm to make sure that every student gets the same amount of classes they asked for
    - the priority is randomized
    - might need to run it a few times to get the desired result

3. Export data to whatever you'd like