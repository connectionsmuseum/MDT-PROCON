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
        'test in the allotted time. This may indicate a problem with the outgoing trunk, '
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
        'It is likely that this is not wired at the museum as of 2026.'
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
        'the line link appearance of the tandem trunk in the number group.'
    ),
    'TT-': (
        'Tens Trunk. Used on tandem calls to identify the tens digit of the line link '
        'appearance of the tandem trunk in the number group.'
    ),
    'UT-': (
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
        'this card was using GS2)', 
    ),
    'GS2': (
        'Ground Supply 2. The marker has advanced to Ground Supply 3. GS3 contains route relays 20-29, '
        'and is used for second-choice routes when the marker is unable to establish a connection using '
        'a first choice route. Routes here include Kercheep, and any primary route that does not have its '
        'own alternate.'
        '(A punch here indicates we have *advanced* past Ground Supply 2 and the operation that dropped '
        'this card was using GS3)'
    ),
    'GS3': (
        'Ground Supply 3. The marker has advanced to Ground Supply 4. GS4 contains route relays 10-19, '
        'and is used for third-choice routes when the marker is unable to establish a connection using ' 
        'a second choice route. Not used in the museum. '
        '(A punch here indicates we have *advanced* past Ground Supply 3 and the operation that dropped '
        'this card was using GS4)'
    ),
    'GS4': (
        'Ground Supply 4. The marker has advanced to Ground Supply 5. GS5 contains route relays 6-9, '
        'or 0-5 depending on the marker. Routes in this ground supply are generally reserved for intercept, '
        'permanent signal, or an announcement, and do not usually have an alternate. '
        '(A punch here indicates we have *advanced* past Ground Supply 4 and the operation that dropped '
        'this card was using GS5)'
    ),
    'GS5': (
        'Ground Supply 5. THe marker has advanced to Ground Supply 6. GS6 contains routes of last resort, '
        'and there can be no further advancement past here. '
        '(A punch here indicates we have *advanced* past Ground Supply 5 and the operation that dropped '
        'this card was using GS6)'
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
        'The originating register signaled the marker that this is a ring party call.'
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
    'NOB': 'The NOB relay in the sender should have operated to indicate this call is not on service observation.',
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
        'marginal trunk test is required.'
    ),
    'CL4': (
        'To a DP sender, that battery and ground pulsing is required, as opposed to loop disconnect pulsing.'
    ),
    'CL5': (
        'Subscriber access to CX In te rto ll or CX 2-way trunks.'
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
        'One of the N1A/N2A/N3A/N4A (number translator cut-in '
        'auxiliary) relays in the marker operated on an incoming '
        'or intra-office trunk connection. These relays '
        'are operated for number group translation of the '
        'called number.'
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
        'The cut-in relay of a selected route operated, thus closing the test leads to the '
        'trunk link connector frames serving this route.'
    ),
    'FTCK': (
        'Frame Test Check. Trunk link frames have been tested for the presence of an idle trunk '
        'for the selected route, and at least one frame has an idle route available.'
    ),
    'SNK': (
        'If not perforated, the marker released the selections made before a recycle takes place.'
    ),
    'CK': 'Marker preference (MP or E) relay on the selected trunk link frame operated.',
    'FML': (
        'Frame Memory Lock relay in the marker operated to insure a different trunk link frame '
        'is selected on the next call. Ineffective at museum, but important from a sequence-of-events perspective.'
    ),
    'MAK1': (
        'Marker Connector Cut-In Check. Both halves of the MCA relay operated in the selected Trunk Link Connector (TLC).'
    ),
    'TBK': (
        'Trunk Block Check. A TB- relay of the selected trunk link connector operated.'
    ),
    'ORK': (
        'Originating Register Check. Also coincident with RK1. '
        'RK1 indicates that no false ground is present on the calling-line identification '
        'leads from the OR. '
        'ORK indicates that the called number from the OR/IR has been properly received and validated.'
    ),
    'RK2': (
        'Register Check 2. Indicates that no false battery was detected on the calling line leads from the OR. '
        'Operation of both RK1 and RK2 indicates that the calling line information from the OR has been properly '
        'received and validated.'
    ),
    'VTK1': (
        'Vertical Group Test Check. When punched, indicates that only one of the VGT0-11 relays is locked operated '
        'in the marker for vertical group selection. This is a test for the presence of a valid vertical group selection.'
    ),
    'HTK1': (
        'Horizontal Group Test Check. When punched, indicates that only one of the HGT0-9 relays is locked operated '
        'in the marker for horizontal group selection. This is a test for the presence of a valid horizontal group selection.'
    ),
    'FTK1': (
        'Vertical File Test Check. When punched, indicates that only one of the VFT0-4 relays is locked operated for '
        'vertical file selection. This is a test for the presence of a valid vertical file selection.'
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
        'selected trunk link frame. This causes the marker to test Junctors serving the right half of the trunk '
        'link frame.'
    ),
    'LK': (
        'LK (left-half frame check) relay in the marker operated from an operated L (left) relay on the '
        'selected trunk link frame. This causes the marker to test Junctors serving the left half of the trunk '
        'link frame.'
    ),
    'JCK': (
        'Operation of a JC- (Junctor cut-in) relay in the selected trunk link connector has operated the JCKO '
        'and JCK1 relays in the marker. If CHO or CH1 operates, JCKO and JCK1 will release.'
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
        'Line hold magnet. Indicates operation of the line hold magnet.'
    ),
    'JXPA': (
        'Junctor sleeve continuity has been checked.'
    ),
    'SL': (
        'Sleeve lead (TLF). Indicates the closure of the trunk link frame crosspoints.'
    ),
    'JXP1': (
        'Junctor crosspoints closed.'
    ),
    'LXP1': (
        'Line Crosspoints 1. When punched, indicates its friend, the LXP relay is released. When unpunched, indicates that its friend, the '
        'LXP relay is operated.'
    ),
    'GLH': (
        'Ground Line Hold Magnet. The marker started to operate the hold magnet for the line on the LLF.'
    ),
    'CON': (
        'Continuity test has been successfully completed. This test is canceled at the museum via the operation of the CCT key in the MTC.'
    ),
    'GT2': (
        'Ground Test 2. Checks the operation of CON1, CON2, SL, and LLCl and '
        'the nonoperation of LXP1, LXP, and SP relays.'
    ),
    'DCT': (
        'Double Connection Test. Double connection did not exist on the selected channel. This is good. '
        'ref CD-25550-01 7.5332'
    ),
    'RSC': (
        'Release Sender Connector. Registration of information transmitted by the marker to the outgoing sender was successful. The OSC may '
        'now release.'
    ),

}

def describe(name: str) -> str:
    """
    Return a human‑readable description for *name*; if the name isn’t
    known the raw name is echoed back.
    """
    return PUNCH_DESCRIPTIONS.get(name, f"unknown punch '{name}'")