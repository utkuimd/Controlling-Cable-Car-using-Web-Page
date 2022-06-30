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

$sql = "SELECT * FROM `rasp_status` WHERE 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {

	$row = $result->fetch_assoc();
	$data =  json_encode($row);
} else {
	$data = "Error";
}

echo $data;

$result->free();
//close data base
$conn->close();


?>