import ete3
from ete3 import NCBITaxa
ncbi = NCBITaxa()
import sys

class NCBI2NewickPlugin:
    def input(self, filename):
       infile = open(filename, 'r')
       self.ids=[]
       for line in infile:
           self.ids.append(int(line.strip()))


    def run(self):
       self.tree = ncbi.get_topology(self.ids)
       #self.tree.set_outgroup(self.tree.get_midpoint_outgroup())
       self.tree.resolve_polytomy()
       count = 10000000;
       #for node in self.tree.traverse(strategy="levelorder"):
           #if (len(node.get_children()) > 2):
           #print(len(node.get_children()))
           #   node.set_outgroup(node.get_children()[1])
       #    if (len(node.get_children()) == 1):
       #        node.add_child(name=str(count), dist=0)
       #        count += 1
       #self.tree.set_outgroup(self.tree&"239935")
       print(self.tree)
       print(self.tree.write(format=1))
       #print(self.tree)

    def output(self, filename):
       self.tree.write(format=1, outfile=filename)

