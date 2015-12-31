from itertools import chain

class tree(object):
    def __init__(self, name, children = [], parent = None):
        self.name = name
        self.children = children
        self.parent = parent
            
    def setChildren(self, children):
        self.children = children
    
    def setParent(self, parent):
        self.parent = parent
    
    def getName(self):
        return self.name
        
    def getParent(self):
        return self.parent
        
    def getChildren(self):
        return self.children  
          
    def __str__(self, level=0):
        ret = "\t"*level+str(self.name)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
        
                        
def depthFirst(tree, name):
    """Finds the node - name in the tree.
    returns name if name is in the tree
    else, returns None
    tree: a tree object
    """
    queue = [tree]
    while len(queue) > 0:
        print "Now Searching: ", queue[0].getName()
        if queue[0].getName() == name:
            return queue[0]
        else:
            temp = queue.pop(0)
            if len(temp.getChildren()) > 0:
                children = temp.getChildren()[::-1]
                for child in children:
                    queue.insert(0, child)
                    
def breadthFirst(tree, name):
    """Finds the node - name in the tree.
    returns name if name is in the tree
    else, returns None
    tree: a tree object
    """
    queue = [tree]
    while len(queue) > 0:
        print "Now Searching: ", queue[0].getName()
        if queue[0].getName() == name:
            return queue[0]
        else:
            temp = queue.pop(0)
            if len(temp.getChildren()) > 0:
                for child in temp.getChildren():
                    queue.append(child)
    

def depthFirstR(tree,name):
    queue = [tree]
    result = None
    for item in queue:
        print "Now Searching: ", item.getName()
        if item.getName() == name:
            return item
        else:
            for child in item.getChildren():
                if depthFirstR(child, name) != None:
                    result = child
    return result
    

    

def breadthFirstR(tree,name):
    queue = [tree]
    listT = []
    children = []
    for item in queue:
        if type(item) == list:
            for node in item:
                listT.append(node)
        else:
            listT.append(item)
            
    for item in listT:

        print "Now Searching: ", item.getName()
        if item.getName() == name:
            return item
        for child in item.getChildren():
            children.append(child)
    
    breadthFirstR(children,name)
                
def BFR(tree,name):
    if type(tree) == list:
        queue = list(chain.from_iterable(tree))
    else:
        queue = [tree]
    children = []

    for item in queue:
        print "Now Searching: ", item.getName()
        if item.getName() == name:
            return item
        else:
            children.append(item.getChildren())

    return BFR(children,name)
    




T1 = tree("a", [tree("b", [tree("d"),tree("e"),tree("f")]), tree("c", [tree("g", [tree("h")])])])

#print BFR(T1, "h")

#print breadthFirst(T1, "h")

print depthFirstR(T1, "d")

#print depthFirst(T1, "h")

#print T1





