import time

import shadebags

input_path = '/root/Downloads/stairs_compressed.bag' # '../../renv/stairs_compressed.bag'  # '/root/Downloads/stairs_compressed.bag'
output_path = '/root/Downloads/output.shade'

if __name__ == "__main__":
    writer = shadebags.Writer(input_path, output_path, shadebags.types.ROS1)

    writer.write()

    reader = shadebags.Reader(output_path, '/root/Downloads/output.ros', shadebags.types.ROS1)

    reader.read()

    time.sleep(1000000000)
