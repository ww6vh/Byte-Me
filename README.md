[![Build Status](https://travis-ci.org/ww6vh/Byte-Me.svg?branch=master)](https://travis-ci.org/ww6vh/Byte-Me)
# Byte-Me
An online market place for buying and selling computers (desktops and laptops). 

Our home page for the website is accessed at http://127.0.0.1:8000/home/ and http://127.0.0.1:8000/

**Home Page:** 
The home page displays the three most reccently added computers in the market place. Each computer is displayed with it's name, and a "View Details" button underneath it. The button, when clicked, leads to the description page for the respective computer. 

**Description Page:**
The computer is looked up based on its primary key, and its details/specs are display. The specs include "make", "model", "condition", and "description".  

**Project 5:** 
To use the search function, please create a new listing and search for those new computers. The search function cannot find the computers from the fixture.

**Project 7:**
Please run the following command after all containers are up. It automatically sets up the two spark containers to have MySQL packages and executes the spark program every 30 seconds.  
~~~~
sh spark_setup.sh
~~~~
