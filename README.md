# Unclosed File Handle in Python Function

This repository demonstrates a common error in Python: unclosed file handles.

The `bug.py` file shows a function that opens a file but fails to close it, leading to potential resource leaks. The `bugSolution.py` shows the correct way to handle the file.

**Problem:**
Unclosed file handles can lead to several issues, such as:

* **Resource leaks:** The operating system might not be able to release the file resources immediately.
* **File corruption:** If an error occurs, data might not be properly written to the file.
* **Unexpected behavior:** Other parts of the program might attempt to access the file, leading to errors.

**Solution:**
Always ensure that you close files using a `finally` block or a `with` statement to guarantee proper resource cleanup even if exceptions occur.
