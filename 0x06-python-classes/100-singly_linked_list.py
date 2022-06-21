#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    def __str__(self):
        return str(self.__data)

    @property
    def data(self):
        return (self.__data)

    @property
    def next_node(self):
        return (self.__next_node)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        temp = self.__head
        if temp is None or temp.data >= value:
            if temp:
                new.next_node = temp
            self.__head = new
            return
        while temp.next_node is not None:
            if temp.next_node.data >= value:
                break
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new

    def __str__(self):
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp)
            if temp.next_node is not None:
                string += "\n"
            temp = temp.next_node
        return (string)
