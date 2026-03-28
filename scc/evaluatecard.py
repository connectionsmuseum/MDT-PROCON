#!/usr/bin/env python3
import cardmap as cm
import punch_descriptions as pd

'''
punchName - row, col or (row,col) -> punch name
punchCoords - 'punch name' -> (row, col)
punchValue - 'punch name' -> bool
'''

# ---------------------------------------------------------------------------
# these are used to generate card metadata
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
        result = (punch, )
    else:
        for n in ('MTPT', 'SRT', 'TKT', 'MLV'):
            if cm.punchValue(n):
                result = (n, )
                break
        else:
            result = (None, )
    if describe and result[0] is not None:
        return result + (describe_punch(result[0]),)
    return result

def marker_no(card, describe: bool = False):
    cm.set_current_card(card)
    print(">>> evaluating marker number...")
    number = next((f'DR{i}' for i in range(10) if cm.punchValue(f'DR{i}')), None)
    if number is None:
        raise ValueError("no marker punch detected")
    if describe:
        return (number, describe_punch(number))
    return number[2:]

def trial_getmeta(card, describe: bool = False):
    cm.set_current_card(card)
    print(">>> evaluating trial punches...")
    names = ['1TR', '2TR']

    trial = next((n for n in names if cm.punchValue(n)), None)
    if describe:
        return (trial, describe_punch(trial))
    else:
        return (trial)

def timer_getmeta(card, describe: bool = False):
    '''
    Evaluates which timer expired, if any.

    returns that punch if true
    '''
    print('>>> evaluating marker timers...')
    names = (['WT', 'SDT', 'LDT', 'TRS'])
    
    timer = next((n for n in names if cm.punchValue(n)), None)

    if describe:
        return (timer, describe_punch(timer))
    else:
        return(timer)

def ch_tk_getmeta(card, describe: bool = False):
    '''
    Evaluates the following punches and returns a dictionary as follows

        "channel": int or None,  # 0-9 if CH0-9 detected, otherwise None
        "pattern": str or None,  # pattern name if P0-9 detected, otherwise None
        "pattern_type": str or None,  # one of PNR, PA, PB, PC if detected, otherwise None
        # Trunk group choice (new part of the dict)
        "TB": str or None,  # trunk block if TB0-5 detected, otherwise None
        "TG: str or None, # trunk group if TG0-19 detected, otherwise None
        # Selected frame/trunk/link/level (new part of the dict)
        "FS": str or None, # frame select if FS0-29 detected, otherwise None
        "TS": str or None, # trunk select if TS0-19 detected, otherwise None
        "LC": str or None, # link connector if LC0-9 detected, otherwise None
        "LV": str or None, # level if LV2-9 detected, otherwise None

    '''
    print(">>> evaluating channel/tk punches...")
    result = {
        "channel": None,
        "pattern": None,
        "pattern_type": None,
        "TB": None,
        "TG": None,
        "FS": None,
        "TS": None,
        "LC": None,
        "LV": None,
    }
    cm.set_current_card(card)

    result["channel"] = next((i for i in range(10) if cm.punchValue(f'CH{i}')), None)
    result["pattern"] = next((f'P{i}' for i in range(10) if cm.punchValue(f'P{i}')), None)
    result["pattern_type"] = next((n for n in ('PNR', 'PA', 'PB', 'PC') if cm.punchValue(n)), None)
    result["TB"] = next((f'TB{i}' for i in range(6) if cm.punchValue(f'TB{i}')), None)
    result["TG"] = next((f'TG{i}' for i in range(20) if cm.punchValue(f'TG{i}')), None)
    result["FS"] = next((f'FS{i}' for i in range(30) if cm.punchValue(f'FS{i}')), None)
    result["TS"] = next((f'TS{i}' for i in range(20) if cm.punchValue(f'TS{i}')), None)
    result["LC"] = next((f'LC{i}' for i in range(10) if cm.punchValue(f'LC{i}')), None)
    result["LV"] = next((f'LV{i}' for i in range(2, 10) if cm.punchValue(f'LV{i}')), None)

    return result

def status_flag_getmeta(card, describe: bool = False):
    '''
    Evaluates which status flag is set, if any.

    returns that punch if true
    returns an array containing the punch and its description if describe is true
    returns multiple punches if multiple punches are true
    
    '''
    print(">>> evaluating marker status flags...")
    cm.set_current_card(card)
    names = ['TRS', 'TGT', 'FCG', 'LR', 'DCK', 'GT5', 'SQA']

    status_flags = [n for n in names if cm.punchValue(n)]
    if not status_flags:
        return None

    if describe:
        described_flags = [(n, describe_punch(n)) for n in status_flags]
        return described_flags[0] if len(described_flags) == 1 else described_flags

    return status_flags[0] if len(status_flags) == 1 else status_flags

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
    crosses = []

    crosses = [n for n in names if cm.punchValue(n)]
    if not crosses:
        return None

    if describe:
        described_flags = [(n, describe_punch(n)) for n in crosses]
        return described_flags[0] if len(described_flags) == 1 else described_flags

    return crosses[0] if len(crosses) == 1 else crosses

def ps_getmeta(card, describe: bool = False):
    '''
    Permanent Signal & Partial Dial calls.
    PS or PD punched.
    '''
    # check for PS, PD, PK and bounce out to those handlers if needed
    
    punches = ['PS', 'PD', 'PK'] 

    perm_sig = next((n for n in punches if cm.punchValue(n)), None)

    return (perm_sig, describe_punch(perm_sig)) if describe and perm_sig else perm_sig

def coin_getmeta(card, describe: bool = False):
    '''
    Checks punches related to coin service for payphones.
    SCK and SCN 
    '''
    # check for SCN, SCK, and bounce out to those handlers if needed
    punches = ['SCK', 'SCN']

    see_coin = next((n for n in punches if cm.punchValue(n)), None)

    return (see_coin, describe_punch(see_coin)) if describe and see_coin else see_coin

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
    kind = 'IR' if (cm.punchValue('TER') or cm.punchValue('INC')) else 'OR'
    print(">>> evaluating ", kind, " data...")

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
    errors = []
    seen_zero = False       # True once we hit a completely empty group
    terminated = False      # True once we hit the single-7 marker
    skipped_before = None   # Set once we detect a skipped reed pack

    # we capture the raw reed pack contents as we go so that an exception can
    # report exactly what was seen in each letter.
    registers = {}

    def record_error(msg: str):
        """Record an error message and continue scanning."""
        errors.append(msg)

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
                record_error(f"punches present after termination at {letter}: {punched}")
            continue

        if not punched:
            seen_zero = True
            skipped = letter
            continue

        if seen_zero:
            # we previously saw an empty group, so this is a skipped digit
            record_error(f"skipped digit {skipped}")
            decoded.append("-")
            seen_zero = False

        # check for termination marker (exactly one hole at position 7)
        if punched == [7]:
            terminated = True
            #decoded.append("m7")
            continue

        # normal digit: must be two-of-five
        if len(punched) != 2:
            record_error(
                f"{letter}-group has {len(punched)} punch(es) {punched}; "
                f"exactly two required for a digit, OR {OR_number}")
            continue

        pair = tuple(sorted(punched))
        if pair not in rev:
            # This technically can't even happen??
            record_error(f"invalid two-of-five pair {pair} for {letter}")
            continue
        decoded.append(rev[pair])

    # if we collected digits, we expect a terminator somewhere afterwards
    if decoded and not terminated:
        errors.append("digit sequence not terminated with a 7")

    if errors:
        raise RegCheckError("; ".join(errors),
                           or_number=OR_number,
                           registers=registers, decoded=decoded, kind=kind)

    return decoded, OR_number, kind

