#!/usr/bin/python3
"""console AirBnb"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter"""

    prompt = "(hbnb) "

    file_path = "file.json"
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl-D (EOF)"""
        return True

    def emptyline(self):
        """Do nothing for an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        all_objs = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        all_objs = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all instances"""
        args = arg.split()
        all_objs = storage.all()

        if not args:
            print([str(obj) for obj in all_objs.values()])
        else:
            class_name = args[0]
            if class_name in self.classes:
                class_objs = [str(obj) for key, obj in all_objs.items(
                ) if key.startswith(class_name + ".")]
                print(class_objs)
            else:
                print("** class doesn't exist **")

    def parse_value(self, value_str):
        """Parse and cast the value to the appropriate type"""
        try:
            value = int(value_str)
        except ValueError:
            try:
                value = float(value_str)
            except ValueError:
                value = value_str.strip('"')
        return value

    def do_update(self, arg):
        """Update an instance attribute"""
        args = shlex.split(arg)
        print(args)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        all_objs = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        value_str = args[3]
        value = self.parse_value(value_str)

        if value is None:
            return

        obj = all_objs[key]
        setattr(obj, attr_name, value)
        obj.save()

    def default(self, args):
        """default"""

        if "." not in args:
            print("*** Unknown syntax: {}".format(args))
            return

        class_method = args.split(".")
        class_name = class_method[0]
        method_name = class_method[1].split("(")[0]

        if class_name not in self.classes:
            print("*** Unknown class: {}".format(class_name))
            return

        if method_name == "count":
            count = 0
            for obj in storage.all().values():
                if class_name == type(obj).__name__:
                    count += 1
            print(count)
            return

        if not hasattr(self, "do_" + method_name):
            print("*** Unknown method: {}.{}".format(class_name, "do_" + method_name))
            return

        method = getattr(self, "do_" + method_name)
        if not callable(method):
            print("*** Unknown method: {}.{}".format(class_name, "do_" + method_name))
            return

        if "(" in args and args.endswith(")"):
            args_of_method = args.split("(")[1][:-1]
            if args_of_method:
                args_of_method = args_of_method.replace(",", " ")
                args_of_method = shlex.split(args_of_method)
                # print(args_of_method)
                method(class_name + " " + " ".join(args_of_method))
            else:
                method(class_name)
        else:
            method(class_name)

    def help_quit(self):
        """help function"""
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
