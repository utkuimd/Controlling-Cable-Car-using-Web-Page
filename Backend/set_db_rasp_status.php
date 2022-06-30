<?php


$servername = "localhost";
$username = "cablecar_utku";
$password = "";
$dbname = "cablecar_rasp_prj";


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}else{
	echo "Connecton established! <br/>";
}


//http://192.168.1.24/set_db_rasp_status.php?weight=on&motor_cur_pos=-343&motor_is_en_dis=enabled
print_r($_GET);

if (isset($_GET["weight"])){
	
	if( $_GET["weight"] == 'on'){
		$sql = "UPDATE `rasp_status` SET `weight`='on' WHERE 1";
	}else{
		$sql = "UPDATE `rasp_status` SET `weight`='off' WHERE 1";
	}
	
	$result = $conn->query($sql);
}

if (isset($_GET["motor_cur_pos"])){

	$sql = "UPDATE `rasp_status` SET `motor_cur_pos`=".$_GET["motor_cur_pos"]." WHERE 1";

	$result = $conn->query($sql);
}

if (isset($_GET["motor_is_en_dis"])){
	
	if( $_GET["motor_is_en_dis"] == 'enabled'){
		$sql = "UPDATE `rasp_status` SET `motor_is_en_dis`='enabled' WHERE 1";
	}else{
		$sql = "UPDATE `rasp_status` SET `motor_is_en_dis`='disabled' WHERE 1";
	}
	
	$result = $conn->query($sql);
}

if (isset($_GET["motor_speed"])){
	
	$sql = "UPDATE `rasp_status` SET `motor_speed`='".$_GET["motor_speed"]."' WHERE 1";
	$result = $conn->query($sql);
}

$result = $conn->query($sql);

//close data base
$conn->close();

exit();

?>