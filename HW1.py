a="am fost la bunici si am vazut o pisica mare"
b=a.replace("o pisica mare", " ")
print(b)

def func(x):
 return lambda a:a%x
rest10=func (10)
print(rest10(127))

def func(x):
 return lambda a:a%x
rest100=func (100)
print(rest100(243))

def func(x):
     return lambda a:a%x
rest1000=func (1000)
print(rest1000(5290))
