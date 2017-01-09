<!DOCTYPE html>
<html>
<head><title></title></head>
<body>

	<script type="text/javascript">
	function Invalid() {
	    alert("Wrong user ID and password!");
	}
	</script>

</body>
</html>


<?php
session_start();
include_once("connectdb.php");

//select database
mysql_select_db('puru', $db) or die("Couldn't find DB!");

	if (isset($_POST["username"]) and isset($_POST["password"])) {
	    
		$username = $_POST["username"];
		$password = $_POST["password"];
		$_SESSION["username"] = $username;
		$_SESSION['is_auth'] = true;

	    $query = "Select * from usercredentials where User_Name='$username' and Password='$password';";
		$result = mysql_query($query);

	    if (mysql_num_rows($result)) {
	        include_once("WebApp.php");
	    } else {
	        echo '<script type="text/javascript"> Invalid(); </script>';

	        include("Login.html");
	    }
	} else {
	    echo '<script type="text/javascript"> Invalid(); </script>';
	    include("Login.html");
	}

?>