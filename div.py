import xml.etree.ElementTree as ET
from io import BytesIO

# Build XML ElementTree #
root = ET.Element("div")

div1 = ET.SubElement(root, "div")
div1.set('class', 'div1')
div1.text = str("div1")

div2 = ET.SubElement(root, "div")
div2.set('class', 'div2')
div2.text = str("div2")

div3 = ET.SubElement(root, "div")
div3.set('class', 'div3')
div3.text = str("div3")

tree = ET.ElementTree(root)
io = BytesIO()
tree.write(io)
xml = io.getvalue().decode('UTF8')
# print(xml)

index_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DIV</title>
    <style>
        .div1 {
            float: left;
            background-color: transparent;
            height: 100px;
            width: 200px;
            padding: 0;
            border: 3px solid yellow;
            display: block;
        }
        .div2 {
            background-color: transparent;
            height: 200px;
            width: 400px;
            margin-left: 200px;
            margin-top: 100px;
            padding: 0;
            border: 3px solid red;
            display: inline-block;
        }
        .div3 {
            float: right;
            background-color: transparent;
            height: 100px;
            width: 200px;
            margin-top: 100px;
            padding: 0;
            border: 3px solid green;
            display: inline-block;
        }
    </style>
</head>
<body>
        %s
</body>
</html>
""" % (xml)

GET_HTML = "div.html"
f = open(GET_HTML, 'w')
f.write(index_page)
f.close()
