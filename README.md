<p><strong>usage: mqttForTerminal [-h] [-t TOPIC] [-m MESSAGE] [-r]</strong></p>
<p>options:</p>
<div>
	<table>
		<tr>
			<th>-h, --help</th>
			<th>show this help message and exit</th>
		</tr>
		<tr>
			<th>-t, --topic</th>
			<th>MQTT topic</th>
		</tr>
		<tr>
			<th>-m, --message</th>
			<th>Message to send</th>
		</tr>
		<tr>
			<th>-r, --read</th>
			<th>Read messages from topic</th>
		</tr>
	</table>
</div>
<br>
<p><strong>Examples</strong></p>
<p>./mqttForTerminal -t mqttTerminal/mytopic -m "Hi"</p>
<p>Response: OK</p>
<br>
<p>./mqttForTerminal -t mqttTerminal/mytopic -r</p>
<p>Response: Hi</p>
