from mininet.topo import Topo

class BinaryTree(Topo):
    "Binary tree topology with a depth of 3."

    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Create hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')

        # Create switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')

        # Add links between hosts and switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(h7, s4)
        self.addLink(h8, s4)

        # Add links between switches
        self.addLink(s1, s5)
        self.addLink(s2, s5)
        self.addLink(s3, s6)
        self.addLink(s4, s6)
        self.addLink(s5, s7)
        self.addLink(s6, s7)

topos = {'binarytree': BinaryTree}
