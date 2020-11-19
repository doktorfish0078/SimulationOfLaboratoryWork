import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QSlider, QWidget
from PyQt5.QtSvg import QSvgWidget


class svg_widget_ammeter:
    def __init__(self):
        self.svg_str = """<?xml version="1.0" encoding="utf-8"?>
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 73.7 73.7" style="enable-background:new 0 0 73.7 73.7;" xml:space="preserve">
<style type="text/css">
	.st0{{fill:#343434;}}
	.st1{{fill:#4E4D4D;}}
	.st2{{fill:#F2F2F2;}}
	.st3{{fill:#1B1B1B;}}
	.st4{{fill:none;stroke:#343434;stroke-width:0.5;stroke-miterlimit:10;}}
	.st5{{fill:none;stroke:#575756;stroke-miterlimit:10;}}
	.st6{{fill:none;stroke:#343434;stroke-width:0.75;stroke-miterlimit:10;}}
	.st7{{fill:#F2F2F2;stroke:#343434;stroke-miterlimit:10;}}
	.st8{{fill:#343434;stroke:#343434;stroke-miterlimit:10;}}
	.st9{{fill:none;stroke:#000000;stroke-width:0.5;stroke-miterlimit:10;}}
	.st10{{font-family:'ComicSansMS';}}
	.st11{{font-size:4px;}}
</style>
<g id="Слой_3">
	<path class="st0" d="M65.11,73.62H8.6c-4.7,0-8.51-3.81-8.51-8.51V8.6c0-4.7,3.81-8.51,8.51-8.51h56.51c4.7,0,8.51,3.81,8.51,8.51
		v56.51C73.62,69.81,69.81,73.62,65.11,73.62z"/>
	<path class="st1" d="M62.47,56.6H11.23c-4.14,0-7.49-3.35-7.49-7.49V12.68c0-4.14,3.35-7.49,7.49-7.49h51.23
		c4.14,0,7.49,3.35,7.49,7.49v36.43C69.96,53.24,66.6,56.6,62.47,56.6z"/>
	<path class="st2" d="M63.02,55.09H11.2c-2.68,0-4.85-2.17-4.85-4.85V13.98c0-2.68,2.17-4.85,4.85-4.85h51.82
		c2.68,0,4.85,2.17,4.85,4.85v36.26C67.87,52.91,65.7,55.09,63.02,55.09z"/>
	<g>
		<path class="st3" d="M33.46,67.97l5.6-7.76c-0.66-0.34-1.41-0.55-2.21-0.55c-2.68,0-4.85,2.17-4.85,4.85
			C32,65.87,32.56,67.09,33.46,67.97z"/>
		<path class="st3" d="M40.24,61.05l-5.6,7.76c0.66,0.34,1.41,0.55,2.21,0.55c2.68,0,4.85-2.17,4.85-4.85
			C41.7,63.15,41.14,61.93,40.24,61.05z"/>
	</g>
	<path class="st0" d="M28.6,53.5c0,0,1.08-5.62,8.25-5.62s8.25,5.62,8.25,5.62H28.6z"/>
	<line class="st2" x1="21.05" y1="32.91" x2="18.68" y2="29.91"/>
	<path class="st4" d="M62.5,49.04h-4.16c-0.6,0-1.09-0.49-1.09-1.09v-4.16c0-0.6,0.49-1.09,1.09-1.09h4.16
		c0.6,0,1.09,0.49,1.09,1.09v4.16C63.58,48.55,63.1,49.04,62.5,49.04z"/>
	<polyline class="st5" points="34.49,47.89 37,40.68 39.25,47.89 	"/>
	<line class="st5" x1="35.19" y1="45.77" x2="38.55" y2="45.77"/>
	<polyline class="st6" points="11.08,52.19 12.29,52.19 13.51,52.19 	"/>
	<line class="st6" x1="12.29" y1="49.22" x2="12.29" y2="52.19"/>
	<path class="st6" d="M14.24,52.19v-2.23c0,0,0-0.88,0.9-0.85s1.02,0.76,1.02,0.76v2.33"/>
	<line class="st6" x1="14.8" y1="52.11" x2="15.6" y2="52.11"/>
	<line class="st6" x1="17.1" y1="52.19" x2="19.2" y2="52.19"/>
	<path class="st4" d="M17.26,49.77c0,0,0.01-0.39,0.33-0.34c0.32,0.05,0.35,0.34,0.35,0.34l-0.68,1.28h0.72"/>
	<path class="st4" d="M18.31,51.09c0.34-0.01,0.52-0.19,0.52-0.19c0.3-0.95-0.4-0.98-0.4-0.98v-0.5h0.55"/>
	<polygon class="st4" points="20.65,50.3 21.45,51.14 21.22,52.11 22.14,51.61 23.26,52.19 23.1,51 23.8,50.34 22.9,50.11 
		22.23,49.19 21.63,50.04 	"/>
	<line class="st4" x1="60.54" y1="49.04" x2="60.54" y2="45.06"/>
	<polyline class="st4" points="59.37,46.1 60.56,44.86 61.71,46.1 	"/>
	<g transform="rotate({} 36.62 53.39)">
	<line class="st7" x1="36.62" y1="53.39" x2="36.62" y2="32.62"/>
	<circle class="st8" cx="36.62" cy="39.09" r="1.07"/>
	<polygon class="st8" points="36.56,29.82 37.7,34.4 35.55,34.4 	"/>
	</g>
</g>
<g id="Слой_2">
	<line class="st9" x1="36.85" y1="26.16" x2="36.85" y2="22.48"/>
	<path class="st9" d="M40.09,22.65"/>
	<path class="st9" d="M39.71,26.31"/>
	<path class="st9" d="M43.3,23.16"/>
	<path class="st9" d="M42.54,26.75"/>
	<path class="st9" d="M46.43,24"/>
	<path class="st9" d="M45.3,27.49"/>
	<line class="st9" x1="47.97" y1="28.52" x2="49.47" y2="25.17"/>
	<path class="st9" d="M52.36,26.64"/>
	<path class="st9" d="M50.52,29.82"/>
	<path class="st9" d="M55.08,28.41"/>
	<path class="st9" d="M52.92,31.38"/>
	<path class="st9" d="M57.6,30.45"/>
	<path class="st9" d="M55.15,33.18"/>
	<line class="st9" x1="57.17" y1="35.2" x2="59.9" y2="32.75"/>
	<path class="st9" d="M33.61,22.65"/>
	<path class="st9" d="M33.99,26.31"/>
	<path class="st9" d="M30.4,23.16"/>
	<path class="st9" d="M31.17,26.75"/>
	<path class="st9" d="M27.27,24"/>
	<path class="st9" d="M28.4,27.49"/>
	<line class="st9" x1="25.73" y1="28.52" x2="24.24" y2="25.17"/>
	<line class="st9" x1="16.53" y1="35.2" x2="13.8" y2="32.75"/>
	<line class="st9" x1="16.53" y1="35.2" x2="13.8" y2="32.75"/>
	<line class="st9" x1="13.16" y1="39.82" x2="8.99" y2="37.41"/>
	<line class="st9" x1="60.54" y1="39.82" x2="64.71" y2="37.41"/>
	<line class="st9" x1="52.93" y1="31.37" x2="55.76" y2="27.47"/>
	<line class="st9" x1="42.54" y1="26.75" x2="43.54" y2="22.03"/>
	<line class="st9" x1="31.16" y1="26.75" x2="30.16" y2="22.03"/>
	<line class="st9" x1="20.77" y1="31.37" x2="17.94" y2="27.47"/>
	<line class="st9" x1="14.74" y1="37.44" x2="12.99" y2="36.16"/>
	<line class="st9" x1="18.56" y1="33.19" x2="17.11" y2="31.58"/>
	<line class="st9" x1="23.19" y1="29.83" x2="22.1" y2="27.95"/>
	<line class="st9" x1="28.41" y1="27.51" x2="27.74" y2="25.45"/>
	<line class="st9" x1="33.99" y1="26.32" x2="33.77" y2="24.16"/>
	<line class="st9" x1="39.71" y1="26.32" x2="39.93" y2="24.16"/>
	<line class="st9" x1="45.3" y1="27.51" x2="45.97" y2="25.45"/>
	<line class="st9" x1="50.51" y1="29.83" x2="51.6" y2="27.95"/>
	<line class="st9" x1="55.14" y1="33.19" x2="56.59" y2="31.58"/>
	<line class="st9" x1="58.96" y1="37.44" x2="60.71" y2="36.16"/>
	<text transform="matrix(0.5 -0.866 0.866 0.5 8.4141 37.8727)" class="st10 st11">0</text>
	<text transform="matrix(0.7141 -0.5188 0.5878 0.809 15.5953 28.4077)" class="st10 st11">0.2</text>
	<text transform="matrix(0.9781 -0.2079 0.2079 0.9781 27.0153 21.7679)" class="st10 st11">0.4</text>
	<text transform="matrix(0.9781 0.2079 -0.2079 0.9781 40.9588 20.6846)" class="st10 st11">0.6</text>
	<text transform="matrix(0.809 0.5878 -0.5878 0.809 53.9314 25.2428)" class="st10 st11">0.8</text>
	<text transform="matrix(0.5 0.866 -0.866 0.5 64.6013 36.1688)" class="st10 st11">1</text>
</g>
</svg>
"""
        self.svg_widget = self.create_widget_ammeter()
        self.value_ammeter = 0

    def create_widget_ammeter(self):
        svg_widget = QSvgWidget()
        svg_bytes = bytearray(self.svg_str.format('-60'), encoding='utf-8')
        svg_widget.renderer().load(svg_bytes)
        return svg_widget

    def update_svg_ammeter(self, value_ammeter):
        # value_ammeter - это то количество амперов,которое нужно отобразить на приборе
        # 1 градус равен 0,0083 ампер, соответственно 120 градусов это 1 ампер, 0 это 0
        self.value_ammeter = value_ammeter

        angle = -60 + (value_ammeter / 0.0083)
        svg_bytes = bytearray(self.svg_str.format(str(angle)), encoding='utf-8')
        self.svg_widget.renderer().load(svg_bytes)

    def value(self):
        return self.value_ammeter
