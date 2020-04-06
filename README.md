# asterisk_blacklist
[blcall]
exten => _XXXX,1,GotoIf($[${BLACKLIST()}]?black)
exten => s,n,Dial(SIP/${EXTEN},,m)
exten => s(black),n,Hangup()
