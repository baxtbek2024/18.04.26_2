def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error"

a = float(input("a: "))
b = float(input("b: "))
op = input("Operator (+ - * /): ")

if op == '+': print(add(a, b))
elif op == '-': print(sub(a, b))
elif op == '*': print(mul(a, b))
elif op == '/': print(div(a, b))

email = input("Email: ")

username, domain = email.split("@")
print("Username:", username)
print("Domain:", domain)
