import pyopencl as cl

# Create the context
context = cl.create_some_context()
ref_count = context.get_info(cl.context_info.REFERENCE_COUNT)

print("Initial reference count:", ref_count)

# Update and display the reference count
context2 = cl.Context.from_int_ptr(context.int_ptr, retain=True)
ref_count = context.get_info(cl.context_info.REFERENCE_COUNT)
print("Reference count:", ref_count)

# Release the context and display reference count again
# Note: I am not sure if simply changing the Python reference to the context
# is the correct way to release it
context2 = None
ref_count = context.get_info(cl.context_info.REFERENCE_COUNT)
print("Reference count:", ref_count)
