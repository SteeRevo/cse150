#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
class MyTopology(Topo):
  """
  A basic topology
  """
  def __init__(self):
    Topo.__init__(self)
    # Set Up Topology Here
    switch1 = self.addSwitch('s1') ## Adds a Switch
    switch2 = self.addSwitch('s2')
    switch3 = self.addSwitch('s3')
    user1 = self.addHost('User 1') ## Adds a Host
    user2 = self.addHost('User 2') ## Adds a Host
    laptop = self.addHost("Laptop")
    self.addLink(user1, switch1) ## Add a link
    self.addLink(user2, switch1) ## Add a link
    self.addLink(laptop, switch1)
    self.addLink(switch1, switch2)

if __name__ == '__main__':
  """
  If this script is run as an executable (by chmod +x), this is
  what it will do
  """
  topo = MyTopology() ## Creates the topology
  net = Mininet( topo=topo ) ## Loads the topology
  net.start() ## Starts Mininet
  # Commands here will run on the simulated topology
  CLI(net)
  net.stop() ## Stops Mininet
