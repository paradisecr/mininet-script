#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def createTopo():

    net = Mininet(build= False, controller=RemoteController);

    c0 = net.addController('c0', ip="127.0.0.1", port=6633)

    s1 = net.addSwitch('s1');
    s2 = net.addSwitch('s2');

    h1 = net.addHost('h1', ip='192.168.0.1/24')
    h2 = net.addHost('h2', ip='192.168.0.2/24')
    net.addLink(s1, h1)
    net.addLink(s2, h2)
    net.addLink(s1, s2)
    net.addLink(s1, s2)


    net.start()

    CLI(net)

    net.stop()


if __name__=='__main__':
    setLogLevel('debug')
    createTopo()