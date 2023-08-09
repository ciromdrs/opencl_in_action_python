import pyopencl as cl
import numpy

# Constants
PROGRAM_FILE = "matvec.cl"
n = 4 # Length of the vector

# Initialize data to be processed by the kernel
vector = [0.] * n
matrix = [0.] * (n**2)
correct = [0.] * n
for i in range(n**2):
    matrix[i] = i * 2.
for i in range(n):
    vector[i] = i * 3.
    for j in range(n):
        correct[j] += matrix[i+j*n] * vector[i]

# Create context
ctx = cl.create_some_context()
# Create command queue
queue = cl.CommandQueue(ctx)

# Create host arrays
host_matrix = numpy.array(matrix, dtype=numpy.float32)
host_vector = numpy.array(vector, dtype=numpy.float32)

# Read OpenCL C source file
source = ''.join(open(PROGRAM_FILE, 'r').readlines())
# Build the program
program = cl.Program(ctx, source).build()

# Create OpenCL buffers
matrix_buf = cl.Buffer(
    ctx,
    cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR,
    hostbuf = host_matrix)
vector_buf = cl.Buffer(
    ctx,
    cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR,
    hostbuf = host_vector)
result_buf = cl.Buffer(ctx,
        cl.mem_flags.WRITE_ONLY,
        host_vector.nbytes)

# Every call to program.kernel_name produces a new kernel instance,
# so it is preferrable to use a variable to refer to one same instance.
kernel = program.matvec_mult
kernel(
    queue,
    host_matrix.shape, # Not sure about this
    None,
    matrix_buf,
    vector_buf,
    result_buf
)
result = numpy.empty_like(host_vector)
cl._enqueue_read_buffer(queue, result_buf, result).wait()


# Test the result
for i in range(n):
    if result[i] != correct[i]:
        print('Matrix:', matrix)
        print('Vector',vector)
        print('Want:', correct)
        print('Got:', result)
        print("Matrix-vector multiplication unsuccessful.\n")
        exit(0)
else:
    print("Matrix-vector multiplication successful.\n")