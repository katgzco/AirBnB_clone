# AirBnB_Clone The Console

![image1](hbnb.png)
This project you find the fisrt step for you create a command interpreter to manage your AirBnB

## **Modules**

<table>
<thead>
<tr>
  <th>#</th>
  <th>Directory</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td>1</td>
  <td> README.md</td>
  <td>...<td>
</tr>
<tr>
  <td>2</td>
  <td>console.py</td>
  <td> In this file you find all commands of the console.
  <td>
</tr>
<tr>
  <td>3</td>
  <td>models

    models/
    ├── __init__.py
    ├── amenity.py
    ├── base_model.py
    ├── city.py
    ├── engine
    │   ├── __init__.py
    │   └── file_storage.py
    ├── main.py
    ├── place.py
    ├── review.py
    ├── state.py
    └── user.py

1 directory, 11 files</td>

  <td>This is a directory that contein all the class

  <table>
  <thead>
  <tr>
    <th>#</th>
    <th>File</th>
    <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>1</td>
    <td>__init__.py</td>
    <td>You find the unique instance of FileStorage
    <td>
  </tr>
  <tr>
    <td>2</td>
    <td>base_model.py</td>
    <td>You find the body of the patern Class with the public instace atributtes and methods of the class
    <td>
  </tr>
  <tr>
    <td>3</td>
    <td>amenity.py</td>
    <td>class amenity that inherits of the Base_model class<td>
  </tr>
  <tr>
    <td>4</td>
    <td>city.py</td>
    <td>class city that inherits of the Base_model class<td>
  </tr>
  <tr>
    <td>5</td>
    <td>place.py</td>
    <td>class place that inherits of the Base_model class<td>
  </tr>
  <tr>
    <td>6</td>
    <td>review.py</td>
    <td>class review that inherits of the Base_model class<td>
  </tr>
  <tr>
    <td>7</td>
    <td>state.py</td>
    <td>class state that inherits of the Base_model class<td>
  </tr>
  <tr>
    <td>8</td>
    <td>user.py</td>
    <td>class user that inherits of the Base_model class<td>
  </tr>
  </tr>
  </tbody>
  </table>

  </td>
</tr>
<tr>
  <td>3.1</td>
  <td>engine</td>
  <td>In this directory you will find the file FileStorage.py and the __init__.py necesary for the package</td>
</tr>
<tr>
  <td>4</td>
  <td>tests
  ├── __init__.py
  └── test_models
    ├── __init__.py
    ├── test_amenity.py
    ├── test_base_model.py
    ├── test_city.py
    ├── test_engine
    │   ├── __init__.py
    │   └── test_file_storage.py
    ├── test_place.py
    ├── test_review.py
    ├── test_state.py
    └── test_user.py
  </td>
  <td>In this directory you will find the unittest for each file on models directory</td>
</tr>
<tr>
  <td>5</td>
  <td>AUTHORS
  <td>You will find the name and the email of the contributors
  </td>
</tr>
<tr>
</tbody>
</table>

# Description of the project

For you get an interactive console. It is necessary to have the following steps in mind:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## **Description of the command interpreter**

On the console you have the posibility to manage the objects of our project

> The prompt looks like this:
>
> > `(hbnb)`

## How to start it and How to use it:

You can start in two Modes:

### Interactiva Mode:

you need execute the file console.py, and then you can use the command help and you know the commands.

`$ ./console.py`

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  counter  create  destroy  help  manage  quit  show  update

(hbnb) help all
Prints all string representation of all
instances based or not on the class name

(hbnb) help create
Creates a new instance of the class

(hbnb) help destroy
Deletes an instance based on the class name and id

(hbnb) help counter
 Counter of class

(hbnb) help show
Prints the string representation of an instance
based on the class name

(hbnb) help update
Updates an instance based on the class name and
id by adding or updating attribute

(hbnb) help quit
Quit command to exit the program
```

========== NOW WE ARE USE THE COMMANDS ===========

So if you want to creat new intance like User, Place, Review, State

Sintax: _command_ _className_

```
(hbnb) create User
f7f699fa-0ef1-4cf0-8a7c-64365c681098
```

Prints all string representation of all instances based or not on the class name there are two way:

Sintax: _command_ _className_ or
_className_._command_()

```
(hbnb) all User
["[User] (f7f699fa-0ef1-4cf0-8a7c-64365c681098) {'id': 'f7f699fa-0ef1-4cf0-8a7c-64365c681098', 'created_at': datetime.datetime(2021, 2, 22, 10, 7, 25, 432978), 'updated_at': datetime.datetime(2021, 2, 22, 10, 7, 25, 432992)}", "[User] (18e264e0-b528-42ad-b325-79372d85d795) {'id': '18e264e0-b528-42ad-b325-79372d85d795', 'created_at': datetime.datetime(2021, 2, 22, 10, 16, 52, 234498), 'updated_at': datetime.datetime(2021, 2, 22, 10, 16, 52, 234509)}"]
```

Prints the string representation of an instance based on the class name. with command _show_

sintax: _className_._show_("_id_") or _show_ _className_ _id_

```
(hbnb) User.show("f7f699fa-0ef1-4cf0-8a7c-64365c681098")
[User] (f7f699fa-0ef1-4cf0-8a7c-64365c681098) {'id': 'f7f699fa-0ef1-4cf0-8a7c-64365c681098', 'created_at': datetime.datetime(2021, 2, 22, 10, 7, 25, 432978), 'updated_at': datetime.datetime(2021, 2, 22, 10, 7, 25, 432992)}
```

You can know the number of the objects using command _counter_

Sintax: _counter_ _className_

```
(hbnb) counter User
2
```

### None interactive Mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

##

## BY:

- _Giraluna Gomez_ <lunagolo@hotmail.com> @Giraluna1
- _Katherin Gomez_ <katzco@gmail.com> @katgzco
