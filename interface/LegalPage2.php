<?php
error_reporting(0);
session_start();
if (!isset($_SESSION["is_auth"])) {
	header("location: Login.html");
	exit();
}
	include_once("connectdb.php");
	//select database
	mysql_select_db('puru', $db) or die("Couldn't find DB!");
		if(isset($_POST['search'])){
	
		$search = $_POST['search'];
	    $search1 = $_POST['search1'];

}
	if(isset($_POST['select'])){
		$select = $_POST['select'];
		
		switch ($select) {
		
			
            
			case 'dc':
				$sql = "SELECT * FROM legal_compliance where Drug LIKE '%$search%' AND Company LIKE '%$search1%'";
				$records = mysql_query($sql);
			break;

			case 'yc':
				$sql = "SELECT * FROM legal_compliance where Year LIKE '%$search%' AND Company LIKE '%$search1%'";
				$records = mysql_query($sql);
			break;
			
			case 'spon1':
				$sql = "SELECT * FROM legal_compliance where Company LIKE '%" .'$search'. "%'";
				$records = mysql_query($sql);
			break;


			case 'all1':
				$sql = "SELECT * FROM legal_compliance where Company LIKE '%$search' AND Drug LIKE '%$search2'";
				$records = mysql_query($sql);
			break;
			
		}
	}
?>
<!DOCTYPE html>
<html>
<head>
	<title>Bioethics International: Score Page</title>
</head>
<style>
	table {
	    border-collapse: collapse;
	    width: 100%;
	}
	th, td {
	    padding: 8px;
	    text-align: left;
	    border-bottom: 1px solid #ddd;
	}
	tr:nth-child(even) {background-color: #f2f2f2}
	th {
	    background-color: #2eb8b8;
	    color: white;
	}
	
	body {
    	background-color: aliceblue;
	}
</style>

<body>

    <h1 align=right>Top companies</h1>
    <div align = "right">
        <ul> 
        <p><a href="ima.html" style="font-size:36px;" style="color:blue;" >Pfizer</a></p>
        <p><a href="http://en.wikipedia.org/wiki/Tennis" style="font-size:36px;">Sanofi</a></p>
        <p><a href="http://en.wikipedia.org/wiki/Rugby_football" style="font-size:36px;">Novartis</a></p>
        </ul>

    </div>

    
    <form action="LegalPage2.php">
    <input type="submit" value="Previous" />
    </form>
    

	<h1 align=center>Bioethics International Database: Score Page for Advanced search</h1>
	<div align = "center">	
	<form action = "LegalPage2.php" method = "POST">
		<p>
		Advanced Search   <select name = "select">
		  <option value="yc">Year and Company</option>
		  
		  <option value="dc">Drug Name and Company</option>
		  
		</select>
		
		<input type = "text" name = "search" placeholder = "Search for drugs..."/>
		<input type = "text" name = "search1" placeholder = "Search for drugs..."/>
		

		<input type = "submit" name = "submit" value = ">>"/>

    </p>
    </form>
	




   	</div>
	<p align="right">
  		<a href="logout.php">Logout</a>
	</p><br/><br/>
	
	<table>
		<tr>
			<th>Year</th>
			<th>Drug</th>
			<th>Company</th>
			<th>Definition_1_number of trials</th>
			<th>Def1_Registration</th>
			<th>Def1_Reporting</th>
			<th>Def1_Compliance</th>
			<th>Definition_2_number of trials</th>
			<th>Def2_Registration</th>
			<th>Def2_Reporting</th>
			<th>Def2_Compliance</th>
			
		</tr>
		
		<?php
			while($record = mysql_fetch_assoc($records)){ ?>
				<tr>
					<td>
						<?php echo $record['Year']; ?>
					</td>
					
					<td>
						<?php echo $record['Drug']; ?>
					</td>
					
					<td>
						<?php echo $record['Company']; ?>
					</td>
					
					<td>
						<?php echo $record['Definition_1_number of trials']; ?>
					</td>
					
					<td>
						<?php echo $record['Def1_Registration']; ?>
					</td>
					
					<td>
						<?php echo $record['Def1_Reporting']; ?>
					</td>
					
					<td>
						<?php echo $record['Def1_Compliance']; ?>
					</td>
					
					<td>
						<?php echo $record['Definition_2_number of trials']; ?>
					</td>
					
					<td>
						<?php echo $record['Def2_Registration']; ?>
					</td>
					
					<td>
						<?php echo $record['Def2_Reporting']; ?>
					</td>
					
					<td>
						<?php echo $record['Def2_Compliance']; ?>
					</td>
					
				
				</tr>
		<?php	}
		?>
	</table>
</body>
</html>