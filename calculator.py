import re
print("#1 the calculator")
print("type 'quit' to exit \n ")
prev=0
run=True
def perform():
    global prev
    global run
    equation=""
    if prev==0:
       equation=input("enter the equation:")
    else:
        equation=input(str(prev))


    if equation == 'quit':
        print("bye")
        run=False
    else:
        equation=re.sub('[a-zA-Z]','',equation)
        if prev==0:
          prev= eval(equation)
        else:
          prev=eval(str(prev)+equation)

        print("ans=",prev)
while run:
    perform()
