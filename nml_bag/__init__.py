""" ROS2 bag file processing for NML experimental data.

ROS2 facilitates data recording and playback via bag_ files. By default_, the 
ROS2 bag mechanism uses the sqlite_ 3 storage format, and the Common Data 
Representation (CDR_) serialization format. This package provides functionality 
for extracting and translating data stored in bag files.

The ROS2 **design_ document** for rosbags is currently unpublished, but the 
draft_ is available. 

Note: Although the sqlite3_ package is part of the standard distribution of 
Python 3 -- and it can be used to interpret bag files -- it is recommended that 
the ROS2 API be used for decoding bag files wherever possible.

.. _bag: https://docs.ros.org/en/galactic/Tutorials/Ros2bag
         /Recording-And-Playing-Back-Data.html)
.. _default: https://github.com/ros2/rosbag2#storage-format-plugin-architecture
.. _sqlite: https://en.wikipedia.org/wiki/SQLite
.. _CDR: https://en.wikipedia.org/wiki/Common_Data_Representation
.. _sqlite3: https://docs.python.org/3/library/sqlite3.html
.. _design: https://design.ros2.org/
.. _draft: https://github.com/ros2/design/blob/ros2bags/articles/rosbags.md
"""

# Copyright 2022 Carnegie Mellon University Neuromechatronics Lab
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Contact: a.whit (nml@whit.contact)

from .reader import Reader

__version__ = '1.0.0'

