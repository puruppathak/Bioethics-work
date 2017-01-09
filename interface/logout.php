<?php

session_start();
unset($_SESSION['is_auth']);
session_destroy();
header("location:Login.html");
exit();

?>