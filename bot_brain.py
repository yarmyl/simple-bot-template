#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Brain:

    """Manual"""
    HELP = [
        '/start - Enjoy\n',
        '/help - This message\n'
    ]
    
    """Brain init"""
    def __init__(self, conf):
        if conf:
            pass

    """Argument Parser"""
    def parseArgs(self, text):
        arr = text.split(' ')
        args = arr[1:]
        ret = []
        for arg in args:
            if arg:
                ret.append(arg)
        return (ret, arr[0])

    """Bot Brain"""
    def botBrain(self, text):
        if text[0] == "/":
            args, cmd = self.parseArgs(text)
        else:
            return (None, None)
        if cmd == "/help":
            return (''.join(self.HELP), None)
        elif cmd == "/start":
            return ("Please, use /help", None)
        else:
            if args:
                if args[0] in ["Yes", "No"]:
                    return ("OK!", None)
                else:
                    return ("Wrong request!", None)
            else:
                return ("Unknown command, Are u sure", [["Yes", "No"]])
#        else:
#            return (None, None)
