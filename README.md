# ANTLRv4-In-Python

## How to use:-

```
python3 traverse.py
```
Then give standard input and press Ctrl+D after it is complete.

## Example:-

```
 cat incorrect_sample.json | python3 traverse.py 
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
cat correct_sample.json | python3 traverse.py
```

## Output:-

```
"a":1
"b":{"c":2,"d":3}
"c":2
"d":3
```
