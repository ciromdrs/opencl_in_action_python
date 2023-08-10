import pyopencl as cl

# Kernel to search for
kernel_name = 'mult'

# Create the context
ctx = cl.create_some_context()

# Read program file and place content into buffer */
source = open('test.cl', 'r').read()
program = cl.Program(ctx, source).build()

# Search for the named kernel
for i, k in enumerate(program.all_kernels()):
    if k.get_info(cl.kernel_info.FUNCTION_NAME) == kernel_name:
        print('Found', kernel_name, 'kernel at index', i)
        break
else:
    print('Kernel', kernel_name, ' not found')