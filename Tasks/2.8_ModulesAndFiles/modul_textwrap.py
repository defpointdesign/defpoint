import textwrap
text='Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.'
wrapped_text=textwrap.wrap(text, width=35)
for line in wrapped_text:
    print(line)
