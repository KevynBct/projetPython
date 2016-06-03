<!DOCTYPE html>
<html>
<head>
	<title></title>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8/jquery.min.js"></script>
    <link rel="stylesheet" type="text/css" href="/static/jquery.dataTables.min.css"/>
    <script type="text/javascript" src="/static/jquery.dataTables.min.js"></script>

    <script type="text/javascript">
        function init() {
            $('#table').DataTable();
        }
    </script>

	<style type="text/css">

        body 
        {
            font-family : Helvetica;
            background: url("/static/boxe.jpg")no-repeat center fixed; 
            -webkit-background-size: cover;
            background-size: cover;

        }


		h1 
        {
			font-family: Impact;
		}

		.mainDiv {
            
            background-color: rgba(240, 240, 240, 0.5);
            width: 70%;
            margin-left: 15%;
            margin-top: 80px;
            min-height: 20%;
            border-radius: 10px;
            box-shadow: 2px 2px 0 0 grey;
            padding-top: 0.5px; 
		}

/*        a.top {
           position:fixed;
        }*/


/*        .backtotop
        {
            position:fixed;
            height:10px;
            width:50px; 
            bottom:300px;
            right:0px;
            border-radius:4px 0 0 4px;
            line-height:48px; 
            border-radius: 15px;
        }*/


</style>


</head>
<body onload="init()">
<div class='mainDiv'>

<!-- <a href="#" class="backtotop"><img src="/static/backtotop.png"></a> -->

        <table id="table">
            <thead>
                <tr>
                    <td class="colonne">Sport</td>
                    <td class="colonne">Adresse</td>
                    <td class="colonne">Equipement</td>
                    <td class="colonne">Ville</td>
                    <td class="colonne">Maps</td>
                </tr>
            </thead>
            <tbody>
                
                % for row in resultat:
                <tr>
                    <td style="text-indent: 10px">{{row[3]}}</td>
                    <td style="text-align:center">{{row[0]}}</td>
                    <td style="text-align: center">{{row[2]}}</td>
                    <td>{{row[1]}}</td>
                    <td><a href="/map/{{row[5]}}/{{row[4]}}">
                    <img src="/static/marker1.png"></a></td>
                </tr>
                %end
            </tbody>
       </table>


</div>
</body>
</html>