<?php
	$filename = "";
	$result = exec_shell("python predict.py $filename");
	echo "{'prediction':'$result'}";
?>
	
