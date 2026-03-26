#!/usr/bin/python3
import json

card_map = {}


def _build_card_map():
    """Populate :data:`card_map` from the CSV file.

    This is extracted from ``punchname`` so that the same cache can be used
    by other lookup helpers (e.g. reverse lookup by punch name).
    Calling it multiple times is safe; once the map is filled the function
    simply returns.
    """
    if card_map:
        return

    with open("cardpack/punchnames.csv") as f:
        names = iter(line.strip() for line in f)

        for row in range(18):
            for col in range(69):   # has to include the 9 blank punches in the center of the card
                card_map[(row, col)] = next(names)


def punchName(rno, cno=None):
    """Return the punch name at the given ``(row, column)`` coordinates.

    The CSV is loaded lazily on first access and cached in :data:`card_map`.

    The caller may supply the coordinates either as two separate integer
    arguments ``row, col`` or as a single two‑item sequence/tuple
    ``(row, col)``.  Passing anything else raises :class:`TypeError`.

    Examples::

        >>> punchname(2, 5)
        'A123'
        >>> punchname((2, 5))
        'A123'
    """
    _build_card_map()

    if cno is None:
        # user probably handed us a single tuple-like object
        try:
            rno, cno = rno
        except Exception:
            raise TypeError("punchname() requires either two integer "
                            "arguments or a single (row, column) tuple")

    return card_map[(rno, cno)]


def punchCoords(name):
    """Return the ``(row, col)`` coordinates for a given punch name.

    An exact string match is performed against the cached map.  If the name
    isn't present a :class:`KeyError` is raised.

    Example::

        >>> punchCoords('A123')
        (2, 5)
    """
    _build_card_map()

    for coord, pname in card_map.items():
        if pname == name:
            return coord
    # not found
    raise KeyError(f"Punch name {name!r} not found. Check punchnames.csv for valid names.")

# print(json.dumps(json_map))
# card currently being processed, stored by the caller
_current_card = None

def set_current_card(card):
    """Remember a card grid so :func:`punchValue` can work implicitly.

    ``card`` is expected to be a 2‑dimensional list/tuple indexed as
    ``card[row][col]`` containing truthy values for holes.
    """
    global _current_card
    _current_card = card


def punchValue(name, card=None):
    """Return the value of a named punch on a card.

    If ``card`` is supplied it is used directly; otherwise the most recent
    card passed to :func:`set_current_card` is used.  The return value is the
    value stored in the card grid at the punch's coordinates (typically
    ``True``/``False``).  A :class:`ValueError` is raised if no card is
    available.

    Example::

        >>> card = [[False]*69 for _ in range(18)]
        >>> cardmap.set_current_card(card)
        >>> cardmap.punchValue('A123')
        False
    """
    _build_card_map()
    if card is None:
        if _current_card is None:
            raise ValueError("no card has been set")
        card = _current_card

    # locate the punch and read its value
    coords = punchCoords(name)
    row, col = coords
    return card[row][col]
