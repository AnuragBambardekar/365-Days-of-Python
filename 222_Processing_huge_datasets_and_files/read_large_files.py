"""
readline() is not inherently "bad," but it can have performance and memory usage issues when used to read large files. 
The main concern is that readline() reads files line by line, 
and if you're dealing with very large files, reading line by line can be inefficient and memory-intensive.

Memory Usage: Each line read by readline() is stored in memory until processed. If your file has many lines or very 
long lines, this can quickly consume a lot of memory.

Slow Performance: Reading line by line can be slower compared to reading in larger chunks. This is because there's overhead 
associated with repeatedly calling readline().

Disk Access: Reading a file line by line involves frequent disk access, which can be slow if the file is stored on a traditional 
hard disk drive (HDD).

Limited Parallelism: Reading line by line might not take full advantage of modern CPUs that can process data in parallel. Reading 
larger chunks allows for better utilization of CPU cores.

"""

# In chunks

chunk_size = 1024  # Specify the size of each chunk in bytes
# with open('./huge_file.txt', 'rb') as file:
#     while True:
#         chunk = file.read(chunk_size)
#         if not chunk:
#             break
#         print(chunk)
#         # Process the chunk
#         # For example: do_something_with(chunk)


# using iterators

# def read_large_file(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             yield line.strip()

# for line in read_large_file('./huge_file.txt'):
#     # Process the line
#     print(line)


# Memory maps
import mmap

with open('./huge_file.txt', 'r') as file:
    with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
        # Now you can use mmap_obj to access the file's content
        # For example: data = mmap_obj[:100]  # Read the first 100 bytes
        print(mmap_obj[:100])