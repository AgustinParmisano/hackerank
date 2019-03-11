# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

for s in sys.stdin:
    try:
        float(s)
        n = s.split(".")
        if len(n) == 2:
            if n[1] != "":
                if not ("+" in s[:2] and "-" in s[:2]):
                    print(isinstance(float(s),float))
                    continue
        else:
            if float(s) == 0:
                print(False)
    except Exception as e:
        print(False)
