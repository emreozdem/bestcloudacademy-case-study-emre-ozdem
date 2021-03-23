<html>
<head>
<meta charset="utf-8">
<title>Deneme</title>
</head>
<body>


<?php
error_reporting(0);

$userinfo=array("firstname" =>$_GET["firstname"] ,"lastname"  =>$_GET["lastname"]);
echo json_encode($userinfo);




?>

</body>

</html>