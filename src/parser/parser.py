from src.tokn.token import Token
from src.tokn.tokenType import TokenType
from src.parser.node import Node
from src.parser.node import NodeShape
from typing import Optional

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.token_index = 0 # used for iterating through tokens
        self.current_token = tokens[self.token_index]

    def get_parse_tree(self):
        try:
            parse_tree = self.statement_sequence()
            return parse_tree

        except Exception as e:
            raise RuntimeError(f"Error during parsing process: {str(e)}")

    def advance_token(self):
        if self.token_index < len(self.tokens) - 1:
            self.token_index += 1
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None

    def match(self, token_type: TokenType):
        if  self.current_token and self.current_token.get_type() == token_type:
            self.advance_token()
        else:
            raise ValueError(f"Expected {token_type} but got {self.current_token.get_type()}")

    #define the EBNF grammar
    def statement_sequence(self) -> Optional[Node]:
        root_node = self.statement()
        current_node = root_node

        while self.current_token and self.current_token.get_type() == TokenType.SEMICOLON:
            try:
                self.match(TokenType.SEMICOLON)
                next_node = self.statement()

                if next_node is None:
                    break

                if root_node is None:
                    root_node = next_node
                    current_node = root_node
                else:
                    current_node.set_sibling(next_node)
                    current_node = next_node

            except Exception as e:
                raise RuntimeError(f"Error parsing statement sequence: {str(e)}")
            
        return root_node

    def statement(self) -> Optional[Node]:
        try:
            token_type = self.current_token.get_type()

            match token_type:
                case TokenType.IF:
                    return self.if_statement()
                case TokenType.REPEAT:
                    return self.repeat_statement()
                case TokenType.IDENTIFIER:
                    return self.assign_statement()
                case TokenType.READ:
                    return self.read_statement()
                case TokenType.WRITE:
                    return self.write_statement()
                case _:
                    raise ValueError(f"Unexpected token type: {token_type}")
                
        except Exception as e:
            raise RuntimeError(f"Error parsing statement: {str(e)}")

    def if_statement(self)-> Optional[Node]:
        try:
            if_node = Node(self.current_token.get_type(), self.current_token.get_value(), NodeShape.SQUARE)
            self.match(TokenType.IF)
          
            condition_node = self.expression()
            if not condition_node:
                raise ValueError("Missing condition in if statement")
            if_node.add_child(condition_node)

            self.match(TokenType.THEN)
            then_node = self.statement_sequence()
            if not then_node:
                raise ValueError("Empty THEN branch in if statement")
            if_node.add_child(then_node)

            self.match(TokenType.END)

            return if_node
        
        except Exception as e:
            raise RuntimeError(f"Error parsing if statement: {str(e)}")

    def repeat_statement(self) -> Optional[Node]:
        try:
            repeat_node = Node(self.current_token.get_type(), self.current_token.get_value(), NodeShape.SQUARE)
            self.match(TokenType.REPEAT)

            repeat_body = self.statement_sequence()
            if not repeat_body:
                raise ValueError("Empty repeat body")
            repeat_node.add_child(repeat_body)

            self.match(TokenType.UNTIL)
            until_condition = self.expression()
            if not until_condition:
                raise ValueError("Missing condition in repeat statement")
            repeat_node.add_child(until_condition)

            return repeat_node
        
        except Exception as e:
            raise RuntimeError(f"Error parsing repeat statement: {str(e)}")

    def assign_statement(self) -> Optional[Node]:
        try:
            assign_node = Node(TokenType.ASSIGN, self.current_token.get_value(), NodeShape.SQUARE)
            self.match(TokenType.IDENTIFIER)
            self.match(TokenType.ASSIGN)

            expression_node = self.expression()
            if not expression_node:
                raise ValueError("Missing expression in assign statement")
            assign_node.add_child(expression_node)

            return assign_node
        
        except Exception as e:
            raise RuntimeError(f"Error parsing assign statement: {str(e)}")

    def read_statement(self)-> Optional[Node]:
        try:
            self.match(TokenType.READ)
            read_node = Node(TokenType.READ, self.current_token.get_value(), NodeShape.SQUARE)
            self.match(TokenType.IDENTIFIER)
        
            return read_node
        
        except Exception as e:
            raise RuntimeError(f"Error parsing read statement: {str(e)}")

    def write_statement(self)-> Optional[Node]:
        try:
            write_node = Node(self.current_token.get_type(), self.current_token.get_value(), NodeShape.SQUARE)
            self.match(TokenType.WRITE)

            expression_node = self.expression()
            if not expression_node:
                raise ValueError("Missing expression in write statement")
            write_node.add_child(expression_node)

            return write_node

        except Exception as e:
            raise RuntimeError(f"Error parsing write statement: {str(e)}")

    def expression(self) -> Optional[Node]:
        try:
            left_expr_node = self.simple_expression()
            if not left_expr_node:
                raise ValueError("Missing simple-expression in expression")

            if self.current_token and self.current_token.get_type() in [TokenType.LESSTHAN, TokenType.EQUAL]:
                comparison_op_node = Node(self.current_token.get_type(), self.current_token.get_value(), NodeShape.SQUARE)
                comparison_op_node.add_child(left_expr_node) 

                self.comparison_operator()

                right_expr_node = self.simple_expression()
                if not right_expr_node:
                    raise ValueError("Missing simple-expression in expression")
                comparison_op_node.add_child(right_expr_node) # right child

                return comparison_op_node
            else:
                return left_expr_node
            
        except Exception as e:
            raise RuntimeError(f"Error parsing expression: {str(e)}")

    def comparison_operator(self):
        try:
            match self.current_token.get_type():
                case TokenType.LESSTHAN:
                    self.match(TokenType.LESSTHAN)
                case TokenType.EQUAL:
                    self.match(TokenType.EQUAL)
                case _:
                    raise ValueError(f"Unexpected token type: {self.current_token.get_type()}")
        
        except Exception as e:
            raise RuntimeError(f"Error parsing comparison operator: {str(e)}")

    def simple_expression(self) -> Optional[Node]:
        try:
            left_term_node = self.term()
            if not left_term_node:
                raise ValueError("Missing term in simple-expression")

            while self.current_token and self.current_token.get_type() in [TokenType.PLUS, TokenType.MINUS]:
                add_op_node = Node(self.current_token.get_type(), self.current_token.get_value(), NodeShape.SQUARE)
                add_op_node.add_child(left_term_node)

                self.add_operator()

                right_term_node = self.term()
                if not right_term_node:
                    raise ValueError("Missing term in simple-expression")
                add_op_node.add_child(right_term_node)

                left_term_node = add_op_node
            
            return left_term_node
        
        except Exception as e:
            raise RuntimeError(f"Error parsing simple expression: {str(e)}")

    def add_operator(self):
        try:
            match self.current_token.get_type():
                case TokenType.PLUS:
                    self.match(TokenType.PLUS)
                case TokenType.MINUS:
                    self.match(TokenType.MINUS)
                case _:
                    raise ValueError(f"Unexpected token type: {self.current_token.get_type()}")
        
        except Exception as e:
            raise RuntimeError(f"Error parsing add operator: {str(e)}")

    def term(self) -> Optional[Node]:
        try:
            left_factor_node = self.factor()
            if not left_factor_node:
                raise ValueError("Missing factor in term")

            while self.current_token and self.current_token.get_type() in [TokenType.MULT, TokenType.DIV]:
                mul_op_node = Node(self.current_token.get_type(), self.current_token.get_value(), NodeShape.SQUARE)
                mul_op_node.add_child(left_factor_node)

                self.mul_operator()

                right_factor_node = self.factor()
                if not right_factor_node:
                    raise ValueError("Missing factor in term")
                mul_op_node.add_child(right_factor_node)

                left_factor_node = mul_op_node
            
            return left_factor_node
        
        except Exception as e:
            raise RuntimeError(f"Error parsing term:: {str(e)}")

    def mul_operator(self):
        try:
            match self.current_token.get_type():
                case TokenType.MULT:
                    self.match(TokenType.MULT)
                case TokenType.DIV:
                    self.match(TokenType.DIV)
                case _:
                    raise ValueError(f"Unexpected token type: {self.current_token.get_type()}")
        
        except Exception as e:
            raise RuntimeError(f"Error parsing mul operator: {str(e)}")

    def factor(self) -> Optional[Node]:
        try:
            match self.current_token.get_type():
                case TokenType.IDENTIFIER:
                    identifier_node = Node(self.current_token.get_type(), self.current_token.get_value(), NodeShape.CIRCLE)
                    self.match(TokenType.IDENTIFIER)
                    return identifier_node
                case TokenType.NUMBER:
                    number_node = Node(self.current_token.get_type(), self.current_token.get_value(), NodeShape.CIRCLE)
                    self.match(TokenType.NUMBER)
                    return number_node
                case TokenType.OPENBRACKET:
                    self.match(TokenType.OPENBRACKET)
                    expression_node = self.expression()
                    if not expression_node:
                        raise ValueError("Missing expression in factor")
                    self.match(TokenType.CLOSEDBRACKET)
                    return expression_node
                case _:
                    raise ValueError(f"Expected identifier, number or '(' but got {self.current_token.get_type()}")
        
        except Exception as e:
            raise RuntimeError(f"Error parsing factor: {str(e)}")