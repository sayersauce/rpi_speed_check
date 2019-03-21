<?php

$host = '';
$username = '';
$password = '';
$name = '';

$conn = mysqli_connect($host,$username,$password,$name);

$sql = "select * from SPEEDS order by id desc;";
$result = mysqli_query($conn, $sql);
$no_results = 0;

while ($row = mysqli_fetch_assoc($result)){
   if ($no_results == 0){
	echo '<h3 class="latest_speed">' . number_format(floatval($row['speed'])/125000, 2) . " Mbps" . '</h3>';
	echo "<br>";
	echo "<table>";
	echo "<tr>";
	echo "<th>Download Speed</th>";
	echo "<th>ID</th>";
	echo "<th>Date/Time</th>";
	echo "<tr>";
   }
   if ($no_results < 10){
        echo "<tr>";
        echo "<td>" . number_format(floatval($row['speed'])/125000, 2) . " Mb/s" . "</td>";
        echo "<td>" . $row['id'] . "</td>";
        echo "<td>" . $row['time'] . "</td>";
        echo "</tr>";
        $no_results += 1;
    }
}

echo "</table>";
