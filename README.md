# CS50's Introduction to Computer Science
## HarvardX - CS50x
### Week 7 Problem Set - Mario.py
<hr>


### Assignment and Requirements:
Write and execute the program that recreates Nintendo’s Super Mario Brothers' pyramids in Python, using hashes (#) for bricks.\
Program should allow the user to decide how tall the pyramids should be by prompting them for a positive integer between 1 and 8, inclusive.\

Here’s how the program might work if the user inputs 8 when prompted:

```Python
$ python mario.py
Height: 8
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```


If the user doesn’t input a positive integer between 1 and 8, inclusive, when prompted, the program should re-prompt the user until they cooperate:

```Python
$ python mario.py
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

#### Compiling And Execution:

To run a program we wrote in Python, we’ll only need to run:

```Python
$ python mario.py
```
```python``` is the name of a program called an interpreter, which reads in our source code and translates it to code that our CPU can understand, line by line.
