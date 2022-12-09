def search(self, val):
        # if value to be searched is found
        if val==self.data:
            return str(val)+" is found in the BST"
        # if value is lesser than the value of the parent node
        elif val < self.data:
            # if we still need to move towards the left subtree
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return str(val)+" is not found in the BST"
        # if value is greater than the value of the parent node
        else:
            # if we still need to move towards the right subtree
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return str(val)+" is not found in the BST" 