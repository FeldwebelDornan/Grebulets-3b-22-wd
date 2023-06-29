def calculator(a:int,b:str,c:int):
    if b=='+':
        return(int(a)+int(c))
    if b=='-':
        return(int(a)-int(c))
    if b=='*':
        return(int(a)*int(c))
    if b=='/':
       return(int(a)/int(c))