<!DOCTYPE html>
<html>
<head>
	<title></title>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
	<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
	<script src="/static/gmaps.js"></script>
	<script type="text/javascript">
		function init()
		{
			var map = new GMaps({
			    div: '#map',
			    lat: {{lat}},
			    lng: -0.1276831
		  	});


		}
	</script>
	<style type="text/css">
		body 
		{
			font-family : Helvetica;
			background-color : #D3FEE4;
		}

		h1 
		{
			font-family: Impact;
		}

		.mainDiv 
		{
			background-color: white;
			text-align : center;
			width: 70%;
			margin-left: 15%;
			border-radius: 5px;
			box-shadow: 2px 2px 0 0 grey;
			height: 500px ; 

		}

		#map
		{
			width: 90% ; 
			height: 400px ; 
			margin-left: 5%;
		}
	</style>

</script>

</head>
<body onload="init()">
<div class='mainDiv'>
	<h1>Ceci est la page de map</h1>
	<p>lat =  et long = {{long}}

	<div id="map"></div>


</div>
</body>
</html>