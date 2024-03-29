import os, pytest, re
import numpy as np

@pytest.mark.it("Import Numpy as np on the app.py file")
def test_declare_variable():
    path = 'app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import\s+numpy\s+as\s+np")
        assert bool(regex.search(content)) == True

