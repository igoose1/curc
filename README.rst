.. image:: https://raw.githubusercontent.com/igoose1/curc/master/img/curc.png

====
curc
====

.. image:: https://badge.fury.io/py/curc.svg
    :target: https://badge.fury.io/py/curc

curc is a currency converter.

Installation::

    python -m pip install curc

Usage::

    curc <amount> <from> <to>

Example::

    curc 150 usd eur

Use "``curc --help``" for more information.

More:

- curc loads rates from ECB.

- rates are downloaded just once a day and cached.

- curc was written as everything sucks in response time.

- yes, I know Python sucks too if I want performance in CLI-applications.
