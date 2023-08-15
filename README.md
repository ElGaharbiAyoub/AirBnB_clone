# AirBnB Clone - The Console

## Description

Project 0x00 - AirBnB clone - The console
The first step in the full web application: the AirBnB clone.
Starting with the two major complonents the data models and the storage engine.

## Unit Tests

All unit tests are found in the tests directory

## How to start

Starting the console, which is a command interpreter, you run the executable script "console.py" from the root directory of this repository.

Commands are seperated by line breaks.

## How to use it

There are various commands for the interpreter which you would input when prompted.

### Create

Creates a new instance of the given class and saves it.

- `create <class name>`

This command prints the ID of the new object, which is a random UUID, which can be used for other commands

```
(hbnb) create BaseModel
c462b36d-98d2-47cd-adab-5a3781ad0283
(hbnb) create User
2bf63de4-0d4f-4332-b8c3-6453db9e9f02
```

### Show

Prints a description of the specified object.

- `show <class name> <id>`
- or `<class name>.show(<id>)`

```
(hbnb) show BaseModel c462b36d-98d2-47cd-adab-5a3781ad0283
[BaseModel] (c462b36d-98d2-47cd-adab-5a3781ad0283) {'id': 'c462b36d-98d2-47cd-adab-5a3781ad0283', 'created_at': datetime.datetime(2023, 8, 14, 19, 13, 52, 189079), 'updated_at': datetime.datetime(2023, 8, 14, 19, 13, 52, 189100)}
```

### Destroy

Destroys a specific object

- `destroy <class name> <id>`
- or `<class name>.destroy(<id>)`

```
(hbnb) destroy BaseModel c462b36d-98d2-47cd-adab-5a3781ad0283
```

### All

Prints all objects in storage, or all objects in storage of particular class.

- `all`
- or `all <class name>`
- or `<class name>.all()`

Output looks like a Python list of strings (["object1", "object2" ...])

```
(hbnb) all
["[BaseModel] (66fa06f6-c4a5-4aa4-9f24-22eaec0ccc48) {'id': '66fa06f6-c4a5-4aa4-9f24-22eaec0ccc48', 'created_at': datetime.datetime(2023, 8, 14, 19, 44, 11, 866473), 'updated_at': datetime.datetime(2023, 8, 14, 19, 44, 11, 866501)}", "[User] (5aa09e85-66dc-4d67-a340-ce2b7eab3d9d) {'id': '5aa09e85-66dc-4d67-a340-ce2b7eab3d9d', 'created_at': datetime.datetime(2023, 8, 14, 22, 29, 40, 26275), 'updated_at': datetime.datetime(2023, 8, 14, 22, 29, 40, 26290), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}"]
```

- show all users

```
(hbnb) all User
["[User] (5aa09e85-66dc-4d67-a340-ce2b7eab3d9d) {'id': '5aa09e85-66dc-4d67-a340-ce2b7eab3d9d', 'created_at': datetime.datetime(2023, 8, 14, 22, 29, 40, 26275), 'updated_at': datetime.datetime(2023, 8, 14, 22, 29, 40, 26290), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}"]
```

### Update

Updates one or more attributes on the specified object.

- `update <class name> <id> <attribute name> "<attribute value>"`
- or `<class name>.update(<id>, <attribute name> "<attribute value>")`

```
(hbnb) update User 5aa09e85-66dc-4d67-a340-ce2b7eab3d9d first_name "ayoub"
(hbnb) all User
["[User] (5aa09e85-66dc-4d67-a340-ce2b7eab3d9d) {'id': '5aa09e85-66dc-4d67-a340-ce2b7eab3d9d', 'created_at': datetime.datetime(2023, 8, 14, 22, 29, 40, 26275), 'updated_at': datetime.datetime(2023, 8, 15, 0, 6, 3, 523483), 'first_name': 'ayoub', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}"]
```
