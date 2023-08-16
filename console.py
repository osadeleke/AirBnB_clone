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
from models.place import Place
from models.city import City
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Provides methods for handling commands in the program CLI
    """
    prompt = "(hbnb) "

    CLASSES = [
            "BaseModel", "User", "State",
            "Amenity", "Place", "City", "Review"
            ]

    def do_create(self, line):
        """
        Creates a new instance of an object

        Usage create <object>
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
            elif args[0] == "Place":
                base = Place()
            elif args[0] == "City":
                base = City()
            elif args[0] == "Review":
                base = Review()
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
            args[1] = args[1].replace('"', '') \
                    if args[1][0] == '"' else args[1]
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
        args = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            args[1] = args[1].replace('"', '') \
                    if args[1][0] == '"' else args[1]
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
        args = line.split(" ")
        if args[0] != "":
            if args[0] not in HBNBCommand.CLASSES:
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
        args = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            args[1] = args[1].replace('"', '') \
                    if args[1][0] == '"' else args[1]
            classname_id = args[0] + "." + args[1]
            if classname_id not in objs.keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                args[2] = args[2].replace('"', '').replace("'", "")
                obj = objs[classname_id]
                if args[3].startswith('"') and args[3].endswith('"') or \
                        args[3].startswith("'") and args[3].endswith("'"):
                    setattr(obj, args[2], str(args[3][1:-1]))
                elif args[3].startswith('"') and not args[3].endswith('"') or \
                        args[3].startswith("'") and not args[3].endswith("'"):
                    str_value = ""
                    for arg in args[3:]:
                        str_value += " " + arg
                        if arg.endswith('"') or arg.endswith("'"):
                            break
                    setattr(obj, args[2], str(str_value[2:-1]))
                elif "." in args[3]:
                    setattr(obj, args[2], float(args[3]))
                else:
                    setattr(obj, args[2], int(args[3]))
                storage.save()

    def do_count(self, line):
        """
        Count the number of objects
        """
        objs = storage.all()
        args = line.split(" ")
        obj_names = list(map(lambda obj: type(obj).__name__, objs.values()))
        print("{}".format(obj_names.count(line)))

    def update_dict(self, command, line):
        attr = line.split("{")[1][0:-2].replace(":", "").split(", ")
        for item in attr:
            comm = command + " " + item
            self.onecmd(comm)

    def default(self, line):
        """
        Handle other commands like:
            <class name>.all()
            <class name>.count()
        """
        METHODS = ["all", "count", "show", "destroy", "update"]

        if "." in line:
            command = line[:-1].replace(",", "")\
                    .replace("(", " ").replace(".", " ").split(" ")
            command[0], command[1] = command[1], command[0]
            if command[1] in HBNBCommand.CLASSES and command[0] in METHODS:
                if command[0] == "update" and "{" in line:
                    self.update_dict(" ".join(command[:3]), line)
                    return None
                self.onecmd(" ".join(command))
                return None
        return cmd.Cmd.default(self, line)

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
