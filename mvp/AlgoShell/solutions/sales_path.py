def get_cheapest_cost(rootNode):
    return getMinSalesPath(rootNode)

def getMinSalesPath(node):
    if not node.children:
        return node.cost
    childSums = [getMinSalesPath(child) for child in node.children]
    return node.cost + min(childSums)

# NOTE: This Node class should be kept commented for the user to see.
#       An exact version is also used in the test cases.
class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None
