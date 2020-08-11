from log_monitor.log_monitor import log_monitor
import io
import os

NUM_TEST_CASES = 3
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


def test_log_monitor():
    for i in range(NUM_TEST_CASES):
        with open(os.path.join(DATA_DIR, '{}.in.txt'.format(i))) as f:
            in_contents = f.read()
        with open(os.path.join(DATA_DIR, '{}.out.txt'.format(i))) as f:
            out_contents = f.read()

        stdin = io.StringIO(in_contents)
        stdout = io.StringIO()
        log_monitor(stdin, stdout)
        assert stdout.getvalue() == out_contents

