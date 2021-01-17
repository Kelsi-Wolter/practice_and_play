# write a function to see if a tree is superbalanced(if the depths of any 2 leaf nodes
# is <= 1)

class BinaryTreeNode(object):
    '''sample tree class from interview cake'''

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def is_superbalanced(self):
        '''Check if there are any leafs with difference > 1'''
        # find two leafs with difference > 1

        #     traverse tree to find leafs
        #     do BFS to find depths of leafs (queue) - NOPE 
        #     do DFS to find leafs quickest, then use short-circuit to quit program
        #     once a difference of greater than 1 is found

            nodes_to_check = [root]
            depth = 1
            min_leaf_depth = 0
            max_leaf_depth = 0

            while nodes_to_check:
                current = nodes_to_check.pop()
                current_node = current[0]
                if current_node.left or current_node.right != None:
                    nodes_to_check.append((current.left, depth), (current.right, depth))
                    depth += 1
                else:
                    node_depth = current[1]
                    if min == 0:
                        set min 
                    else:
                        if node_depth < min:
                            if min - node_depth > 1 or max - node_depth > 1:
                                return False
                            else:
                                min = depth 
                        else depth > max:
                            if max - min > 1:
                                return False
                            else:
                                max = depth 
                        
                        
            # Pseudocode guide
            # check for children, 
            #     if children --> go to those children and continue, depth = 2
            #     if children (self.left & self.right) == None --> 
            #     depth = current depth
            #     and see if it is greater than or less than min/max
            #     update as appropriate
            #     continue until all nodes have been checked 
# edge cases:
# tree of one node 
# super balanced tree 
# super unbalanced tree 