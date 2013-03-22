#!/usr/bin/python

# from artnet import dmx
from dmx import *


def main(config, controller=None):
	q = controller or dmx.Controller(config.get('base', 'address'), nodaemon=False)
	q.add(iter([[0] * 512]))
	if not controller:
		q.start()
