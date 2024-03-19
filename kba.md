# Overview
Provide brief answers to the knowledge-question worksheet.

## Answers

1. Briefly explain what is modular programming.
 
- Modular programming involves creating reusable classes and methods contained in their own files. 
These files can be imported into other programs. Each class or module should be responsible for a single purpose or group of closely related functions.

2. How can you import only a specific function or class from a module in Python? What is the syntax for this?

- To import a class use:  -- from my_module import MyClass
- To import a class method use: -- from my_module import MyClass.my_method
- To import a function use: -- from my_module import my_function

3. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference? Justify your answer.

- It is more like pass-by-reference, although if the parameter is an immutable type, then the reference refers to the value anyway.

4. Given the following Python code, what will be the output and why?

    ```python
    def modify_list(list_):
        list_.append("new")
        list_ = ["completely", "new"]

    items = ["original"]
    modify_list(items)
    print(items)
    ```
   
- It will print:  "['original', 'new']"
- This is because the first line in the function changes the original list using the append function.
- The second line creates a new list inside the scope of the function, that does not change the original list.


5. In Python, even though variables created within a function are local, there are still situations where you can modify data outside the scope with a local variable. Explain this anomaly and relate it to both mutability and pass by reference.

- If the variable created within the function is a list of lists, the nested lists may contain references to objects defined outside the function. Changing these would change them wherever they are.

6. List two benefits of modular coding approaches. How do these benefits assist in the development of medium-sized applications?

- Modules keep code that does one job or closely related jobs organised into a single location. This makes it easy to only import the classes or functions into your program that are relevant to your purpose.
- It is easier to create tests for a single module.