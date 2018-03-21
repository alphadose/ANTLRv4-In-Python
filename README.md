# ANTLRv4-In-Python

## How to use:-

```
python traverse.py
```
Then give standard input and press Ctrl+D after it is complete.

## Example:-

```
 cat incorrect_sample.json | python traverse.py 
```
 
 ## Output:-
 
```
line 1:1 token recognition error at: '''
line 1:2 token recognition error at: 'a'
line 1:3 token recognition error at: '''
line 1:4 no viable alternative at input '{:'
```
## Example:-

```
cat correct_sample.json | python traverse.py
```

There would be no output in this case as the given JSON format is correct.
In other words the tree walker encountered no errors while traversing the Abstract Syntax Tree of the source.
