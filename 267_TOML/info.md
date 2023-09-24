# Using TOML with Python

TOML—Tom’s Obvious Minimal Language—is a reasonably new configuration file format that the Python community has embraced over the last couple of years.

TOML is short for Tom’s Obvious Minimal Language and is humbly named after its creator, Tom Preston-Werner. It was designed expressly to be a configuration file format that should be “easy to parse into data structures in a wide variety of languages”.

A configuration is an important part of almost any application or system. It’ll allow you to change settings or behavior without changing the source code. Sometimes you’ll use a configuration to specify information needed to connect to another service like a database or cloud storage. Other times you’ll use configuration settings to allow your users to customize their experience with your project.

TOML is restrictive in a few aspects:

- All keys are interpreted as strings. You can’t easily use, say, a number as a key.
- TOML has no null type.
- Some whitespace is important, which makes it less efficient to compress the size of TOML documents.

TOML is built around key-value pairs that map nicely to hash table data structures. TOML values have different types. Each value must have one of the following types:

- String
- Integer
- Float
- Boolean
- Offset date-time
- Local date-time
- Local date
- Local time
- Array
- Inline table

**Keys are always interpreted as strings, even if quotation marks don’t surround them.**

Dots (.) play a special role in TOML keys. You can use dots in unquoted keys, but in that case, they’ll trigger grouping by splitting the dotted key at each dot.

```toml
[user]
player_x.symbol = "X"
player_x.color = "blue"
player_o.symbol = "O"
player_o.color = "green"
```

Here, you specify two dotted keys. Since they both start with player_x, the keys symbol and color will be grouped together inside a section named player_x.

A header is a key without a value, wrapped inside square brackets ([]).

**Indentation isn’t important in TOML.**

**In-line table representation:**

```toml
[user]
player_x = { symbol = "X", color = "blue" }
player_o = { symbol = "O", color = "green" }
```


TOML supports **defining times and dates** directly in your documents. You can choose between four different representations, each with its own specific use case:

An offset date-time is a timestamp with time zone information, representing a specific instant in time.
A local date-time is a timestamp without time zone information.
A local date is a date without any time zone information. You typically use this to represent a full day.
A local time is a time with any date or time zone information. You use a local time to represent a time of day.


```toml
offset_date-time     = 2021-01-12 01:23:45+01:00
offset_date-time_utc = 2021-01-12 00:23:45Z
local_date-time      = 2021-01-12 01:23:45
local_date           = 2021-01-12
local_time           = 01:23:45
local_time_with_us   = 01:23:45.654321
```

- TOML Arrays

```toml
potpourri = ["flower", 1749, { symbol = "X", color = "blue" }, 1994-02-14]
skiers = ["Thomas", "Bjørn", "Mika"]
players = [
    { symbol = "X", color = "blue", ai = true },
    { symbol = "O", color = "green", ai = false },
]
```

- Array of Tables

```toml
[[players]]
symbol = "X"
color = "blue"
ai = true

[[players]]
symbol = "O"
color = "green"
ai = false
```

The double square brackets define an array of tables instead of a regular table. 

