"""
mapping of punch names to a human‑readable explanation.

"""

PUNCH_DESCRIPTIONS: dict[str, str] = {
    'TI': 'Trouble encountered on a service, monitored, or test call.',
    'MTPT': 'Marker, transverter pretranslator test from MTF.',
    'SRT': 'Sender-register test from MTF.',
    'TKT': 'Trunk test from MTF.',
    'M': "This call was being monitored by the AMRST",
    'MLV': 'Marker Line Verification.',
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
    'DR0': (
        'This call was handled by Completing Marker 0, which is the wirespring '
        'marker SD-26002-01.'
    ),
    'DR1': (
        'This call was handled by Completing Marker 1, which is the U&Y relay '
        'marker, SD-25550-01.'
    ),
    'DR8': 'This call was handled by the Dial Tone Marker, SD-26001-01',
    '1TR': (
        'This card was the result of the markers first attempt to handle the call. '
        'If there was a second attempt, there may be a card immediately '
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
        'test in the allotted time. This may indicate a problem with the '
        'outgoing trunk, '
        'since the TG test requires a wet loop to complete.'
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
        'It is likely '
        'that this is not wired at the museum as of 2026.'
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
        'This was a Terminating call. The call originated from a line in a different '
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
        'Sender Outgoing. An outgoing call that does require a sender. This includes '
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
    'HT-': (
        'Hundreds Trunk. Used on tandem calls to identify the hundreds digit of '
        'the Line Link appearance of the tandem trunk in the number group.'
    ),
    'TT-': (
        'Tens Trunk. Used on tandem calls to identify the tens digit of the Line Link '
        'appearance of the tandem trunk in the number group.'
    ),
    'UT-': (
        'Units Trunk. Used on tandem calls to identify the units digit of the Line Link '
        'appearance of the tandem trunk in the number group.'
    ),
    'CN-RG-': (
        'The position of the OR in the ORMC connector group. In the museum, this '
        'is identical to the OR number.'
    ),
    'FG-': 'Trunk Link Frame Group. Always 0 in the museum.',
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
        'A register has directed the marker to employ its TT translator for this '
        'connection.'
    ),
    '2DT': (
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
        'for this connection.'
    ),
    '11': (
        'A register has directed the marker to employ its 11 translator for '
        'this connection.'
    ),
    'OA': (
        'On an incoming trunk connection, this is the office unit to which the '
        'marker should complete the connection.'
    ),
    'OB': (
        'On an incoming trunk connection, this is the office unit to which the '
        'marker should complete the connection.'
    ),
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
        'is an originating connection. If you see this, it means the call came from a '
        '5XB line.'
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
    'TF-': (
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
    'A-': (
        'The A-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.'
    ),
    'B-': (
        'The B-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.'
    ),
    'C-': (
        'The C-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.'
    ),
    'D-': (
        'The D-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.'
    ),
    'E-': (
        'The E-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.'
    ),
    'F-': (
        'The F-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.'
    ),
    'G-': (
        'The G-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.'
    ),
    'H-': (
        'The H-digit received from the OR or IR. Must be in 2-of-5 code in order to be valid.'
    ),
    'J-': (
        'The J-digit received from the OR or IR. Not used at museum.'
    ),
    'K-': (
        'The K-digit received from the OR or IR. Not used at museum.'
    ),
    'L-': (
        'The L-digit received from the OR or IR. Not used at museum.'
    ),
    'M-': (
        'The M-digit received from the OR or IR. Not used at museum.'
    ),
    'GS1': (
        'Ground Supply 1. The marker has advanced to Ground Supply 2, since it was unable to establish '
        'a route for the call in GS1. GS2 contains route relays 30-39 and is not used in the museum.). '
        '(A punch here indicates we have *advanced* past Ground Supply 1 and the operation that dropped '
        'this card was using GS2.)', 
    ),
    'GS2': (
        'Ground Supply 2. The marker has advanced to Ground Supply 3. GS3 contains route relays 20-29, '
        'and is used for second-choice routes when the marker is unable to establish a connection using '
        'a first choice route. Routes here include Kercheep, and any primary route that does not have its '
        'own alternate.'
        '(A punch here indicates we have *advanced* past Ground Supply 2 and the operation that dropped '
        'this card was using GS3.)'
    ),
    'GS3': (
        'Ground Supply 3. The marker has advanced to Ground Supply 4. GS4 contains route relays 10-19, '
        'and is used for third-choice routes when the marker is unable to establish a connection using ' 
        'a second choice route. Not used in the museum. '
        '(A punch here indicates we have *advanced* past Ground Supply 3 and the operation that dropped '
        'this card was using GS4.)'
    ),
    'GS4': (
        'Ground Supply 4. The marker has advanced to Ground Supply 5. GS5 contains route relays 6-9, '
        'or 0-5 depending on the marker. Routes in this ground supply are generally reserved for intercept, '
        'permanent signal, or an announcement, and do not usually have an alternate. '
        '(A punch here indicates we have *advanced* past Ground Supply 4 and the operation that dropped '
        'this card was using GS5.)'
    ),
    'GS5': (
        'Ground Supply 5. THe marker has advanced to Ground Supply 6. GS6 contains routes of last resort, '
        'and there can be no further advancement past here. '
        '(A punch here indicates we have *advanced* past Ground Supply 5 and the operation that dropped '
        'this card was using GS6.)'
    ),
    'CNS': (
        'Coin Service. This call is a coin class.'
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
    'RP': (
        'The originating reg ister signaled the marker that this is a ring party call.'
    ),
    'FR0': (
        'Outgoing Sender Connector (OSC) frame zero was used on this call.'
    ),
    'FR1': (
        'Outgoing Sender Connector (OSC) frame one was used on this call.'
    ),
    'FR2': (
        'Outgoing Sender Connector (OSC) frame two was used on this call.'
    ),
    'FR3': (
        'Outgoing Sender Connector (OSC) frame three was used on this call.'
    ),
    'FR4': (
        'Outgoing Sender Connector (OSC) frame four was used on this call.'
    ),
    'CN0': (
        'Connector 0 in the selected OSC was used on this call.'
    ),
    'CN1': (
        'Connector 1 in the selected OSC was used on this call.'
    ),
    'CN2': (
        'Connector 2 in the selected OSC was used on this call.'
    ),
    'CN3': (
        'Connector 3 in the selected OSC was used on this call.'
    ),
    'S0': (
        'Sender 0 in the selected OSC was used on this call.'
    ),
    'S1': (
        'Sender 1 in the selected OSC was used on this call.'
    ),
    'S2': (
        'Sender 2 in the selected OSC was used on this call.'
    ),
    'S3': (
        'Sender 3 in the selected OSC was used on this call.'
    ),
    'S4': (
        'Sender 4 in the selected OSC was used on this call.'
    ),
    'S5': (
        'Sender 5 in the selected OSC was used on this call.'
    ),
    'S6': (
        'Sender 6 in the selected OSC was used on this call.'
    ),
    'S7': (
        'Sender 7 in the selected OSC was used on this call.'
    ),
    'S8': (
        'Sender 8 in the selected OSC was used on this call.'
    ),
    'S9': (
        'Sender 9 in the selected OSC was used on this call.'
    ),
    'S10': (
        'Sender 10 in the selected OSC was used on this call.'
    ),
    'S11': (
        'Sender 11 in the selected OSC was used on this call.'
    ),
    'S12': (
        'Sender 12 in the selected OSC was used on this call.'
    ),
    'OSG0': (
        'Outgoing Sender Group 0 was selected by the marker.'
    ),
    'OSG1': (
        'Outgoing Sender Group 1 was selected by the marker.'
    ),
    'OSG2': (
        'Outgoing Sender Group 2 was selected by the marker.'
    ),
    'OSG3': (
        'Outgoing Sender Group 3 was selected by the marker.'
    ),
    'OSG4': (
        'Outgoing Sender Group 4 was selected by the marker.'
    ),
    'OSG5': (
        'Outgoing Sender Group 5 was selected by the marker.'
    ),
    'OSG6': (
        'Outgoing Sender Group 6 was selected by the marker.'
    ),
    'OSG7': (
        'Outgoing Sender Group 7 was selected by the marker.'
    ),
    'OSG8': (
        'Outgoing Sender Group 8 was selected by the marker.'
    ),
    'OSG9': (
        'Outgoing Sender Group 9 was selected by the marker.'
    ),
    'OSG10': (
        'Outgoing Sender Group 10 was selected by the marker.'
    ),
    'OSG11': (
        'Outgoing Sender Group 11 was selected by the marker.'
    ),
    'SSA': (
        'Outgoing sender subgroup A was seized by the marker.'
    ),
    'SSB': (
        'Outgoing sender subgroup B was seized by the marker.'
    ),
    'OS0': (
        'Outgoing sender 0 was selected in the sender group.'
    ),
    'OS1': (
        'Outgoing sender 1 was selected in the sender group.'
    ),
    'OS2': (
        'Outgoing sender 2 was selected in the sender group.'
    ),
    'OS3': (
        'Outgoing sender 3 was selected in the sender group.'
    ),
    'OS4': (
        'Outgoing sender 4 was selected in the sender group.'
    ),
    'RO\'': (
        'Operation of the RO (Reorder) relay In the outgoing sender to set the outgoing trunk for reorder.'
    ),
    
}

def describe(name: str) -> str:
    """
    Return a human‑readable description for *name*; if the name isn’t
    known the raw name is echoed back.
    """
    return PUNCH_DESCRIPTIONS.get(name, f"unknown punch '{name}'")