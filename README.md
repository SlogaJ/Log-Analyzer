#Log-Analyzer

<<<<<<< HEAD
This project started off as trying to code something that can filter through a log and print its contents in a readable format, then I decided to try and filter for specifc things like HTTP method, specific IP's, and then Status Codes. Finally, I put them together into one code that is able to search and print for all the desired attributes. These pieces are my first attempt at writting code that's not something like a number guessing game, a simple calculator and even a rock, paper, scissors game so they do have a lot of similarites between each other and in future projects I will work on only having the necessary code needed. :) 
=======
This project started off as trying to code something that can filter through a log and print its contents in a readable format, then I decided to try and filter for specifc things like HTTP method, specific IP's, and then Status Codes. Finally, I put them together into one code that is able to search and print for all the desired attributes. These pieces are my first attempt at writting code that's not something like a number guessing game, a simple calculator and even a rock, paper, scissors game so they do have a lot of similarites between each other and in future projects I will work on only having the necessary code needed. :)
>>>>>>> 3e6a7a31845d876836b9b137bcb4d96545125810

Log Checker allows the user to open a file depiciting apache http logs like "203.0.113.10 - - [16/May/2025:09:28:47] "GET /search?q=admin HTTP/1.1" 200 1050" and formats it in a clean and readable way.

Log HTTP Method Checker prompts the users to enter an HTTP method they want to filter for either "GET" or "POST" and it prints the logs that have the requested method.

Log IP Checker asks the user to input an IP they wish to search for and then it filters through a log file that was provided by the user and depicts every entry with the targeted IP.

Log Status Code Checker requires the user to input a valid status code to search for within their log file and prints the results.

The Log Analyzer puts the prior codes together and prompts the user to input search filters for status code, http method, and ip's. It then looks through a log file that is provided by the user for anything that matches the set filters and then shows the results.
