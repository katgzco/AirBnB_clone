#!/usr/bin/python3
from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
import shlex


class HBNBCommand(Cmd):

    __dict_class = {"BaseModel": BaseModel, "User": User,
                    "City": City, "State": State, "Place": Place,
                    "Amenity": Amenity, "Review": Review}

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ to exit the program"""
        return True

    def do_quit(self, line):
        """ to exit the program """
        return True

    def do_emptyline(self, line):
        """ an empty line + ENTER shouldn’t execute anything """
        pass

    def do_create(self, line):
        """ Creates a new instance of the class """
        line_tokenized = HBNBCommand.do_manage(line)
        if line_tokenized:
            if not line_tokenized[0] in HBNBCommand.__dict_class:
                print("** class doesn't exist **")
                return

                instance = HBNBCommand.__dict_class[line_tokenized[0]]()
                storage.save()
                print(instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name
        """
        line_tokenized = HBNBCommand.do_manage(line)

        if line_tokenized:
            if not line_tokenized[0] in HBNBCommand.__dict_class:
                print("** class doesn't exist **")
                return

            if len(line_tokenized) >= 2 and line_tokenized[1]:
                key = line_tokenized[0]+"."+line_tokenized[1]
                dictionary = storage.all()
                try:
                    print(dictionary[key])
                except BaseException:
                    print("** no instance found **")
                    return
            else:
                print("** instance id missing **")
                return
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        line_tokenized = HBNBCommand.do_manage(line)

        if line_tokenized:
            if not line_tokenized[0] in HBNBCommand.__dict_class:
                print("** class doesn't exist **")
                return

            if len(line_tokenized) >= 2 and line_tokenized[1]:
                key = line_tokenized[0]+"."+line_tokenized[1]
                dictionary = storage.all()
                try:
                    del(dictionary[key])
                    storage.save()
                except BaseException:
                    print("** no instance found **")
                    return
            else:
                print("** instance id missing **")
                return
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        line_tokenized = HBNBCommand.do_manage(line)
        if line_tokenized:
            if not line_tokenized[0] in HBNBCommand.__dict_class:
                print("** class doesn't exist **")
                return

        dictionary = storage.all()
        list_objects = []
        for key, value in dictionary.items():
            if len(line_tokenized) >= 1:
                token = key
                token = str(token).split(".")
                if token[0] == line_tokenized[0]:
                    list_objects.append(str(dictionary[key]))
            else:
                list_objects.append(str(dictionary[key]))
        print(list_objects)

    def do_update(self, line):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        line_tokenized = HBNBCommand.do_manage(line)

        if line:
            if not line_tokenized[0] in HBNBCommand.__dict_class:
                print("** class doesn't exist **")
                return

            if len(line_tokenized) >= 2 and line_tokenized[1]:
                key = line_tokenized[0]+"."+line_tokenized[1]
                dictionary = storage.all()
                try:
                    dictionary[key]
                except BaseException:
                    print("** no instance found **")
                    return
            else:
                print("** instance id missing **")
                return

            if not len(line_tokenized) >= 3:
                print("** attribute name missing **")
                return

            if not len(line_tokenized) >= 4:
                print("** value missing **")
                return

            instance = dictionary[key].__dict__
            line_tokenized[3] = str(line_tokenized[3])
            instance[line_tokenized[2]] = line_tokenized[3]
        else:
            print("** class name missing **")

    def manage(line):
        """ splits the line arguments splits and return an array """
        tokens = shlex.split(line)
        return list(tokens)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
