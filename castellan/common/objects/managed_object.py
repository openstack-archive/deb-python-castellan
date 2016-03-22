# Copyright (c) The Johns Hopkins University/Applied Physics Laboratory
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Base ManagedObject Class

This module defines the ManagedObject class. The ManagedObject class
is the base class to represent all objects managed by the key manager.
"""
import abc

import six


@six.add_metaclass(abc.ABCMeta)
class ManagedObject(object):
    """Base class to represent all managed objects."""

    def __init__(self, name=None, created=None):
        """Managed Object

        :param name: the name of the managed object.
        :param created: the time a managed object was created.
        """
        self._name = name

        # If None or POSIX times
        if not created or type(created) == int:
            self._created = created
        else:
            raise ValueError('created must be of long type, actual type %s' %
                             type(created))

    @property
    def name(self):
        """Returns the name.

        Returns the object's name or None if this object does not have one.
        """
        return self._name

    @property
    def created(self):
        """Returns the POSIX time(long) of the object that was created.

        Returns the POSIX time(long) of the object that was created or None if
        the object does not have one, meaning it has not been persisted.
        """
        return self._created

    @abc.abstractproperty
    def format(self):
        """Returns the encoding format.

        Returns the object's encoding format or None if this object is not
        encoded.
        """
        pass

    @abc.abstractmethod
    def get_encoded(self):
        """Returns the encoded object.

        Returns a bytestring object in a format represented in the encoding
        specified.
        """
        pass