def orlm_check(card):
    '''
    Verify that the digits stored in the ORLM are valid 2-of-5

    The originating line location is recorded in the ORLM in reed packs.
    Each *digit* in the line location occupies one reed pack and is
    encoded using the two‑out‑of‑five scheme: exactly two of the positions
    ``0, 1, 2, 4, 7`` must be punched.  The exception to this is the ``FT``
    frame tens digit that is 0,1,2,3, and the ``VF`` digit which is
    0, 1, 2, 3, 4. The following additional constraints are present.

    * reed packs must all be full. Nothing may be omitted.
    * the ``CT`` digit must be 0 (hole at position 0).

    Order of output should always be FT, FU, VG, HG, VF, CT, CU

    Example::

        >>> orlm_check(card)
        [3, 1, 3, 9, 2, 0, 4]
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

    print(">>> evaluating ORLM reed packs...")


    # build reverse lookup: given a pair of positions -> digit
    rev = {tuple(sorted(v)): k for k, v in two_of_five.items()}

    packs = []
    errors = []
    decoded = {"FT": None, "FU": None, "VG": None, "HG": None, "VF": None, "CT": None, "CU": None}

    # we capture the raw reed pack contents as we go so that an exception can
    # report exactly what was seen in each field.
    packs = {}

    def record_error(msg: str):
        """Record an error message and continue scanning."""
        errors.append(msg)

    for k in decoded:
        if k == "CT" or k == "FT" or k == "VF":
            # these have special rules and are not two-of-five, so we check them first

            #FT must always have values 0 + 3
            if k == "FT":
                punched = [pos for pos in [0, 1, 2, 3] if cm.punchValue(f"{k}{pos}")]
                packs[k] = punched.copy()
                if punched != [0, 3]:
                    record_error(f"FT digit must be 0 and 3 (holes at 0 and 3), but found {punched}")
                decoded[k] = sum(punched) # add up the values of punched and store the total in the packs dict for later output
                continue

            # CT simply must be 0, just one punch.
            if k == "CT":
                punched = [pos for pos in [0, 1, 2] if cm.punchValue(f"{k}{pos}")]
                packs[k] = punched.copy()
                if punched != [0]:
                    record_error(f"CT digit must be 0, but found {punched}")
                decoded[k] = sum(punched)
                continue

            # VF must be 0, 1, 2, 3, or 4
            if k == "VF":
                punched = [pos for pos in [0, 1, 2, 3, 4] if cm.punchValue(f"{k}{pos}")]
                packs[k] = punched.copy()
                if punched not in ([0], [1], [2], [3], [4]):
                    record_error(f"VF value must be 0, 1, 2, 3, or 4 (holes at one of positions 0-4), but found {punched}")
                decoded[k] = sum(punched)
                continue
        else:
            # these packs should be 2-of-5
            punched = [pos for pos in [0, 1, 2, 4, 7] if cm.punchValue(f"{k}{pos}")]
            packs[k] = punched.copy()
            if len(punched) != 2:
                record_error(f"{k} field has {len(punched)} punch(es) {punched}; exactly two required for a digit")
                continue
            decoded[k] = rev[tuple(sorted(punched))]

            # maintain standard 5XB ordering for consistency
            desired_order = ['FT', 'FU', 'VG', 'HG', 'VF', 'CT', 'CU']
            decoded = {k: decoded[k] for k in desired_order}

    if errors:
        raise ORLMCheckError("; ".join(errors),
                           packs=packs,
                           decoded=decoded, bin="ORLM_FAILURE")

    return decoded

def os_getmeta(card, outsender=None):
    '''
    Verify punches related to outgoing sender selection. Called only when an OSG0-4 punch is detected.

    * ``OSG0-4`` punches indicate the selected outsender group. One and only one may be punched.
    * ``OS0-4`` punches indicate the selected sender in the group. One and only one may be punched.
    * One and only one of ``SSA`` and ``SSB`` should be punched.
    * Originating line information deposited into the sender must be correct (almost exactly the same as :func:`orlm_check`,
      but with different field names and the additional constraint that the ``OR`` punch must be present to indicate that
      this information is valid at all).

    When valid, this populates and returns an ``outsender`` dict containing
    sender group/number/subgroup metadata.
    '''

    errors = []
    if outsender is None:
        outsender = {}

    if card_has(card, ["OSG0", "OSG1", "OSG2", "OSG3", "OSG4"]):
        # determine group
        for n in ["OSG0", "OSG1", "OSG2", "OSG3", "OSG4"]:
            if cm.punchValue(n):
                outsender["group"] = int(n[3])
                break
        else:
            errors.append("NO_OSG: no OSG punch detected among OSG0-4")

        # determine sender
        for n in ["OS0", "OS1", "OS2", "OS3", "OS4"]:
            if cm.punchValue(n):
                outsender["sender"] = int(n[2])
                break
        else:
            errors.append("NO_OS: no OS punch detected among OS0-4")

        # check SSA/SSB
        if cm.punchValue("SSA") and not cm.punchValue("SSB"):
            outsender["subgroup"] = "SSA"
        elif cm.punchValue("SSB") and not cm.punchValue("SSA"):
            outsender["subgroup"] = "SSB"
        else:
            errors.append(f"invalid subgroup punches: SSA={cm.punchValue('SSA')}, SSB={cm.punchValue('SSB')}")

        if errors:
            raise OSCheckError("; ".join(errors), bin="POSSIBLE_OSC_FAILURE")

    return outsender

def os_reedcheck(card, outsender=None):
    '''
    Verify that the digits stored in the sender reed packs are valid

    On calls requiring an outsender, the originating line location
    is passed to the sender by the marker and stored in the sender's reed packs.
    This info includes both the CLI (calling line identification), and
    the number to be outpulseed. The sender uses CLI for AMA, which itself
    is checked elsewhere.

    If the call is SOG, each digit in the calling line identification portion
    should match what was passed into the CM from the OR. These are all in 2-of-5 format.

    Each *digit* in the CLI (line location) occupies one reed pack and is
    encoded using the two‑out‑of‑five scheme: exactly two of the positions
    ``0, 1, 2, 4, 7`` must be punched.  The exceptions to this are the ``FT``
    frame tens digit that is 0,1,2,3, and the ``VF`` vertical file digit which is
    0, 1, 2, 3, 4.

    The following additional constraints are present.

    * CLI reed packs must all be full. Nothing may be omitted.
    * one and only one of ``OBS`` and ``NOB`` must be punched to indicate
      whether the line is observed or not observed.

    When a valid sequence is present the return value is a list of integers
    corresponding to the decoded line location (terminator excluded).

    Order of output should always be FT', FU', VG', HG', VF, OBS/NOB'

    Example::

        >>> os_reedcheck(card)
        {"CLI_reeds": {"FT'": 3, ...}, "OS_reeds": []}
    '''

    if cm.punchValue("SOG") or cm.punchValue("TOG"): # this function only applicable if call requires a sender

        cm.set_current_card(card)
        if outsender is None:
            outsender = {}

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

        print(">>> evaluating sender reed packs...")

        # build reverse lookup: given a pair of positions -> digit
        rev = {tuple(sorted(v)): k for k, v in two_of_five.items()}

        errors = []
        decoded = {"FT'": None, "FU'": None, "VG'": None, "HG'": None, "VF'": None, "OBS'": None, "NOB'": None}

        # we capture the raw reed pack contents as we go so that an exception can
        # report exactly what was seen in each field.
        packs_calling_line = {}

        def record_error(msg: str):
            """Record an error message and continue scanning."""
            errors.append(msg)

        for k in decoded:
            if k == "OBS'" or k == "NOB'" or k == "FT'" or k == "VF'":
                # these have special rules and are not two-of-five, so we check them first
                if k == "OBS'" or k == "NOB'":
                    obs_punched = cm.punchValue("OBS'")
                    nob_punched = cm.punchValue("NOB'")
                    packs_calling_line["OBS'"] = obs_punched
                    packs_calling_line["NOB'"] = nob_punched
                    if obs_punched and nob_punched:
                        record_error("both OBS' and NOB' punched; exactly one must be punched to indicate observed vs not observed")
                    elif not obs_punched and not nob_punched:
                        record_error("neither OBS' nor NOB' punched; exactly one must be punched to indicate observed vs not observed")
                    else:
                        decoded["OBS'"] = obs_punched
                        decoded["NOB'"] = nob_punched
                    continue

                # FT must always have values 0 + 3
                if k == "FT'":
                    punched = [pos for pos in [0, 1, 2, 3] if cm.punchValue(f"{k}{pos}")]
                    packs_calling_line[k] = punched.copy()
                    if punched != [0, 3]:
                        record_error(f"FT' digit must be 0 and 3 (holes at 0 and 3), but found {punched}")
                    decoded[k] = sum(punched)
                    continue

                # VF must be 0, 1, 2, 3, or 4
                if k == "VF'":
                    punched = [pos for pos in [0, 1, 2, 3, 4] if cm.punchValue(f"{k}{pos}")]
                    packs_calling_line[k] = punched.copy()
                    if punched not in ([0], [1], [2], [3], [4]):
                        record_error(f"VF value must be 0, 1, 2, 3, or 4 (holes at one of positions 0-4), but found {punched}")
                    decoded[k] = sum(punched)
                    continue
            else:
                # these packs should be 2-of-5
                punched = [pos for pos in [0, 1, 2, 4, 7] if cm.punchValue(f"{k}{pos}")]
                packs_calling_line[k] = punched.copy()
                if len(punched) != 2:
                    record_error(f"{k} field has {len(punched)} punch(es) {punched}; exactly two required for a digit")
                    continue
                decoded[k] = rev[tuple(sorted(punched))]

                # maintain standard 5XB ordering for consistency
                # sadly, this is ineffective for raw JSON output
                desired_order = ["FT'", "FU'", "VG'", "HG'", "VF'", "OBS'", "NOB'"]
                decoded = {k: decoded[k] for k in desired_order}

        sender_prime_decoded = None
        # For SOG calls, sender packs A'-H' should carry the register sequence.
        # In practice this should be only an immediate single-7 terminator.
        try:
            register_digits, _, _ = register_check(card)
        except RegCheckError as exc:
            record_error(f"cannot validate A'-H' sender/OR copy because register data is invalid: {exc}")
            register_digits = None

        sender_prime_decoded = []
        packs_outpulse = {}
        sender_prime_seen_zero = False
        sender_prime_terminated = False
        sender_prime_skipped = None

        for letter in "ABCDEFGH":
            group = f"{letter}'"
            punched = [pos for pos in [0, 1, 2, 4, 7] if cm.punchValue(f"{group}{pos}")]
            packs_outpulse[group] = punched.copy()

            if sender_prime_terminated:
                if punched:
                    record_error(f"punches present after sender A'-H' termination at {group}: {punched}")
                continue

            if not punched:
                sender_prime_seen_zero = True
                sender_prime_skipped = group
                continue

            if sender_prime_seen_zero:
                record_error(f"skipped sender A'-H' group {sender_prime_skipped}")
                sender_prime_seen_zero = False

            if punched == [7]:
                sender_prime_terminated = True
                continue

            if len(punched) != 2:
                record_error(
                    f"{group} has {len(punched)} punch(es) {punched}; exactly two required for a digit, or single 7 terminator")
                continue

            pair = tuple(sorted(punched))
            if pair not in rev:
                record_error(f"invalid two-of-five pair {pair} for {group}")
                continue

            sender_prime_decoded.append(rev[pair])

        if sender_prime_decoded and not sender_prime_terminated:
            record_error("sender A'-H' digit sequence must be terminated with a single 7")

        if not sender_prime_terminated:
            record_error("sender H' data must include a single-7 terminator")

        if register_digits is not None and sender_prime_decoded != register_digits:
            record_error(
                f"sender A'-H' decoded digits {sender_prime_decoded} do not match register data {register_digits}")

        if errors:
            raise OSReedCheckError("; ".join(errors),
                            packs_calling_line=packs_calling_line, packs_outpulse=packs_outpulse,
                            decoded=decoded, sender_prime_decoded=sender_prime_decoded, bin="OS_CLI_FAILURE")

        outsender["reeds_calling_line"] = decoded
        outsender["reeds_outpulse"] = sender_prime_decoded
        return outsender

def ng_getmeta(card):
    '''
    Verify punches related to the number group.
    * If RNG detected, get data from NG currently stored in Completing Marker (CM) in fields ``FTT0-5``, ``FUT0-9``,
    ``VGT0-11``, ``HGT0-9``, ``VFT0-4``, ``RCT1-15``
    * One and only one of each of the above may be punched.
    * If ``SNG`` detected, skip the ``FTT-``, ``FUT-``, etc. related tests, and check the ``HN-``, ``T-``, and ``U-`` punches instead.
    * Number group numericals ``HN0-9``, ``T0-9``, ``U0-9`` must correspond to the base-10 values of the
        digits stored in the register reed packs.
    *

    Returns a dictionary containing the decoded number group information when valid, otherwise raises an exception with details about the failure.
    '''

    cm.set_current_card(card)
    print(">>> evaluating number group punches...")

    if card_has(card, "NGK1"):
        # we should have a translation. check the values transmitted to the CM
        ng_fields = {
            "FTT": [f"FTT{i}" for i in range(6)],
            "FUT": [f"FUT{i}" for i in range(10)],
            "VGT": [f"VGT{i}" for i in range(12)],
            "HGT": [f"HGT{i}" for i in range(10)],
            "VFT": [f"VFT{i}" for i in range(5)],
            "RCT": [f"RCT{i}" for i in range(1, 16)],
        }

        observed = {}
        errors = []

        for prefix, names in ng_fields.items():
            punched = [n for n in names if cm.punchValue(n)]
            if len(punched) == 1:
                observed[prefix] = punched[0][len(prefix):]
            elif len(punched) == 0:
                errors.append(f"no {prefix} punch detected")
                observed[prefix] = None
            else:
                errors.append(f"multiple {prefix} punches found: {punched}")
                observed[prefix] = punched

        if errors:
            raise NumberGroupCheckError(
                "; ".join(errors),
                details={"observed": observed},
            )
        return observed

    if card_has(card, "SNG"):
        # If number group has been seized but not released, we should check these active punches.
        # H,T,U punches should correspond to the digits stored in the register reed packs.
        try:
            register_digits, reg_number, kind = register_check(card)
        except RegCheckError as exc:
            raise NumberGroupCheckError(
                "cannot validate number group because register data is invalid",
                details={
                    "register_error": str(exc),
                    "registers": exc.registers,
                    "decoded": exc.decoded,
                    "kind": exc.kind,
                },
            ) from exc

        expected = {
            "HN": register_digits[-3] if len(register_digits) >= 3 else None,
            "T": register_digits[-2] if len(register_digits) >= 2 else None,
            "U": register_digits[-1] if len(register_digits) >= 1 else None,
        }
        observed = {}
        errors = []
        for prefix in ("HN", "T", "U"):
            punched = [i for i in range(10) if cm.punchValue(f"{prefix}{i}")]
            if len(punched) == 1:
                observed[prefix] = punched[0]
            if len(punched) > 1:
                observed[prefix] = punched
                errors.append(f"multiple punches found for {prefix}: {punched}")
            if len(punched) == 0:
                observed[prefix] = None
            want = expected[prefix]

            if want is None:
                if punched:
                    errors.append(f"{prefix} should be blank but found {observed[prefix]}")
                continue

            if observed[prefix] != want:
                errors.append(f"{prefix} expected {want} but found {observed[prefix]}")

        if errors:
            raise NumberGroupCheckError(
                "; ".join(errors),
                details={
                    "expected": expected,
                    "observed": observed,
                },
            )

        return observed

def cm_check(card):
    """Evaluates a whole bunch of things to ensure that the completing marker's operation is sane.
    Source: BSP 218-404-50_ and various 5XB troubleshooting books

    Checks below are listed in the same order as the function body.

    # Number group registration checks
    * If SNG then must have NGK: raise NO_NGK
    * If NGK then must have HTUK: raise NO_HTUK
    * If HTUK and WT: raise WT_WHILE_IN_NG
    * If FLG and SNG then must have RNG: raise SNG_NO_RNG

    # TER calls
    * If TER or TOG then must have FLG: raise NO_FLG
    * If TER then must have TF4 and TF7: raise INC_NO_TF
    * If TER and (BY or OV or OFH) then must have RS9: raise NO_RS9
    * If RCT1-9 then must have RSK: raise NO_RSK
    * If TER and BY then must have RS1: raise BY_NO_RS1
    * If TER and OV then must have RS0: raise OV_NO_RS0
    * If TER and RS9 then must have RSK: raise NO_RSK
    * If TER and RCK2 then must have RCK3: raise NO_RCK3
    * If TER and RSK then must have SRK: raise NO_SRK
    * If TER and SRK then must have LI: raise SRK_NO_LI
    * If TER and LI then must have DIS1: raise TER_NO_DIS1

    # Double Connection Tests
    * If GT2 or AVK1 or RCK3 or CLK then must have DCT1: raise NO_DCT1
    * If RCK3 and not DCT1 then must have DCT: raise TER_NO_DCT
    * If DCT1 then must have DIS1 and must not have DCT: raise DCT1_NO_DIS1
    * If DCT1 then must have LK1: raise NO_LK1
    * If (DCT1 and LK1) or DCT2 or LK1 then must have DIS1: raise NO_DIS1

    # TLF checks
    * If LV2-9 then must have FAK or FBK: raise NO_FAK_FBK
    * If FUT0-9 or JG0-4 and both LK and RK operate: raise LK_RK_CONFLICT
    * If (not TER) and MAK1 then must have one and only one TS0-19: raise NO_TS
    * If TS0-19 then must have one and only one LV2-9: raise NO_LV
    * If LV2-9 then must have one and only one LC0-9: raise NO_LC
    * If LC0-9 then must have LCK: raise NO_LCK

    # Crosspoint checks
    * If no HMS1 then must not have SL: raise FALSE_SL
    * If no HTR and no HMS1 then must not have JXP1 or LXP1: raise FALSE_JXP1_LXP1
    * If HMS1 then must have SL: raise NO_SL
    * If JXP1 then must have LXP1: raise NO_LXP1
    * If SL then must have JXP1: raise NO_JXP1
    * If SL and JXP1 and LXP1 then must have GT2: raise NO_GT2
    * If CH0-9 then must have HMS1: raise NO_HMS1
    * If JC0-9 then must have JCK: raise NO_JCK
    * If (not TER) and (P0-9 or PNR or PA or PB or PC or PE) then must have TCHK: raise NO_TCHK

    # IRL LR Checks
    * If LR and no DCK: raise LR_INC_XPTS
    * If LR and DCK and one of INC, TOL, TAN: raise LR_FAILURE_TO_ATTACH
    * If LR and DCK then must have one of INC, TOL, TAN: raise LR_NOCLASS
    * If LR then must have LV2-9: raise LR_NO_TRUNK

    # Outgoing calls with sender
    * If OSG0-4 then must have SOG: raise NO_SOG
    * If SOG then must have OSK: raise NO_OSK
    * If OSK then must have SLK2: raise NO_SLK2
    * If OS0-4 then must have RSC: raise NO_RSC
    * If TI and RSC and SLK2 then must have AVK1: raise NO_AVK1
    * If LT1 then must have AMA: raise NO_AMA
    * If TGT: raise TG_FAIL

    # Barebones checks if all others fall thru
    * If FLG then must have JCK: raise NO_JCK
    * If FLG then must have LCK: raise NO_LCK
    * If FLG then must have HGK: raise NO_HGK
    * If FLG then must have TCHK: raise NO_TCHK
    * If FLG then must have LK or RK: raise NO_LK_RK
    * If FLG then must have RK3: raise NO_RK3
    * If FLG and JCK and LCK and HGK and TCHK and RK3 and (LK or RK) then must have TK: raise NO_TK
    * If SCB then must have FAK: raise NO_FAK
    * If SCB then must have LCK: raise NO_LCK
    * If SCB then must have JCK: raise NO_JCK
    * If SCB then must have DTK: raise NO_DTK
    * If SCB then must have HGK: raise NO_HGK
    * If SCB then must have RK3: raise NO_RK3
    * If SCB and FAK and LFK and LCK and JCK and HGK and RK3 then must have TK: raise NO_TK
    * If FLG and HGK and JCK and TCHK and LCK and (FAK or FBK) then must have TK: raise NO_TK
    * If TK then must have HMS1: raise NO_HMS1
    * If HMS1 then must have DCT1: raise NO_DCT1
    * If TK then must have CK: raise NO_CK
    * If TI and one of (SOG, ITR, TOG, NSO) then must have one and only one TG0-19: raise NO_TG
    * If TI and one of (SOG, ITR, TOG, NSO) then must have one and only one TB0-5: raise NO_TB
    * If TI and one of (SOG, ITR, TOG, NSO) and TB0-4 then must have one and only one TS0-19: raise NO_TS
    * If TI and one of (SOG, ITR, TOG, NSO) and TB0-5 then must have one and only one FS0-29: raise NO_FS
    * If FS0 then must have FTCK: raise NO_FTCK
    * If LK1 then must have SCB: raise NO_SCB
    * If FLG and LB then must have BY or OV: raise NO_BY_OV
    * If TM and CKG then must have TK: raise NO_TK
    * If TM and CKG and TSE: raise TSE_NO_TRUNK
    """

    cm.set_current_card(card)

    lv_punches = [f"LV{i}" for i in range(2, 10)]
    fut_punches = [f"FUT{i}" for i in range(10)]
    jg_0_4_punches = [f"JG{i}" for i in range(5)]
    ch_punches = [f"CH{i}" for i in range(10)]
    jc_punches = [f"JC{i}" for i in range(10)]
    p_punches = [f"P{i}" for i in range(10)]
    lc_punches = [f"LC{i}" for i in range(10)]
    osg_punches = [f"OSG{i}" for i in range(5)]
    tb_0_5_punches = [f"TB{i}" for i in range(6)]
    tg_0_19_punches = [f"TG{i}" for i in range(20)]
    ts_punches = [f"TS{i}" for i in range(20)]
    fs_punches = [f"FS{i}" for i in range(30)]
    jg_0_4_punches = [f"JG{i}" for i in range(5)]
    rs_0_1_punches = ["RS0", "RS1"]
    rs_2_9_punches = [f"RS{i}" for i in range(2, 10)]
    rs_all_punches = rs_0_1_punches + rs_2_9_punches
    os_0_4_punches = [f"OS{i}" for i in range(5)]
    rct_punches = [f"RCT{i}" for i in range(1, 10)]

    def found(names):
        return [name for name in names if card_has(card, name)]

    def found_count(names):
        return len(found(names))

    def raise_cm_error(code, message, required=None, trigger=None, context=None, requirement="all", bin="yellow"):
        required = list(required or [])
        trigger = list(trigger or [])
        context = list(context or [])
        checked = []
        for name in trigger + required + context:
            if name not in checked:
                checked.append(name)
        details = {
            "required": required,
            "found": found(checked),
            "missing": [name for name in required if card_lacks(card, name)],
        }
        if trigger:
            details["triggered_by"] = found(trigger)
        if requirement != "all":
            details["requirement"] = requirement
        raise CMCheckError(message, code=code, details=details, bin=bin)

    # --- Number group registration checks ---
    if card_has(card, "SNG") and card_lacks(card, "NGK"):
        raise_cm_error("NO_NGK", "marker timed out while attemptime to seize number group", required=["NGK"], trigger=["SNG"], bin="NG_FAILURE")

    if card_has(card, "NGK") and card_lacks(card, "HTUK"):
        raise_cm_error("NO_HTUK", "number group seized, but one or more "
                        "H T U relays failed to operate", required=["HTUK"], trigger=["NGK"], bin="NG_FAILURE")

    if card_has_all(card, "HTUK", "WT"):
        raise_cm_error("WT_WHILE_IN_NG", "WT timed out while recording called "
        "line information from number group", trigger=["HTUK", "WT"], bin="NG_FAILURE")

    if card_has_all(card, "FLG", "SNG") and card_lacks(card, "RNG"):
        raise_cm_error("SNG_NO_RNG", "FLG with SNG requires RNG",
                       required=["RNG"], trigger=["FLG", "SNG"], bin="NG_FAILURE")

    # --- TER calls ---
    if card_has(card, ["TER", "TOG"]) and card_lacks(card, "FLG"):
        raise_cm_error("NO_FLG", "TER or TOG requires FLG", required=["FLG"], trigger=["TER", "TOG"], bin="NO_FLG")

    if card_has(card, "TER") and not card_has_all(card, "TF4", "TF7"):
        raise_cm_error("INC_NO_TF", "TLF indication not recorded in IR or CM", required=["TF4", "TF7"], trigger=["TER"], bin="INC_NO_TF")

    if card_has(card, "TER") and card_has(card, ["BY", "OV", "OFH"]) and card_lacks(card, "RS9"):
        raise_cm_error("NO_RS9", "horizontal 9 in the Ringing Selection Switch failed to operate",
                       required=["RS9"], trigger=["TER", "BY", "OV", "OFH"], bin="NO_RS9")

    if card_has(card, rct_punches) and card_lacks(card, "RSK"):
        raise_cm_error("NO_RSK", "RCT1-9 requires RSK",
                       required=["RSK"], trigger=rct_punches, bin="NO_RSK")

    if card_has_all(card, "TER", "BY") and card_lacks(card, "RS1"):
        raise_cm_error("BY_NO_RS1", "horizontal 1 in the Ringing Selection Switch failed to operate",
                       required=["RS1"], trigger=["TER", "BY"], bin="BY_NO_RS1")

    if card_has_all(card, "TER", "OV") and card_lacks(card, "RS0"):
        raise_cm_error("OV_NO_RS0", "horizontal 0 in the Ringing Selection Switch failed to operate",
                       required=["RS0"], trigger=["TER", "OV"], bin="OV_NO_RS0")

    if card_has_all(card, "TER", "RS9") and card_lacks(card, "RSK"):
        raise_cm_error("NO_RSK", "TER with RS9 requires RSK",
                       required=["RSK"], trigger=["TER", "RS9"], bin="RSS_CHECK")

    if card_has_all(card, "TER", "RCK2") and card_lacks(card, "RCK3"):
        raise_cm_error("NO_RCK3", "TER with RCK2 requires RCK3",
                       required=["RCK3"], trigger=["TER", "RCK2"], bin="RSS_CHECK")

    if card_has_all(card, "TER", "RSK") and card_lacks(card, "SRK"):
        raise_cm_error("NO_SRK", "TER with RSK requires SRK",
                       required=["SRK"], trigger=["TER", "RSK"], bin="RSS_CHECK")

    if card_has_all(card, "TER", "SRK") and card_lacks(card, "LI"):
        raise_cm_error("SRK_NO_LI", "TER with SRK requires LI", required=["LI"], trigger=["TER", "SRK"], bin="RSS_CHECK")

    if card_has_all(card, "TER", "LI") and card_lacks(card, "DIS1"):
        raise_cm_error("TER_NO_DIS1", "TER with LI requires DIS1. "
        "Possible RSS failure?", required=["DIS1"], trigger=["TER", "LI"], bin="TER_NO_DIS1")

    # --- Double Connection Tests ---
    if card_has(card, ["GT2", "AVK1", "RCK3", "CLK"]) and card_lacks(card, "DCT1"):
        raise_cm_error("NO_DCT1", "GT2, AVK1, RCK3, or CLK requires DCT1",
                       required=["DCT1"], trigger=["GT2", "AVK1", "RCK3", "CLK"], bin="DCT_FAILURES")

    if card_has(card, "RCK3") and card_lacks(card, "DCT1") and card_lacks(card, "DCT"):
        raise_cm_error("TER_NO_DCT", "RCK3 without DCT1 requires DCT",
                       required=["DCT"], trigger=["RCK3"], context=["DCT1"], bin="DCT_FAILURES")

    if card_has(card, "DCT1") and (card_has(card, "DCT") or card_lacks(card, "DIS1")):
        raise_cm_error("DCT1_NO_DIS1", "DCT1 must have DIS1 and must not have DCT",
                       required=["DIS1"], trigger=["DCT1"], context=["DCT"], bin="DCT_FAILURES")

    if card_has(card, "DCT1") and card_lacks(card, "LK1"):
        raise_cm_error("NO_LK1", "DCT1 is punched without LK1", required=["LK1"], trigger=["DCT1"], bin="DCT_FAILURES")

    if (card_has_all(card, "DCT1", "LK1") or card_has(card, ["DCT2", "LK1"])) and card_lacks(card, "DIS1"):
        raise_cm_error("NO_DIS1", "DCT/LK combination requires DIS1",
                       required=["DIS1"], trigger=["DCT1", "DCT2", "LK1"], bin="NO_DIS1")

    # --- TLF checks ---
    if card_has(card, lv_punches) and card_lacks(card, ["FAK", "FBK"]):
        raise_cm_error("NO_FAK_FBK", "LV2-9 requires FAK or FBK",
                       required=["FAK", "FBK"], trigger=lv_punches, requirement="any", bin="NO_FAK_FBK")

    if card_has(card, fut_punches + jg_0_4_punches):
        lk_rk_found = found(["LK", "RK"])
        if len(lk_rk_found) != 0 and len(lk_rk_found) != 1:
            raise_cm_error("LK_RK_CONFLICT", "FUT-/JG- requires zero or one (but not both) of LK or RK",
                           required=["LK", "RK"], trigger=fut_punches + jg_0_4_punches,
                           context=["LK", "RK"], requirement="exactly_one", bin="LK_RK_CONFLICT")

    if card_lacks(card, "TER") and card_has(card, "MAK1") and found_count(ts_punches) != 1:
        raise_cm_error("NO_TS", "MAK1 requires one and only one TS0-19",
                       trigger=["MAK1"], context=ts_punches, requirement="exactly_one", bin="INV_TS")

    if card_has(card, ts_punches) and found_count(lv_punches) != 1:
        raise_cm_error("NO_LV", "TS0-19 requires one and only one LV2-9",
                       trigger=ts_punches, context=lv_punches, requirement="exactly_one", bin="INV_LV")

    if card_has(card, lv_punches) and found_count(lc_punches) != 1:
        raise_cm_error("NO_LC", "LV2-9 requires one and only one LC0-9",
                       trigger=lv_punches, context=lc_punches, requirement="exactly_one", bin="INV_LC")

    if card_has(card, lc_punches) and card_lacks(card, "LCK"):
        raise_cm_error("NO_LCK", "LC0-9 requires LCK", required=["LCK"], trigger=lc_punches, bin="NO_LCK")

    # --- Crosspoint checks ---
    if card_lacks(card, "HMS1") and card_has(card, "SL"):
        raise_cm_error("FALSE_SL", "SL is punched without HMS1",
                       required=["HMS1"], trigger=["SL"], bin="XPT_CHECK")

    if card_lacks(card, "HTR", "HMS1") and card_has(card, ["JXP1", "LXP1"]):
        raise_cm_error("FALSE_JXP1_LXP1", "JXP1/LXP1 punched without HMS1",
                       required=["HMS1"], trigger=["JXP1", "LXP1"], bin="XPT_CHECK")

    if card_has(card, "HMS1") and card_lacks(card, "SL"):
        raise_cm_error("NO_SL", "HMS1 is punched without SL", required=["SL"], trigger=["HMS1"], bin="XPT_CHECK")

    if card_has(card, "JXP1") and card_lacks(card, "LXP1"):
        raise_cm_error("NO_LXP1", "JXP1 is punched without LXP1", required=["LXP1"], trigger=["JXP1"], bin="XPT_CHECK")

    if card_has(card, "SL") and card_lacks(card, "JXP1"):
        raise_cm_error("NO_JXP1", "SL is punched without JXP1", required=["JXP1"], trigger=["SL"], bin="XPT_CHECK")

    if card_has_all(card, "SL", "JXP1", "LXP1") and card_lacks(card, "GT2"):
        raise_cm_error("NO_GT2", "SL/JXP1/LXP1 combination requires GT2",
                       required=["GT2"], trigger=["SL", "JXP1", "LXP1"], bin="XPT_CHECK")

    if card_has(card, ch_punches) and card_lacks(card, "HMS1"):
        raise_cm_error("NO_HMS1", "CH0-9 requires HMS1", required=["HMS1"], trigger=ch_punches, bin="XPT_CHECK")

    if card_has(card, jc_punches) and card_lacks(card, "JCK"):
        raise_cm_error("NO_JCK", "JC0-9 requires JCK", required=["JCK"], trigger=jc_punches, bin="XPT_CHECK")

    if card_lacks(card, "TER") and card_has(card, p_punches + ["PNR", "PA", "PB", "PC", "PE"]) and card_lacks(card, "TCHK"):
        raise_cm_error("NO_TCHK", "P/PNR/PA/PB/PC/PE activity requires TCHK",
                       required=["TCHK"], trigger=p_punches + ["PNR", "PA", "PB", "PC", "PE"], bin="XPT_CHECK")

    # --- IRL LR Checks ---
    if card_has(card, "LR") and card_lacks(card, "DCK"):
        raise_cm_error("LR_INC_XPTS", "LR is punched without DCK",
                       required=["DCK"], trigger=["LR"], bin="IRL_FAILURE")

    if card_has_all(card, "LR", "DCK") and card_has(card, ["INC", "TOL", "TAN"]):
        raise_cm_error("LR_FAILURE_TO_ATTACH", "LR and DCK indicates possible double connection in IRL",
                       required=["INC", "TOL", "TAN"], trigger=["LR", "DCK"], requirement="any", bin="IRL_FAILURE")

    if card_has_all(card, "LR", "DCK") and card_lacks(card, ["INC", "TOL", "TAN"]):
        raise_cm_error("LR_NOCLASS", "LR with DCK requires INC, TOL, or TAN",
                       required=["INC", "TOL", "TAN"], trigger=["LR", "DCK"], requirement="any", bin="IRL_FAILURE")

    if card_has(card, "LR") and card_lacks(card, lv_punches):
        raise_cm_error("LR_NO_TRUNK", "LR requires one of LV2-9",
                       required=lv_punches, trigger=["LR"], requirement="any", bin="IRL_FAILURE")

    # --- Outgoing calls with sender ---
    if card_has(card, osg_punches) and card_lacks(card, "SOG"):
        raise_cm_error("NO_SOG", "OSG0-4 requires SOG", required=["SOG"], trigger=osg_punches, bin="SENDER_ATTACH_FAILURE")

    if card_has(card, "SOG") and card_lacks(card, "OSK"):
        raise_cm_error("NO_OSK", "SOG is punched without OSK", required=["OSK"], trigger=["SOG"], bin="SENDER_ATTACH_FAILURE")

    if card_has(card, "OSK") and card_lacks(card, "SLK2"):
        raise_cm_error("NO_SLK2", "OSK is punched without SLK2", required=["SLK2"], trigger=["OSK"], bin="SENDER_ATTACH_FAILURE")

    if card_has(card, os_0_4_punches) and card_lacks(card, "RSC"):
        raise_cm_error("NO_RSC", "OS0-4 requires RSC", required=["RSC"], trigger=os_0_4_punches, bin="SENDER_ATTACH_FAILURE")

    if card_has_all(card, "TI", "RSC", "SLK2") and card_lacks(card, "AVK1"):
        raise_cm_error("NO_AVK1", "sender unable to operate its AV relay, thus no AVK1",
                       required=["AVK1"], trigger=["TI", "RSC", "SLK2"], bin="NO_AVK1")

    if card_has(card, "LT1") and card_lacks(card, "AMA"):
        raise_cm_error("NO_AMA", "calls to kercheep require AMA", required=["AMA"], trigger=["LT1"], bin="NO_AMA")

    if card_has(card, "TGT"):
        raise_cm_error("TG_FAIL", "sender failed to complete TG test in allotted time. "
                        "suspect OGT trouble", trigger=["TGT"], bin="OGT_ISSUE")

    # --- Barebones checks if all others fall thru ---
    if card_has(card, "FLG") and card_lacks(card, "JCK"):
        raise_cm_error("NO_JCK", "FLG requires JCK", required=["JCK"], trigger=["FLG"], bin="XPT_CHECK")

    if card_has(card, "FLG") and card_lacks(card, "LCK"):
        raise_cm_error("NO_LCK", "FLG requires LCK", required=["LCK"], trigger=["FLG"], bin="XPT_CHECK")

    if card_has(card, "FLG") and card_lacks(card, "HGK"):
        raise_cm_error("NO_HGK", "FLG requires HGK", required=["HGK"], trigger=["FLG"], bin="XPT_CHECK")

    if card_has(card, "FLG") and card_lacks(card, "TCHK"):
        raise_cm_error("NO_TCHK", "FLG requires TCHK", required=["TCHK"], trigger=["FLG"], bin="XPT_CHECK")

    if card_has(card, "FLG") and card_lacks(card, ["LK", "RK"]):
        raise_cm_error("NO_LK_RK", "FLG requires LK or RK", required=["LK", "RK"], trigger=["FLG"], requirement="any", bin="XPT_CHECK")

    if card_has(card, "FLG") and card_lacks(card, "RK3"):
        raise_cm_error("NO_RK3", "FLG requires RK3", required=["RK3"], trigger=["FLG"], bin="XPT_CHECK")

    if card_has_all(card, "FLG", "JCK", "LCK", "HGK", "TCHK", "RK3") and card_has(card, ["LK", "RK"]) and card_lacks(card, "TK"):
        raise_cm_error("NO_TK", "TK failed to operate when it should have on FLG",
                       required=["TK"], trigger=["FLG", "JCK", "LCK", "HGK", "TCHK", "RK3"], context=["LK", "RK"], bin="NO_TK")

    if card_has(card, "SCB") and card_lacks(card, "FAK"):
        raise_cm_error("NO_FAK", "SCB requires FAK", required=["FAK"], trigger=["SCB"], bin="TLF_NO_FAK")

    if card_has(card, "SCB") and card_lacks(card, "LCK"):
        raise_cm_error("NO_LCK", "SCB requires LCK", required=["LCK"], trigger=["SCB"], bin="XPT_CHECK")

    if card_has(card, "SCB") and card_lacks(card, "JCK"):
        raise_cm_error("NO_JCK", "SCB requires JCK", required=["JCK"], trigger=["SCB"], bin="XPT_CHECK")

    if card_has(card, "SCB") and card_lacks(card, "DTK"):
        raise_cm_error("NO_DTK", "SCB requires DTK", required=["DTK"], trigger=["SCB"], bin="XPT_CHECK")

    if card_has(card, "SCB") and card_lacks(card, "HGK"):
        raise_cm_error("NO_HGK", "SCB requires HGK", required=["HGK"], trigger=["SCB"], bin="XPT_CHECK")

    if card_has(card, "SCB") and card_lacks(card, "RK3"):
        raise_cm_error("NO_RK3", "SCB requires RK3", required=["RK3"], trigger=["SCB"], bin="XPT_CHECK")

    if card_has_all(card, "SCB", "FAK", "LFK", "LCK", "JCK", "HGK", "RK3") and card_lacks(card, "TK"):
        raise_cm_error("NO_TK", "TK failed to operate when it should have on SCB linkage",
                       required=["TK"], trigger=["SCB", "FAK", "LCK", "JCK", "DTK", "HGK", "RK3"], bin="NO_TK")

    if card_has_all(card, "FLG", "HGK", "JCK", "TCHK", "LCK") and card_has(card, ["FAK", "FBK"]) and card_lacks(card, "TK"):
        raise_cm_error("NO_TK", "TK failed to operate when it should have on FLG linkage",
                       required=["TK"], trigger=["HGK", "JCK", "TCHK", "LCK", "FAK", "FBK"], bin="NO_TK")

    if card_has(card, "TK") and card_lacks(card, "HMS1"):
        raise_cm_error("NO_HMS1", "TK is punched without HMS1", required=["HMS1"], trigger=["TK"], bin="NO_HMS1")

    if card_has(card, "HMS1") and card_lacks(card, "DCT1"):
        raise_cm_error("NO_DCT1", "HMS1 is punched without DCT1", required=["DCT1"], trigger=["HMS1"], bin="DCT_FAILURE")

    if card_has(card, "TK") and card_lacks(card, "CK"):
        raise_cm_error("NO_CK", "TK is punched without CK", required=["CK"], trigger=["TK"], bin="NO_CK")

    if card_has(card, "TI") and card_has(card, ["SOG", "ITR", "TOG", "NSO"]) and found_count(tg_0_19_punches) != 1:
        raise_cm_error("NO_TG", "SOG/ITR/TOG/NSO requires one and only one TG0-19",
                       trigger=["TI", "SOG", "ITR", "TOG", "NSO"], context=tg_0_19_punches, requirement="exactly_one", bin="INV_TG")

    if card_has(card, "TI") and card_has(card, ["SOG", "ITR", "TOG", "NSO"]) and found_count(tb_0_5_punches) != 1:
        raise_cm_error("NO_TB", "TI with SOG/ITR/TOG/NSO requires one and only one TB0-5",
                       trigger=["TI", "SOG", "ITR", "TOG", "NSO"], context=tb_0_5_punches, requirement="exactly_one", bin="INV_TB")

    if card_has(card, "TI") and card_has(card, ["SOG", "ITR", "TOG", "NSO"]) and card_has(card, tb_0_4_punches) and found_count(ts_punches) != 1:
        raise_cm_error("NO_TS", "TI with SOG/ITR/TOG/NSO and TB0-4 requires one and only one TS0-19",
                       trigger=["TI", "SOG", "ITR", "TOG", "NSO"] + tb_0_4_punches, context=ts_punches, requirement="exactly_one", bin="INV_TS")

    if card_has(card, "TI") and card_has(card, ["SOG", "ITR", "TOG", "NSO"]) and card_has(card, tb_0_5_punches) and found_count(fs_punches) != 1:
        raise_cm_error("NO_FS", "TI with SOG/ITR/TOG/NSO and TB0-5 requires one and only one FS0-29",
                       trigger=["TI", "SOG", "ITR", "TOG", "NSO"] + tb_0_5_punches, context=fs_punches, requirement="exactly_one", bin="INV_FS")

    if card_has(card, "FS0") and card_lacks(card, "FTCK"):
        raise_cm_error("NO_FTCK", "FS0 is punched without FTCK", required=["FTCK"], trigger=["FS0"], bin="NO_FTCK")

    if card_has(card, "LK1") and card_lacks(card, "SCB"):
        raise_cm_error("NO_SCB", "when LK1 is punched, the marker should be ready to Start Call Back (SCB)", required=["SCB"], trigger=["LK1"], bin="NO_SCB")

    if card_has_all(card, "FLG", "LB") and card_lacks(card, ["BY", "OV"]):
        raise_cm_error("NO_BY_OV", "FLG and LB requires BY or OV",
                       required=["BY", "OV"], trigger=["FLG", "LB"], requirement="any", bin="LB_BY_OV_FAIL")

    if card_has_all(card, ["TM", "CKG"]) and card_lacks(card, "TK"):
        raise_cm_error("FALLTHROUGH", "TK check fallthrough. Please examine card and create a bin for this",
                       required=["TK"], trigger=["FLG", "LB"], bin="NO_TK")

    if card_has_all(card, "TM", "CKG", "TSE"):
        raise_cm_error("TSE_NO_TRUNK", "TSE indicates marker unable to complete trunk selection. Probable translation or route relay failure.",
                       trigger=["TM", "CKG"], context=["TSE"], bin="TSE_NO_TRUNK")

    return {"ok": True}

def evaluate(card, describe: bool = False):
    """Evaluate a card and return a serializable metadata dict.

    This is useful for generating reports and persisting results.
    """
    cm.set_current_card(card)

    meta = {
        "type": type_of_card(card, describe),                       # does not bin, binned below
        "coin": coin_getmeta(card, describe),
        "marker": marker_no(card, describe),
        "channel": ch_tk_getmeta(card, describe),
        "trial": trial_getmeta(card, describe),
        "timer": timer_getmeta(card, describe),
        "status_flag": status_flag_getmeta(card, describe),
        "register": {"number": None, "digits": None, "kind": None}, # checked and binned below
        "perm_sig": ps_getmeta(card),
        "crosses": [],                                              # checked and binned below
        "bin": "unbinned",                                          # default bin, updated as checks are performed
    }

    def set_bin_if_unbinned(bin_name):
        if bin_name and meta.get("bin") == "unbinned":
            meta["bin"] = bin_name

    if meta["type"][0] in ("MTPT", "SRT", "TKT", "MLV"):
        set_bin_if_unbinned("TEST_CARD")

    # Cross check supersedes all other bins, so run this first.
    meta["crosses"] = x_check(card)
    if meta["crosses"]:
        set_bin_if_unbinned("X_INDICATION")

    # Register check + binning
    try:
        decoded, reg_number, kind = register_check(card)
        meta["register"] = {"number": reg_number, "digits": decoded, "kind": kind}
    except RegCheckError as exc:
        meta["register"] = {
            "error": str(exc),
            "or_number": exc.or_number,
            "registers": exc.registers,
            "kind": exc.kind,
        }
        set_bin_if_unbinned("REG_ERROR")

    # ORLM check + binning
    if meta["register"].get("kind") == "OR":
        try:
            orlm_decoded = orlm_check(card)
            meta["orlm"] = orlm_decoded
        except ORLMCheckError as exc:
            meta["orlm"] = {
                "error": str(exc),
                "packs": exc.packs,
                "decoded": exc.decoded,
            }
            set_bin_if_unbinned("ORLM_ERROR")

    # OS check + binning
    if card_has(card, ["SON"]):
        outsender = {}
        try:
            outsender = os_getmeta(card, outsender)
        except OSCheckError as exc:
            outsender["os_getmeta"] = {
                "error": str(exc),
                "details": exc.details,
            }
        try:
            outsender = os_reedcheck(card, outsender)
        except OSReedCheckError as exc:
            outsender["os_reed_check"] = {
                "error": str(exc),
                "packs_outpulse": exc.packs_outpulse or {},
                "packs_calling_line": exc.packs_calling_line or {},
                "decoded": exc.decoded,
                "sender_prime_decoded": exc.sender_prime_decoded,
                "bin": exc.bin,
            }

        meta["outsender"] = outsender
        set_bin_if_unbinned(outsender.get("os_reed_check", {}).get("bin") or outsender.get("os_getmeta", {}).get("bin"))

    # Number Group check. Binning for errors here is done in func:`cm_check()`, since we can get
    # better granularity on the failure mode there.
    try:
        number_group = ng_getmeta(card)
        meta["number_group"] = number_group
    except NumberGroupCheckError as exc:
        meta["number_group"] = {
            "error": str(exc),
            "details": exc.details,
        }

    # Completing Marker check + binning
    if card_has(card, "TI"):
        try:
            cm_check_result = cm_check(card)
            meta["cm_check"] = cm_check_result
        except CMCheckError as exc:
            meta["cm_check"] = {
                "error": str(exc),
                "code": exc.code,
                "details": exc.details,
            }
            set_bin_if_unbinned(exc.bin)

    meta["punches"] = truthy_punches(card)


    for k in meta:
        print(meta[k])

    return meta



# ---------------------------------------------------------------------------
# helper routines for binning/sorting by punches
# ---------------------------------------------------------------------------

def card_has_all(card, *names):
    """Return ``True`` if *card* has **all** of the punches in *names*.

    *names* may be provided as a series of positional arguments (``card_has_all(card, "TI", "MOR")``)
    or as a single iterable list/tuple/set (``card_has_all(card, ["TI", "MOR"])``).

    The card is activated for each lookup automatically.
    """
    cm.set_current_card(card)
    if len(names) == 1 and isinstance(names[0], (list, tuple, set)):
        names = names[0]
    return all(cm.punchValue(n) for n in names)

def card_has(card, *names):
    """Return ``True`` if *card* has any of the punches in *names*.

    *names* may be provided as a series of positional arguments (``card_has(card, "TI", "MOR")``)
    or as a single iterable list (``card_has(card, ["TI", "MOR"])``).

    The card is activated for each lookup automatically.
    """
    cm.set_current_card(card)
    if len(names) == 1 and isinstance(names[0], (list, tuple, set)):
        names = names[0]
    return any(cm.punchValue(n) for n in names)

def card_lacks(card, *names):
    """Return ``True`` if *card* has **none** of the punches in *names*."""
    cm.set_current_card(card)
    if len(names) == 1 and isinstance(names[0], (list, tuple, set)):
        names = names[0]
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
            ("or_error", lambda c: card_has(c, "OR") and card_lacks(c, "CN-RG0")),
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
# helpful functions that are friendly and helpful to callers
# ---------------------------------------------------------------------------

def describe_punch(name):
    # Shorthand for clients that don't feel like importing the module
    return pd.describe(name)

def truthy_punches(card):
    """Return a list of punch names that are present (True) on the card."""
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
    examined.
    """

    def __init__(self, message, or_number=None, registers=None, decoded=None, kind=None):
        super().__init__(message)
        self.or_number = or_number
        # ``registers`` is a dict mapping letter names (``'A'``..``'L'``) to the
        # list of punched positions seen in that group.  It is populated as the
        # check iterates through the letters so that even if an error occurs we
        # still have the state up through the failure point.
        self.registers = registers or {}
        self.decoded = decoded
        self.kind = kind

class ORLMCheckError(ValueError):
    """Raised when ``orlm_check`` encounters malformed data.

    The exception carries attributes that make it possible for callers to
    inspect the OR number and the raw contents of the letter groups that were
    examined.
    """

    def __init__(self, message, packs=None, decoded=None):
        super().__init__(message)
        self.packs = packs or {}
        self.decoded = decoded

class OSReedCheckError(ValueError):
    """Raised when :func:`os_reedcheck` encounters malformed data.

    The exception carries attributes that make it possible for callers to
    inspect the raw contents of the letter groups that were
    examined.
    """

    def __init__(self, message, packs_calling_line=None, packs_outpulse=None, decoded=None, sender_prime_decoded=None, bin=None):
        super().__init__(message)
        self.packs_calling_line = packs_calling_line or {}
        self.packs_outpulse = packs_outpulse or {}
        self.decoded = decoded
        self.sender_prime_decoded = sender_prime_decoded
        self.bin = bin

class OSCheckError(ValueError):
    """Raised when :func:`os_check` encounters malformed data.

    The exception carries attributes that make it possible for callers to
    inspect the raw contents of the letter groups that were
    examined.  ``os_check_fails`` uses this information to record diagnostics
    for later analysis.
    """

    def __init__(self, message, packs=None, decoded=None, details=None, bin=None):
        super().__init__(message)
        self.packs = packs or {}
        self.decoded = decoded
        self.details = details
        self.bin = bin

class NumberGroupCheckError(ValueError):
    """Raised when :func:`ng_getmeta` detects invalid number-group punches."""

    def __init__(self, message, details=None, bin=None):
        super().__init__(message)
        self.details = details or {}

class CMCheckError(ValueError):
    """Raised when :func:`cm_check` detects an invalid completing-marker state."""

    def __init__(self, message, code=None, details=None, bin=None):
        super().__init__(message)
        self.code = code
        self.details = details or {}
        self.bin = bin
