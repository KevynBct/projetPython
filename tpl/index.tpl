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

        table {
            width : 60%;
            margin-left : 20%;
        }

        .mainDiv {
            background-color: #FFF;
            text-align : center;
            width: 70%;
            margin-left: 15%;
        }
    </style>

</head>
<body>
    <div class='mainDiv'>
        <h1> Effectuez votre recherche </h1>
        <form action="/index" method="post">
            <table>
                <tr>
                    <td>Activité</td>
                    <td>Equipement</td>
                    <td>Installation</td>
                </tr>
                <tr>
                    <td>
                        <select name="activite">
                            
                        </select>
                    </td>
                    <td>
                        <select name="equipement">
                            
                        </select>
                    </td>
                    <td>
                        <select name="installation">
                            
                        </select>
                    </td>
                    <td><input value="Valider" type="submit"></td>
                </tr>
            </table>
        </form>
    </div>
</body>
</html>