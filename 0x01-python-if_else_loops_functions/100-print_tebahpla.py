#!/usr/bin/python3
print("".join(chr(219 - i) if i % 2 == 0 else chr(155 - i) for i in range(26)), end="")
