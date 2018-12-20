# MovieTrailerUdacity
MovieTrailerProject for Udacity 

# About 
Utilzling the Webbrowser library, make a website which displays a movie poster as a clickable button which then displays the corresponding trailer for the film selected. 

# Installation

1. Python (used 3.6.5) Download latest: https://www.python.org/downloads/

# Dependencies

webbrowser
os
re 

# Methodology: 

The provided fresh_tomatoes.py file does an excellent job creating an abstracted template with corresponding
html, css and js which then just requires the student to create an array of favorite movies as well as one class. In the media.py file, 
I created a class: movie. This class calls itself and corresponds with different characteristics required to for the fresh_tomatoes.py file to run properly. Furthermore, the entertainment_center.py file creates a list of movies with the characteristics described by media.py. 

So, for example: my first movie listed "Good Will Hunting" in entertainment_center.py has a corresponding title, story, poster image and a link to the trailer.  

If you were to look at the fresh_tomatoes file, the last function def open_movies_page(movies) requires a class called movies to be passed through it. As aforementioned, the movies class was created in the media.py file and contains all the required chars.  

# How to run: 
  Go to project directory and run: python entertainment_center.py
  
  

