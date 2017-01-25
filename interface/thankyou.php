<?php

require 'connection.php'; 
$conn    = Connect();
$dname    = $conn->real_escape_string($_POST['FDA_Drug_Name']);
$ddate   = $conn->real_escape_string($_POST['FDA_Drug_Approval_Date']);
$orgid    = $conn->real_escape_string($_POST['FDA_Org_ID']);
$altid = $conn->real_escape_string($_POST['FDA_Alt_ID']);
$query   = "INSERT into master (FDA_Drug_Name,FDA_Drug_Approval_Date,FDA_Org_ID,FDA_Alt_ID) VALUES('" . $dname . "','" . $ddate . "','" . $orgid . "','" . $altid . "')";
$success = $conn->query($query);

if (!$success) {
    die("Couldn't enter data: ".$conn->error);

}

echo "Thank You! Your data has been recorded. <br>";

$conn->close();

?>