
********************************************************************************
NO pos constraints
********************************************************************************

2790 "MALWARE-CNC Win.Trojan.Rovnix malicious download"
content:"/config.php?";
content:"version=";
content:"user=";
content:"server=";
content:"id=";
content:"crc=";
content:"id=";

XX
3013 "MALWARE-CNC Win.Trojan.MadnessPro outbound connection attempt"
content:"/?";
content:"uid=";
content:"&mk=";
content:"&os=";
content:"&rs=";
content:"&c=";
content:"&rq=";

3071 "MALWARE-CNC Win.Banker.Delf variant outbound connection attempt"
content:"POST";
content:"/notify.php";
content:"Content-Length: 0|0D 0A|";
content:" HTTP/1.0|0D 0A|";
content:"Content-Type: application/x-www-form-urlencoded|0D 0A|";
content:"User-Agent|3A 20|Mozilla/4.0 (compatible|3B| MyApp)|0D 0A 0D 0A|";

X
3086 "MALWARE-CNC Win.Trojan.Symmi variant HTTP response attempt"
content:"%set_intercepts%";
content:"%ban_contact%";
content:"%ebaylive%";
content:"%dep_host%";
content:"%relay_soxid%";

3170 "MALWARE-CNC Win.Trojan.Darkhotel outbound connection attempt"
content:"/bin/read_i.php?";
content:"a1=";
content:"&a2=step2-down";
content:"&a3=";
content:"&a4=";

3127 "MALWARE-CNC Win.Trojan.Graftor variant outbound connection"
content:"form-data|3B| name=|22|PLUG|22 0D 0A|";
content:"form-data|3B| name=|22|PC|22 0D 0A|";
content:"form-data|3B| name=|22|SEG|22 0D 0A|"; distance:0;
content:"User-Agent: Mozilla/3.0 (compatible|3B| Indy Library)|0D 0A|";

3165 "MALWARE-CNC Win.Dropper.Ch variant outbound connection attempt"
content:"POST";
content:"/tasks.php";
content:"Content-length:";
content:"Content-type:";


********************************************************************************
SOME pos constraints
********************************************************************************

3000 "MALWARE-CNC Win.Trojan.Bancos variant outbound connection attempt"
content:"POST";
content:"/js/prototype/order.php";
content:" HTTP/1.1|0D 0A|Content-Type: application/x-www-form-urlencoded|0D 0A|User-Agent: Mozilla/";
content:"|3B 20|MSIE|20|"; distance:0;
content:"|29 0D 0A|Host:"; distance:0;

3118 "MALWARE-CNC Win.Trojan.Zemot payload download attempt"
content:"/mod_articles-auth-"; depth:19;
content:"/jquery/"; within:8; distance:7;
content:"Accept: */*|0D 0A|Connection|3A 20|Close|0D 0A|";
content:"Cache-Control|3A 20|no-cache|0D 0A|";

X
3225 "MALWARE-CNC Win.Trojan.HawkEye keylogger exfiltration attempt"
content:"Subject|3A 20|HawkEye Keylogger|20 7C 20|";
content:"=0D=0APC";
content:"=0D=0AInstalled";
content:"=0D=0AOperating System"; within:75; distance 15;
content:"=0D=0AInternal IP"; within:200; distance 10;
content:"=0D=0AExternal IP"; within:50; distance 5;

3123 "MALWARE-CNC WIN.Trojan.Plugx variant outbound connection"
content:"HHV1:";
content:"HHV2:"; within:20;
content:"HHV3: 61456"; within:20;
content:"HHV4:"; within:20;

********************************************************************************
ALL pos constraints
********************************************************************************

XX
1303 "PROTOCOL-RPC status GHBN format string attack"
content:"|00 01 86 B8|"; depth:4; offset:12;
content:"|00 00 00 02|"; within:4; distance:4;
content:"%x %x"; within:256;
content:"|00 00 00 00|"; depth:4; offset:4;

XX
1634 "OS-WINDOWS SMB-DS DCERPC Messenger Service buffer overflow attempt"
content:"|FF|SMB%"; depth:5; offset:4;
content:"&|00|"; within:2; distance:56;
content:"|5C 00|P|00|I|00|P|00|E|00 5C 00|"; within:12; distance:5;
content:"|04 00|"; within:2;

X
2445 "MALWARE-CNC Win.Trojan.Gupd variant outbound connection"
content:"cstype="; depth:7;
content:"&authname="; within:48; distance:1;
content:"&authpass="; within:48; distance:1;
content:"&hostname="; within:48; distance:1;
content:"&ostype="; within:256; distance:1;
content:"&macaddr="; within:64; distance:16;
content:"&owner="; within:48; distance:17;

********************************************************************************
TASIEMCE
********************************************************************************

2947 "MALWARE-CNC Win.Trojan.Glupteba.M initial outbound connection attempt"
content:"/stat?";
content:"uptime=";
content:"&downlink="; distance:0;
content:"&uplink="; distance:0;
content:"&id="; distance:0;
content:"&statpass=bpass"; distance:0;
content:"&version="; distance:0;
content:"&features="; distance:0;
content:"&guid="; distance:0;
content:"&comment="; distance:0;
content:"&p="; distance:0;
content:"&s="; distance:0;

X
2930 "MALWARE-OTHER ANDR.Trojan.iBanking outbound connection attempt"
content:"/android/sms/sync.php";
content:"User-Agent|3A 20|Apache-HttpClient|2F|";
content:"bot_id=";
content:"&imei="; distance:0;
content:"&iscallhack="; distance:0;
content:"&issmshack="; distance:0;
content:"&isrecordhack="; distance:0;
content:"&isadmin="; distance:0;
content:"&control_number="; distance:0;

