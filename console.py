#!/usr/bin/python3

import cmd
import sys
from models import storage
from models.base_model import  BaseModel

class HBNBCommand(cmd.Cmd):
    """
    command line shell interepreter
    """

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_EOF(self, line):
        '''
exits the shell
        '''
        return True

    def do_quit(self, line):
        '''
Quit command to exit the program
        '''
        return True

    def do_create(self, line):
        '''
 Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        '''

        if not line:
            print("** class name missing **")
            return
        '''retrieve class name as key'''
        class_objects = storage.Classes()
        if line in class_objects:
            '''retrieve class object'''
            class_obj = class_objects[line]
            '''create instance'''
            obj = class_obj()
            obj.save()
            print(obj.id)
            del obj
        else:
            print("** class doesn't exist **")

        '''if line not in storage.Classes():
            print("** class doesn't exist **")
            return
        obj = storage.Classes()[line]()
        obj.save()
        print(obj.id)'''

    def do_show(self, line):
        '''
Prints the string representation of an instance based on the class name and id
        '''
        if not line:
            print("** class name missing **")
            return
        else:
            lines = line.split(' ')
            class_name = lines[0]
            if class_name not in storage.Classes():
                print("** class doesn't exist **")
                return
            elif len(lines) < 2:
                print("** instance id missing **")
                return
            else:
                id_ = lines[1]
        
                key = "{}.{}".format(class_name, id_)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    obj = storage.all()[key]
                    obj = storage.Classes()[class_name](**obj)
                    print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
            return
        lines = line.split(' ')
        class_name = lines[0]
        id_ = lines[1]
        
        if class_name not in storage.Classes():
            print("** class doesn't exist **")
            return
        if len(lines) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, id_)
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, line):
        '''Prints all string representation of all instances based or
        not class name
        '''
        all_models = []

        if line:
            lines = line.split(' ')
            class_name = lines[0]

            if  class_name not in storage.Classes():
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    if class_name in key:
                        # each matching  model
                        mo = storage.Classes()[class_name](**value)
                        all_models.append(str(mo))
        else:
            for key, value in storage.all().items():
                class_name = key.split('.')[0]
                all_models.append(str(storage.Classes()[class_name](**value)))
        print(all_models)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
