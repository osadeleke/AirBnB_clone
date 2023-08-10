#!/usr/bin/python3
"""
This module provides a command line interface for the program
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Provides methods for handling commands in the program CLI
    """
    prompt = "(hbnb) "

    CLASSES = ["BaseModel", "User", "State", "Amenity"]

    def do_create(self, line):
        """
        Creates a new instance of an object

        Usage: create <object>
        """
        args = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        else:
            if args[0] == "BaseModel":
                base = BaseModel()
            elif args[0] == "User":
                base = User()
            elif args[0] == "State":
                base = State()
            elif args[0] == "Amenity":
                base = Amenity()
            print(base.id)
            storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance

        Usage: show <object> <id>
        """
        objs = storage.all()
        args = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            classname_id = args[0] + "." + args[1]
            if classname_id not in objs.keys():
                print("** no instance found **")
            else:
                print(objs[classname_id])

    def do_destroy(self, line):
        """
        Deletes an instance

        Usage: destroy <object> <id>
        """
        objs = storage.all()
        objs_list = []
        for key in objs.keys():
            if (key.split(".")[0] not in objs_list):
                objs_list.append(key.split(".")[0])
        args = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif args[0] not in objs_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            classname_id = args[0] + "." + args[1]
            if classname_id not in objs.keys():
                print("** no instance found **")
            else:
                del objs[classname_id]
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances

        Usage: all <object> | all
        """
        objs = storage.all()
        objs_list = []
        for key in objs.keys():
            if (key.split(".")[0] not in objs_list):
                objs_list.append(key.split(".")[0])
        args = line.split(" ")
        if args[0] != "":
            if args[0] not in objs_list:
                print("** class doesn't exist **")
            else:
                all_list = []
                for obj in objs:
                    if obj.startswith(args[0]):
                        all_list.append(str(objs[obj]))
                print(all_list)
        else:
            all_list = []
            for obj in objs:
                all_list.append(str(objs[obj]))
            print(all_list)

    def do_update(self, line):
        """
        Updates an instance by adding or updating attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        objs = storage.all()
        objs_list = []
        for key in objs.keys():
            if (key.split(".")[0] not in objs_list):
                objs_list.append(key.split(".")[0])
        args = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif args[0] not in objs_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            classname_id = args[0] + "." + args[1]
            if classname_id not in objs.keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = objs[classname_id]
                if args[3].startswith('"') and args[3].endswith('"'):
                    setattr(obj, args[2], str(args[3][1:-1]))
                elif args[3].startswith('"') and not args[3].endswith('"'):
                    str_value = ""
                    for arg in args[3:]:
                        str_value += " " + arg
                        if arg.endswith('"'):
                            break
                    print(str_value)
                    setattr(obj, args[2], str(str_value[2:-1]))
                elif "." in args[3]:
                    setattr(obj, args[2], float(args[3]))
                else:
                    setattr(obj, args[2], int(args[3]))
                storage.save()

    def do_EOF(self, line):
        """
        Ends the command line interpreter

        Usage: CTRL+D
        """
        return True

    def do_quit(self, line):
        """
        Ends the command line interpreter

        Usage: quit
        """
        return True

    def emptyline(self):
        """
        Ignore empty lines (ENTER)
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
