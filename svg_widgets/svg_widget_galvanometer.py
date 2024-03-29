from PyQt5.QtSvg import QSvgWidget


class svg_widget_galvanometer:
    """
    Свг-виджет, прибор гальванометр.
    Для использования в форме необходимо:
    1) создать layout с размером и желаемым расположением прибора
    2) добавить в этот layout поле self.svg_widget экземпляра данного класса
    3) всё готово!
    """
    def __init__(self):
        self.svg_str = """<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 24.3.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 286.09 255.83" style="enable-background:new 0 0 286.09 255.83;" xml:space="preserve">
<style type="text/css">
	.st0{{fill:#1B1B1B;}}
	.st1{{fill:#343434;}}
	.st2{{fill:#F2F2F2;}}
	.st3{{fill:#4E4D4D;}}
	.st4{{fill:#808181;}}
	.st5{{fill:none;stroke:#343434;stroke-width:0.75;stroke-miterlimit:10;}}
	.st6{{fill:none;}}
	.st7{{fill:#666159;}}
	.st8{{fill:none;stroke:#19495D;stroke-miterlimit:10;}}
	.st9{{fill:none;stroke:#19495D;stroke-width:0.5;stroke-miterlimit:10;}}
	.st10{{fill:#19495D;}}
	.st11{{font-family:'MyriadPro-Regular';}}
	.st12{{font-size:8px;}}
	.st13{{font-size:6px;}}
	.st14{{fill:#2F4950;}}
	.st15{{font-size:7px;}}
	.st16{{font-size:9px;}}
	.st17{{fill:#F1F1F1;stroke:#343434;stroke-miterlimit:10;}}
	.st18{{fill:#343434;stroke:#343434;stroke-miterlimit:10;}}
</style>
<g id="Слой_1">
	<path class="st0" d="M262.53,255.83H23.55C10.55,255.83,0,245.28,0,232.28V23.55C0,10.55,10.55,0,23.55,0h238.98
		c13.01,0,23.55,10.55,23.55,23.55v208.72C286.09,245.28,275.54,255.83,262.53,255.83z"/>
	<path class="st1" d="M258.26,170.89H31.19c-8.37,0-15.15-6.78-15.15-15.15V38.3c0-8.37,6.78-15.15,15.15-15.15h227.06
		c8.37,0,15.15,6.78,15.15,15.15v117.45C273.4,164.11,266.62,170.89,258.26,170.89z"/>
	<path class="st2" d="M253.23,162.21H36.21c-7.57,0-13.7-6.13-13.7-13.7V45.53c0-7.57,6.13-13.7,13.7-13.7h217.02
		c7.57,0,13.7,6.13,13.7,13.7v102.98C266.94,156.08,260.8,162.21,253.23,162.21z"/>
	<circle class="st1" cx="144.72" cy="217.66" r="10.98"/>
	<g>
		<path class="st3" d="M152.04,221.09c1.73-3.68,0.45-8.15-3.1-10.33c-3.55-2.17-8.11-1.28-10.61,1.94L152.04,221.09z"/>
		<path class="st3" d="M137.33,214.41c-1.61,3.65-0.32,8.01,3.17,10.15c3.49,2.14,7.97,1.3,10.48-1.79L137.33,214.41z"/>
	</g>
	<rect x="52.81" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="59.28" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="65.57" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="72.04" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="78.51" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="84.81" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="200.89" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="207.36" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="213.66" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="220.13" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="226.6" y="170.89" class="st1" width="3.06" height="84.94"/>
	<rect x="232.89" y="170.89" class="st1" width="3.06" height="84.94"/>
	<polygon class="st1" points="145.12,187.19 145.12,202.21 156.85,194.7 	"/>
	<polygon class="st1" points="143.91,187.19 143.91,202.21 132.59,194.7 	"/>
	<path class="st4" d="M57.87,119.58L57.87,119.58c-2.15-2.06-2.16-5.58-0.02-7.65c11.05-10.65,44.65-38.92,89.39-38.25
		c44.25,0.68,76.05,26.25,86.79,36.23c2.19,2.03,2.22,5.56,0.1,7.66l-0.01,0.01c-1.9,1.87-4.87,1.94-6.84,0.14
		c-9.72-8.91-39.68-32.98-80.19-33.6c-40.86-0.63-72.36,25.92-82.35,35.48C62.8,121.45,59.8,121.43,57.87,119.58z"/>
	<path class="st5" d="M43.53,100.38c0,0,38.3-44.6,104-44.26c0,0,60.6-0.33,99.06,41.2"/>
	<g>
		<path class="st1" d="M39.14,95.47c1.48,1.8,3.12,3.43,4.81,5.02c1.7,1.57,3.43,3.1,5.32,4.47l-0.51,0.55
			c-1.49-1.79-3.13-3.43-4.81-5.02c-1.69-1.58-3.43-3.11-5.32-4.47L39.14,95.47z"/>
	</g>
	<line class="st5" x1="43.53" y1="91.66" x2="47.6" y2="96.16"/>
	<line class="st5" x1="51.15" y1="92.87" x2="54.89" y2="97.15"/>
	<line class="st5" x1="55.53" y1="89.12" x2="51.7" y2="84.76"/>
	<line class="st5" x1="57.06" y1="80.25" x2="65.48" y2="91.15"/>
	<line class="st5" x1="62.97" y1="76.64" x2="65.97" y2="81.33"/>
	<line class="st5" x1="69.91" y1="78.74" x2="73.18" y2="83.45"/>
	<line class="st5" x1="70.29" y1="71.96" x2="73.32" y2="76.64"/>
	<line class="st5" x1="75.53" y1="65.91" x2="82.16" y2="77.91"/>
	<line class="st5" x1="83.74" y1="65.02" x2="86.08" y2="69.82"/>
	<line class="st5" x1="90.38" y1="67.87" x2="92.72" y2="73.06"/>
	<line class="st5" x1="92.25" y1="61.57" x2="94.24" y2="66.26"/>
	<line class="st5" x1="97.57" y1="57.66" x2="102.42" y2="70.68"/>
	<line class="st5" x1="105.36" y1="56.81" x2="106.92" y2="61.86"/>
	<line class="st5" x1="110.3" y1="60.91" x2="111.91" y2="66.68"/>
	<line class="st5" x1="114.8" y1="54.34" x2="116.12" y2="59.48"/>
	<line class="st5" x1="121.27" y1="51.45" x2="123.61" y2="65.02"/>
	<line class="st5" x1="128.16" y1="52.04" x2="128.97" y2="57.24"/>
	<line class="st5" x1="133.74" y1="56.91" x2="134.16" y2="62.55"/>
	<line class="st5" x1="138.08" y1="51.02" x2="138.29" y2="56.12"/>
	<line class="st5" x1="145.7" y1="49.15" x2="145.7" y2="63.1"/>
	<line class="st5" x1="151.36" y1="50.81" x2="151.14" y2="56.12"/>
	<line class="st5" x1="155.31" y1="56.52" x2="155.31" y2="61.66"/>
	<line class="st5" x1="162.5" y1="51.74" x2="161.69" y2="57.18"/>
	<line class="st5" x1="168.97" y1="51.23" x2="166.97" y2="64.47"/>
	<line class="st5" x1="175.91" y1="53.74" x2="174.76" y2="59.34"/>
	<line class="st5" x1="178.7" y1="60.2" x2="177.61" y2="65.32"/>
	<line class="st5" x1="183.76" y1="61.44" x2="185.44" y2="56.12"/>
	<line class="st5" x1="187.91" y1="69.06" x2="191.74" y2="56.12"/>
	<line class="st5" x1="196.12" y1="65.24" x2="198.16" y2="60.2"/>
	<line class="st5" x1="199.79" y1="66.58" x2="197.82" y2="71.57"/>
	<line class="st5" x1="204.86" y1="68.63" x2="207.06" y2="63.79"/>
	<line class="st5" x1="207.48" y1="77.06" x2="213.31" y2="64.98"/>
	<line class="st5" x1="216.21" y1="74.07" x2="218.72" y2="69.4"/>
	<line class="st5" x1="217.46" y1="81.49" x2="220.54" y2="76.51"/>
	<line class="st5" x1="224.81" y1="79.14" x2="227.61" y2="74.76"/>
	<line class="st5" x1="226.21" y1="88.38" x2="233.95" y2="77.53"/>
	<line class="st5" x1="235.61" y1="87" x2="238.93" y2="83.19"/>
	<line class="st5" x1="234.93" y1="94" x2="238.54" y2="89.49"/>
	<line class="st5" x1="242.44" y1="93.08" x2="246.16" y2="89.27"/>
	<line class="st5" x1="242.44" y1="101.96" x2="251.61" y2="92.3"/>
	<path class="st5" d="M147.78,52.04"/>
	<path class="st5" d="M33.49,93.91l1.6-1.35c0,0-0.35,2.43,1.79,4.24"/>
	<path class="st5" d="M37.74,89.69L36.62,91l0.86,0.89c0,0,1.34-1.97,2.65-0.74s-0.45,2.76-0.45,2.76"/>
	<path class="st5" d="M52.48,76.64c0,0-1.54-0.25-1.33,1.62c0.21,1.86,2.06,2.44,2.06,2.44s1.98,0.26,1.37-1.95
		c0,0-1.47-1.44-2.59,0.7"/>
	<path class="st5" d="M55.39,74.3c0,0-1.31,1.1-0.29,2.34c1.02,1.24,1.18,1.53,2.46,1.44c1.28-0.1,0.57-1.88,0.57-1.88
		s-1.11-2.06-2.01-1.9H55.39z"/>
	<polyline class="st5" points="73.04,63.89 71.46,64.86 71.68,61.48 73.72,65.02 	"/>
	<path class="st5" d="M74.93,59.31l-1.52,0.97l0.69,1.2c0,0,1.66-1.45,2.47-0.27c0.81,1.18,0.35,1.96-0.67,2.44"/>
	<path class="st5" d="M92.25,53.42l1.74-0.72c0,0,0.17,1.57-0.6,1.96c0,0,1.55-1.09,2.19,0.7c0.64,1.79-1.32,2.09-1.87,1.7"/>
	<path class="st5" d="M96.91,51.7c0,0-0.96,0.28-0.79,1.17c0.17,0.89,0.94,2.32,0.94,2.32s0.26,0.55,1.36,0.43s0.85-1.38,0.85-1.38
		l-0.94-2.32C98.33,51.91,97.97,51.36,96.91,51.7z"/>
	<polyline class="st5" points="117.37,47.2 118.07,46.08 118.95,50.07 	"/>
	<path class="st5" d="M120.73,49.59c0,0-0.29,0.02,0.54,0c0.82-0.02,2.06-0.85,1.41-2.17c-0.65-1.32-2.6-0.21-2.6-0.21l-0.46-1.63
		l2.01-0.45"/>
	<path class="st5" d="M145.16,42.5c0,0-1.07-0.13-1.1,0.69c-0.02,0.82-0.09,2.79-0.09,2.79s0.04,0.78,0.86,0.87s1.32-0.16,1.37-0.7
		s0.09-2.93,0.09-2.93S146.34,42.51,145.16,42.5z"/>
	<polyline class="st5" points="167.36,45.81 168.5,45.17 167.72,49.34 	"/>
	<path class="st5" d="M172.01,45.42l-2.11-0.26l-0.26,1.38c0,0,2.45-0.15,2.23,1.36c-0.21,1.51-1.13,1.83-2.53,1.43"/>
	<path class="st5" d="M190.29,49.4l1.53,0.65c0,0-1.02,0.94-1.53,0.89c-0.51-0.05,2.12,0.83,0.99,2.17
		c-1.13,1.34-2.27,0.34-2.43,0.26"/>
	<path class="st5" d="M194.93,50.8c0,0-1.04-0.13-1.36,0.43c-0.32,0.56-0.81,2.25-0.81,2.25s-0.38,0.86,0.62,1.44
		c1.01,0.57,1.6-0.24,1.64-0.62c0.05-0.38,0.83-2.33,0.83-2.33S195.88,51.3,194.93,50.8z"/>
	<polyline class="st5" points="213.31,62.08 211.65,61.23 214.65,59.76 212.74,63.23 	"/>
	<path class="st5" d="M218.18,60.83L216.44,60l-0.64,1.5c0,0,1.79,0.78,1.32,1.9c-0.47,1.13-1.62,1.19-2.57,0.53"/>
	<path class="st5" d="M236.03,72.04c0,0-0.64-1.37-1.84-0.85s-2.04,2.55-2.04,2.55s0.19,1.26,1.47,1.2
		c1.28-0.06,1.44-0.97,0.94-1.53s-1.37-1.18-1.37-1.18"/>
	<path class="st5" d="M238.82,74.07c0,0-0.75-0.75-1.72,0s-1.5,1.88-1.23,2.53c0.27,0.65,0.59,0.83,1.18,0.8s1.61-0.67,2.06-1.63
		C239.55,74.82,238.82,74.07,238.82,74.07z"/>
	<path class="st5" d="M253.29,86.36l1.51,1.51c0,0-2.26-0.21-4.06,1.72"/>
	<path class="st5" d="M257.65,90.38l-1.38-1.11l-0.94,0.83c0,0,1.96,1.09,0.91,2.64c-1.04,1.55-2.81-0.34-2.98-0.45"/>
	<path class="st5" d="M50.97,108.51l-1.68,1.7l1.43,1.26c0,0,0.06-2.19,2.09-1.38c2.02,0.81,0.51,2.66,0,2.74"/>
	<path class="st5" d="M52.93,106.34c0,0-0.64,0.87,0,1.62c0.64,0.74,1.62,1.57,1.62,1.57s0.87,0.4,1.4,0
		c0.53-0.4,0.79-1.3,0.38-1.68s-1.74-1.68-1.74-1.68S53.78,105.47,52.93,106.34z"/>
	<path class="st5" d="M68.97,97.59c-0.06,0.03-1.68,1.24-1.68,1.24l-0.27-3.88l2.68,3.54"/>
	<path class="st5" d="M69.25,92.96c0,0-0.96,0.24-0.29,1.45s1.58,2.03,1.58,2.03s1.13,0.41,1.52,0s0.91-1.04,0.56-1.8
		c-0.35-0.77-1.72-1.95-1.72-1.95S70.05,92.27,69.25,92.96z"/>
	<path class="st5" d="M82.55,83.74l1.77-1c0,0-0.09,1.81-0.51,2.09c0,0,1.68-1.04,2.23,0.19s-0.19,2.32-1.57,1.96"/>
	<path class="st5" d="M86.93,81.25c0,0-0.74,0.26-0.53,1.11c0.21,0.85,1.21,2.36,1.21,2.36s0.68,0.66,1.4,0.3s1.06-0.79,0.74-1.57
		c-0.32-0.79-1.17-2.35-1.17-2.35S87.61,80.53,86.93,81.25z"/>
	<path class="st5" d="M101.38,75.23c0,0,0.73-1.72,2.23-0.61c0,0,0.89,0.99-0.77,2.17c-1.66,1.18-0.86,2.36-0.86,2.36l2.23-0.91"/>
	<path class="st5" d="M105.75,72.93c0,0-0.86,0.1-0.86,0.89s0.86,2.46,0.86,2.46s0.29,0.7,1.24,0.64c0.96-0.06,1.21-0.64,0.99-1.37
		c-0.22-0.73-0.86-2.23-0.86-2.23S106.67,72.77,105.75,72.93z"/>
	<polyline class="st5" points="122.01,70.14 122.74,68.83 123.45,73.11 	"/>
	<path class="st5" d="M125.5,67.7c0,0-0.54-0.13-0.91,0.34c-0.37,0.46,0.37,3.59,0.37,3.59s0.32,0.83,1.18,0.72s1.34-0.67,1.23-1.37
		c-0.11-0.7-0.49-2.65-0.49-2.65S126.57,67.38,125.5,67.7z"/>
	<path class="st5" d="M146.59,67.02c0,0-0.87-0.43-1.13,0.89c-0.26,1.32-0.15,2.36-0.15,2.36s0.26,1.04,1,1.17
		c0.74,0.13,1.28-0.3,1.23-0.87s0-2.96,0-2.96S147.36,66.9,146.59,67.02z"/>
	<polyline class="st5" points="163.95,69.66 165.44,68.72 164.55,72.7 	"/>
	<path class="st5" d="M168.33,68.72c0,0-1.32-0.3-1.66,1.7s-0.34,2-0.34,2s-0.04,0.64,0.74,0.91c0.79,0.28,1.38-0.13,1.68-0.87
		c0.3-0.74,0.6-2.74,0.6-2.74S169.14,68.98,168.33,68.72z"/>
	<path class="st5" d="M183.14,72.7c0,0,0.7-1.07,1.82-0.66s0.26,1.91,0.26,1.91l-3.57,1.72l2.74,0.96"/>
	<path class="st5" d="M188.46,73.3c0,0-1-0.36-1.55,0.83s-0.85,2.02-0.85,2.02s-0.57,0.81,0.64,1.34c1.21,0.53,1.62,0.04,1.77-0.51
		c0.15-0.55,0.83-2.23,0.83-2.23S189.48,73.72,188.46,73.3z"/>
	<path class="st5" d="M202.12,79.98l1.89,1.02c0,0-1.53,0.94-2.34,0.79c0,0,2.28,0.62,1.66,1.98s-1.96,1.11-2.7,0"/>
	<path class="st5" d="M206.8,82.21c0,0-0.91-0.51-1.68,0.79s-1.32,1.98-0.55,2.81s1.79,0.11,2.04-0.23s1.11-1.91,1.11-1.91
		S208.01,82.59,206.8,82.21z"/>
	<polyline class="st5" points="220.42,94.55 222.76,91.13 219.36,92.49 220.84,93.66 	"/>
	<path class="st5" d="M222.91,96.23c0,0-0.94-0.87,0.26-2.4c1.19-1.53,1.94-1.28,2.32-0.99c0.38,0.29,1.26,1.12-0.11,2.56
		C224.01,96.85,223.91,96.68,222.91,96.23z"/>
	<path class="st5" d="M238.27,103.85l-1.53-1.51l-1.04,1.38c0,0,2.23,0.45,1.15,2.06c-1.09,1.62-2.81-0.15-2.81-0.15"/>
	<path class="st5" d="M237.4,109c0,0-0.8-0.93-0.16-1.53c0.64-0.61,1.96-1.98,1.96-1.98s0.69-0.54,1.5,0.45s-0.43,2.07-0.43,2.07
		l-1.68,1.26C238.59,109.27,237.97,109.51,237.4,109z"/>
	<rect x="147.28" y="-0.05" class="st1" width="3.06" height="23.2"/>
	<rect id="_x3C_Фрагмент_x3E_" x="125.3" y="-68.06" class="st6" width="40" height="67"/>
	<rect x="153.74" y="-0.05" class="st1" width="3.06" height="23.2"/>
	<rect x="160.04" y="-0.05" class="st1" width="3.06" height="23.2"/>
	<rect x="134.51" y="-0.05" class="st1" width="3.06" height="23.2"/>
	<rect x="128.04" y="-0.05" class="st1" width="3.06" height="23.2"/>
	<rect x="140.81" y="-0.05" class="st1" width="3.06" height="23.2"/>
	<circle class="st7" cx="29.08" cy="117.9" r="1.65"/>
	<circle class="st7" cx="29.08" cy="73.24" r="1.65"/>
	<circle class="st7" cx="260.96" cy="116.88" r="1.65"/>
	<circle class="st7" cx="260.96" cy="72.23" r="1.65"/>
</g>
<g id="Слой_3">
	<g>
	</g>
	<path class="st8" d="M224.56,143.65v-7.83c0-1.94,1.59-3.52,3.53-3.52c0.96,0,1.84,0.39,2.48,1.03c0.64,0.64,1.04,1.52,1.04,2.49
		v7.83"/>
	<line class="st8" x1="226.52" y1="143.48" x2="229.65" y2="143.48"/>
	<polyline class="st9" points="233.96,144.2 233.96,139.18 243.94,139.18 243.94,144.2 	"/>
	<text transform="matrix(1 0 0 1 236.5729 137.092)" class="st10 st11 st12">Б</text>
	<g>
		<text transform="matrix(0.6385 0 0 1 245.763 144.201)" class="st10 st11 st12">3,75 mA</text>
	</g>
	<polygon class="st9" points="243.7,145.43 245.93,149.96 250.93,150.68 247.31,154.21 248.16,159.18 243.7,156.84 239.23,159.18 
		240.08,154.21 236.47,150.68 241.46,149.96 	"/>
	<text transform="matrix(1 0 0 1 242.3976 155.3208)" class="st10 st11 st13">2</text>
	<text transform="matrix(0.6598 0 0 1 229.9898 158.7698)" class="st10 st11 st13">1,0</text>
	<line class="st9" x1="214.39" y1="137.61" x2="221.89" y2="137.61"/>
	<text transform="matrix(0.7658 0 0 1 27.4259 144.6449)" class="st14 st11 st12"> </text>
	<text transform="matrix(0.7658 0 0 1 130.7676 155.3206)" class="st14 st11 st15">ГОСТ 8711-60</text>
	<text transform="matrix(0.7658 0 0 1 128.2399 146.3569)" class="st14 st11 st16">нш 75mV кп</text>
	<text transform="matrix(0.7658 0 0 1 30.95 146.3571)" class="st14 st11 st12">М145М</text>
	<text transform="matrix(0.7658 0 0 1 33.5782 153.2212)" class="st14 st11 st12">1975</text>
	<text transform="matrix(0.7658 0 0 1 30.7293 159.185)" class="st14 st11 st12">050455</text>
</g>
<g transform="rotate({} 145.67 162.26)">
	<g id="Стрелка">
		<line class="st17" x1="145.67" y1="162.26" x2="145.67" y2="76.84"/>
		<circle class="st18" cx="145.67" cy="103.45" r="4.42"/>
		<polygon class="st18" points="145.43,65.32 150.09,84.14 141.25,84.14 	"/>
	</g>
</g>
</svg>
"""
        self.svg_widget = self.create_widget_galvanometer()
        self.value_galvanometer = 0
        self.value_angle_now = 0

    def create_widget_galvanometer(self):
        """
        Создаёт свг_виджет, устанавливает стрелку прибора на 0 градусов,
        тобишь на 0 вольт
        :return: готовый к интеграции виджет
        """
        svg_widget = QSvgWidget()
        svg_bytes = bytearray(self.svg_str.format('0'), encoding='utf-8')
        svg_widget.renderer().load(svg_bytes)
        return svg_widget

    def update_svg_galvanometer(self, value_galvanometer):
        """
        Обновляет показания прибора,путём изменения угла наклона стрелки прибора
        1 градус равен 0,862 деления гальванометра
        :param value_galvanometer: это то, какое значение нужно отобразить на приборе
        :return:
        """
        self.value_galvanometer = value_galvanometer

        angle = value_galvanometer / 0.862
        if value_galvanometer > 50:
            angle = 66
        elif value_galvanometer < -50:
            angle = -66
        svg_bytes = bytearray(self.svg_str.format(str(angle)), encoding='utf-8')
        self.svg_widget.renderer().load(svg_bytes)
        self.value_angle_now = angle

    def value(self):
        """
        :return: Возвращает текущее показание гальванометра
        """
        return self.value_galvanometer
