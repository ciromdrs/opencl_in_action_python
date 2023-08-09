#Port from Adventures in OpenCL Part1 to PyOpenCL
# http://enja.org/2010/07/13/adventures-in-opencl-part-1-getting-started/
# http://documen.tician.de/pyopencl/

import pyopencl as cl
import numpy

class CL:
    def __init__(self):
        self.ctx = cl.create_some_context()
        self.queue = cl.CommandQueue(self.ctx)

    def load_program(self, filename):
        # Read OpenCL source file
        f = open(filename, 'r')
        fstr = "".join(f.readlines())
        # Build program
        self.program = cl.Program(self.ctx, fstr).build()

    def initialize(self):
        mf = cl.mem_flags

        # Initialize client-side (CPU) arrays
        self.a = numpy.array(range(10), dtype=numpy.float32)
        self.b = numpy.array(range(10), dtype=numpy.float32)

        # Create OpenCL buffers
        self.a_buf = cl.Buffer(self.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=self.a)
        self.b_buf = cl.Buffer(self.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=self.b)
        self.dest_buf = cl.Buffer(self.ctx, mf.WRITE_ONLY, self.b.nbytes)

    def execute(self):
        self.program.do_something(self.queue, self.a.shape, None, self.a_buf, self.b_buf, self.dest_buf)
        c = numpy.empty_like(self.a)
        cl._enqueue_read_buffer(self.queue, self.dest_buf, c).wait()
        print("a", self.a)
        print("b", self.b)
        print("c", c)



if __name__ == "__main__":
    example = CL()
    example.load_program("example.cl")
    example.initialize()
    example.execute()
