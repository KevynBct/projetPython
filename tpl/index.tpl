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
            width : 70%;
            margin-left : 15%;
        }

        select {
            width : 100%;
        }

        td {
            width: 25%;
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
                        <select id="activite" name="activite">
                            
                        </select>
                    </td>
                    <td>
                        <select id="equipement" name="equipement" >
                           % for nom in equipement:
                                <option value="{{nom[0]}}">{{nom[0]}}
                            %end 
                        </select>
                    </td>
                    <td>
                        <select id="installation" name="installation">
                            
                        </select>
                    </td>
                </tr>
            </table>
            </br>
            <input value="Valider" type="submit">
        </form>
    </div>
</body>
</html>