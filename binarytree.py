from __future__ import annotations

from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int 
    left: TreeNode | None = None 
    right: TreeNode | None = None 

    def __repr__(self) -> str: 
        return f"Node({self.val})"

class BinaryTree: 
    def __init__(self, value: int):
        self.root = TreeNode(value)
    
    def __len__(self) -> int: 
        """Gets the length of a tree"""
        
        def lenhelper(node: TreeNode | None) -> int:
            if node is None: 
                return 0
            return 1 + lenhelper(node.left) + lenhelper(node.right)

        return lenhelper(self.root)

    def insert(self, value: int) -> None: 
        new_node = TreeNode(value)

        def insert_helper(node: TreeNode | None) -> bool | None: 
            if node is None: 
                return 
            
            if node.left is None:
                node.left = new_node
                return True
            elif node.right is None: 
                node.right = new_node 
                return True
            
            else:
                if insert_helper(node.left): 
                    return True 
                
                insert_helper(node.right)
                
        insert_helper(self.root)
    
    def reverse(self) -> None: 
        """Reverses the node"""

        def helper(node: TreeNode | None = None) -> None | TreeNode:
            
            if node is None: return None 
            print(node)
            left = helper(node.left) # None -> 4
            right = helper(node.right) # None -> 5
            

            node.left = right # Node.left = None -> node.left = 5
            node.right = left # Node.right = None -> node.right = 4

            return node 
        
        helper(self.root)

