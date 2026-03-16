#!/usr/bin/env python3
import cardmap as cm
import punch_descriptions as pd

'''
punchName - row, col or (row,col) -> punch name
punchCoords - 'punch name' -> (row, col)
punchValue - 'punch name' -> bool
'''

# ---------------------------------------------------------------------------
# checks are all here 
# ---------------------------------------------------------------------------

def type_of_card(card, describe: bool = False):
    cm.set_current_card(card)
    print(">>> evaluating card type...")
    if cm.punchValue('TI'):
        for n in ('MOR', 'MIR', 'MOS'):
            if cm.punchValue(n):
                punch = n
                break
        else:
            punch = 'TI'
        result = ("Trouble Card", punch)
    else:
        for n in ('MTPT', 'SRT', 'TKT'):
            if cm.punchValue(n):
                result = ("Test Card", n)
                break
        else:
            result = ("Neither test call nor Trouble Indication", None)
    if describe and result[1] is not None:
        return result + (describe_punch(result[1]),)
    return result

def marker_no(card, describe: bool = False):
    cm.set_current_card(card)
    print(">>> evaluating marker number...")
    names = ['DR0', 'DR1', 'DR8']
    for n in names:
        if cm.punchValue(n):
            result = ("Marker", int(n[2:]))
            break
    else:
        raise ValueError("no marker punch detected")
    if describe:
        return result + (describe_punch(n),)
    return result

def trial_check(card, describe: bool = False):
    cm.set_current_card(card)
    print(">>> evaluating trial punches...")
    names = ['1TR', '2TR']
    for n in names:
        if cm.punchValue(n):
            if describe:
                return ("Trial", n, describe_punch(n))
            return ("Trial", n)
    return ("Trial", None)

def timer_check(card, describe: bool = False):
    '''
    Evaluates which timer expired, if any.

    returns that punch if true
    '''
    print('>>> evaluating marker timers...')
    names = (['WT', 'SDT', 'LDT', 'TRS'])
    for n in names:
        if cm.punchValue(n):
            return ("Timer", n)
    else:
        return ("Timer", None)

def status_flag_check(card, describe: bool = False):
    '''
    Evaluates which status flag is set, if any.

    returns that punch if true
    '''
    print(">>> evaluating marker status flags...")
    names = (['TRS', 'TGT', 'FCG', 'LR', 'DCK', 'GT5', 'SQA'])
    for n in names:
        if cm.punchValue(n):
            return ("Status Flag", n)
    else:
        return ("Status Flag", None)

def x_check(card, describe: bool = False):
    '''
    Time to check for crosses! This should be easy.
    '''
    print(">>> evaluating X punches...")
    names = (['XCL', 'XCR', 'XDL', 'XMB', 'XCP', 'XOB', 'XTV', 'XT5', 'XTB', 'XTG', 'XTB1', 'XTG1', 'XJC',
            'XJG', 'XJS', 'XLR', 'XTS', 'XLC', 'XLV', 'XAB', 'XF', 'XSL', 'XTS1', 'XPT', 'XRS', 'XRS1', 'XFT',
            'XHG', 'XLG', 'XCS', 'XLS', 'XLH', 'XLO', 'XFUT', 'XSS', 'XS', 'XSA', 'XN', 'XFG', 'XPG', 'XPTN',
            'XT', 'XCLC', 'XCKR', 'XTC', 'XTC1', 'XTRK', 'XTRL', 'XBT', 'XRL', 'XMRL', 'XAN', 'XCH', 'XVGA',
            'XVGB'])
    for n in names:
        if cm.punchValue(n):
            if describe:
                raise XError(describe_punch(n), n)
            raise XError(
                f"Cross detected ", xpunch=n)
    return ("Cross: ", None)

