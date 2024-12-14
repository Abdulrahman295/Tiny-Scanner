import os
from PyQt5 import QtWidgets
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import QByteArray
from graphviz import Graph
from src.parser.node import Node
from src.tokn.tokenType import TokenType

class TreeWindow(QtWidgets.QDialog):
    def __init__(self, root):
        super().__init__()
        self.setWindowTitle("Parse Tree")
        self.resize(800, 600)
        self.setStyleSheet("background-color: #19232D;")
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.root = root
        self.nodes = []
        self.current_node_index = 1
        self.build_visualization_data(self.root)
        self.visualize_tree()

    
    def build_visualization_data(self, node: Node, parent_index: int = None):
        if not node:
            return
        
        # Set node attributes
        node.set_index(self.current_node_index)
        self.current_node_index += 1
        node.set_parent(parent_index if parent_index else 0)
        
        # Add to nodes list
        self.nodes.append(node)
        
        # Process children
        for child in node.get_children():
            child.set_connect_parent(True)
            self.build_visualization_data(child, node.get_index())
            
        # Process siblings
        if node.get_sibling():
            node.get_sibling().set_connect_parent(False)
            self.build_visualization_data(node.get_sibling(), parent_index)

    def get_node_label(self, node):
        type = ""
        match node.get_token_type():
            case TokenType.NUMBER:
                type = "const"
            case TokenType.IDENTIFIER:
                type = "id"
            case TokenType.READ:
                type = "read"
            case TokenType.ASSIGN:
                type = "assign"
            case TokenType.PLUS | TokenType.MINUS | TokenType.MULT | TokenType.DIV | TokenType.LESSTHAN | TokenType.EQUAL:
                type = "op"

        lable = f"{type}\\n{node.get_token_value()}"
        return lable

    def visualize_tree(self):
        dot = Graph(comment='Syntax Tree', format='svg')
        
        # Global graph attributes
        dot.attr(rankdir='TB', ranksep='0.5')
        
        for node in self.nodes:
            label = self.get_node_label(node)
            if node.get_shape() == 'square':
                dot.node(str(node.get_index()),
                        label,
                        shape='square',
                        fixedsize='false')
            else:
                dot.node(str(node.get_index()),
                        label,
                        shape='ellipse',
                        fixedsize='false')
        
        # Create edges
        for node in self.nodes:
            if node.get_parent() != 0 and node.get_connect_parent():
                dot.edge(str(node.get_parent()), str(node.get_index()))
            elif node.get_parent() != 0:
                dot.edge(str(node.get_parent()), str(node.get_index()),
                        style='dashed', color='white')
        
        # Handle sibling connections
        for i, node1 in enumerate(self.nodes):
            for node2 in self.nodes[i+1:]:
                if (node1.get_parent() == node2.get_parent() and
                    not node2.get_connect_parent() and
                    node2.is_statement() and node1.is_statement()):
                    dot.edge(str(node1.get_index()), str(node2.get_index()),
                            constraint='false')
                    break
                    
        # Generate the graph
        temp_path = 'temp_tree'
        dot.render(temp_path, view=False, cleanup=True)
        
        # Create SVG widget and add to layout
        svg_widget = QSvgWidget()
        with open(f"{temp_path}.svg", 'r') as f:
            svg_content = f.read()
        svg_widget.load(QByteArray(svg_content.encode('utf-8')))
        
        # Add widget to layout
        self.layout().addWidget(svg_widget)
        
        # Clean up temporary file
        try:
            os.remove(f"{temp_path}.svg")
        except Exception as e:
            print(str(e))

    