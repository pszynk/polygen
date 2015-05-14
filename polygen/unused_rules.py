0633 "SERVER-WEBAPP technote print.cgi directory traversal attempt"
content:"/technote/print.cgi";
content:"board=";
content:"../../";
content:"%00";

0634 "SERVER-WEBAPP ads.cgi command execution attempt"
content:"/ads.cgi";
content:"file=";
content:"../../";
content:"|7C|";

1223 "SERVER-IIS .asa HTTP header buffer overflow attempt"
content:"HTTP/"
content:".asa";
content:"|3A|";
content:"|0A|";
content:"|00|";

1304 "PROTOCOL-RPC status GHBN format string attack"
content:"|00 01 86 B8|"; depth:4; offset:16;
content:"|00 00 00 02|"; within:4; distance:4;
content:"%x %x"; within:256;
content:"|00 00 00 00|"; depth:4; offset:8;

1475 "SERVER-WEBAPP BitKeeper arbitrary command attempt"
content:"/diffs/";
content:"'";
content:"|3B|"; distance:0;
content:"'"; distance:1;

1494 "SERVER-MAIL From comment overflow attempt"
content:"From|3A|";
content:"<><><><><><><><><><><><><><><><><><><><><><>"; distance:0;
content:"|28|"; distance:1;
content:"|29|"; distance:1;

1571 "NETBIOS SMB DCERPC invalid bind attempt"
content:"|FF|SMB%"; depth:5; offset:4;
content:"&|00|"; within:2; distance:56;
content:"|5C 00|P|00|I|00|P|00|E|00 5C 00|"; within:12; distance:5;
content:"|05|"; within:1; distance:2;
content:"|0B|"; within:1; distance:1;
content:"|00|"; within:1; distance:21;

2615 "EXPLOIT-KIT Unknown Malvertising exploit kit stage-1 redirect"
content:"<html><body><script>|0A|var ";
content:"document.createElement("; within:80;
content:".setAttribute(|22|archive|22|, "; within:65;
content:".setAttribute(|22|codebase|22|, "; within:65;
content:".setAttribute(|22|id|22|, "; within:65;
content:".setAttribute(|22|code|22|, "; within:65;
content:"|22|)|3B 0A|document.body.appendChild("; within:65;
content:"</script>|0A|</body>|0A|</html>|0A 0A|";

2485 "MALWARE-OTHER Win.Trojan.Zeus Spam 2013 dated zip/exe HTTP Response - potential malware download"
content:"-2013.zip|0D 0A|";
content:"-2013.zip|0D 0A|";
content:"-"; within:1; distance:-14;
content:"-2013.exe";
content:"-"; within:1; distance:-14;

3072 "MALWARE-CNC Win.Trojan.Graftor variant outbound connection attempt"
content:"dados="; depth:6;
content:"&ct="; distance:0;
content:"/"; within:1; distance:2;
content:"/201"; within:4; distance:2;
content:"="; within:1; distance:1;
content:"&windows=";

