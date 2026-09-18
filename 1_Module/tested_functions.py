def adder(*args):
    for arg in args:
        if isinstance(arg,str):
            raise TypeError
    
    if len(args) < 2:
        raise ValueError
    else:
        return sum(args)
def divider(*args):
    if len(args) > 2 or len(args)<2:
        raise ValueError

    elif [arg for arg in args if not isinstance(arg,int)]:
        raise TypeError 
    elif args[-1] == 0:
        raise ValueError
        
    else:
        return args[0]/args[1]

print(divider(1,0))