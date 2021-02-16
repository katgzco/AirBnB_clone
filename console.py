#!/usr/bin/python3
from cmd import Cmd
from models import storage
from models.base_model import BaseModel
import shlex


class HBNBCommand(Cmd):

    __dict_class = {"BaseModel":BaseModel}   

    prompt = "(hbnb) "
    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def do_create(self, line):
        line_tokenized = HBNBCommand.do_manage(line)
        if line:
            try:
                HBNBCommand.__dict_class[line]
                instance = HBNBCommand.__dict_class[line]()
                print(instance.id)
                storage.save()
            except BaseException:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


    def do_show(self, line):
        line_tokenized = HBNBCommand.do_manage(line)

        if line_tokenized:
            try:
                HBNBCommand.__dict_class[line_tokenized[0]]
            except BaseException:
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

    def do_manage(line):
        tokens = shlex.split(line)
        return (list(tokens))


if __name__ == '__main__':
   HBNBCommand().cmdloop()