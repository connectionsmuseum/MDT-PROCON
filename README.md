# MDT-PROCON

This set of applications functions as a replacement for both the PK-AA32 PROCON in the No. 5 Crossbar, and the SCC (Switching Control Center) that would ordinarily be located in a centralized switching entity downtown. The PROCON was designed to intercept trouble records originally destined for the KS-13834 Trouble Recorder, and instead direct that information to the SCC, via a modem and a dedicated wet pair. This allowed for centralized maintenance of a remote No. 5 Crossbar office, without needing a switchman to be on-site to observe the trouble records manually.

Using these two applications, we can do the same. The MDT portion of the code runs on a NodeMCU (ESP-32), which reads a matrix of 160 inputs multipled several times in order to produce a trouble record. (Kids these days would refer to this as a core dump.) The trouble record is then sent to the SCC via an HTTP POST, where it is converted to an actual image of a trouble card, and from there, can be posted to Twitter, or viewed in a browser.
