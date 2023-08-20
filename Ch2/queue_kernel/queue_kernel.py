import pyopencl as cl

PROGRAM_FILE = "blank.cl"

# Create context
ctx = cl.create_some_context()
# Create command queue
queue = cl.CommandQueue(ctx)
# Create program
source = open(PROGRAM_FILE, 'r').read()
program = cl.Program(ctx, source).build()

# Create the kernel
# Every call to program.kernel_name produces a new kernel instance, so it is
# preferrable to use a variable to refer to that same instance.
kernel = program.blank
try:
    kernel(
        queue,
        (0,0), # numpy's array shape. I use (0,0) as a zero value for this.
        None   # Up to this moment, I've always set this to None.
    )
    print('Successfully queued kernel.')
except cl.Error as err:
    print('Could not enqueue the kernel execution command')
    print(err)
