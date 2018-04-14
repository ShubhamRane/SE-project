
<?php
	
	// define('UPLOAD_DIR', 'images/');
	// $img = $_POST['img'];
	// $img = str_replace('data:image/png;base64,', '', $img);
	// $img = str_replace(' ', '+', $img);
	// $data = base64_decode($img);
	// $file = UPLOAD_DIR . uniqid() . '.png';
	// $success = file_put_contents($file, $data);
	// print $success ? $file : 'Unable to save the file.';
	// $result = shell_exec("python predict.py $filename");
	// echo "{'prediction':'$result'}";
$data = substr($_POST['imageData'], strpos($_POST['imageData'], ",") + 1);
$decodedData = base64_decode($data);
$fp = fopen("canvas.png", 'wb');
fwrite($fp, $decodedData);
fclose();
echo "canvas.png";
?>