def register_check(card):
    '''
    Verify that the digits stored in the OR/IR are valid 2-of-5 codes

    Also records the number of the OR/IR used on this call.

    The digits recorded in the register are stored in reed packs labelled ``A`` through
    ``M``.  Each *digit* in the number occupies one letter group and is
    encoded using the two‑out‑of‑five scheme: exactly two of the positions
    ``0, 1, 2, 4, 7`` must be punched.  The sequence of digits has the
    following additional constraints:

    * digits always begin at group ``A`` and continue in alphabetical order
      without gaps; skipping a letter (e.g. ``A, B, D``) is invalid.
    * the number may be of **variable length**; groups after the last digit
      are allowed to remain completely empty.
    * the end of the information is marked by a special terminator group
      containing **only a single hole at position 7**.  This terminator must
      immediately follow the last two‑of‑five digit.  Any punches after the
      terminator are forbidden, and the terminator itself is not considered a
      digit.

    When a valid sequence is present the return value is a list of integers
    corresponding to the decoded digits (terminator excluded).

    Example::

        >>> register_check(card)
        [1, 0, 3, 9, 5]
    '''
    cm.set_current_card(card)

    # helpful dictionary for decoding integers to their respective two-of-five punches
    # this is different than the dictionary in sccweb.py because that dict uses positions in
    # a list. This dict uses the values of the holes.
    two_of_five = {
        0: [4, 7],
        1: [0, 1],
        2: [0, 2],
        3: [1, 2],
        4: [0, 4],
        5: [1, 4],
        6: [2, 4],
        7: [0, 7],
        8: [1, 7],
        9: [2, 7],
    }
    global register_type
    register_type = None

    if(cm.punchValue('TER') or cm.punchValue('INC')):
        register_type = 'IR'
    else:
        register_type = 'OR'
    print(">>> evaluating ", register_type, " data...")

    # retrieve the OR number
    names = (['CN-RG0', 'CN-RG1', 'CN-RG2', 'CN-RG3', 'CN-RG4', 'CN-RG5', 'CN-RG6', 'CN-RG7', 'CN-RG8', 'CN-RG9'])
    OR_number = None
    for n in names:
        if cm.punchValue(n):
            OR_number = int(n[5:])

    if OR_number is None and cm.punchValue('TER'):
        pass  # No OR punch on this call. IR's dont currently punch a hole here.

    # build reverse lookup: given a pair of positions -> digit
    rev = {tuple(sorted(v)): k for k, v in two_of_five.items()}

    decoded = []
    seen_zero = False       # True once we hit a completely empty group
    terminated = False      # True once we hit the single-7 marker

    # we capture the raw reed pack contents as we go so that an exception can
    # report exactly what was seen in each letter.
    registers = {}

    for letter_ord in range(ord('A'), ord('M') + 1):
        if letter_ord == ord('I'):
            # 'I' is not used for digit encoding, skip it
            continue
        if letter_ord == ord('M'):
            # 'M' has different rules and we don't use it anyway, skip it
            continue
        letter = chr(letter_ord)
        positions = [0, 1, 2, 4, 7]
        punched = [pos for pos in positions
                   if cm.punchValue(f"{letter}{pos}")]
        registers[letter] = punched.copy()

        if terminated:
            # once we have seen the terminator, no further punches are allowed
            if punched:
                raise RegCheckError(
                    f"punches present after termination at {letter}: {punched}",
                    or_number=OR_number,
                    registers=registers)
            continue

        if not punched:
            seen_zero = True
            continue

        if seen_zero:
            # we previously saw an empty group, so this is a skipped digit
            raise RegCheckError(f"skipped digit before {letter}",
                               or_number=OR_number,
                               registers=registers)

        # check for termination marker (exactly one hole at position 7)
        if punched == [7]:
            terminated = True
            continue

        # normal digit: must be two-of-five
        if len(punched) != 2:
            raise RegCheckError(
                f"{letter}-group has {len(punched)} punch(es) {punched}; "
                f"exactly two required for a digit, OR {OR_number}",
                or_number=OR_number,
                registers=registers)

        pair = tuple(sorted(punched))
        if pair not in rev:
            # This technically can't even happen??
            raise RegCheckError(f"invalid two-of-five pair {pair} for {letter}",
                               or_number=OR_number,
                               registers=registers)
        decoded.append(rev[pair])

    # if we collected digits, we expect a terminator somewhere afterwards
    if decoded and not terminated:
        raise RegCheckError("digit sequence not terminated with a 7",
                           or_number=OR_number,
                           registers=registers)

    return decoded, OR_number


last_or_failure = None
def register_check_fails(card):
    """Return ``True`` when :func:`register_check` reports invalid data.

    Instead of simply converting the exception to a boolean we also populate
    :data:`last_or_failure` with a tuple ``(or_number, registers, message)``
    describing the failure.  ``registers`` maps letter names to the list of
    punched positions seen in that group; ``or_number`` may be ``None`` if the
    card did not have a valid OR punch.

    Analysis can then be performed on the contents without interrupting program execution.
    """
    global last_or_failure

    try:
        register_check(card)
        last_or_failure = None
        return False
    except RegCheckError as exc:
        # record details for later inspection
        last_or_failure = (exc.or_number, exc.registers, str(exc))
        print(f"{register_type} check failed: {last_or_failure}")
        return True



