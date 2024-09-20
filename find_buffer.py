import sys
import subprocess

def find_buffer_overflow(program):
    buffer_size = 1
    while True:
        payload = 'A' * buffer_size
        try:
            result = subprocess.run([f'./{program}', payload], capture_output=True, text=True, timeout=1)
            if result.returncode != 0:
                #print(f"Buffer overflow detected at {buffer_size} bytes")
                return buffer_size
            buffer_size += 1
        except subprocess.TimeoutExpired:
            print(f"Program timed out at {buffer_size} bytes")
            return buffer_size
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":

    program = sys.argv[1] if len(sys.argv) > 1 else "pie"
    overflow_size = find_buffer_overflow(program)

    if overflow_size:
        #print(f"Buffer overflow occurs at approximately {overflow_size} bytes")
        print(overflow_size)
    else:
        print("Failed to determine buffer overflow size")
