# ng-students
Minimal implementation of a "Students management system" using Python 3, Django 1.7, Django-rest-framework and AngularJS.

### Installation

```bash
$ mkvirtualenv ng-students -p $(which python3)
$ pip install -r requirements/base.txt
$ echo "export DJANGO_SETTINGS_MODULE=students_management.settings" >> ${HOME}/.virtualenvs/ng-students/bin/postactivate
$ echo "unset DJANGO_SETTINGS_MODULE" >> ${HOME}/.virtualenvs/ng-students/bin/postdeactivate
$ add2virtualenv ./students_management
$ npm install && bower install
```

### Usage

The fronted is decoupled from the backend, that's why you will need to run their servers separately:

```bash
$ django-admin.py runserver &  # You can use a different terminal if you want
$ grunt serve
```

### Tests

To test the backend:

```bash
$ django-admin.py test students  # test the whole students app
$ django-admin.py test students.test_models.TestStudentModel.test_student_full_name_property  # individual tests
$ django-admin.py test api  # test the API app
```

### Preview

![screenshot](http://i.imgur.com/HA18smP.png)
