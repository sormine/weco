#!/usr/bin/perl
use CGI qw(:standard);

#VERSION 5.12.9

chomp($dtime=`date`);

#conffile
my $conffile="/etc/stats.conf";

#Get domaininfo
my $userinfo="/web/sites/stats/global/domaininfo";

#Get domain, hostname and path I am called by
my $cgiurl = $ENV{'SCRIPT_NAME'};
chop(my $hostname=`/bin/hostname`);

#Get expected cgi values
my $domain = param("domain");
my $function = param("function");
my $month = param("month");
my $day = param("day");
my $year = param("year");
my $count=param("count");
my $date="";
my @now=localtime(time);
$cmonth=$now[4]+1;
$cyear=$now[5]+1900;
$cday=$now[3];

if (!((($month)&&($day))&&($year))){
	$month=$cmonth;
	$day=$cday;
	$year=$cyear;
}
if (!((($cyear == $year)&&($month == $cmonth)) && ($day == $cday))){
	$date="$year";
	if ($month<10){
		$date.="0";
	}
	$date.="$month";
	if ($day<10){
		$date.="0";
	}
	$date.="$day";
}

if (!$domain){
        $domain=$ENV{'HTTP_HOST'};
	$domain=~s/www\.//;
}


#Populate domaininfo
my %domaininfo=();
open(TMP,"$userinfo");
	while(<TMP>){
		chomp;
		s/\s+//g;
		if ($_){
			(my $user,my $domain,my $docroot, my $log,my $curlog,$aliases)=split(/\:/,$_);
			$domain=~s/www\.//;
			$domaininfo{$domain}{'user'}=$user;
			$domaininfo{$domain}{'docroot'}=$docroot;
			$domaininfo{$domain}{'log'}=$log;
			$domaininfo{$domain}{'curlog'}=$curlog;
			$domaininfo{$domain}{'aliases'}=$aliases;
		}
	}
close TMP;




my %allowedstats=();
if (-e "$conffile"){
	open(my $statsfile,"$conffile");
		while(<$statsfile>){
			chomp;
			s/\#.*//;
			if ($_=~/\S+/){
				$allowedstats{$_}=1;
			}
		}
	close $statsfile;
}
else{
	%allowedstats=( "awstats" => 1,"analog" => 1,"webalizer" => 1);
}

%functionmap=(
"Errors" => "showerrors",
"Real Time Referers" => "getrefs",
);

foreach (sort keys %allowedstats){
	$functionmap{$_}=$_;
}

if ($function){
	if ($functionmap{$function}){
		my $tempo=$functionmap{$function};
		&$tempo;
	}
}
elsif (($function == 0) && ($ENV{'REQUEST_METHOD'} eq "POST")){
        &error;
}
else{
	print header;
        print <<EOF;
<center>
<form action="$cgiurl" method="post" target="main">
<input type="hidden" name="username" value="$domaininfo{$domain}{'user'}">
<table border=0 cellpadding=0 cellspacing=0>
<tr>
<td align=center>

<select name="function">
<option value="0">Select Function</option>
EOF
foreach(sort keys %functionmap){
	print "<option value=\"$_\">$_\n";
}
        print <<EOF;
</select>
</td>
<td>
<select name="count">
<option value="0">Number of referrers
<option value="10">Show top 10 referrers
<option value="50">Show top 50 referrers
<option value="100">Show top 100 referrers
<option value="500">Show top 500 referrers
</select>
</td>
<td align=center valign=middle>
<select name="domain">
<option value=0>Select domain</option>
EOF
foreach(sort keys %domaininfo){
	if ($domaininfo{$_}{'user'} eq $domaininfo{$domain}{'user'}){
		print "<option value=\"$_\">$_\n";
	}
}
        print <<EOF;
</select>
</td>
<td>
<input type="submit" name="usage" value="Go!">
</td></tr></table>
<br />
For historical Information, Select a date:
<select name="month">
<option value="0">Month
EOF
my @months=("","January","Feburary","March","April","May","June","July","August","September","October","November","December");
for(my $j=1;$j<13;$j++){
	print "<option value=\"$j\"";
	print " selected" unless $j != $month;
	print ">$months[$j]\n";

}
print <<EOF;
</select>
 <select name="day">
<option value="0">day
EOF
for(my $i=1;$i<32;$i++){
	print "<option value=\"$i\"";
	print " selected" unless $i != $day;
	print ">$i\n";
}
print <<EOF;
</select>
,
<input name="year" value="$year">
EOF



}



