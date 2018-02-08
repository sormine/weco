#!/usr/bin/perl


require "./cgi-lib.pl";

$userinfo="/web/sites/stats/global/domaininfo";
$bodyfile="/web/sites/stats/global/bodyfile";
$cgiurl = $ENV{'SCRIPT_NAME'};

$pwd=`/bin/pwd`;
@path=split(/\//, $pwd);
$username=($path[3]);

&ReadParse(*input);

print &PrintHeader;

$cgiurl = $ENV{'SCRIPT_NAME'};

$du=`/usr/bin/du -s /web/sites/$username`;
($used,$junk)=split(/\s+/,$du);
$mbused = ($used / 1000);
$mbused = sprintf("%.1f", $mbused);

print <<EOF;
<html>
<head>
<title>Disk space used</title>
<body bgcolor="white">
<center>
<font face="verdana,arial">Your account of</font><font face="verdana,arial" color="red">
$username</font><font face="verdana,arial"> is using a total of </font>
<font face="verdana,arial" color="red">$mbused MBs</font> 
<font face="verdana,arial">of disk space.<p>
To see what your allowable disk space is, please check the pricing page at<br>
<a href="http://national-net.com/pricing.html">http://national-net.com/pricing.html</a>
</font>
</body>
</html>
EOF
