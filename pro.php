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

	$powershell="
	SELECT * FROM reg_set_value_tbl where targetobject like 'HKLM%software%policies%Microsoft%windows%powershell%';
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

  $mimikatz="
SELECT * from proc_access_tbl where TargetImage like '%lsass.exe' and GrantedAccess like '0x1010';";
// Mimikatz - sekursla::logonpasswords

  $PwDump7="
 SELECT Image from raw_access_read_tbl where Image not like '%System32%' and Image not like 'System' and Image not like '%TrustedInstaller.exe' and Image not like '%Everything.exe';
";

  $RemotePwdump="
SELECT * from create_remote_thread_tbl where TargetImage like '%lsass.exe' and SourceImage not like '%System32%';";
  // lsass.exe에 CreateRemoteThread -> 강력한 의심 가능

  $net="
SELECT * from proc_create_tbl where Image like '%net1.exe' or Image like '%net.exe';";

  $netuser="
SELECT * from pipe_connected_tbl where Image like '%net1.exe' and PipeName like '%\lsass';";

  $netview="
SELECT * from pipe_connected_tbl where Image like '%net1.exe' and PipeName like '%\browser';";

  $netuse="
SELECT * from pipe_connected_tbl where Image like '%net.exe' and PipeName like '%\wkssvc';";

  $netuse2="
SELECT * from network_connect_tbl where Image like '%net.exe';";
// 어떤 netuse명령이었는지 추적할 수 있는 쿼리
  
  $wmic="
SELECT * from proc_create_tbl where ParentImage like '%WmiPrvSE.exe';";
// Explorer.exe 등이 아닌 WmiPrvSE.exe가 프로세스 실행 -> 원격 실행 의심 가능

  $wmic2="
SELECT * from network_connect_tbl  where Image like '%wmic.exe';";
// 실제 원격 연결 여부 확인

  $wmiexecvbs="
SELECT * from proc_create_tbl where ParentImage like '%WScript.exe';";
// net use 명령어가 실행되었을 경우($myquery_netuse) 그것이 wmiexec.vbs에 의한 실행인지 파악할 수 있는 쿼리

  $winrs="
SELECT * from proc_create_tbl where ParentImage like '%WinrsHost.exe';";

  $winrs2="
SELECT * from network_connect_tbl where Image like '%winrs.exe';";

  $winrs3="
SELECT * from network_connect_tbl where SourcePort like 5985;";
// Port 5985를 기본으로 사용한다는 점을 이용

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
	$query_net=mysqli_query($server,$net);
	$query_netuser=mysqli_query($server,$netuser);
	$query_netview=mysqli_query($server,$netview);
	$query_netuse=mysqli_query($server,$netuse);
	$query_netuse2=mysqli_query($server,$netuse2);
	$query_mimikatz=mysqli_query($server,$mimikatz);
	$query_wmic=mysqli_query($server,$wmic);
	$query_wmic2=mysqli_query($server,$wmic2);
	$query_winrs=mysqli_query($server,$winrs);
	$query_winrs3=mysqli_query($server,$winrs3);
	$query_winrs2=mysqli_query($server,$winrs2);
	$query_wmiexecvbs=mysqli_query($server,$wmiexecvbs);
	$query_pwdump7=mysqli_query($server,$PwDump7);

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

echo "net";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_net);$x++){
$data[$x]=mysqli_fetch_array($query_net);
}
echo "<tr><td>EventTime</td><td>CommandLine</td><td>hostname</td><td>parentimage</td></tr>";
for($x=0;$x<mysqli_num_rows($query_net);$x++){
$eventtime[]=$data[$x][EventTime];
$commandline[]=$data[$x][CommandLine];
$hname[]=$data[$x][Hostname];
$pimage[]=$data[$x][ParentImage];
echo "<tr><td>$eventtime[$x]</td><td>$commandline[$x]</td><td>$hname[$x]</td><td>$pimage[$x]</td></tr>";
}
echo "</table>";


