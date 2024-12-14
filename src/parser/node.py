from enum import Enum
from typing import Optional
from src.tokn.tokenType import TokenType

class NodeShape(Enum):
    CIRCLE = 'circle'    
    SQUARE = 'square'    

class Node:
    def __init__(self, token_type: TokenType, token_value: str, shape: NodeShape):
        self.token_type = token_type
        self.token_value = "(" + token_value + ")"
        self.children: list[Node] =[]
        self.sibling: Optional[Node] = None
        self.shape = shape.value
        self.parent_index = None
        self.connect_parent = True
        self.index = 0

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, children):
        self.children.extend(children)

    def get_token_type(self):
        return self.token_type

    def get_token_value(self):
        return self.token_value

    def get_children(self):
        return self.children

    def get_sibling(self):
        return self.sibling

    def set_sibling(self, sibling):
        self.sibling = sibling
    
    def set_shape(self, shape: NodeShape):
        self.shape = shape.value

    def get_shape(self) -> str:
        return self.shape
    
    def set_index(self, index: int):
        self.index = index
    
    def get_index(self) -> int:
        return self.index
    
    def set_parent(self, parent_index):
        self.parent_index = parent_index

    def get_parent(self):
        return self.parent_index
    
    def set_connect_parent(self, connect_parent):
        self.connect_parent = connect_parent

    def get_connect_parent(self):
        return self.connect_parent
    
    def is_statement(self):
        return self.token_type in [TokenType.IF, TokenType.REPEAT, TokenType.ASSIGN, TokenType.READ, TokenType.WRITE]