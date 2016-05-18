<!DOCTYPE html>
<html>
<head>
	<title></title>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
	<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
	 <script src="gmaps.js"></script>
<script type="text/javascript">
var map = new GMaps({
    div: '#map',
    lat: 51.5073346,
    lng: -0.1276831,
    width : 100%, 
    height : 150p
  });
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
			height: 800px ; 

		}

		#map
		{
			width: 300px ; 
			height: 400px ; 
		}
	</style>

</script>

</head>
<body>
<div class='mainDiv'>
	<h1>Ceci est la page de map</h1>
	<p>lat = {{lat}} et long = {{long}}

	<div id="map"></div>


</div>
</body>
</html>

