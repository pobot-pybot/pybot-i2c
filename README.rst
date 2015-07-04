''pybot'' collection
====================

This package is part of POBOT's `pybot` packages collection, which aims
at gathering contributions created while experimenting with various technologies or
hardware in the context of robotics projects.

Although primarily focused on robotics applications (taken with its widest acceptation)
some of these contributions can be used in other contexts. Don't hesitate to keep us informed
on any usage you could have made.

Implementation note
-------------------

The collection code is organized using namespace packages, in order to group them in
a single tree rather that resulting in a invading flat collection. Please refer to [this official
documentation](https://www.python.org/dev/peps/pep-0382/) for details.

Package content
===============

This packages provides helpers for dealing with I2C, and especially in the Raspberry Pi
context. 

This is achieved by defining and abstraction of the I2C bus wrapping the low level interface provided
by the target system. This allow accommodating to the various contexts, such as I2C being made available
via the `SMBus` class on the RasPi. 

In addition, a mock-up implementation is proposed as a fall-back instance for being able to run tests outside of the real 
target environment, using it for simulating real data traffic.

A thread-safe wrapper of SMBus is also available (`MTSMBus`), using serialized calls to the low
level read/write operations.

Dependencies
============

- pybot.core
