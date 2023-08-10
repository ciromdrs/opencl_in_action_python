import pyopencl as cl

# Source files
PROGRAM_FILE_1 = 'good.cl'
PROGRAM_FILE_2 = 'bad.cl'
input(
'''WARNING: the book example is intended to crash if you run this code 
as is. To avoid crashing, go to file `bad.cl` and change the name of the
`good` kernel to something else.
Press ENTER to continue'''
)
file_names = [PROGRAM_FILE_1, PROGRAM_FILE_2]
# Compiler options
options = "-cl-finite-math-only -cl-no-signed-zeros";  

# Create a context
ctx = cl.create_some_context()

# Read each program file and place content into list
sources = ''
for n in file_names:
    sources += open(n,'r').read() + '\n\n'

# Build a program containing all program content
program = cl.Program(ctx, sources).build()
print('Build status:', program.get_build_info(program.devices[0], cl.program_build_info.STATUS))
print('Build options:', program.get_build_info(program.devices[0], cl.program_build_info.OPTIONS))
print('Build log:', program.get_build_info(program.devices[0], cl.program_build_info.LOG))
