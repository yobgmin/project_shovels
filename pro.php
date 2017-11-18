<?php
    $username = "root"; 
    $password = "12345";   
    $host = "localhost";
    $database="winlogs";
    
//    $filetest=fopen('/home/ubuntu/testfiles.json','a+');
//   $datas=array();
//    $datas[]="aa:bb";
//    fwrite($filetest,$datas[0]);

   $server = mysqli_connect($host, $username, $password, $database);

 //   if(!$server)
 //   {
 //       echo "db연결실패";
 //   }
  //  else{
 //   $connection = mysql_select_db($database, $server);
  //  }

    $myquery = "
SELECT * FROM file_create_tbl where msg like '%processid: 4\r\n%' and not msg like '%.etl%' and not msg like '%.cache%';
";
	$myquery_at="
SELECT date FROM reg_create_delete_tbl where targetobject like 'HKLM%Software%Microsoft%windows nt%currentversion%schedule%Taskcache%plain%';
";

	$myquery_wce="
SELECT date FROM reg_set_value_tbl where targetobject like 'hklm%system%currentcontrolset%services%wceservice%type';
";

	$myquery_badcmd="
SELECT * from proc_create_tbl where image like '%cmd.exe' and not parentimage like '%explorer.exe' and not parentimage like '%vmtoolsd.exe';
";
	$psexesvc="
select * from proc_create_tbl where image like '%psexesvc.exe' and processid='1500';
";
	$psexesvc_low="
select * from proc_create_tbl where parentimage like '%psexesvc.exe' and processid='1500';
";
	$taskeng_low="
select * from proc_create_tbl where parentimage like '%taskeng.exe' and processid='1504' and not image like '%Program files (x86)%google%update%googleupdate.exe' and not image like '%program files (x86)%opera%launcher.exe';
";
	$psexesvc_low2="
select * from proc_create_tbl where parentimage like '%cmd.exe' and processid='1500';
";
	$taskeng_low2="
select * from proc_create_tbl where parentimage like '%cmd.exe' and processid='1504';
";
	$psexec="
select * from proc_create_tbl where image like '%psexec.exe' and eventtime in (select eventtime from proc_create_tbl where image like '%psexesvc.exe' and processid='1500');
";
	$psexec_upper="
select * from proc_create_tbl where image like '%cmd.exe' and processid='1468';
";
	$psexec_upcmd="
select * from proc_create_tbl where processid ='1468' and not image like '%cmd.exe' and parentimage like '%cmd.exe';
";
	$taskeng="
select * from proc_create_tbl where image like '%taskeng.exe' and processid ='1504';
";
    $query = mysqli_query($server,$myquery);
	$query2 = mysqli_query($server,$myquery2);
	$query_at=mysqli_query($server,$myquery_at);
	$query_at2=mysqli_query($server,$myquery_at2);
	$query_at_exe=mysqli_query($server,$myquery_at_exe);
	$query_wce=mysqli_query($server,$myquery_wce);
	$query_wce2=mysqli_query($server,$myquery_wce2);    
	$query_badcmd=mysqli_query($server,$myquery_badcmd);
	$query_psexesvc=mysqli_query($server,$psexesvc);
	$query_psexesvc_low=mysqli_query($server,$psexesvc_low); 
	$query_psexesvc_low2=mysqli_query($server,$psexesvc_low2); 
	$query_psexec=mysqli_query($server,$psexec);
	$query_psexec_up=mysqli_query($server,$psexec_upper);
	$query_psexec_upcmd=mysqli_query($server,$psexec_upcmd);
	$query_taskeng=mysqli_query($server,$taskeng);
	$query_taskeng_low=mysqli_query($server,$taskeng_low);
	$query_taskeng_low2=mysqli_query($server,$taskeng_low2);
 if ( ! $query ) {
        echo mysql_error();
        die;
    }