sub webalizer
{
	if ($input{'domain'} eq "0")
	{
		&domainerror;
		return;
	}
	print "Location: http://$domain/stats/webalizer\n\n";
}



sub myheader
{
	print header;
print <<EOF;
<html>
<head>
<title>Console</title>
</head>
<body bgcolor="white">
EOF
}

sub analog{
	if ($domain){
		if ($date){
			print header;
			if (-e "$domaininfo{$domain}{docroot}/stats/reports/analog$date.gz"){
				open(my $zfh,"zcat $domaininfo{$domain}{docroot}/stats/reports/analog$date.gz|");
					while(<$zfh>){
						print $_;
					}
				close $zfh;
			}
			else{
				print "There are no stats for that date: $date\n";
			}
		}
		else{
			print "Location: http://$domain/stats/analog.html\n\n";
		}
	}
	else{
		&domainerror;
	}
}

sub showerrors
{
	if ($domain){
		&myheader;
		my $errorfile = "/var/log/apache/error.log";
		print <<EOF;
<html>
<head>
<title>Error Logs</title>
</head>                                                                         
<body bgcolor="white">
<center>
<font face="arial,helvetica" size=-1>
<p>
Current server date/time - $dtime
<p>
<font face="arial,helvetica">
<h3>Error log entries for $domain</h3>
<p>
Note: If nothing displays below here, then there are not any errors for this dom
a
in.
<p>
<table border=2 cellpadding=4 cellspacing=2>
<tr>
EOF
        open (ERRORFILE, "$errorfile") || die "Couldn't open $errorfile\n";
        while (<ERRORFILE>)
        {
                if ((/\/$domain\//) && ( ! /\.exe/ ))
                {
                        print "<td bgcolor=\"bbccdd\"><font color=red size=-1>$_
<
/font></td></tr><tr>\n";
                }
        }
        print <<EOF;
</tr></table>
</body>
</html>
EOF
	}
	else{
		&domainerror;
	}
}


sub gig_per_domain{
	if ($domain){
		my %statInfo=();
		my $user=$domaininfo{$domain}{'user'};
		my $totgigs=0;
		foreach my $doms (sort keys %domaininfo){
		        if ($domaininfo{$doms}{'user'} eq $user){
				my $gigs=0;
				open(my $datfile,$domaininfo{$doms}{'docroot'}."/stats/datafile");
					while(<$datfile>){
						(my $date,my $gig,my $junk)=split(/,/,$_);
						$gigs+=$gig;
					}
				close $datfile;
				$totgigs+=$gigs;
				$statInfo{$doms}=$gigs;
			}
		}

		print header;
		print <<EOF;
<html>
<head>
<title>gig_per_domain for all domains</title>
</head>
<body bgcolor="white">
<center>
<font face="arial,helvetica" size=-1>
<p>
<font face="arial,helvetica">
<h3>gig_per_domain for all domains </h3>
Total gigs= $totgigs</h3>
<table border=2 cellpadding=4 cellspacing=2>
<tr>
<td bgcolor="aaaaaa" align=center>
<font face="arial,helvetica">
Domain
</td>
<td bgcolor="aaaaaa" align=center>
<font face="arial,helvetica">
Gigs</td>
</tr>
EOF

	foreach (sort keys %statInfo){
		 print "<tr><td bgcolor=\"bbccdd\">$_</td><td bgcolor=\"bbccdd\">$statInfo{$_}</td></tr>\n";
	}
	 print <<EOF;
</table>
</body>
</html>
EOF
	}
	else{
		&domainerror();
	}
}


sub getrefs {
	if ($domain){
		if ($count){
			my @aliases=split(/\,/,$domaininfo{$domain}{'aliases'});

			for(my $i=0;$i<@aliases;$i++){
				$aliases[$i]=~s/\*/\.\*/;
			}
			%refcounter=();
			my $number=0;
			if ($date){
				if (-e "$domaininfo{$domain}{'docroot'}/stats/reports/rrefs$date.gz"){
				       open(my $zfh,"zcat $domaininfo{$domain}{'docroot'}/stats/reports/rrefs$date.gz|");
					      chomp($number=<$zfh>);
					       while(<$zfh>){
						      chomp;
						      my @entry=split(/\|/,$_);
						      $refcounter{$entry[1]}=$entry[0];
						}
				       close $zfh;
				}
				else{
					print header;
					print "There are no stats for that date: $date\n";
					exit;
				}
			}
			else{
			my $reffile = $domaininfo{$domain}{'curlog'};

			open(TMP,"$reffile")||die "I couldn't open $reffile";
				my @info=();
				while(<TMP>){
				my @entry=split(/\s+/,$_);
					if ($entry[10] && $entry[6]){
						$entry[10]=~s/\"//g;
						$_="$entry[10] -> $entry[6]\n";

						if ((!/file:/) && ((/^http/) || (/^news/))){
							my $good=1;
							foreach my $alias(@aliases){
								if (/^https?\:\/\/$alias/){
									$good=0;	
								}
							}
							if ($good){	
								chomp;
								$refcounter{$_}+=1;
								$number++;
							}
						}
					}
				}
			close TMP;
			}
			my @keys=sort by_hits (keys %refcounter);
			&myheader;
			print <<EOF;
<html>
<head>
<title>Daily referers for domain $domain</title>
</head>
<body bgcolor="white">
<center>
<font face="arial,helvetica" size=-1>
<p>
EOF
			if ( $yesterday) {
				print <<EOF;
<font face="arial,helvetica" size=-1>
<p>
<font face="arial,helvetica">
<h3>Top $count raw referrals for domain<font color="red"> $domain </font>
for YESTERDAY.
<br>
Total referrals= $number</h3>
<p>
EOF
			}
			else{
				print <<EOF;
<font face="arial,helvetica" size=-1>
Current date/time - $dtime
<p>
<font face="arial,helvetica">
<h3>Top $count raw referrals for domain<font color="red"> $domain </font>.
Total referrals= $number</h3>
<p>
<b>NOTE: Stats reset at midnight.</b>
<p>
EOF
			}
			print <<EOF;
<table border=2 cellpadding=4 cellspacing=2>
<tr>
<td bgcolor="aaaaaa" align=center>
<font face="arial,helvetica">
Hit Count
</td>
<td bgcolor="aaaaaa" align=center>
<font face="arial,helvetica">
Referrer Source</td>
<td bgcolor="aaaaaa" align=center>
<font face="arial,helvetica">
Referrer Destination
</td>
</tr>
EOF
			for(my $i=0;$i<$count;$i++){
				(my $one,my $two)=split(/\s+\-\>\s+/,$keys[$i]);
				print "<tr><td bgcolor=\"bbccdd\">$refcounter{$keys[$i]}</td><td bgcolor=\"bbccdd\"><a href=\"$one\">$one</a></td><td bgcolor=\"ccddee\"><a href=\"$two\">$two</a></td></tr>\n";

			}
			print <<EOF;
</table>
</body>
</html>
EOF
		}
		else{
			&myheader;
			print <<EOF;
<font face="verdana,arial" color="red">
You did not select the number of referrers to show...please try again
</font>
EOF
		}
	}
	else{
		&domainerror;
	}
}

sub awstats{
	if ($domain)
	{
		print "Location: http://$domain/stats/awstats.html\n\n";
	}
	else{
		&domainerror;
	}
}

sub domainerror
{
print header;
print <<EOF;
<html>
<head>
<title>Error</title>
<b>
<font face="verdana" size=-1 color="red">
You did not select a domain to view.  Please select a domain from the 
"Select Domain" drop down list...
</font>
</b>
</body>
</html>
EOF
exit;
}

sub error
{
print header;
print <<EOF;
<font face="verdana,arial" color="red" size=-1>
Please select a function from the "Select Function" drop down menu to begin
</font>
EOF
}


sub by_hits{
	if ($refcounter{$a}<$refcounter{$b}){
		return 1;
	}
	else{
		return -1;
	}
}
