<!DOCTYPE html>
<html lang="en">
<head>
    <title>post method ile json</title>
</head>
<body>

<?php



if(isset($_POST["firstname"]) && isset($_POST["lastname"]))

{
    
    $userinfo=array("firstname" =>$_POST["firstname"] ,"lastname"  =>$_POST["lastname"]);
    echo json_encode($userinfo);
    //	https://webhook.site/2692a602-d539-46a7-b864-a63f38c42cc0 unique webhook.site URL si
}




?>

<form action="" method="POST">
<input name="firstname" type="text" value="" />
<input name="lastname" type="text" value="" />
<input name="gonder" type="submit" value="Gönder" />
</form>


</body>