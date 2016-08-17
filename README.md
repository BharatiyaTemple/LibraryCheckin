
<p align="center">
  <img src="https://github.com/BharatiyaTemple/LibraryCheckin/blob/master/static/img/logo.png" width="350"/>
  
</p>

# Library Checkin  :books:

This application allows library visitors to check in themselves so the front desk can focus on providing a warm and personal welcome.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisities
<a href="https://www.python.org/downloads/">Python 3.5 or Higher running on your local system </a> <br>
<a href="http://flask.pocoo.org/docs/0.11/installation/">Install Virtual Enviorment</a>


### Installing

Activate Virtual Enviorment
```
venv/bin/activate
```
Install requirements.txt
```
pip install -r /path/to/requirements.txt
```
Run main Python Checkin.py
```
sudo python3 checkin.py
```

## Deployment
Open models.py

comment or remove
```
DATABASE = SqliteDatabase('test.db', check_same_thread=False)
```
uncomment AWS file and fillout the info from your AWS account 
```
#for AWS use this
#DATABASE = MySQLDatabase("checkin", host="AWS KEY.amazonaws.com", port=3306, user="AWS user", passwd="AWS password!")
```

## Built With

* Flask - A lightweight Python web framework
* Peewee - An open source object-relational mapper (ORM) for the Python 
* Skeleton - Small collection of CSS files
* HTML and CSS


## Issues
Feel free to submit issues and enhancement requests.

## Contributing

In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!


## Authors

**Arpan Rughani** - *Initial work* - [arraypan](https://github.com/arraypan)

See also the list of [contributors](https://github.com/BharatiyaTemple/LibraryCheckin/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Thanks

* Shah Shah - Chairman of Bharatiya Temple Troy Library 
* Bharatiya Temple IT Team


##Screenshot

  SignIn Page
  ![ScreenShot](https://github.com/BharatiyaTemple/LibraryCheckin/blob/master/screenshots/signin.png)
  SignUp Page
  ![ScreenShot](https://github.com/BharatiyaTemple/LibraryCheckin/blob/master/screenshots/signup.png)
  Admin Page
  ![ScreenShot](https://github.com/BharatiyaTemple/LibraryCheckin/blob/master/screenshots/admin.png)



