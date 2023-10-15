# How To Manipulate Strings?

When you have string manipulation tasks to handle, the `string_manipulation` module is here to assist you. This section provides a guide on how to use the provided functions to solve common string-related challenges.

## Capitalize the First Letter of a String

If you need to capitalize the first letter of a string, the `capitalize_first` function is at your service. Follow these steps to integrate it into your project:

**Download the code**: Start by acquiring the `string_manipulation` module. You can obtain it from this GitHub repository or source it from your preferred location.

**Project Structure**: Ensure that you have a project structure similar to the following:

    
    your_project/
    │
    ├── string_manipulation/
    │   ├── __init__.py
    │   └── manipulator.py
    │
    └── your_script.py
    

**Import the Function**: In your Python script (`your_script.py`), import the `capitalize_first` function from the `string_manipulation.manipulator` module:

    
    from string_manipulation.manipulator import capitalize_first
    

**Utilize the Function**: Now that you've imported the function, you can use it to capitalize the first letter of any string:

    
    from string_manipulation.manipulator import capitalize_first

    result = capitalize_first('hello, world')
    print(result)  # OUTPUT: 'Hello, world'
    

## Reverse a String

If you need to reverse the characters in a string, the `reverse_string` function is the tool for the job. Follow these steps to make it part of your project:

**Download the code**: Obtain the `string_manipulation` module as described earlier.

**Project Structure**: Ensure your project structure is set up as shown above.

**Import the Function**: In your Python script, import the `reverse_string` function from the `string_manipulation.manipulator` module, just like in the previous example.

**Utilize the Function**: You can now use the function to reverse strings in your project:

    from string_manipulation.manipulator import reverse_string

    result = reverse_string('python')
    print(result)  # OUTPUT: 'nohtyp'
    

## Extract Numbers from a String

To extract all the numbers from a string, you can rely on the `extract_numbers` function. Here's how to incorporate it into your project:

**Download the code**: Obtain the `string_manipulation` module as described earlier.

**Project Structure**: Maintain the same project structure as before.

**Import the Function**: Import the `extract_numbers` function from the `string_manipulation.manipulator` module in your Python script.

**Utilize the Function**: Now, you can use the function to extract numbers from strings within your project:

    # your_script.py
    from string_manipulation.manipulator import extract_numbers

    result = extract_numbers('abc123xyz456')
    print(result)  # OUTPUT: [123, 456]
    

With these functions at your disposal, you're well-equipped to tackle various string manipulation tasks with ease.
