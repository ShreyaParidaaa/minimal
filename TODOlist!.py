#!/usr/bin/env python
# coding: utf-8

# In[5]:


tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def show_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Task removed: {removed}")
    except IndexError:
        print("Invalid task number!")

add_task("Learn Python")
add_task("Build a minimal project")
show_tasks()
delete_task()
show_tasks()


# In[ ]:




