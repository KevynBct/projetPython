<!DOCTYPE html>
<html>
<head>
	<title></title>
	<style type="text/css">
		body {
			font-family : Helvetica;
			background-color : #D3FEE4;
		}

		h1 {
			font-family: Impact;
		}

		.mainDiv {
            background-color: white;
            width: 70%;
            height: 400px;
            margin-left: 15%;
            margin-top: 80px;
            min-height: 20%;
            border-radius: 5px;
            box-shadow: 2px 2px 0 0 grey;
		}
	</style>

</head>
<body>
<div class='mainDiv'>
	
        <table>
        	<tr>
        		<td>Sport</td>
        		<td>Adresse</td>
        		<td>Equipement</td>
        		<td>Ville</td>
        	</tr>
        	% for row in resultat:
        	<tr>
        		<td>{{row[3]}}</td>
        		<td>{{row[0]}}</td>
        		<td>{{row[2]}}</td>
        		<td>{{row[1]}}</td>
        		<td><a href="/map/{{row[4]}}/{{row[5]}}">Map</a></td>
        	</tr>
        	%end
        </table>
</div>
</body>
</html>