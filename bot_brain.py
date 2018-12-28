#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import os
#from subprocess import Popen, PIPE


class Brain:

    """Manual"""
    HELP = [
        '/start - Enjoy\n',
        '/help - This message\n'
    ]

    """Argument Parser"""
    def parseArgs(self, text):
        args = text.split(' ')[1:]
        ret = []
        for arg in args:
            if arg:
                ret.append(arg)
        return ret

    """Bot Brain"""
    def botBrain(self, text):
        if text == "/help":
            return (''.join(self.HELP), None)
        elif text == "/start":
            return ("Please, use /help", None)
        elif text[:1] == "/":
            args = self.parseArgs(text)
            if args:
                if args[0] in ["Yes", "No"]:
                    return ("OK!", None)
                else:
                    return ("Wrong request!", None)
            else:
                return ("Unknown command, Are u sure", [["Yes", "No"]])
        else:
            return (None, None)
