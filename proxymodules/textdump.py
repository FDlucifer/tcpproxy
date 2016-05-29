#!/usr/bin/env python2


class Module:
    def __init__(self, incoming=False):
        self.name = 'Text display'
        self.description = 'Simply print the received data as text'
        self.incoming = incoming  # incoming means module is on -im chain

    def execute(self, data):
        print data
        return data

if __name__ == '__main__':
    print 'This module is not supposed to be executed alone!'
