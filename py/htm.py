# ---
# htm.py
# ---

header_markup = """
<!DOCTYPE html>
<html>
<head>
<title>
    AECI Power Production - 
    Primary Frequency Response Analysis and Reporting Interface
</title>
<link rel="stylesheet" type="text/css" href="css/base_css.css" />
<script src="js/base_js.js"></script>
</head>
<body>
<h2>Primary Frequency Response Reporting Interface</h2>
<hr/>
"""

footer_markup = """
</body>
</html>
"""

index_nav_markup = """
<!-- Index Year Navigation Start -->
<div id='index_nav'>
    <table>
        <tr>
            <td><a href=''>2017</a></td>
            <td><a href=''>2018</a></td>
            <td><a href=''>2019</a></td>
            <td><a href=''>2020</a></td>
            <td><a href='basics.html'>PFR Basics</a></td>
        </tr>
    </table>
</div>
<!-- Index Year Navigation End -->
"""

event_nav_markup = """
<!-- Event Navigation Start -->
<div id='event_nav'>
    <table>
        <tr>
            <td><a href=''>Index</a></td> 
            <td><a href='basics.html'>PFR Basics</a></td>
        </tr>
    </table>
</div>
<!-- Event Navigation End -->
"""

# ---
# Combine the markup for master htm strings
# ---
index_master_markup = \
header_markup + \
index_nav_markup + \
footer_markup

event_master_markup = \
header_markup + \
event_nav_markup + \
footer_markup

