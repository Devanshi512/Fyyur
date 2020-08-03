# Fyyur: Venue Booking Site for Artists

This project is a part of Udacity Full-Stack Nano Degree Program. Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and available venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.

I built the data models to power the API endpoints for the Fyyur site by connecting to a PostgreSQL database for storing, querying, and creating information about artists and venues on Fyyur.

### Overview

This site is capable of using models and model interactions to store, retrieve, and update the data from PostgreSQL database.

>> creating new venues, artists, and shows.<br />
>> searching for venues and artists.<br />
>> learning more about a specific artist or venue or show.

### Tech Stack

>> **SQLAlchemy ORM** to be our ORM library of choice<br />
>> **PostgreSQL** as database of choice<br />
>> **Python3** and **Flask** as server language and server framework<br />
>> **Flask-Migrate** for creating and running schema migrations<br />
>> **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) to render beautiful look for website

### Screenshots:::

>> A. Home Page with capabilities of creating, editing, displaying the venue, artist and show details
![Alt text](Image/fyyur_home_page.png?raw=true "Home Page")

>> B. Find Venue
![Alt text](Image/fyyur_find_venue.png?raw=true "Find Venue")

>> C. Find an Artist
![Alt text](Image/fyyur_find_artist.png?raw=true "Find Artist")

>> D. See available shows
![Alt text](Image/fyyur_available_shows.png?raw=true "Available Shows")

### Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app.
                    "python3 app.py" to run after installing dependences
  ├── config.py *** Database URLs, CSRF generation, etc
  ├── error.log
  ├── forms.py
  ├── models.py  
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├── static
  │   ├── css
  │   ├── font
  │   ├── ico
  │   ├── img
  │   └── js
  └── templates
      ├── errors
      ├── forms
      ├── layouts
      └── pages
  ```

### Summary

* Models are located in `models.py`.
* Controllers are located in `app.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `static/`.
* Web forms for creating data are located in `form.py`

### Getting Started

* Install Flask if not installed: ```pip install flask```
* Clone this repo: ```git clone <cloned repo-path>```
* Change to the repo directory: ```cd Fyyur```
* If you want to use virtualenv: ```virtualenv ENV && source ENV/bin/activate```
* Install dependencies with pip: ```pip install -r requirements.txt```
* To connect with your local database, do the replacement below:
  * in app.py ```app.config['SQLALCHEMY_DATABASE_URI'] = '<your database>'```
  * in config.py ```SQLALCHEMY_DATABASE_URI = '<your database>'```
* Run the development server:
  ```
  $ export FLASK_APP=myapp
  $ export FLASK_ENV=development #Enables debug mode
  $ python3 app.py
  ```
* Navigate to Home page [http://localhost:5000](http://localhost:5000)