echo "netuser";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_netuser);$x++){
$data[$x]=mysqli_fetch_array($query_netuser);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td></tr>";
for($x=0;$x<mysqli_num_rows($query_netuser);$x++){
$pid11[]=$data[$x][ProcessID];
$msg11[]=$data[$x][msg];
$hname11[]=$data[$x][Hostname];
echo "<tr><td>$pid11[$x]</td><td>$msg11[$x]</td><td>$hname11[$x]</td></tr>";
}
echo "</table>";

echo "netuse";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_netuse);$x++){
$data[$x]=mysqli_fetch_array($query_netuse);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td></tr>";
for($x=0;$x<mysqli_num_rows($query_netuse);$x++){
$pid12[]=$data[$x][ProcessID];
$msg12[]=$data[$x][msg];
$hname12[]=$data[$x][Hostname];
echo "<tr><td>$pid12[$x]</td><td>$msg12[$x]</td><td>$hname12[$x]</td></tr>";
}
echo "</table>";

echo "netuse2";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_netuse2);$x++){
$data[$x]=mysqli_fetch_array($query_netuse2);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td></tr>";
for($x=0;$x<mysqli_num_rows($query_netuse2);$x++){
$pid13[]=$data[$x][ProcessID];
$msg13[]=$data[$x][msg];
$hname13[]=$data[$x][Hostname];
echo "<tr><td>$pid13[$x]</td><td>$msg13[$x]</td><td>$hname13[$x]</td></tr>";
}
echo "</table>";

echo "netview";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_netview);$x++){
$data[$x]=mysqli_fetch_array($query_netview);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>hostname</td></tr>";
for($x=0;$x<mysqli_num_rows($query_netview);$x++){
$pid14[]=$data[$x][ProcessID];
$msg14[]=$data[$x][msg];
$hname14[]=$data[$x][Hostname];
echo "<tr><td>$pid14[$x]</td><td>$msg14[$x]</td><td>$hname14[$x]</td></tr>";
}
echo "</table>";

echo "mimikatz";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_mimikatz);$x++){
$data[$x]=mysqli_fetch_array($query_mimikatz);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td<td>ParentImage</td>></tr>";
for($x=0;$x<mysqli_num_rows($query_mimikatz);$x++){
$pid15[]=$data[$x][ProcessID];
$msg15[]=$data[$x][msg];
$hname15[]=$data[$x][Hostname];
$pimage15[]=$data[$x][ParentImage];
echo "<tr><td>$pid15[$x]</td><td>$msg15[$x]</td><td>$hname15[$x]</td><td>$pimage15[$x]</td></tr>";
}
echo "</table>";

echo "wmic_process";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_wmic);$x++){
$data[$x]=mysqli_fetch_array($query_wmic);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td></tr>";
for($x=0;$x<mysqli_num_rows($query_wmic);$x++){
$pid16[]=$data[$x][ProcessID];
$msg16[]=$data[$x][msg];
$hname16[]=$data[$x][Hostname];
echo "<tr><td>$pid16[$x]</td><td>$msg16[$x]</td><td>$hname16[$x]</td></tr>";
}
echo "</table>";

echo "wmic_network";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_wmic2);$x++){
$data[$x]=mysqli_fetch_array($query_wmic2);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td></tr>";
for($x=0;$x<mysqli_num_rows($query_wmic2);$x++){
$pid17[]=$data[$x][ProcessID];
$msg17[]=$data[$x][msg];
$hname17[]=$data[$x][Hostname];
echo "<tr><td>$pid17[$x]</td><td>$msg17[$x]</td><td>$hname17[$x]</td></tr>";
}
echo "</table>";

echo "winrs_process";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_winrss);$x++){
$data[$x]=mysqli_fetch_array($query_winrs);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td></tr>";
for($x=0;$x<mysqli_num_rows($query_winrs);$x++){
$pid18[]=$data[$x][ProcessID];
$msg18[]=$data[$x][msg];
$hname18[]=$data[$x][Hostname];
echo "<tr><td>$pid18[$x]</td><td>$msg18[$x]</td><td>$hname18[$x]</td></tr>";
}
echo "</table>";

echo "winrs_network";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_winrs2);$x++){
$data[$x]=mysqli_fetch_array($query_winrs2);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>Time</td></tr>";
for($x=0;$x<mysqli_num_rows($query_winrs2);$x++){
$pid19[]=$data[$x][ProcessID];
$msg19[]=$data[$x][msg];
$hname19[]=$data[$x][Hostname];
$EventTime[]=$data[$x][EventTime];
echo "<tr><td>$pid19[$x]</td><td>$msg19[$x]</td><td>$hname19[$x]</td><td>$EventTime[$x]</td></tr>";
}
echo "</table>";

echo "winrs_network2";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_winrs3);$x++){
$data[$x]=mysqli_fetch_array($query_winrs3);
}
echo "<tr><td>pid</td><td>msg</td><td>hostname</td><td>Time</td></tr>";
for($x=0;$x<mysqli_num_rows($query_winrs3);$x++){
$pid20[]=$data[$x][ProcessID];
$msg20[]=$data[$x][msg];
$hname20[]=$data[$x][Hostname];
$EventTime[]=$data[$x][EventTime];
echo "<tr><td>$pid20[$x]</td><td>$msg20[$x]</td><td>$hname20[$x]</td><td>$EventTime[$x]</td></tr>";
}
echo "</table>";

echo "wmiexecvbs";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_wmiexecvbs);$x++){
$data[$x]=mysqli_fetch_array($query_wmiexecvbs);
}
echo "<tr><td>pid</td><td>hostname</td><td>Time</td><td>commandline</td></tr>";
for($x=0;$x<mysqli_num_rows($query_wmiexecvbs);$x++){
$pid20[]=$data[$x][ProcessID];
$hname20[]=$data[$x][Hostname];
$EventTime[]=$data[$x][EventTime];
$CommandLine[]=$data[$x][CommandLine];
echo "<tr><td>$pid20[$x]</td><td>$hname20[$x]</td><td>$EventTime[$x]</td><td>$CommandLine[$x]</td></tr>";
}
echo "</table>";

echo "Pwdump7(suspicious)";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_pwdump7);$x++){
$data[$x]=mysqli_fetch_array($query_pwdump7);
}
echo "<tr><td>Image</td><td>hostname</td><td>Time</td></tr>";
for($x=0;$x<mysqli_num_rows($query_pwdump7);$x++){
$Image21[]=$data[$x][Image];
$hname21[]=$data[$x][Hostname];
$EventTime[]=$data[$x][EventTime];
echo "<tr><td>$Image21[$x]</td><td>$hname21[$x]</td><td>$EventTime[$x]</td></tr>";
}
echo "</table>";

echo "RemotePwdump";
echo "<table border=1>";
 	for($x=0;$x<mysqli_num_rows($query_pwdump7);$x++){
$data[$x]=mysqli_fetch_array($query_pwdump7);
}
echo "<tr><td>Image</td><td>hostname</td><td>Time</td></tr>";
for($x=0;$x<mysqli_num_rows($query_pwdump7);$x++){
$Image21[]=$data[$x][Image];
$hname21[]=$data[$x][Hostname];
$EventTime[]=$data[$x][EventTime];
echo "<tr><td>$Image21[$x]</td><td>$hname21[$x]</td><td>$EventTime[$x]</td></tr>";
}
echo "</table>";

    mysqli_close($server); 
?>