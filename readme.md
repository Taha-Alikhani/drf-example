
# Python DjangoRestFramework Example

A very simple drf project with a course, student and professor model to make my github look a little bit greener overnight

## Installation

Using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install -r requirements.txt
```

_you can (and should) run this command and the code in a virtual environment_

## Running the app
I haven't written the dockerfile example yet, so for now:

```bash
python3 manage.py runserver
```

## Usage

Use django admin panel to create courses and add professors, you can then send a request to
`localhost:8000/students/enroll/<student_slug>/<class_slug>` to enroll the student in that course untill the course is full

## TODO
- [x] Write this readme file.
- [ ] Write templates.
- [ ] Implement authentication
- [ ] Write tests.
- [ ] Dockerize the app.

## License

[MIT](https://choosealicense.com/licenses/mit/)
