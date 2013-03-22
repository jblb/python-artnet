#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# test1_ambilight_sender.py
#
# Copyright © 2013 Mathieu Gaborit (matael) <mathieu@matael.org>
#
#
# Distributed under WTFPL terms
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

"""
Simple Ambilight Sender
"""

from artnet import dmx
import threading

class Sender(threading.Thread):
    """ Simple class that read colors from a Queue and
    output them through DMX over ArtNet
    """


    def __init__(self, color_queue, controller=None, address=None):

        if not controller and not address:
            raise ValueError('You should specify at least a controller or address')

        self.controller = controller or dmx.Controller(address, nodaemon=False)
        if not controller:
            self.controller.start()
        self.queue = color_queue

    def run(self):
        while 1:
            color = self.queue.get()

            for i in xrange(len(color)):
                self.controller.add(color[i])

            self.queue.task_done()


