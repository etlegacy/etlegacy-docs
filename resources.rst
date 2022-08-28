=========
Resources
=========

.. _cvar-types:

CVAR Types
^^^^^^^^^^

Bitflag
-------
Bit Flags are used to store more than one `boolean value <Boolean>`_ in one number. To achieve this the value is read as a binary number.
A binary number is represented in the following way:

Normal: 128 64 32 16 8 4 2 1
Binary    0  0  0  0 0 0 0 0

A binary number of '11111111' would mean 255. As all the boolean values are true for their respective value.
So if you take the number 7 represented in binary it would look like this: '111'. This is because it adds 1 + 2 + 4 = 7.

This representation is used to enable or disable selectively multiple features through a single number.

List
----

A simple list of values, usually numbers that follow each other like '1,2,3'.

Range
-----

A range value is a value that can be between two numbers. For example 1 until 100. Depending on the CVAR this can be positive, negative or both positive and negative. See the following example:

1 until 3 - Available values: '1, 2, 3'.
-3 until -1 - Available values: '-3, -2, -1'.
-1 until 1 - Available values: '-1, 0, 1'.

The CVAR value can be a decimal or a integer.

Decimal: 1.0
Integer: 1


Boolean
-------

A value represented in '0' and '1'. Usually '1' means On/Enabled where '0' is Off/Disabled.

String
------

A text value.

Colors
^^^^^^

.. _menu-colors:

Menu Colors
------------

  +---------------+--------------+
  | Color         | Ingame value |
  +===============+==============+
  | White         | white        |
  +---------------+--------------+
  | Yellow        | yellow       |
  +---------------+--------------+
  | Red           | red          |
  +---------------+--------------+
  | Green         | green        |
  +---------------+--------------+
  | Blue          | blue         |
  +---------------+--------------+
  | Magenta       | magenta      |
  +---------------+--------------+
  | Cyan          | cyan         |
  +---------------+--------------+
  | Orange        | orange       |
  +---------------+--------------+
  | Light Blue    | 0xa0c0ff     |
  +---------------+--------------+
  | Medium Blue   | mdblue       |
  +---------------+--------------+
  | Light Red     | 0xffc0a0     |
  +---------------+--------------+
  | Medium Red    | mdred        |
  +---------------+--------------+
  | Light Green   | 0xa0ffc0     |
  +---------------+--------------+
  | Medium Green  | mdgreen      |
  +---------------+--------------+
  | Dark Green    | dkgreen      |
  +---------------+--------------+
  | Medium Cyan   | mdcyan       |
  +---------------+--------------+
  | Medium Yellow | mdyellow     |
  +---------------+--------------+
  | Medium Orange | mdorange     |
  +---------------+--------------+
  | Light Grey    | ltgrey       |
  +---------------+--------------+
  | Medium Grey   | mdgrey       |
  +---------------+--------------+
  | Dark Grey     | 0xa0c0ff     |
  +---------------+--------------+
  | Black         | black        |
  +---------------+--------------+

.. _crosshairs:

Crosshairs
^^^^^^^^^^

 - `Crosshair 0 <https://i.imgur.com/X4afYVt.png>`_
 - `Crosshair 1 <https://i.imgur.com/wmka5ZA.png>`_
 - `Crosshair 2 <https://i.imgur.com/2G4ZbhM.png>`_
 - `Crosshair 3 <https://i.imgur.com/7zGM3Lg.png>`_
 - `Crosshair 4 <https://i.imgur.com/pdjwUct.png>`_
 - `Crosshair 5 <https://i.imgur.com/wNus1y3.png>`_
 - `Crosshair 6 <https://i.imgur.com/XTc6phh.png>`_
 - `Crosshair 7 <https://i.imgur.com/iZ2LzQv.png>`_
 - `Crosshair 8 <https://i.imgur.com/KA2PFPW.png>`_
 - `Crosshair 9 <https://i.imgur.com/gfMRukk.png>`_