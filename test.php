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
SELECT date FROM file_create_tbl where msg like '%processid: 4\r\n%' and not msg like '%.etl%' and not msg like '%.cache%';
";
	$myquery2="
SELECT * FROM file_create_tbl where msg like '%processid: 4\r\n%' and not msg like '%.etl%' and not msg like '%.cache%';
";
	$myquery_at="
SELECT date FROM reg_create_delete_tbl where targetobject like 'HKLM%Software%Microsoft%windows nt%currentversion%schedule%Taskcache%plain%';
";
	$myquery_at2="
SELECT * FROM reg_create_delete_tbl where targetobject like 'HKLM%Software%Microsoft%windows nt%currentversion%schedule%Taskcache%plain%';
";
	$myquery_at_exe="
SELECT * FROM proc_create_tbl where (parentimage like '%taskeng%' and not image like 'C:%program files (x86)%google%update%googleupdate.exe' and not image like 'c:%program files (x86)%opera%launcher.exe') or (parentimage like '%cmd.exe' and parentprocessid in (select processid from proc_create_tbl where parentimage like '%taskeng%'));
";


	$myquery_wce="
SELECT date FROM reg_set_value_tbl where targetobject like 'hklm%system%currentcontrolset%services%wceservice%type';
";
	$myquery_wce2="
SELECT msg FROM reg_set_value_tbl where targetobject like 'hklm%system%currentcontrolset%services%wceservice%type';
";

	$myquery_badcmd="
SELECT * from proc_create_tbl where imgae like '%cmd.exe' and not parentimage like '%explorer.exe' and not parentimage like '%vmtoolsd.exe');
";

    $query = mysqli_query($server,$myquery);
	$query2 = mysqli_query($server,$myquery2);
	$query_at=mysqli_query($server,$myquery_at);
	$query_at2=mysqli_query($server,$myquery_at2);
	$query_at_exe=mysqli_query($server,$myquery_at_exe);
	$query_wce=mysqli_query($server,$myquery_wce);
	$query_wce2=mysqli_query($server,$myquery_wce2);    
	

    if ( ! $query ) {
        echo mysql_error();
        die;
    }
    
    $data = array();
//	$data2=array();
//	$data_at=array();
//	$data_at2=array();
$y=1;

    for ($x = 0; $x < mysqli_num_rows($query); $x++) {
	//$data[]=array("name"=>"Copy");
        $data[] = mysqli_fetch_assoc($query)+array("id"=>($y++))+array("from"=>"F")+mysqli_fetch_assoc($query2);
//echo json_encode($data[$x]);
    }
	for($x=0;$x<mysqli_num_rows($query_at);$x++){
	$data[]=mysqli_fetch_assoc($query_at)+array("id"=>$y++)+array("from"=>"F")+mysqli_fetch_assoc($query_at2);
}
	for($x=0;$x<mysqli_num_rows($query_wce);$x++){
	$data[]=mysqli_fetch_assoc($query_wce)+array("id"=>$y++)+array("from"=>"F")+mysqli_fetch_assoc($query_wce2);
}


  $intell["nodes"]=$data; 
  $intell["links"]="";
//    echo json_encode($data);     
//	echo $data[5];
	$output=json_encode($intell);
//ehco $output;  


 $file=fopen("moon.json","w+");
    if(!$file) die("파일을 열 수없음");
 fwrite($file,$output);
    mysqli_close($server); 
?>
