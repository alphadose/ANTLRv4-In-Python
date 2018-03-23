from antlr4 import *
from JSONLexer import JSONLexer
from JSONListener import JSONListener
from JSONParser import JSONParser
import sys

def main():
    lexer = JSONLexer(InputStream(sys.stdin.read()))
    stream = CommonTokenStream(lexer)
    parser = JSONParser(stream)
    tree = parser.json()
    printer = JSONListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()