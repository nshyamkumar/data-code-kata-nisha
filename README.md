***********************************Data Engineering Coding Challenges - Solution - Approach and other info *********************************************
-As the requirement was to 'generate' a fwf file, the code right now does not take any input from the user. 
It simply generates a sample fwf file with 2 records and one header ,the format of which corresponds to that in spec.json
-At this point the code does not deal with the datatype of each field or anything as it is not mentioned in spec.
--Default alignment is left and padded with spaces at the end of each record to comply with the total length of each record( which is the sum of offsets)
-For parsing fixed width records, the modules used are 'itertools' and 'operator'. Same thing can be done using Struct module or string slicing  etc .
But googled a bit and found the current approach is faster compared to others in case of dealing with huge number of records.
--While writing to or reading from fwf or csv files, the encoding specified in spec.json file is used
--Testing Strategies : As I am new to the TDD approach, I googled and used Python's 'unittest' module for developing tests.
The test implementation is not a perfect test suite, rather its an attempt to demonstrate that I can catchup with the TDD approach when it comes to 
Python development.I implented basic functionality tests like one for each function to check the main functionality of that function.
This need to be enhanced to include more tests , negative test scenarios and even for handling of huge number of records.
---For code quality, I looked at the alignment, variable definition formats,unused variable declarations, comments with description of functions, readability etc.
I did not use any tools like Pylint or so for the code quality check, which will be used in a production environment.
--On Docker implementation side,as this is something new to me, I gave it a try. But my laptop has Windows 10 home, which gives me errors 
which takes time for me to fix now.I am aware of the steps to dockerize this, but as of now I am submitting the code without that.
I will definitely try this out.
---A better approach would have been to define separate classes , one for FWF generation and another for FWF to CSV writing, 
so that they would have remained as base classes for further development.Also current code does not include exception handling.
However, right now within the available time, this is the best code I could produce.

***************************************************************************************************************************************
#################################Data Engineering Coding Challenge 
# Data Engineering Coding Challenges


## Judgment Criteria
- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

## Parse fixed width file
- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding