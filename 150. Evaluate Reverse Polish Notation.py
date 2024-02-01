#150. Evaluate Reverse Polish Notation
#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=daily-question&envId=2024-01-30

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
#        result=0
        for t in tokens:
            c=d=0
            #if t.isnumeric():
            #    a.append(int(t))
            #    print('#',result,a)
            #else:
            match t:
                case '+':
                    if result==0:
                        c=a.pop()
                        d=a.pop()
                        a.append(int(c+d))
                    #else:
                    #    c=a.pop()
                    #    result+=c
                    #print('+',result,a,c,d)
                case '-':
                    
                    if result==0:
                        c=a.pop()
                        d=a.pop()
                        a.append(int(d-c))
                        #result=c-d
                    #else:
                    #    c=a.pop()
                    #    result=c-result
                    #print('-',result,a,c,d)
                case '*':
                    if result==0:
                        c=a.pop()
                        d=a.pop()
                        a.append(int(c*d))
                        #result=c*d
                    #else:
                    #    c=a.pop()
                    #    result=c*result
                    #print('*',result,a,c,d)
                case '/':
                    if result==0:
                        c=a.pop()
                        d=a.pop()
                        #result=int(c/d)
                        a.append(int(d/c))
                    #else:
                    #    c=a.pop()
                    #    result=int(c/result)
                    #print('/',result,a,d,c)
                case _:
                    a.append(int(t))
                    #print('#',result,a)
        #print('=',a)
        return a.pop()
                        
        