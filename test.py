from importlib.util import set_loader
import pdb

s = "the sky is blue"
s_list = list(s)
n = len(s)
ans = []
listl, listr = 0,0
for r in range(n-1,-1,-1):
    if s_list[r] == ' ': continue
    if r == n-1 or s_list[r+1] == ' ':
        listr = r
    if r == 0 or s_list[r-1] == ' ':
        listl = r
        while listl <= listr:
            ans.append(s_list[listl])
            listl += 1 
print("".join(ans))
