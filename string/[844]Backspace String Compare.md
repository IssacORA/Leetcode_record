'#' in a string means backspace. Multiple '#' mean backspace many times.

My solution:
Accumulate number of '#' then offset with characters before it.
```
class Solution:
    def simplfy(string):
        res=''
        symbol=0
        for i in string[::-1]:
            if i=='#':
                symbol+=1
            elif symbol >0:
                symbol-=1
            else:
                res=i+res
        return res

    def backspaceCompare(self, s: str, t: str) -> bool:
        return Solution.simplfy(s)==Solution.simplfy(t)
```

Stack:
Similar to stack legos one by one with each letter and remove one on the top with each '#'
```
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(s: str) -> str:
            ret = list()
            for ch in s:
                if ch != "#":
                    ret.append(ch)
                elif ret:
                    ret.pop()
            return "".join(ret)
        
        return build(S) == build(T)
```


Regular expression:

Far more cooool than any above.
> re.sub(pattern, replacement, string) => replace any part of "string" in "pattern" with "replacement".
> If leave "replacement" empty, "pattern" in "string" will be deleted as below.
> Scanning the string, every time match a single letter and a '#' after it like 'x#' then delete that.
> After that delete all '#', so I guess '|' has a order to execute
```
class Solution:
    import re

    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(s):
            # while s.find(r'#') > 0:
            while '#' in s:
                s = re.sub(r'(^|[^#])#', "", s)
            return s
        return f(s) == f(t)

```