def evaluate(card, describe: bool = False):
    """Evaluate a card and return a serializable metadata dict.

    This is useful for generating reports and persisting the results.
    """
    cm.set_current_card(card)

    meta = {
        "type": type_of_card(card, describe),
        "marker": marker_no(card, describe),
        "trial": trial_check(card, describe),
        "timer": timer_check(card, describe),
        "status_flag": status_flag_check(card, describe),
        "punches": truthy_punches(card),
    }

    # Register check + binning
    try:
        decoded, reg_number = register_check(card)
        meta["register"] = {"number": reg_number, "digits": decoded}
        meta["bin"] = bin_card(card, rules=[("reg_error", register_check_fails)], default="unbinned")
    except RegCheckError as exc:
        meta["register"] = {
            "error": str(exc),
            "or_number": exc.or_number,
            "registers": exc.registers,
        }
        meta["bin"] = "reg_error"

    # Cross detection is handled separately so we can keep metadata even if a cross occurs
    try:
        meta["cross"] = x_check(card, describe)
    except Exception as e:
        meta["cross_error"] = str(e)

    for k in meta:
        print(meta[k]) 

    return meta




# ---------------------------------------------------------------------------
# helper routines for binning/sorting by punches
# ---------------------------------------------------------------------------

def card_has(card, *names):
    """Return ``True`` if *card* has **all** of the punches in *names*.

    The card is activated for each lookup automatically.
    """
    cm.set_current_card(card)
    return all(cm.punchValue(n) for n in names)


def card_lacks(card, *names):
    """Return ``True`` if *card* has **none** of the punches in *names*."""
    cm.set_current_card(card)
    return all(not cm.punchValue(n) for n in names)


def bin_card(card, rules, default=None):
    """Assign *card* to the first bin whose predicate returns true.

    ``rules`` should be an iterable of ``(bin_name, predicate)`` pairs where
    *predicate* is a callable taking the card object and returning a truthy
    value.  The order of the rules matters; the first matching rule wins.  If
    no rule matches ``default`` is returned (``None`` by default).

    Example::

        rules = [
            ("trouble_TI", lambda c: card_has(c, "TI")),
            ("or_error", register_check_fails),
            ("TI_and_MOR", lambda c: card_has(c, "TI", "MOR")),
        ]
        bin_name = bin_card(card, rules)

    Because predicates are ordinary callables you can express arbitrarily
    complex combinations (presence *and* absence of punches, numerical checks
    on the output of :func:`register_check`, etc.).
    """
    cm.set_current_card(card)
    for name, predicate in rules:
        try:
            if predicate(card):

                return name
        except Exception as e:
            # wrap with context to make debugging easier
            raise RuntimeError(f"error evaluating bin '{name}': {e}") from e
    return default



# ---------------------------------------------------------------------------
# helpful functions that are friendly and helpful
# ---------------------------------------------------------------------------

def describe_punch(name):
    # Shorthand for clients that don't feel like importing the module
    return pd.describe(name)

def truthy_punches(card):
    """Return a list of punch names that are present (True) on the card."""
    cm.set_current_card(card)
    cm._build_card_map()

    punches = [name for name in cm.card_map.values() if cm.punchValue(name)]
    #punches.sort()
    return punches


# ---------------------------------------------------------------------------
# custom error classes
# ---------------------------------------------------------------------------

class RegCheckError(ValueError):
    """Raised when ``register_check`` encounters malformed OR data.

    The exception carries attributes that make it possible for callers to
    inspect the OR number and the raw contents of the letter groups that were
    examined.  ``register_check_fails`` uses this information to record diagnostics
    for later analysis.
    """

    def __init__(self, message, or_number=None, registers=None):
        super().__init__(message)
        self.or_number = or_number
        # ``registers`` is a dict mapping letter names (``'A'``..``'L'``) to the
        # list of punched positions seen in that group.  It is populated as the
        # check iterates through the letters so that even if an error occurs we
        # still have the state up through the failure point.
        self.registers = registers or {}

class XError(ValueError):
    """Raised when ``x_check`` encounters a cross indication.
    
    This exception carries attributes that make it possible for callers
    to gather information about the cross indication."""

    def __init__(self, message, xpunch=None):
        super().__init__(message)
        self.xpunch = xpunch