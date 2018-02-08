#!/usr/bin/perl

require "./cgi-lib.pl";

$userinfo="/web/sites/stats/global/domaininfo";
$bodyfile="/web/sites/stats/global/bodyfile";
$cgiurl = $ENV{'SCRIPT_NAME'};

$pwd=`/bin/pwd`;
@path=split(/\//, $pwd);
$username=($path[3]);
$domain=($path[4]);

&ReadParse(*input);
$cgiurl = $ENV{'SCRIPT_NAME'};

print &PrintHeader;
print <<EOF;
<html>
<head>
<title>Improved stats</title>
</head>
<body bgcolor="white">
<font face="verdana">
The stats have been improved.  To view the new, improved stats page,
click <a href="http://$domain.com/stats/stats.html">here.</a>
<p>
<font color="red">
NOTE: ON THE NEW STATS, YOU HAVE ACCESS TO "YESTERDAY", HOWEVER THE YESTERDAY
STATS WILL NOT WORK UNTIL THE NEW STATS PROGRAM HAS RUN THE FIRST TIME.             
</font>
<p>
Don't forget to change your bookmarks.
<p>
Thanks
<p>
admin\@national-net.com
</body>
</html>
EOF
#}
