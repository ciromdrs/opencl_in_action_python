import pyopencl as cl
import numpy

# Extension to test
icd_ext = "cl_khr_icd"


# Access all installed platforms
platforms = cl.get_platforms()

# Find extensions of all platforms
found_icd = False
for p in platforms:
    # Access extension data
    ext_data = p.get_info(cl.platform_info.EXTENSIONS)
    print('Platform', p.get_info(cl.platform_info.NAME))
    # print('Supported extensions:', ext_data) # Commented because it is annoying

    # Look for ICD extension
    if icd_ext in ext_data.split(' '):
        print('Suports', icd_ext)
        found_icd = True
    else:
        print('Does not support', icd_ext)

if not found_icd:
    print('No platforms support the',icd_ext,'extension.\n')
