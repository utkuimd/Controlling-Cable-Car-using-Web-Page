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



print_r($_GET);

if (isset($_GET["redon"])){
	$sql = "UPDATE `rasp_commands` SET `led_red`='on' WHERE 1";
	$result = $conn->query($sql);
}
if (isset($_GET["redoff"])){
	$sql = "UPDATE `rasp_commands` SET `led_red`='off' WHERE 1";
	$result = $conn->query($sql);
}

if (isset($_GET["greenon"])){
	$sql = "UPDATE `rasp_commands` SET `led_green`='on' WHERE 1";
	$result = $conn->query($sql);
}
if (isset($_GET["greenoff"])){
	$sql = "UPDATE `rasp_commands` SET `led_green`='off' WHERE 1";
	$result = $conn->query($sql);
}

if (isset($_GET["blueon"])){
	$sql = "UPDATE `rasp_commands` SET `led_blue`='on' WHERE 1";
	$result = $conn->query($sql);
}
if (isset($_GET["blueoff"])){
	$sql = "UPDATE `rasp_commands` SET `led_blue`='off' WHERE 1";
	$result = $conn->query($sql);
}

if( isset($_GET["motor_speed"] )){
	$sql = "UPDATE `rasp_commands` SET `motor_speed`='".$_GET["motor_speed"]."' WHERE 1";
	$result = $conn->query($sql);
}

if (isset($_GET["motor_start"])){
	$sql = "UPDATE `rasp_commands` SET `motor_start_stop`='enable' WHERE 1";
	$result = $conn->query($sql);
}
if (isset($_GET["motor_stop"])){
	$sql = "UPDATE `rasp_commands` SET `motor_start_stop`='disable' WHERE 1";
	$result = $conn->query($sql);
}

if (isset($_GET["dir_forward"])){
	$sql = "UPDATE `rasp_commands` SET `motor_direction`='forward' WHERE 1";
	$result = $conn->query($sql);
}
if (isset($_GET["dir_backward"])){
	$sql = "UPDATE `rasp_commands` SET `motor_direction`='backward' WHERE 1";
	$result = $conn->query($sql);
}


//close data base
$conn->close();


header("Location: http://cablecarelohab.xyz/index.html"); /* Redirect browser */
exit();

?>