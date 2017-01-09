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
	}

	if(isset($_POST['select'])){
		$select = $_POST['select'];
		
		switch ($select) {
		
			case 'all':
				$sql = "SELECT * FROM master";
				$records = mysql_query($sql);
			break;
			

            case 'drugASC':
				$sql = "SELECT * FROM master where FDA_Drug_Name LIKE '%$search%' ORDER BY FDA_Phase DESC";
				$records = mysql_query($sql);
			break;

			case 'drug':
				$sql = "SELECT * FROM master where FDA_Drug_Name LIKE '%$search%'";
				$records = mysql_query($sql);
			break;
			
			case 'org_id':
				$sql = "SELECT * FROM master where FDA_Org_ID LIKE '%$search%'";
				$records = mysql_query($sql);
			break;
			
			case 'nct':
				$sql = "SELECT * FROM master where CT_NCT LIKE '%$search%'";
				$records = mysql_query($sql);
			break;
			
			case 'sponsor':
				$sql = "SELECT * FROM master where FDA_Sponsor_Country LIKE '%$search%'";
				$records = mysql_query($sql);
			break;
			
		}
	}
?>
<!DOCTYPE html>
<html>
<head>
	<title>Bioethics International</title>
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
	<h1 align=center>Bioethics International Database</h1>
	<div align = "center">	
	<form action = "WebApp.php" method = "POST">
		Basic Search   <select name = "select">
		  <option value="all">All</option>
		  <option value="drug">Drug Name</option>
		  <option value="org_id">Org ID</option>
		  <option value="nct">NCT</option>
		  <option value="sponsor">Sponsor</option>
		  <option value="drugASC">Drug Name ASC</option>
		</select>
		
		<input type = "text" name = "search" placeholder = "Search for drugs..."/>
		<input type = "submit" name = "submit" value = ">>"/>

       <p>
  Search in Ascending <select name = "select">
		  <option value="all">All</option>
		  <option value="drug">Drug Name</option>
		  <option value="org_id">Org ID</option>
		  <option value="nct">NCT</option>
		  <option value="sponsor">Sponsor</option>
		  <option value="drugASC">Drug Name ASC</option>
		</select>
		
		<input type = "text" name = "search" placeholder = "Search for drugs..."/>
		<input type = "submit" name = "submit" value = ">>"/>
       </p>


       <p>
        Search in Descending <select name = "select">
		  <option value="all">All</option>
		  <option value="drug">Drug Name</option>
		  <option value="org_id">Org ID</option>
		  <option value="nct">NCT</option>
		  <option value="sponsor">Sponsor</option>
		  <option value="drugASC">Drug Name ASC</option>
		</select>
		
		<input type = "text" name = "search" placeholder = "Search for drugs..."/>
		<input type = "submit" name = "submit" value = ">>"/>
       </p>



	</form> 
	</div>
	<p align="right">
  		<a href="logout.php">Logout</a>
	</p><br/><br/>
	
	<table>
		<tr>
			<th>FDA_Drug_Name</th>
			<th>FDA_Org_ID</th>
			<th>FDA_Drug_Approval_Date</th>
			<th>FDA_Alt_ID</th>
			<th>FDA_Phase</th>
			<th>FDA_Type</th>
			<th>FDA_Study_Population</th>
			<th>FDA_Participants</th>
			<th>FDA_Countries</th>
			<th>FDA_Review_Page</th>
			<th>FDA_Dosage</th>
			<th>FDA_Sponsor_Country</th>
			<th>CT_NCT</th>
			<th>CT_Brief_Title</th>
			<th>CT_Conditions</th>
			<th>CT_Status</th>
			<th>CT_Interventions</th>
			<th>CT_Acronym</th>
			<th>CT_Agency</th>
			<th>CT_Study_Type</th>
			<th>CT_Enrollment</th>
			<th>CT_Agency_Class</th>
			<th>CT_Phase</th>
			<th>CT_Study_Design</th>
			<th>CT_Secondary_ID</th>
			<th>CT_First_Received_Date</th>
			<th>CT_Start_Date</th>
			<th>CT_Completion_Date</th>
			<th>CT_Last_Changed_Date</th>
			<th>CT_Verification_Date</th>
			<th>Derived_CT_Is_Result</th>
			<th>CT_First_Received_Results_Date</th>
			<th>Derived_CT_Is_Certificate</th>
			<th>CT_Certificate_Of_Delay</th>
			<th>CT_PCD</th>
			<th>CT_Countries</th>
			<th>CT_CSR_Summary</th>
			<th>CT_Study_Arms</th>
			<th>CT_Is_FDA_Regulated</th>
			<th>CT_Is_Section_801</th>
			<th>Pubmed_Link</th>
			<th>Pubmed_Published_Date</th>
			<th>Pubmed_Abstract</th>
			<th>Pubmed_NCT</th>
			<th>Pubmed_Type_Design</th>
			<th>Pubmed_Enrollment</th>
			<th>Pubmed_Phase</th>
			<th>Pubmed_Conditions</th>
			<th>Pubmed_Location</th>
			<th>Derived_FDA_Applicable</th>
			<th>Derived_Ethics_2_Applicable</th>
			<th>Derived_CT_Results_Within_30_Days</th>
			<th>Derived_Is_Reported</th>
			<th>Derived_Is_Published</th>
			<th>Derived_Is_Available</th>
			<th>Derived_Is_Registered</th>
			<th>Derived_Has_US_Site</th>
			<th>Derived_Is_DataSharing_Applicable</th>
			<th>Derived_Results_Within_1_Year</th>
			<th>Derived_FDAAA_Timely_Registration</th>
			<th>Derived_Is_FDA_Compliant</th>
			<th>Derived_Is_FDA_Compliant_Certificate</th>
			<th>Derived_Ethics_Applicable</th>
			<th>Derived_Is_Published_Cutoff</th>
			<th>Derived_Certificate_Validation</th>
			<th>Derived_Certificate_Expression_Date</th>
			<th>Derived_FDAAA_2017_Compliant</th>
		</tr>
		
		<?php
			while($record = mysql_fetch_assoc($records)){ ?>
				<tr>
					<td>
						<?php echo $record['FDA_Drug_Name']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Org_ID']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Drug_Approval_Date']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Alt_ID']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Phase']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Type']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Study_Population']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Participants']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Countries']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Review_Page']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Dosage']; ?>
					</td>
					
					<td>
						<?php echo $record['FDA_Sponsor_Country']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_NCT']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Brief_Title']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Conditions']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Status']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Interventions']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Acronym']; ?>
					</td>

					<td>
						<?php echo $record['CT_Agency']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Study_Type']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Enrollment']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Agency_Class']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Phase']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Study_Design']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Secondary_ID']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_First_Received_Date']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Start_Date']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Completion_Date']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Last_Changed_Date']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Verification_Date']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_CT_Is_Result']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_First_Received_Results_Date']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_CT_Is_Certificate']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Certificate_Of_Delay']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_PCD']; ?>
					</td>			
					
					<td>
						<?php echo $record['CT_Countries']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_CSR_Summary']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Study_Arms']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Is_FDA_Regulated']; ?>
					</td>
					
					<td>
						<?php echo $record['CT_Is_Section_801']; ?>
					</td>
					
					<td>
						<?php echo $record['Pubmed_Link']; ?>
					</td>
					
					<td>
						<?php echo $record['Pubmed_Published_Date']; ?>
					</td>
					
					<td>
						<?php echo $record['Pubmed_Abstract']; ?>
					</td>
					
					<td>
						<?php echo $record['Pubmed_NCT']; ?>
					</td>
					
					<td>
						<?php echo $record['Pubmed_Type_Design']; ?>
					</td>
					
					<td>
						<?php echo $record['Pubmed_Enrollment']; ?>
					</td>
					
					<td>
						<?php echo $record['Pubmed_Phase']; ?>
					</td>
					
					<td>
						<?php echo $record['Pubmed_Conditions']; ?>
					</td>
					
					<td>
						<?php echo $record['Pubmed_Location']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_FDA_Applicable']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Ethics_2_Applicable']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_CT_Results_Within_30_Days']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Is_Reported']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Is_Published']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Is_Applicable']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Is_Registered']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Has_US_Site']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Is_DataSharing_Applicable']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Results_Within_1_Year']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_FDAAA_Timely_Registration']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Is_FDA_Compliant']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Ethics_Applicable']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Is_Published_Cutoff']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Certificate_Validation']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Certificate_Validation']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_Certificate_Expression_Date']; ?>
					</td>
					
					<td>
						<?php echo $record['Derived_FDAAA_2017_Compliant']; ?>
					</td>
				</tr>
		<?php	}
		?>
	</table>
</body>
</html>