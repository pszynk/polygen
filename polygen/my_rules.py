3013 "MALWARE-CNC Win.Trojan.MadnessPro outbound connection attempt"
content:"/?";
content:"uid=";
content:"&mk=";
content:"&os=";
content:"&rs=";
content:"&c=";
content:"&rq=";

3086 "MALWARE-CNC Win.Trojan.Symmi variant HTTP response attempt"
content:"%set_intercepts%";
content:"%ban_contact%";
content:"%ebaylive%";
content:"%dep_host%";
content:"%relay_soxid%";

3225 "MALWARE-CNC Win.Trojan.HawkEye keylogger exfiltration attempt"
content:"Subject|3A 20|HawkEye Keylogger|20 7C 20|";
content:"=0D=0APC";
content:"=0D=0AInstalled";
content:"=0D=0AOperating System"; within:75; distance 15;
content:"=0D=0AInternal IP"; within:200; distance 10;
content:"=0D=0AExternal IP"; within:50; distance 5;

1303 "PROTOCOL-RPC status GHBN format string attack"
content:"|00 01 86 B8|"; depth:4; offset:12;
content:"|00 00 00 02|"; within:4; distance:4;
content:"%x %x"; within:256;
content:"|00 00 00 00|"; depth:4; offset:4;

1634 "OS-WINDOWS SMB-DS DCERPC Messenger Service buffer overflow attempt"
content:"|FF|SMB%"; depth:5; offset:4;
content:"&|00|"; within:2; distance:56;
content:"|5C 00|P|00|I|00|P|00|E|00 5C 00|"; within:12; distance:5;
content:"|04 00|"; within:2;

2445 "MALWARE-CNC Win.Trojan.Gupd variant outbound connection"
content:"cstype="; depth:7;
content:"&authname="; within:48; distance:1;
content:"&authpass="; within:48; distance:1;
content:"&hostname="; within:48; distance:1;
content:"&ostype="; within:256; distance:1;
content:"&macaddr="; within:64; distance:16;
content:"&owner="; within:48; distance:17;
