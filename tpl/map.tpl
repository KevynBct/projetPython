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
			    lng: {{long}}
		  	});
			map.addMarker({
			  lat: {{lat}},
			  lng: {{long}},
			  icon: "/static/flag.jpg"
			});

		}
	</script>
	<style type="text/css">
		

 		body 
        {
            font-family : Helvetica;
            background: url("/static/tennis2.jpg");
            background-repeat:no-repeat;
            -webkit-background-size: cover;
		    -moz-background-size: cover;
		    -o-background-size: cover;
		    background-size: cover;

        }



		h1 
		{
			font-family: Impact;
		}


		#map
		{
			
			/*margin-top: 200px; */
			margin-left: 2px; 

			background-color: rgba(240, 240, 240, 0.5);
			text-align : center;
			width: 70%;
			margin-left: 0.5%;
			margin-top: 1%;
			border-radius: 5px;
			box-shadow: 2px 2px 0 0 grey;
			height: 500px ; 
			padding-top: 2px; 

		}

	</style>

</script>

</head>
<body onload="init()">

	<div id="map"></div>

</body>
</html>