#!/usr/bin/env python

"""
This will run a tcp pub/sub server on port 1025
"""

import optparse, os, socket, time

from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic

class PubProtocol(basic.LineReceiver):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.clients.add(self)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        for c in self.factory.clients:
            c.sendLine(line.strip())

class PubFactory(protocol.Factory):
    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        return PubProtocol(self)

def parse_args():
    usage = """usage: %prog [options]

This is a basic "pub/usb" server taken right from
http://www.twistedmatrix.com and some arguments added
on.

  python fakeaprsserver.py

Any client (even telnet) that connects to this will be able
to send lines of text to each other.
"""

    parser = optparse.OptionParser(usage)

    help = "The port to listen on. Defaults to port 1025."
    parser.add_option('--port', type='int', help=help, default=1025)

    help = "The interface to listen to. Default is localhost."
    parser.add_option('--iface', help=help, default='localhost')

    options, args = parser.parse_args()

    return options


def main():

    options = parse_args()
    point = "tcp:{0}:interface={1}".format(options.port, options.iface)
    endpoints.serverFromString(reactor, point).listen(PubFactory())
    reactor.run()

if __name__ == '__main__':
    main()
