import sys, subprocess

grammar_name = sys.argv[1]
grammar_rule = sys.argv[2]
file_path = sys.argv[3]

with open(file_path) as f:
	file = f.read()

subprocess.call('java -jar /usr/local/lib/antlr-4.7.1-complete.jar {}.g4'.format(grammar_name), shell=True)

subprocess.call('/usr/bin/javac {}*.java'.format(grammar_name), shell=True)

out = subprocess.check_output('echo \'{}\' | java org.antlr.v4.gui.TestRig {} {} -tree'.format(file, grammar_name, grammar_rule), shell=True)

print ("AST output:\n" + out)
