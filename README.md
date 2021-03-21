<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Airport Parking App</h3>
  <p align="center">
    A simple app to map airport car parking spaces
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Running The Application](#installation)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

![Screen Shot][product-screenshot]

This project is a small assignment which was to make a car parking map where people could input their numberplates and that parking space would be assigned to them. It uses a tkinter frontend with a REST API backend using Flask and SQLite3. It is very buggy and also does not use the best practises whatsoever. Heck, there is no ability to remove the numberplates from the database! As with all my archived projects, I probably will not update this ever, its just a good reference and example of some of my work (allbeit not the best).


### Built With

* [Python](https://python.org)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Flask](https://flask.palletsprojects.com/)
* [SQLite3](https://www.sqlite.org/)

### Run The Application
You need Python 3 and PIP installed to run this. Python 2 is not supported.

1. Clone the repo
```sh
git clone https://github.com/JackHumphries9/formula-calculator.git
```

EXTRA STEP FOR LINUX:
If you are on Linux, you may need to install tkinter using the package manager. On debian based systems do:
```
sudo apt install python-tk
```

2. Install the dependencies
```
pip install requests flask
```
3. In one terminal window run the server:
```
python3 server.py
```
4. In another terminal window, run the client:
```
python3 client.py
```

<!-- CONTRIBUTING -->
## Contributing

I am not actively working on this project so I will not be merging any pull requests. Feel free to fork the project though and make it your own.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Your Name - [@JackPHumphries](https://twitter.com/JackPHumphries) - me@jackhumphries.dev

Project Link: [https://github.com/JackHumphries9/airport-parking](https://github.com/JackHumphries9/airport-parking)

[product-screenshot]: ./screenshot.png
