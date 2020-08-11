from collections import deque
import re
import sys


def log_monitor(stdin, stdout):
    error_pattern = re.compile(r'^.+ .+ \[.+\] ERROR: .+$')
    context = deque()
    for line in stdin:
        is_error = bool(error_pattern.match(line))
        if is_error:
            stdout.write('-----\n')
            for context_line in context:
                stdout.write(context_line)
            stdout.write(line)
            context.clear()
        else:
            context.append(line)
            if len(context) > 3:
                context.popleft()


if __name__ == '__main__':
    log_monitor(sys.stdin, sys.stdout)
