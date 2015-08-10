import Tkinter as tk


class App:
	def __init__(self, master):
		self.master = master
		version = ' Version 1.60'
		master.title('The Inside Sales Buddy' + version)
		
		master.grid()
		self.Master_Label = 'Verdana 12 bold'
		self.Output_Label = 'Verdana 10 bold'
		self.Two = 2
		Black = 'black'
		
		
		# Frames
		b_frame = tk.Frame(master)
		b_frame.grid(row = 0, column = 0)
		l_frame = tk.Frame(master)
		l_frame.grid(row = 1, column = 0)
		s_frame = tk.Frame(master)
		s_frame.grid(row = 0, column = 3)
		sf_to_lf_frame = tk.Frame(master)
		sf_to_lf_frame.grid(row = 1, column = 3)
		lf_to_sf_frame = tk.Frame(master)
		lf_to_sf_frame.grid(row = 2, column = 3)
		
		# Frame Borders -----------------------------------------------------------------
		#b_frame.configure(highlightbackground = Black, borderwidth = self.Two, highlightcolor = Black, highlightthickness = self.Two)
		#l_frame.configure(highlightbackground = Black, borderwidth = self.Two, highlightcolor = Black, highlightthickness = self.Two)
		#s_frame.configure(highlightbackground = Black, borderwidth = self.Two, highlightcolor = Black, highlightthickness = self.Two)
		#sf_to_lf_frame.configure(highlightbackground = Black, borderwidth = self.Two, highlightcolor = Black, highlightthickness = self.Two)
		#lf_to_sf_frame.configure(highlightbackground = Black, borderwidth = self.Two, highlightcolor = Black, highlightthickness = self.Two)
		#b_frame.configure(highlightbackground = Black, borderwidth = self.Two, highlightcolor = Black, highlightthickness = self.Two)
		
		
		# Board > Lineal: ----------------------------------------------------------------
		b_label = tk.Label(b_frame, text = 'Board Feet to Lineal Feet', font = self.Master_Label)
		b_label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
		
		# Label bft, thick, width
		a = tk.Label(b_frame, text = 'Total Board Feet:')
		b = tk.Label(b_frame, text = 'Thickness:')
		c = tk.Label(b_frame, text = 'Width:')
		a.grid(row = 1, column = 0, padx = 7)
		b.grid(row = 2, column = 0, padx = 7)
		c.grid(row = 3, column = 0, padx = 7)
		
		# Entry bft, thick, width
		self.ae1 = tk.Entry(b_frame)
		self.be1 = tk.Entry(b_frame)
		self.ce1 = tk.Entry(b_frame)
		self.ae1.grid(row = 1, column = 1, padx = 7)
		self.be1.grid(row = 2, column = 1, padx = 7)
		self.ce1.grid(row = 3, column = 1, padx = 7)
		
		
		# Lineal > Board: ----------------------------------------------------------------		
		l_label = tk.Label(l_frame, text = 'Lineal Feet to Board Feet', font = self.Master_Label)
		l_label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
		
		# Label lft, thick, width
		a = tk.Label(l_frame, text = 'Total Lineal Feet:')
		b = tk.Label(l_frame, text = 'Thickness:')
		c = tk.Label(l_frame, text = 'Width')
		a.grid(row = 1, column = 0, padx = 7)
		b.grid(row = 2, column = 0, padx = 7)
		c.grid(row = 3, column = 0, padx = 7)
				
		# Entry lft, thick, width
		self.ae2 = tk.Entry(l_frame)
		self.be2 = tk.Entry(l_frame)
		self.ce2 = tk.Entry(l_frame)
		self.ae2.grid(row = 1, column = 1, padx = 7)
		self.be2.grid(row = 2, column = 1, padx = 7)
		self.ce2.grid(row = 3, column = 1, padx = 7)
		
		
		# Sonotube: -------------------------------------------------------------------
		s_label = tk.Label(s_frame, text = 'Sonotube Concrete Calc', font = self.Master_Label)
		s_label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
		
		self.diam = tk.Label(s_frame, text = 'Tube Diameter(inches):')
		self.dept = tk.Label(s_frame, text = 'Hole Depth / Tube Length(inches):')
		self.quan = tk.Label(s_frame, text = 'Number of Holes / Tubes:')
		self.diam.grid(row = 1, column = 0, padx = 7)
		self.dept.grid(row = 2, column = 0, padx = 7)
		self.quan.grid(row = 3, column = 0, padx = 7)
		self.diame = tk.Entry(s_frame)
		self.depte = tk.Entry(s_frame)
		self.quane = tk.Entry(s_frame)
		self.diame.grid(row = 1, column = 1, padx = 7)
		self.depte.grid(row = 2, column = 1, padx = 7)
		self.quane.grid(row = 3, column = 1, padx = 7)
		
		
		# Square > Lineal: ------------------------------------------------------------
		square_lineal = tk.Label(sf_to_lf_frame, text = 'Square Feet to Lineal Feet', font = self.Master_Label)
		square_lineal.grid(row = 0, columnspan = 2)
		sf_fill = tk.Label(sf_to_lf_frame, text = 'Total Square Feet:')
		sf_fill.grid(row = 1, column = 0, padx = 7)
		expl_fill = tk.Label(sf_to_lf_frame, text = 'Exposure (inches):')
		expl_fill.grid(row = 2, column = 0, padx = 7)
		self.sf_fill_entry = tk.Entry(sf_to_lf_frame)
		self.expl_fill_entry = tk.Entry(sf_to_lf_frame)
		self.sf_fill_entry.grid(row = 1, column = 1)
		self.expl_fill_entry.grid(row = 2, column = 1)
		

		
		# Lineal > Square: -------------------------------------------------------------
		lineal_square = tk.Label(lf_to_sf_frame, text = 'Lineal Feet to Square Feet', font = self.Master_Label)
		lineal_square.grid(row = 0, columnspan = 2)
		lf_fill = tk.Label(lf_to_sf_frame, text = 'Total Lineal Feet:')
		lf_fill.grid(row = 1, column = 0, padx = 7)
		exp2_fill = tk.Label(lf_to_sf_frame, text = 'Exposure (inches):')
		exp2_fill.grid(row = 2, column = 0, padx = 7)
		self.lf_fill_entry = tk.Entry(lf_to_sf_frame)
		self.exp2_entry = tk.Entry(lf_to_sf_frame)
		self.lf_fill_entry.grid(row = 1, column = 1, padx = 7)
		self.exp2_entry.grid(row = 2, column = 1, padx = 7)
		

		
		# Dynamic Labels: -------------------------------------------------------------
		# Board > Lineal
		self.boutput = tk.Label(b_frame, text = 'Lineal Feet', font = self.Output_Label)
		self.boutput.grid(row = 4, columnspan = 2, pady = 5, padx = 10)
		
		# Lineal > Board
		self.loutput = tk.Label(l_frame, text = 'Board Feet', font = self.Output_Label)
		self.loutput.grid(row = 4, columnspan = 2, pady = 5, padx = 10)
		
		# SonoTube
		self.soutput = tk.Label(s_frame, text = '80# bags of concrete', font = self.Output_Label)
		self.soutput.grid(row = 4, columnspan = 2, padx = 10, pady = 5)
		
		# Square Feet to Lineal Feet
		self.sqr_to_lineal_output = tk.Label(sf_to_lf_frame, text = 'Lineal Feet', font = self.Output_Label)
		self.sqr_to_lineal_output.grid(row = 3, columnspan = 2, padx = 7, pady = 5)
		
		# Lineal Feet to Square Feet
		self.lin_to_sqr_output = tk.Label(lf_to_sf_frame, text = 'Square Feet', font = self.Output_Label)
		self.lin_to_sqr_output.grid(row = 10, columnspan = 2, padx = 7, pady = 5)
		
		
		
		# Buttons: --------------------------------------------------------------------
		# Button Board
		b_button = tk.IntVar()
		b_button = tk.Button(b_frame, text = 'Convert', command = self.bconvert)
		b_button.grid(row = 5, columnspan = 2, pady = 2, padx = 10)
		
		# Button Lineal
		l_button = tk.IntVar()
		l_button = tk.Button(l_frame, text = 'Convert', command = self.lconvert)
		l_button.grid(row = 5, columnspan = 2, pady = 2, padx = 10)
		
		# Button Quit
		#Quit = tk.Button(master, text = 'Quit', command = self.quit)
		#Quit.grid(row = 3, columnspan = 4, padx = 10, pady = 20)
		
		# Button Sono
		s_button = tk.IntVar()
		s_button = tk.Button(s_frame, text = 'Calculate', command = self.sconvert)
		s_button.grid(row = 5, columnspan = 2, pady = 2, padx = 10)
		
		# sf to lf button
		sq_button_1 = tk.IntVar()
		sq_button_1 = tk.Button(sf_to_lf_frame, text = 'Calculate', command = self.sft_to_lft)
		sq_button_1.grid(row = 4, columnspan = 2, pady = 2, padx = 10)
		
		# lf to sf button
		sq_button_2 = tk.IntVar()
		sq_button_2 = tk.Button(lf_to_sf_frame, text = 'Calculate', command = self.lft_to_sft)
		sq_button_2.grid(row = 9, columnspan = 2, pady = 2, padx = 10)
		
		
		# Credits
		credit = tk.Label(master, text = 'Created by Chris Nicholson' + version, font = 'Verdana 10 italic')
		credit.grid(columnspan = 4)
		
		
	# Function Calls: ------------------------------------------------------------------
	# Board > Lineal
	def bconvert(self):
		a = float(self.ae1.get())
		b = int(self.be1.get())
		c = int(self.ce1.get())
		result = int(((a * 12)/b)/c), 'Lineal Feet'
		self.boutput.configure(text = result)
			
	# Lineal > Board
	def lconvert(self):
		a = int(self.ae2.get())
		b = int(self.be2.get())
		c = int(self.ce2.get())
		result = float((a * b * c)/12.0), 'Board Feet'
		self.loutput.configure(text = result)
	
	# Sonotube
	def sconvert(self):
		d = int(self.diame.get())
		de = int(self.depte.get())
		q = int(self.quane.get())
		e = int(d/2)
		result = int((((((e * e)*3.14)*de)/1728)/.6)*q), '80# bags of concrete required'
		self.soutput.configure(text = result)
		
	# Sft > Lft
	def sft_to_lft(self):
		a = int(self.sf_fill_entry.get())
		b = float(self.expl_fill_entry.get())
		result = int((a * 12 )/b), 'Lineal Feet of material'
		self.sqr_to_lineal_output.configure(text = result)
		
	# Lft > Sft
	def lft_to_sft(self):
		a = int(self.lf_fill_entry.get())
		b = float(self.exp2_entry.get())
		result = int((a * b)/12), 'Square Feet of material'
		self.lin_to_sqr_output.configure(text = result)
		
		





		
root = tk.Tk()
root.resizable(0,0)
App(root)
root.mainloop()
