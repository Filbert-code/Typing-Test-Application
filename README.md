# Typing-Test-Application

A GUI program that measures a user's typing speed based on characters typed per-minute divided by 
the average character count for words (which is 5) and subtracting by the number of incorrect words per-minute.

The Python GUI library used is TKinter. A class is made for each major TKinter Frame object (a container for TKinter widgets). 
This helps to decouple the classes and allows for scalability of the program. 

A single data class, called WidgetModel, is used to store shared data between the Frame classes. The variables are updated
within the Frame classes themselves. 

![Typing-Test-Application](typingTestDemo.gif)
