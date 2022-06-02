""" Functions for working with ROS2 messages that have been read from bag files.

ROS2 bag_ files serialize message objects (by default_, in CDR_ format). The 
rosbag2 package does not automatically convert messages to common Python3 data 
structures. This module provides convenient functions for accomplishing that 
conversion.

.. _bag: https://docs.ros.org/en/galactic/Tutorials/Ros2bag
         /Recording-And-Playing-Back-Data.html)
.. _default: https://github.com/ros2/rosbag2#storage-format-plugin-architecture
.. _rosbag2: https://github.com/ros2/rosbag2#rosbag2
.. _CDR: https://en.wikipedia.org/wiki/Common_Data_Representation
"""

# Copyright 2022 Carnegie Mellon University Neuromechatronics Lab
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Contact: a.whit (nml@whit.contact)


# Import functionality for dynamically loading message objects.
import importlib

# Import ROS2 functionality for deserializing and translating messages.
from rclpy.serialization import deserialize_message
from rosidl_runtime_py import message_to_ordereddict



def string_to_message_type(specification):
    """ Converts a string message specification into the ROS2 message class 
        that it represents.
        
    Parameters
    ----------
    specification : str
        The _full_ package resource_ specification for a ROS2 message. This 
        consists of a package name, a module name, and a `message name`_, 
        separated by forward slashes (`/`). The convention_ is for message 
        names to use upper camel case, and to consist of only alphanumeric 
        characters. 
        Example: The specification of the `String` message, in the 
        `example_interfaces` package is `example_interfaces/msg/String`.
        
        .. _message name: https://design.ros2.org/articles
                          /legacy_interface_definition.html#messages
        .. _convention: https://design.ros2.org/articles
                        /legacy_interface_definition.html#conventions
        .. _resource: http://wiki.ros.org/Names#Package_Resource_Names
    
    Returns
    -------
    message_type : class
        The ROS2 message class corresponding to the message specification.
    
    Examples
    --------
    """
    (package_name,
     module_name,
     message_name) = specification.split('/')
    module = importlib.import_module(f'.{module_name}', package=package_name)
    message_type = getattr(module, message_name)
    return message_type
str2msg = string_to_message_type


def deserialize(data, message_type):
    """ Convert a serialized ROS2 message data object into a message object.
    
    Parameters
    ----------
    data : 
        A serialized ROS2 message.
    message_type : str or object
        The type of the serialized message, in the form of a string 
        specification (e.g., `'example_interfaces/msg/String'`) or a ROS2 
        message class (e.g., `example_interfaces.msg.String`).
        
    Returns
    -------
    message :
        A ROS2 message object of the class specified by the `message_type` 
        parameter.
    """
    message_type = string_to_message_type(message_type) \
                   if isinstance(message_type, str) \
                   else message_type
    message = deserialize_message(data, message_type=message_type)
    return message
    
  

def to_dict(data, message_type):
    """ Convert a serialized ROS2 message data object into an OrderedDict_.
    
    .. _OrderedDict: https://docs.python.org/3/library
                     /collections.html#collections.OrderedDict
    
    Parameters
    ----------
    data : 
        A serialized ROS2 message.
    message_type : str or object
        The type of the serialized message, in the form of a string 
        specification (e.g., `'example_interfaces/msg/String'`) or a ROS2 
        message class (e.g., `example_interfaces.msg.String`).
        
    Returns
    -------
    message : OrderedDict
        A ROS2 message organized as an ordered dictionary data structure.
    """
    message = deserialize(data, message_type)
    return message_to_ordereddict(message)
to_record = to_dict


