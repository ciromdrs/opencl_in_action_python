# OpenCL in Action using PyOpenCL
This is a reimplementation of the examples from OpenCL in Action, by Matthew Scarpino using [PyOpenCL](https://pypi.org/project/pyopencl/).

## How to run

*Note:* You must first install the driver, SDK and/or libraries necessary for your hardware and OS.

Build the docker image:
```
docker build -t ocl .
```

Run the docker container:
```
docker run -ti --rm --device /dev/dri:/dev/dri -v ./:/app ocl
```

Run a program inside the container:
```
python3 example.py
```

Try changing the contents in `example.cl` and running `example.py` again.