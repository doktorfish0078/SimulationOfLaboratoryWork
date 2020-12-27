import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QSlider, QWidget
from PyQt5.QtSvg import QSvgWidget

svg_str = """<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 24.3.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 966.32 737.81" style="enable-background:new 0 0 966.32 737.81;" xml:space="preserve">
<g id="Ванна">
	<path style="fill:#3C3C3B;stroke:#000000;stroke-miterlimit:10;" d="M109.69,3.67v623.62h850.4V3.67H109.69z M931.74,598.94h-793.7
		V32.01h793.7V598.94z"/>
	<line style="fill:none;stroke:#000000;stroke-miterlimit:10;" x1="138.04" y1="32.01" x2="109.69" y2="3.67"/>
	<line style="fill:none;stroke:#000000;stroke-miterlimit:10;" x1="931.74" y1="32.01" x2="960.09" y2="3.67"/>
	<line style="fill:none;stroke:#000000;stroke-miterlimit:10;" x1="109.69" y1="627.29" x2="138.04" y2="598.94"/>
	<line style="fill:none;stroke:#000000;stroke-miterlimit:10;" x1="931.74" y1="598.94" x2="960.09" y2="627.29"/>
	<rect x="138.03" y="32.01" style="fill:#00AFB6;stroke:#000000;stroke-miterlimit:10;" width="793.7" height="566.93"/>
</g>
<g id="Зонд">
	<g transform="translate({x} {y})">
		<path style="fill:#BF1C1D;stroke:#000000;stroke-miterlimit:10;" d="M104.82,90.27c0,12.54-10.15,22.69-22.66,22.69h-0.25
			l10-10.39l0.06-0.06c1.04-0.83,1.99-1.81,2.76-2.91l0.06-0.06c1.93-2.61,3.04-5.8,3.04-9.26c0-8.65-7.02-15.67-15.67-15.67
			c-4.17,0-7.94,1.63-10.76,4.29l-0.74,0.74L59.5,91.13c-0.03-0.28-0.03-0.58-0.03-0.86c0-12.51,10.15-22.66,22.69-22.66h0.15
			c12.08,0.09,21.89,9.6,22.44,21.55C104.82,89.54,104.82,89.91,104.82,90.27z"/>
		<path style="fill:#BF1C1D;stroke:#000000;stroke-miterlimit:10;" d="M94.73,99.59c-0.77,1.1-1.72,2.08-2.76,2.91L94.73,99.59z"/>
		<path style="fill:#BF1C1D;stroke:#000000;stroke-miterlimit:10;" d="M64.53,124.73c0,4.06-1.54,7.75-4.08,10.56l-0.52,0.55
			c-2.82,2.85-6.75,4.59-11.1,4.59c-8.68,0-15.7-7.05-15.7-15.7c0-4.32,1.75-8.25,4.6-11.1c2.82-2.85,6.75-4.59,11.1-4.59
			C57.5,109.05,64.53,116.06,64.53,124.73z"/>
		<path style="fill:#BF1C1D;stroke:#000000;stroke-miterlimit:10;" d="M94.73,99.59c-0.77,1.1-1.72,2.08-2.76,2.91L94.73,99.59z"/>
		<path style="fill:#BF1C1D;stroke:#000000;stroke-miterlimit:10;" d="M97.82,90.27c0,3.46-1.09,6.66-3.03,9.27l-0.06,0.06
			l-2.76,2.91l-0.06,0.06l-10,10.39l-21.46,22.33c2.53-2.8,4.08-6.49,4.08-10.56c0-8.67-7.03-15.69-15.7-15.69
			c-4.35,0-8.28,1.74-11.1,4.59l21.76-22.51l11.17-11.49l0.73-0.73c2.82-2.67,6.58-4.3,10.75-4.3
			C90.81,74.6,97.82,81.63,97.82,90.27z"/>
		<path style="fill:#BF1C1D;stroke:#000000;stroke-miterlimit:10;" d="M130.17,56.69c0,3.31-1.03,6.42-2.82,8.95l-3.25,3.4
			c-0.03,0.03-0.03,0.03-0.06,0.06l-19.28,20.06C104.2,77.21,94.39,67.7,82.32,67.61l19.28-19.93c0.03-0.03,0.03-0.03,0.06-0.06
			l3.21-3.31c2.67-2.08,5.98-3.31,9.6-3.31C123.15,40.99,130.17,48.03,130.17,56.69z"/>
		<path style="fill:#BF1C1D;stroke:#000000;stroke-miterlimit:10;" d="M104.88,44.31l-3.22,3.31
			C102.58,46.37,103.65,45.23,104.88,44.31z"/>
		<path style="fill:#BF1C1D;stroke:#000000;stroke-miterlimit:10;" d="M127.35,65.65c-0.89,1.29-1.99,2.45-3.25,3.4L127.35,65.65z"
			/>
		<line style="fill:#BF1C1D;stroke:#000000;stroke-miterlimit:10;" x1="125" y1="45.04" x2="138.04" y2="32.01"/>
		<path style="fill:none;stroke:#000000;stroke-miterlimit:10;" d="M55.52,124.85c0,1.18-0.3,2.28-0.85,3.24
			c-0.12,0.21-0.24,0.42-0.37,0.61c0.02,0.02,0,0.02-0.02,0.03c-1.21,1.71-3.22,2.82-5.47,2.82c-3.7,0-6.72-3-6.72-6.7
			c0-1.41,0.43-2.73,1.17-3.81c1.23-1.75,3.25-2.91,5.55-2.91C52.51,118.13,55.52,121.13,55.52,124.85z"/>
		<path style="fill:#941914;stroke:#000000;stroke-miterlimit:10;" d="M53.97,128.41c-0.72,3.39-13.15,10.45-13.15,10.45
			c-4.79,2.72-9.05,5.61-13.89,9.85c-2.71,2.38-5.34,5.07-6.57,8.46c-1.45,4.03-0.88,8.91-3.6,12.22l-11.52-7.11
			c2.71-3.33,2.14-8.19,3.6-12.22c1.23-3.4,3.85-6.09,6.57-8.47c4.91-4.31,8.14-6.16,13.89-9.85c3.48-2.24,8.43-5.66,14.09-10.51
			c0.42-0.22,0.84-0.44,1.27-0.65c0.32-0.08,0.79-0.19,1.35-0.26c1.11-0.13,3.02-0.36,4.93,0.66c0.38,0.2,2.12,1.14,2.84,3.08
			c0.4,1.07,0.39,2.16,0.38,2.65C54.16,126.7,54.15,127.57,53.97,128.41z"/>
		<line style="fill:none;stroke:#000000;stroke-miterlimit:10;" x1="16.77" y1="140.43" x2="16.77" y2="140.43"/>
		<path style="fill:#941914;stroke:#000000;stroke-miterlimit:10;" d="M63.49,149.48"/>
	</g>
</g>
</svg>

"""

app = QApplication(sys.argv)

layout = QGridLayout()  # планировка
widget = QWidget()
widget.setLayout(layout)

svgWidget = QSvgWidget()  # SVG виджет
svg_bytes = bytearray(svg_str.format(x='0', y='0'), encoding='utf-8')  # подставить угол и перевести в байтовую строку
svgWidget.renderer().load(svg_bytes)  # загрузить SVG в виджет
layout.addWidget(svgWidget)

sliderX = QSlider(Qt.Horizontal)  # слайдер
sliderX.setRange(0, 793)
sliderY = QSlider(Qt.Horizontal)  # слайдер
sliderY.setRange(0, 566)

def updateSVG():
    """ Обновляет SVG при движении слайдера"""
    x = sliderX.value()
    y = sliderY.value()
    svg_bytes = bytearray(svg_str.format(x=str(x), y=str(y)), encoding='utf-8')  # обновить угол и перевести в байтовую строку
    svgWidget.renderer().load(svg_bytes)  # загрузить SVG в виджет


sliderX.valueChanged.connect(updateSVG)
sliderY.valueChanged.connect(updateSVG)

layout.addWidget(sliderX)
layout.addWidget(sliderY)
widget.show()

sys.exit(app.exec_())
