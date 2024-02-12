#!/usr/bin/python3
"""hbnb console"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """disolay interactive mode
    Attributes:
        prompt: string
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emotyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
