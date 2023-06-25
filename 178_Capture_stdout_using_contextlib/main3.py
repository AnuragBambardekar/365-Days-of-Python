import contextlib
import io

captured_output = io.StringIO()

with contextlib.redirect_stdout(captured_output):
    help(pow)

captured_string = captured_output.getvalue()

print(captured_string)