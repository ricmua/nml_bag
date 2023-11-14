<!-- License

Copyright 2022-2023 Neuromechatronics Lab, Carnegie Mellon University (a.whit)

Contributors: 
  a. whit. (nml@whit.contact)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
-->

# Usage example

This example demonstrates use of the ROS2 bag reader. 

The [doctest]s in this example can be run from the command line by invoking a 
command with the following form:

```bash
> python3 -m doctest path/to/example.md
```

## Write to a bag file

In order to illustrate the reader, a bag file must be available. Create a 
temporary directory to contain such a file.

```python
>>> import tempfile
>>> from os import sep
>>> tempdir = tempfile.TemporaryDirectory()
>>> bag_name = 'bag_test'
>>> bag_path = f'{tempdir.name}{sep}{bag_name}'

```

Open a bag for storage.

```python
>>> import rosbag2_py
>>> storage_options = rosbag2_py.StorageOptions(uri=bag_path,
...                                             max_cache_size=0,
...                                             storage_id='mcap')
>>> converter_options = rosbag2_py.ConverterOptions('', '')
>>> writer = rosbag2_py.SequentialWriter()
>>> writer.open(storage_options, converter_options)

```

Initialize topics in the bag.

```python
>>> topic = 'test'
>>> topic_metadata \
...  = rosbag2_py.TopicMetadata(name=topic,
...                             type='example_interfaces/msg/String',
...                             serialization_format='cdr')
>>> writer.create_topic(topic_metadata)

```

Write a message to the topic in the bag file.

```python
>>> import rclpy.clock
>>> from rclpy.serialization import serialize_message
>>> from example_interfaces import msg
>>> clock = rclpy.clock.Clock()
>>> message = msg.String(data='Hello World!')
>>> writer.write(topic, serialize_message(message), clock.now().nanoseconds)

```

Write a second message.

```python
>>> message.data = 'Goodybye World!'
>>> writer.write(topic, serialize_message(message), clock.now().nanoseconds)

```

Close the bag file.

```python
>>> writer.close()

```

## Read from the bag file

Initialize a bag reader.

```python
>>> from nml_bag import Reader
>>> reader = Reader(f'{bag_path}{sep}{bag_name}_0.mcap', 
...                 storage_id='mcap', 
...                 serialization_format='cdr')

```

Display the topics.

```python
>>> from pprint import pprint
>>> pprint(reader.topics)
['test']

```

Display the mapping between topics and message types.

```python
>>> pprint(reader.type_map)
{'test': 'example_interfaces/msg/String'}

```

Display the messages stored in the bag.

```python
>>> pprint(reader.records) # doctest: +ELLIPSIS
[{'data': 'Hello World!',
  'time_ns': ...,
  'topic': 'test',
  'type': 'example_interfaces/msg/String'},
 {'data': 'Goodybye World!',
  'time_ns': ...,
  'topic': 'test',
  'type': 'example_interfaces/msg/String'}]

```

## Cleanup

Clean up the temporary files and directory.

```python
>>> tempdir.cleanup()

```



<!------------------------------------------------------------------------------
   References
------------------------------------------------------------------------------->

[doctest]: https://docs.python.org/3/library/doctest.html

