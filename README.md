# AMAZON RASPBERRY PI SCRAPER

## INITIALLY

  Was in search of a new phone (had my eyes on the Samsung A70 at the time) and wanted a way to save the files and incorporate it into my personal project Flask server
  that I was working on to control different objects, view my 3D printer and keep track of a few programs that were running. In this case I didnt want to bog down
  my own computer with checking, so I decided to write the script to run on a Raspberry Pi and return the data to the Flask server I had running on my home server.

## LOOKING BACK

  This functioned for what I was trying to do, although there are a few things I would change if I was to do this code again...
  - Make the code more modular
    -  I had to go in and manually edit the code to keep track of the system, what I would rather do is have a way of adding it via the flask server to monitor it that way.
  - Likely use a different form of notification
    - I believe I was using Pushbullet at the time, I would rather use just plain email for something like this to keep track of stock and prices. Tend to notice it come in more then a rarely used app.

  I have learned alot since making this web scraper but it does come in handy to look back reference some of the code I used at the time.
