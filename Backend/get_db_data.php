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

$sql = "SELECT * FROM rasp_commands";
$result = $conn->query($sql);

//echo "num of rows in Table TelState is: ";
//echo $result->num_rows."<br/>";

if ($result->num_rows > 0) {
	
    // output data of each row
    while($row = $result->fetch_assoc()) {
       
		$array = $row; 
		$keys = array_keys($array);

		for($i=0; $i < count($keys); ++$i) {
			//echo $keys[$i] . '=' . $array[$keys[$i]] . "\n";
		}
		//echo "<br/><br/><br/><br/>";
		echo json_encode($row);
		//echo "<br/><br/><br/><br/>";	
		break;
    }

} else {
    echo "0 results";
}

/* free result set */
$result->free();

//close data base
$conn->close();

?>