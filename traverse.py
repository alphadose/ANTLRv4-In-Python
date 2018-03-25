from antlr4 import *
from JSONLexer import JSONLexer
from JSONVisitor import JSONVisitor
from JSONParser import JSONParser
import sys

class CustomVisitor(JSONVisitor):
	def visitPair(self, ctx:JSONParser.PairContext):
		print(ctx.getText())
		return self.visitChildren(ctx)

def main():
    lexer = JSONLexer(InputStream(sys.stdin.read()))
    stream = CommonTokenStream(lexer)
    parser = JSONParser(stream)
    tree = parser.json()
    visitor = CustomVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()