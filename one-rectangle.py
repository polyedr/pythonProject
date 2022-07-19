from PIL import Image
import xml.etree.ElementTree as ET
from io import BytesIO
import webbrowser
import json
from jsonpath import jsonpath

with open('json-doc/via_project_18Jul2022_22h36m_json.json') as json_file:
    via_file = json.load(json_file)

# Extract element content from JSON #
filename_value = jsonpath(via_file, "$..filename")
size_value = jsonpath(via_file, "$..size")

name_shape_value = jsonpath(via_file, "$..shape_attributes.name")
x_value = jsonpath(via_file, "$..shape_attributes.x")
y_value = jsonpath(via_file, "$..shape_attributes.y")
width_value = jsonpath(via_file, "$..shape_attributes.width")
height_value = jsonpath(via_file, "$..shape_attributes.height")
element_region_value = jsonpath(via_file, "$..region_attributes.HTML element")

file_path = 'image/' + filename_value[0]

img = Image.open(file_path)
w = img.width
h = img.height

# Build ElementTree #
root = ET.Element("div")
div1 = ET.SubElement(root, "div")
div1.set('class', 'div1')
img = ET.SubElement(div1, "img")
img.set('src', file_path)
img.set('class', 'img')
div2 = ET.SubElement(div1, "div")
div2.set('class', 'div2')
div2.text = str(element_region_value[0])

# Convert to XML #
tree = ET.ElementTree(root)
io = BytesIO()
tree.write(io)
xml = io.getvalue().decode('UTF8')

index_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        .div1 {
            background-color: transparent;
            height: 1000px;
            width: 1000px;
            padding: 0;
            border: 1px solid black;
            display: block;
        }
        .img {
            position: absolute;
        }
        .div2 {
            position: absolute;
            background-color: transparent;
            height: """ + str(height_value[0]) + """px;
            width: """ + str(width_value[0]) + """px;
            margin-left: """ + str(x_value[0]) + """px;
            margin-top: """ + str(y_value[0]) + """px;
            padding: 0;
            text-align:center;
            box-sizing: border-box;
            font-size:10pt;
            border: 5px solid yellow;
            display: block;
        }
    </style>
</head>
<body>
        """ + str(xml) + """
</body>
</html>
"""

GET_HTML = "one-rectangle.html"
f = open(GET_HTML, 'w')
f.write(index_page)
f.close()

webbrowser.open("one-rectangle.html")