echo "cmd's parent is not explorer.exe";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_badcmd);$x++){
$data[$x]=mysqli_fetch_array($query_badcmd);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td></tr>";
for($x=0;$x<mysqli_num_rows($query_badcmd);$x++){
$pid2[]=$data[$x][ProcessID];
$ms2g[]=$data[$x][msg];
$hname[]=$data[$x][Hostname];
echo "<tr><td>$pid2[$x]</td><td>$ms2g[$x]</td><td>$hname[$x]</td></tr>";
}
echo "</table>";


echo "psexesvc.exe";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_psexesvc);$x++){
$data[$x]=mysqli_fetch_array($query_psexesvc);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>parentimage</td></tr>";
for($x=0;$x<mysqli_num_rows($query_psexesvc);$x++){
$pid1[]=$data[$x][ProcessID];
$msg[]=$data[$x][msg];
$hname2[]=$data[$x][Hostname];
$pimage2[]=$data[$x][ParentImage];
echo "<tr><td>$pid1[$x]</td><td>$msg[$x]</td><td>$hname2[$x]</td><td>$pimage2[$x]</td></tr>";
}
echo "</table>";


echo "psexesvc.exe Lower 1 step";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_psexesvc_low);$x++){
$data[$x]=mysqli_fetch_array($query_psexesvc_low);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>parentimage</td></tr>";
for($x=0;$x<mysqli_num_rows($query_psexesvc_low);$x++){
$pid3[]=$data[$x][ProcessID];
$msg3[]=$data[$x][msg];
$hname3[]=$data[$x][Hostname];
$pimage3[]=$data[$x][ParentImage];
echo "<tr><td>$pid3[$x]</td><td>$msg3[$x]</td><td>$hname3[$x]</td><td>$pimage3[$x]</td></tr>";
}
echo "</table>";


echo "psexesvc.exe Lower 2 step";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_psexesvc_low2);$x++){
$data[$x]=mysqli_fetch_array($query_psexesvc_low2);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>parentimage</td></tr>";
for($x=0;$x<mysqli_num_rows($query_psexesvc_low2);$x++){
$pid4[]=$data[$x][ProcessID];
$msg4[]=$data[$x][msg];
$hname4[]=$data[$x][Hostname];
$pimage4[]=$data[$x][ParentImage];
echo "<tr><td>$pid4[$x]</td><td>$msg4[$x]</td><td>$hname4[$x]</td><td>$pimage4[$x]</td></tr>";
}
echo "</table>";


echo "psexec-psexesvc source pc";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_psexec);$x++){
$data[$x]=mysqli_fetch_array($query_psexec);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>parentimage</td></tr>";
for($x=0;$x<mysqli_num_rows($query_psexec);$x++){
$pid5[]=$data[$x][ProcessID];
$msg5[]=$data[$x][msg];
$hname5[]=$data[$x][Hostname];
$pimage5[]=$data[$x][ParentImage];
echo "<tr><td>$pid5[$x]</td><td>$msg5[$x]</td><td>$hname5[$x]</td><td>$pimage5[$x]</td></tr>";
}
echo "</table>";


echo "psexec-psexesvc source pc-upper 1 step";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_psexec_up);$x++){
$data[$x]=mysqli_fetch_array($query_psexec_up);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>parentimage</td></tr>";
for($x=0;$x<mysqli_num_rows($query_psexec_up);$x++){
$pid6[]=$data[$x][ProcessID];
$msg6[]=$data[$x][msg];
$hname6[]=$data[$x][Hostname];
$pimage6[]=$data[$x][ParentImage];
echo "<tr><td>$pid6[$x]</td><td>$msg6[$x]</td><td>$hname6[$x]</td><td>$pimage6[$x]</td></tr>";
}
echo "</table>";


echo "psexec-psexesvc source pc-upcmd what do it?";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_psexec_upcmd);$x++){
$data[$x]=mysqli_fetch_array($query_psexec_upcmd);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>parentimage</td><td>commandline</td></tr>";
for($x=0;$x<mysqli_num_rows($query_psexec_upcmd);$x++){
$pid7[]=$data[$x][ProcessID];
$msg7[]=$data[$x][msg];
$hname7[]=$data[$x][Hostname];
$pimage7[]=$data[$x][ParentImage];
$cmdline7[]=$data[$x][CommandLine];
echo "<tr><td>$pid7[$x]</td><td>$msg7[$x]</td><td>$hname7[$x]</td><td>$pimage7[$x]</td><td>$cmdline7[$x]</td></tr>";
}
echo "</table>";


echo "cmd parent is taskeng.exe";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_taskeng);$x++){
$data[$x]=mysqli_fetch_array($query_taskeng);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>parentimage</td></tr>";
for($x=0;$x<mysqli_num_rows($query_taskeng);$x++){
$pid8[]=$data[$x][ProcessID];
$msg8[]=$data[$x][msg];
$hname8[]=$data[$x][Hostname];
$pimage8[]=$data[$x][ParentImage];
echo "<tr><td>$pid8[$x]</td><td>$msg8[$x]</td><td>$hname8[$x]</td><td>$pimage8[$x]</td></tr>";
}
echo "</table>";


echo "taskeng.exe lower 1 step";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_taskeng_low);$x++){
$data[$x]=mysqli_fetch_array($query_taskeng_low);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>parentimage</td></tr>";
for($x=0;$x<mysqli_num_rows($query_taskeng_low);$x++){
$pid9[]=$data[$x][ProcessID];
$msg9[]=$data[$x][msg];
$hname9[]=$data[$x][Hostname];
$pimage9[]=$data[$x][ParentImage];
echo "<tr><td>$pid9[$x]</td><td>$msg9[$x]</td><td>$hname9[$x]</td><td>$pimage9[$x]</td></tr>";
}
echo "</table>";


echo "taskeng.exe lower 2 step";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_taskeng_low2);$x++){
$data[$x]=mysqli_fetch_array($query_taskeng_low2);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>parentimage</td></tr>";
for($x=0;$x<mysqli_num_rows($query_taskeng_low2);$x++){
$pid10[]=$data[$x][ProcessID];
$msg10[]=$data[$x][msg];
$hname10[]=$data[$x][Hostname];
$pimage10[]=$data[$x][ParentImage];
echo "<tr><td>$pid10[$x]</td><td>$msg10[$x]</td><td>$hname10[$x]</td><td>$pimage10[$x]</td></tr>";
}
echo "</table>";


    mysqli_close($server); 
?>
