#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
import optparse, os
import re
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from random import randrange

class Skeleton():

    def __init__(self):
        self.options, self.traffic_file = self.parse_args()

    def parse_args(self):
        usage = """usage: %prog [options] trafficfile

    This is a fake aprs client. It will read in a file
    containing APRS messages, prepend a current time stamp
    and loop over it continuously, injecting traffic into
    an tcp aprs system.

      python fakeaprsclient.py <path/to/traffic.txt>

    If no file is specificied, it will default to
    data/sampletraffic.txt.
    """

        parser = optparse.OptionParser(usage)

        help = "The port to connect to. Default to port 1025."
        parser.add_option('--port', type='int', help=help, default=1025)

        help = "The interface to connect to. Default is localhost."
        parser.add_option('--iface', help=help, default='localhost')

        help = "The number of seconds between sending lines. Default to 1.2 seconds"
        parser.add_option('--delay', type='float', help=help, default=1.2)

        help = "Strip timestamps (experimental). Will remove @.*z timestamps from messages, off by default."
        parser.add_option('--strip', action="store_true", help=help, dest="strip", default=True)

        options, args = parser.parse_args()

        if len(args) != 1:
            traffic_file = 'data/sampletraffic.txt'
        else:
            traffic_file = args[0]

        if not os.path.exists(traffic_file):
            parser.error('No such file: %s' % traffic_file)

        self.options = options
        self.traffic_file = traffic_file

        return options, traffic_file

    def readfile(self, filename):

        try:
            ref = open(filename)
        except (OSError, IOError) as e:
            print e
            exit(1)

        data = ref.readlines()
        ref.close()
        return data

    def main(self):

        factory = APRSClientFactory()
        reactor.connectTCP(self.options.iface, self.options.port, factory)
        reactor.run()

class APRSPush(LineReceiver):

    # options, traffic_file = parse_args()

    stop = "/stop"
    start = "/start"

    s = Skeleton()
    messages = s.readfile('data/sampletraffic.txt')
    delay = s.options.delay
    strip = s.options.strip

    def sendmessage(self):

        top = len(self.messages)
        message = self.messages[randrange(0,top)]
        message.strip()

        if self.strip:
            message = re.sub(':@.*z',':@', message)

        self.sendLine(message)

    def connectionMade(self):
        self.lc = LoopingCall(self.sendmessage)
        self.lc.start(self.delay)

    def lineReceived(self, line):
        print "receive:", line
        if line == self.stop:
            if self.lc.running:
                self.sendLine("received stop command")
                self.lc.stop()
            else:
                self.sendLine("not running!")

        if line == self.start:
            if self.lc.running:
                self.sendLine("already running, try /stop")
            else:
                self.sendLine("starting messages")
                self.lc.start(self.delay)

class APRSClientFactory(ClientFactory):

    protocol = APRSPush

    def clientConnectionFailed(self, connector, reason):
        print 'connection failed:', reason.getErrorMessage()
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print 'connection lost:', reason.getErrorMessage()
        reactor.stop()


if __name__ == '__main__':
    m = Skeleton()
    m.main()

