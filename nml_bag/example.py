""" Example use of the `nml_bags` package.
"""

# Copyright 2022 Carnegie Mellon University Neuromechatronics Lab
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Contact: a.whit (nml@whit.contact)


# Imports.
from os import sep
import tempfile
from pprint import pprint
import rosbag2_py
import rclpy.clock
from example_interfaces import msg
from rclpy.serialization import serialize_message
from nml_bag import Reader


# Write a sample bag.
def write_bag_file(bag_path, topic='test'):
    """ Write sample data to a temporary ROS2 bag file.
    """
    
    # Open the writer.
    storage_options = rosbag2_py.StorageOptions(uri=bag_path,
                                                max_cache_size=0,
                                                storage_id='sqlite3')
    converter_options = rosbag2_py.ConverterOptions('', '')
    writer = rosbag2_py.SequentialWriter()
    writer.open(storage_options, converter_options)
    
    # Create a topics.
    topic_metadata \
      = rosbag2_py.TopicMetadata(name=topic,
                                 type='example_interfaces/msg/String',
                                 serialization_format='cdr')
    writer.create_topic(topic_metadata)
    
    # Write a message.
    clock = rclpy.clock.Clock()
    message = msg.String(data='Hello World!')
    writer.write(topic, serialize_message(message), clock.now().nanoseconds)
    
    # Write a second message.
    message.data = 'Goodybye World!'
    writer.write(topic, serialize_message(message), clock.now().nanoseconds)
    
    # Return
    return 
    
  

# Run an example.
def main(bag_name='bag_test', topic='test'):
    """ Run an example to illustrate use of the bag Reader class.
    """
    
    # Create a temporary bag path.
    tempdir = tempfile.TemporaryDirectory()
    bag_path = f'{tempdir.name}{sep}{bag_name}'
    
    # Write a sample bag file to the temporary path.
    write_bag_file(bag_path, topic=topic)
    
    # Initialize a bag reader.
    reader = Reader(f'{bag_path}{sep}{bag_name}_0.db3', storage_id='sqlite3', serialization_format='cdr')
    
    # Print the topics.
    print(f'The bag contains the following topics:')
    pprint(reader.topics)
    
    # Print the mapping between topics and message types.
    print(f'The message types associated with each topic are as follows:')
    pprint(reader.type_map)
    
    # Print the messages stored in the bag.
    print(f'All message data records:')
    pprint(reader.records)
    
    # Clean up the temporary files and directory.
    tempdir.cleanup()
    
    # Return
    return
    
  

if __name__ == '__main__': main()



