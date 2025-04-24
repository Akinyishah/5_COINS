 -We have been returning strings step forward 
 return a simple HTML page (homepage)
 SERVE HTML PAGES FOLLOW THE BELOW RULES:
                  5 COINS RESTAURANT structured
5coins                  
    -main.py
    -database.py
 create a folder that holds all the HTML stuff 
    1.templates(all html files will be inside here() e.g 
    index.html.
    menu.html.
    contact.html )   
    2.static-(Files that do not change much)
    -all static files which are the 
    styling e.g myduka.css.style.css,home.css
    images
    java script files
    favicons-small logos that appear at the top there.
    fonts, PDF files
#

#RENDERING- Process of serving HTML with Flask
Goal is to display HTML page file using flask

#IMPLEMENTATION-
we render HTML pages using functions provided by flask
its called render_template()-this function:
1.has to be imported from flask in order to be used next to import from flask put a comma then render_template
2.it takes some parameters - full name of my HTML page
e.g render_template('index.html')