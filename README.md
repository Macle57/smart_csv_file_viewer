
This program only runs on python 3.0+; it's also recommended to use a better console than the default for properly viewing the tables like alaconda's, pycharm's etc.

This program version uses shorthand notation for variable unions to hint variables types with the 
pipe symbol(|), which was only made available after 3.10. To run the program in lower versions, <type1> | <type2> can be replaced with typing.Union[<type1>,<type2>,.....]
while importing the typing library. Variable type hinting/annotations can also be removed entirely without impacting the practical use of the program.

Between python 3.7-3.10, uncomment this line "from __future__ import annotations" to solve the pipe(|) issue from both files.

A file without any variable type hinting is also provided.

What it offers?
The system is immune to any sort of imput errors.
 Our system provides with lots of auto-correcting features like- 
- All the things except integers are ignored in all int inputs to avoid 
breaking the system. 
- Date inputs are checked for the correct format, delimiter, and 
their validity. 
- Other inputs like employee ID, phone number etc are all checked 
to avoid non-sensible inputs. 
 Smart searching features which automatically detect what the user 
is entering from Serial No. of records, Employee ID to Names and 
display the appropriate records accordingly 
 Smart name search features allow employee to enter, just the first 
name, last name or full name and have the system automatically 
detect the type and show records accordingly. 
 Employee sex, basic choice inputs, etc all support various 
synonyms for the same word to increase user’s comfort. 
 Does not use data systems like MySQL; instead, opts for more 
common and suitable and user-friendly data types like .csv which 
are used commonly by popular industries. 
 Generates smart Division and Salary reports in properly formatted 
and organized manner. 
 The code written is very versatile and can be used to display and 
format other files as well that may not share the same column 
names or degree. It can be easily optimized by changing the initial 
variables
