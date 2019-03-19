### Author is Aaron Miller

This is program allows a user to create and update a database for movies. Specifically,
a database which contains the names of movies, directors of movies and the genres of
those movies.

Through this program, a person will be able to add movies to that database,
check on all of the directors in the database and all of the movies in the database.

### Details of the program

To successfully run this program, there are a small number of files to consider:

- SI507_project3.py: This file contains the flask routes which enable us to access our
program on the internet, models (and classes) which allow us to create data tables, and through SQLAlchemy,
a database, and functions which allow our tables to be successfully created.
- all_directors.html: A template file which prints our code from the .py file to
the internet web page.
- all_movies.html: Another template file which prints our code from the .py file to
the internet web page.
- index.html: Another template file which prints our code from the .py file to
the internet web page.
- requirements.txt: A document which contains installed modules essential to successfully
running our program.

### Running the program

To run this program, a user must run the SI507_project3.py file in their terminal,
and should see a message come back similar to the below:

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 341-928-223

The user can then enter the http://127.0.0.1:5000/ code into a web browser to take them
to the index page of the program.

When this webpage is launched, the browser should print the number of movies recorded.
An example would be "0 movies saved."
-------------------------
To add a movie to the database, the user must update the web url by adding
"/movie/new/<title>/<director>/<genre>/" to the end of the web url. However,
the fields in the updated url are meant to be manually replaced with data.

title = title of the movie the user wants to enter
director = name of the director of the movie the user wants to enter
genre = genre of the movie the user wants to enter

After this is entered, the web page will send a message similar to the one below,
confirming that the movie has been added to the database:
"New movie: It's A Wonderful Life by Frank Capra."
--------------------------
To see all of the movies in the database, the user should update the web url
after http://127.0.0.1:5000/ with /all_movies. This will print on the webpage
a bulleted list of all the movies, similar to the example below:

Jurrasic Park by Steven Speilberg - Action

Good Will Hunting by Gus Van Sant - Drama

Catch Me If You Can by Steven Spielberg - Drama

It's A Wonderful Life by Frank Capra - Drama
--------------------------
To see all of the directors in the database, the user should update the web url
after http://127.0.0.1:5000/ with /all_directors. This will print on the webpage
a bulleted list of all the directors, similar to the example below:

Gus Van Sant: 1 movie

Steven Spielberg: 1 movie

Frank Capra: 1 movie
--------------------------

As a user works with this program, it will update a file called sample_movies.db,
which is the SQLAlchemy database which a user can utilize in SQL.
