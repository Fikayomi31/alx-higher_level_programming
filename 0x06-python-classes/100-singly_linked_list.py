#!/usr/bin/python3

"""Defining a class"""


class Node:
    """A class that represent a Node"""

    def __init__(self, data, next_node=None):
        """Initializing this Node class
        Args:
            data: the data in the linked list
            next_node: link to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieve node data """
        return self.__data

    @data.setter
    def data(self, value):
        """setting a node data
        Raise:
            TypeError: if the data is not integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setting a next node to value
        Raise:
            TypeError: if next_node is not node object
        """
        if value != None:
            raise TypeError("next_node must be a Node objectt")
        self.__next_node = value



class SinglyLinkedList:
    """Representing a singly linked list"""

    def __init__(self):
        """Initializing the class singly linked list"""
        self.__head = None

    def __str__(self):
        """Representation of string in singly linked list"""

        string = ""
        start = self.__head
        while start:
            if start is not self.__head:
                string += '\n'
            string += str(start.data)
            start = start.next_node
        return string

    def sorted_insert(self, value):
        """inserting new node into sorted position of the list"""
        new_node = Node(value)

        if not self.__head:
            self.__head = new_node
            return
        if value < self.__head_data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        node = self.__head

        while node.next_node and node.next.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
