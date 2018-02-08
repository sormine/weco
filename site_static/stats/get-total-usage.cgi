#!/usr/bin/perl

require "./cgi-lib.pl";
require "/web/sites/stats/global/datelib.pl";

$date =`date +%m/%d/%y`;

&ReadParse(*input);
print &PrintHeader;
$totalstats="/web/sites/stats/global/savedtotalstats";

$login = "$input{'login'}";

open(TOTSTATS, "<$totalstats") || die "Could not open $totalstats\n";
while (<TOTSTATS>)
{
	if (/^$login:/)
	{
		@line = split (/\,/, $_);
		$totalused = ($line[1]); 
	
	}
}
if ( $day eq "02")
{
        $average = ($totalused / $yesterday);
        $projected = ($average * $monthnumber);
        $projected = sprintf("%.4f", $projected); 
}
elsif ( $day eq "01")
{
        $projected = $totalused;
        $projected = sprintf("%.4f", $projected); 
}
else
{
        
        $average = ($totalused / $yesterday);
        $projected = ($average * $monthnumber);
        $projected = sprintf("%.4f", $projected); 
}
print <<EOF
<html>
<head>
<title>Total bandwidth </title>
</head>
<body bgcolor="white">
<font face="arial,helvetica">
<center>
<h3>Total bandwidth for all domains owned by $login as of $date</h3>
<table>
<tr>
<td align=center>
<font face="arial,helvetica" color="red" size=+1>
<b>$totalused GB's</font><font face="arial,helvetica" color="black"> used so far this month</font></b>
<p>
<font face="arial,helvetica">Projected month end usage -
</font><font face="arial,helvetica" color="red">$projected GB's</font>
</td></tr></table>
</body>
</html>
EOF
