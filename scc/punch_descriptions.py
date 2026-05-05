"""
mapping of punch names to a human‑readable explanation.

"""

PUNCH_DESCRIPTIONS: dict[str, str] = {
    'TI': 'Trouble encountered on a service, monitored, or test call.',
    'MTPT': 'Marker, transverter, pretranslator test from master test frame.',
    'SRT': 'Sender-register test from master test frame.',
    'TKT': 'Trunk test from master test frame.',
    'M': "This call was being monitored by the AMRST",
    'MLV': 'Marker Line Verification test from the master test frame.',
    'TLV': 'Transverter line verification.',
    'LVF': (
        'Line Verification Failed. The line information input into the MTF '
        'does not agree with the information present in the Number Group.'
    ),
    'LVM': (
        'Line Verification Match. The line information input into the MTF '
        'agrees with the line information present in the Number Group'
    ),
    'MOR': (
        'This card was dropped because the AMRST encountered a failure while '
        'monitoring an Originating Register.'
    ),
    'MIR': (
        'This card was dropped because the AMRST encountered a failure while '
        'monitoring an Incoming Register.'
    ),
    'MOS': (
        'This card was dropped because the AMRST encountered a failure while '
        'monitoring an Outgoing Sender'
    ),
    'LIT': (
        'Line Insulation Test. This card was dropped as a result of a failed LIT. Not used at musem.'
    ),
    'PRT': (
        'A pretranslator dropped this card. Not used at museum.'
    ),
    'MKR': (
        'A marker dropped this card. The DR punch indicates which maker in particular.'
    ),
    'TURN OVER': (
        'This card wants you to turn it over and read from the back side.'
    ),
    'DR0': (
        'This call was handled by Completing Marker 0, which is the wirespring '
        'marker, SD-26002-01.'
    ),
    'DR1': (
        'This call was handled by Completing Marker 1, which is the U&Y relay '
        'marker, SD-25550-01.'
    ),
    'DR8': 'This call was handled by the Dial Tone Marker, SD-26001-01',
    'DRT0': 'Display Registered Tens 0. The tens digit of the DR punches.',
    '1TR': (
        'This card was the result of the markers first attempt to handle the call. '
        'If there was also a failure on a second attempt, there may be a card immediately '
        'following this one.'
    ),
    '2TR': (
        'This card was the result of the markers second attempt to handle the call. '
        'There will be no further attempts after this.'
    ),
    'WT': (
        'Work Timer expired. This usually indicates that the marker timed out while '
        'trying to complete an internal function or functions.'
    ),
    'SDT': (
        'Short Delay Timer expired. This indicates that the marker timed out while '
        'trying to seize a line link, trunk link, sender group, or number group.'
    ),
    'LDT': (
        'Long Delay Timer expired. This timer supersedes the SDT when the marker has '
        'encountered trouble but was waiting on another marker to complete '
        'its trouble record.'
    ),
    'TRS': (
        'Transfer Start Lead. This indicates a possible issue in the marker '
        'connector.'
    ),
    'TGT': (
        'Trunk Guard Test. The outgoing sender failed to complete its trunk guard (TG) '
        'test in the allotted time. This may indicate a problem with the outgoing trunk.'
    ),
    'FCG': (
        'False Cross or Ground. The marker FCG relay operated due to trouble on tip '
        'and ring of the selected channel prior to operating the hold magnet.'
    ),
    'LR': (
        'Link Release. The IRL encountered a trouble condition, and the associated IR '
        '(after a waiting period) sent a trouble indication to the marker.'
    ),
    'DCK': (
        'Operated when the IR has detected NO double connection at the IRL. '
    ),
    'GT5': (
        'Ground Test Failure on a subscriber line. This test is normally canceled at '
        'the museum, so if this hole is punched, someone has un-operated the CGT key '
        'at the MTC Jack Lamp Key frame.'
    ),
    'SQA': (
        'Marker SQA (sequence advance) relay remained operated long enough for '
        'SQA1 relay to release (an abnormal length of time), thus indicating a '
        'failure in the sequence advance circuit.'
    ),
    'ITR': (
        'This call was an Intraoffice call. It was from a 5XB line to a different '
        '5XB line.'
    ),
    'SOG': (
        'This was a Subscriber OutGoing call. A 5XB line placed an outgoing call to '
        'another office. This can also indicate that this call went to an announcement '
        'or permanent signal trunk--which, for the purposes of the marker, are '
        'indistinguishable from outgoing calls.'
    ),
    'TER': (
        'This was a Terminating call. The call originated in a different '
        'office, and terminated here via an incoming trunk and incoming register.'
    ),
    'TOG': (
        'This was a Tandem Outgoing call. A call originated from a different office, '
        'and is destined to some other office, but is passing through the 5XB on the '
        'way. This punch is also used for the final outgoing leg of a Coin Junctor '
        'call. (Check CU4,7, SCK are true to validate a coin call.)'
    ),
    'RV': (
        'This is a Reverting call. From a station on a party line to another station '
        'on the same party line. Not used in the museum.'
    ),
    'ROA': 'Marker received reorder indication, and will send the call to reorder tone.',
    'FLG': (
        'Forward Linkage Ground. Marker is ready to set up the terminating stage of '
        'an intraoffice trunk connection or is ready to set up the linkage on an '
        'incoming trunk connection.'
    ),
    'SCB': (
        'Start Call-Back. Marker is establishing the originating stage of an '
        'intraoffice trunk connection.'
    ),
    'NSO': (
        'No Sender Outgoing. Outgoing trunk connection not requiring a sender. For '
        'example, a call to a test trunk, an announcement, or the Audichron.'
    ),
    'NSI': (
        'No Sender Intraoffice. An intraoffice call not requiring a sender '
        '(pretty much all of them.)'
    ),
    'SON': (
        'Sender Outgoing. An outgoing call that requires a sender. This includes '
        'calls to the 1XB, Panel, SxS, DMS-100, etc.'
    ),
    'DRT1': (
        'Display Registered Tens. The tens digit of the DR punches. Since we have '
        'only 3 markers, we dont use this.'
    ),
    'LB': (
        'Line busy. The line called is currently in use and the calling subscriber '
        'should receive a busy signal.'
    ),
    'FM': (
        'Failure to Match. After several attempts, the marker failed to find an idle '
        'channel through the switching network to reach the called destination. This '
        'call has failed.'
    ),
    'RCY': (
        'Failure to Recycle. The marker has failed to recycle when required to do '
        'so because of a trouble condition.'
    ),
    'RA': 'Marker has prepared to Route Advance.',
    'AMA': (
        'The marker has recognized that this call requires AMA, and will prime '
        'the outgoing sender to request and transmit AMA billing information. Used '
        'on CAMA calls to kercheep.'
    ),
    'FR-': (
        'Frame Number. Either the IRMC, ORMC, LLMC, or PTRC, depending on the '
        'specific nature of the card.'
    ),
    'CN-': 'Connector Number of the following frames: LLMC, ORMC, IRMC.',

    # Note: the following group of punches isn't really prime ('), but I had to 
    # address them this way to avoid a name collision with HT- hour tens punches.
    'HT\'0': (
        'Hundreds Trunk. Used on tandem calls to identify the hundreds digit of '
        'the line link appearance of the tandem trunk in the number group.'
    ),
    'HT\'1': (
        'Hundreds Trunk. Used on tandem calls to identify the hundreds digit of '
        'the line link appearance of the tandem trunk in the number group.'
    ),
    'HT\'2': (
        'Hundreds Trunk. Used on tandem calls to identify the hundreds digit of '
        'the line link appearance of the tandem trunk in the number group.'
    ),
    'HT\'4': (
        'Hundreds Trunk. Used on tandem calls to identify the hundreds digit of '
        'the line link appearance of the tandem trunk in the number group.'
    ),
    'HT\'7': (
        'Hundreds Trunk. Used on tandem calls to identify the hundreds digit of '
        'the line link appearance of the tandem trunk in the number group.'
    ),
    'TT0': (
        'Tens Trunk. Used on tandem calls to identify the tens digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),
    'TT1' : (
        'Tens Trunk. Used on tandem calls to identify the tens digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),
    'TT2': (
        'Tens Trunk. Used on tandem calls to identify the tens digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),  
    'TT4': (
        'Tens Trunk. Used on tandem calls to identify the tens digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),
    'TT7': (
        'Tens Trunk. Used on tandem calls to identify the tens digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),
    'UT0': (
        'Units Trunk. Used on tandem calls to identify the units digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),
    'UT1': (
        'Units Trunk. Used on tandem calls to identify the units digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),
    'UT2': (
        'Units Trunk. Used on tandem calls to identify the units digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),
    'UT4': (
        'Units Trunk. Used on tandem calls to identify the units digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),
    'UT7': (
        'Units Trunk. Used on tandem calls to identify the units digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),
    'CN-RG0': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'CN-RG1': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'CN-RG2': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'CN-RG3': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'CN-RG4': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'CN-RG5': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'CN-RG6': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'CN-RG7': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'CN-RG8': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'CN-RG9': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'FG0': 'Trunk Link Frame Group. Always 0 in the museum.',
    'ECN': (
        'Even Connector. The even-numbered marker connector in the IRMC. This '
        'information is used to steer the marker to a preferred number group for '
        'obtaining tandem LLF appearance information.'
    ),
    'OCN': (
        'Odd Connector. The odd-numbered marker connector in the IRMC. This '
        'information is used to steer the marker to a preferred number group for '
        'obtaining tandem LLF appearance information.'
    ),
    'LT': (
        'Local Translator. The OR has instructed the marker to employ its Local '
        'Translator for this connection. This is the default translator that is used '
        'for calls originated by 5XB subscriber lines.'
    ),
    'TT': (
        'A register has directed the marker to employ its Toll translator for this '
        'connection.'
    ),
    '2DT': (
        'Two-Digit translator. Not used at museum. '
        'On incoming calls, the office code transmitted to the marker is the last '
        'two digits of a 3-digit code where the first digit of the 3-digit code has '
        'been absorbed by the originating office.'
    ),
    'FVD': (
        'A register has directed the marker to employ its five-digit translator '
        'for this connection.'
    ),
    'X11': (
        'A register has directed the marker to employ its service code translator '
        'for this connection. e.g. 411, 511, 911, etc.'
    ),
    '11': (
        'A register has directed the marker to employ its +11 translator for '
        'this connection.'
    ),
    'OA': (
        'Office A. On an incoming trunk connection, this is the office unit to which the '
        'marker should complete the connection.'
    ),
    'OB': (
        'Office B. On an incoming trunk connection, this is the office unit to which the '
        'marker should complete the connection.'
    ),
    'AN': 'The marker is working with an Allotted PBX Number',
    'PHC': (
        'Physical Office. The incoming register directed the marker to complete '
        'the connection to the physical subdivision of telephone numbers in this '
        'office.'
    ),
    'THC': (
        'Theoretical Office. The incoming register directed the marker to complete '
        'the connection to the theoretical subdivision of telephone numbers in this '
        'office.'
    ),
    'OR': (
        'The originating register marker connector notified the marker that this '
        'is an originating connection. This call came from a line in this office.'
    ),
    'FAC': (
        'Foreign Area Code. Originating register marker connector informed the '
        'marker that this is a Direct Distance Dialled call. Not used at the museum.'
    ),
    'INC': (
        'Incoming Call. The incoming register marker connector informed the '
        'marker that this is an incoming local call.'
    ),
    'TAN': (
        'Tandem Call. The incoming register marker connector informed the '
        'marker that this call is from a tandem trunk.'
    ),
    'TOL': (
        'Toll Call. The incoming register marker connector informed the '
        'marker that this call is from a toll trunk.'
    ),
    'LT1': (
        'Local Translator 1. The OR has instructed the marker to employ its Local '
        'Translator 1 for this connection. In the museum, this is used for 1+ dialed '
        'calls to C*NET. This call was sent to Kercheep for handling.'
    ),
    'RO': (
        'Reorder. Incoming register signaled the marker for a reorder (overflow) '
        'signal.'
    ),
    'NT': 'No Test. The incoming trunk signaled the marker that the terminating line should *not* be tested for busy before establishing connection.',
    'NN': 'No Nothing. The incoming trunk signaled the marker that this call is neither no test nor no hunt. It is just normal.',
    'NH': 'No Hunt. The incoming trunk signaled the marker that there shall be no PBX hunting on this call.',
    'TF0': (
        'Indicates the trunk link frame that an incoming call came in on. Always '
        '0 (4,7) at the museum.'
    ),
    'TF1': (
        'Indicates the trunk link frame that an incoming call came in on. Always '
        '0 (4,7) at the museum.'
    ),
    'TF2': (
        'Indicates the trunk link frame that an incoming call came in on. Always '
        '0 (4,7) at the museum.'
    ),
    'TF4': (
        'Indicates the trunk link frame that an incoming call came in on. Always '
        '0 (4,7) at the museum.'
    ),
    'TF7': (
        'Indicates the trunk link frame that an incoming call came in on. Always '
        '0 (4,7) at the museum.'
    ),
    'PS': (
        'Permanent Signal. The OR timed out while waiting for a customer to dial, '
        'and informed the marker to send this call to a permanent signal holding '
        'trunk.'
    ),
    'PD': (
        'Partial Dial. The OR received some digits, but not enough to complete the '
        'call. It informed the marker to send to a partial dial route. In the museum, '
        'this is the same as Permanent Signal.'
    ),
    'PK': (
        'Permanent Signal ChecK. The OR informed the marker that dialing functions '
        'were completed within the allotted time. This is good.'
    ),
    'CR': (
        'Coin Returned. Originating register informed the marker that it (the OR) '
        'has successfully returned the subscriber\'s coin.'
    ),
    'SCN': (
        '\"See Coin? No!\" The OR informed the marker that the subscriber *has '
        'not* deposited a coin for this call. This punch appears when someone is '
        'using a pay phone, but has not inserted a coin. The marker should route '
        'this call to an announcement.'
    ),
    'SCK': (
        '\"See Coin ChecK\" The OR informed the marker that the subscriber *has* '
        'deposited a coin for this call, or that no coin was necessary because this '
        'is not a payphone.'
    ),
    'CNR': (
        'Marker signals the originating register to return '
        'the coin.'
    ),
    'MAN': (
        'The Dial Tone Marker has received an indication that this is a manual '
        'subscriber, and that dial tone should not be provided. The call will be '
        'routed directly to an operator trunk. Not used at the museum.'
    ),
    '2P': (
        'Two Party. The Dial Tone Marker has received an indication that this '
        'is a party line subscriber and that the OR should make party test to '
        'determine if the calling sub is tip party or ring party.'
    ),
    'OBS': (
        'Observed. The OR signals the marker that this call is is up on service '
        'observation. Not used at museum.'
    ),
    'NOB': (
        'Not OBserved. The OR signals the marker that this call is not set up '
        'on service observation. This is the default case in the museum.'
    ),
    'WC': (
        'Water Closet'
    ),
    'A0': 'The A-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'A1': 'The A-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'A2': 'The A-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'A4': 'The A-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'A7': 'The A-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'B0': 'The B-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'B1': 'The B-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'B2': 'The B-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'B4': 'The B-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'B7': 'The B-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'C0': 'The C-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'C1': 'The C-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'C2': 'The C-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'C4': 'The C-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'C7': 'The C-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'D0': 'The D-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'D1': 'The D-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'D2': 'The D-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'D4': 'The D-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'D7': 'The D-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'E0': 'The E-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'E1': 'The E-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'E2': 'The E-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'E4': 'The E-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'E7': 'The E-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'F0': 'The F-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'F1': 'The F-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'F2': 'The F-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'F4': 'The F-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'F7': 'The F-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'G0': 'The G-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'G1': 'The G-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'G2': 'The G-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'G4': 'The G-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'G7': 'The G-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'H0': 'The H-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'H1': 'The H-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'H2': 'The H-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'H4': 'The H-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'H7': 'The H-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.',
    'J0': 'The J-digit received from the OR or IR. Not used at museum.',
    'J1': 'The J-digit received from the OR or IR. Not used at museum.',
    'J2': 'The J-digit received from the OR or IR. Not used at museum.',
    'J4': 'The J-digit received from the OR or IR. Not used at museum.',
    'J7': 'The J-digit received from the OR or IR. Not used at museum.',
    'K0': 'The K-digit received from the OR or IR. Not used at museum.',
    'K1': 'The K-digit received from the OR or IR. Not used at museum.',
    'K2': 'The K-digit received from the OR or IR. Not used at museum.',
    'K4': 'The K-digit received from the OR or IR. Not used at museum.',
    'K7': 'The K-digit received from the OR or IR. Not used at museum.',
    'L0': 'The L-digit received from the OR or IR. Not used at museum.',
    'L1': 'The L-digit received from the OR or IR. Not used at museum.',
    'L2': 'The L-digit received from the OR or IR. Not used at museum.',
    'L4': 'The L-digit received from the OR or IR. Not used at museum.',
    'L7': 'The L-digit received from the OR or IR. Not used at museum.',
    'M7': 'The M-digit received from the OR or IR. Not used at museum.',
    'A\'0': 'The A-digit passed to the outsender, or the A digit registered in the monitor.',
    'A\'1': 'The A-digit passed to the outsender, or the A digit registered in the monitor.',
    'A\'2': 'The A-digit passed to the outsender, or the A digit registered in the monitor.',
    'A\'4': 'The A-digit passed to the outsender, or the A digit registered in the monitor.',
    'A\'7': 'The A-digit passed to the outsender, or the A digit registered in the monitor.',
    'B\'0': 'The B-digit passed to the outsender, or the B digit registered in the monitor.',
    'B\'1': 'The B-digit passed to the outsender, or the B digit registered in the monitor.',
    'B\'2': 'The B-digit passed to the outsender, or the B digit registered in the monitor.',
    'B\'4': 'The B-digit passed to the outsender, or the B digit registered in the monitor.',
    'B\'7': 'The B-digit passed to the outsender, or the B digit registered in the monitor.',
    'C\'0': 'The C-digit passed to the outsender, or the C digit registered in the monitor.',
    'C\'1': 'The C-digit passed to the outsender, or the C digit registered in the monitor.',
    'C\'2': 'The C-digit passed to the outsender, or the C digit registered in the monitor.',
    'C\'4': 'The C-digit passed to the outsender, or the C digit registered in the monitor.',
    'C\'7': 'The C-digit passed to the outsender, or the C digit registered in the monitor.',
    'D\'0': 'The D-digit passed to the outsender, or the D digit registered in the monitor.',
    'D\'1': 'The D-digit passed to the outsender, or the D digit registered in the monitor.',
    'D\'2': 'The D-digit passed to the outsender, or the D digit registered in the monitor.',
    'D\'4': 'The D-digit passed to the outsender, or the D digit registered in the monitor.',
    'D\'7': 'The D-digit passed to the outsender, or the D digit registered in the monitor.',
    'E\'0': 'The E-digit passed to the outsender, or the E digit registered in the monitor.',
    'E\'1': 'The E-digit passed to the outsender, or the E digit registered in the monitor.',
    'E\'2': 'The E-digit passed to the outsender, or the E digit registered in the monitor.',
    'E\'4': 'The E-digit passed to the outsender, or the E digit registered in the monitor.',
    'E\'7': 'The E-digit passed to the outsender, or the E digit registered in the monitor.',
    'F\'0': 'The F-digit passed to the outsender, or the F digit registered in the monitor.',
    'F\'1': 'The F-digit passed to the outsender, or the F digit registered in the monitor.',
    'F\'2': 'The F-digit passed to the outsender, or the F digit registered in the monitor.',
    'F\'4': 'The F-digit passed to the outsender, or the F digit registered in the monitor.',
    'F\'7': 'The F-digit passed to the outsender, or the F digit registered in the monitor.',
    'G\'0': 'The G-digit passed to the outsender, or the G digit registered in the monitor.',
    'G\'1': 'The G-digit passed to the outsender, or the G digit registered in the monitor.',
    'G\'2': 'The G-digit passed to the outsender, or the G digit registered in the monitor.',
    'G\'4': 'The G-digit passed to the outsender, or the G digit registered in the monitor.',
    'G\'7': 'The G-digit passed to the outsender, or the G digit registered in the monitor.',
    'H\'0': 'The H-digit passed to the outsender, or the H digit registered in the monitor.',
    'H\'1': 'The H-digit passed to the outsender, or the H digit registered in the monitor.',
    'H\'2': 'The H-digit passed to the outsender, or the H digit registered in the monitor.',
    'H\'4': 'The H-digit passed to the outsender, or the H digit registered in the monitor.',
    'H\'7': 'The H-digit passed to the outsender, or the H digit registered in the monitor.',
    'J\'0': 'The J-digit passed to the outsender, or the J digit registered in the monitor. Not used at museum.',
    'J\'1': 'The J-digit passed to the outsender, or the J digit registered in the monitor. Not used at museum.',
    'J\'2': 'The J-digit passed to the outsender, or the J digit registered in the monitor. Not used at museum.',
    'J\'4': 'The J-digit passed to the outsender, or the J digit registered in the monitor. Not used at museum.',
    'J\'7': 'The J-digit passed to the outsender, or the J digit registered in the monitor. Not used at museum.',
    'K\'0': 'The K-digit passed to the outsender, or the K digit registered in the monitor. Not used at museum.',
    'K\'1': 'The K-digit passed to the outsender, or the K digit registered in the monitor. Not used at museum.',
    'K\'2': 'The K-digit passed to the outsender, or the K digit registered in the monitor. Not used at museum.',
    'K\'4': 'The K-digit passed to the outsender, or the K digit registered in the monitor. Not used at museum.',
    'K\'7': 'The K-digit passed to the outsender, or the K digit registered in the monitor. Not used at museum.',
    'L\'0': 'The L-digit passed to the outsender, or the L digit registered in the monitor. Not used at museum.',
    'L\'1': 'The L-digit passed to the outsender, or the L digit registered in the monitor. Not used at museum.',
    'L\'2': 'The L-digit passed to the outsender, or the L digit registered in the monitor. Not used at museum.',
    'L\'4': 'The L-digit passed to the outsender, or the L digit registered in the monitor. Not used at museum.',
    'L\'7': 'The L-digit passed to the outsender, or the L digit registered in the monitor. Not used at museum.',
    'M\'7': 'The M-digit passed to the outsender, or the M digit registered in the monitor. Not used at museum.',
    'GS1': (
           'Ground Supply 1. The marker has advanced to Ground Supply 3, since it was unable to establish '
           'a route for the call in GS1. GS3 contains route relays 10-19. '
           'Ground Supply 3 is used for second-choice routes when the marker is unable to establish a connection using '
           'a first choice route. Routes here include Kercheep, and any primary route that does not have its '
           'own alternate.'
    ),
    'GS2': (
        'Ground Supply 2. Not used in museum.'
    ),
    'GS3': (
        'Ground Supply 3. The marker has advanced to Ground Supply 5. GS5 contains route relays 6-9, '
        'or 0-5 depending on the marker. Routes in this ground supply are generally reserved for intercept, '
        'permanent signal, or an announcement, and do not usually have an alternate. '
        '(A punch here indicates we have advanced *past* Ground Supply 3 and the operation that dropped '
        'this card was using GS5).'
    ),
    'GS4': (
        'Ground Supply 4. Not used in museum.'
    ),
    'GS5': (
        'Ground Supply 5. The marker has advanced to Ground Supply 6. GS6 contains routes of last resort, '
        'and there can be no further advancement past here. '
        '(A punch here indicates we have advanced *past* Ground Supply 5 and the operation that dropped '
        'this card was using GS6)'
    ),
    'FAA': (
        'Foreign Area A. Foreign area translator "A" was associated with '
        'the marker when trouble record was taken.'
    ),
    'FAB': (
        'Foreign Area B. Foreign area translator "B" was associated with '
        'the marker when trouble record was taken.'
    ),
    'GPA': (
        'Group Preference A. The marker selected the subgroup A trunks or senders in an allotted group.'
    ),
    'GPB': (
        'Group Preference B. The marker selected the subgroup B trunks or senders in an allotted group.'
    ),
    'TWT': (
        'Two-way Trunk Route. A TWT0-2 relay was operated in the marker for 2-way trunk operation.'
    ),
    'CNS': (
        'Coin Service. This is a coin class call.'
    ),
    'DR': (
        'Denied Route. A DR0-2 relay was operated in the marker for a denied service route.'
    ),
    'CRR0': (
        'Coin Reroute. A marker CR0 (coin zone reroute) relay was operated for rerouting a coin class of a call to an operator.'
    ),
    'CRR1': (
        'Coin Reroute. A marker CR1 (coin zone reroute) relay was operated for rerouting a coin class of a call to an operator.'
    ),
    'CRR2': (
        'Coin Reroute. A marker CR2 (coin zone reroute) relay was operated for rerouting a coin class of a call to an operator.'
    ),
    'RT0': (
        'Route transfer 0 relay operated in the marker because the \'RT 0\' key was operated in the MTF'
    ),
    'RT1': (
        'Route transfer 1 relay operated in the marker because the \'RT 1\' key was operated in the MTF'
    ),
    'RT2': (
        'Route transfer 2 relay operated in the marker because the \'RT 2\' key was operated in the MTF'
    ),
    'RT3': (
        'Route transfer 3 relay operated in the marker because the \'RT 3\' key was operated in the MTF'
    ),
    'RT4': (
        'Route transfer 4 relay operated in the marker because the \'RT 4\' key was operated in the MTF'
    ),
    'TC': 'Talk Charge. The marker operated the \'TC\' (talk charge) relay in the trunk used for this call.',
    'TP': 'Tip Party. The originating register signaled the marker that this is a tip party call.',
    'CN': 'Coin Call. The marker operated the \'CN\' (coin class) relay in the trunk used for this call.',
    'RP': 'Ring Party. The originating register signaled the marker that this is a ring party call.',
    'FR0': 'Outgoing Sender Connector (OSC) frame 0 was used on this call.',
    'FR1': 'Outgoing Sender Connector (OSC) frame 1 was used on this call.',
    'FR2': 'Outgoing Sender Connector (OSC) frame 2 was used on this call.',
    'FR3': 'Outgoing Sender Connector (OSC) frame 3 was used on this call.',
    'FR4': 'Outgoing Sender Connector (OSC) frame 4 was used on this call.',
    'CN0': 'Connector 0 in the selected OSC was used on this call.',
    'CN1': 'Connector 1 in the selected OSC was used on this call.',
    'CN2': 'Connector 2 in the selected OSC was used on this call.',
    'CN3': 'Connector 3 in the selected OSC was used on this call.',
    'S0': 'Sender 0 in the selected OSC was used on this call.',
    'S1': 'Sender 1 in the selected OSC was used on this call.',
    'S2': 'Sender 2 in the selected OSC was used on this call.',
    'S3': 'Sender 3 in the selected OSC was used on this call.',
    'S4': 'Sender 4 in the selected OSC was used on this call.',
    'S5': 'Sender 5 in the selected OSC was used on this call.',
    'S6': 'Sender 6 in the selected OSC was used on this call.',
    'S7': 'Sender 7 in the selected OSC was used on this call.',
    'S8': 'Sender 8 in the selected OSC was used on this call.',
    'S9': 'Sender 9 in the selected OSC was used on this call.',
    'S10': 'Sender 10 in the selected OSC was used on this call.',
    'S11': 'Sender 11 in the selected OSC was used on this call.',
    'S12': 'Sender 12 in the selected OSC was used on this call.',
    'OSG0': 'Outgoing Sender Group 0 was selected by the marker. This group includes the MF outsenders.',
    'OSG1': 'Outgoing Sender Group 1 was selected by the marker. This group includes the DP and RP outsenders.',
    'OSG2': 'Outgoing Sender Group 2 was selected by the marker.',
    'OSG3': 'Outgoing Sender Group 3 was selected by the marker.',
    'OSG4': 'Outgoing Sender Group 4 was selected by the marker.',
    'OSG5': 'Outgoing Sender Group 5 was selected by the marker.',
    'OSG6': 'Outgoing Sender Group 6 was selected by the marker.',
    'OSG7': 'Outgoing Sender Group 7 was selected by the marker.',
    'OSG8': 'Outgoing Sender Group 8 was selected by the marker.',
    'OSG9': 'Outgoing Sender Group 9 was selected by the marker.',
    'OSG10': 'Outgoing Sender Group 10 was selected by the marker.',
    'OSG11': 'Outgoing Sender Group 11 was selected by the marker.',
    'SSA': 'Outgoing sender subgroup A was seized by the marker.',
    'SSB': 'Outgoing sender subgroup B was seized by the marker.',
    'OS0': 'Outgoing sender 0 was selected in the sender group.',
    'OS1': 'Outgoing sender 1 was selected in the sender group.',
    'OS2': 'Outgoing sender 2 was selected in the sender group.',
    'OS3': 'Outgoing sender 3 was selected in the sender group.',
    'OS4': 'Outgoing sender 4 was selected in the sender group.',
    'RO\'': 'Operation of the RO (Reorder) relay In the outgoing sender to set the outgoing trunk for reorder.',
    'RN-SPC-ITC0': 'Incoming trunk class NN',
    'RN-SPC-ITC1': 'Incoming trunk class TB',
    'RN-SPC-ITC2': 'Incoming trunk class MB',
    'RN-SPC-ITC3': 'Incoming trunk class FB',
    'RN-SPC-ITC4': 'Incoming trunk class TT',
    'RN-SPC-ITC5': 'Incoming trunk class MT',
    'RN-SPC-ITC6': 'Incoming trunk class FT',
    'RN-SPC-ITC7': 'Incoming trunk class TP',
    'RN-SPC-ITC8': 'Incoming trunk class MP',
    'RN-SPC-ITC9': 'Incoming trunk class FP',
    'SC': 'The SC relay in the sender should have operated to indicate this is an AMA service call.',
    'TVT': 'The TVT relay in the sender should have operated to indicate this is an AMA test call.',
    'OBS\'': 'The OBS\' relay in the sender should have operated to indicate this call is on service observation.',
    'NOB\'': 'The NOB\' relay in the sender should have operated to indicate this call is not on service observation.',
    'CP0': 'The Code Pattern indication transmitted from the marker to the sender on a LAMA call.',
    'CP1': 'The Code Pattern indication transmitted from the marker to the sender on a LAMA call.',
    'CP2': 'The Code Pattern indication transmitted from the marker to the sender on a LAMA call.',
    'CP4': 'The Code Pattern indication transmitted from the marker to the sender on a LAMA call.',
    'CP7': 'The Code Pattern indication transmitted from the marker to the sender on a LAMA call.',
    'MB0': 'The message billing index transmitted from the marker to the sender on a LAMA call.',
    'MB1': 'The message billing index transmitted from the marker to the sender on a LAMA call.',
    'MB2': 'The message billing index transmitted from the marker to the sender on a LAMA call.',
    'MB4': 'The message billing index transmitted from the marker to the sender on a LAMA call.',
    'MB7': 'The message billing index transmitted from the marker to the sender on a LAMA call.',
    'RN0': 'The recorder number transmitted from the marker to the sender on a LAMA call.',
    'RN1': 'The recorder number transmitted from the marker to the sender on a LAMA call.',
    'RN2': 'The recorder number transmitted from the marker to the sender on a LAMA call.',
    'RN4': 'The recorder number transmitted from the marker to the sender on a LAMA call.',
    'RN7': 'The recorder number transmitted from the marker to the sender on a LAMA call.',
    'DL1': 'The marker informed the sender to delete the A digit of the called number before outpulsing.',
    'DL2': 'The marker informed the sender to delete the A+B digits of the called number before outpulsing.',
    'DL3': 'The marker informed the sender to delete the A+B+C digits of the called number before outpulsing.',
    'DL4': 'The marker informed the sender to delete the A+B+C+D digits of the called number before outpulsing.',
    'DL5': 'The marker informed the sender to delete the A+B+C+D+E digits of the called number before outpulsing.',
    'DL6': 'The marker informed the sender to delete the A+B+C+D+E+F digits of the called number before outpulsing.',
    'CL1': (
        'To DP and MF senders, that a 11 is to be outpulsed before the called number. '
        'To RP senders, that the call is to a No. 1 Crossbar office.'
    ),
    'CL2': (
        'To DP sender, that the call is over a 2-way trunk. '
        'To an MF sender, to give immediate trunk closure on this call. '
        'To an RP sender, that the call is to a 2 digit office in a 2-3 digit area.'
    ),
    'CL3': (
        'To a DP sender, to delay dialing until a start signal is received from the distant office. '
        'To RP sender, that the call is to a non-repeating incoming panel ground cutoff office and thus a '
        'marginal trunk test is required. '
        'To an MF sender (with 5), that ANI is required on this call (AMA calls only).'
    ),
    'CL4': (
        'To a DP sender, that dial pulsing at 20 PPS is required. '
        'To an RP sender, that this call is to a high incoming group in a BCO panel or XBR office.'
    ),
    'CL5': (
        'To a DP sender, that battery and ground pulsing is required, as opposed to loop disconnect pulsing. '
        'To an MF sender (with 3), that ANI identification is required on this call (AMA calls only).'
    ),
    'CL6': (
        'To a DP sender, that this is a CX Intertoll or CX 2-way trunk. '
        'To an RP sender, that the call is to a 3 digit office in a 2-3 digit area.'
    ),
    'FT0': 'Frame Tens 0. The tens digit of the line link frame associated with the calling line.',
    'FT1': 'Frame Tens 1. The tens digit of the line link frame associated with the calling line.',
    'FT2': 'Frame Tens 2. The tens digit of the line link frame associated with the calling line.',
    'FT3': 'Frame Tens 3. The tens digit of the line link frame associated with the calling line.',
    'FU0': 'Frame Units 0. The units digit of the line link frame associated with the calling line.',
    'FU1': 'Frame Units 1. The units digit of the line link frame associated with the calling line.',
    'FU2': 'Frame Units 2. The units digit of the line link frame associated with the calling line.',
    'FU4': 'Frame Units 4. The units digit of the line link frame associated with the calling line.',
    'FU7': 'Frame Units 7. The units digit of the line link frame associated with the calling line.',
    'VG0': 'Vertical Group 0. The vertical group associated with the calling line.',
    'VG1': 'Vertical Group 1. The vertical group associated with the calling line.',
    'VG2': 'Vertical Group 2. The vertical group associated with the calling line.',
    'VG4': 'Vertical Group 4. The vertical group associated with the calling line.',
    'VG7': 'Vertical Group 7. The vertical group associated with the calling line.',
    'VG10': 'Vertical Group 10. The vertical group associated with the calling line.',
    'HG0': 'Horizontal Group 0. The horizontal group associated with the calling line.',
    'HG1': 'Horizontal Group 1. The horizontal group associated with the calling line.',
    'HG2': 'Horizontal Group 2. The horizontal group associated with the calling line.',
    'HG4': 'Horizontal Group 4. The horizontal group associated with the calling line.',
    'HG7': 'Horizontal Group 7. The horizontal group associated with the calling line.',
    'VF0': 'Vertical File 0. The vertical file associated with the calling line.',
    'VF1': 'Vertical File 1. The vertical file associated with the calling line.',
    'VF2': 'Vertical File 2. The vertical file associated with the calling line.',
    'VF3': 'Vertical File 3. The vertical file associated with the calling line.',
    'VF4': 'Vertical File 4. The vertical file associated with the calling line.',
    'CT0': 'Class of Service, Tens 0. The tens digit of the class of service of the calling line.',
    'CT1': 'Class of Service, Tens 1. The tens digit of the class of service of the calling line.',
    'CT2': 'Class of Service, Tens 2. The tens digit of the class of service of the calling line.',
    'CU0': 'Class of Service, Units 0. The units digit of the class of service of the calling line.',
    'CU1': 'Class of Service, Units 1. The units digit of the class of service of the calling line.',
    'CU2': 'Class of Service, Units 2. The units digit of the class of service of the calling line.',
    'CU4': 'Class of Service, Units 4. The units digit of the class of service of the calling line.',
    'CU7': 'Class of Service, Units 7. The units digit of the class of service of the calling line.',
    'FT0\'': 'Frame Tens 0. The tens digit of the line link frame as registered in the sender.',
    'FT1\'': 'Frame Tens 1. The tens digit of the line link frame as registered in the sender.',
    'FT2\'': 'Frame Tens 2. The tens digit of the line link frame as registered in the sender.',
    'FT3\'': 'Frame Tens 3. The tens digit of the line link frame as registered in the sender.',
    'FU0\'': 'Frame Units 0. The units digit of the line link frame as registered in the sender.',
    'FU1\'': 'Frame Units 1. The units digit of the line link frame as registered in the sender.',
    'FU2\'': 'Frame Units 2. The units digit of the line link frame as registered in the sender.',
    'FU4\'': 'Frame Units 4. The units digit of the line link frame as registered in the sender.',
    'FU7\'': 'Frame Units 7. The units digit of the line link frame as registered in the sender.',
    'VG0\'': 'Vertical Group 0. The vertical group as registered in the sender.',
    'VG1\'': 'Vertical Group 1. The vertical group as registered in the sender.',
    'VG2\'': 'Vertical Group 2. The vertical group as registered in the sender.',
    'VG4\'': 'Vertical Group 4. The vertical group as registered in the sender.',
    'VG7\'': 'Vertical Group 7. The vertical group as registered in the sender.',
    'VG10\'': 'Vertical Group 10. The vertical group as registered in the sender.',
    'HG0\'': 'Horizontal Group 0. The horizontal group as registered in the sender.',
    'HG1\'': 'Horizontal Group 1. The horizontal group as registered in the sender.',
    'HG2\'': 'Horizontal Group 2. The horizontal group as registered in the sender.',
    'HG4\'': 'Horizontal Group 4. The horizontal group as registered in the sender.',
    'HG7\'': 'Horizontal Group 7. The horizontal group as registered in the sender.',
    'VF0\'': 'Vertical File 0. The vertical file as registered in the sender.',
    'VF1\'': 'Vertical File 1. The vertical file as registered in the sender.',
    'VF2\'': 'Vertical File 2. The vertical file as registered in the sender.',
    'VF3\'': 'Vertical File 3. The vertical file as registered in the sender.',
    'VF4\'': 'Vertical File 4. The vertical file as registered in the sender.',
    'TM': 'Timing. The timing lead has been grounded by the marker connector.',
    'CKG': (
        'Checking Ground is closed from marker connector relays to provide '
        'off-normal grounds and remove certain standing tests.'
    ),
    'TC1': (
        'Traffic Control 1. Used for dial tone calls only. Marker has assumed control of the LLMC.'
    ),
    'NE': (
        'One of the N1A/N2A/N3A/N4A (number translator cut-in auxiliary) relays in the marker '
        'operated on an incoming or intra-office trunk connection. These relays '
        'are operated for number group translation of the called number.'
    ),
    'TRN': (
        'The (trunk number) relay in the marker, operated to pass the trunk number '
        '(numerical digits) into the number group for a tandem or toll trunk connection.'
    ),
    'GTL': (
        'GTL (ground transmitting lead) relay in the marker functions to apply ground '
        'on transmitting leads to registers or senders.'
    ),
    'TSE': (
        'Trunk Selection End. When punched, indicates that the marker was '
        'unable to complete trunk selection. Should be unpunched for a successful call.'
    ),
    'FCK': ( 
        'Frame Connector Check. The cut-in relay of a selected route operated, thus closing '
        'the test leads to the trunk link connector frames serving this route.'
    ),
    'FTCK': (
        'Frame Test Check. Trunk link frames have been tested for the presence of an idle trunk '
        'for the selected route, and at least one frame has an idle route available.'
    ),
    'SNK': (
        'Selections Normal Check. Releases on a Recycle call when the marker has cleared '
        'the information used in its previous attempt. If not a recycle, this punch doesn\'t matter.'
    ),
    'CK': 'Marker preference (MP or E) relay on the selected trunk link frame operated.',
    'FML': (
        'Frame Memory Lock relay in the marker operated to insure a different trunk link frame '
        'is selected on the next call. Ineffective at museum.'
    ),
    'MAK1': (
        'Marker Connector Cut-In Check. Both halves of the MCA relay operated in the selected '
        'Trunk Link Connector (TLC).'
    ),
    'TBK': (
        'Trunk Block Check. A TB- relay of the selected trunk link connector operated.'
    ),
    'ORK': (
        'Originating Register Check. Also replaced by RK1 on dial tone calls. '
        'RK1 indicates that no false ground is present on the calling-line identification '
        'leads to the OR. ORK indicates that the called number from the OR/IR has been '
        'properly received and validated.'
    ),
    'RK2': (
        'Register Check 2. Indicates that no false battery was detected on the calling line leads from the OR. '
        'Operation of both RK1 and RK2 indicates that the calling line information has been properly transmitted '
        'to the OR by the dial tone marker (DTM).'
    ),
    'VTK1': (
        'Vertical Group Test Check. When punched, indicates that only one of the VGT0-11 relays is locked operated '
        'in the marker for vertical group selection. VG- selection is valid.'
    ),
    'HTK1': (
        'Horizontal Group Test Check. When punched, indicates that only one of the HGT0-9 relays is locked operated '
        'in the marker for horizontal group selection. HG- selection is valid.'
    ),
    'FTK1': (
        'Vertical File Test Check. When punched, indicates that only one of the VFT0-4 relays is locked operated for '
        'vertical file selection. VF- selection is valid.'
    ),
    'LFK1': (
        'Line Link Frame Check. Indicates that the associated Marker Cut In (MCA) relay has operated in the selected '
        'line link frame (LLF).'
    ),
    'DTK': (
        'Dial Tone Check. Used only by the dial tone marker (DTM). Indicates that the DT relay in the associated '
        'line link connector (LLC) has operated.'
    ),
    'FAK': (
        'Frame A Appearance Check. The FA- relay in the selected TLF has operated, indicating that the A appearance '
        'location in the selected trunk link frame will be used.'
    ),
    'FBK': (
        'Frame B Appearance Check. The FB- relay in the selected TLF has operated, indicating that the B appearance '
        'location in the selected trunk link frame will be used.'
    ),
    'LCK': (
        'Link Connector Check. The LC- relay in the selected trunk link connector has operated.'
    ),
    'RK3': (
        'RK3 relay in the marker has operated to show that all necessary information '
        'has been forwarded and is locked into the originating register. With the RK1 '
        'and RK2 punched, an absence of the indicates that the check of the register '
        'locking path is incomplete.'
    ),
    'HGK': (
        'Horizontal Group Check. One of the HG0-9 relays has operated in associated LLF.'
    ),
    'RK': (
        'RK (right-half frame check) relay in the marker operated from an operated R (right) relay on the '
        'selected trunk link frame. This causes the marker to test junctors serving the right half of the trunk '
        'link frame.'
    ),
    'LK': (
        'LK (left-half frame check) relay in the marker operated from an operated L (left) relay on the '
        'selected trunk link frame. This causes the marker to test junctors serving the left half of the trunk '
        'link frame.'
    ),
    'JCK': (
        'Operation of a JC- (Junctor cut-in) relay in the selected trunk link connector.'
    ),
    'TCHK': (
        'Marker TCHO-9 (test channel) relay operated to indicate channel numbers in the selected Junctor '
        'subgroup associated with the trunk link frame.'
    ),
    'TK': (
        'Test Check. The marker has completed all necessary functions to enable it to close a channel.'
    ),
    'RL': (
        'Marker grounded the RL lead to the originating register marker connector.'
    ),
    'HTR': (
        'Heavy Traffic. The marker has been idle less than one second from the previous marker seizure. '
        'When HTR is operated the marker skips or shortens the length of certain tests in order to speed up '
        'job completion time.'
    ),
    'HMS1': (
        'Hold Magnet Start 1. Marker initiated the operation of the selected channel hold magnets.'
    ),
    'LXPA': (
        'Line Crosspoints. Indicates the operation of the line switch hold magnet, and continuity on the sleeve lead.'
    ),
    'JXPA': (
        'Indicates operation of the LLF junctor switch hold magnet, and continuity of the sleeve lead.'
    ),
    'SL': (
        'Sleeve lead (TLF). Indicates the operation of the trunk switch hold magnet and continuity on the sleeve lead.'
    ),
    'JXP1': (
        'Junctor Crosspoints. Indicates the operation of the TLF junctor switch hold magnets.'

    ),
    'LXP1': (
        'Line Crosspoints 1. When punched, indicates its friend, the LXP relay is released. When unpunched, '
        'indicates that its friend, the LXP relay is operated.'
    ),
    'GLH': (
        'Ground Line Hold Magnet. The marker started to operate the hold magnet for the line on the LLF.'
    ),
    'CON': (
        'Continuity test has been successfully completed. This test is canceled at the museum via the operation '
        'of the CCT key in the MTC.'
    ),
    'GT2': (
        'Ground Test 2. Checks the operation of CON1, CON2, SL, and LLC1 and '
        'the *non operation* of LXP1, LXP, and SP relays.'
    ),
    'DCT': (
        'Double Connection Test. Double connection did not exist on the selected channel. This is good. '
        'ref CD-25550-01 7.5332'
    ),
    'RSC': (
        'Release Sender Connector. Registration of information transmitted by the marker to the outgoing sender was successful. '
        'The OSC may now release.'
    ),
    'AVK1': (
        'Sender advance check. The sender has successfully received the information transmitted by the marker, '
        'and has operated its AV relay to indicate that it is ready to outpulse the called number. '
        'The marker may now release the sender and complete the call.'
    ),
    'DCT1': (
        'Double Connection Test 1. Locks in the indication of a successful double connection test on '
        'terminating (call-forward) stage of an Intraoffice trunk connection. Also successful similar '
        'test on a dial tone connection, an outgoing, or an incoming trunk connection.'
    ),
    'DCT3': (
        'Double Connection Test 3. Indicates successful double connection test on a tandem or toll job. '
        'Indicates that the linkage to the tandem or toll completing path is set up.'
    ),
    'LK1': (
        'Linkage Check 1. This is a gating relay that indicates successful completion of the linkage between '
        'an originating line and an OR, an incoming trunk and a called line, IAO trunk and a called line, '
        'or outgoing trunk and a calling line. On IAO FLG calls, this relay operated allows the SCB to begin.'
    ),
    'DCT2': (
        'Double Connection Test 2. Successful completion of a double connection test on the callback (SCB) '
        'stage of an intraoffice (IAO) call.'
    ),
    'DIS1': (
        'Disconnect 1. The marker has completed all its functions and is ready to request that the marker '
        'connector make a normal disconnect. Sarah calls this DIZZY.'
    ),
    'OSE': (
        'Outgoing Sender End. Indicates that the outgoing sender selection process has completed.'
    ),
    'OSK': (
        'Outgoing Sender Check. Indicates that the outgoing sender selection process has completed.'
    ),
    'TSR': (
        'Timing Sender Registration. All sender connector relays had operated and the marker '
        'is to start timing for the operation of the sender memory relays. '
    ),
    'OST2': (
        'Outgoing Sender Timing 2. Sender registration timing is complete and the sender '
        'memory relays are being checked for holding before releasing the sender connector (OSC).'
    ),
    'RNT2': (
        'Recorder Number Timing 2. On AMA calls, the timing interval for operation of the '
        'recorder number (RN-) relays in the sender has completed.'
    ),
    'RNK': (
        'Recorder Number Check. On AMA calls, the marker has completed the check of the '
        'recorder number (RN-) relays in the sender.'
    ),
    'SLK1': (
        'Sender Link Check 1. Indicates that the lead through the sender link (OSL) hold '
        'magnets is continuous.'
    ),
    'SLK2': (
        'Sender Link Check 2. Indicates that the sender link (OSL) hold magnet has operated '
        'and closed the connection between the sender and the associated trunk.'
    ),
    'CGT': (
        'Cancel Ground Test. Indicates that the marker has canceled ground test as is required '
        'on certain types of connections, such as all originating and certain types of terminating calls, '
        'or if one of the cancel ground test keys is operated at the master test frame.'
    ),
    'XCL': 'Cross Class. More than one CL lead to an outgoing marker is grounded.',
    'XCR': 'Cross Compensating Resistance. More than one CR lead to an outgoing sender is grounded.',
    'XDL': 'Cross Deletion. More than on DL lead to an outgoing sender is grounded.',
    'XMB': 'Cross Message Billing. More than one MB lead to an outgoing sender is grounded.',
    'XCP': 'Cross Code Pattern. More than one CP lead to an outgoing sender is grounded.',
    'XOB': 'Both the NOB and OBS leads to the marker have operated.',
    'XTV': (
        'Cross Transverter. Both the TVA and the SCC leads in the marker operated, indicating '
        'this is somehow both a test call and a service call, which is not possible.'
    ),
    'XT5': 'Cross Transmission. False ground on unused transmission leads to the outgoing sender.',
    'XTB': 'Cross Trunk Block. More than one TB- relay in the marker has operated.',
    'XTG': 'Cross Trunk Group. More than one TG- relay in the marker has operated.',
    'XTB1': 'Cross Trunk Block Leads. More than one TB- lead to the TLF has battery on it.',
    'XTG1': 'Cross Trunk Group Leads. More than one TG- lead to the TLF has ground on it.',
    'XJC': 'Cross Junctor Connector Leads to the TLF.',
    'XJG': 'Cross Junctor Group Leads to the TLF.',
    'XJS': 'Cross JS- (Junctor Select Magnet) leads to the TLF.',
    'XLR': 'Cross Left and Right Side leads to the TLF.',
    'XTS': 'Cross Trunk Switch select magnets on the TLF.',
    'XLC': 'Crossed LC- (link connector) leads to the TLF.',
    'XLV': 'Crossed LV- (level) leads to the TLF.',
    'XAB': 'Indicates simultaneous operation of FAK and FBK in the marker, which is not allowed.',
    'XF': 'Crossed RF (regular frame) and EF (extension frame) leads.',
    'XSL': 'Crossed Sleeve Trunk. Indicates crossed AST and BST leads to the TLF.',
    'XTS1': 'False ground on TSX- (trunk select magnet) lead to the TLF during trunk selection.',
    'XPT': 'Crossed incoming trunk class and AMA recorder number leads to TLF.',
    'XRS': 'Crossed ringing switch select magnet leads to the TLF.',
    'XRS1': 'Both RS0/RS1 or multiple RS2-9 relays in the marker have operated.',
    'XFT': (
        'An unused FTC lead in the selected trunk link frame is falsely grounded or that the marker '
        'had been directed to a trunk link frame which does not include any trunks for the route.'
    ),
    'TRL': (
        'Ground placed on TRL lead to marker connector by the marker after a trouble record or an attempt to seize '
        'the trouble recorder on first trial failures. This causes the connector to reseize a marker on a second '
        'trial basis.'
    ),
    'BT': (
        'Busy Tone. The marker, by grounding BT lead to marker connector, requested: '
        'a. Originating register to return busy tone to calling subscriber or to release because of a second trial failure. '
        'b. Incoming register to release because of a second trial failure. '
        'c. Line link to release because of a second trial failure.'
    ),
    'MRL': (
        'Marker Release. The marker signaled the OR or IR through the connector to release the OR or IR.'
    ),
    'XHG': (
        'More than one HG- (horizontal group) relay operated in line link connector.'
    ),
    'XLG': (
        'More than one LG- (line group connector) relay operated in line link connector.'
    ),
    'XCS': (
        'Crossed Class of Service. More than one CS- (class of service) relay in the '
        'marker had operated due to crossed CS- leads in line link frame.'
    ),
    'XLS': (
        'Crossed Line Select Magnets. Crossed SM- leads to the line link frame.'
    ),
    'XLH': (
        'Crossed Line Hold Magnets. Crossed LH- leads to the line link frame.'
    ),
    'XLO': (
        'False ground on L0/L0B/L0K/G leads to LO (lockout for dial tone calls) relay in line link frame.'
    ),
    'XFUT': (
        'Crossed Frame Units and Tens. More than one FUT- (frame units test) or FTT- (frame '
        'tens test) relay in the marker had operated.'
    ),
    'XSS': (
        'Crossed Sender Select. More than one select magnet operated in the OSC (outsender connector).'
    ),
    'XS': (
        'Crossed Sender Connector. More than one S- relay operated in the OSC (outsender connector).'
    ),
    'XSA': (
        'Crossed Sender Connector Relay. More than one AMA relay in an outgoing sender connector '
        'has operated.'
    ),
    'XN': (
        'Cross Number control. Mismatch due to more than one called number control relay '
        '(TBIA, RIA, TNRI, NE, OAN, OBN) being operated in the marker.'
    ),
    'XFG': (
        'Crossed Frame Group. Simultaneous operation of FGO and FG1 relays in the marker.'
    ),
    'XPG': (
        'Crossed Pattern Group. Operation of more than one pattern (PA, PB, PC, PNR) relay in the marker.'
    ),
    'XPTN': (
        'Crossed Pattern relays. Operation of more than one P- relay in the marker.'
    ),
    'XT': (
        'Cross Translation control. Operation of more than one translation control relay in the marker. '
        '(THC, PHC, OA, OB, X11, 11X, TC5, TC6, TC7)'
    ),
    'XCLC': (
        'Crossed Class Control. Operation of more than one class control relay '
        '(OR, TAN, TOL, INC, RO) in the marker.'
    ),
    'XCKR': (
        'Cross or Ground on Class Check circuit. False ground on the class check circuit during a dial tone '
        'connection or during IAO and outgoing trunk connections.'
    ),
    'XTC': (
        'Crossed Traffic Control. False ground on TC lead to LLMC.'
    ),
    'XTC1': (
        'Crossed Traffic Control Auxiliary. False ground on TC1 lead to LLMC.'
    ),
    'XTRK': (
        'Cross First Trial Check lead. False ground on TRK lead to marker connectors '
        'when marker is functioning on a second trial.'
    ),
    'XTRL': (
        'Cross Trouble Release. False ground on TRL lead to the marker connector.'
    ),
    'XBT': (
        'Cross Busy Tone. False ground on BT lead to the marker connector.'
    ),
    'XRL': (
        'Cross Release. False ground on the RL lead to the originating register marker connector.'
    ),
    'XMRL': (
        'Cross Marker Release. False ground on MRL lead to the marker connector.'
    ),
    'XAN': (
        'Crossed Allotter Number. Not used at the museum.'
    ),
    'XCH': (
        'Crossed Channel Test. False ground on any of the J0-9, LH0-9 leads to a '
        'trunk link frame or LL0-9 leads to a line link frame.'
    ),
    'XVGA': (
        'Crossed Vertical Group A lead to the line link marker connector (LLMC).'
    ),
    'XVGB': (
        'Crossed Vertical Group B lead to the line link marker connector (LLMC).'
    ),
    'FTT0': (
        'Frame Tens Test 0. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used.'
    ),
    'FTT1': (
        'Frame Tens Test 1. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used.'
    ),
    'FTT2': (
        'Frame Tens Test 2. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used.'
    ),
    'FTT3': (
        'Frame Tens Test 3. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used.'
    ),
    'FTT4': (
        'Frame Tens Test 4. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used.'
    ),
    'FTT5': (
        'Frame Tens Test 5. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used.'
    ),
    'FUT0': (
        'Frame Units Test 0. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used (or the frame '
        'that was used on SOG calls).'
    ),
    'FUT1': (
        'Frame Units Test 1. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used (or the frame '
        'that was used on SOG calls).'
    ),
    'FUT2': (
        'Frame Units Test 2. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used (or the frame '
        'that was used on SOG calls).'
    ),
    'FUT3': (
        'Frame Units Test 3. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used (or the frame '
        'that was used on SOG calls).'
    ),
    'FUT4': (
        'Frame Units Test 4. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used (or the frame '
        'that was used on SOG calls).'
    ),
    'FUT5': (
        'Frame Units Test 5. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used (or the frame '
        'that was used on SOG calls).'
    ),
    'FUT6': (
        'Frame Units Test 6. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used (or the frame '
        'that was used on SOG calls).'
    ),
    'FUT7': (
        'Frame Units Test 7. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used (or the frame '
        'that was used on SOG calls).'
    ),
    'FUT8': (
        'Frame Units Test 8. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used (or the frame '
        'that was used on SOG calls).'
    ),
    'FUT9': (
        'Frame Units Test 9. Required to aid in closing the ST- lead to the line link connector. '
        'One FTT- and one FUT- performation indicates the line link frame to be used (or the frame '
        'that was used on SOG calls).'
    ),
    'VGT0': (
        'Vertical Group Test 0. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT1': (
        'Vertical Group Test 1. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT2': (
        'Vertical Group Test 2. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT3': (
        'Vertical Group Test 3. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT4': (
        'Vertical Group Test 4. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT5': (
        'Vertical Group Test 5. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT6': (
        'Vertical Group Test 6. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT7': (
        'Vertical Group Test 7. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT8': (
        'Vertical Group Test 8. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT9': (
        'Vertical Group Test 9. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT10': (
        'Vertical Group Test 10. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'VGT11': (
        'Vertical Group Test 11. The marker VGT- relay operated from the number group to identify '
        'the vertical group of the called line. On SOG calls, the VGT- relays indicate the vertical '
        'group of the calling line.'
    ),
    'HGT0': (
        'Horizontal Group Test. The marker HGT- relay operated from the number group to identify '
        'the horizontal group of the called line. On SOG calls, the HGT- relays indicate the horizontal '
        'group of the calling line.'
    ),
    'HGT1': (
        'Horizontal Group Test. The marker HGT- relay operated from the number group to identify '
        'the horizontal group of the called line. On SOG calls, the HGT- relays indicate the horizontal '
        'group of the calling line.'
    ),
    'HGT2': (
        'Horizontal Group Test. The marker HGT- relay operated from the number group to identify '
        'the horizontal group of the called line. On SOG calls, the HGT- relays indicate the horizontal '
        'group of the calling line.'
    ),
    'HGT3': (
        'Horizontal Group Test. The marker HGT- relay operated from the number group to identify '
        'the horizontal group of the called line. On SOG calls, the HGT- relays indicate the horizontal '
        'group of the calling line.'
    ),
    'HGT4': (
        'Horizontal Group Test. The marker HGT- relay operated from the number group to identify '
        'the horizontal group of the called line. On SOG calls, the HGT- relays indicate the horizontal '
        'group of the calling line.'
    ),
    'HGT5': (
        'Horizontal Group Test. The marker HGT- relay operated from the number group to identify '
        'the horizontal group of the called line. On SOG calls, the HGT- relays indicate the horizontal '
        'group of the calling line.'
    ),
    'HGT6': (
        'Horizontal Group Test. The marker HGT- relay operated from the number group to identify '
        'the horizontal group of the called line. On SOG calls, the HGT- relays indicate the horizontal '
        'group of the calling line.'
    ),
    'HGT7': (
        'Horizontal Group Test. The marker HGT- relay operated from the number group to identify '
        'the horizontal group of the called line. On SOG calls, the HGT- relays indicate the horizontal '
        'group of the calling line.'
    ),
    'HGT8': (
        'Horizontal Group Test. The marker HGT- relay operated from the number group to identify '
        'the horizontal group of the called line. On SOG calls, the HGT- relays indicate the horizontal '
        'group of the calling line.'
    ),
    'HGT9': (
        'Horizontal Group Test. The marker HGT- relay operated from the number group to identify '
        'the horizontal group of the called line. On SOG calls, the HGT- relays indicate the horizontal '
        'group of the calling line.'
    ),
    'VFT0': (
        'Vertical File Test 0. The marker VFT- relay operated from the number group to identify '
        'the vertical file of the called line. On SOG calls, the VFT- relays indicate the vertical '
        'file of the calling line.'
    ),
    'VFT1': (
        'Vertical File Test 1. The marker VFT- relay operated from the number group to identify '
        'the vertical file of the called line. On SOG calls, the VFT- relays indicate the vertical '
        'file of the calling line.'
    ),
    'VFT2': (
        'Vertical File Test 2. The marker VFT- relay operated from the number group to identify '
        'the vertical file of the called line. On SOG calls, the VFT- relays indicate the vertical '
        'file of the calling line.'
    ),
    'VFT3': (
        'Vertical File Test 3. The marker VFT- relay operated from the number group to identify '
        'the vertical file of the called line. On SOG calls, the VFT- relays indicate the vertical '
        'file of the calling line.'
    ),
    'VFT4': (
        'Vertical File Test 4. The marker VFT- relay operated from the number group to identify '
        'the vertical file of the called line. On SOG calls, the VFT- relays indicate the vertical '
        'file of the calling line.'
    ),
    'RCT1': (
        'Ringing Control Test 1. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT2': (
        'Ringing Control Test 2. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT3': (
        'Ringing Control Test 3. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT4': (
        'Ringing Control Test 4. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT5': (
        'Ringing Control Test 5. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT6': (
        'Ringing Control Test 6. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT7': (
        'Ringing Control Test 7. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT8': (
        'Ringing Control Test 8. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT9': (
        'Ringing Control Test 9. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT10': (
        'Ringing Control Test 10. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT11': (
        'Ringing Control Test 11. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT12': (
        'Ringing Control Test 12. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT13': (
        'Ringing Control Test 13. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT14': (
        'Ringing Control Test 14. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'RCT15': (
        'Ringing Control Test 15. The marker RCT- relay operated from the number group to control '
        'the ringing of the called line.'
    ),
    'CS0': (
        'Class of Service 0. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS1': (
        'Class of Service 1. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS2': (
        'Class of Service 2. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS3': (
        'Class of Service 3. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS4': (
        'Class of Service 4. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS5': (
        'Class of Service 5. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS6': (
        'Class of Service 6. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS7': (
        'Class of Service 7. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS8': (
        'Class of Service 8. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS9': (
        'Class of Service 9. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS10' :(
        'Class of Service 10. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS11': (
        'Class of Service 11. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS12': (
        'Class of Service 12. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS13': (
        'Class of Service 13. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS14': (
        'Class of Service 14. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS15': (
        'Class of Service 15. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS16': (
        'Class of Service 16. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS17': (
        'Class of Service 17. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS18': (
        'Class of Service 18. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS19': (
        'Class of Service 19. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS20': (
        'Class of Service 20. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS21': (
        'Class of Service 21. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS22': (
        'Class of Service 22. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS23': (
        'Class of Service 23. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS24': (
        'Class of Service 24. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS25': (
        'Class of Service 25. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS26': (
        'Class of Service 26. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS27': (
        'Class of Service 27. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS28': (
        'Class of Service 28. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'CS29': (
        'Class of Service 29. Class of service of the calling line on a dial tone connection, '
        'or class of service of a called coin ground start line on a terminating connection.'
    ),
    'TB0': (
        'Trunk Block 0. Part of the process of trunk selection. Operated by the chosen route relay '
        'and controls which TB- relay operates in the associated trunk link frame.'
    ),
    'TB1': (
        'Trunk Block 1. Part of the process of trunk selection. Operated by the chosen route relay '
        'and controls which TB- relay operates in the associated trunk link frame.'
    ),
    'TB2': (
        'Trunk Block 2. Part of the process of trunk selection. Operated by the chosen route relay '
        'and controls which TB- relay operates in the associated trunk link frame.'
    ),
    'TB3': (
        'Trunk Block 3. Part of the process of trunk selection. Operated by the chosen route relay '
        'and controls which TB- relay operates in the associated trunk link frame.'
    ),
    'TB4': (
        'Trunk Block 4. Part of the process of trunk selection. Operated by the chosen route relay '
        'and controls which TB- relay operates in the associated trunk link frame.'
    ),
    'TB5': (
        'Trunk Block 5. Part of the process of trunk selection. Operated by the chosen route relay '
        'and controls which TB- relay operates in the associated trunk link frame.'
    ),
    'TG0': (
        'Trunk Group 0. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG1': (
        'Trunk Group 1. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG2': (
        'Trunk Group 2. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG3': (
        'Trunk Group 3. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG4': (
        'Trunk Group 4. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG5': (
        'Trunk Group 5. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG6': (
        'Trunk Group 6. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG7': (
        'Trunk Group 7. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG8': (
        'Trunk Group 8. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG9': (
        'Trunk Group 9. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG10': (
        'Trunk Group 10. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG11': (
        'Trunk Group 11. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG12': (
        'Trunk Group 12. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG13': (
        'Trunk Group 13. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG14': (
        'Trunk Group 14. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG15': (
        'Trunk Group 15. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG16': (
        'Trunk Group 16. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG17': (
        'Trunk Group 17. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG18': (
        'Trunk Group 18. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'TG19': (
        'Trunk Group 19. Part of the process of trunk selection. Operated by the chosen route relay '
        'and provides ground to test the trunks in the associated route.'
    ),
    'FS1': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS2': 'Trunk link frame selected for this call. Always 0 in the museum.',    
    'FS3': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS4': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS5': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS6': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS7': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS8': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS9': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS10': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS11': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS12': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS13': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS14': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS15': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS16': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS17': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS18': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS19': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS20': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS21': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS22': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS23': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS24': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS25': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS26': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS27': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS28': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'FS29': 'Trunk link frame selected for this call. Always 0 in the museum.',
    'TS0': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS1': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS2': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS3': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS4': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS5': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS6': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS7': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS8': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS9': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS10': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS11': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS12': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS13': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS14': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS15': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS16': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS17': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS18': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'TS19': 'The trunk selected for this call from the possible twenty in the trunk block (TB).',
    'LV0': 'Level 0. Not used in the museum 5XB.',
    'LV1': 'Level 1. Not used in the museum 5XB.',
    'LV2': 'Level 2. The LV- relay operated in the TLF to indicate the horizontal level of the trunk switch on which this trunk appears.',
    'LV3': 'Level 3. The LV- relay operated in the TLF to indicate the horizontal level of the trunk switch on which this trunk appears.',
    'LV4': 'Level 4. The LV- relay operated in the TLF to indicate the horizontal level of the trunk switch on which this trunk appears.',
    'LV5': 'Level 5. The LV- relay operated in the TLF to indicate the horizontal level of the trunk switch on which this trunk appears.',
    'LV6': 'Level 6. The LV- relay operated in the TLF to indicate the horizontal level of the trunk switch on which this trunk appears.',
    'LV7': 'Level 7. The LV- relay operated in the TLF to indicate the horizontal level of the trunk switch on which this trunk appears.',
    'LV8': 'Level 8. The LV- relay operated in the TLF to indicate the horizontal level of the trunk switch on which this trunk appears.',
    'LV9': 'Level 9. The LV- relay operated in the TLF to indicate the horizontal level of the trunk switch on which this trunk appears.',
    'LC0': 'Link Connector 0. The LC- relay operated in the TLF. This also indicates the number of the trunk switch on which the trunk is located.',
    'LC1': 'Link Connector 1. The LC- relay operated in the TLF. This also indicates the number of the trunk switch on which the trunk is located.',
    'LC2': 'Link Connector 2. The LC- relay operated in the TLF. This also indicates the number of the trunk switch on which the trunk is located.',
    'LC3': 'Link Connector 3. The LC- relay operated in the TLF. This also indicates the number of the trunk switch on which the trunk is located.',
    'LC4': 'Link Connector 4. The LC- relay operated in the TLF. This also indicates the number of the trunk switch on which the trunk is located.',
    'LC5': 'Link Connector 5. The LC- relay operated in the TLF. This also indicates the number of the trunk switch on which the trunk is located.',
    'LC6': 'Link Connector 6. The LC- relay operated in the TLF. This also indicates the number of the trunk switch on which the trunk is located.',
    'LC7': 'Link Connector 7. The LC- relay operated in the TLF. This also indicates the number of the trunk switch on which the trunk is located.',
    'LC8': 'Link Connector 8. The LC- relay operated in the TLF. This also indicates the number of the trunk switch on which the trunk is located.',
    'LC9': 'Link Connector 9. The LC- relay operated in the TLF. This also indicates the number of the trunk switch on which the trunk is located.',
    'SF': 'Single Frame. The TLF signals the marker that it is not paired.',
    'PF': 'Paired Frame. The TLF signals the marker that it is paired with another TLF.',
    'TTF': 'Tripled Frame. The TLF signals the marker that it is paired with two other TLFs.',
    'RF': 'Regular Frame. Marker functions to operate the RF relay on the TLF.',
    'EF': 'Extension Frame. Marker functions to operate the EF relay on the TLF.',
    'NOC': 'No Class. No trunk class conditions are required for this call.',
    'CLG': 'Class Grounds. The marker CLG relay is operated to operate the required class relays in the outgoing trunk.',
    'CLT1': 'Class Timing 1. The marker is timing and awaiting the operation of the class relays in the outgoing trunk.',
    'CLT2': 'Class Timing 2. The marker has completed timing for the operation of the class relays and is now timing for their locking in feature.',
    'CLK': 'Class Check. The marker has successfully verified the lock-in of the class relay in the trunk.',
    'OTT': 'Operate Trunk Test. The marker has attempted to operate the TT relay in the trunk for testing purposes. Only used on test calls.',
    'TTK': 'The marker has successfully verified the operation of the TT relay in the trunk. Only used on test calls.',
    'ND1': 'No Digits. The marker prepares to send a No Digits signal to the sender.',
    'NDK': 'No Digits Check. The marker verified that the sender received and locked-in the No Digits signal.',
    'JC0': 'Junctor Cut-In 0. The JC0 relay has operated in the TLF, closing the J0-9 leads for idle junctor selection.',
    'JC1': 'Junctor Cut-In 1. The JC1 relay has operated in the TLF, closing the J0-9 leads for idle junctor selection.',
    'JC2': 'Junctor Cut-In 2. The JC2 relay has operated in the TLF, closing the J0-9 leads for idle junctor selection.',
    'JC3': 'Junctor Cut-In 3. The JC3 relay has operated in the TLF, closing the J0-9 leads for idle junctor selection.',
    'JC4': 'Junctor Cut-In 4. The JC4 relay has operated in the TLF, closing the J0-9 leads for idle junctor selection.',
    'JC5': 'Junctor Cut-In 5. The JC5 relay has operated in the TLF, closing the J0-9 leads for idle junctor selection.',
    'JC6': 'Junctor Cut-In 6. The JC6 relay has operated in the TLF, closing the J0-9 leads for idle junctor selection.',
    'JC7': 'Junctor Cut-In 7. The JC7 relay has operated in the TLF, closing the J0-9 leads for idle junctor selection.',
    'JC8': 'Junctor Cut-In 8. The JC8 relay has operated in the TLF, closing the J0-9 leads for idle junctor selection.',
    'JC9': 'Junctor Cut-In 9. The JC9 relay has operated in the TLF, closing the J0-9 leads for idle junctor selection.',
    'JG0': 'Junctor Group 0. The JG- relay operated in the marker, indicating the junctor group that will be used on this call.',
    'JG1': 'Junctor Group 1. The JG- relay operated in the marker, indicating the junctor group that will be used on this call.',
    'JG2': 'Junctor Group 2. The JG- relay operated in the marker, indicating the junctor group that will be used on this call.',
    'JG3': 'Junctor Group 3. The JG- relay operated in the marker, indicating the junctor group that will be used on this call.',
    'JG4': 'Junctor Group 4. The JG- relay operated in the marker, indicating the junctor group that will be used on this call.',
    'PNR': 'Pattern Normal. The marker PNR relay operated signifying that the junctor group is a standard group of 10 junctors.',
    'PA': 'Pattern A. The marker PA relay operated signifying that the junctor group contains fewer than 10 junctors.',
    'PB': 'Pattern B. The marker PB relay operated signifying that the junctor group contains fewer than 10 junctors.',
    'PC': 'Pattern C. The marker PC relay operated signifying that the junctor group contains fewer than 10 junctors.',
    'PE': 'Pattern E. The marker PE relay operated signifying that the junctor group contains fewer than 10 junctors.',
    'P0': (
        'Pattern 0. The P- (pattern) relay operated in the marker to identify the junctor subgroup pattern and '
        'the junctors which are available within the subgroup. The PA, PB or PC punch together with a '
        'P0-9 determine the available junctors according to the pattern.'
    ),
    'P1': (
        'Pattern 1. The P- (pattern) relay operated in the marker to identify the junctor subgroup pattern and '
        'the junctors which are available within the subgroup. The PA, PB or PC punch together with a '
        'P0-9 determine the available junctors according to the pattern.'
    ),
    'P2': (
        'Pattern 2. The P- (pattern) relay operated in the marker to identify the junctor subgroup pattern and '
        'the junctors which are available within the subgroup. The PA, PB or PC punch together with a '
        'P0-9 determine the available junctors according to the pattern.'
    ),
    'P3': (
        'Pattern 3. The P- (pattern) relay operated in the marker to identify the junctor subgroup pattern and '
        'the junctors which are available within the subgroup. The PA, PB or PC punch together with a '
        'P0-9 determine the available junctors according to the pattern.'
    ),
    'P4': (
        'Pattern 4. The P- (pattern) relay operated in the marker to identify the junctor subgroup pattern and '
        'the junctors which are available within the subgroup. The PA, PB or PC punch together with a '
        'P0-9 determine the available junctors according to the pattern.'
    ),
    'P5': (
        'Pattern 5. The P- (pattern) relay operated in the marker to identify the junctor subgroup pattern and '
        'the junctors which are available within the subgroup. The PA, PB or PC punch together with a '
        'P0-9 determine the available junctors according to the pattern.'
    ),
    'P6': (
        'Pattern 6. The P- (pattern) relay operated in the marker to identify the junctor subgroup pattern and '
        'the junctors which are available within the subgroup. The PA, PB or PC punch together with a '
        'P0-9 determine the available junctors according to the pattern.'
    ),
    'P7': (
        'Pattern 7. The P- (pattern) relay operated in the marker to identify the junctor subgroup pattern and '
        'the junctors which are available within the subgroup. The PA, PB or PC punch together with a '
        'P0-9 determine the available junctors according to the pattern.'
    ),
    'P8': (
        'Pattern 8. The P- (pattern) relay operated in the marker to identify the junctor subgroup pattern and '
        'the junctors which are available within the subgroup. The PA, PB or PC punch together with a '
        'P0-9 determine the available junctors according to the pattern.'
    ),
    'P9': (
        'Pattern 9. The P- (pattern) relay operated in the marker to identify the junctor subgroup pattern and '
        'the junctors which are available within the subgroup. The PA, PB or PC punch together with a '
        'P0-9 determine the available junctors according to the pattern.'
    ),
    'LL0': (
        'The line link used on a dial tone connection. This information, which was stored in the register while '
        'the call was being set up, is passed back to the marker after dialing, to indicate that this part of '
        'the channel is to be considered idle when making channel test for the subsequent stage of this connection.'
    ),
    'LL1': (
        'The line link used on a dial tone connection. This information, which was stored in the register while '
        'the call was being set up, is passed back to the marker after dialing, to indicate that this part of '
        'the channel is to be considered idle when making channel test for the subsequent stage of this connection.'
    ),
    'LL2': (
        'The line link used on a dial tone connection. This information, which was stored in the register while '
        'the call was being set up, is passed back to the marker after dialing, to indicate that this part of '
        'the channel is to be considered idle when making channel test for the subsequent stage of this connection.'
    ),
    'LL4': (
        'The line link used on a dial tone connection. This information, which was stored in the register while '
        'the call was being set up, is passed back to the marker after dialing, to indicate that this part of '
        'the channel is to be considered idle when making channel test for the subsequent stage of this connection.'
    ),
    'LL7': (
        'The line link used on a dial tone connection. This information, which was stored in the register while '
        'the call was being set up, is passed back to the marker after dialing, to indicate that this part of '
        'the channel is to be considered idle when making channel test for the subsequent stage of this connection.'
    ),
    'CH0': (
        'Selected channel. The channel number corresponds to the number of the select magnet operated on the LLF line switch, '
        'the junctor switch number on both the LLF and TLF, and vertical unit on the TLF trunk switch.'
    ),
    'CH1': (
        'Selected channel. The channel number corresponds to the number of the select magnet operated on the LLF line switch, '
        'the junctor switch number on both the LLF and TLF, and vertical unit on the TLF trunk switch.'
    ),
    'CH2': (
        'Selected channel. The channel number corresponds to the number of the select magnet operated on the LLF line switch, '
        'the junctor switch number on both the LLF and TLF, and vertical unit on the TLF trunk switch.'
    ),
    'CH3': (
        'Selected channel. The channel number corresponds to the number of the select magnet operated on the LLF line switch, '
        'the junctor switch number on both the LLF and TLF, and vertical unit on the TLF trunk switch.'
    ),
    'CH4': (
        'Selected channel. The channel number corresponds to the number of the select magnet operated on the LLF line switch, '
        'the junctor switch number on both the LLF and TLF, and vertical unit on the TLF trunk switch.'
    ),
    'CH5': (
        'Selected channel. The channel number corresponds to the number of the select magnet operated on the LLF line switch, '
        'the junctor switch number on both the LLF and TLF, and vertical unit on the TLF trunk switch.'
    ),
    'CH6': (
        'Selected channel. The channel number corresponds to the number of the select magnet operated on the LLF line switch, '
        'the junctor switch number on both the LLF and TLF, and vertical unit on the TLF trunk switch.'
    ),
    'CH7': (
        'Selected channel. The channel number corresponds to the number of the select magnet operated on the LLF line switch, '
        'the junctor switch number on both the LLF and TLF, and vertical unit on the TLF trunk switch.'
    ),
    'CH8': (
        'Selected channel. The channel number corresponds to the number of the select magnet operated on the LLF line switch, '
        'the junctor switch number on both the LLF and TLF, and vertical unit on the TLF trunk switch.'
    ),
    'CH9': (
        'Selected channel. The channel number corresponds to the number of the select magnet operated on the LLF line switch, '
        'the junctor switch number on both the LLF and TLF, and vertical unit on the TLF trunk switch.'
    ),
    'RS0': (
        'Ringing Selection 0. The select magnet that operated on the associated RSS to set ringing code for this call. 0 or 1 '
        'must be operated.'
    ),
    'RS1': (
        'Ringing Selection 1. The select magnet that operated on the associated RSS to set ringing code for this call. 0 or 1 '
        'must be operated.'
    ),
    'RS2': (
        'Ringing Selection 2. The select magnet that operated on the associated RSS to set ringing code for this call. One of 2-9 '
        'must be operated.'
    ),
    'RS3': (
        'Ringing Selection 3. The select magnet that operated on the associated RSS to set ringing code for this call. One of 2-9 '
        'must be operated.'
    ),
    'RS4': (
        'Ringing Selection 4. The select magnet that operated on the associated RSS to set ringing code for this call. One of 2-9 '
        'must be operated.'
    ),
    'RS5': (
        'Ringing Selection 5. The select magnet that operated on the associated RSS to set ringing code for this call. One of 2-9 '
        'must be operated.'
    ),
    'RS6': (
        'Ringing Selection 6. The select magnet that operated on the associated RSS to set ringing code for this call. One of 2-9 '
        'must be operated.'
    ),
    'RS7': (
        'Ringing Selection 7. The select magnet that operated on the associated RSS to set ringing code for this call. One of 2-9 '
        'must be operated.'
    ),
    'RS8': (
        'Ringing Selection 8. The select magnet that operated on the associated RSS to set ringing code for this call. One of 2-9 '
        'must be operated.'
    ),
    'RS9': (
        'Ringing Selection 9. The select magnet that operated on the associated RSS to set ringing code for this call. One of 2-9 '
        'must be operated.'
    ),
    'STP1': (
        'Junctor Step 1. The marker has made its first test of the junctor subgroup. This is normal.'
    ),
    'STP2': (
        'Junctor Step 2. The marker made another test of the junctor subgroup, as all were busy on the first attempt.'
    ),
    'NGCT0': 'Number group connector tens digit 0.',
    'NGCT1': 'Number group connector tens digit 1,',
    'NGCT2': 'Number group connector tens digit 2.',
    'NGCT3': 'Number group connector tens digit 3.',
    'NGCU0': 'Number group connector units digit 0.',
    'NGCU1': 'Number group connector units digit 1.',
    'NGCU2': 'Number group connector units digit 2.',
    'NGCU3': 'Number group connector units digit 3.',
    'NGCU4': 'Number group connector units digit 4.',
    'NGCU5': 'Number group connector units digit 5.',
    'NGCU6': 'Number group connector units digit 6.',
    'NGCU7': 'Number group connector units digit 7.',
    'NGCU8': 'Number group connector units digit 8.',
    'NGCU9': 'Number group connector units digit 9.',
    'HN0': 'The marker applied battery to the HB0 relay in the number group.',
    'HN1': 'The marker applied battery to the HB1 relay in the number group.',
    'HN2': 'The marker applied battery to the HB2 relay in the number group.',
    'HN3': 'The marker applied battery to the HB3 relay in the number group.',
    'HN4': 'The marker applied battery to the HB4 relay in the number group.',
    'HN5': 'The marker applied battery to the HB5 relay in the number group.',
    'HN6': 'The marker applied battery to the HB6 relay in the number group.',
    'HN7': 'The marker applied battery to the HB7 relay in the number group.',
    'HN8': 'The marker applied battery to the HB8 relay in the number group.',
    'HN9': 'The marker applied battery to the HB9 relay in the number group.',
    'T0': 'The marker applied battery to the TB0 relay in the number group.',
    'T1': 'The marker applied battery to the TB1 relay in the number group.',
    'T2': 'The marker applied battery to the TB2 relay in the number group.',
    'T3': 'The marker applied battery to the TB3 relay in the number group.',
    'T4': 'The marker applied battery to the TB4 relay in the number group.',
    'T5': 'The marker applied battery to the TB5 relay in the number group.',
    'T6': 'The marker applied battery to the TB6 relay in the number group.',
    'T7': 'The marker applied battery to the TB7 relay in the number group.',
    'T8': 'The marker applied battery to the TB8 relay in the number group.',
    'T9': 'The marker applied battery to the TB9 relay in the number group.',
    'U0': 'The marker applied battery to the U0 relay in the number group.',
    'U1': 'The marker applied battery to the U1 relay in the number group.',
    'U2': 'The marker applied battery to the U2 relay in the number group.',
    'U3': 'The marker applied battery to the U3 relay in the number group.',
    'U4': 'The marker applied battery to the U4 relay in the number group.',
    'U5': 'The marker applied battery to the U5 relay in the number group.',
    'U6': 'The marker applied battery to the U6 relay in the number group.',
    'U7': 'The marker applied battery to the U7 relay in the number group.',
    'U8': 'The marker applied battery to the U8 relay in the number group.',
    'U9': 'The marker applied battery to the U9 relay in the number group.',
    'SNG': 'The marker is attempting to Seize the Number Group.',
    'NGK': 'Number Group Check. The marker has seized the number group and operated its MCA relay.',
    'NGK1': 'Number Group Check Auxiliary. Battery has been supplied to the F, L, and G leads to the NG.',
    'UK': 'Units Check. The U- (units) relay in the number group operated.',
    'HTUK': 'Satisfactory operation of the Hundreds, Tens, and Units relays in the number group.',
    'TNK': 'Trunk Number Check. That on a toll/tandem or coin junctor call, that a trunk number is involved.',
    'PTK': (
        'Physical Theoretical Check. The connection has satisfactorily completed the physical and theoretical office check.'
    ),
    'PBX1': (
        'Private Branch Exchange. The call is to a PBX subscriber or to other lines having PBX hunting.'
    ),
    'SLCK': (
        'The SC (sleeve connector) relay in the number group had operated and locked, in series with the SLCK '
        '(sleeve connector check) relay in the marker.'
    ),
    'CKO': (
        'Check Operation. The marker has begun a recycle of called line identification on a PBX, RI, TBI, or BN class.'
    ),
    'CKR': (
        'Check Release. The marker has completed the recycle of called line identification on a PBX, RI, TBI, or BN class.'
    ),
    'A': (
        'The marker performed a number group advance from one tens block relay to the next, in the event '
        'that no idle line is found in the first tens block or to prepare the marker to set up busy-back if all '
        'PBX lines are busy.'
    ),
    'AK': 'Advance Check. The marker completed advance from one tens block to another.',
    'SAE': 'There is at least one idle PBX line available within the tens block.',
    'EG': 'End Group. NG reports that the end of the tens block has been reached without finding an idle line.',
    'RNG': 'Release Number Group. The called line information has been recorded and the marker will release the NG.',
    'NR': (
        'Number Release. Marker RNG (release number group), TBI (trouble Intercept), RI (regular intercept), BN (blank number), '
        'or PUL (plugged-up line) relay operated to release the number group.'
    ),
    'PTN': (
        'Physical Theoretical Number. The HB- (hundreds block) relay operated in a number '
        'group serving a nondiscriminating office.'
    ),
    'PN': (
        'Physical Number. The HB- (hundreds block) relay operated in a number group serving a physical office.'
    ),
    'TN': (
        'Theoretical Number. The HB- (hundreds block) relay operated in a number group serving a theoretical office.'
    ),
    'EN': (
        'Extra-theoretical Number. The HB- (hundreds block) relay operated in a number group serving an extra-theoretical office.'
    ),
    'PBN': (
        'Permanently Busy Number. The marker PBN relay operated to record that the called number is a permanently busy line.'
    ),
    'FNA': (
        'Free Number Group A. The operated FN- (free number) relay In the number group is cross-connected to operate the marker FNA relay '
        'when 4-wire ringing selection switches are installed.'
    ),
    'FNB': (
        'The operated FN- (free number) relay In the number group is cross-connected to operate the marker FNB relay '
        'when 6-wire or a combination of 4- and 6-wire ringing selection switches are installed.'
    ),
    'LIN': 'Local Intercept. The marker is preparing to route this INC, IAO, or RV call to intercept with local (non-toll) treatment.',
    'TIN': 'Toll Intercept. The marker is preparing to route this incoming call call to a toll intercept position or recording.',
    'BN': 'The marker recognized that this call is to an unassigned number with no cross connections in the number group.',
    'RI': 'Regulat Intercept. The marker is preparing to route this call to a regular intercept trunk.',
    'TBI': 'Trouble Intercept. The marker is preparing to route this call to a trouble intercept trunk.',
    'TBH': (
        'The marker functioned to operate its TBH (trouble intercept, hold magnet, operate ringing switch) '
        'relay to reset the trunk ringing switch for ringing into a trouble intercept trunk.'
    ),
    'OV': 'Overflow. The marker will set the incoming trunk to return overflow (reorder) signal.',
    'BY': 'Busy. The marker will set the incoming trunk to return busy signal.',
    'OFH': 'Overflow Hold Magnet. The marker operated its OFH relay to reset the RSS for BY or OV condition.',
    'PUL': 'Plugged-Up Line. The marker has recognized that the called line on plugup for route to operator or intercept.',
    'LCH': 'Local Charge. The marker operated its LCH relay to set local charge supervision on this call.',
    'TCH': 'Toll Charge. The marker operated its TCH relay to set toll charge supervision on this call.',
    'RSK': 'Ringing Switch Select Magnet Check. A ringing switch select magnet has operated.',
    'LI': 'Indicates to the marker that the called line is idle and there is an idle channel available for connection to it.',
    'TCK1': (
        'Talking Charge Check. The marker\'s TCH relay has operated to indicate that the talking charge (TC) lead '
        'has continuity.',
    ),
    'SRK': (
        'Start Ringing Check. The marker has checked the continuity of the RC lead to the trunk and operated the RC '
        'relay, in turn causing the operation of the RSS hold magnet.'
    ),
    'RCK2': (
        'Ringing Crosspoint Check. Indicates the marker has checked the continuity of the RSS crosspoints.'
    ),
    'RCK3': (
        'Ringing Crosspoint Check 3. Indicates the marker has satisfactorily checked the charge and ringing conditions in the trunk.'
    ),
    'EX': (
        'Extra. This punch is user-configurable and can be assigned by maintenance forces to observe a condition that is otherwise not '
        'represented on the trouble card. See EXB and EXG cross connections in the marker SD.'
    ),
    'DT0': 'Day Tens 0. The tens digit of the day of the month.',
    'DT1': 'Day Tens 1. The tens digit of the day of the month.',
    'DT2': 'Day Tens 2. The tens digit of the day of the month.',
    'DT4': 'Day Tens 4. The tens digit of the day of the month.',
    'DT7': 'Day Tens 7. The tens digit of the day of the month.',
    'DU0': 'Day Units 0. The units digit of the day of the month.',
    'DU1': 'Day Units 1. The units digit of the day of the month.',
    'DU2': 'Day Units 2. The units digit of the day of the month.',
    'DU4': 'Day Units 4. The units digit of the day of the month.',
    'DU7': 'Day Units 7. The units digit of the day of the month.',
    'HT0': "Hour Tens 0. The tens digit of the hour in 24 hour time.",
    'HT1': "Hour Tens 1. The tens digit of the hour in 24 hour time.",
    'HT2': "Hour Tens 2. The tens digit of the hour in 24 hour time.",
    'HT4': "Hour Tens 4. The tens digit of the hour in 24 hour time.",
    'HT7': "Hour Tens 7. The tens digit of the hour in 24 hour time.",
    'HU0': "Hour Units 0. The units digit of the hour in 24 hour time.",
    'HU1': "Hour Units 1. The units digit of the hour in 24 hour time.",
    'HU2': "Hour Units 2. The units digit of the hour in 24 hour time.",
    'HU4': "Hour Units 4. The units digit of the hour in 24 hour time.",
    'HU7': "Hour Units 7. The units digit of the hour in 24 hour time.",
    'MT0': "Minute Tens 0. The tens digit of the minute of the hour.",
    'MT1': "Minute Tens 1. The tens digit of the minute of the hour.",
    'MT2': "Minute Tens 2. The tens digit of the minute of the hour.",
    'MT4': "Minute Tens 4. The tens digit of the minute of the hour.",
    'MT7': "Minute Tens 7. The tens digit of the minute of the hour.",
    'MU0': "Minute Units 0. The units digit of the minute of the hour.",
    'MU1': "Minute Units 1. The units digit of the minute of the hour.",
    'MU2': "Minute Units 2. The units digit of the minute of the hour.",
    'MU4': "Minute Units 4. The units digit of the minute of the hour.",
    'MU7': "Minute Units 7. The units digit of the minute of the hour.",

}   

def describe(name: str) -> str:
    """
    Return a human‑readable description for *name*; if the name isn’t
    known the raw name is echoed back.
    """
    return PUNCH_DESCRIPTIONS.get(name, f"unknown punch '{name}'")