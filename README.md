![image](https://raw.githubusercontent.com/igoose1/curc/master/img/curc.png)

# curc

[![image](https://badge.fury.io/py/curc.svg)](https://badge.fury.io/py/curc)

curc is a currency converter.

Usage:

    curc <amount> <from> <to>

Invoke directly with [uvx][uvx]:

    uvx curc 150 usd eur

Or install with pip:

    pip install curc

More:

-   curc loads rates from [ECB][ECB].
-   rates are downloaded once a day and cached in /tmp.

[uvx]: https://docs.astral.sh/uv/
[ECB]: https://www.ecb.europa.eu/
