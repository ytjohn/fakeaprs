# FakeAPRS

This is a fake APRS daemon designed to emulate traffic you might receive on a tcp serial
port. It comprises of a server and a traffic injection client.

The purpose of this to facilitate building real APRS clients and giving them a traffic
stream to test against.

## Requirements

You need the python library [twisted](http://www.twistedmatrix.com/).

 * On a Debian system: `sudo apt-get install python-twisted`
 * On a system with pip: `sudo pip install -r requirements.txt`

## Quick Start

1. Start the server: `python fakeaprsserver.py`
2. Start the client: `python fakeaprsclient.py data/sampletraffic.txt`

## Server

`fakeaprsserver.py` will open a tcp port that clients can connect to. Any text sent by
these clients will be relayed to any other client connected. 


    Usage: fakeaprsserver.py [options]
    
    This is a basic "pub/usb" server taken right from
    http://www.twistedmatrix.com and some arguments added
    on.
    
      python fakeaprsserver.py
    
    Any client (even telnet) that connects to this will be able
    to send lines of text to each other.
    
    
    Options:
      -h, --help     show this help message and exit
      --port=PORT    The port to listen on. Defaults to port 1025.
      --iface=IFACE  The interface to listen to. Default is localhost.



## Client

`fakeaprsclient.py` reads in a text file containing traffic (one has been provided in 
`data/sampletraffic.txt`) and pushes that traffic to the defined tcp port, prepending it
with a current timestamp.

If no file is given, it will default to data/sampletraffic.txt

    Usage: fakeaprsclient.py [options] trafficfile
    
        This is a fake aprs client. It will read in a file
        containing APRS messages, prepend a current time stamp
        and loop over it continuously, injecting traffic into
        an tcp aprs system.
    
          python fakeaprsclient.py <path/to/traffic.txt>
    
        If no file is specificied, it will default to
        data/sampletraffic.txt.
        
    
    Options:
      -h, --help     show this help message and exit
      --port=PORT    The port to connect to. Default to port 1025.
      --iface=IFACE  The interface to connect to. Default is localhost.
      --delay=DELAY  The number of seconds between sending lines. Default to 1.2
                     seconds
      --strip        Strip timestamps (experimental). Will remove @.*z timestamps
                     from messages, off by default.


## Vagrant

We use [vagrant](http://www.vagrantup.com/) to test this system. Assuming you have Vagrant
and a provider such as [VirtualBox](http://www.virtualbox.org/) installed, you can spin
up a virtual machine and run these programs inside it.

To start the virtual machine:  `vagrant up`

To ssh into the running virtual machine (linux): `vagrant ssh`

If you are using an application like putty and want to know how to ssh in, use 
`vagrant ssh-config` to get the parameters to enter into your client.

Once inside the virtual machine, all of these files are located in `/vagrant`

To halt the VM, type `vagrant halt` (from outside the VM).

To destroy the VM, type `vagrant destroy` (from outside the VM).


