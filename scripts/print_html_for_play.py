import os
import sys
import json

def generateHTML():
	output_html_file = "play.html"

	# Start creating the HTML file content
	html_content = '''<html>
	<head>
	  <title>All Sets</title>
	  <link rel="icon" type="image/x-icon" href="/img/sets.png">
	  <link rel="stylesheet" href="/resources/mana.css">
	  <link rel="stylesheet" href="/resources/header.css">
	</head>
	<style>
		@font-face {
			font-family: 'Beleren Small Caps';
			src: url('/resources/beleren-caps.ttf');
		}
		@font-face {
			font-family: Beleren;
			src: url('/resources/beleren.ttf');
		}
		body {
			font-family: 'Helvetica', 'Arial', sans-serif;
			overscroll-behavior: none;
			margin: 0px;
			background-color: #f3f3f3;
			font-size: 20px;
			padding-bottom: 30px;
		}
		a {
			text-decoration: none;
			color: #171717;
		}
		.set-table {
			width: 60%;
			max-width: 1000px;
			display: grid;
			grid-template-columns: 1fr;
			padding-top: 20px;
			margin: auto;
		}
		.set-header-row {
			width: 100%;
			display: grid;
			grid-template-columns: 0.5fr 2.5fr 0.5fr 0.5fr;
			gap: 5px;
			font-weight: bold;
			padding-bottom: 10px;
		}
		.set-row {
			height: 6em;
			width: 100%;
			display: grid;
			grid-template-columns: 0.5fr 2.5fr 0.5fr 0.5fr;
			gap: 5px;
			align-items: center;
			border-top: 1px solid #171717;
		}
		.set-row:hover {
			background-color: #fafafa;
		}
		.set-row:nth-child(2n) {
		  background-color: #dedede;
		}
		.set-row:nth-child(2n):hover {
			background-color: #e6e6e6;
		}
		.set-row img {
			width: 70%;
			justify-self: center;
		}
		.set-title {
			font-family: Beleren;
			letter-spacing: .02em;
			font-size: 22px;
		}
		.set-group {
			font-family: Beleren Small Caps;
			text-align: center;
			font-size: 40px;
			padding-top: 20px;
		}
	</style>
	<body>
		'''

	with open(os.path.join('resources', 'snippets', 'header.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	html_content += '''

	<input type="text" id="display" class="hidden" value="cards-and-text"> <!-- here to make img-container-defs snippet work properly -->
	<div class="banner-container">
		<a class="set-banner" id="set-banner">
			<img class="set-logo" id="set-banner-logo">
			<div class="set-title" id="set-banner-title"></div>
		</a>
	</div>

	<div class="grid-container" id="grid">
	</div>

	<script>
'''

	with open(os.path.join('resources', 'snippets', 'random-card.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	html_content += '''
	</script>
</body>
</html>'''

	# Write the HTML content to the output HTML file
	with open(output_html_file, 'w', encoding='utf-8-sig') as file:
		file.write(html_content)

	print(f"HTML file saved as {output_html_file}")