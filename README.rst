====
curc
====

curc is a currency converter.

Install::

    python -m pip install curc

Usage::

    curc <amount> <from> <to>

Example::

    curc 150 usd eur

Use "``curc --help``" for that information.

Use "``curc --list``" to print possible currencies.

Set "``SCRIPTING``" environment variable to print raw result.

More:

- curc loads rates from ECB.

- rates are downloaded just once a day and cached.

- curc was written as everything sucks in response time.

- yes, I know Python sucks too if I want performance in CLI-applications.
