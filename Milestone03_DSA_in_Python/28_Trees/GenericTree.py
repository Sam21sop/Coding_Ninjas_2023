class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)

    
