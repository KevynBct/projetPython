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
            background-color: white;
            text-align : center;
            width: 70%;
            margin-left: 15%;
            border-radius: 5px;
            box-shadow: 2px 2px 0 0 grey;
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
                    <td>Lieu</td>
                </tr>
                <tr>
                    <td>
                        <select id="activite" name="activite">
                            % for nom in activite:
                                <option value="{{nom[0]}}">{{nom[0]}}
                            %end 
                        </select>
                    </td>
                    <td>
                        <select id="installation" name="installation">
                            <option value=""></option>
                            % for nom in installation:
                                <option value="{{nom[0]}}">{{nom[0]}}
                            %end 
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