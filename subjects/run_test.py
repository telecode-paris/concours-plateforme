import io
import os
import sys
import contextlib
import tempfile

def temp_opener(name, flag, mode=0o777):
    return os.open(name, flag | os.O_TEMPORARY, mode)

def get_res_test(input, fp):
    res = ""
    old_stdin = sys.stdin

    with tempfile.NamedTemporaryFile(mode="w") as ftmp:
        ftmp.write(input)
        ftmp.flush()
        with open(ftmp.name, "r") as f:
            sys.stdin = f

            with io.StringIO() as buf, contextlib.redirect_stdout(buf):
                fp()
                res = buf.getvalue()
        sys.stdin = old_stdin
    return res