24-05-2020
----------
Version 0.2 released.

1)
 Change order of parameters in CLI fro.

    punits <choice> <source> <values> <target>

to

    punits <choice> <source> <target> <values>

2)
Use `ValueError` instead of user defined exceptions

3)
Refactor code for CLI to make __main__.py minimal by placing the rest in app.py
