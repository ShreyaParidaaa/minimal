#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculator():
    print("Minimal Calculator (Type 'quit' to exit)")
    while True:
        expr = input("Enter expression: ")
        if expr.lower() == "quit":
            break
        try:
            print("Result:", eval(expr))
        except Exception as e:
            print("Error:", e)

calculator()


# In[ ]:




