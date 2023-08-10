import pyopencl as cl

# Identify a platform
platform = cl.get_platforms()[0]

# Obtain data for each connected device
devices = platform.get_devices()
for d in devices:
    name = d.get_info(cl.device_info.NAME)
    address_width = d.get_info(cl.device_info.ADDRESS_BITS)
    extensions = d.get_info(cl.device_info.EXTENSIONS)
    dots = '...'
    max_length = 145
    extensions = extensions[:max_length-len(dots)] + dots if len(extensions) > max_length else extensions
    print('NAME:', name)
    print('ADDRESS_WIDTH:', address_width)
    print('EXTENSIONS:', extensions)