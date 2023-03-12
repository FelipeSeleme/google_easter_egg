Mounting /home/guest...
Welcome to foobar version 1-335-gea1c3e3-beta (2023-03-11T23:47:04.615939)

Google has a code challenge ready for you.
Success! You've managed to infiltrate Commander Lambda's evil organization, and finally earned yourself an entry-level position as a Minion on their space station. From here, you just might be able to subvert Commander Lambda's plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you'll never make it to the top...

Warning! Your invitation may expire if you leave this page. Click here to sign in so you can save your progress and resume later.

For a list of commands type help. To get started with your first challenge type request.

Mounting /home/felipeselemeribeiro...
Logged in as felipeselemeribeiro. Welcome Back!
foobar:~/ felipeselemeribeiro$ help
Use the following shell commands:

cd	change directory [dir_name]
cat	print file [file_name]
deleteme	delete all of your data associated with foobar
edit	open file in editor [file_name]
feedback	provide feedback on foobar
less	print a file a page at a time [file_name]
ls	list directory contents [dir_name]
request	request new challenge
status	print progress
submit	submit final solution file for assessment [file_name]
verify	runs tests on solution file [file_name]

Keyboard help:

Ctrl + S	save the open file [when editor is focused]
Ctrl + E	close the editor [when editor is focused]

Toggle between the editor and terminal using ESC followed by TAB, then activate with ENTER.

foobar:~/ felipeselemeribeiro$ request
Requesting challenge...
At least all this time spent running errands all over Commander Lambda's space station have given you a really good understanding of the station's layout. You'll need that when you're finally ready to destroy the LAMBCHOP and rescue the bunny workers.
New challenge "Gearing Up for Destruction" added to your home folder.
Time to solve: 168 hours.
foobar:~/ felipeselemeribeiro$ ls
gearing-up-for-destruction
journal.txt
start_here.txt
foobar:~/ felipeselemeribeiro$ cd gearing-up-for-destruction
foobar:~/gearing-up-for-destruction felipeselemeribeiro$ ls
Solution.java
constraints.txt
readme.txt
solution.py
foobar:~/gearing-up-for-destruction felipeselemeribeiro$ cat readme.txt
Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({4, 17, 50})
Output:
    -1,-1

Input:
Solution.solution({4, 30, 50})
Output:
    12,1

-- Python cases --
Input:
solution.solution([4, 30, 50])
Output:
    12,1

Input:
solution.solution([4, 17, 50])
Output:
    -1,-1

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
foobar:~/gearing-up-for-destruction felipeselemeribeiro$ cat constraints.txt
Java
====
Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method inside the Solution class

Execution time is limited.

Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive an error when you verify your solution if you have used a blacklisted class.

Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

Python
======
Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.
foobar:~/gearing-up-for-destruction felipeselemeribeiro$  
  
foobar:~/gearing-up-for-destruction felipeselemeribeiro$ edit solution.py
foobar:~/gearing-up-for-destruction felipeselemeribeiro$ verify solution.py
Verifying solution...
All test cases passed. Use submit solution.py to submit your solution  
foobar:~/gearing-up-for-destruction felipeselemeribeiro$ submit solution.py
Are you sure you want to submit your solution?
[Y]es or [N]o: y
Submitting solution...
Submission: SUCCESSFUL. Completed in: 20 hrs, 52 mins, 2 secs.

Current level: 2
Challenges left to complete level: 1

Level 1: 100% [==========================================]  
Level 2:  50% [=====================.....................]  
Level 3:   0% [..........................................]  
Level 4:   0% [..........................................]  
Level 5:   0% [..........................................]  

Type request to request a new challenge now, or come back later.
foobar:~/ felipeselemeribeiro$