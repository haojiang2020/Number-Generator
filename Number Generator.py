# Number Generator
# version 0.1.0

import os
from platform import system
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter.messagebox import askyesno
from random import uniform
from random import seed


class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.current_version = "0.1.0"
        self.init_win_width = 1120
        self.init_win_height = 630  
        self.sub_win_width = 800
        self.sub_win_height = 600  
        self.title_name = "Number Generator"
        self.geometry(f"{self.init_win_width}x{self.init_win_height}+0+0")
        self.resizable(False, False)
        self.title(self.title_name)
        self.version = (0, 1, 0)
        temp_str_0 = system()
        if not os.path.exists("assets"):
            os.mkdir("assets")
        if temp_str_0 == "Windows":
            if os.path.exists("assets/NumGene.ico"):
                self.iconbitmap("assets/NumGene.ico")
        elif temp_str_0 == "Darwin":
            if os.path.exists("assets/NumGene.icns"):
                self.iconbitmap("assets/NumGene.icns")
        self.dat_file_sep = ";"+"\u0009"+"\u000a"
        self.dat_file_read_sep = ";"+"\u0009"
        self.dat_file_sub_sep = ","+"\u0009" 
        self.fonsize_s = (None, 14)
        self.fonsize_s_b = (None, 14, "bold")
        self.fonsize_m = (None, 18)
        self.fonsize_m_b = (None, 18, "bold")
        self.fonsize_l = (None, 22)
        self.fonsize_l_b = (None, 22, "bold")
        self.org_name_max_len = 140
        self.virtual_type = ("None", "Name in other language", 
                             "Social media APP",                              
                             "Other")
        self.English_name_capital = ("A", "B", "C", "D", "E", "F", "G", 
                                     "H", "I", "J", "K", "L", "M", "N", 
                                     "O", "P", "Q", "R", "S", "T", 
                                     "U", "V", "W", "X", "Y", "Z")
        self.numeric_digits = ("0", "1", "2", "3", "4", 
                               "5", "6", "7", "8", "9")
        self.numeric_hex_digits = ("0", "1", "2", "3", "4", 
                                   "5", "6", "7", "8", "9", 
                                   "A", "B", "C", "D", "E", "F")
        self.English_name_other = (" ", "-", "'")
        self.English_name_other_1 = (" ", "-", "'", "‘", "’", "&", 
                                     "/", ".", ":", "(", ")")
        self.regions_vec = ("nam - Northern America", 
                            "cam - Central America", 
                            "car - Caribbean", 
                            "sam - South America", 
                            "weu - Western Europe", 
                            "seu - Southern Europe", 
                            "neu - Northern Europe", 
                            "eeu - Eastern Europe", 
                            "naf - North Africa", 
                            "eaf - East Africa", 
                            "maf - Middle Africa", 
                            "saf - Southern Africa", 
                            "waf - West Africa",
                            "eas - East Asia", 
                            "sea - Southeast Asia", 
                            "nas - North Asia / Siberia", 
                            "cas - Central Asia", 
                            "sas - South Asia", 
                            "me - Western Asia / Middle East", 
                            "omi - Micronesia", 
                            "ome - Melanesia", 
                            "opo - Polynesia", 
                            "oau - Australasia", 
                            "int - Internation", 
                            "other - Other")
        self.regions_short_vec = []
        for n in range(len(self.regions_vec)):
            temp_list = self.regions_vec[n].split(" - ")
            self.regions_short_vec.append(temp_list[0].strip())
        self.preread()
        self.main_win() 
        self.generate_page() 
        self.check_validity_page()
        self.output_csv_page()
        self.setting_page()
        self.other_page()
        self.main_switch_page("setting")
    
    def main_win(self):
        main_upper_frame = tk.Frame(self)
        main_upper_frame.grid(row = 0, column = 0,
                              padx = 5, pady = 5, 
                              sticky = tk.W)
        self.login_state = False
        self.cur_sel_page = ""
        ttk.Separator(main_upper_frame, 
                      orient="horizontal").grid(row = 1, column = 0, 
                                                columnspan = 5, 
                                                sticky = tk.EW)
        main_upper_fun_frame = tk.Frame(main_upper_frame)
        main_upper_fun_frame.grid(row = 0, column = 0,
                                  padx = 2, pady = 2, 
                                  sticky = tk.W)        
        main_upper_fun_frame_line_0 = tk.Frame(main_upper_fun_frame)
        main_upper_fun_frame_line_0.grid(row = 0, column = 0,
                                         sticky = tk.W)
        main_upper_fun_frame_line_1 = tk.Frame(main_upper_fun_frame)
        main_upper_fun_frame_line_1.grid(row = 1, column = 0,
                                         sticky = tk.W)
        self.generate_num_page_button = tk.Button(main_upper_fun_frame_line_0, 
                                                  text = "Generate numbers", 
                                                  width = 18, 
                                                  font = self.fonsize_l)
        self.generate_num_page_button.grid(row = 0, column = 0,
                                           padx = 2, pady = 2,
                                           sticky = tk.W)
        self.generate_num_page_frame = tk.Frame(self)
        self.generate_num_page_frame.grid_forget()
        self.check_validity_page_button = tk.Button(main_upper_fun_frame_line_1, 
                                                    text = "Check validity", 
                                                    width = 16, 
                                                    font = self.fonsize_l)
        self.check_validity_page_button.grid(row = 0, column = 0,
                                             padx = 2, pady = 2,
                                             sticky = tk.W)
        self.check_validity_page_frame = tk.Frame(self)
        self.check_validity_page_frame.grid_forget()
        self.output_csv_page_button = tk.Button(main_upper_fun_frame_line_1, 
                                                text = "Output *.csv", 
                                                width = 14, 
                                                font = self.fonsize_l)
        self.output_csv_page_button.grid(row = 0, column = 1,
                                         padx = 2, pady = 2,
                                         sticky = tk.W)
        self.output_csv_page_frame = tk.Frame(self)
        self.output_csv_page_frame.grid_forget()
        ttk.Separator(main_upper_frame, 
                      orient="vertical").grid(row = 0, column = 1, 
                                              sticky = tk.NS)
        main_upper_set_frame = tk.Frame(main_upper_frame)
        main_upper_set_frame.grid(row = 0, column = 2,
                                  padx = 2, pady = 2, 
                                  sticky = tk.W) 
        self.setting_page_button = tk.Button(main_upper_set_frame, 
                                             text = "Setting", 
                                             width = 9, 
                                             font = self.fonsize_l)
        self.setting_page_button.grid(row = 0, column = 0,
                                      padx = 2, pady = 2,
                                      sticky = tk.W)
        self.setting_page_frame = tk.Frame(self)
        self.setting_page_frame.grid_forget() 
        self.other_page_button = tk.Button(main_upper_set_frame, 
                                           text = "other", 
                                           width = 9, 
                                           font = self.fonsize_l)
        self.other_page_button.grid(row = 1, column = 0,
                                    padx = 2, pady = 2,
                                    sticky = tk.W)
        self.other_page_frame = tk.Frame(self)
        self.other_page_frame.grid(row = 1, column = 0,
                                   padx = 5, pady = 5,
                                   sticky = tk.W)
        ttk.Separator(main_upper_frame, 
                      orient="vertical").grid(row = 0, column = 3, 
                                              sticky = tk.NS)
        self.org_num_frame = tk.Frame(main_upper_frame)
        self.org_num_frame.grid(row = 0, column = 4,
                                padx = 5, pady = 5, 
                                sticky = tk.W)
        self.label_org_num_is = ttk.Label(self.org_num_frame, 
                                          text = "Organization number: ",                          
                                          font = self.fonsize_s)
        self.label_org_num_is.grid(row = 0, column = 0,
                                   sticky = tk.W)
        self.label_org_num = ttk.Label(self.org_num_frame, 
                                       text = "",                          
                                       font = self.fonsize_s)
        self.label_org_num.grid(row = 1, column = 0,
                                sticky = tk.E)
        self.label_mani_num_is = ttk.Label(self.org_num_frame, 
                                          text = "Manipulation number: ",                          
                                          font = self.fonsize_s)
        self.label_mani_num_is.grid(row = 2, column = 0,
                                    sticky = tk.W)
        self.label_mani_num = ttk.Label(self.org_num_frame, 
                                        text = "",                          
                                        font = self.fonsize_s)
        self.label_mani_num.grid(row = 3, column = 0,
                                 sticky = tk.E)
        self.sel_org = None
        self.cur_org = None
        self.cur_org_file_name = None
        self.cur_mani_num = None
        self.cur_progress_bool = False
        self.cur_multi_gene_bool = False
        ## command
        self.setting_page_button["command"] = lambda in_str = "setting": self.main_switch_page(in_str)
        self.other_page_button["command"] = lambda in_str = "other": self.main_switch_page(in_str)
        self.generate_num_page_button["command"] = lambda in_str = "generate_num": self.main_switch_page(in_str)
        self.check_validity_page_button["command"] = lambda in_str = "check_validity": self.main_switch_page(in_str)
        self.output_csv_page_button["command"] = lambda in_str = "output_csv": self.main_switch_page(in_str)
    
    def main_switch_page(self, in_str):
        if not self.cur_progress_bool:
            if self.cur_sel_page != in_str:    
                self.cur_sel_page = in_str
                if in_str == "setting":
                    self.setting_page_frame.grid(row = 1, column = 0,
                                                 padx = 5, pady = 5,
                                                 sticky = tk.W)
                    self.setting_page_button["font"] = self.fonsize_s_b
                    self.setting_page_mani_num_radio.select()
                    self.setting_fun_select()
                    self.other_page_frame.grid_forget() 
                    self.other_page_button["font"] = self.fonsize_s
                    self.generate_num_page_frame.grid_forget()
                    self.generate_num_page_button["font"] = self.fonsize_s
                    self.check_validity_page_frame.grid_forget()
                    self.check_validity_page_button["font"] = self.fonsize_s
                    self.output_csv_page_frame.grid_forget()
                    self.output_csv_page_button["font"] = self.fonsize_s
                elif in_str == "other":
                    self.setting_page_frame.grid_forget()
                    self.setting_page_button["font"] = self.fonsize_s
                    self.other_page_frame.grid(row = 1, column = 0,
                                               padx = 5, pady = 5,
                                               sticky = tk.W)
                    self.other_page_button["font"] = self.fonsize_s_b
                    self.other_page_scan_validity_radio.select()
                    self.other_fun_select()
                    self.generate_num_page_frame.grid_forget()
                    self.generate_num_page_button["font"] = self.fonsize_s
                    self.check_validity_page_frame.grid_forget()
                    self.check_validity_page_button["font"] = self.fonsize_s
                    self.output_csv_page_frame.grid_forget()
                    self.output_csv_page_button["font"] = self.fonsize_s
                elif self.login_state:
                    if in_str == "generate_num":
                        self.setting_page_frame.grid_forget()
                        self.setting_page_button["font"] = self.fonsize_s
                        self.other_page_frame.grid_forget()
                        self.other_page_button["font"] = self.fonsize_s
                        self.generate_num_page_frame.grid(row = 1, column = 0,
                                                          padx = 5, pady = 5,
                                                          sticky = tk.W)
                        self.generate_page_single_radio.select()                        
                        self.generate_fun_select()
                        self.gene_single_gn_entry.delete(0, "end")
                        self.gene_single_mn_entry.delete(0, "end")
                        self.gene_single_fn_entry.delete(0, "end")
                        self.gene_single_vt_combo.set("Other")
                        self.gene_single_vn_entry.delete(0, "end")
                        self.gene_single_va_entry.delete(0, "end")
                        self.cur_gene_import_csv_str_list = None
                        self.cur_gene_import_csv_title = None
                        self.gene_multiple_gene_state_0["text"] = "No *.csv file is imported. "
                        self.gene_multiple_gene_progressbar_0["value"] = 0
                        self.gene_multiple_gene_state_0_0["text"] = ""
                        self.gene_multiple_gene_state_0_1["text"] = ""                        
                        self.gene_multiple_gene_progressbar_1["value"] = 0
                        self.gene_multiple_gene_state_1_0["text"] = ""
                        self.gene_multiple_gene_state_1_1["text"] = ""                        
                        self.gene_multiple_gene_progressbar_2["value"] = 0
                        self.gene_multiple_gene_state_2_0["text"] = ""
                        self.gene_multiple_gene_state_2_1["text"] = ""                    
                        self.gene_multiple_gene_progressbar_3["value"] = 0
                        self.gene_multiple_gene_state_3_0["text"] = ""
                        self.gene_multiple_gene_state_3_1["text"] = ""
                        self.gene_multiple_gene_state_2["text"] = ""
                        self.generate_num_page_button["font"] = self.fonsize_s_b
                        self.check_validity_page_frame.grid_forget()
                        self.check_validity_page_button["font"] = self.fonsize_s
                        self.output_csv_page_frame.grid_forget()
                        self.output_csv_page_button["font"] = self.fonsize_s
                    elif in_str == "check_validity":
                        self.setting_page_frame.grid_forget()
                        self.setting_page_button["font"] = self.fonsize_s
                        self.other_page_frame.grid_forget()
                        self.other_page_button["font"] = self.fonsize_s
                        self.generate_num_page_frame.grid_forget()
                        self.generate_num_page_button["font"] = self.fonsize_s
                        self.check_validity_page_frame.grid(row = 1, column = 0,
                                                            padx = 5, pady = 5,
                                                            sticky = tk.W)
                        self.check_validity_page_button["font"] = self.fonsize_s_b
                        self.check_valid_page_mem_num_radio.select()
                        self.check_valid_fun_select()
                        self.check_valid_mix_num_main_entry.delete(0, "end")
                        self.check_valid_mix_num_single_state["text"] = ""
                        self.check_valid_mix_num_gn_entry.delete(0, "end")
                        self.check_valid_mix_num_fn_entry.delete(0, "end")
                        self.check_valid_mix_num_year_entry.delete(0, "end")
                        self.check_valid_mix_num_month_entry.delete(0, "end")
                        self.check_valid_mix_num_day_entry.delete(0, "end")
                        self.check_valid_mix_num_hour_entry.delete(0, "end")
                        self.check_valid_mix_num_minute_entry.delete(0, "end")
                        self.check_valid_mix_num_multiple_state["text"] = ""
                        self.check_valid_mem_num_main_entry.delete(0, "end")
                        self.check_valid_mem_num_single_state["text"] = ""
                        self.check_valid_mem_num_mix_entry.delete(0, "end")
                        self.check_valid_mem_num_org_entry.delete(0, "end")
                        self.check_valid_mem_num_vn_entry.delete(0, "end")
                        self.check_valid_mem_num_multiple_state["text"] = ""
                        self.check_valid_org_num_main_entry.delete(0, "end")
                        self.check_valid_org_num_single_state["text"] = ""
                        self.check_valid_org_num_year_entry.delete(0, "end")
                        self.check_valid_org_num_month_entry.delete(0, "end")
                        self.check_valid_org_num_day_entry.delete(0, "end")
                        self.check_valid_org_num_hour_entry.delete(0, "end")
                        self.check_valid_org_num_minute_entry.delete(0, "end")
                        self.check_valid_org_num_multiple_state["text"] = ""
                        self.check_valid_mani_num_main_entry.delete(0, "end")
                        self.check_valid_mani_num_single_state["text"] = ""
                        self.check_valid_mani_num_org_entry.delete(0, "end")
                        self.check_valid_mani_num_multiple_state["text"] = ""
                        self.output_csv_page_frame.grid_forget()
                        self.output_csv_page_button["font"] = self.fonsize_s
                    elif in_str == "output_csv":
                        self.setting_page_frame.grid_forget()
                        self.setting_page_button["font"] = self.fonsize_s
                        self.other_page_frame.grid_forget()
                        self.other_page_button["font"] = self.fonsize_s
                        self.generate_num_page_frame.grid_forget()
                        self.generate_num_page_button["font"] = self.fonsize_s
                        self.check_validity_page_frame.grid_forget()
                        self.check_validity_page_button["font"] = self.fonsize_s
                        self.output_csv_page_frame.grid(row = 1, column = 0,
                                                        padx = 5, pady = 5,
                                                        sticky = tk.W)
                        self.output_csv_page_button["font"] = self.fonsize_s_b
                        self.output_csv_page_mem_scan_progressbar["value"] = 0
                        self.output_csv_page_mem_scan_state["text"] = ""
                        self.output_csv_page_mem_copy_progressbar["value"] = 0
                        self.output_csv_page_mem_copy_state["text"] = ""
                        self.output_csv_page_mem_output_progressbar["value"] = 0
                        self.output_csv_page_mem_output_state["text"] = ""
                        self.output_csv_page_mem_state["text"] = ""                     
                        self.output_csv_page_cur_process_vari = ""
                        self.output_csv_mem_name_copy_from_list = None
                        self.output_csv_mem_name_copy_list = None
                        self.output_csv_mem_content_list = None
                        self.output_csv_page_mem_radio.select()
                        self.output_csv_fun_select()
                else:
                    self.setting_page_frame.grid_forget()
                    self.setting_page_button["font"] = self.fonsize_s
                    self.other_page_frame.grid_forget()
                    self.other_page_button["font"] = self.fonsize_s
                    self.generate_num_page_frame.grid_forget()
                    self.generate_num_page_button["font"] = self.fonsize_s
                    self.check_validity_page_frame.grid_forget()
                    self.check_validity_page_button["font"] = self.fonsize_s
                    self.output_csv_page_frame.grid_forget()
                    self.output_csv_page_button["font"] = self.fonsize_s
    
    def generate_page(self):
        generate_page_radio_frame = tk.LabelFrame(self.generate_num_page_frame, 
                                                  text = "Generate member numbers: select a function", 
                                                  font = self.fonsize_s)
        generate_page_radio_frame.grid(row = 0, column = 0,
                                       padx = 5, pady = 5,
                                       sticky = tk.W)
        generate_page_radio_line_0 = tk.Frame(generate_page_radio_frame)
        generate_page_radio_line_0.grid(row = 0, column = 0,
                                        sticky = tk.W)
        generate_page_radio_line_1 = tk.Frame(generate_page_radio_frame)
        generate_page_radio_line_1.grid(row = 1, column = 0,
                                        sticky = tk.W)
        self.generate_page_radio_vari = tk.StringVar()
        self.generate_page_single_radio = tk.Radiobutton(generate_page_radio_line_0, 
                                                         variable = self.generate_page_radio_vari, 
                                                         text = "Output single member number", 
                                                         value = "single", 
                                                         font = self.fonsize_s)
        self.generate_page_single_radio.grid(row = 0, column = 0,
                                             padx = 2, pady = 2, 
                                             sticky = tk.W)
        self.generate_page_multiple_radio = tk.Radiobutton(generate_page_radio_line_0, 
                                                           variable = self.generate_page_radio_vari, 
                                                           text = "Output multiple member numbers by *.csv file", 
                                                           value = "multiple", 
                                                           font = self.fonsize_s)
        self.generate_page_multiple_radio.grid(row = 0, column = 1,
                                               padx = 2, pady = 2, 
                                               sticky = tk.W)
        ## command
        self.generate_page_single_radio["command"] = self.generate_fun_select
        self.generate_page_multiple_radio["command"] = self.generate_fun_select
        
        # single
        self.generate_page_single_frame = tk.Frame(self.generate_num_page_frame)
        self.generate_page_single_frame.grid(row = 1, column = 0,
                                             padx = 5, pady = 5,
                                             sticky = tk.W)
        gene_single_en_name_frame = tk.Frame(self.generate_page_single_frame)
        gene_single_en_name_frame.grid(row = 0, column = 0,
                                       padx = 2, pady = 2,
                                       sticky = tk.W)
        gene_single_en_name_frame_line_0 = tk.Frame(gene_single_en_name_frame)
        gene_single_en_name_frame_line_0.grid(row = 0, column = 0,
                                              sticky = tk.NW)
        ttk.Label(gene_single_en_name_frame_line_0, 
                  text = "1. English name: ",                     
                  font = self.fonsize_m).grid(row = 0, column = 0,
                                              padx = 2, 
                                              sticky = tk.NW)
        gene_single_en_name_frame_line_0_right = tk.Frame(gene_single_en_name_frame_line_0)
        gene_single_en_name_frame_line_0_right.grid(row = 0, column = 1,
                                                    padx = 2, 
                                                    sticky = tk.NW)
        ttk.Label(gene_single_en_name_frame_line_0_right, 
                  text = "Given Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.gene_single_gn_entry_vari = tk.StringVar()
        self.gene_single_gn_entry = tk.Entry(gene_single_en_name_frame_line_0_right, 
                                             textvariable = self.gene_single_gn_entry_vari, 
                                             width = 14, 
                                             font = self.fonsize_s)
        self.gene_single_gn_entry.grid(row = 1, column = 0,
                                       sticky = tk.W)
        ttk.Label(gene_single_en_name_frame_line_0_right, 
                  text = "Middle Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 1,
                                              sticky = tk.W)
        self.gene_single_mn_entry_vari = tk.StringVar()
        self.gene_single_mn_entry = tk.Entry(gene_single_en_name_frame_line_0_right, 
                                             textvariable = self.gene_single_mn_entry_vari, 
                                             width = 14, 
                                             font = self.fonsize_s)
        self.gene_single_mn_entry.grid(row = 1, column = 1,
                                       sticky = tk.W)
        ttk.Label(gene_single_en_name_frame_line_0_right, 
                  text = "Family Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        self.gene_single_fn_entry_vari = tk.StringVar()
        self.gene_single_fn_entry = tk.Entry(gene_single_en_name_frame_line_0_right, 
                                             textvariable = self.gene_single_fn_entry_vari, 
                                             width = 14, 
                                             font = self.fonsize_s)
        self.gene_single_fn_entry.grid(row = 1, column = 2,
                                       sticky = tk.W)
        ttk.Label(gene_single_en_name_frame_line_0, 
                  text = "    ",
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              padx = 2, 
                                              sticky = tk.NW)
        self.gene_single_gene_button = tk.Button(gene_single_en_name_frame_line_0, 
                                                 text = "Generate", 
                                                 width = 10, 
                                                 font = self.fonsize_m, 
                                                 foreground = "green", 
                                                 activeforeground = "green")
        self.gene_single_gene_button.grid(row = 0, column = 3,
                                          padx = 2, pady = 2,
                                          sticky = tk.SE)
        self.gene_single_clean_button = tk.Button(gene_single_en_name_frame_line_0, 
                                                  text = "Clean", 
                                                  width = 7, 
                                                  font = self.fonsize_m, )
        self.gene_single_clean_button.grid(row = 0, column = 4,
                                           padx = 2, pady = 2,
                                           sticky = tk.SE)
        gene_single_en_name_frame_line_1 = tk.Frame(gene_single_en_name_frame)
        gene_single_en_name_frame_line_1.grid(row = 1, column = 0,
                                              sticky = tk.W)
        ttk.Label(gene_single_en_name_frame_line_1, 
                  text = "Note, ",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              padx = 2, 
                                              sticky = tk.NW)
        gene_single_en_name_frame_line_1_right = tk.Frame(gene_single_en_name_frame_line_1)
        gene_single_en_name_frame_line_1_right.grid(row = 0, column = 1,
                                                    padx = 2, 
                                                    sticky = tk.NW)
        temp_str_0 = "(1) The valid format requires either "
        temp_str_0 = temp_str_0+"\"all the 3 parts of the name are empty\" as \"no name provided\", "
        temp_str_0 = temp_str_0+"or \"at least the given name is non-empty\" as \"name provided\". "
        ttk.Label(gene_single_en_name_frame_line_1_right, 
                  text = temp_str_0,
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        temp_str_0 = "(2) For any part of the English name, if it is non-empty, "
        temp_str_0 = temp_str_0+"its initial character should be from 26 English capital letters, "
        temp_str_0 = temp_str_0+"and each character of the rest should be from 26 English capital letters, "
        temp_str_0 = temp_str_0+"26 English small letters, space \" \", hyphen \"-\", single quotation mark \"'\" and \"‘\" and \"’\"."
        ttk.Label(gene_single_en_name_frame_line_1_right, 
                  text = temp_str_0,
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.W)
        ttk.Separator(self.generate_page_single_frame, 
                      orient="horizontal").grid(row = 1, column = 0, 
                                                sticky = tk.EW)     
        gene_single_vn_name_frame = tk.Frame(self.generate_page_single_frame)
        gene_single_vn_name_frame.grid(row = 2, column = 0,
                                       padx = 2, pady = 2,
                                       sticky = tk.W)
        gene_single_vn_name_frame_line_0 = tk.Frame(gene_single_vn_name_frame)
        gene_single_vn_name_frame_line_0.grid(row = 0, column = 0,
                                              sticky = tk.NW)
        ttk.Label(gene_single_vn_name_frame_line_0, 
                  text = "2. Another name / virtual name: ",                     
                  font = self.fonsize_m).grid(row = 0, column = 0,
                                              sticky = tk.NW)
        gene_single_vn_name_frame_line_0_right = tk.Frame(gene_single_vn_name_frame_line_0)
        gene_single_vn_name_frame_line_0_right.grid(row = 0, column = 1,
                                                    sticky = tk.NW)
        gene_single_vn_name_frame_line_0_right_line_0 = tk.Frame(gene_single_vn_name_frame_line_0_right)
        gene_single_vn_name_frame_line_0_right_line_0.grid(row = 0, column = 0,
                                                           sticky = tk.NW)
        ttk.Label(gene_single_vn_name_frame_line_0_right_line_0, 
                  text = "Name type ",        
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.gene_single_vt_combo_vari = tk.StringVar()
        self.gene_single_vt_combo = ttk.Combobox(gene_single_vn_name_frame_line_0_right_line_0, 
                                                 textvariable = self.gene_single_vt_combo_vari, 
                                                 values = self.virtual_type, 
                                                 width = 35, 
                                                 state = "readonly",
                                                 font = self.fonsize_s)
        self.gene_single_vt_combo.grid(row = 0, column = 1, 
                                       sticky = tk.W)
        self.gene_single_vt_combo.set("Other")
        gene_single_vn_name_frame_line_0_right_line_1 = tk.Frame(gene_single_vn_name_frame_line_0_right)
        gene_single_vn_name_frame_line_0_right_line_1.grid(row = 1, column = 0,
                                                           sticky = tk.NW)
        ttk.Label(gene_single_vn_name_frame_line_0_right_line_1, 
                  text = "Name ",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.gene_single_vn_entry_vari = tk.StringVar()
        self.gene_single_vn_entry = tk.Entry(gene_single_vn_name_frame_line_0_right_line_1, 
                                             textvariable = self.gene_single_vn_entry_vari, 
                                             width = 14, 
                                             font = self.fonsize_s)
        self.gene_single_vn_entry.grid(row = 0, column = 1,
                                       sticky = tk.W)
        ttk.Label(gene_single_vn_name_frame_line_0_right_line_1, 
                  text = ", Addition (@ or #) ",
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        self.gene_single_va_entry_vari = tk.StringVar()
        self.gene_single_va_entry = tk.Entry(gene_single_vn_name_frame_line_0_right_line_1, 
                                             textvariable = self.gene_single_va_entry_vari, 
                                             width = 14, 
                                             font = self.fonsize_s)
        self.gene_single_va_entry.grid(row = 0, column = 3,
                                       sticky = tk.W)
        gene_single_vn_name_frame_line_1 = tk.Frame(gene_single_vn_name_frame)
        gene_single_vn_name_frame_line_1.grid(row = 1, column = 0,
                                              sticky = tk.NW)
        ttk.Label(gene_single_vn_name_frame_line_1, 
                  text = "Note, ",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              padx = 2, 
                                              sticky = tk.NW)
        gene_single_vn_name_frame_line_1_right = tk.Frame(gene_single_vn_name_frame_line_1)
        gene_single_vn_name_frame_line_1_right.grid(row = 0, column = 1,
                                                    padx = 2, 
                                                    sticky = tk.NW)
        temp_str_0 = "(1) Another name / virtual name will be treated as empty, "
        temp_str_0 = temp_str_0+"if the type is \"None\" or the name is empty."
        ttk.Label(gene_single_vn_name_frame_line_1_right, 
                  text = temp_str_0,
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        temp_str_0 = "(2) The characters in the name and addition (@ or #) are ranging within the Unicode U+0020 to U+FFFF. "
        temp_str_0 = temp_str_0+"and among them the quotation mark \"\"\" and \"'\" will be replaced with \"?\"."
        ttk.Label(gene_single_vn_name_frame_line_1_right, 
                  text = temp_str_0,
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.W)
        temp_str_0 = "(3) At least, one of the English name or another name / virtual name should be non-empty."
        ttk.Label(gene_single_vn_name_frame_line_1_right, 
                  text = temp_str_0,
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 2, column = 0,
                                              sticky = tk.W)
        ## command
        self.gene_single_gene_button["command"] = self.generate_fun_single_gene
        self.gene_single_clean_button["command"] = self.generate_fun_single_clean
        
        # multiple
        self.generate_page_multiple_frame = tk.Frame(self.generate_num_page_frame)
        self.generate_page_multiple_frame.grid(row = 1, column = 0,
                                               padx = 5, pady = 5,
                                               sticky = tk.W)   
        generate_page_multiple_import_frame = tk.Frame(self.generate_page_multiple_frame)
        generate_page_multiple_import_frame.grid(row = 0, column = 0,
                                                 padx = 2, pady = 2,
                                                 sticky = tk.W)  
        generate_page_multiple_import_frame_line_0 = tk.Frame(generate_page_multiple_import_frame)
        generate_page_multiple_import_frame_line_0.grid(row = 0, column = 0,
                                                        sticky = tk.W)  
        self.gene_multiple_import_csv_button = tk.Button(generate_page_multiple_import_frame_line_0, 
                                                         text = "Import a *.csv file", 
                                                         width = 21, 
                                                         font = self.fonsize_s)
        self.gene_multiple_import_csv_button.grid(row = 0, column = 0,
                                                  sticky = tk.W)
        self.gene_multiple_clean_csv_button = tk.Button(generate_page_multiple_import_frame_line_0, 
                                                         text = "Clean", 
                                                         width = 7, 
                                                         font = self.fonsize_s)
        self.gene_multiple_clean_csv_button.grid(row = 0, column = 1,
                                                 sticky = tk.W)
        generate_page_multiple_import_frame_line_1 = tk.Frame(generate_page_multiple_import_frame)
        generate_page_multiple_import_frame_line_1.grid(row = 1, column = 0,
                                                        padx = 2, pady = 2,
                                                        sticky = tk.W)  
        self.cur_gene_import_csv_str_list = None
        self.cur_gene_import_csv_title = None
        temp_str = "(1) In the first row, title row of the *.csv file, there must be 6 or 7 cells (regardless capital or small letters): "
        temp_str = temp_str+"(i) \"Given Names\" or \"GN\", "
        temp_str = temp_str+"(ii) \"Middle Names\" or \"MN\", "
        temp_str = temp_str+"(iii) \"Family Names\" or \"FN\", "
        temp_str = temp_str+"(iv) \"Another Types\" or \"Virtual Types\" or \"AT\" or \"VT\", "
        temp_str = temp_str+"(v) \"Another Names\" or \"Virtual Names\" or \"AN\" or \"VN\", "
        temp_str = temp_str+"(vi) \"Another Additions\" or \"Virtual Additions\" or \"AA\" or \"VA\", "
        temp_str = temp_str+"(vii) an optional cell \"Index\" or \"No\"."
        ttk.Label(generate_page_multiple_import_frame_line_1, 
                  text = temp_str,
                  wraplength = 1100, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.NW) 
        temp_str = "(2) The max row number (excluding first row, title row) is 20 000."
        ttk.Label(generate_page_multiple_import_frame_line_1, 
                  text = temp_str,
                  wraplength = 1100, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.NW) 
        ttk.Separator(self.generate_page_multiple_frame, 
                      orient="horizontal").grid(row = 1, column = 0, 
                                                sticky = tk.EW)   
        generate_page_multiple_gene_frame = tk.Frame(self.generate_page_multiple_frame)
        generate_page_multiple_gene_frame.grid(row = 2, column = 0,
                                               padx = 2, pady = 2,
                                               sticky = tk.W) 
        generate_page_multiple_gene_frame_line_0 = tk.Frame(generate_page_multiple_gene_frame)
        generate_page_multiple_gene_frame_line_0.grid(row = 0, column = 0,
                                                      padx = 2, pady = 2,
                                                      sticky = tk.W)  
        self.gene_multiple_gene_button = tk.Button(generate_page_multiple_gene_frame_line_0, 
                                                   text = "Generate", 
                                                   width = 10, 
                                                   font = self.fonsize_m, 
                                                   foreground = "green", 
                                                   activeforeground = "green")
        self.gene_multiple_gene_button.grid(row = 0, column = 0,
                                            padx = 2, pady = 2,
                                            sticky = tk.W)
        self.gene_multiple_gene_stop_button = tk.Button(generate_page_multiple_gene_frame_line_0, 
                                                        text = "Stop", 
                                                        width = 6, 
                                                        font = self.fonsize_s)        
        self.gene_multiple_gene_stop_button.grid(row = 0, column = 1, 
                                                 sticky = tk.W)          
        self.gene_multiple_gene_state_0 = ttk.Label(generate_page_multiple_gene_frame_line_0, 
                                                    text = "",
                                                    wraplength = 700, 
                                                    font = self.fonsize_s)
        self.gene_multiple_gene_state_0.grid(row = 0, column = 2,
                                             sticky = tk.W)
        generate_page_multiple_gene_frame_line_1 = tk.Frame(generate_page_multiple_gene_frame)
        generate_page_multiple_gene_frame_line_1.grid(row = 1, column = 0,
                                                      padx = 2, pady = 2,
                                                      sticky = tk.W)  
        generate_page_multiple_gene_frame_line_1_0 = tk.Frame(generate_page_multiple_gene_frame_line_1)
        generate_page_multiple_gene_frame_line_1_0.grid(row = 0, column = 0,
                                                        sticky = tk.NW)  
        ttk.Label(generate_page_multiple_gene_frame_line_1_0, 
                  text = "(1) Analyze rows' contents",
                  wraplength = 490, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.NW)        
        self.gene_multiple_gene_progressbar_0 = ttk.Progressbar(generate_page_multiple_gene_frame_line_1_0, 
                                                                length = 490, 
                                                                mode="determinate", 
                                                                orient = "horizontal")
        self.gene_multiple_gene_progressbar_0.grid(row = 1, column = 0, 
                                                   padx = 2, pady = 2,
                                                   sticky = tk.N)
        generate_page_multiple_gene_frame_line_1_0_2 = tk.Frame(generate_page_multiple_gene_frame_line_1_0)
        generate_page_multiple_gene_frame_line_1_0_2.grid(row = 2, column = 0,
                                                          sticky = tk.N) 
        self.gene_multiple_gene_state_0_0 = ttk.Label(generate_page_multiple_gene_frame_line_1_0_2, 
                                                      text = "",
                                                      wraplength = 230, 
                                                      font = self.fonsize_s)
        self.gene_multiple_gene_state_0_0.grid(row = 0, column = 0,
                                               sticky = tk.N)
        ttk.Label(generate_page_multiple_gene_frame_line_1_0_2, 
                  text = " ; ", 
                  font = self.fonsize_s).grid(row = 0, column = 1,
                                              sticky = tk.N)  
        self.gene_multiple_gene_state_0_1 = ttk.Label(generate_page_multiple_gene_frame_line_1_0_2, 
                                                      text = "",
                                                      wraplength = 230, 
                                                      font = self.fonsize_s)
        self.gene_multiple_gene_state_0_1.grid(row = 0, column = 2,
                                               sticky = tk.N)        
        ttk.Separator(generate_page_multiple_gene_frame_line_1, 
                      orient="vertical").grid(row = 0, column = 1, 
                                              sticky = tk.NS) 
        generate_page_multiple_gene_frame_line_1_1 = tk.Frame(generate_page_multiple_gene_frame_line_1)
        generate_page_multiple_gene_frame_line_1_1.grid(row = 0, column = 2,
                                                        sticky = tk.NW)
        ttk.Label(generate_page_multiple_gene_frame_line_1_1, 
                  text = "(2) Forming mixed numbers",
                  wraplength = 490, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.NW) 
        self.gene_multiple_gene_progressbar_1 = ttk.Progressbar(generate_page_multiple_gene_frame_line_1_1, 
                                                                length = 490, 
                                                                mode="determinate", 
                                                                orient = "horizontal")
        self.gene_multiple_gene_progressbar_1.grid(row = 1, column = 0, 
                                                   padx = 2, pady = 2,
                                                   sticky = tk.N)
        generate_page_multiple_gene_frame_line_1_1_2 = tk.Frame(generate_page_multiple_gene_frame_line_1_1)
        generate_page_multiple_gene_frame_line_1_1_2.grid(row = 2, column = 0,
                                                          sticky = tk.N) 
        self.gene_multiple_gene_state_1_0 = ttk.Label(generate_page_multiple_gene_frame_line_1_1_2, 
                                                      text = "",
                                                      wraplength = 230, 
                                                      font = self.fonsize_s)
        self.gene_multiple_gene_state_1_0.grid(row = 0, column = 0,
                                               sticky = tk.N)
        ttk.Label(generate_page_multiple_gene_frame_line_1_1_2, 
                  text = " ; ", 
                  font = self.fonsize_s).grid(row = 0, column = 1,
                                              sticky = tk.N)  
        self.gene_multiple_gene_state_1_1 = ttk.Label(generate_page_multiple_gene_frame_line_1_1_2, 
                                                      text = "",
                                                      wraplength = 230, 
                                                      font = self.fonsize_s)
        self.gene_multiple_gene_state_1_1.grid(row = 0, column = 2,
                                               sticky = tk.N) 
        ttk.Separator(generate_page_multiple_gene_frame_line_1, 
                      orient="horizontal").grid(row = 1, column = 0, 
                                              sticky = tk.EW) 
        ttk.Separator(generate_page_multiple_gene_frame_line_1, 
                      orient="horizontal").grid(row = 1, column = 2, 
                                              sticky = tk.EW) 
        generate_page_multiple_gene_frame_line_1_2 = tk.Frame(generate_page_multiple_gene_frame_line_1)
        generate_page_multiple_gene_frame_line_1_2.grid(row = 2, column = 0,
                                                        sticky = tk.NW)
        ttk.Label(generate_page_multiple_gene_frame_line_1_2, 
                  text = "(3) Forming member numbers",
                  wraplength = 490, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.NW)        
        self.gene_multiple_gene_progressbar_2 = ttk.Progressbar(generate_page_multiple_gene_frame_line_1_2, 
                                                                length = 490, 
                                                                mode="determinate", 
                                                                orient = "horizontal")
        self.gene_multiple_gene_progressbar_2.grid(row = 1, column = 0, 
                                                   padx = 2, pady = 2,
                                                   sticky = tk.N)
        generate_page_multiple_gene_frame_line_1_2_2 = tk.Frame(generate_page_multiple_gene_frame_line_1_2)
        generate_page_multiple_gene_frame_line_1_2_2.grid(row = 2, column = 0,
                                                          sticky = tk.N) 
        self.gene_multiple_gene_state_2_0 = ttk.Label(generate_page_multiple_gene_frame_line_1_2_2, 
                                                      text = "",
                                                      wraplength = 230, 
                                                      font = self.fonsize_s)
        self.gene_multiple_gene_state_2_0.grid(row = 0, column = 0,
                                               sticky = tk.N)
        ttk.Label(generate_page_multiple_gene_frame_line_1_2_2, 
                  text = " ; ", 
                  font = self.fonsize_s).grid(row = 0, column = 1,
                                              sticky = tk.N)  
        self.gene_multiple_gene_state_2_1 = ttk.Label(generate_page_multiple_gene_frame_line_1_2_2, 
                                                      text = "",
                                                      wraplength = 230, 
                                                      font = self.fonsize_s)
        self.gene_multiple_gene_state_2_1.grid(row = 0, column = 2,
                                               sticky = tk.N) 
        ttk.Separator(generate_page_multiple_gene_frame_line_1, 
                      orient="vertical").grid(row = 2, column = 1, 
                                              sticky = tk.NS) 
        generate_page_multiple_gene_frame_line_1_3 = tk.Frame(generate_page_multiple_gene_frame_line_1)
        generate_page_multiple_gene_frame_line_1_3.grid(row = 2, column = 2,
                                                        sticky = tk.NW)
        ttk.Label(generate_page_multiple_gene_frame_line_1_3, 
                  text = "(4) Output files",
                  wraplength = 490, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.NW)        
        self.gene_multiple_gene_progressbar_3 = ttk.Progressbar(generate_page_multiple_gene_frame_line_1_3, 
                                                                length = 490, 
                                                                mode="determinate", 
                                                                orient = "horizontal")
        self.gene_multiple_gene_progressbar_3.grid(row = 1, column = 0, 
                                                   padx = 2, pady = 2,
                                                   sticky = tk.N)
        generate_page_multiple_gene_frame_line_1_3_2 = tk.Frame(generate_page_multiple_gene_frame_line_1_3)
        generate_page_multiple_gene_frame_line_1_3_2.grid(row = 2, column = 0,
                                                          sticky = tk.N) 
        self.gene_multiple_gene_state_3_0 = ttk.Label(generate_page_multiple_gene_frame_line_1_3_2, 
                                                      text = "",
                                                      wraplength = 230, 
                                                      font = self.fonsize_s)
        self.gene_multiple_gene_state_3_0.grid(row = 0, column = 0,
                                               sticky = tk.N)
        ttk.Label(generate_page_multiple_gene_frame_line_1_3_2, 
                  text = " ; ", 
                  font = self.fonsize_s).grid(row = 0, column = 1,
                                              sticky = tk.N)  
        self.gene_multiple_gene_state_3_1 = ttk.Label(generate_page_multiple_gene_frame_line_1_3_2, 
                                                      text = "",
                                                      wraplength = 230, 
                                                      font = self.fonsize_s)
        self.gene_multiple_gene_state_3_1.grid(row = 0, column = 2,
                                               sticky = tk.N)
        generate_page_multiple_gene_frame_line_2 = tk.Frame(generate_page_multiple_gene_frame)
        generate_page_multiple_gene_frame_line_2.grid(row = 2, column = 0,
                                                      padx = 2, pady = 2,
                                                      sticky = tk.NE) 
        self.gene_multiple_gene_state_2 = ttk.Label(generate_page_multiple_gene_frame_line_2, 
                                                    text = "",
                                                    wraplength = 1000, 
                                                    font = self.fonsize_s)
        self.gene_multiple_gene_state_2.grid(row = 0, column = 0,
                                             sticky = tk.NE) 
        ## command
        self.gene_multiple_import_csv_button["command"] = self.generate_fun_multiple_import
        self.gene_multiple_clean_csv_button["command"] = self.generate_fun_multiple_clean
        self.gene_multiple_gene_button["command"] = self.generate_fun_multiple_generate
        self.gene_multiple_gene_stop_button["command"] = self.generate_fun_multiple_stop
    
    def generate_fun_select(self):
        if not self.cur_progress_bool:
            temp_str = self.generate_page_radio_vari.get()
            if temp_str == "single":
                self.generate_page_single_frame.grid(row = 1, column = 0,
                                                     padx = 5, pady = 5, 
                                                     sticky = tk.NW)
                self.generate_page_multiple_frame.grid_forget()
            elif temp_str == "multiple":
                self.generate_page_single_frame.grid_forget()
                self.generate_page_multiple_frame.grid(row = 1, column = 0,
                                                       padx = 5, pady = 5, 
                                                       sticky = tk.NW)                
        else:
            self.generate_page_multiple_radio.select()
    
    def generate_fun_single_gene(self):
        temp_bool_0 = True
        if os.path.exists(self.cur_org_file_name):
            with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.cur_org = self.reading_str_text_org(read_text)
            if not self.cur_org is None:
                temp_num_0 = -1
                for n in range(len(self.cur_org[2])):
                    if self.cur_org[2][n] == self.cur_mani_num:
                        temp_num_0 = n
                        break
                if temp_num_0 >= 0:
                    temp_bool_0 = self.cur_org[3][temp_num_0]
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        if not temp_bool_0:
            showerror(title = "Error", 
                      message = "No privilege to do so.") 
        else:
            temp_bool_1 = True
            temp_file_list = os.scandir(self.basic_parameter[1][0])
            for e in temp_file_list:
                temp_str_0 = e.name
                if len(temp_str_0) > 4:
                    temp_str_1 = temp_str_0[-4:].upper()
                    if (temp_str_1 == ".CSV") | (temp_str_1 == ".TXT"):
                        temp_bool_1 = False
                    if temp_bool_1:
                        if len(temp_str_0) > 5:
                            temp_str_1 = temp_str_0[-5:].upper()
                            if temp_str_1 == ".IDEN":
                                temp_bool_1 = False
                if not temp_bool_1:
                    break
            if temp_bool_1:
                for n in range(len(self.basic_parameter[1][1])):
                    temp_file_list = os.scandir(self.basic_parameter[1][1][n])
                    for e in temp_file_list:
                        temp_str_0 = e.name
                        if len(temp_str_0) > 4:
                            temp_str_1 = temp_str_0[-4:].upper()
                            if (temp_str_1 == ".CSV") | (temp_str_1 == ".TXT"):
                                temp_bool_1 = False
                            if temp_bool_1:
                                if len(temp_str_0) > 5:
                                    temp_str_1 = temp_str_0[-5:].upper()
                                    if temp_str_1 == ".IDEN":
                                        temp_bool_1 = False
                        if not temp_bool_1:
                            break
                    if not temp_bool_1:
                        break
            if not temp_bool_1:
                showerror(title = "Error", 
                          message = "There exists other *.iden or *.txt, *.csv in '"+self.basic_parameter[1][0]+"/', or its sub-folders.")
            else:
                temp_str_0 = self.gene_single_gn_entry_vari.get().strip()
                temp_str_1 = self.gene_single_mn_entry_vari.get().strip()
                temp_str_2 = self.gene_single_fn_entry_vari.get().strip()
                temp_list_0 = [temp_str_0, temp_str_1, temp_str_2]
                temp_list_0 = self.English_name_change_quotation_mark(temp_list_0)
                if not temp_list_0 is None: 
                    self.cur_progress_bool = True
                    temp_list_1 = self.number_mix_generate([[temp_list_0[0], temp_list_0[2]]], self.cur_org[0][3])
                    self.cur_progress_bool = False
                    temp_list_1 = temp_list_1[0]                    
                    if not temp_list_1 is None:
                        temp_str_0 = self.gene_single_vt_combo_vari.get().strip()
                        temp_str_1 = self.gene_single_vn_entry_vari.get().strip()
                        temp_str_2 = self.gene_single_va_entry_vari.get().strip()
                        temp_list_2 = [temp_str_0, temp_str_1, temp_str_2]
                        temp_list_2 = self.virtual_name_change_quotation_mark(temp_list_2)
                        if not temp_list_2 is None:
                            self.cur_progress_bool = True
                            temp_list_3 = self.number_member_generate([[temp_list_1[0], temp_list_0[0], temp_list_0[2], 
                                                                        temp_list_2[1], self.cur_org[0][0], 
                                                                        temp_list_1[4], temp_list_1[5]]])
                            self.cur_progress_bool = False
                            temp_list_3 = temp_list_3[0]
                            if not temp_list_3 is None:
                                temp_list_4 = [temp_list_3[1], temp_list_3[0]]
                                temp_list_5 = [temp_list_1[4], temp_list_1[5]]
                                temp_list_6 = [self.cur_org[0][0], self.cur_org[0][5][1], 
                                               self.cur_org[0][5][2], self.cur_mani_num]
                                out_str_list_1 = self.forming_str_text_member_lang(temp_list_4, temp_list_0, 
                                                                                   temp_list_2, temp_list_5, 
                                                                                   temp_list_6, 
                                                                                   self.basic_parameter[1][2][1], 
                                                                                   self.basic_parameter[1][2][2], 
                                                                                   self.basic_parameter[1][2][3])
                                temp_str_1 = "Mem_"
                                temp_str_1 = temp_str_1+temp_list_1[4][0]
                                temp_str_1 = temp_str_1+temp_list_1[4][1]
                                temp_str_1 = temp_str_1+temp_list_1[4][2]
                                temp_str_1 = temp_str_1+temp_list_1[4][3]
                                temp_str_1 = temp_str_1+temp_list_1[4][5]
                                temp_str_1 = temp_str_1+temp_list_1[4][6]
                                temp_str_1 = temp_str_1+temp_list_1[4][8]
                                temp_str_1 = temp_str_1+temp_list_1[4][9]
                                temp_str_1 = temp_str_1+temp_list_1[5][0]
                                temp_str_1 = temp_str_1+temp_list_1[5][1]
                                temp_str_1 = temp_str_1+temp_list_1[5][3]
                                temp_str_1 = temp_str_1+temp_list_1[5][4]
                                temp_str_1 = temp_str_1+"_"
                                temp_str_1 = temp_str_1+temp_list_0[0]
                                temp_str_1 = temp_str_1+"_"
                                temp_str_1 = temp_str_1+temp_list_0[1]
                                temp_str_1 = temp_str_1+"_"
                                temp_str_1 = temp_str_1+temp_list_0[2]
                                temp_str_1 = temp_str_1+"_"
                                temp_str_1 = temp_str_1+temp_list_3[0]
                                temp_str_1_0 = temp_str_1+".iden"
                                temp_str_1_0 = self.basic_parameter[1][1][0]+"/"+temp_str_1_0
                                with open(temp_str_1_0, "w", encoding = "utf-8") as save_file:
                                    save_file.write(out_str_list_1[0])
                                    save_file.close()
                                temp_str_2 = "The file with path '"+temp_str_1_0+"' is output."
                                if self.basic_parameter[1][2][1]:
                                    temp_str_1_0 = temp_str_1+"_English.txt"
                                    temp_str_1_0 = self.basic_parameter[1][1][1]+"/"+temp_str_1_0
                                    temp_str_2 = temp_str_2+"\n"
                                    temp_str_2 = temp_str_2+"The file with path '"+temp_str_1_0+"' is output."
                                    with open(temp_str_1_0, "w", encoding = "utf-8") as save_file:
                                        save_file.write(out_str_list_1[1])
                                        save_file.close()
                                if self.basic_parameter[1][2][2]:
                                    temp_str_1_0 = temp_str_1+"_简体中文.txt"
                                    temp_str_1_0 = self.basic_parameter[1][1][2]+"/"+temp_str_1_0
                                    temp_str_2 = temp_str_2+"\n"
                                    temp_str_2 = temp_str_2+"The file with path '"+temp_str_1_0+"' is output."
                                    with open(temp_str_1_0, "w", encoding = "utf-8") as save_file:
                                        save_file.write(out_str_list_1[2])
                                        save_file.close()
                                if self.basic_parameter[1][2][3]:
                                    temp_str_1_0 = temp_str_1+"_正體中文.txt"
                                    temp_str_1_0 = self.basic_parameter[1][1][3]+"/"+temp_str_1_0
                                    temp_str_2 = temp_str_2+"\n"
                                    temp_str_2 = temp_str_2+"The file with path '"+temp_str_1_0+"' is output."
                                    with open(temp_str_1_0, "w", encoding = "utf-8") as save_file:
                                        save_file.write(out_str_list_1[3])
                                        save_file.close()
                                showinfo(title = "output *.iden (and *txt) file", 
                                         message = temp_str_2) 
                                self.gene_single_gn_entry.delete(0, "end")
                                self.gene_single_mn_entry.delete(0, "end")
                                self.gene_single_fn_entry.delete(0, "end")
                                self.gene_single_vt_combo.set("Other")
                                self.gene_single_vn_entry.delete(0, "end")
                                self.gene_single_va_entry.delete(0, "end")
                            else:
                                showerror(title = "Error", 
                                          message = "Another name / virtual is in wrong format.")
                        else:
                            showerror(title = "Error", 
                                      message = "Another name / virtual is in wrong format.")
                    else:
                        showerror(title = "Error", 
                                  message = "The English name is in wrong format.")
                else:
                    showerror(title = "Error", 
                              message = "The English name is in wrong format.")
    
    def generate_fun_single_clean(self):
        self.gene_single_gn_entry.delete(0, "end")
        self.gene_single_mn_entry.delete(0, "end")
        self.gene_single_fn_entry.delete(0, "end")
        self.gene_single_vt_combo.set("Other")
        self.gene_single_vn_entry.delete(0, "end")
        self.gene_single_va_entry.delete(0, "end")
    
    def generate_fun_multiple_import(self):
        if not self.cur_progress_bool:
            if os.path.exists(self.cur_org_file_name):
                with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                    read_text = read_file.read()
                    self.cur_org = self.reading_str_text_org(read_text)
                if not self.cur_org is None:
                    temp_num_0 = -1
                    for n in range(len(self.cur_org[2])):
                        if self.cur_org[2][n] == self.cur_mani_num:
                            temp_num_0 = n
                            break
                    if temp_num_0 >= 0:
                        temp_bool_0 = self.cur_org[3][temp_num_0]
                    else:
                        temp_bool_0 = False
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
            if not temp_bool_0:
                showerror(title = "Error", 
                          message = "No privilege to do so.") 
            else:
                file = askopenfile(mode = "r", 
                                   filetypes=[("Comma separated values file of UTF-8", "*.csv")])  
                if file:
                    file_path = file.name
                    with open(file_path, "r", encoding = "utf-8") as open_file:
                        temp_str_0 = open_file.read()
                        if ord(temp_str_0[0]) == 65279:
                            temp_str_0 = temp_str_0[1:]
                        temp_str_list_0 = temp_str_0.split("\n")
                        file.close()
                    temp_bool_0 = True
                    valid_index_tuple = ("INDEX", "NUMBER", "NO.", "NO", "IND", "I", "N")
                    valid_index_bool = False
                    valid_gn_tuple = ("GIVEN NAME", "GIVEN NAMES", "GIVEN-NAME", "GIVEN-NAMES", 
                                      "GIVEN_NAME", "GIVEN_NAMES", "GIVENNAME", "GIVENNAMES", 
                                      "GIV NAME", "GIV NAMES", "GIV-NAME", "GIV-NAMES", 
                                      "GIV_NAME", "GIV_NAMES", "GIVNAME", "GIVNAMES", 
                                      "G NAME", "G NAMES", "G-NAME", "G-NAMES", 
                                      "G_NAME", "G_NAMES", "GNAME", "GNAMES",
                                      "GIVEN N", "GIVEN-N", "GIVEN_N", "GIVENN", 
                                      "GIV N", "GIV-N", "GIV_N", "GIVN", 
                                      "G N", "G-N", "G_N", "GN", 
                                      "N G", "N-G", "N_G", "NG")
                    valid_gn_bool = False
                    valid_gn_num = -1
                    valid_mn_tuple = ("MIDDLE NAME", "MIDDLE NAMES", "MIDDLE-NAME", "MIDDLE-NAMES", 
                                      "MIDDLE_NAME", "MIDDLE_NAMES", "MIDDLENAME", "MIDDLENAMES", 
                                      "MID NAME", "MID NAMES", "MID-NAME", "MID-NAMES", 
                                      "MID_NAME", "MID_NAMES", "MIDNAME", "MIDNAMES", 
                                      "M NAME", "M NAMES", "M-NAME", "M-NAMES", 
                                      "M_NAME", "M_NAMES", "MNAME", "MNAMES",
                                      "MIDDLE N", "MIDDLE-N", "MIDDLE_N", "MIDDLEN", 
                                      "MID N", "MID-N", "MID_N", "MIDN", 
                                      "M N", "M-N", "M_N", "MN", 
                                      "N M", "N-M", "N_M", "NM")
                    valid_mn_bool = False
                    valid_mn_num = -1
                    valid_fn_tuple = ("FAMILY NAME", "FAMILY NAMES", "FAMILY-NAME", "FAMILY-NAMES", 
                                      "FAMILY_NAME", "FAMILY_NAMES", "FAMILYNAME", "FAMILYNAMES", 
                                      "FAM NAME", "FAM NAMES", "FAM-NAME", "FAM-NAMES", 
                                      "FAM_NAME", "FAM_NAMES", "FAMNAME", "FAMNAMES", 
                                      "F NAME", "F NAMES", "F-NAME", "F-NAMES", 
                                      "F_NAME", "F_NAMES", "FNAME", "FNAMES",
                                      "FAMILY N", "FAMILY-N", "FAMILY_N", "FAMILYN", 
                                      "FAM N", "FAM-N", "FAM_N", "FAMN", 
                                      "F N", "F-N", "F_N", "FN", 
                                      "N F", "N-F", "N_F", "NF")
                    valid_fn_bool = False
                    valid_fn_num = -1
                    valid_vt_tuple = ("VIRTUAL TYPE", "VIRTUAL TYPES", "VIRTUAL-TYPE", "VIRTUAL-TYPES", 
                                      "VIRTUAL_TYPE", "VIRTUAL_TYPES", "VIRTUALTYPE", "VIRTUALTYPES", 
                                      "ANOTHER TYPE", "ANOTHER TYPES", "ANOTHER-TYPE", "ANOTHER-TYPES", 
                                      "ANOTHER_TYPE", "ANOTHER_TYPES", "ANOTHERTYPE", "ANOTHERTYPES", 
                                      "VIR TYPE", "VIR TYPES", "VIR-TYPE", "VIR-TYPES", 
                                      "VIR_TYPE", "VIR_TYPES", "VIRTYPE", "VIRTYPES", 
                                      "ANO TYPE", "ANO TYPES", "ANO-TYPE", "ANO-TYPES", 
                                      "ANO_TYPE", "ANO_TYPES", "ANOTYPE", "ANOTYPES",
                                      "V TYPE", "V TYPES", "V-TYPE", "V-TYPES", 
                                      "V_TYPE", "V_TYPES", "VTYPE", "VTYPES",
                                      "A TYPE", "A TYPES", "A-TYPE", "A-TYPES", 
                                      "A_TYPE", "A_TYPES", "ATYPE", "ATYPES",
                                      "VIRTUAL T", "VIRTUAL-T", "VIRTUAL_T", "VIRTUALT",
                                      "ANOTHER T", "ANOTHER-T", "ANOTHER_T", "ANOTHERT",
                                      "VIR T", "VIR-T", "VIR_T", "VIRT",
                                      "ANO T", "ANO-T", "ANO_T", "ANOT",
                                      "V T", "V-T", "V_T", "VT", 
                                      "T V", "T-V", "T_V", "TV", 
                                      "A T", "A-T", "A_T", "AT", 
                                      "T A", "T-A", "T_A", "TA")
                    valid_vt_bool = False
                    valid_vt_num = -1
                    valid_vn_tuple = ("VIRTUAL NAME", "VIRTUAL NAMES", "VIRTUAL-NAME", "VIRTUAL-NAMES", 
                                      "VIRTUAL_NAME", "VIRTUAL_NAMES", "VIRTUALNAME", "VIRTUALNAMES", 
                                      "ANOTHER NAME", "ANOTHER NAMES", "ANOTHER-NAME", "ANOTHER-NAMES", 
                                      "ANOTHER_NAME", "ANOTHER_NAMES", "ANOTHERNAME", "ANOTHERNAMES", 
                                      "VIR NAME", "VIR NAMES", "VIR-NAME", "VIR-NAMES", 
                                      "VIR_NAME", "VIR_NAMES", "VIRNAME", "VIRNAMES", 
                                      "ANO NAME", "ANO NAMES", "ANO-NAME", "ANO-NAMES", 
                                      "ANO_NAME", "ANO_NAMES", "ANONAME", "ANONAMES",
                                      "V NAME", "V NAMES", "V-NAME", "V-NAMES", 
                                      "V_NAME", "V_NAMES", "VNAME", "VNAMES",
                                      "A NAME", "A NAMES", "A-NAME", "A-NAMES", 
                                      "A_NAME", "A_NAMES", "ANAME", "ANAMES",
                                      "VIRTUAL N", "VIRTUAL-N", "VIRTUAL_N", "VIRTUALN",
                                      "ANOTHER N", "ANOTHER-N", "ANOTHER_N", "ANOTHERN",
                                      "VIR N", "VIR-N", "VIR_N", "VIRN",
                                      "ANO N", "ANO-N", "ANO_N", "ANON",
                                      "V N", "V-N", "V_N", "VN", 
                                      "N V", "N-V", "N_V", "NV", 
                                      "A N", "A-N", "A_N", "AN", 
                                      "N A", "N-A", "N_A", "NA")
                    valid_vn_bool = False
                    valid_vn_num = -1
                    valid_va_tuple = ("VIRTUAL ADDITION", "VIRTUAL ADDITIONS", "VIRTUAL-ADDITION", "VIRTUAL-ADDITIONS", 
                                      "VIRTUAL_ADDITION", "VIRTUAL_ADDITIONS", "VIRTUALADDITION", "VIRTUALADDITIONS", 
                                      "ANOTHER ADDITION", "ANOTHER ADDITIONS", "ANOTHER-ADDITION", "ANOTHER-ADDITIONS", 
                                      "ANOTHER_ADDITION", "ANOTHER_ADDITIONS", "ANOTHERADDITION", "ANOTHERADDITIONS", 
                                      "VIR ADDITION", "VIR ADDITIONS", "VIR-ADDITION", "VIR-ADDITIONS", 
                                      "VIR_ADDITION", "VIR_ADDITIONS", "VIRADDITION", "VIRADDITIONS", 
                                      "ANO ADDITION", "ANO ADDITIONS", "ANO-ADDITION", "ANO-ADDITIONS", 
                                      "ANO_ADDITION", "ANO_ADDITIONS", "ANOADDITION", "ANOADDITIONS",
                                      "V ADDITION", "V ADDITIONS", "V-ADDITION", "V-ADDITIONS", 
                                      "V_ADDITION", "V_ADDITIONS", "VADDITION", "VADDITIONS",
                                      "A ADDITION", "A ADDITIONS", "A-ADDITION", "A-ADDITIONS", 
                                      "A_ADDITION", "A_ADDITIONS", "AADDITION", "AADDITIONS",
                                      "VIRTUAL ADD", "VIRTUAL ADDS", "VIRTUAL-ADD", "VIRTUAL-ADDS", 
                                      "VIRTUAL_ADD", "VIRTUAL_ADDS", "VIRTUALADD", "VIRTUALADDS", 
                                      "ANOTHER ADD", "ANOTHER ADDS", "ANOTHER-ADD", "ANOTHER-ADDS", 
                                      "ANOTHER_ADD", "ANOTHER_ADDS", "ANOTHERADD", "ANOTHERADDS", 
                                      "VIR ADD", "VIR ADDS", "VIR-ADD", "VIR-ADDS", 
                                      "VIR_ADD", "VIR_ADDS", "VIRADD", "VIRADDS", 
                                      "ANO ADD", "ANO ADDS", "ANO-ADD", "ANO-ADDS", 
                                      "ANO_ADD", "ANO_ADDS", "ANOADD", "ANOADDS",
                                      "V ADD", "V ADDS", "V-ADD", "V-ADDS", 
                                      "V_ADD", "V_ADDS", "VADD", "VADDS",
                                      "A ADD", "A ADDS", "A-ADD", "A-ADDS", 
                                      "A_ADD", "A_ADDS", "AADD", "AADDS",
                                      "VIRTUAL A", "VIRTUAL-A", "VIRTUAL_A", "VIRTUALA",
                                      "ANOTHER A", "ANOTHER-A", "ANOTHER_A", "ANOTHERA",
                                      "VIR A", "VIR-A", "VIR_A", "VIRA",
                                      "ANO A", "ANO-A", "ANO_A", "ANOA",
                                      "V A", "V-A", "V_A", "VA", 
                                      "A V", "A-V", "A_V", "AV", 
                                      "A A", "A-A", "A_A", "AA")
                    valid_va_bool = False
                    valid_va_num = -1
                    temp_str_list_1 = temp_str_list_0[0].split(",")
                    temp_len_0 = len(temp_str_list_1)
                    if temp_len_0 == 6:
                        for n in range(temp_len_0):
                            temp_str_0 = temp_str_list_1[n].strip()
                            temp_bool_1 = True
                            while temp_bool_1:
                                temp_len_1 = len(temp_str_0)
                                if temp_len_1 >= 2:
                                    temp_str_1 = temp_str_0[0]
                                    temp_str_2 = temp_str_0[temp_len_1-1]
                                    if (temp_str_1 == '"') & (temp_str_2 == '"'):
                                        temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                                    elif (temp_str_1 == "'") & (temp_str_2 == "'"):
                                        temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                                    else:
                                        temp_bool_1 = False
                                else:
                                    temp_bool_1 = False
                            temp_str_0 = temp_str_0.strip().upper()
                            if temp_str_0 in valid_gn_tuple:
                                if not valid_gn_bool:
                                    valid_gn_bool = True
                                    valid_gn_num = n
                                else:
                                    temp_bool_0 = False
                            elif temp_str_0 in valid_mn_tuple:
                                if not valid_mn_bool:
                                    valid_mn_bool = True
                                    valid_mn_num = n
                                else:
                                    temp_bool_0 = False
                            elif temp_str_0 in valid_fn_tuple:
                                if not valid_fn_bool:
                                    valid_fn_bool = True
                                    valid_fn_num = n
                                else:
                                    temp_bool_0 = False
                            elif temp_str_0 in valid_vt_tuple:
                                if not valid_vt_bool:
                                    valid_vt_bool = True
                                    valid_vt_num = n
                                else:
                                    temp_bool_0 = False
                            elif temp_str_0 in valid_vn_tuple:
                                if not valid_vn_bool:
                                    valid_vn_bool = True
                                    valid_vn_num = n
                                else:
                                    temp_bool_0 = False
                            elif temp_str_0 in valid_va_tuple:
                                if not valid_va_bool:
                                    valid_va_bool = True
                                    valid_va_num = n
                                else:
                                    temp_bool_0 = False
                            else:
                                temp_bool_0 = False
                            if not temp_bool_0:
                                break
                    elif temp_len_0 == 7:
                        for n in range(temp_len_0):
                            temp_str_0 = temp_str_list_1[n].strip()
                            temp_bool_1 = True
                            while temp_bool_1:
                                temp_len_1 = len(temp_str_0)
                                if temp_len_1 >= 2:
                                    temp_str_1 = temp_str_0[0]
                                    temp_str_2 = temp_str_0[temp_len_1-1]
                                    if (temp_str_1 == '"') & (temp_str_2 == '"'):
                                        temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                                    elif (temp_str_1 == "'") & (temp_str_2 == "'"):
                                        temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                                    else:
                                        temp_bool_1 = False
                                else:
                                    temp_bool_1 = False
                            temp_str_0 = temp_str_0.strip().upper()
                            if temp_str_0 in valid_index_tuple:
                                if not valid_index_bool:
                                    valid_index_bool = True
                                else:
                                    temp_bool_0 = False
                            elif temp_str_0 in valid_gn_tuple:
                                if not valid_gn_bool:
                                    valid_gn_bool = True
                                    valid_gn_num = n
                                else:
                                    temp_bool_0 = False
                            elif temp_str_0 in valid_mn_tuple:
                                if not valid_mn_bool:
                                    valid_mn_bool = True
                                    valid_mn_num = n
                                else:
                                    temp_bool_0 = False
                            elif temp_str_0 in valid_fn_tuple:
                                if not valid_fn_bool:
                                    valid_fn_bool = True
                                    valid_fn_num = n
                                else:
                                    temp_bool_0 = False
                            elif temp_str_0 in valid_vt_tuple:
                                if not valid_vt_bool:
                                    valid_vt_bool = True
                                    valid_vt_num = n
                                else:
                                    temp_bool_0 = False
                            elif temp_str_0 in valid_vn_tuple:
                                if not valid_vn_bool:
                                    valid_vn_bool = True
                                    valid_vn_num = n
                                else:
                                    temp_bool_1 = False
                            elif temp_str_0 in valid_va_tuple:
                                if not valid_va_bool:
                                    valid_va_bool = True
                                    valid_va_num = n
                                else:
                                    temp_bool_0 = False
                            else:
                                temp_bool_0 = False
                            if not temp_bool_0:
                                break
                    else:
                        temp_bool_0 = False
                    if temp_bool_0:
                        if (valid_gn_bool & valid_mn_bool & valid_fn_bool & 
                            valid_vt_bool & valid_vn_bool & valid_va_bool):                    
                            del(temp_str_list_0[0])
                            temp_len_1 = len(temp_str_list_0)
                            if temp_len_1 > 0:
                                for n in range(temp_len_1):
                                    temp_str_list_0[n] = temp_str_list_0[n].strip()     
                                if len(temp_str_list_0[temp_len_1-1]) < 1:
                                    del(temp_str_list_0[temp_len_1-1])
                                    temp_len_1 -= 1
                                if (temp_len_1 > 0) & (temp_len_1 <= 20000):
                                    self.cur_gene_import_csv_str_list = temp_str_list_0
                                    self.cur_gene_import_csv_title = (valid_gn_num, valid_mn_num, valid_fn_num, 
                                                                      valid_vt_num, valid_vn_num, valid_va_num)
                                    temp_str = "Ready. "
                                    temp_str = "There are "+str(temp_len_1)+" rows."
                                    self.gene_multiple_gene_state_0["text"] = temp_str
                                    self.gene_multiple_gene_progressbar_0["value"] = 0
                                    self.gene_multiple_gene_state_0_0["text"] = ""
                                    self.gene_multiple_gene_state_0_1["text"] = ""                        
                                    self.gene_multiple_gene_progressbar_1["value"] = 0
                                    self.gene_multiple_gene_state_1_0["text"] = ""
                                    self.gene_multiple_gene_state_1_1["text"] = ""                        
                                    self.gene_multiple_gene_progressbar_2["value"] = 0
                                    self.gene_multiple_gene_state_2_0["text"] = ""
                                    self.gene_multiple_gene_state_2_1["text"] = ""                    
                                    self.gene_multiple_gene_progressbar_3["value"] = 0
                                    self.gene_multiple_gene_state_3_0["text"] = ""
                                    self.gene_multiple_gene_state_3_1["text"] = ""
                                    self.gene_multiple_gene_state_2["text"] = file_path
                                else:
                                    showerror(title = "Error", 
                                              message = "The row number (excluding the first row, title row) should range within 1-20 000.") 
                            else:
                                showerror(title = "Error", 
                                          message = "The row number (excluding the first row, title row) should range within 1-20 000.") 
                        else:
                            showerror(title = "Error", 
                                      message = "The first row, title row is not readable.") 
                    else:
                        showerror(title = "Error", 
                                  message = "The first row, title row is not readable.") 
    
    def generate_fun_multiple_clean(self):
        if not self.cur_progress_bool:
            if ((not self.cur_gene_import_csv_str_list is None) | 
                (not self.cur_gene_import_csv_title is None)):
                answer = askyesno(title="Clean",
                                  message="Are you sure that you want to clean the imported *.csv file?")
                if answer:  
                    self.cur_gene_import_csv_str_list = None
                    self.cur_gene_import_csv_title = None
                    self.gene_multiple_gene_state_0["text"] = "No *.csv file is imported. "
                    self.gene_multiple_gene_progressbar_0["value"] = 0
                    self.gene_multiple_gene_state_0_0["text"] = ""
                    self.gene_multiple_gene_state_0_1["text"] = ""                        
                    self.gene_multiple_gene_progressbar_1["value"] = 0
                    self.gene_multiple_gene_state_1_0["text"] = ""
                    self.gene_multiple_gene_state_1_1["text"] = ""                        
                    self.gene_multiple_gene_progressbar_2["value"] = 0
                    self.gene_multiple_gene_state_2_0["text"] = ""
                    self.gene_multiple_gene_state_2_1["text"] = ""                    
                    self.gene_multiple_gene_progressbar_3["value"] = 0
                    self.gene_multiple_gene_state_3_0["text"] = ""
                    self.gene_multiple_gene_state_3_1["text"] = ""
                    self.gene_multiple_gene_state_2["text"] = ""
    
    def generate_fun_multiple_generate(self):
        if not self.cur_progress_bool:
            if os.path.exists(self.cur_org_file_name):
                with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                    read_text = read_file.read()
                    self.cur_org = self.reading_str_text_org(read_text)
                if not self.cur_org is None:
                    temp_num_0 = -1
                    for n in range(len(self.cur_org[2])):
                        if self.cur_org[2][n] == self.cur_mani_num:
                            temp_num_0 = n
                            break
                    if temp_num_0 >= 0:
                        temp_bool_0 = self.cur_org[3][temp_num_0]
                    else:
                        temp_bool_0 = False
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
            if not temp_bool_0:
                showerror(title = "Error", 
                          message = "No privilege to do so.") 
            else:
                if ((not self.cur_gene_import_csv_str_list is None) & 
                    (not self.cur_gene_import_csv_title is None)):
                    answer = askyesno(title="Generate",
                                      message="Are you sure that you want to start the generating process?")
                    if answer:  
                        temp_bool_1 = True
                        temp_file_list = os.scandir(self.basic_parameter[1][0])
                        for e in temp_file_list:
                            temp_str_0 = e.name
                            if len(temp_str_0) > 4:
                                temp_str_1 = temp_str_0[-4:].upper()
                                if (temp_str_1 == ".CSV") | (temp_str_1 == ".TXT"):
                                    temp_bool_1 = False
                                if temp_bool_1:
                                    if len(temp_str_0) > 5:
                                        temp_str_1 = temp_str_0[-5:].upper()
                                        if temp_str_1 == ".IDEN":
                                            temp_bool_1 = False
                            if not temp_bool_1:
                                break
                        if temp_bool_1:
                            for n in range(len(self.basic_parameter[1][1])):
                                temp_file_list = os.scandir(self.basic_parameter[1][1][n])
                                for e in temp_file_list:
                                    temp_str_0 = e.name
                                    if len(temp_str_0) > 4:
                                        temp_str_1 = temp_str_0[-4:].upper()
                                        if (temp_str_1 == ".CSV") | (temp_str_1 == ".TXT"):
                                            temp_bool_1 = False
                                        if temp_bool_1:
                                            if len(temp_str_0) > 5:
                                                temp_str_1 = temp_str_0[-5:].upper()
                                                if temp_str_1 == ".IDEN":
                                                    temp_bool_1 = False
                                    if not temp_bool_1:
                                        break
                                if not temp_bool_1:
                                    break
                        if not temp_bool_1:
                            showerror(title = "Error", 
                                      message = "There exists other *.iden or *.txt, *.csv in '"+self.basic_parameter[1][0]+"/', or its sub-folders.")
                        else:
                            self.cur_progress_bool = True
                            self.cur_multi_gene_bool = True
                            max_column_num = max(self.cur_gene_import_csv_title)+1
                            row_num = len(self.cur_gene_import_csv_str_list)
                            row_num_str = str(row_num)
                            temp_vt_capital = []
                            temp_vt_num = len(self.virtual_type)
                            for n in range(temp_vt_num):
                                temp_vt_capital.append(self.virtual_type[n].upper())
                            temp_vt_capital = tuple(temp_vt_capital)
                            temp_list_0 = []
                            temp_list_step_1 = []
                            temp_success_num = 0
                            temp_failure_num = 0
                            for n in range(row_num):
                                if self.cur_progress_bool:
                                    temp_bool_1 = True
                                    temp_list_1 = self.csv_row_read(self.cur_gene_import_csv_str_list[n])
                                    if len(temp_list_1) >= max_column_num:
                                        temp_str_0 = temp_list_1[self.cur_gene_import_csv_title[0]]
                                        temp_str_1 = temp_list_1[self.cur_gene_import_csv_title[1]]
                                        temp_str_2 = temp_list_1[self.cur_gene_import_csv_title[2]]
                                        temp_list_2 = [temp_str_0, temp_str_1, temp_str_2]
                                        temp_list_2 = self.English_name_change_quotation_mark(temp_list_2)
                                        if not temp_list_2 is None:
                                            temp_num_0 = -1
                                            temp_str_3 = temp_list_1[self.cur_gene_import_csv_title[3]].upper()
                                            for n1 in range(temp_vt_num):
                                                if temp_vt_capital[n1] == temp_str_3:
                                                    temp_num_0 = n1
                                                    break
                                            if temp_num_0 >= 0:
                                                temp_str_4 = temp_list_1[self.cur_gene_import_csv_title[4]]
                                                temp_str_5 = temp_list_1[self.cur_gene_import_csv_title[5]]
                                                temp_list_3 = [self.virtual_type[temp_num_0], temp_str_4, temp_str_5]
                                                temp_list_3 = self.virtual_name_change_quotation_mark(temp_list_3)
                                                temp_bool_1 = (not temp_list_3 is None)
                                            else:
                                                temp_bool_1 = False
                                        else:
                                            temp_bool_1 = False
                                    else:
                                        temp_bool_1 = False
                                    if temp_bool_1:
                                        if (len(temp_list_2[0]) > 0) | (len(temp_list_3[1]) > 0):
                                            temp_list_0.append((temp_list_2, temp_list_3))
                                            temp_list_step_1.append((temp_list_2[0], temp_list_2[2]))
                                            temp_success_num += 1
                                        else:
                                            temp_list_0.append(None)
                                            temp_list_step_1.append(None)
                                            temp_failure_num += 1
                                    else:
                                        temp_list_0.append(None)
                                        temp_list_step_1.append(None)
                                        temp_failure_num += 1
                                    temp_num_1 = n+1
                                    temp_float_1 = (temp_num_1/row_num)*100
                                    self.gene_multiple_gene_state_0_0["text"] = str(temp_num_1)+"/"+row_num_str
                                    self.gene_multiple_gene_state_0_1["text"] = str(round(temp_float_1, 2))+"%"
                                    self.gene_multiple_gene_progressbar_0["value"] = int(temp_float_1)
                                    self.update()
                                else:
                                    break
                            if self.cur_progress_bool:
                                self.gene_multiple_gene_state_0_0["text"] = "Valid: "+str(temp_success_num)
                                self.gene_multiple_gene_state_0_1["text"] = "Invalid: "+str(temp_failure_num)
                                temp_list_step_1 = self.number_mix_generate(temp_list_step_1, self.cur_org[0][3])
                            if self.cur_progress_bool:
                                temp_list_step_2 = []
                                for n in range(row_num):
                                    if self.cur_progress_bool:
                                        if not temp_list_step_1[n] is None:
                                            temp_list_1 = [temp_list_step_1[n][0], 
                                                           temp_list_0[n][0][0], 
                                                           temp_list_0[n][0][2], 
                                                           temp_list_0[n][1][1], 
                                                           self.cur_org[0][0], 
                                                           temp_list_step_1[n][4], 
                                                           temp_list_step_1[n][5]]
                                        else:
                                            temp_list_1 = None
                                        temp_list_step_2.append(temp_list_1)
                                    else:
                                        break
                            if self.cur_progress_bool:
                                temp_list_step_2 = self.number_member_generate(temp_list_step_2)
                            if self.cur_progress_bool:
                                temp_mix_num_list = []
                                temp_mem_num_list = []
                                temp_path_0 = self.basic_parameter[1][0]+"/"+"Report.csv"
                                temp_str_0 = chr(65279)
                                temp_str_0 = temp_str_0+'"'+"index"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"valid"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"iden file"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"mixed number"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"member number"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"given name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"middle name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"family name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"type of another name / virtual name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"another name / virtual name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"addition (@ or #)"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"date"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"time"+'"'
                                with open(temp_path_0, "w", encoding = "utf-8") as save_file:
                                    save_file.write(temp_str_0)
                                    save_file.close()
                                for n in range(row_num):
                                    if self.cur_progress_bool:
                                        temp_list_6 = [self.cur_org[0][0], self.cur_org[0][5][1], 
                                                       self.cur_org[0][5][2], self.cur_mani_num]
                                        if not temp_list_0[n] is None:
                                            temp_bool_2 = True
                                            if (not temp_list_step_2[n] is None):
                                                if ((temp_list_step_2[n][1] in temp_mix_num_list) | 
                                                    (temp_list_step_2[n][0] in temp_mem_num_list)):
                                                    temp_bool_2 = False
                                            else:
                                                temp_bool_2 = False
                                            if temp_bool_2:
                                                temp_list_2 = [temp_list_step_2[n][1], temp_list_step_2[n][0]]
                                                temp_mix_num_list.append(temp_list_2[0])
                                                temp_mem_num_list.append(temp_list_2[1])
                                                temp_list_3 = temp_list_0[n][0]
                                                temp_list_4 = temp_list_0[n][1]
                                                temp_list_5 = [temp_list_step_1[n][4], temp_list_step_1[n][5]]
                                                out_str_list_1 = self.forming_str_text_member_lang(temp_list_2, temp_list_3, 
                                                                                                   temp_list_4, temp_list_5, 
                                                                                                   temp_list_6, 
                                                                                                   self.basic_parameter[1][2][1], 
                                                                                                   self.basic_parameter[1][2][2], 
                                                                                                   self.basic_parameter[1][2][3])
                                                temp_str_1 = "Mem_"
                                                temp_str_1 = temp_str_1+temp_list_5[0][0]
                                                temp_str_1 = temp_str_1+temp_list_5[0][1]
                                                temp_str_1 = temp_str_1+temp_list_5[0][2]
                                                temp_str_1 = temp_str_1+temp_list_5[0][3]
                                                temp_str_1 = temp_str_1+temp_list_5[0][5]
                                                temp_str_1 = temp_str_1+temp_list_5[0][6]
                                                temp_str_1 = temp_str_1+temp_list_5[0][8]
                                                temp_str_1 = temp_str_1+temp_list_5[0][9]
                                                temp_str_1 = temp_str_1+temp_list_5[1][0]
                                                temp_str_1 = temp_str_1+temp_list_5[1][1]
                                                temp_str_1 = temp_str_1+temp_list_5[1][3]
                                                temp_str_1 = temp_str_1+temp_list_5[1][4]
                                                temp_str_1 = temp_str_1+"_"
                                                temp_str_1 = temp_str_1+temp_list_3[0]
                                                temp_str_1 = temp_str_1+"_"
                                                temp_str_1 = temp_str_1+temp_list_3[1]
                                                temp_str_1 = temp_str_1+"_"
                                                temp_str_1 = temp_str_1+temp_list_3[2]
                                                temp_str_1 = temp_str_1+"_"
                                                temp_str_1 = temp_str_1+temp_list_2[1]
                                                temp_str_1_0 = temp_str_1+".iden"
                                                temp_num_1 = n+1
                                                temp_str_2 = "\n"
                                                temp_str_2 = temp_str_2+str(temp_num_1)
                                                temp_str_2 = temp_str_2+","+"1"
                                                temp_str_2 = temp_str_2+","+temp_str_1_0
                                                temp_str_2 = temp_str_2+","+'"'+"'"+temp_list_2[0]+"'"+'"'
                                                temp_str_2 = temp_str_2+","+'"'+"'"+temp_list_2[1]+"'"+'"'
                                                temp_str_2 = temp_str_2+","+'"'+temp_list_3[0]+'"'
                                                temp_str_2 = temp_str_2+","+'"'+temp_list_3[1]+'"'
                                                temp_str_2 = temp_str_2+","+'"'+temp_list_3[2]+'"'
                                                temp_str_2 = temp_str_2+","+'"'+temp_list_4[0]+'"'
                                                temp_str_2 = temp_str_2+","+'"'+temp_list_4[1]+'"'
                                                temp_str_2 = temp_str_2+","+'"'+temp_list_4[2]+'"'
                                                temp_str_2 = temp_str_2+","+'"'+"'"+temp_list_5[0]+"'"+'"'
                                                temp_str_2 = temp_str_2+","+'"'+"'"+temp_list_5[1]+"'"+'"'
                                                temp_str_1_1 = self.basic_parameter[1][1][0]+"/"+temp_str_1_0
                                                with open(temp_str_1_1, "w", encoding = "utf-8") as save_file:
                                                    save_file.write(out_str_list_1[0])
                                                    save_file.close()
                                                if self.basic_parameter[1][2][1]:
                                                    temp_str_1_1 = temp_str_1+"_English.txt"
                                                    temp_str_1_1 = self.basic_parameter[1][1][1]+"/"+temp_str_1_1
                                                    with open(temp_str_1_1, "w", encoding = "utf-8") as save_file:
                                                        save_file.write(out_str_list_1[1])
                                                        save_file.close()
                                                if self.basic_parameter[1][2][2]:
                                                    temp_str_1_1 = temp_str_1+"_简体中文.txt"
                                                    temp_str_1_1 = self.basic_parameter[1][1][2]+"/"+temp_str_1_1
                                                    with open(temp_str_1_1, "w", encoding = "utf-8") as save_file:
                                                        save_file.write(out_str_list_1[2])
                                                        save_file.close()
                                                if self.basic_parameter[1][2][3]:
                                                    temp_str_1_1 = temp_str_1+"_正體中文.txt"
                                                    temp_str_1_1 = self.basic_parameter[1][1][3]+"/"+temp_str_1_1
                                                    with open(temp_str_1_1, "w", encoding = "utf-8") as save_file:
                                                        save_file.write(out_str_list_1[3])
                                                        save_file.close()
                                            else:  
                                                temp_list_2 = temp_list_0[n][0]
                                                temp_list_3 = temp_list_0[n][1]
                                                if (self.English_name_valid(temp_list_2)) & (self.virtual_name_valid(temp_list_3)):
                                                    if (len(temp_list_2[0]) > 0) | (len(temp_list_3[1]) > 0):
                                                        temp_bool_3 = True
                                                        temp_bool_2 = True
                                                    else:
                                                        temp_bool_3 = False
                                                        temp_bool_2 = False
                                                else:
                                                    temp_bool_3 = False
                                                    temp_bool_2 = False                                            
                                                while temp_bool_2:
                                                    temp_list_4 = self.number_mix_generate([[temp_list_2[0], temp_list_2[2]]], self.cur_org[0][3])
                                                    temp_list_4 = temp_list_4[0]
                                                    if not temp_list_4 is None:
                                                        if not temp_list_4[0] in temp_mix_num_list:
                                                            temp_list_5 = self.number_member_generate([[temp_list_4[0], temp_list_2[0], temp_list_2[2], 
                                                                                                        temp_list_3[1], self.cur_org[0][0], 
                                                                                                        temp_list_4[4], temp_list_4[5]]])
                                                            temp_list_5 = temp_list_5[0]
                                                            if not temp_list_5 is None:
                                                                if not temp_list_5[0] in temp_mem_num_list:
                                                                    temp_bool_2 = False
                                                if temp_bool_3:
                                                    temp_list_7 = [temp_list_5[1], temp_list_5[0]]
                                                    temp_mix_num_list.append(temp_list_7[0])
                                                    temp_mem_num_list.append(temp_list_7[1])
                                                    temp_list_8 = [temp_list_4[4], temp_list_4[5]]
                                                    out_str_list_1 = self.forming_str_text_member_lang(temp_list_7, temp_list_2, 
                                                                                                       temp_list_3, temp_list_8, 
                                                                                                       temp_list_6, 
                                                                                                       self.basic_parameter[1][2][1], 
                                                                                                       self.basic_parameter[1][2][2], 
                                                                                                       self.basic_parameter[1][2][3])
                                                    temp_str_1 = "Mem_"
                                                    temp_str_1 = temp_str_1+temp_list_8[0][0]
                                                    temp_str_1 = temp_str_1+temp_list_8[0][1]
                                                    temp_str_1 = temp_str_1+temp_list_8[0][2]
                                                    temp_str_1 = temp_str_1+temp_list_8[0][3]
                                                    temp_str_1 = temp_str_1+temp_list_8[0][5]
                                                    temp_str_1 = temp_str_1+temp_list_8[0][6]
                                                    temp_str_1 = temp_str_1+temp_list_8[0][8]
                                                    temp_str_1 = temp_str_1+temp_list_8[0][9]
                                                    temp_str_1 = temp_str_1+temp_list_8[1][0]
                                                    temp_str_1 = temp_str_1+temp_list_8[1][1]
                                                    temp_str_1 = temp_str_1+temp_list_8[1][3]
                                                    temp_str_1 = temp_str_1+temp_list_8[1][4]
                                                    temp_str_1 = temp_str_1+"_"
                                                    temp_str_1 = temp_str_1+temp_list_2[0]
                                                    temp_str_1 = temp_str_1+"_"
                                                    temp_str_1 = temp_str_1+temp_list_2[1]
                                                    temp_str_1 = temp_str_1+"_"
                                                    temp_str_1 = temp_str_1+temp_list_2[2]
                                                    temp_str_1 = temp_str_1+"_"
                                                    temp_str_1 = temp_str_1+temp_list_7[1]
                                                    temp_str_1_0 = temp_str_1+".iden"
                                                    temp_num_1 = n+1
                                                    temp_str_2 = "\n"
                                                    temp_str_2 = temp_str_2+str(temp_num_1)
                                                    temp_str_2 = temp_str_2+","+"1"
                                                    temp_str_2 = temp_str_2+","+temp_str_1_0
                                                    temp_str_2 = temp_str_2+","+'"'+"'"+temp_list_7[0]+"'"+'"'
                                                    temp_str_2 = temp_str_2+","+'"'+"'"+temp_list_7[1]+"'"+'"'
                                                    temp_str_2 = temp_str_2+","+'"'+temp_list_2[0]+'"'
                                                    temp_str_2 = temp_str_2+","+'"'+temp_list_2[1]+'"'
                                                    temp_str_2 = temp_str_2+","+'"'+temp_list_2[2]+'"'
                                                    temp_str_2 = temp_str_2+","+'"'+temp_list_3[0]+'"'
                                                    temp_str_2 = temp_str_2+","+'"'+temp_list_3[1]+'"'
                                                    temp_str_2 = temp_str_2+","+'"'+temp_list_3[2]+'"'
                                                    temp_str_2 = temp_str_2+","+'"'+"'"+temp_list_8[0]+"'"+'"'
                                                    temp_str_2 = temp_str_2+","+'"'+"'"+temp_list_8[1]+"'"+'"'
                                                    temp_str_1_1 = self.basic_parameter[1][1][0]+"/"+temp_str_1_0
                                                    with open(temp_str_1_1, "w", encoding = "utf-8") as save_file:
                                                        save_file.write(out_str_list_1[0])
                                                        save_file.close()
                                                    if self.basic_parameter[1][2][1]:
                                                        temp_str_1_1 = temp_str_1+"_English.txt"
                                                        temp_str_1_1 = self.basic_parameter[1][1][1]+"/"+temp_str_1_1
                                                        with open(temp_str_1_1, "w", encoding = "utf-8") as save_file:
                                                            save_file.write(out_str_list_1[1])
                                                            save_file.close()
                                                    if self.basic_parameter[1][2][2]:
                                                        temp_str_1_1 = temp_str_1+"_简体中文.txt"
                                                        temp_str_1_1 = self.basic_parameter[1][1][2]+"/"+temp_str_1_1
                                                        with open(temp_str_1_1, "w", encoding = "utf-8") as save_file:
                                                            save_file.write(out_str_list_1[2])
                                                            save_file.close()
                                                    if self.basic_parameter[1][2][3]:
                                                        temp_str_1_1 = temp_str_1+"_正體中文.txt"
                                                        temp_str_1_1 = self.basic_parameter[1][1][3]+"/"+temp_str_1_1
                                                        with open(temp_str_1_1, "w", encoding = "utf-8") as save_file:
                                                            save_file.write(out_str_list_1[3])
                                                            save_file.close()
                                                else:
                                                    temp_str_2 = "\n"
                                                    temp_str_2 = temp_str_2+str(n+1)
                                                    temp_str_2 = temp_str_2+","+"0"
                                                    for n1 in range(11):
                                                        temp_str_0 = temp_str_0+","
                                            with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                                save_file.write(temp_str_2)
                                                save_file.close()
                                            temp_float_1 = (temp_num_1/row_num)*100
                                            self.gene_multiple_gene_state_3_0["text"] = str(temp_num_1)+"/"+row_num_str
                                            self.gene_multiple_gene_state_3_1["text"] = str(round(temp_float_1, 2))+"%"
                                            self.gene_multiple_gene_progressbar_3["value"] = int(temp_float_1)
                                            self.gene_multiple_gene_state_2["text"] = temp_str_1_0
                                            self.update()                                            
                                        else:
                                            temp_str_0 = "\n"
                                            temp_str_0 = temp_str_0+str(n+1)
                                            temp_str_0 = temp_str_0+","+"0"
                                            for n1 in range(11):
                                                temp_str_0 = temp_str_0+","
                                            with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                                save_file.write(temp_str_0)
                                                save_file.close()
                                            temp_num_1 = n+1
                                            temp_float_1 = (temp_num_1/row_num)*100
                                            self.gene_multiple_gene_state_3_0["text"] = str(temp_num_1)+"/"+row_num_str
                                            self.gene_multiple_gene_state_3_1["text"] = str(round(temp_float_1, 2))+"%"
                                            self.gene_multiple_gene_progressbar_3["value"] = int(temp_float_1)
                                            self.gene_multiple_gene_state_2["text"] = temp_str_1_0
                                            self.update()      
                                    else:
                                        break
                                if self.cur_progress_bool:
                                    
                                    self.cur_progress_bool = False
                                    self.cur_multi_gene_bool = False
                                    self.gene_multiple_gene_state_0["text"] = "Finished. "                                
                                    self.gene_multiple_gene_state_2["text"] = "'"+temp_path_0+"' is output."
    
    def generate_fun_multiple_stop(self):
        if self.cur_progress_bool:
            answer = askyesno(title="Stop current process",
                              message="Are you sure that you want to stop the current process?")
            if answer:  
                self.cur_progress_bool = False
                self.cur_multi_gene_bool = False
                self.gene_multiple_gene_state_0["text"] = "Stopped. "
        
    def check_validity_page(self):
        check_valid_page_radio_frame = tk.LabelFrame(self.check_validity_page_frame, 
                                                     text = "Check validity: select a function", 
                                                     font = self.fonsize_s)
        check_valid_page_radio_frame.grid(row = 0, column = 0,
                                          padx = 5, pady = 5,
                                          sticky = tk.W)
        check_valid_page_radio_line_0 = tk.Frame(check_valid_page_radio_frame)
        check_valid_page_radio_line_0.grid(row = 0, column = 0,
                                           sticky = tk.W)
        check_valid_page_radio_line_1 = tk.Frame(check_valid_page_radio_frame)
        check_valid_page_radio_line_1.grid(row = 1, column = 0,
                                           sticky = tk.W)
        self.check_valid_page_radio_vari = tk.StringVar()
        self.check_valid_page_mix_num_radio = tk.Radiobutton(check_valid_page_radio_line_0, 
                                                             variable = self.check_valid_page_radio_vari, 
                                                             text = "Mixed number", 
                                                             value = "mix", 
                                                             font = self.fonsize_s)
        self.check_valid_page_mix_num_radio.grid(row = 0, column = 0,
                                                 padx = 2, pady = 2, 
                                                 sticky = tk.W)
        self.check_valid_page_mem_num_radio = tk.Radiobutton(check_valid_page_radio_line_0, 
                                                             variable = self.check_valid_page_radio_vari, 
                                                             text = "Member number", 
                                                             value = "mem", 
                                                             font = self.fonsize_s)
        self.check_valid_page_mem_num_radio.grid(row = 0, column = 1,
                                                 padx = 2, pady = 2, 
                                                 sticky = tk.W)
        self.check_valid_page_org_num_radio = tk.Radiobutton(check_valid_page_radio_line_0, 
                                                             variable = self.check_valid_page_radio_vari, 
                                                             text = "Organization number", 
                                                             value = "org", 
                                                             font = self.fonsize_s)
        self.check_valid_page_org_num_radio.grid(row = 0, column = 2,
                                                 padx = 2, pady = 2, 
                                                 sticky = tk.W)
        self.check_valid_page_mani_num_radio = tk.Radiobutton(check_valid_page_radio_line_0, 
                                                              variable = self.check_valid_page_radio_vari, 
                                                              text = "Manipulation number", 
                                                              value = "mani", 
                                                              font = self.fonsize_s)
        self.check_valid_page_mani_num_radio.grid(row = 0, column = 3,
                                                  padx = 2, pady = 2, 
                                                  sticky = tk.W)
        ##command
        self.check_valid_page_mix_num_radio["command"] = self.check_valid_fun_select
        self.check_valid_page_mem_num_radio["command"] = self.check_valid_fun_select
        self.check_valid_page_org_num_radio["command"] = self.check_valid_fun_select
        self.check_valid_page_mani_num_radio["command"] = self.check_valid_fun_select
        
        # mix
        self.check_valid_page_mix_num_frame = tk.Frame(self.check_validity_page_frame)
        self.check_valid_page_mix_num_frame.grid(row = 1, column = 0,
                                                 padx = 5, pady = 5,
                                                 sticky = tk.W)
        check_valid_page_mix_num_frame_single = tk.Frame(self.check_valid_page_mix_num_frame)
        check_valid_page_mix_num_frame_single.grid(row = 0, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        check_valid_page_mix_num_frame_line_0 = tk.Frame(check_valid_page_mix_num_frame_single)
        check_valid_page_mix_num_frame_line_0.grid(row = 0, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_mix_num_frame_line_0, 
                  text = "1. Mixed number: ",                          
                  font = self.fonsize_m).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.check_valid_mix_num_main_entry_vari = tk.StringVar()
        self.check_valid_mix_num_main_entry = tk.Entry(check_valid_page_mix_num_frame_line_0, 
                                                       textvariable = self.check_valid_mix_num_main_entry_vari, 
                                                       width = 23, 
                                                       font = self.fonsize_m)
        self.check_valid_mix_num_main_entry.grid(row = 0, column = 1,
                                                 sticky = tk.W)
        self.check_valid_mix_num_check_button = tk.Button(check_valid_page_mix_num_frame_line_0, 
                                                          text = "Check", 
                                                          width = 7, 
                                                          font = self.fonsize_m, 
                                                          foreground = "green", 
                                                          activeforeground = "green")        
        self.check_valid_mix_num_check_button.grid(row = 0, column = 2)
        self.check_valid_mix_num_clean_button = tk.Button(check_valid_page_mix_num_frame_line_0, 
                                                         text = "Clean", 
                                                         width = 7, 
                                                         font = self.fonsize_s)        
        self.check_valid_mix_num_clean_button.grid(row = 0, column = 3)
        self.check_valid_mix_num_single_state = ttk.Label(check_valid_page_mix_num_frame_line_0, 
                                                          text = "",                          
                                                          font = self.fonsize_s)
        self.check_valid_mix_num_single_state.grid(row = 0, column = 4,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_mix_num_frame_single, 
                  text = "Note: it is not necessary that all the following blanks are filled.",
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.W)
        check_valid_page_mix_num_frame_line_1 = tk.Frame(check_valid_page_mix_num_frame_single)
        check_valid_page_mix_num_frame_line_1.grid(row = 2, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_mix_num_frame_line_1, 
                  text = " (1) English given name: ",                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.check_valid_mix_num_gn_entry_vari = tk.StringVar()
        self.check_valid_mix_num_gn_entry = tk.Entry(check_valid_page_mix_num_frame_line_1, 
                                                     textvariable = self.check_valid_mix_num_gn_entry_vari, 
                                                     width = 14, 
                                                     font = self.fonsize_s)
        self.check_valid_mix_num_gn_entry.grid(row = 0, column = 1,
                                               sticky = tk.W)
        ttk.Label(check_valid_page_mix_num_frame_line_1, 
                  text = " (2) English family name: ",                          
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        self.check_valid_mix_num_fn_entry_vari = tk.StringVar()
        self.check_valid_mix_num_fn_entry = tk.Entry(check_valid_page_mix_num_frame_line_1, 
                                                     textvariable = self.check_valid_mix_num_fn_entry_vari, 
                                                     width = 14, 
                                                     font = self.fonsize_s)
        self.check_valid_mix_num_fn_entry.grid(row = 0, column = 3,
                                               sticky = tk.W)
        check_valid_page_mix_num_frame_line_2 = tk.Frame(check_valid_page_mix_num_frame_single)
        check_valid_page_mix_num_frame_line_2.grid(row = 3, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_mix_num_frame_line_2, 
                  text = " (3) Issued date (UTC): ",                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        check_valid_page_mix_num_frame_line_2_date = tk.Frame(check_valid_page_mix_num_frame_line_2)
        check_valid_page_mix_num_frame_line_2_date.grid(row = 0, column = 1,
                                                        padx = 2, pady = 2,
                                                        sticky = tk.W)
        ttk.Label(check_valid_page_mix_num_frame_line_2_date, 
                  text = "Year", 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.N)
        self.check_valid_mix_num_year_entry_vari = tk.StringVar()
        self.check_valid_mix_num_year_entry = tk.Entry(check_valid_page_mix_num_frame_line_2_date, 
                                                       textvariable = self.check_valid_mix_num_year_entry_vari, 
                                                       width = 6, 
                                                       font = self.fonsize_s)
        self.check_valid_mix_num_year_entry.grid(row = 1, column = 0,
                                                 sticky = tk.N)
        ttk.Label(check_valid_page_mix_num_frame_line_2_date, 
                  text = "-",                          
                  font = self.fonsize_s).grid(row = 1, column = 1,
                                              sticky = tk.N)
        ttk.Label(check_valid_page_mix_num_frame_line_2_date, 
                  text = "Month",                          
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.N)
        self.check_valid_mix_num_month_entry_vari = tk.StringVar()
        self.check_valid_mix_num_month_entry = tk.Entry(check_valid_page_mix_num_frame_line_2_date, 
                                                        textvariable = self.check_valid_mix_num_month_entry_vari, 
                                                        width = 4, 
                                                        font = self.fonsize_s)
        self.check_valid_mix_num_month_entry.grid(row = 1, column = 2,
                                                  sticky = tk.N)
        ttk.Label(check_valid_page_mix_num_frame_line_2_date, 
                  text = "-",                          
                  font = self.fonsize_s).grid(row = 1, column = 3,
                                              sticky = tk.N)
        ttk.Label(check_valid_page_mix_num_frame_line_2_date, 
                  text = "Day",                          
                  font = self.fonsize_s).grid(row = 0, column = 4,
                                              sticky = tk.N)
        self.check_valid_mix_num_day_entry_vari = tk.StringVar()
        self.check_valid_mix_num_day_entry = tk.Entry(check_valid_page_mix_num_frame_line_2_date, 
                                                      textvariable = self.check_valid_mix_num_day_entry_vari, 
                                                      width = 4, 
                                                      font = self.fonsize_s)
        self.check_valid_mix_num_day_entry.grid(row = 1, column = 4,
                                                sticky = tk.N)
        ttk.Label(check_valid_page_mix_num_frame_line_2, 
                  text = " (4) Issued time (UTC): ",                          
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        check_valid_page_mix_num_frame_line_2_time = tk.Frame(check_valid_page_mix_num_frame_line_2)
        check_valid_page_mix_num_frame_line_2_time.grid(row = 0, column = 3,
                                                        padx = 2, pady = 2,
                                                        sticky = tk.W)
        ttk.Label(check_valid_page_mix_num_frame_line_2_time, 
                  text = "Hour",                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.N)
        self.check_valid_mix_num_hour_entry_vari = tk.StringVar()
        self.check_valid_mix_num_hour_entry = tk.Entry(check_valid_page_mix_num_frame_line_2_time, 
                                                       textvariable = self.check_valid_mix_num_hour_entry_vari, 
                                                       width = 4, 
                                                       font = self.fonsize_s)
        self.check_valid_mix_num_hour_entry.grid(row = 1, column = 0,
                                                 sticky = tk.N)
        ttk.Label(check_valid_page_mix_num_frame_line_2_time, 
                  text = ":",                          
                  font = self.fonsize_s).grid(row = 1, column = 1,
                                              sticky = tk.N)
        ttk.Label(check_valid_page_mix_num_frame_line_2_time, 
                  text = "Minute",                          
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.N)
        self.check_valid_mix_num_minute_entry_vari = tk.StringVar()
        self.check_valid_mix_num_minute_entry = tk.Entry(check_valid_page_mix_num_frame_line_2_time, 
                                                         textvariable = self.check_valid_mix_num_minute_entry_vari, 
                                                         width = 4, 
                                                         font = self.fonsize_s)
        self.check_valid_mix_num_minute_entry.grid(row = 1, column = 2,
                                                   sticky = tk.N)
        ttk.Separator(self.check_valid_page_mix_num_frame, 
                      orient="horizontal").grid(row = 1, column = 0, 
                                                sticky = tk.EW) 
        check_valid_page_mix_num_frame_multiple = tk.Frame(self.check_valid_page_mix_num_frame)
        check_valid_page_mix_num_frame_multiple.grid(row = 2, column = 0,
                                                     padx = 2, pady = 2,
                                                     sticky = tk.W)
        check_valid_page_mix_num_frame_multiple_line_0 = tk.Frame(check_valid_page_mix_num_frame_multiple)
        check_valid_page_mix_num_frame_multiple_line_0.grid(row = 0, column = 0,
                                                            padx = 2, pady = 2,
                                                            sticky = tk.W)
        self.check_valid_mix_num_multi_check_button = tk.Button(check_valid_page_mix_num_frame_multiple_line_0, 
                                                                text = "To check from *.csv file", 
                                                                width = 26, 
                                                                font = self.fonsize_m)        
        self.check_valid_mix_num_multi_check_button.grid(row = 0, column = 0,
                                                         padx = 2, pady = 2,
                                                         sticky = tk.W)
        self.check_valid_mix_num_multiple_state = ttk.Label(check_valid_page_mix_num_frame_multiple_line_0, 
                                                            text = "",                          
                                                            font = self.fonsize_s)
        self.check_valid_mix_num_multiple_state.grid(row = 0, column = 1,
                                                     padx = 2, pady = 2,
                                                     sticky = tk.W)
        check_valid_page_mix_num_frame_multiple_line_1 = tk.Frame(check_valid_page_mix_num_frame_multiple)
        check_valid_page_mix_num_frame_multiple_line_1.grid(row = 1, column = 0,
                                                            padx = 2, pady = 2,
                                                            sticky = tk.W)
        temp_str = "(1) In the first row, title row of the *.csv file, there is 1 required cell, \"Mixed Numbers\" or \"Mix\" , and 7 optional cells (regardless capital or small letters): "
        temp_str = temp_str+"(i) \"Given Names\" or \"GN\", "
        temp_str = temp_str+"(ii) \"Family Names\" or \"FN\", "
        temp_str = temp_str+"(iii) \"Issued Year\" or \"Iss Y\", "
        temp_str = temp_str+"(iv) \"Issued Month\" or \"Iss M\", "
        temp_str = temp_str+"(v) \"Issued Day\" or \"Iss D\", "
        temp_str = temp_str+"(vi) \"Issued Hour\" or \"Iss H\", "
        temp_str = temp_str+"(vii) \"Issued Minute\" or \"Iss Min\"."
        ttk.Label(check_valid_page_mix_num_frame_multiple_line_1, 
                  text = temp_str,
                  wraplength = 1100, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.NW) 
        temp_str = "(2) The max row number (excluding first row, title row) is 1 000."
        ttk.Label(check_valid_page_mix_num_frame_multiple_line_1, 
                  text = temp_str,
                  wraplength = 1100, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.NW) 
        ## command 
        self.check_valid_mix_num_check_button["command"] = self.check_valid_fun_mix_num_check
        self.check_valid_mix_num_clean_button["command"] = self.check_valid_fun_mix_num_clean
        self.check_valid_mix_num_multi_check_button["command"] = self.check_valid_fun_mix_num_multiple_check
        
        # mem
        self.check_valid_page_mem_num_frame = tk.Frame(self.check_validity_page_frame)
        self.check_valid_page_mem_num_frame.grid(row = 1, column = 0,
                                                 padx = 5, pady = 5,
                                                 sticky = tk.W)
        check_valid_page_mem_num_frame_single = tk.Frame(self.check_valid_page_mem_num_frame)
        check_valid_page_mem_num_frame_single.grid(row = 0, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        check_valid_page_mem_num_frame_line_0 = tk.Frame(check_valid_page_mem_num_frame_single)
        check_valid_page_mem_num_frame_line_0.grid(row = 0, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_mem_num_frame_line_0, 
                  text = "2. Member number: ",                          
                  font = self.fonsize_m).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.check_valid_mem_num_main_entry_vari = tk.StringVar()
        self.check_valid_mem_num_main_entry = tk.Entry(check_valid_page_mem_num_frame_line_0, 
                                                       textvariable = self.check_valid_mem_num_main_entry_vari, 
                                                       width = 16, 
                                                       font = self.fonsize_m)
        self.check_valid_mem_num_main_entry.grid(row = 0, column = 1,
                                                 sticky = tk.W)
        self.check_valid_mem_num_check_button = tk.Button(check_valid_page_mem_num_frame_line_0, 
                                                          text = "Check", 
                                                          width = 7, 
                                                          font = self.fonsize_m, 
                                                          foreground = "green", 
                                                          activeforeground = "green")        
        self.check_valid_mem_num_check_button.grid(row = 0, column = 2)
        self.check_valid_mem_num_clean_button = tk.Button(check_valid_page_mem_num_frame_line_0, 
                                                         text = "Clean", 
                                                         width = 7, 
                                                         font = self.fonsize_s)        
        self.check_valid_mem_num_clean_button.grid(row = 0, column = 3)
        self.check_valid_mem_num_single_state = ttk.Label(check_valid_page_mem_num_frame_line_0, 
                                                          text = "",                          
                                                          font = self.fonsize_s)
        self.check_valid_mem_num_single_state.grid(row = 0, column = 4,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_mem_num_frame_single, 
                  text = "Note: it is not necessary that all the following blanks are filled.",
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.W)
        check_valid_page_mem_num_frame_line_1 = tk.Frame(check_valid_page_mem_num_frame_single)
        check_valid_page_mem_num_frame_line_1.grid(row = 2, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_mem_num_frame_line_1, 
                  text = " (1) Mixed number: ",                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.check_valid_mem_num_mix_entry_vari = tk.StringVar()
        self.check_valid_mem_num_mix_entry = tk.Entry(check_valid_page_mem_num_frame_line_1, 
                                                      textvariable = self.check_valid_mem_num_mix_entry_vari, 
                                                      width = 23, 
                                                      font = self.fonsize_s)
        self.check_valid_mem_num_mix_entry.grid(row = 0, column = 1,
                                                sticky = tk.W)
        check_valid_page_mem_num_frame_line_2 = tk.Frame(check_valid_page_mem_num_frame_single)
        check_valid_page_mem_num_frame_line_2.grid(row = 3, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_mem_num_frame_line_2, 
                  text = " (2) Issuer's organization number': ",                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.check_valid_mem_num_org_entry_vari = tk.StringVar()
        self.check_valid_mem_num_org_entry = tk.Entry(check_valid_page_mem_num_frame_line_2, 
                                                      textvariable = self.check_valid_mem_num_org_entry_vari, 
                                                      width = 16, 
                                                      font = self.fonsize_s)
        self.check_valid_mem_num_org_entry.grid(row = 0, column = 1,
                                                sticky = tk.W)
        check_valid_page_mem_num_frame_line_3 = tk.Frame(check_valid_page_mem_num_frame_single)
        check_valid_page_mem_num_frame_line_3.grid(row = 4, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_mem_num_frame_line_3, 
                  text = " (3) Another name / virtual name: ",                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.check_valid_mem_num_vn_entry_vari = tk.StringVar()
        self.check_valid_mem_num_vn_entry = tk.Entry(check_valid_page_mem_num_frame_line_3, 
                                                     textvariable = self.check_valid_mem_num_vn_entry_vari, 
                                                     width = 14, 
                                                     font = self.fonsize_s)
        self.check_valid_mem_num_vn_entry.grid(row = 0, column = 1,
                                               sticky = tk.W)
        ttk.Separator(self.check_valid_page_mem_num_frame, 
                      orient="horizontal").grid(row = 1, column = 0, 
                                                sticky = tk.EW) 
        check_valid_page_mem_num_frame_multiple = tk.Frame(self.check_valid_page_mem_num_frame)
        check_valid_page_mem_num_frame_multiple.grid(row = 2, column = 0,
                                                     padx = 2, pady = 2,
                                                     sticky = tk.W)
        check_valid_page_mem_num_frame_multiple_line_0 = tk.Frame(check_valid_page_mem_num_frame_multiple)
        check_valid_page_mem_num_frame_multiple_line_0.grid(row = 0, column = 0,
                                                            padx = 2, pady = 2,
                                                            sticky = tk.W)
        self.check_valid_mem_num_multi_check_button = tk.Button(check_valid_page_mem_num_frame_multiple_line_0, 
                                                                text = "To check from *.csv file", 
                                                                width = 26, 
                                                                font = self.fonsize_m)        
        self.check_valid_mem_num_multi_check_button.grid(row = 0, column = 0,
                                                         padx = 2, pady = 2,
                                                         sticky = tk.W)
        self.check_valid_mem_num_multiple_state = ttk.Label(check_valid_page_mem_num_frame_multiple_line_0, 
                                                            text = "",                          
                                                            font = self.fonsize_s)
        self.check_valid_mem_num_multiple_state.grid(row = 0, column = 1,
                                                     padx = 2, pady = 2,
                                                     sticky = tk.W)
        check_valid_page_mem_num_frame_multiple_line_1 = tk.Frame(check_valid_page_mem_num_frame_multiple)
        check_valid_page_mem_num_frame_multiple_line_1.grid(row = 1, column = 0,
                                                            padx = 2, pady = 2,
                                                            sticky = tk.W)
        temp_str = "(1) In the first row, title row of the *.csv file, there is 1 required cell, \"Member Numbers\" or \"Mem\" , and 3 optional cells (regardless capital or small letters): "
        temp_str = temp_str+"(i) \"Mixed Numbers\" or \"Mix\", "
        temp_str = temp_str+"(ii) \"Organization Numbers\" or \"Org\", "
        temp_str = temp_str+"(iii) \"Another Names\" or \"Virtual Names\" or \"AN\" or \"VN\"."
        ttk.Label(check_valid_page_mem_num_frame_multiple_line_1, 
                  text = temp_str,
                  wraplength = 1100, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.NW) 
        temp_str = "(2) The max row number (excluding first row, title row) is 1 000."
        ttk.Label(check_valid_page_mem_num_frame_multiple_line_1, 
                  text = temp_str,
                  wraplength = 1100, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.NW) 
        ## command 
        self.check_valid_mem_num_check_button["command"] = self.check_valid_fun_mem_num_check
        self.check_valid_mem_num_clean_button["command"] = self.check_valid_fun_mem_num_clean
        self.check_valid_mem_num_multi_check_button["command"] = self.check_valid_fun_mem_num_multiple_check
        
        # org
        self.check_valid_page_org_num_frame = tk.Frame(self.check_validity_page_frame)
        self.check_valid_page_org_num_frame.grid(row = 1, column = 0,
                                                 padx = 5, pady = 5,
                                                 sticky = tk.W)
        check_valid_page_org_num_frame_single = tk.Frame(self.check_valid_page_org_num_frame)
        check_valid_page_org_num_frame_single.grid(row = 0, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        check_valid_page_org_num_frame_line_0 = tk.Frame(check_valid_page_org_num_frame_single)
        check_valid_page_org_num_frame_line_0.grid(row = 0, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_org_num_frame_line_0, 
                  text = "3. Organization number: ",                          
                  font = self.fonsize_m).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.check_valid_org_num_main_entry_vari = tk.StringVar()
        self.check_valid_org_num_main_entry = tk.Entry(check_valid_page_org_num_frame_line_0, 
                                                       textvariable = self.check_valid_org_num_main_entry_vari, 
                                                       width = 16, 
                                                       font = self.fonsize_m)
        self.check_valid_org_num_main_entry.grid(row = 0, column = 1,
                                                 sticky = tk.W)
        self.check_valid_org_num_check_button = tk.Button(check_valid_page_org_num_frame_line_0, 
                                                          text = "Check", 
                                                          width = 7, 
                                                          font = self.fonsize_m, 
                                                          foreground = "green", 
                                                          activeforeground = "green")        
        self.check_valid_org_num_check_button.grid(row = 0, column = 2)
        self.check_valid_org_num_clean_button = tk.Button(check_valid_page_org_num_frame_line_0, 
                                                         text = "Clean", 
                                                         width = 7, 
                                                         font = self.fonsize_s)        
        self.check_valid_org_num_clean_button.grid(row = 0, column = 3)
        self.check_valid_org_num_single_state = ttk.Label(check_valid_page_org_num_frame_line_0, 
                                                          text = "",                          
                                                          font = self.fonsize_s)
        self.check_valid_org_num_single_state.grid(row = 0, column = 4,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_org_num_frame_single, 
                  text = "Note: it is not necessary that all the following blanks are filled.",
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.W)
        check_valid_page_org_num_frame_line_1 = tk.Frame(check_valid_page_org_num_frame_single)
        check_valid_page_org_num_frame_line_1.grid(row = 3, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(check_valid_page_org_num_frame_line_1, 
                  text = " (1) Created date (UTC): ",                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        check_valid_page_org_num_frame_line_1_date = tk.Frame(check_valid_page_org_num_frame_line_1)
        check_valid_page_org_num_frame_line_1_date.grid(row = 0, column = 1,
                                                        padx = 2, pady = 2,
                                                        sticky = tk.W)
        ttk.Label(check_valid_page_org_num_frame_line_1_date, 
                  text = "Year",                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.N)
        self.check_valid_org_num_year_entry_vari = tk.StringVar()
        self.check_valid_org_num_year_entry = tk.Entry(check_valid_page_org_num_frame_line_1_date, 
                                                       textvariable = self.check_valid_org_num_year_entry_vari, 
                                                       width = 6, 
                                                       font = self.fonsize_s)
        self.check_valid_org_num_year_entry.grid(row = 1, column = 0,
                                                 sticky = tk.N)
        ttk.Label(check_valid_page_org_num_frame_line_1_date, 
                  text = "-",                          
                  font = self.fonsize_s).grid(row = 1, column = 1,
                                              sticky = tk.N)
        ttk.Label(check_valid_page_org_num_frame_line_1_date, 
                  text = "Month",                          
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.N)
        self.check_valid_org_num_month_entry_vari = tk.StringVar()
        self.check_valid_org_num_month_entry = tk.Entry(check_valid_page_org_num_frame_line_1_date, 
                                                        textvariable = self.check_valid_org_num_month_entry_vari, 
                                                        width = 4, 
                                                        font = self.fonsize_s)
        self.check_valid_org_num_month_entry.grid(row = 1, column = 2,
                                                  sticky = tk.N)
        ttk.Label(check_valid_page_org_num_frame_line_1_date, 
                  text = "-",                          
                  font = self.fonsize_s).grid(row = 1, column = 3,
                                              sticky = tk.N)
        ttk.Label(check_valid_page_org_num_frame_line_1_date, 
                  text = "Day",                          
                  font = self.fonsize_s).grid(row = 0, column = 4,
                                              sticky = tk.N)
        self.check_valid_org_num_day_entry_vari = tk.StringVar()
        self.check_valid_org_num_day_entry = tk.Entry(check_valid_page_org_num_frame_line_1_date, 
                                                      textvariable = self.check_valid_org_num_day_entry_vari, 
                                                      width = 4, 
                                                      font = self.fonsize_s)
        self.check_valid_org_num_day_entry.grid(row = 1, column = 4,
                                                sticky = tk.N)
        ttk.Label(check_valid_page_org_num_frame_line_1, 
                  text = " (2) Created time (UTC): ",                          
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        check_valid_page_org_num_frame_line_1_time = tk.Frame(check_valid_page_org_num_frame_line_1)
        check_valid_page_org_num_frame_line_1_time.grid(row = 0, column = 3,
                                                        padx = 2, pady = 2,
                                                        sticky = tk.W)
        ttk.Label(check_valid_page_org_num_frame_line_1_time, 
                  text = "Hour",                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.N)
        self.check_valid_org_num_hour_entry_vari = tk.StringVar()
        self.check_valid_org_num_hour_entry = tk.Entry(check_valid_page_org_num_frame_line_1_time, 
                                                       textvariable = self.check_valid_org_num_hour_entry_vari, 
                                                       width = 4, 
                                                       font = self.fonsize_s)
        self.check_valid_org_num_hour_entry.grid(row = 1, column = 0,
                                                 sticky = tk.N)
        ttk.Label(check_valid_page_org_num_frame_line_1_time, 
                  text = ":",                          
                  font = self.fonsize_s).grid(row = 1, column = 1,
                                              sticky = tk.N)
        ttk.Label(check_valid_page_org_num_frame_line_1_time, 
                  text = "Minute",                          
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.N)
        self.check_valid_org_num_minute_entry_vari = tk.StringVar()
        self.check_valid_org_num_minute_entry = tk.Entry(check_valid_page_org_num_frame_line_1_time, 
                                                         textvariable = self.check_valid_org_num_minute_entry_vari, 
                                                         width = 4, 
                                                         font = self.fonsize_s)
        self.check_valid_org_num_minute_entry.grid(row = 1, column = 2,
                                                   sticky = tk.N)
        ttk.Separator(self.check_valid_page_org_num_frame, 
                      orient="horizontal").grid(row = 1, column = 0, 
                                                sticky = tk.EW) 
        check_valid_page_org_num_frame_multiple = tk.Frame(self.check_valid_page_org_num_frame)
        check_valid_page_org_num_frame_multiple.grid(row = 2, column = 0,
                                                     padx = 2, pady = 2,
                                                     sticky = tk.W)
        check_valid_page_org_num_frame_multiple_line_0 = tk.Frame(check_valid_page_org_num_frame_multiple)
        check_valid_page_org_num_frame_multiple_line_0.grid(row = 0, column = 0,
                                                            padx = 2, pady = 2,
                                                            sticky = tk.W)
        self.check_valid_org_num_multi_check_button = tk.Button(check_valid_page_org_num_frame_multiple_line_0, 
                                                                text = "To check from *.csv file", 
                                                                width = 26, 
                                                                font = self.fonsize_m)        
        self.check_valid_org_num_multi_check_button.grid(row = 0, column = 0,
                                                         padx = 2, pady = 2,
                                                         sticky = tk.W)
        self.check_valid_org_num_multiple_state = ttk.Label(check_valid_page_org_num_frame_multiple_line_0, 
                                                            text = "",                          
                                                            font = self.fonsize_s)
        self.check_valid_org_num_multiple_state.grid(row = 0, column = 1,
                                                     padx = 2, pady = 2,
                                                     sticky = tk.W)
        check_valid_page_org_num_frame_multiple_line_1 = tk.Frame(check_valid_page_org_num_frame_multiple)
        check_valid_page_org_num_frame_multiple_line_1.grid(row = 1, column = 0,
                                                            padx = 2, pady = 2,
                                                            sticky = tk.W)
        temp_str = "(1) In the first row, title row of the *.csv file, there is 1 required cell, \"Organization Numbers\" or \"Org\" , and 5 optional cells (regardless capital or small letters): "
        temp_str = temp_str+"(i) \"Created Year\" or \"Cre Y\", "
        temp_str = temp_str+"(ii) \"Created Month\" or \"Cre M\", "
        temp_str = temp_str+"(iii) \"Created Day\" or \"Cre D\", "
        temp_str = temp_str+"(iv) \"Created Hour\" or \"Cre H\", "
        temp_str = temp_str+"(v) \"Created Minute\" or \"Cre Min\"."
        ttk.Label(check_valid_page_org_num_frame_multiple_line_1, 
                  text = temp_str,
                  wraplength = 1100, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.NW) 
        temp_str = "(2) The max row number (excluding first row, title row) is 1 000."
        ttk.Label(check_valid_page_org_num_frame_multiple_line_1, 
                  text = temp_str,
                  wraplength = 1100, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.NW) 
        ## command 
        self.check_valid_org_num_check_button["command"] = self.check_valid_fun_org_num_check
        self.check_valid_org_num_clean_button["command"] = self.check_valid_fun_org_num_clean
        self.check_valid_org_num_multi_check_button["command"] = self.check_valid_fun_org_num_multiple_check
        
        # mani
        self.check_valid_page_mani_num_frame = tk.Frame(self.check_validity_page_frame)
        self.check_valid_page_mani_num_frame.grid(row = 1, column = 0,
                                                  padx = 5, pady = 5,
                                                  sticky = tk.W)        
        check_valid_page_mani_num_frame_single = tk.Frame(self.check_valid_page_mani_num_frame)
        check_valid_page_mani_num_frame_single.grid(row = 0, column = 0,
                                                    padx = 2, pady = 2,
                                                    sticky = tk.W)
        check_valid_page_mani_num_frame_line_0 = tk.Frame(check_valid_page_mani_num_frame_single)
        check_valid_page_mani_num_frame_line_0.grid(row = 0, column = 0,
                                                    padx = 2, pady = 2,
                                                    sticky = tk.W)
        ttk.Label(check_valid_page_mani_num_frame_line_0, 
                  text = "4. Manipulation number: ",                          
                  font = self.fonsize_m).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.check_valid_mani_num_main_entry_vari = tk.StringVar()
        self.check_valid_mani_num_main_entry = tk.Entry(check_valid_page_mani_num_frame_line_0, 
                                                        textvariable = self.check_valid_mani_num_main_entry_vari, 
                                                        width = 9, 
                                                        font = self.fonsize_m)
        self.check_valid_mani_num_main_entry.grid(row = 0, column = 1,
                                                  sticky = tk.W)
        self.check_valid_mani_num_check_button = tk.Button(check_valid_page_mani_num_frame_line_0, 
                                                           text = "Check", 
                                                           width = 7, 
                                                           font = self.fonsize_m, 
                                                           foreground = "green", 
                                                           activeforeground = "green")        
        self.check_valid_mani_num_check_button.grid(row = 0, column = 2)
        self.check_valid_mani_num_clean_button = tk.Button(check_valid_page_mani_num_frame_line_0, 
                                                           text = "Clean", 
                                                           width = 7, 
                                                           font = self.fonsize_s)        
        self.check_valid_mani_num_clean_button.grid(row = 0, column = 3)
        self.check_valid_mani_num_single_state = ttk.Label(check_valid_page_mani_num_frame_line_0, 
                                                           text = "",                          
                                                           font = self.fonsize_s)
        self.check_valid_mani_num_single_state.grid(row = 0, column = 4,
                                                    padx = 2, pady = 2,
                                                    sticky = tk.W)
        ttk.Label(check_valid_page_mani_num_frame_single, 
                  text = "Note: the organization number is required.",
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.W)
        check_valid_page_mani_num_frame_line_1 = tk.Frame(check_valid_page_mani_num_frame_single)
        check_valid_page_mani_num_frame_line_1.grid(row = 2, column = 0,
                                                    padx = 2, pady = 2,
                                                    sticky = tk.W)
        ttk.Label(check_valid_page_mani_num_frame_line_1, 
                  text = " (1) Organization number: ",                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.check_valid_mani_num_org_entry_vari = tk.StringVar()
        self.check_valid_mani_num_org_entry = tk.Entry(check_valid_page_mani_num_frame_line_1, 
                                                      textvariable = self.check_valid_mani_num_org_entry_vari, 
                                                      width = 16, 
                                                      font = self.fonsize_s)
        self.check_valid_mani_num_org_entry.grid(row = 0, column = 1,
                                                sticky = tk.W)
        ttk.Separator(self.check_valid_page_mani_num_frame, 
                      orient="horizontal").grid(row = 1, column = 0, 
                                                sticky = tk.EW) 
        check_valid_page_mani_num_frame_multiple = tk.Frame(self.check_valid_page_mani_num_frame)
        check_valid_page_mani_num_frame_multiple.grid(row = 2, column = 0,
                                                      padx = 2, pady = 2,
                                                      sticky = tk.W)
        check_valid_page_mani_num_frame_multiple_line_0 = tk.Frame(check_valid_page_mani_num_frame_multiple)
        check_valid_page_mani_num_frame_multiple_line_0.grid(row = 0, column = 0,
                                                             padx = 2, pady = 2,
                                                             sticky = tk.W)
        self.check_valid_mani_num_multi_check_button = tk.Button(check_valid_page_mani_num_frame_multiple_line_0, 
                                                                 text = "To check from *.csv file", 
                                                                 width = 26, 
                                                                 font = self.fonsize_m)        
        self.check_valid_mani_num_multi_check_button.grid(row = 0, column = 0,
                                                          padx = 2, pady = 2,
                                                          sticky = tk.W)
        self.check_valid_mani_num_multiple_state = ttk.Label(check_valid_page_mani_num_frame_multiple_line_0, 
                                                             text = "",                          
                                                             font = self.fonsize_s)
        self.check_valid_mani_num_multiple_state.grid(row = 0, column = 1,
                                                      padx = 2, pady = 2,
                                                      sticky = tk.W)
        check_valid_page_mani_num_frame_multiple_line_1 = tk.Frame(check_valid_page_mani_num_frame_multiple)
        check_valid_page_mani_num_frame_multiple_line_1.grid(row = 1, column = 0,
                                                             padx = 2, pady = 2,
                                                             sticky = tk.W)
        temp_str = "(1) In the first row, title row of the *.csv file, there are 2 required cells (regardless capital or small letters): "
        temp_str = temp_str+"(i) \"Manipulation Numbers\" or \"Mani\", "
        temp_str = temp_str+"(ii) \"Organization Numbers\" or \"Org\"."
        ttk.Label(check_valid_page_mani_num_frame_multiple_line_1, 
                  text = temp_str,
                  wraplength = 1100, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.NW) 
        temp_str = "(2) The max row number (excluding first row, title row) is 1 000."
        ttk.Label(check_valid_page_mani_num_frame_multiple_line_1, 
                  text = temp_str,
                  wraplength = 1100, 
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.NW) 
        ## command 
        self.check_valid_mani_num_check_button["command"] = self.check_valid_fun_mani_num_check
        self.check_valid_mani_num_clean_button["command"] = self.check_valid_fun_mani_num_clean
        self.check_valid_mani_num_multi_check_button["command"] = self.check_valid_fun_mani_num_multiple_check
    
    def check_valid_fun_select(self):
        temp_str = self.check_valid_page_radio_vari.get()
        if temp_str == "mix":
            self.check_valid_page_mix_num_frame.grid(row = 1, column = 0,
                                                     padx = 5, pady = 5,
                                                     sticky = tk.W)
            self.check_valid_page_mem_num_frame.grid_forget()
            self.check_valid_page_org_num_frame.grid_forget()
            self.check_valid_page_mani_num_frame.grid_forget()
        elif temp_str == "mem":
            self.check_valid_page_mix_num_frame.grid_forget()
            self.check_valid_page_mem_num_frame.grid(row = 1, column = 0,
                                                     padx = 5, pady = 5,
                                                     sticky = tk.W)
            self.check_valid_page_org_num_frame.grid_forget()
            self.check_valid_page_mani_num_frame.grid_forget()
        elif temp_str == "org":
            self.check_valid_page_mix_num_frame.grid_forget()
            self.check_valid_page_mem_num_frame.grid_forget()
            self.check_valid_page_org_num_frame.grid(row = 1, column = 0,
                                                     padx = 5, pady = 5,
                                                     sticky = tk.W)
            self.check_valid_page_mani_num_frame.grid_forget()
        elif temp_str == "mani":
            
            self.check_valid_page_mix_num_frame.grid_forget()
            self.check_valid_page_mem_num_frame.grid_forget()
            self.check_valid_page_org_num_frame.grid_forget()
            self.check_valid_page_mani_num_frame.grid(row = 1, column = 0,
                                                      padx = 5, pady = 5,
                                                      sticky = tk.W)
    
    def check_valid_fun_mix_num_check(self):
        if os.path.exists(self.cur_org_file_name):
            with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.cur_org = self.reading_str_text_org(read_text)
            if not self.cur_org is None:
                temp_num_0 = -1
                for n in range(len(self.cur_org[2])):
                    if self.cur_org[2][n] == self.cur_mani_num:
                        temp_num_0 = n
                        break
                if temp_num_0 >= 0:
                    temp_bool_0 = self.cur_org[3][temp_num_0]
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        if not temp_bool_0:
            showerror(title = "Error", 
                      message = "No privilege to do so.") 
        else:
            main_str_0 = self.check_valid_mix_num_main_entry_vari.get().strip()
            temp_str_0 = self.check_valid_mix_num_gn_entry_vari.get().strip()
            temp_str_1 = self.check_valid_mix_num_fn_entry_vari.get().strip()
            temp_str_2 = self.check_valid_mix_num_year_entry_vari.get().strip()
            temp_str_3 = self.check_valid_mix_num_month_entry_vari.get().strip()
            temp_str_4 = self.check_valid_mix_num_day_entry_vari.get().strip()
            temp_str_5 = self.check_valid_mix_num_hour_entry_vari.get().strip()
            temp_str_6 = self.check_valid_mix_num_minute_entry_vari.get().strip()
            if len(main_str_0) == 21:
                temp_bool_0 = True                
                temp_len_0 = len(temp_str_2)
                if temp_len_0 > 0:
                    for n in range(temp_len_0):
                        if not temp_str_2[n] in self.numeric_digits:
                            temp_bool_0 = False
                            break
                    if temp_bool_0:
                        temp_num_2 = int(temp_str_2)
                else:
                    temp_num_2 = None
                if temp_bool_0:
                    temp_len_0 = len(temp_str_3)
                    if temp_len_0 > 0:
                        for n in range(temp_len_0):
                            if not temp_str_3[n] in self.numeric_digits:
                                temp_bool_0 = False
                                break
                        if temp_bool_0:
                            temp_num_3 = int(temp_str_3)
                    else:
                        temp_num_3 = None
                if temp_bool_0:
                    temp_len_0 = len(temp_str_4)
                    if temp_len_0 > 0:
                        for n in range(temp_len_0):
                            if not temp_str_4[n] in self.numeric_digits:
                                temp_bool_0 = False
                                break
                        if temp_bool_0:
                            temp_num_4 = int(temp_str_4)
                    else:
                        temp_num_4 = None
                if temp_bool_0:
                    temp_len_0 = len(temp_str_5)
                    if temp_len_0 > 0:
                        for n in range(temp_len_0):
                            if not temp_str_5[n] in self.numeric_digits:
                                temp_bool_0 = False
                                break
                        if temp_bool_0:
                            temp_num_5 = int(temp_str_5)
                    else:
                        temp_num_5 = None
                if temp_bool_0:
                    temp_len_0 = len(temp_str_6)
                    if temp_len_0 > 0:
                        for n in range(temp_len_0):
                            if not temp_str_6[n] in self.numeric_digits:
                                temp_bool_0 = False
                                break
                        if temp_bool_0:
                            temp_num_6 = int(temp_str_6)
                    else:
                        temp_num_6 = None
                if temp_bool_0:
                    temp_len_0 = len(temp_str_0)
                    temp_len_1 = len(temp_str_1)
                    if (temp_len_0 < 1) & (temp_len_1 < 1):
                        temp_bool_1 = self.num_mix_valid(main_str_0, temp_str_0, temp_str_1, 
                                                         temp_num_2, temp_num_3, temp_num_4, 
                                                         temp_num_5, temp_num_6)
                        if temp_bool_1:
                            self.check_valid_mix_num_single_state["text"] = "Valid (empty name)."
                        else:
                            temp_bool_2 = self.num_mix_valid(main_str_0, None, None, 
                                                             temp_num_2, temp_num_3, temp_num_4, 
                                                             temp_num_5, temp_num_6)
                            if temp_bool_2:
                                self.check_valid_mix_num_single_state["text"] = "Valid (non-empty name)."
                            else:
                                self.check_valid_mix_num_single_state["text"] = "Invalid (non-empty name)."
                    elif temp_len_1 < 1:
                        temp_bool_1 = self.num_mix_valid(main_str_0, temp_str_0, temp_str_1, 
                                                         temp_num_2, temp_num_3, temp_num_4, 
                                                         temp_num_5, temp_num_6)
                        if temp_bool_1:
                            self.check_valid_mix_num_single_state["text"] = "Valid (empty family name)."
                        else:
                            temp_bool_2 = self.num_mix_valid(main_str_0, temp_str_0, None, 
                                                             temp_num_2, temp_num_3, temp_num_4, 
                                                             temp_num_5, temp_num_6)
                            if temp_bool_2:
                                self.check_valid_mix_num_single_state["text"] = "Valid."
                            else:
                                self.check_valid_mix_num_single_state["text"] = "Invalid."
                    else:
                        if temp_len_0 < 1:
                            temp_str_0 = None
                        temp_bool_1 = self.num_mix_valid(main_str_0, temp_str_0, temp_str_1, 
                                                         temp_num_2, temp_num_3, temp_num_4, 
                                                         temp_num_5, temp_num_6)
                        if temp_bool_1:
                            self.check_valid_mix_num_single_state["text"] = "Valid."
                        else:
                            self.check_valid_mix_num_single_state["text"] = "Invalid."
                        
                else:
                    self.check_valid_mix_num_single_state["text"] = "Invalid."
            else:
                self.check_valid_mix_num_single_state["text"] = "Invalid."
    
    def check_valid_fun_mix_num_clean(self):
        self.check_valid_mix_num_main_entry.delete(0, "end")
        self.check_valid_mix_num_single_state["text"] = ""
        self.check_valid_mix_num_gn_entry.delete(0, "end")
        self.check_valid_mix_num_fn_entry.delete(0, "end")
        self.check_valid_mix_num_year_entry.delete(0, "end")
        self.check_valid_mix_num_month_entry.delete(0, "end")
        self.check_valid_mix_num_day_entry.delete(0, "end")
        self.check_valid_mix_num_hour_entry.delete(0, "end")
        self.check_valid_mix_num_minute_entry.delete(0, "end")
    
    def check_valid_fun_mix_num_multiple_check(self):
        if os.path.exists(self.cur_org_file_name):
            with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.cur_org = self.reading_str_text_org(read_text)
            if not self.cur_org is None:
                temp_num_0 = -1
                for n in range(len(self.cur_org[2])):
                    if self.cur_org[2][n] == self.cur_mani_num:
                        temp_num_0 = n
                        break
                if temp_num_0 >= 0:
                    temp_bool_0 = self.cur_org[3][temp_num_0]
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        if not temp_bool_0:
            showerror(title = "Error", 
                      message = "No privilege to do so.") 
        else:
            file = askopenfile(mode = "r", 
                               filetypes=[("Comma separated values file of UTF-8", "*.csv")])  
            if file:
                file_path = file.name
                with open(file_path, "r", encoding = "utf-8") as open_file:
                    temp_str_0 = open_file.read()
                    if ord(temp_str_0[0]) == 65279:
                        temp_str_0 = temp_str_0[1:]
                    temp_str_list_0 = temp_str_0.split("\n")
                    file.close()
                temp_bool_0 = True
                temp_str_list_1 = temp_str_list_0[0].split(",")
                temp_len_0 = len(temp_str_list_1)
                for n in range(temp_len_0):
                    temp_str_0 = temp_str_list_1[n].strip().upper()
                    temp_bool_1 = True
                    while temp_bool_1:
                        temp_len_1 = len(temp_str_0)
                        if temp_len_1 > 1:
                            if (temp_str_0[0] == '"') & (temp_str_0[temp_len_1-1] == '"'):
                                temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                            elif (temp_str_0[0] == "'") & (temp_str_0[temp_len_1-1] == "'"):
                                temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                            else:
                                temp_bool_1 = False
                        else:
                            temp_bool_1 = False
                    temp_str_list_1[n] = temp_str_0.strip()
                valid_mix_num_tuple = ("MIXED NUMBER", "MIXED NUMBERS", "MIXED-NUMBER", "MIXED-NUMBERS", 
                                       "MIXED_NUMBER", "MIXED_NUMBERS", "MIXEDNUMBER", "MIXEDNUMBERS", 
                                       "MIX NUMBER", "MIX NUMBERS", "MIX-NUMBER", "MIX-NUMBERS",
                                       "MIX_NUMBER", "MIX_NUMBERS", "MIXNUMBER", "MIXNUMBERS",
                                       "MIXED NUM", "MIXED-NUM", "MIXED_NUM", "MIXEDNUM", 
                                       "MIX NUM", "MIX-NUM", "MIX_NUM", "MIXNUM", 
                                       "MIXED NO", "MIXED-NO", "MIXED_NO", "MIXEDNO", 
                                       "MIX NO", "MIX-NO", "MIX_NO", "MIXNO", 
                                       "MIXED", "MIX")
                temp_num_0 = -1
                temp_bool_1 = True
                for n in range(temp_len_0):
                    temp_str_0 = temp_str_list_1[n].upper()
                    if temp_str_0 in valid_mix_num_tuple:
                        if temp_bool_1:
                            temp_num_0 = n
                            temp_bool_1 = False
                        else:
                            temp_bool_0 = False
                            break
                if temp_bool_0:
                    if temp_bool_1:
                        temp_bool_0 = False
                    else:
                        valid_mix_num_num = temp_num_0
                if temp_bool_0:
                    valid_gn_tuple = ("GIVEN NAME", "GIVEN NAMES", "GIVEN-NAME", "GIVEN-NAMES", 
                                      "GIVEN_NAME", "GIVEN_NAMES", "GIVENNAME", "GIVENNAMES", 
                                      "GIV NAME", "GIV NAMES", "GIV-NAME", "GIV-NAMES", 
                                      "GIV_NAME", "GIV_NAMES", "GIVNAME", "GIVNAMES", 
                                      "G NAME", "G NAMES", "G-NAME", "G-NAMES", 
                                      "G_NAME", "G_NAMES", "GNAME", "GNAMES",
                                      "GIVEN N", "GIVEN-N", "GIVEN_N", "GIVENN", 
                                      "GIV N", "GIV-N", "GIV_N", "GIVN", 
                                      "G N", "G-N", "G_N", "GN", 
                                      "N G", "N-G", "N_G", "NG")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_gn_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_gn_num = None
                        else:
                            valid_gn_num = temp_num_0
                if temp_bool_0:
                    valid_fn_tuple = ("FAMILY NAME", "FAMILY NAMES", "FAMILY-NAME", "FAMILY-NAMES", 
                                      "FAMILY_NAME", "FAMILY_NAMES", "FAMILYNAME", "FAMILYNAMES", 
                                      "FAM NAME", "FAM NAMES", "FAM-NAME", "FAM-NAMES", 
                                      "FAM_NAME", "FAM_NAMES", "FAMNAME", "FAMNAMES", 
                                      "F NAME", "F NAMES", "F-NAME", "F-NAMES", 
                                      "F_NAME", "F_NAMES", "FNAME", "FNAMES",
                                      "FAMILY N", "FAMILY-N", "FAMILY_N", "FAMILYN", 
                                      "FAM N", "FAM-N", "FAM_N", "FAMN", 
                                      "F N", "F-N", "F_N", "FN", 
                                      "N F", "N-F", "N_F", "NF")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_fn_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_fn_num = None
                        else:
                            valid_fn_num = temp_num_0
                if temp_bool_0:
                    valid_issue_year_tuple = ("ISSUED YEAR", "ISSUED-YEAR", "ISSUED_YEAR", "ISSUEDYEAR", 
                                              "ISSUE YEAR", "ISSUE-YEAR", "ISSUE_YEAR", "ISSUEYEAR", 
                                              "ISS YEAR", "ISS-YEAR", "ISS_YEAR", "ISSYEAR", 
                                              "ISSUED Y", "ISSUED-Y", "ISSUED_Y", "ISSUEDY", 
                                              "ISSUE Y", "ISSUE-Y", "ISSUE_Y", "ISSUEY", 
                                              "ISS Y", "ISS-Y", "ISS_Y", "ISSY", 
                                              "Y")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_issue_year_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_issue_year_num = None
                        else:
                            valid_issue_year_num = temp_num_0
                if temp_bool_0:
                    valid_issue_month_tuple = ("ISSUED MONTH", "ISSUED-MONTH", "ISSUED_MONTH", "ISSUEDMONTH", 
                                               "ISSUE MONTH", "ISSUE-MONTH", "ISSUE_MONTH", "ISSUEMONTH", 
                                               "ISS MONTH", "ISS-MONTH", "ISS_MONTH", "ISSMONTH", 
                                               "ISSUED M", "ISSUED-M", "ISSUED_M", "ISSUEDM", 
                                               "ISSUE M", "ISSUE-M", "ISSUE_M", "ISSUEM", 
                                               "ISS M", "ISS-M", "ISS_M", "ISSM", 
                                               "M")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_issue_month_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_issue_month_num = None
                        else:
                            valid_issue_month_num = temp_num_0
                if temp_bool_0:
                    valid_issue_day_tuple = ("ISSUED DAY", "ISSUED-DAY", "ISSUED_DAY", "ISSUEDDAY", 
                                             "ISSUE DAY", "ISSUE-DAY", "ISSUE_DAY", "ISSUEDAY", 
                                             "ISS DAY", "ISS-DAY", "ISS_DAY", "ISSDAY", 
                                             "ISSUED D", "ISSUED-D", "ISSUED_D", "ISSUEDD", 
                                             "ISSUE D", "ISSUE-D", "ISSUE_D", "ISSUED", 
                                             "ISS D", "ISS-D", "ISS_D", "ISSD", 
                                             "D")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_issue_day_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_issue_day_num = None
                        else:
                            valid_issue_day_num = temp_num_0
                if temp_bool_0:
                    valid_issue_hour_tuple = ("ISSUED HOUR", "ISSUED-HOUR", "ISSUED_HOUR", "ISSUEDHOUR", 
                                              "ISSUE HOUR", "ISSUE-HOUR", "ISSUE_HOUR", "ISSUEHOUR", 
                                              "ISS HOUR", "ISS-HOUR", "ISS_HOUR", "ISSHOUR", 
                                              "ISSUED H", "ISSUED-H", "ISSUED_H", "ISSUEDH", 
                                              "ISSUE H", "ISSUE-H", "ISSUE_H", "ISSUEH", 
                                              "ISS H", "ISS-H", "ISS_H", "ISSH", 
                                              "H")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_issue_hour_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_issue_hour_num = None
                        else:
                            valid_issue_hour_num = temp_num_0
                if temp_bool_0:
                    valid_issue_minute_tuple = ("ISSUED MINUTE", "ISSUED-MINUTE", "ISSUED_MINUTE", "ISSUEDMINUTE", 
                                                "ISSUE MINUTE", "ISSUE-MINUTE", "ISSUE_MINUTE", "ISSUEMINUTE", 
                                                "ISS MINUTE", "ISS-MINUTE", "ISS_MINUTE", "ISSMINUTE", 
                                                "ISSUED MIN", "ISSUED-MIN", "ISSUED_MIN", "ISSUEDMIN", 
                                                "ISSUE MIN", "ISSUE-MIN", "ISSUE_MIN", "ISSUEMIN", 
                                                "ISS MIN", "ISS-MIN", "ISS_MIN", "ISSMIN", 
                                                "MIN")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_issue_minute_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_issue_minute_num = None
                        else:
                            valid_issue_minute_num = temp_num_0
                if temp_bool_0:
                    del(temp_str_list_0[0])
                    temp_len_1 = len(temp_str_list_0)
                    if temp_len_1 > 0:
                        for n in range(temp_len_1):
                            temp_str_list_0[n] = temp_str_list_0[n].strip() 
                        if len(temp_str_list_0[temp_len_1-1]) < 1:
                            del(temp_str_list_0[temp_len_1-1])
                            temp_len_1 -= 1
                        if (temp_len_1 > 0) & (temp_len_1 <= 1000):
                            temp_num_2 = valid_mix_num_num
                            if not valid_gn_num is None:
                                if valid_gn_num > temp_num_2:
                                    temp_num_2 = valid_gn_num
                            if not valid_fn_num is None:
                                if valid_fn_num > temp_num_2:
                                    temp_num_2 = valid_fn_num
                            if not valid_issue_year_num is None:
                                if valid_issue_year_num > temp_num_2:
                                    temp_num_2 = valid_issue_year_num
                            if not valid_issue_month_num is None:
                                if valid_issue_month_num > temp_num_2:
                                    temp_num_2 = valid_issue_month_num
                            if not valid_issue_day_num is None:
                                if valid_issue_day_num > temp_num_2:
                                    temp_num_2 = valid_issue_day_num
                            if not valid_issue_hour_num is None:
                                if valid_issue_hour_num > temp_num_2:
                                    temp_num_2 = valid_issue_hour_num
                            if not valid_issue_minute_num is None:
                                if valid_issue_minute_num > temp_num_2:
                                    temp_num_2 = valid_issue_minute_num
                            temp_path_0 = self.basic_parameter[3][0]+"/"+"Report_valid_mixed_number.csv"
                            temp_str_0 = chr(65279)
                            temp_str_0 = temp_str_0+'"'+"index"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"valid"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"aim: mixed number"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"given name"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"family name"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"issued year"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"issued month"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"issued day"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"issued hour"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"issued minute"+'"'
                            with open(temp_path_0, "w", encoding = "utf-8") as save_file:
                                save_file.write(temp_str_0)
                                save_file.close()
                            for n in range(temp_len_1):
                                temp_list_1 = self.csv_row_read(temp_str_list_0[n])                                
                                if len(temp_list_1) > temp_num_2:
                                    temp_bool_1 = True
                                    temp_str_2 = temp_list_1[valid_mix_num_num].strip()
                                    temp_bool_2 = True
                                    while temp_bool_2:
                                        temp_len_1 = len(temp_str_2)
                                        if temp_len_1 > 1:
                                            if (temp_str_2[0] == '"') & (temp_str_2[temp_len_1-1] == '"'):
                                                temp_str_2 = temp_str_2[1:(temp_len_1-1)]
                                            elif (temp_str_2[0] == "'") & (temp_str_2[temp_len_1-1] == "'"):
                                                temp_str_2 = temp_str_2[1:(temp_len_1-1)]
                                            else:
                                                temp_bool_2 = False
                                        else:
                                            temp_bool_2 = False
                                    temp_str_2 = temp_str_2.strip()
                                    if valid_gn_num is None:
                                        temp_str_3 = None
                                    else:
                                        temp_str_3 = temp_list_1[valid_gn_num].strip()
                                        temp_bool_2 = True
                                        while temp_bool_2:
                                            temp_len_1 = len(temp_str_3)
                                            if temp_len_1 > 1:
                                                if (temp_str_3[0] == '"') & (temp_str_3[temp_len_1-1] == '"'):
                                                    temp_str_3 = temp_str_3[1:(temp_len_1-1)]
                                                elif (temp_str_3[0] == "'") & (temp_str_3[temp_len_1-1] == "'"):
                                                    temp_str_3 = temp_str_3[1:(temp_len_1-1)]
                                                else:
                                                    temp_bool_2 = False
                                            else:
                                                temp_bool_2 = False
                                        temp_str_3 = temp_str_3.strip()
                                        if len(temp_str_3) < 1:
                                            temp_str_3 = None
                                    if valid_fn_num is None:
                                        temp_str_4 = None
                                    else:
                                        temp_str_4 = temp_list_1[valid_fn_num].strip()
                                        temp_bool_2 = True
                                        while temp_bool_2:
                                            temp_len_1 = len(temp_str_4)
                                            if temp_len_1 > 1:
                                                if (temp_str_4[0] == '"') & (temp_str_4[temp_len_1-1] == '"'):
                                                    temp_str_4 = temp_str_4[1:(temp_len_1-1)]
                                                elif (temp_str_4[0] == "'") & (temp_str_4[temp_len_1-1] == "'"):
                                                    temp_str_4 = temp_str_4[1:(temp_len_1-1)]
                                                else:
                                                    temp_bool_2 = False
                                            else:
                                                temp_bool_2 = False
                                        temp_str_4 = temp_str_4.strip()
                                        if len(temp_str_4) < 1:
                                            temp_str_4 = None
                                    if valid_issue_year_num is None:
                                        temp_str_5 = None
                                        temp_num_5 = None
                                    else:
                                        temp_str_5 = temp_list_1[valid_issue_year_num].strip()
                                        temp_bool_2 = True
                                        while temp_bool_2:
                                            temp_len_1 = len(temp_str_5)
                                            if temp_len_1 > 1:
                                                if (temp_str_5[0] == '"') & (temp_str_5[temp_len_1-1] == '"'):
                                                    temp_str_5 = temp_str_5[1:(temp_len_1-1)]
                                                elif (temp_str_5[0] == "'") & (temp_str_5[temp_len_1-1] == "'"):
                                                    temp_str_5 = temp_str_5[1:(temp_len_1-1)]
                                                else:
                                                    temp_bool_2 = False
                                            else:
                                                temp_bool_2 = False
                                        temp_str_5 = temp_str_5.strip()
                                        temp_num_5 = len(temp_str_5)
                                        if temp_num_5 > 0:
                                            for n1 in range(temp_num_5):
                                                if not temp_str_5[n1] in self.numeric_digits:
                                                    temp_bool_1 = False
                                                    break
                                            if temp_bool_1:
                                                temp_num_5 = int(temp_str_5)
                                        else:
                                            temp_num_5 = None
                                    if temp_bool_1:
                                        if valid_issue_month_num is None:
                                            temp_str_6 = None
                                            temp_num_6 = None
                                        else:
                                            temp_str_6 = temp_list_1[valid_issue_month_num].strip()
                                            temp_bool_2 = True
                                            while temp_bool_2:
                                                temp_len_1 = len(temp_str_6)
                                                if temp_len_1 > 1:
                                                    if (temp_str_6[0] == '"') & (temp_str_6[temp_len_1-1] == '"'):
                                                        temp_str_6 = temp_str_6[1:(temp_len_1-1)]
                                                    elif (temp_str_6[0] == "'") & (temp_str_6[temp_len_1-1] == "'"):
                                                        temp_str_6 = temp_str_6[1:(temp_len_1-1)]
                                                    else:
                                                        temp_bool_2 = False
                                                else:
                                                    temp_bool_2 = False
                                            temp_str_6 = temp_str_6.strip()
                                            temp_num_6 = len(temp_str_6)
                                            if temp_num_6 > 0:
                                                for n1 in range(temp_num_6):
                                                    if not temp_str_6[n1] in self.numeric_digits:
                                                        temp_bool_1 = False
                                                        break
                                                if temp_bool_1:
                                                    temp_num_6 = int(temp_str_6)
                                            else:
                                                temp_num_6 = None
                                    if temp_bool_1:
                                        if valid_issue_month_num is None:
                                            temp_str_7 = None
                                            temp_num_7 = None
                                        else:
                                            temp_str_7 = temp_list_1[valid_issue_day_num].strip()
                                            temp_bool_2 = True
                                            while temp_bool_2:
                                                temp_len_1 = len(temp_str_7)
                                                if temp_len_1 > 1:
                                                    if (temp_str_7[0] == '"') & (temp_str_7[temp_len_1-1] == '"'):
                                                        temp_str_7 = temp_str_7[1:(temp_len_1-1)]
                                                    elif (temp_str_7[0] == "'") & (temp_str_7[temp_len_1-1] == "'"):
                                                        temp_str_7 = temp_str_7[1:(temp_len_1-1)]
                                                    else:
                                                        temp_bool_2 = False
                                                else:
                                                    temp_bool_2 = False
                                            temp_str_7 = temp_str_7.strip()
                                            temp_num_7 = len(temp_str_7)
                                            if temp_num_7 > 0:
                                                for n1 in range(temp_num_7):
                                                    if not temp_str_7[n1] in self.numeric_digits:
                                                        temp_bool_1 = False
                                                        break
                                                if temp_bool_1:
                                                    temp_num_7 = int(temp_str_7)
                                            else:
                                                temp_num_7 = None
                                    if temp_bool_1:
                                        if valid_issue_month_num is None:
                                            temp_str_8 = None
                                            temp_num_8 = None
                                        else:
                                            temp_str_8 = temp_list_1[valid_issue_hour_num].strip()
                                            temp_bool_2 = True
                                            while temp_bool_2:
                                                temp_len_1 = len(temp_str_8)
                                                if temp_len_1 > 1:
                                                    if (temp_str_8[0] == '"') & (temp_str_8[temp_len_1-1] == '"'):
                                                        temp_str_8 = temp_str_8[1:(temp_len_1-1)]
                                                    elif (temp_str_8[0] == "'") & (temp_str_8[temp_len_1-1] == "'"):
                                                        temp_str_8 = temp_str_8[1:(temp_len_1-1)]
                                                    else:
                                                        temp_bool_2 = False
                                                else:
                                                    temp_bool_2 = False
                                            temp_str_8 = temp_str_8.strip()
                                            temp_num_8 = len(temp_str_8)
                                            if temp_num_8 > 0:
                                                for n1 in range(temp_num_8):
                                                    if not temp_str_8[n1] in self.numeric_digits:
                                                        temp_bool_1 = False
                                                        break
                                                if temp_bool_1:
                                                    temp_num_8 = int(temp_str_8)
                                            else:
                                                temp_num_8 = None
                                    if temp_bool_1:
                                        if valid_issue_month_num is None:
                                            temp_str_9 = None
                                            temp_num_9 = None
                                        else:
                                            temp_str_9 = temp_list_1[valid_issue_minute_num].strip()
                                            temp_bool_2 = True
                                            while temp_bool_2:
                                                temp_len_1 = len(temp_str_9)
                                                if temp_len_1 > 1:
                                                    if (temp_str_9[0] == '"') & (temp_str_9[temp_len_1-1] == '"'):
                                                        temp_str_9 = temp_str_9[1:(temp_len_1-1)]
                                                    elif (temp_str_9[0] == "'") & (temp_str_9[temp_len_1-1] == "'"):
                                                        temp_str_9 = temp_str_9[1:(temp_len_1-1)]
                                                    else:
                                                        temp_bool_2 = False
                                                else:
                                                    temp_bool_2 = False
                                            temp_str_9 = temp_str_9.strip()
                                            temp_num_9 = len(temp_str_9)
                                            if temp_num_9 > 0:
                                                for n1 in range(temp_num_9):
                                                    if not temp_str_9[n1] in self.numeric_digits:
                                                        temp_bool_1 = False
                                                        break
                                                if temp_bool_1:
                                                    temp_num_9 = int(temp_str_9)
                                            else:
                                                temp_num_9 = None
                                    if temp_bool_1:
                                        temp_bool_1 = self.num_mix_valid(temp_str_2, temp_str_3, temp_str_4, 
                                                                         temp_num_5, temp_num_6, temp_num_7, 
                                                                         temp_num_8, temp_num_9)
                                    temp_str_1 = "\n"
                                    temp_str_1 = temp_str_1+str(n+1)
                                    temp_str_1 = temp_str_1+","
                                    if temp_bool_1:
                                        temp_str_1 = temp_str_1+"1"
                                    else:
                                        temp_str_1 = temp_str_1+"0"
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_2 is None:
                                        temp_str_1 = temp_str_1+"'"+temp_str_2+"'"
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_3 is None:
                                        temp_str_1 = temp_str_1+'"'+temp_str_3+'"'
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_4 is None:
                                        temp_str_1 = temp_str_1+'"'+temp_str_4+'"'
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_5 is None:
                                        temp_str_1 = temp_str_1+temp_str_5
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_6 is None:
                                        temp_str_1 = temp_str_1+temp_str_6
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_7 is None:
                                        temp_str_1 = temp_str_1+temp_str_7
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_8 is None:
                                        temp_str_1 = temp_str_1+temp_str_8
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_9 is None:
                                        temp_str_1 = temp_str_1+temp_str_9
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_1)
                                        save_file.close()
                                else:
                                    temp_str_1 = "\n"
                                    temp_str_1 = temp_str_1+str(n+1)
                                    temp_str_1 = temp_str_1+","
                                    temp_str_1 = temp_str_1+"0"
                                    for n1 in range(8):
                                        temp_str_1 = temp_str_1+","
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_1)
                                        save_file.close()
                            self.check_valid_mix_num_multiple_state["text"] = "'"+temp_path_0+"' is output."
                        else:
                            self.check_valid_mix_num_multiple_state["text"] = "Fail."
                            showerror(title = "Error", 
                                      message = "The row number (excluding the first row, title row) should range within 1-1000.") 
                    else:
                        self.check_valid_mix_num_multiple_state["text"] = "Fail."
                        showerror(title = "Error", 
                                  message = "The row number (excluding the first row, title row) should range within 1-1000.") 
                else:
                    self.check_valid_mix_num_multiple_state["text"] = "Fail."
                    showerror(title = "Error", 
                              message = "The the first row, title row is in wrong format.") 
    
    def check_valid_fun_mem_num_check(self):
        if os.path.exists(self.cur_org_file_name):
            with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.cur_org = self.reading_str_text_org(read_text)
            if not self.cur_org is None:
                temp_num_0 = -1
                for n in range(len(self.cur_org[2])):
                    if self.cur_org[2][n] == self.cur_mani_num:
                        temp_num_0 = n
                        break
                if temp_num_0 >= 0:
                    temp_bool_0 = self.cur_org[3][temp_num_0]
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        if not temp_bool_0:
            showerror(title = "Error", 
                      message = "No privilege to do so.") 
        else:
            main_str_0 = self.check_valid_mem_num_main_entry_vari.get().strip().upper()
            temp_str_0 = self.check_valid_mem_num_mix_entry_vari.get().strip()
            temp_str_1 = self.check_valid_mem_num_org_entry_vari.get().strip()
            temp_str_2 = self.check_valid_mem_num_vn_entry_vari.get().strip()
            if len(main_str_0) == 14:
                temp_bool_0 = True            
                temp_len_0 = len(temp_str_0)
                if temp_len_0 < 1:
                    temp_str_0 = None
                elif temp_len_0 != 21:
                    temp_bool_0 = False
                if temp_bool_0:
                    temp_len_0 = len(temp_str_1)
                    if temp_len_0 < 1:
                        temp_str_1 = None
                    elif temp_len_0 != 14:
                        temp_bool_0 = False
                if temp_bool_0:
                    if len(temp_str_2) < 1:
                        temp_bool_1 = self.num_member_valid(main_str_0, temp_str_0, 
                                                            temp_str_2, temp_str_1)
                        if temp_bool_1:
                            self.check_valid_mem_num_single_state["text"] = "Valid (empty another name)."
                        else:
                            temp_bool_2 = self.num_member_valid(main_str_0, temp_str_0, 
                                                                None, temp_str_1)
                            if temp_bool_2:
                                self.check_valid_mem_num_single_state["text"] = "Valid (non-empty another name)."
                            else:
                                self.check_valid_mem_num_single_state["text"] = "Invalid."
                    else:
                        temp_bool_1 = self.num_member_valid(main_str_0, temp_str_0, 
                                                            temp_str_2, temp_str_1)
                        if temp_bool_1:
                            self.check_valid_mem_num_single_state["text"] = "Valid."
                        else:
                            self.check_valid_mem_num_single_state["text"] = "Invalid."
                else:
                    self.check_valid_mem_num_single_state["text"] = "Invalid."
            else:
                self.check_valid_mem_num_single_state["text"] = "Invalid."
    
    def check_valid_fun_mem_num_clean(self):
        self.check_valid_mem_num_main_entry.delete(0, "end")
        self.check_valid_mem_num_single_state["text"] = ""
        self.check_valid_mem_num_mix_entry.delete(0, "end")
        self.check_valid_mem_num_org_entry.delete(0, "end")
        self.check_valid_mem_num_vn_entry.delete(0, "end")
    
    def check_valid_fun_mem_num_multiple_check(self):
        if os.path.exists(self.cur_org_file_name):
            with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.cur_org = self.reading_str_text_org(read_text)
            if not self.cur_org is None:
                temp_num_0 = -1
                for n in range(len(self.cur_org[2])):
                    if self.cur_org[2][n] == self.cur_mani_num:
                        temp_num_0 = n
                        break
                if temp_num_0 >= 0:
                    temp_bool_0 = self.cur_org[3][temp_num_0]
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        if not temp_bool_0:
            showerror(title = "Error", 
                      message = "No privilege to do so.") 
        else:
            file = askopenfile(mode = "r", 
                               filetypes=[("Comma separated values file of UTF-8", "*.csv")])  
            if file:
                file_path = file.name
                with open(file_path, "r", encoding = "utf-8") as open_file:
                    temp_str_0 = open_file.read()
                    if ord(temp_str_0[0]) == 65279:
                        temp_str_0 = temp_str_0[1:]
                    temp_str_list_0 = temp_str_0.split("\n")
                    file.close()
                temp_bool_0 = True
                temp_str_list_1 = temp_str_list_0[0].split(",")
                temp_len_0 = len(temp_str_list_1)
                temp_len_0 = len(temp_str_list_1)
                for n in range(temp_len_0):
                    temp_str_0 = temp_str_list_1[n].strip().upper()
                    temp_bool_1 = True
                    while temp_bool_1:
                        temp_len_1 = len(temp_str_0)
                        if temp_len_1 > 1:
                            if (temp_str_0[0] == '"') & (temp_str_0[temp_len_1-1] == '"'):
                                temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                            elif (temp_str_0[0] == "'") & (temp_str_0[temp_len_1-1] == "'"):
                                temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                            else:
                                temp_bool_1 = False
                        else:
                            temp_bool_1 = False
                    temp_str_list_1[n] = temp_str_0.strip()
                valid_mem_num_tuple = ("MEMBER NUMBER", "MEMBER NUMBERS", "MEMBER-NUMBER", "MEMBER-NUMBERS", 
                                       "MEMBER_NUMBER", "MEMBER_NUMBERS", "MEMBERNUMBER", "MEMBERNUMBERS", 
                                       "MEM NUMBER", "MEM NUMBERS", "MEM-NUMBER", "MEM-NUMBERS",
                                       "MEM_NUMBER", "MEM_NUMBERS", "MEMNUMBER", "MEMNUMBERS",
                                       "MEMBER NUM", "MEMBER-NUM", "MEMBER_NUM", "MEMBERNUM", 
                                       "MEM NUM", "MEM-NUM", "MEM_NUM", "MEMNUM", 
                                       "MEMBER NO", "MEMBER-NO", "MEMBER_NO", "MEMBERNO", 
                                       "MEM NO", "MEM-NO", "MEM_NO", "MEMNO", 
                                       "MEMBER", "MEM")
                temp_num_0 = -1
                temp_bool_1 = True
                for n in range(temp_len_0):
                    temp_str_0 = temp_str_list_1[n].upper()
                    if temp_str_0 in valid_mem_num_tuple:
                        if temp_bool_1:
                            temp_num_0 = n
                            temp_bool_1 = False
                        else:
                            temp_bool_0 = False
                            break
                if temp_bool_0:
                    if temp_bool_1:
                        temp_bool_0 = False
                    else:
                        valid_mem_num_num = temp_num_0
                if temp_bool_0:
                    valid_mix_num_tuple = ("MIXED NUMBER", "MIXED NUMBERS", "MIXED-NUMBER", "MIXED-NUMBERS", 
                                           "MIXED_NUMBER", "MIXED_NUMBERS", "MIXEDNUMBER", "MIXEDNUMBERS", 
                                           "MIX NUMBER", "MIX NUMBERS", "MIX-NUMBER", "MIX-NUMBERS",
                                           "MIX_NUMBER", "MIX_NUMBERS", "MIXNUMBER", "MIXNUMBERS",
                                           "MIXED NUM", "MIXED-NUM", "MIXED_NUM", "MIXEDNUM", 
                                           "MIX NUM", "MIX-NUM", "MIX_NUM", "MIXNUM", 
                                           "MIXED NO", "MIXED-NO", "MIXED_NO", "MIXEDNO", 
                                           "MIX NO", "MIX-NO", "MIX_NO", "MIXNO", 
                                           "MIXED", "MIX")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_mix_num_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_mix_num_num = None
                        else:
                            valid_mix_num_num = temp_num_0
                if temp_bool_0:
                    valid_org_num_tuple = ("ORGANIZATION NUMBER", "ORGANIZATION NUMBERS", "ORGANIZATION-NUMBER", "ORGANIZATION-NUMBERS", 
                                           "ORGANIZATION_NUMBER", "ORGANIZATION_NUMBERS", "ORGANIZATIONNUMBER", "ORGANIZATIONNUMBERS", 
                                           "ORG NUMBER", "ORG NUMBERS", "ORG-NUMBER", "ORG-NUMBERS",
                                           "ORG_NUMBER", "ORG_NUMBERS", "ORGNUMBER", "ORGNUMBERS",
                                           "ORGANIZATION NUM", "ORGANIZATION-NUM", "ORGANIZATION_NUM", "ORGANIZATIONNUM", 
                                           "ORG NUM", "ORG-NUM", "ORG_NUM", "ORGNUM", 
                                           "ORGANIZATION NO", "ORGANIZATION-NO", "ORGANIZATION_NO", "ORGANIZATIONNO", 
                                           "ORG NO", "ORG-NO", "ORG_NO", "ORGNO", 
                                           "ORGANIZATION", "ORG")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_org_num_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_org_num_num = None
                        else:
                            valid_org_num_num = temp_num_0
                if temp_bool_0:
                    valid_vn_tuple = ("VIRTUAL NAME", "VIRTUAL NAMES", "VIRTUAL-NAME", "VIRTUAL-NAMES", 
                                      "VIRTUAL_NAME", "VIRTUAL_NAMES", "VIRTUALNAME", "VIRTUALNAMES", 
                                      "ANOTHER NAME", "ANOTHER NAMES", "ANOTHER-NAME", "ANOTHER-NAMES", 
                                      "ANOTHER_NAME", "ANOTHER_NAMES", "ANOTHERNAME", "ANOTHERNAMES", 
                                      "VIR NAME", "VIR NAMES", "VIR-NAME", "VIR-NAMES", 
                                      "VIR_NAME", "VIR_NAMES", "VIRNAME", "VIRNAMES", 
                                      "ANO NAME", "ANO NAMES", "ANO-NAME", "ANO-NAMES", 
                                      "ANO_NAME", "ANO_NAMES", "ANONAME", "ANONAMES",
                                      "V NAME", "V NAMES", "V-NAME", "V-NAMES", 
                                      "V_NAME", "V_NAMES", "VNAME", "VNAMES",
                                      "A NAME", "A NAMES", "A-NAME", "A-NAMES", 
                                      "A_NAME", "A_NAMES", "ANAME", "ANAMES",
                                      "VIRTUAL N", "VIRTUAL-N", "VIRTUAL_N", "VIRTUALN",
                                      "ANOTHER N", "ANOTHER-N", "ANOTHER_N", "ANOTHERN",
                                      "VIR N", "VIR-N", "VIR_N", "VIRN",
                                      "ANO N", "ANO-N", "ANO_N", "ANON",
                                      "V N", "V-N", "V_N", "VN", 
                                      "N V", "N-V", "N_V", "NV", 
                                      "A N", "A-N", "A_N", "AN", 
                                      "N A", "N-A", "N_A", "NA")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_vn_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_vn_num = None
                        else:
                            valid_vn_num = temp_num_0
                if temp_bool_0:
                    del(temp_str_list_0[0])
                    temp_len_1 = len(temp_str_list_0)
                    if temp_len_1 > 0:
                        for n in range(temp_len_1):
                            temp_str_list_0[n] = temp_str_list_0[n].strip()     
                        if len(temp_str_list_0[temp_len_1-1]) < 1:
                            del(temp_str_list_0[temp_len_1-1])
                            temp_len_1 -= 1
                        if (temp_len_1 > 0) & (temp_len_1 <= 1000):
                            temp_num_2 = valid_mem_num_num
                            if not valid_mix_num_num is None:
                                if valid_mix_num_num > temp_num_2:
                                    temp_num_2 = valid_mix_num_num
                            if not valid_org_num_num is None:
                                if valid_org_num_num > temp_num_2:
                                    temp_num_2 = valid_org_num_num
                            if not valid_vn_num is None:
                                if valid_vn_num > temp_num_2:
                                    temp_num_2 = valid_vn_num
                            temp_path_0 = self.basic_parameter[3][0]+"/"+"Report_valid_member_number.csv"
                            temp_str_0 = chr(65279)
                            temp_str_0 = temp_str_0+'"'+"index"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"valid"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"aim: member number"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"mixed number"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"issuer's organization number"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"another name / virtual name"+'"'
                            with open(temp_path_0, "w", encoding = "utf-8") as save_file:
                                save_file.write(temp_str_0)
                                save_file.close()
                            for n in range(temp_len_1):
                                temp_list_1 = self.csv_row_read(temp_str_list_0[n])
                                if len(temp_list_1) > temp_num_2:
                                    temp_bool_1 = True
                                    temp_str_2 = temp_list_1[valid_mem_num_num].strip()
                                    temp_bool_2 = True
                                    while temp_bool_2:
                                        temp_len_1 = len(temp_str_2)
                                        if temp_len_1 > 1:
                                            if (temp_str_2[0] == '"') & (temp_str_2[temp_len_1-1] == '"'):
                                                temp_str_2 = temp_str_2[1:(temp_len_1-1)]
                                            elif (temp_str_2[0] == "'") & (temp_str_2[temp_len_1-1] == "'"):
                                                temp_str_2 = temp_str_2[1:(temp_len_1-1)]
                                            else:
                                                temp_bool_2 = False
                                        else:
                                            temp_bool_2 = False
                                    temp_str_2 = temp_str_2.strip().upper()
                                    if valid_mix_num_num is None:
                                        temp_str_3 = None
                                    else:
                                        temp_str_3 = temp_list_1[valid_mix_num_num].strip()
                                        temp_bool_2 = True
                                        while temp_bool_2:
                                            temp_len_1 = len(temp_str_3)
                                            if temp_len_1 > 1:
                                                if (temp_str_3[0] == '"') & (temp_str_3[temp_len_1-1] == '"'):
                                                    temp_str_3 = temp_str_3[1:(temp_len_1-1)]
                                                elif (temp_str_3[0] == "'") & (temp_str_3[temp_len_1-1] == "'"):
                                                    temp_str_3 = temp_str_3[1:(temp_len_1-1)]
                                                else:
                                                    temp_bool_2 = False
                                            else:
                                                temp_bool_2 = False
                                        temp_str_3 = temp_str_3.strip()
                                        if len(temp_str_3) < 1:
                                            temp_str_3 = None
                                    if valid_org_num_num is None:
                                        temp_str_4 = None
                                    else:
                                        temp_str_4 = temp_list_1[valid_org_num_num].strip()
                                        temp_bool_2 = True
                                        while temp_bool_2:
                                            temp_len_1 = len(temp_str_4)
                                            if temp_len_1 > 1:
                                                if (temp_str_4[0] == '"') & (temp_str_4[temp_len_1-1] == '"'):
                                                    temp_str_4 = temp_str_4[1:(temp_len_1-1)]
                                                elif (temp_str_4[0] == "'") & (temp_str_4[temp_len_1-1] == "'"):
                                                    temp_str_4 = temp_str_4[1:(temp_len_1-1)]
                                                else:
                                                    temp_bool_2 = False
                                            else:
                                                temp_bool_2 = False
                                        temp_str_4 = temp_str_4.strip()
                                        if len(temp_str_4) < 1:
                                            temp_str_4 = None
                                    if valid_vn_num is None:
                                        temp_str_5 = None
                                    else:
                                        temp_str_5 = temp_list_1[valid_vn_num].strip()
                                        temp_bool_2 = True
                                        while temp_bool_2:
                                            temp_len_1 = len(temp_str_5)
                                            if temp_len_1 > 1:
                                                if (temp_str_5[0] == '"') & (temp_str_5[temp_len_1-1] == '"'):
                                                    temp_str_5 = temp_str_5[1:(temp_len_1-1)]
                                                elif (temp_str_5[0] == "'") & (temp_str_5[temp_len_1-1] == "'"):
                                                    temp_str_5 = temp_str_5[1:(temp_len_1-1)]
                                                else:
                                                    temp_bool_2 = False
                                            else:
                                                temp_bool_2 = False
                                        temp_str_5 = temp_str_5.strip()
                                        if len(temp_str_5) < 1:
                                            temp_str_5 = None 
                                    if temp_bool_1:
                                        temp_bool_1 = self.num_member_valid(temp_str_2, temp_str_3, 
                                                                            temp_str_5, temp_str_4)
                                    temp_str_1 = "\n"
                                    temp_str_1 = temp_str_1+str(n+1)
                                    temp_str_1 = temp_str_1+","
                                    if temp_bool_1:
                                        temp_str_1 = temp_str_1+"1"
                                    else:
                                        temp_str_1 = temp_str_1+"0"
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_2 is None:
                                        temp_str_1 = temp_str_1+"'"+temp_str_2+"'"
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_3 is None:
                                        temp_str_1 = temp_str_1+"'"+temp_str_3+"'"
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_4 is None:
                                        temp_str_1 = temp_str_1+"'"+temp_str_4+"'"
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_5 is None:
                                        temp_str_1 = temp_str_1+'"'+temp_str_5+'"'
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_1)
                                        save_file.close()
                                else:
                                    temp_str_1 = "\n"
                                    temp_str_1 = temp_str_1+str(n+1)
                                    temp_str_1 = temp_str_1+","
                                    temp_str_1 = temp_str_1+"0"
                                    for n1 in range(4):
                                        temp_str_1 = temp_str_1+","
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_1)
                                        save_file.close()
                            self.check_valid_mem_num_multiple_state["text"] = "'"+temp_path_0+"' is output."
                        else:
                            self.check_valid_mem_num_multiple_state["text"] = "Fail."
                            showerror(title = "Error", 
                                      message = "The row number (excluding the first row, title row) should range within 1-1000.") 
                    else:
                        self.check_valid_mem_num_multiple_state["text"] = "Fail."
                        showerror(title = "Error", 
                                  message = "The row number (excluding the first row, title row) should range within 1-1000.") 
                else:
                    self.check_valid_mem_num_multiple_state["text"] = "Fail."
                    showerror(title = "Error", 
                              message = "The the first row, title row is in wrong format.")             
    
    def check_valid_fun_org_num_check(self):
        if os.path.exists(self.cur_org_file_name):
            with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.cur_org = self.reading_str_text_org(read_text)
            if not self.cur_org is None:
                temp_num_0 = -1
                for n in range(len(self.cur_org[2])):
                    if self.cur_org[2][n] == self.cur_mani_num:
                        temp_num_0 = n
                        break
                if temp_num_0 >= 0:
                    temp_bool_0 = self.cur_org[3][temp_num_0]
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        if not temp_bool_0:
            showerror(title = "Error", 
                      message = "No privilege to do so.") 
        else:
            main_str_0 = self.check_valid_org_num_main_entry_vari.get().strip()
            temp_str_0 = self.check_valid_org_num_year_entry_vari.get().strip()
            temp_str_1 = self.check_valid_org_num_month_entry_vari.get().strip()
            temp_str_2 = self.check_valid_org_num_day_entry_vari.get().strip()
            temp_str_3 = self.check_valid_org_num_hour_entry_vari.get().strip()
            temp_str_4 = self.check_valid_org_num_minute_entry_vari.get().strip()
            if len(main_str_0) == 14:
                temp_bool_0 = True            
                temp_len_0 = len(temp_str_0)
                if temp_len_0 > 0:
                    for n in range(temp_len_0):
                        if not temp_str_0[n] in self.numeric_digits:
                            temp_bool_0 = False
                            break
                    if temp_bool_0:
                        temp_num_0 = int(temp_str_0)
                else:
                    temp_num_0 = None
                if temp_bool_0:
                    temp_len_0 = len(temp_str_1)
                    if temp_len_0 > 0:
                        for n in range(temp_len_0):
                            if not temp_str_1[n] in self.numeric_digits:
                                temp_bool_0 = False
                                break
                        if temp_bool_0:
                            temp_num_1 = int(temp_str_1)
                    else:
                        temp_num_1 = None
                if temp_bool_0:
                    temp_len_0 = len(temp_str_2)
                    if temp_len_0 > 0:
                        for n in range(temp_len_0):
                            if not temp_str_2[n] in self.numeric_digits:
                                temp_bool_0 = False
                                break
                        if temp_bool_0:
                            temp_num_2 = int(temp_str_2)
                    else:
                        temp_num_2 = None
                if temp_bool_0:
                    temp_len_0 = len(temp_str_3)
                    if temp_len_0 > 0:
                        for n in range(temp_len_0):
                            if not temp_str_3[n] in self.numeric_digits:
                                temp_bool_0 = False
                                break
                        if temp_bool_0:
                            temp_num_3 = int(temp_str_3)
                    else:
                        temp_num_3 = None
                if temp_bool_0:
                    temp_len_0 = len(temp_str_4)
                    if temp_len_0 > 0:
                        for n in range(temp_len_0):
                            if not temp_str_4[n] in self.numeric_digits:
                                temp_bool_0 = False
                                break
                        if temp_bool_0:
                            temp_num_4 = int(temp_str_4)
                    else:
                        temp_num_4 = None
                if temp_bool_0:
                    temp_bool_1 = self.num_organization_valid(main_str_0, 
                                                              temp_num_0, temp_num_1, temp_num_2, 
                                                              temp_num_3, temp_num_4)
                    if temp_bool_1:
                        self.check_valid_org_num_single_state["text"] = "Valid."
                    else:
                        self.check_valid_org_num_single_state["text"] = "Invalid."
                else:
                    self.check_valid_org_num_single_state["text"] = "Invalid."
            else:
                self.check_valid_org_num_single_state["text"] = "Invalid."
    
    def check_valid_fun_org_num_clean(self):
        self.check_valid_org_num_main_entry.delete(0, "end")
        self.check_valid_org_num_single_state["text"] = ""
        self.check_valid_org_num_year_entry.delete(0, "end")
        self.check_valid_org_num_month_entry.delete(0, "end")
        self.check_valid_org_num_day_entry.delete(0, "end")
        self.check_valid_org_num_hour_entry.delete(0, "end")
        self.check_valid_org_num_minute_entry.delete(0, "end")
    
    def check_valid_fun_org_num_multiple_check(self):
        if os.path.exists(self.cur_org_file_name):
            with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.cur_org = self.reading_str_text_org(read_text)
            if not self.cur_org is None:
                temp_num_0 = -1
                for n in range(len(self.cur_org[2])):
                    if self.cur_org[2][n] == self.cur_mani_num:
                        temp_num_0 = n
                        break
                if temp_num_0 >= 0:
                    temp_bool_0 = self.cur_org[3][temp_num_0]
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        if not temp_bool_0:
            showerror(title = "Error", 
                      message = "No privilege to do so.") 
        else:
            file = askopenfile(mode = "r", 
                               filetypes=[("Comma separated values file of UTF-8", "*.csv")])  
            if file:
                file_path = file.name
                with open(file_path, "r", encoding = "utf-8") as open_file:
                    temp_str_0 = open_file.read()
                    if ord(temp_str_0[0]) == 65279:
                        temp_str_0 = temp_str_0[1:]
                    temp_str_list_0 = temp_str_0.split("\n")
                    file.close()
                temp_bool_0 = True
                temp_str_list_1 = temp_str_list_0[0].split(",")
                temp_len_0 = len(temp_str_list_1)
                temp_len_0 = len(temp_str_list_1)
                for n in range(temp_len_0):
                    temp_str_0 = temp_str_list_1[n].strip().upper()
                    temp_bool_1 = True
                    while temp_bool_1:
                        temp_len_1 = len(temp_str_0)
                        if temp_len_1 > 1:
                            if (temp_str_0[0] == '"') & (temp_str_0[temp_len_1-1] == '"'):
                                temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                            elif (temp_str_0[0] == "'") & (temp_str_0[temp_len_1-1] == "'"):
                                temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                            else:
                                temp_bool_1 = False
                        else:
                            temp_bool_1 = False
                    temp_str_list_1[n] = temp_str_0.strip()
                valid_org_num_tuple = ("ORGANIZATION NUMBER", "ORGANIZATION NUMBERS", "ORGANIZATION-NUMBER", "ORGANIZATION-NUMBERS", 
                                       "ORGANIZATION_NUMBER", "ORGANIZATION_NUMBERS", "ORGANIZATIONNUMBER", "ORGANIZATIONNUMBERS", 
                                       "ORG NUMBER", "ORG NUMBERS", "ORG-NUMBER", "ORG-NUMBERS",
                                       "ORG_NUMBER", "ORG_NUMBERS", "ORGNUMBER", "ORGNUMBERS",
                                       "ORGANIZATION NUM", "ORGANIZATION-NUM", "ORGANIZATION_NUM", "ORGANIZATIONNUM", 
                                       "ORG NUM", "ORG-NUM", "ORG_NUM", "ORGNUM", 
                                       "ORGANIZATION NO", "ORGANIZATION-NO", "ORGANIZATION_NO", "ORGANIZATIONNO", 
                                       "ORG NO", "ORG-NO", "ORG_NO", "ORGNO", 
                                       "ORGANIZATION", "ORG")
                temp_num_0 = -1
                temp_bool_1 = True
                for n in range(temp_len_0):
                    temp_str_0 = temp_str_list_1[n].upper()
                    if temp_str_0 in valid_org_num_tuple:
                        if temp_bool_1:
                            temp_num_0 = n
                            temp_bool_1 = False
                        else:
                            temp_bool_0 = False
                            break
                if temp_bool_0:
                    if temp_bool_1:
                        temp_bool_0 = False
                    else:
                        valid_org_num_num = temp_num_0
                if temp_bool_0:
                    valid_create_year_tuple = ("CREATED YEAR", "CREATED-YEAR", "CREATED_YEAR", "CREATEDYEAR", 
                                               "CREATE YEAR", "CREATE-YEAR", "CREATE_YEAR", "CREATEYEAR", 
                                               "CRE YEAR", "CRE-YEAR", "CRE_YEAR", "CREYEAR", 
                                               "CREATED Y", "CREATED-Y", "CREATED_Y", "CREATEDY", 
                                               "CREATE Y", "CREATE-Y", "CREATE_Y", "CREATEY", 
                                               "CRE Y", "CRE-Y", "CRE_Y", "CREY")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_create_year_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_create_year_num = None
                        else:
                            valid_create_year_num = temp_num_0
                if temp_bool_0:
                    valid_create_month_tuple = ("CREATED MONTH", "CREATED-MONTH", "CREATED_MONTH", "CREATEDMONTH", 
                                                "CREATE MONTH", "CREATE-MONTH", "CREATE_MONTH", "CREATEMONTH", 
                                                "CRE MONTH", "CRE-MONTH", "CRE_MONTH", "CREMONTH", 
                                                "CREATED M", "CREATED-M", "CREATED_M", "CREATEDM", 
                                                "CREATE M", "CREATE-M", "CREATE_M", "CREATEM", 
                                                "CRE M", "CRE-M", "CRE_M", "CREM")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_create_month_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_create_month_num = None
                        else:
                            valid_create_month_num = temp_num_0
                if temp_bool_0:
                    valid_create_day_tuple = ("CREATED DAY", "CREATED-DAY", "CREATED_DAY", "CREATEDDAY", 
                                              "CREATE DAY", "CREATE-DAY", "CREATE_DAY", "CREATEDAY", 
                                              "CRE DAY", "CRE-DAY", "CRE_DAY", "CREDAY", 
                                              "CREATED D", "CREATED-D", "CREATED_D", "CREATEDD", 
                                              "CREATE D", "CREATE-D", "CREATE_D", "CREATED", 
                                              "CRE D", "CRE-D", "CRE_D", "CRED")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_create_day_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_create_day_num = None
                        else:
                            valid_create_day_num = temp_num_0
                if temp_bool_0:
                    valid_create_hour_tuple = ("CREATED HOUR", "CREATED-HOUR", "CREATED_HOUR", "CREATEDHOUR", 
                                               "CREATE HOUR", "CREATE-HOUR", "CREATE_HOUR", "CREATEHOUR", 
                                               "CRE HOUR", "CRE-HOUR", "CRE_HOUR", "CREHOUR", 
                                               "CREATED H", "CREATED-H", "CREATED_H", "CREATEDH", 
                                               "CREATE H", "CREATE-H", "CREATE_H", "CREATEH", 
                                               "CRE H", "CRE-H", "CRE_H", "CREH")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_create_hour_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_create_hour_num = None
                        else:
                            valid_create_hour_num = temp_num_0
                if temp_bool_0:
                    valid_create_minute_tuple = ("CREATED MINUTE", "CREATED-MINUTE", "CREATED_MINUTE", "CREATEDMINUTE", 
                                                 "CREATE MINUTE", "CREATE-MINUTE", "CREATE_MINUTE", "CREATEMINUTE", 
                                                 "CRE MINUTE", "CRE-MINUTE", "CRE_MINUTE", "CREMINUTE", 
                                                 "CREATED MIN", "CREATED-MIN", "CREATED_MIN", "CREATEDMIN", 
                                                 "CREATE MIN", "CREATE-MIN", "CREATE_MIN", "CREATEMIN", 
                                                 "CRE MIN", "CRE-MIN", "CRE_MIN", "CREMIN")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_create_minute_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_create_minute_num = None
                        else:
                            valid_create_minute_num = temp_num_0
                if temp_bool_0:
                    del(temp_str_list_0[0])
                    temp_len_1 = len(temp_str_list_0)
                    if temp_len_1 > 0:
                        for n in range(temp_len_1):
                            temp_str_list_0[n] = temp_str_list_0[n].strip()     
                        if len(temp_str_list_0[temp_len_1-1]) < 1:
                            del(temp_str_list_0[temp_len_1-1])
                            temp_len_1 -= 1
                        if (temp_len_1 > 0) & (temp_len_1 <= 1000):
                            temp_num_2 = valid_org_num_num
                            if not valid_create_year_num is None:
                                if valid_create_year_num > temp_num_2:
                                    temp_num_2 = valid_create_year_num
                            if not valid_create_month_num is None:
                                if valid_create_month_num > temp_num_2:
                                    temp_num_2 = valid_create_month_num
                            if not valid_create_day_num is None:
                                if valid_create_day_num > temp_num_2:
                                    temp_num_2 = valid_create_day_num
                            if not valid_create_hour_num is None:
                                if valid_create_hour_num > temp_num_2:
                                    temp_num_2 = valid_create_hour_num
                            if not valid_create_minute_num is None:
                                if valid_create_minute_num > temp_num_2:
                                    temp_num_2 = valid_create_minute_num
                            temp_path_0 = self.basic_parameter[3][0]+"/"+"Report_valid_organization_number.csv"
                            temp_str_0 = chr(65279)
                            temp_str_0 = temp_str_0+'"'+"index"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"valid"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"aim: organization number"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"created year"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"created month"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"created day"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"created hour"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"created minute"+'"'
                            with open(temp_path_0, "w", encoding = "utf-8") as save_file:
                                save_file.write(temp_str_0)
                                save_file.close()
                            for n in range(temp_len_1):
                                temp_list_1 = self.csv_row_read(temp_str_list_0[n])                                
                                if len(temp_list_1) > temp_num_2:
                                    temp_bool_1 = True
                                    temp_str_2 = temp_list_1[valid_org_num_num].strip()
                                    temp_bool_2 = True
                                    while temp_bool_2:
                                        temp_len_1 = len(temp_str_2)
                                        if temp_len_1 > 1:
                                            if (temp_str_2[0] == '"') & (temp_str_2[temp_len_1-1] == '"'):
                                                temp_str_2 = temp_str_2[1:(temp_len_1-1)]
                                            elif (temp_str_2[0] == "'") & (temp_str_2[temp_len_1-1] == "'"):
                                                temp_str_2 = temp_str_2[1:(temp_len_1-1)]
                                            else:
                                                temp_bool_2 = False
                                        else:
                                            temp_bool_2 = False
                                    temp_str_2 = temp_str_2.strip()
                                    if valid_create_year_num is None:
                                        temp_str_3 = None
                                        temp_num_3 = None
                                    else:
                                        temp_str_3 = temp_list_1[valid_create_year_num].strip()
                                        temp_bool_2 = True
                                        while temp_bool_2:
                                            temp_len_1 = len(temp_str_3)
                                            if temp_len_1 > 1:
                                                if (temp_str_3[0] == '"') & (temp_str_3[temp_len_1-1] == '"'):
                                                    temp_str_3 = temp_str_3[1:(temp_len_1-1)]
                                                elif (temp_str_3[0] == "'") & (temp_str_3[temp_len_1-1] == "'"):
                                                    temp_str_3 = temp_str_3[1:(temp_len_1-1)]
                                                else:
                                                    temp_bool_2 = False
                                            else:
                                                temp_bool_2 = False
                                        temp_str_3 = temp_str_3.strip()
                                        temp_num_3 = len(temp_str_3)
                                        if temp_num_3 > 0:
                                            for n1 in range(temp_num_3):
                                                if not temp_str_3[n1] in self.numeric_digits:
                                                    temp_bool_1 = False
                                                    break
                                            if temp_bool_1:
                                                temp_num_3 = int(temp_str_3)
                                        else:
                                            temp_num_3 = None
                                    if temp_bool_1:
                                        if valid_create_month_num is None:
                                            temp_str_4 = None
                                            temp_num_4 = None
                                        else:
                                            temp_str_4 = temp_list_1[valid_create_month_num].strip()
                                            temp_bool_2 = True
                                            while temp_bool_2:
                                                temp_len_1 = len(temp_str_4)
                                                if temp_len_1 > 1:
                                                    if (temp_str_4[0] == '"') & (temp_str_4[temp_len_1-1] == '"'):
                                                        temp_str_4 = temp_str_4[1:(temp_len_1-1)]
                                                    elif (temp_str_4[0] == "'") & (temp_str_4[temp_len_1-1] == "'"):
                                                        temp_str_4 = temp_str_4[1:(temp_len_1-1)]
                                                    else:
                                                        temp_bool_2 = False
                                                else:
                                                    temp_bool_2 = False
                                            temp_str_4 = temp_str_4.strip()
                                            temp_num_4 = len(temp_str_4)
                                            if temp_num_4 > 0:
                                                for n1 in range(temp_num_4):
                                                    if not temp_str_4[n1] in self.numeric_digits:
                                                        temp_bool_1 = False
                                                        break
                                                if temp_bool_1:
                                                    temp_num_4 = int(temp_str_4)
                                            else:
                                                temp_num_4 = None
                                    if temp_bool_1:
                                        if valid_create_month_num is None:
                                            temp_str_5 = None
                                            temp_num_5 = None
                                        else:
                                            temp_str_5 = temp_list_1[valid_create_day_num].strip()
                                            temp_bool_2 = True
                                            while temp_bool_2:
                                                temp_len_1 = len(temp_str_5)
                                                if temp_len_1 > 1:
                                                    if (temp_str_5[0] == '"') & (temp_str_5[temp_len_1-1] == '"'):
                                                        temp_str_5 = temp_str_5[1:(temp_len_1-1)]
                                                    elif (temp_str_5[0] == "'") & (temp_str_5[temp_len_1-1] == "'"):
                                                        temp_str_5 = temp_str_5[1:(temp_len_1-1)]
                                                    else:
                                                        temp_bool_2 = False
                                                else:
                                                    temp_bool_2 = False
                                            temp_str_5 = temp_str_5.strip()
                                            temp_num_5 = len(temp_str_5)
                                            if temp_num_5 > 0:
                                                for n1 in range(temp_num_5):
                                                    if not temp_str_5[n1] in self.numeric_digits:
                                                        temp_bool_1 = False
                                                        break
                                                if temp_bool_1:
                                                    temp_num_5 = int(temp_str_5)
                                            else:
                                                temp_num_5 = None
                                    if temp_bool_1:
                                        if valid_create_month_num is None:
                                            temp_str_6 = None
                                            temp_num_6 = None
                                        else:
                                            temp_str_6 = temp_list_1[valid_create_hour_num].strip()
                                            temp_bool_2 = True
                                            while temp_bool_2:
                                                temp_len_1 = len(temp_str_6)
                                                if temp_len_1 > 1:
                                                    if (temp_str_6[0] == '"') & (temp_str_6[temp_len_1-1] == '"'):
                                                        temp_str_6 = temp_str_6[1:(temp_len_1-1)]
                                                    elif (temp_str_6[0] == "'") & (temp_str_6[temp_len_1-1] == "'"):
                                                        temp_str_6 = temp_str_6[1:(temp_len_1-1)]
                                                    else:
                                                        temp_bool_2 = False
                                                else:
                                                    temp_bool_2 = False
                                            temp_str_6 = temp_str_6.strip()
                                            temp_num_6 = len(temp_str_6)
                                            if temp_num_6 > 0:
                                                for n1 in range(temp_num_6):
                                                    if not temp_str_6[n1] in self.numeric_digits:
                                                        temp_bool_1 = False
                                                        break
                                                if temp_bool_1:
                                                    temp_num_6 = int(temp_str_6)
                                            else:
                                                temp_num_6 = None
                                    if temp_bool_1:
                                        if valid_create_month_num is None:
                                            temp_str_7 = None
                                            temp_num_7 = None
                                        else:
                                            temp_str_7 = temp_list_1[valid_create_minute_num].strip()
                                            temp_bool_2 = True
                                            while temp_bool_2:
                                                temp_len_1 = len(temp_str_7)
                                                if temp_len_1 > 1:
                                                    if (temp_str_7[0] == '"') & (temp_str_7[temp_len_1-1] == '"'):
                                                        temp_str_7 = temp_str_7[1:(temp_len_1-1)]
                                                    elif (temp_str_7[0] == "'") & (temp_str_7[temp_len_1-1] == "'"):
                                                        temp_str_7 = temp_str_7[1:(temp_len_1-1)]
                                                    else:
                                                        temp_bool_2 = False
                                                else:
                                                    temp_bool_2 = False
                                            temp_str_7 = temp_str_7.strip()
                                            temp_num_7 = len(temp_str_7)
                                            if temp_num_7 > 0:
                                                for n1 in range(temp_num_7):
                                                    if not temp_str_7[n1] in self.numeric_digits:
                                                        temp_bool_1 = False
                                                        break
                                                if temp_bool_1:
                                                    temp_num_7 = int(temp_str_7)
                                            else:
                                                temp_num_7 = None
                                    if temp_bool_1:
                                        temp_bool_1 = self.num_organization_valid(temp_str_2, 
                                                                                  temp_num_3, temp_num_4, temp_num_5, 
                                                                                  temp_num_6, temp_num_7)
                                    temp_str_1 = "\n"
                                    temp_str_1 = temp_str_1+str(n+1)
                                    temp_str_1 = temp_str_1+","
                                    if temp_bool_1:
                                        temp_str_1 = temp_str_1+"1"
                                    else:
                                        temp_str_1 = temp_str_1+"0"
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_2 is None:
                                        temp_str_1 = temp_str_1+"'"+temp_str_2+"'"
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_3 is None:
                                        temp_str_1 = temp_str_1+'"'+temp_str_3+'"'
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_4 is None:
                                        temp_str_1 = temp_str_1+'"'+temp_str_4+'"'
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_5 is None:
                                        temp_str_1 = temp_str_1+temp_str_5
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_6 is None:
                                        temp_str_1 = temp_str_1+temp_str_6
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_7 is None:
                                        temp_str_1 = temp_str_1+temp_str_7
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_1)
                                        save_file.close()
                                else:
                                    temp_str_1 = "\n"
                                    temp_str_1 = temp_str_1+str(n+1)
                                    temp_str_1 = temp_str_1+","
                                    temp_str_1 = temp_str_1+"0"
                                    for n1 in range(6):
                                        temp_str_1 = temp_str_1+","
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_1)
                                        save_file.close()
                            self.check_valid_org_num_multiple_state["text"] = "'"+temp_path_0+"' is output."
                        else:
                            self.check_valid_org_num_multiple_state["text"] = "Fail."
                            showerror(title = "Error", 
                                      message = "The row number (excluding the first row, title row) should range within 1-1000.") 
                    else:
                        self.check_valid_org_num_multiple_state["text"] = "Fail."
                        showerror(title = "Error", 
                                  message = "The row number (excluding the first row, title row) should range within 1-1000.") 
                else:
                    self.check_valid_org_num_multiple_state["text"] = "Fail."
                    showerror(title = "Error", 
                              message = "The the first row, title row is in wrong format.") 
    
    def check_valid_fun_mani_num_check(self):
        if os.path.exists(self.cur_org_file_name):
            with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.cur_org = self.reading_str_text_org(read_text)
            if not self.cur_org is None:
                temp_num_0 = -1
                for n in range(len(self.cur_org[2])):
                    if self.cur_org[2][n] == self.cur_mani_num:
                        temp_num_0 = n
                        break
                if temp_num_0 >= 0:
                    temp_bool_0 = self.cur_org[3][temp_num_0]
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        if not temp_bool_0:
            showerror(title = "Error", 
                      message = "No privilege to do so.") 
        else:
            main_str_0 = self.check_valid_mani_num_main_entry_vari.get().strip().upper()
            temp_str_0 = self.check_valid_mani_num_org_entry_vari.get().strip()
            if len(main_str_0) == 7:     
                if len(temp_str_0) == 14:
                   temp_bool_1 = self.number_manipulation_valid(main_str_0, temp_str_0)
                   if temp_bool_1:
                       self.check_valid_mani_num_single_state["text"] = "Valid."
                   else:
                       self.check_valid_mani_num_single_state["text"] = "Invalid."
                else:
                    self.check_valid_mani_num_single_state["text"] = "Invalid."
            else:
                self.check_valid_mani_num_single_state["text"] = "Invalid."
    
    def check_valid_fun_mani_num_clean(self):
        self.check_valid_mani_num_main_entry.delete(0, "end")
        self.check_valid_mani_num_single_state["text"] = ""
        self.check_valid_mani_num_org_entry.delete(0, "end")
    
    def check_valid_fun_mani_num_multiple_check(self):
        if os.path.exists(self.cur_org_file_name):
            with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.cur_org = self.reading_str_text_org(read_text)
            if not self.cur_org is None:
                temp_num_0 = -1
                for n in range(len(self.cur_org[2])):
                    if self.cur_org[2][n] == self.cur_mani_num:
                        temp_num_0 = n
                        break
                if temp_num_0 >= 0:
                    temp_bool_0 = self.cur_org[3][temp_num_0]
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        if not temp_bool_0:
            showerror(title = "Error", 
                      message = "No privilege to do so.") 
        else:
            file = askopenfile(mode = "r", 
                               filetypes=[("Comma separated values file of UTF-8", "*.csv")])  
            if file:
                file_path = file.name
                with open(file_path, "r", encoding = "utf-8") as open_file:
                    temp_str_0 = open_file.read()
                    if ord(temp_str_0[0]) == 65279:
                        temp_str_0 = temp_str_0[1:]
                    temp_str_list_0 = temp_str_0.split("\n")
                    file.close()
                temp_bool_0 = True
                temp_str_list_1 = temp_str_list_0[0].split(",")
                temp_len_0 = len(temp_str_list_1)
                temp_len_0 = len(temp_str_list_1)
                for n in range(temp_len_0):
                    temp_str_0 = temp_str_list_1[n].strip().upper()
                    temp_bool_1 = True
                    while temp_bool_1:
                        temp_len_1 = len(temp_str_0)
                        if temp_len_1 > 1:
                            if (temp_str_0[0] == '"') & (temp_str_0[temp_len_1-1] == '"'):
                                temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                            elif (temp_str_0[0] == "'") & (temp_str_0[temp_len_1-1] == "'"):
                                temp_str_0 = temp_str_0[1:(temp_len_1-1)]
                            else:
                                temp_bool_1 = False
                        else:
                            temp_bool_1 = False
                    temp_str_list_1[n] = temp_str_0.strip()
                valid_mani_num_tuple = ("MANIPULATION NUMBER", "MANIPULATION NUMBERS", "MANIPULATION-NUMBER", "MANIPULATION-NUMBERS", 
                                        "MANIPULATION_NUMBER", "MANIPULATION_NUMBERS", "MANIPULATIONNUMBER", "MANIPULATIONNUMBERS", 
                                        "MANI NUMBER", "MANI NUMBERS", "MANI-NUMBER", "MANI-NUMBERS",
                                        "MANI_NUMBER", "MANI_NUMBERS", "MANINUMBER", "MANINUMBERS",
                                        "MANIPULATION NUM", "MANIPULATION-NUM", "MANIPULATION_NUM", "MANIPULATIONNUM", 
                                        "MANI NUM", "MANI-NUM", "MANI_NUM", "MANINUM", 
                                        "MANIPULATION NO", "MANIPULATION-NO", "MANIPULATION_NO", "MANIPULATIONNO", 
                                        "MANI NO", "MANI-NO", "MANI_NO", "MANINO", 
                                        "MANIPULATION", "MANI")
                temp_num_0 = -1
                temp_bool_1 = True
                for n in range(temp_len_0):
                    temp_str_0 = temp_str_list_1[n].upper()
                    if temp_str_0 in valid_mani_num_tuple:
                        if temp_bool_1:
                            temp_num_0 = n
                            temp_bool_1 = False
                        else:
                            temp_bool_0 = False
                            break
                if temp_bool_0:
                    if temp_bool_1:
                        temp_bool_0 = False
                    else:
                        valid_mani_num_num = temp_num_0
                if temp_bool_0:
                    valid_org_num_tuple = ("ORGANIZATION NUMBER", "ORGANIZATION NUMBERS", "ORGANIZATION-NUMBER", "ORGANIZATION-NUMBERS", 
                                           "ORGANIZATION_NUMBER", "ORGANIZATION_NUMBERS", "ORGANIZATIONNUMBER", "ORGANIZATIONNUMBERS", 
                                           "ORG NUMBER", "ORG NUMBERS", "ORG-NUMBER", "ORG-NUMBERS",
                                           "ORG_NUMBER", "ORG_NUMBERS", "ORGNUMBER", "ORGNUMBERS",
                                           "ORGANIZATION NUM", "ORGANIZATION-NUM", "ORGANIZATION_NUM", "ORGANIZATIONNUM", 
                                           "ORG NUM", "ORG-NUM", "ORG_NUM", "ORGNUM", 
                                           "ORGANIZATION NO", "ORGANIZATION-NO", "ORGANIZATION_NO", "ORGANIZATIONNO", 
                                           "ORG NO", "ORG-NO", "ORG_NO", "ORGNO", 
                                           "ORGANIZATION", "ORG")
                    temp_num_0 = -1
                    temp_bool_1 = True
                    for n in range(temp_len_0):
                        temp_str_0 = temp_str_list_1[n].upper()
                        if temp_str_0 in valid_org_num_tuple:
                            if temp_bool_1:
                                temp_num_0 = n
                                temp_bool_1 = False
                            else:
                                temp_bool_0 = False
                                break
                    if temp_bool_0:
                        if temp_bool_1:
                            valid_org_num_num = None
                        else:
                            valid_org_num_num = temp_num_0                
                if temp_bool_0:
                    del(temp_str_list_0[0])
                    temp_len_1 = len(temp_str_list_0)
                    if temp_len_1 > 0:
                        for n in range(temp_len_1):
                            temp_str_list_0[n] = temp_str_list_0[n].strip()     
                        if len(temp_str_list_0[temp_len_1-1]) < 1:
                            del(temp_str_list_0[temp_len_1-1])
                            temp_len_1 -= 1
                        if (temp_len_1 > 0) & (temp_len_1 <= 1000):
                            temp_num_2 = valid_mani_num_num
                            if not valid_org_num_num is None:
                                if valid_org_num_num > temp_num_2:
                                    temp_num_2 = valid_org_num_num
                            temp_path_0 = self.basic_parameter[3][0]+"/"+"Report_valid_manipulation_number.csv"
                            temp_str_0 = chr(65279)
                            temp_str_0 = temp_str_0+'"'+"index"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"valid"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"aim: manipulation number"+'"'+","
                            temp_str_0 = temp_str_0+'"'+"organization number"+'"'
                            with open(temp_path_0, "w", encoding = "utf-8") as save_file:
                                save_file.write(temp_str_0)
                                save_file.close()
                            for n in range(temp_len_1):
                                temp_list_1 = self.csv_row_read(temp_str_list_0[n])
                                if len(temp_list_1) > temp_num_2:
                                    temp_bool_1 = True
                                    temp_str_2 = temp_list_1[valid_mani_num_num].strip()
                                    temp_bool_2 = True
                                    while temp_bool_2:
                                        temp_len_1 = len(temp_str_2)
                                        if temp_len_1 > 1:
                                            if (temp_str_2[0] == '"') & (temp_str_2[temp_len_1-1] == '"'):
                                                temp_str_2 = temp_str_2[1:(temp_len_1-1)]
                                            elif (temp_str_2[0] == "'") & (temp_str_2[temp_len_1-1] == "'"):
                                                temp_str_2 = temp_str_2[1:(temp_len_1-1)]
                                            else:
                                                temp_bool_2 = False
                                        else:
                                            temp_bool_2 = False
                                    temp_str_2 = temp_str_2.strip().upper()
                                    if valid_org_num_num is None:
                                        temp_str_3 = None
                                    else:
                                        temp_str_3 = temp_list_1[valid_org_num_num].strip()
                                        temp_bool_2 = True
                                        while temp_bool_2:
                                            temp_len_1 = len(temp_str_3)
                                            if temp_len_1 > 1:
                                                if (temp_str_3[0] == '"') & (temp_str_3[temp_len_1-1] == '"'):
                                                    temp_str_3 = temp_str_3[1:(temp_len_1-1)]
                                                elif (temp_str_3[0] == "'") & (temp_str_3[temp_len_1-1] == "'"):
                                                    temp_str_3 = temp_str_3[1:(temp_len_1-1)]
                                                else:
                                                    temp_bool_2 = False
                                            else:
                                                temp_bool_2 = False
                                        temp_str_3 = temp_str_3.strip()
                                        if len(temp_str_3) < 1:
                                            temp_str_3 = None
                                    if temp_bool_1:
                                        temp_bool_1 = self.number_manipulation_valid(temp_str_2, temp_str_3)
                                    temp_str_1 = "\n"
                                    temp_str_1 = temp_str_1+str(n+1)
                                    temp_str_1 = temp_str_1+","
                                    if temp_bool_1:
                                        temp_str_1 = temp_str_1+"1"
                                    else:
                                        temp_str_1 = temp_str_1+"0"
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_2 is None:
                                        temp_str_1 = temp_str_1+"'"+temp_str_2+"'"
                                    temp_str_1 = temp_str_1+","
                                    if not temp_str_3 is None:
                                        temp_str_1 = temp_str_1+"'"+temp_str_3+"'"
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_1)
                                        save_file.close()
                                else:
                                    temp_str_1 = "\n"
                                    temp_str_1 = temp_str_1+str(n+1)
                                    temp_str_1 = temp_str_1+","
                                    temp_str_1 = temp_str_1+"0"
                                    for n1 in range(2):
                                        temp_str_1 = temp_str_1+","
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_1)
                                        save_file.close()
                            self.check_valid_mani_num_multiple_state["text"] = "'"+temp_path_0+"' is output."
                        else:
                            self.check_valid_mani_num_multiple_state["text"] = "Fail."
                            showerror(title = "Error", 
                                      message = "The row number (excluding the first row, title row) should range within 1-1000.") 
                    else:
                        self.check_valid_mani_num_multiple_state["text"] = "Fail."
                        showerror(title = "Error", 
                                  message = "The row number (excluding the first row, title row) should range within 1-1000.") 
                else:
                    self.check_valid_mani_num_multiple_state["text"] = "Fail."
                    showerror(title = "Error", 
                              message = "The the first row, title row is in wrong format.")             
    
    def output_csv_page(self):
        output_csv_page_radio_frame = tk.LabelFrame(self.output_csv_page_frame, 
                                                    text = "Output *.csv: select a function", 
                                                    font = self.fonsize_s)
        output_csv_page_radio_frame.grid(row = 0, column = 0,
                                         padx = 5, pady = 5,
                                         sticky = tk.W)
        output_csv_page_radio_line_0 = tk.Frame(output_csv_page_radio_frame)
        output_csv_page_radio_line_0.grid(row = 0, column = 0,
                                          sticky = tk.W)
        output_csv_page_radio_line_1 = tk.Frame(output_csv_page_radio_frame)
        output_csv_page_radio_line_1.grid(row = 1, column = 0,
                                          sticky = tk.W)
        self.output_csv_page_radio_vari = tk.StringVar()
        self.output_csv_page_mem_radio = tk.Radiobutton(output_csv_page_radio_line_0, 
                                                        variable = self.output_csv_page_radio_vari, 
                                                        text = "*.csv of database of members' files", 
                                                        value = "mem", 
                                                        font = self.fonsize_s)
        self.output_csv_page_mem_radio.grid(row = 0, column = 0,
                                             padx = 2, pady = 2, 
                                             sticky = tk.W)
        self.output_csv_page_org_radio = tk.Radiobutton(output_csv_page_radio_line_0, 
                                                        variable = self.output_csv_page_radio_vari, 
                                                        text = "*.csv of organization", 
                                                        value = "org", 
                                                        font = self.fonsize_s)
        self.output_csv_page_org_radio.grid(row = 0, column = 1,
                                            padx = 2, pady = 2, 
                                            sticky = tk.W)
        ## command
        self.output_csv_page_mem_radio["command"] = self.output_csv_fun_select
        self.output_csv_page_org_radio["command"] = self.output_csv_fun_select
                                              
        # mem
        self.output_csv_page_mem_frame = tk.Frame(self.output_csv_page_frame)
        self.output_csv_page_mem_frame.grid_forget()
        output_csv_page_mem_frame_line_0 = tk.Frame(self.output_csv_page_mem_frame)
        output_csv_page_mem_frame_line_0.grid(row = 0, column = 0,
                                              padx = 2, pady = 2, 
                                              sticky = tk.W)
        temp_str_0 = "1. To scan *.iden and *.txt in the database, '"
        temp_str_0 = temp_str_0+self.basic_parameter[4][0]+"/"
        temp_str_0 = temp_str_0+"', and then to make copies as *.iden in the slots of database."
        ttk.Label(output_csv_page_mem_frame_line_0, 
                  text = temp_str_0,    
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              padx = 2, pady = 2,
                                              sticky = tk.W)
        output_csv_page_mem_frame_line_0_1 = tk.Frame(output_csv_page_mem_frame_line_0)
        output_csv_page_mem_frame_line_0_1.grid(row = 1, column = 0,
                                                sticky = tk.NW)
        output_csv_page_mem_frame_line_0_1_left = tk.Frame(output_csv_page_mem_frame_line_0_1)
        output_csv_page_mem_frame_line_0_1_left.grid(row = 0, column = 0,
                                                     padx = 2, pady = 2, 
                                                     sticky = tk.NW)
        self.output_csv_page_mem_scan_button = tk.Button(output_csv_page_mem_frame_line_0_1_left, 
                                                         text = "Scan", 
                                                         width = 6, 
                                                         font = self.fonsize_m)        
        self.output_csv_page_mem_scan_button.grid(row = 0, column = 0)
        output_csv_page_mem_scan_progressbar_frame = tk.Frame(output_csv_page_mem_frame_line_0_1_left)
        output_csv_page_mem_scan_progressbar_frame.grid(row = 1, column = 0,
                                                        padx = 2, pady = 2)
        self.output_csv_page_mem_scan_progressbar = ttk.Progressbar(output_csv_page_mem_scan_progressbar_frame, 
                                                                    length = 280, 
                                                                    mode="determinate", 
                                                                    orient = "horizontal")
        self.output_csv_page_mem_scan_progressbar.grid(row = 0, column = 0, 
                                                       columnspan = 2, 
                                                       sticky = tk.W)
        self.output_csv_page_mem_scan_state = ttk.Label(output_csv_page_mem_scan_progressbar_frame, 
                                                        text = "",    
                                                        font = self.fonsize_s)
        self.output_csv_page_mem_scan_state.grid(row = 1, column = 0, 
                                                 sticky = tk.E)
        self.output_csv_page_mem_scan_stop_button = tk.Button(output_csv_page_mem_scan_progressbar_frame, 
                                                         text = "Stop", 
                                                         width = 6, 
                                                         font = self.fonsize_s)        
        self.output_csv_page_mem_scan_stop_button.grid(row = 1, column = 1,  
                                                  sticky = tk.E)
        ttk.Separator(output_csv_page_mem_frame_line_0_1, 
                      orient="vertical").grid(row = 0, column = 1,
                                              sticky = tk.NS)
        output_csv_page_mem_frame_line_0_1_right = tk.Frame(output_csv_page_mem_frame_line_0_1)
        output_csv_page_mem_frame_line_0_1_right.grid(row = 0, column = 2,
                                                      padx = 2, pady = 2, 
                                                      sticky = tk.NW)
        output_csv_page_mem_scan_copy_frame = tk.Frame(output_csv_page_mem_frame_line_0_1_right)
        output_csv_page_mem_scan_copy_frame.grid(row = 0, column = 0,
                                                 padx = 2, pady = 2)
        ttk.Label(output_csv_page_mem_scan_copy_frame, 
                  text = "Copy the scanned results to: ",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        output_csv_page_mem_scan_copy_button_group_frame = tk.Frame(output_csv_page_mem_frame_line_0_1_right)
        output_csv_page_mem_scan_copy_button_group_frame.grid(row = 1, column = 0)
        self.output_csv_page_mem_copy_slot_1_button = tk.Button(output_csv_page_mem_scan_copy_button_group_frame, 
                                                                text = "Slot-1", 
                                                                width = 8, 
                                                                font = self.fonsize_s)        
        self.output_csv_page_mem_copy_slot_1_button.grid(row = 0, column = 0, 
                                                         sticky = tk.NW)
        self.output_csv_page_mem_copy_slot_2_button = tk.Button(output_csv_page_mem_scan_copy_button_group_frame, 
                                                                text = "Slot-2", 
                                                                width = 8, 
                                                                font = self.fonsize_s)        
        self.output_csv_page_mem_copy_slot_2_button.grid(row = 0, column = 1, 
                                                         sticky = tk.NW)
        self.output_csv_page_mem_copy_slot_3_button = tk.Button(output_csv_page_mem_scan_copy_button_group_frame, 
                                                                text = "Slot-3", 
                                                                width = 8, 
                                                                font = self.fonsize_s)        
        self.output_csv_page_mem_copy_slot_3_button.grid(row = 0, column = 2, 
                                                         sticky = tk.NW)
        self.output_csv_page_mem_copy_slot_4_button = tk.Button(output_csv_page_mem_scan_copy_button_group_frame, 
                                                                text = "Slot-4", 
                                                                width = 8, 
                                                                font = self.fonsize_s)        
        self.output_csv_page_mem_copy_slot_4_button.grid(row = 0, column = 3, 
                                                         sticky = tk.NW)
        self.output_csv_page_mem_copy_slot_5_button = tk.Button(output_csv_page_mem_scan_copy_button_group_frame, 
                                                                text = "Slot-5", 
                                                                width = 8, 
                                                                font = self.fonsize_s)        
        self.output_csv_page_mem_copy_slot_5_button.grid(row = 1, column = 0, 
                                                         sticky = tk.NW)
        self.output_csv_page_mem_copy_slot_6_button = tk.Button(output_csv_page_mem_scan_copy_button_group_frame, 
                                                                text = "Slot-6", 
                                                                width = 8, 
                                                                font = self.fonsize_s)        
        self.output_csv_page_mem_copy_slot_6_button.grid(row = 1, column = 1, 
                                                         sticky = tk.NW)
        self.output_csv_page_mem_copy_slot_7_button = tk.Button(output_csv_page_mem_scan_copy_button_group_frame, 
                                                                text = "Slot-7", 
                                                                width = 8, 
                                                                font = self.fonsize_s)        
        self.output_csv_page_mem_copy_slot_7_button.grid(row = 1, column = 2, 
                                                         sticky = tk.NW)
        self.output_csv_page_mem_copy_slot_8_button = tk.Button(output_csv_page_mem_scan_copy_button_group_frame, 
                                                                text = "Slot-8", 
                                                                width = 8, 
                                                                font = self.fonsize_s)        
        self.output_csv_page_mem_copy_slot_8_button.grid(row = 1, column = 3, 
                                                         sticky = tk.NW)
        output_csv_page_mem_copy_progressbar_frame = tk.Frame(output_csv_page_mem_frame_line_0_1_right)
        output_csv_page_mem_copy_progressbar_frame.grid(row = 0, column = 1,
                                                        rowspan = 2, 
                                                        padx = 2, pady = 2)
        self.output_csv_page_mem_copy_progressbar = ttk.Progressbar(output_csv_page_mem_copy_progressbar_frame, 
                                                                    length = 280, 
                                                                    mode="determinate", 
                                                                    orient = "horizontal")
        self.output_csv_page_mem_copy_progressbar.grid(row = 0, column = 0, 
                                                       columnspan = 2, 
                                                       sticky = tk.W)
        self.output_csv_page_mem_copy_state = ttk.Label(output_csv_page_mem_copy_progressbar_frame, 
                                                        text = "",    
                                                        font = self.fonsize_s)
        self.output_csv_page_mem_copy_state.grid(row = 1, column = 0, 
                                                 sticky = tk.E)
        self.output_csv_page_mem_copy_stop_button = tk.Button(output_csv_page_mem_copy_progressbar_frame, 
                                                              text = "Stop", 
                                                              width = 6, 
                                                              font = self.fonsize_s)        
        self.output_csv_page_mem_copy_stop_button.grid(row = 1, column = 1,  
                                                       sticky = tk.E)
        ttk.Separator(self.output_csv_page_mem_frame, 
                      orient="horizontal").grid(row = 1, column = 0,
                                                sticky = tk.EW)
        output_csv_page_mem_frame_line_1 = tk.Frame(self.output_csv_page_mem_frame)
        output_csv_page_mem_frame_line_1.grid(row = 2, column = 0,
                                              padx = 2, pady = 2, 
                                              sticky = tk.W)
        temp_str_0 = "2. To output *.csv into '"
        temp_str_0 = temp_str_0+self.basic_parameter[3][0]+"/"
        temp_str_0 = temp_str_0+"' from the slots of database, '"
        temp_str_0 = temp_str_0+self.basic_parameter[4][0]+"/"
        temp_str_0 = temp_str_0+"'."
        ttk.Label(output_csv_page_mem_frame_line_1, 
                  text = temp_str_0,    
                  wraplength = 1000, 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              padx = 2, pady = 2,
                                              sticky = tk.W)
        output_csv_page_mem_frame_line_1_1 = tk.Frame(output_csv_page_mem_frame_line_1)
        output_csv_page_mem_frame_line_1_1.grid(row = 1, column = 0,
                                                sticky = tk.NW)
        output_csv_page_mem_scan_output_button_group_frame = tk.Frame(output_csv_page_mem_frame_line_1_1)
        output_csv_page_mem_scan_output_button_group_frame.grid(row = 0, column = 0)
        self.output_csv_page_mem_output_slot_1_button = tk.Button(output_csv_page_mem_scan_output_button_group_frame, 
                                                                  text = "Slot-1", 
                                                                  width = 8, 
                                                                  font = self.fonsize_s)        
        self.output_csv_page_mem_output_slot_1_button.grid(row = 0, column = 0, 
                                                           sticky = tk.NW)
        self.output_csv_page_mem_output_slot_2_button = tk.Button(output_csv_page_mem_scan_output_button_group_frame, 
                                                                  text = "Slot-2", 
                                                                  width = 8, 
                                                                  font = self.fonsize_s)        
        self.output_csv_page_mem_output_slot_2_button.grid(row = 0, column = 1, 
                                                           sticky = tk.NW)
        self.output_csv_page_mem_output_slot_3_button = tk.Button(output_csv_page_mem_scan_output_button_group_frame, 
                                                                  text = "Slot-3", 
                                                                  width = 8, 
                                                                  font = self.fonsize_s)        
        self.output_csv_page_mem_output_slot_3_button.grid(row = 0, column = 2, 
                                                           sticky = tk.NW)
        self.output_csv_page_mem_output_slot_4_button = tk.Button(output_csv_page_mem_scan_output_button_group_frame, 
                                                                  text = "Slot-4", 
                                                                  width = 8, 
                                                                  font = self.fonsize_s)        
        self.output_csv_page_mem_output_slot_4_button.grid(row = 0, column = 3, 
                                                           sticky = tk.NW)
        self.output_csv_page_mem_output_slot_5_button = tk.Button(output_csv_page_mem_scan_output_button_group_frame, 
                                                                  text = "Slot-5", 
                                                                  width = 8, 
                                                                  font = self.fonsize_s)        
        self.output_csv_page_mem_output_slot_5_button.grid(row = 1, column = 0, 
                                                           sticky = tk.NW)
        self.output_csv_page_mem_output_slot_6_button = tk.Button(output_csv_page_mem_scan_output_button_group_frame, 
                                                                  text = "Slot-6", 
                                                                  width = 8, 
                                                                  font = self.fonsize_s)        
        self.output_csv_page_mem_output_slot_6_button.grid(row = 1, column = 1, 
                                                           sticky = tk.NW)
        self.output_csv_page_mem_output_slot_7_button = tk.Button(output_csv_page_mem_scan_output_button_group_frame, 
                                                                  text = "Slot-7", 
                                                                  width = 8, 
                                                                  font = self.fonsize_s)        
        self.output_csv_page_mem_output_slot_7_button.grid(row = 1, column = 2, 
                                                           sticky = tk.NW)
        self.output_csv_page_mem_output_slot_8_button = tk.Button(output_csv_page_mem_scan_output_button_group_frame, 
                                                                  text = "Slot-8", 
                                                                  width = 8, 
                                                                  font = self.fonsize_s)        
        self.output_csv_page_mem_output_slot_8_button.grid(row = 1, column = 3, 
                                                           sticky = tk.NW)
        output_csv_page_mem_output_progressbar_frame = tk.Frame(output_csv_page_mem_frame_line_1_1)
        output_csv_page_mem_output_progressbar_frame.grid(row = 0, column = 1,
                                                          padx = 2, pady = 2)
        self.output_csv_page_mem_output_progressbar = ttk.Progressbar(output_csv_page_mem_output_progressbar_frame, 
                                                                    length = 280, 
                                                                    mode="determinate", 
                                                                    orient = "horizontal")
        self.output_csv_page_mem_output_progressbar.grid(row = 0, column = 0, 
                                                       columnspan = 2, 
                                                       sticky = tk.W)
        self.output_csv_page_mem_output_state = ttk.Label(output_csv_page_mem_output_progressbar_frame, 
                                                          text = "",    
                                                          font = self.fonsize_s)
        self.output_csv_page_mem_output_state.grid(row = 1, column = 0, 
                                                   sticky = tk.E)
        self.output_csv_page_mem_output_stop_button = tk.Button(output_csv_page_mem_output_progressbar_frame, 
                                                                text = "Stop", 
                                                                width = 6, 
                                                                font = self.fonsize_s)        
        self.output_csv_page_mem_output_stop_button.grid(row = 1, column = 1,  
                                                         sticky = tk.E)
        ttk.Separator(self.output_csv_page_mem_frame, 
                      orient="horizontal").grid(row = 3, column = 0,
                                                sticky = tk.EW)
        self.output_csv_page_mem_state = ttk.Label(self.output_csv_page_mem_frame, 
                                                   text = "", 
                                                   wraplength = 1000, 
                                                   font = self.fonsize_s)
        self.output_csv_page_mem_state.grid(row = 4, column = 0, 
                                            sticky = tk.E)
        self.output_csv_page_cur_process_vari = ""
        self.output_csv_mem_name_copy_from_list = None
        self.output_csv_mem_name_copy_list = None
        self.output_csv_mem_content_list = None
        ## command                                        
        self.output_csv_page_mem_scan_button["command"] = self.output_csv_fun_scan
        self.output_csv_page_mem_scan_stop_button["command"] = lambda in_str = "scan": self.output_csv_fun_mem_stop(in_str)                 
        self.output_csv_page_mem_copy_slot_1_button["command"] = lambda in_num = 0: self.output_csv_fun_copy(in_num)
        self.output_csv_page_mem_copy_slot_2_button["command"] = lambda in_num = 1: self.output_csv_fun_copy(in_num)
        self.output_csv_page_mem_copy_slot_3_button["command"] = lambda in_num = 2: self.output_csv_fun_copy(in_num)
        self.output_csv_page_mem_copy_slot_4_button["command"] = lambda in_num = 3: self.output_csv_fun_copy(in_num)
        self.output_csv_page_mem_copy_slot_5_button["command"] = lambda in_num = 4: self.output_csv_fun_copy(in_num)
        self.output_csv_page_mem_copy_slot_6_button["command"] = lambda in_num = 5: self.output_csv_fun_copy(in_num)
        self.output_csv_page_mem_copy_slot_7_button["command"] = lambda in_num = 6: self.output_csv_fun_copy(in_num)
        self.output_csv_page_mem_copy_slot_8_button["command"] = lambda in_num = 7: self.output_csv_fun_copy(in_num)
        self.output_csv_page_mem_copy_stop_button["command"] = lambda in_str = "copy": self.output_csv_fun_mem_stop(in_str)  
        self.output_csv_page_mem_output_slot_1_button["command"] = lambda in_num = 0: self.output_csv_fun_output(in_num)
        self.output_csv_page_mem_output_slot_2_button["command"] = lambda in_num = 1: self.output_csv_fun_output(in_num)
        self.output_csv_page_mem_output_slot_3_button["command"] = lambda in_num = 2: self.output_csv_fun_output(in_num)
        self.output_csv_page_mem_output_slot_4_button["command"] = lambda in_num = 3: self.output_csv_fun_output(in_num)
        self.output_csv_page_mem_output_slot_5_button["command"] = lambda in_num = 4: self.output_csv_fun_output(in_num)
        self.output_csv_page_mem_output_slot_6_button["command"] = lambda in_num = 5: self.output_csv_fun_output(in_num)
        self.output_csv_page_mem_output_slot_7_button["command"] = lambda in_num = 6: self.output_csv_fun_output(in_num)
        self.output_csv_page_mem_output_slot_8_button["command"] = lambda in_num = 7: self.output_csv_fun_output(in_num)
        self.output_csv_page_mem_output_stop_button["command"] = lambda in_str = "output": self.output_csv_fun_mem_stop(in_str)  
        
        # org
        self.output_csv_page_org_frame = tk.Frame(self.output_csv_page_frame)
        self.output_csv_page_org_frame.grid_forget()
        output_csv_page_org_frame_line_0 = tk.Frame(self.output_csv_page_org_frame)
        output_csv_page_org_frame_line_0.grid(row = 0, column = 0,
                                              padx = 2, pady = 2, 
                                              sticky = tk.W)
        self.output_csv_page_org_mani_list_button = tk.Button(output_csv_page_org_frame_line_0, 
                                                              text = "Output *.csv of manipulation list", 
                                                              width = 35, 
                                                              font = self.fonsize_s)        
        self.output_csv_page_org_mani_list_button.grid(row = 0, column = 0, 
                                                       padx = 2, pady = 2, 
                                                       sticky = tk.W)
        self.output_csv_page_org_mani_list_state = ttk.Label(output_csv_page_org_frame_line_0, 
                                                             text = "",                          
                                                             font = self.fonsize_s)
        self.output_csv_page_org_mani_list_state.grid(row = 1, column = 0,
                                                      sticky = tk.W)
        self.output_csv_page_org_mani_list_bool = False
        ttk.Separator(self.output_csv_page_org_frame, 
                      orient="horizontal").grid(row = 1, column = 0,
                                                sticky = tk.EW)
        output_csv_page_org_frame_line_1 = tk.Frame(self.output_csv_page_org_frame)
        output_csv_page_org_frame_line_1.grid(row = 2, column = 0,
                                              padx = 2, pady = 2, 
                                              sticky = tk.W)
        self.output_csv_page_org_org_list_button = tk.Button(output_csv_page_org_frame_line_1, 
                                                             text = "Output *.csv of organization list", 
                                                             width = 35, 
                                                             font = self.fonsize_s)        
        self.output_csv_page_org_org_list_button.grid(row = 0, column = 0, 
                                                      padx = 2, pady = 2, 
                                                      sticky = tk.W)
        self.output_csv_page_org_org_list_state = ttk.Label(output_csv_page_org_frame_line_1, 
                                                            text = "",                          
                                                            font = self.fonsize_s)
        self.output_csv_page_org_org_list_state.grid(row = 1, column = 0,
                                                     sticky = tk.W)      
        self.output_csv_page_org_org_list_bool = False  
        ## command
        self.output_csv_page_org_mani_list_button["command"] = self.output_csv_fun_mani
        self.output_csv_page_org_org_list_button["command"] = self.output_csv_fun_org
    
    def output_csv_fun_select(self):
        if not self.cur_progress_bool:
            temp_str = self.output_csv_page_radio_vari.get()
            if temp_str == "mem":
                self.output_csv_page_mem_frame.grid(row = 1, column = 0,
                                                    padx = 5, pady = 5, 
                                                    sticky = tk.NW)
                self.output_csv_page_org_frame.grid_forget()
            elif temp_str == "org":
                self.output_csv_page_mem_frame.grid_forget()
                self.output_csv_page_org_frame.grid(row = 1, column = 0,
                                                    padx = 5, pady = 5, 
                                                    sticky = tk.NW) 
                if not self.cur_org_file_name is None:
                    self.output_csv_page_org_mani_list_state["text"] = "File from 'assets/"+self.cur_org_file_name+"'."
                    self.output_csv_page_org_mani_list_bool = True
                else:
                    self.output_csv_page_org_mani_list_state["text"] = "No *.dat file."
                    self.output_csv_page_org_mani_list_bool = False
                if not self.basic_org_list is None:
                    if not self.basic_org_list[1] is None:
                        if self.basic_org_list[0][0][0:3].upper() == self.cur_org[0][0][0:3].upper():
                            self.output_csv_page_org_org_list_state["text"] = "Preread file from 'assets/OrganizationList.dat'."
                            self.output_csv_page_org_org_list_bool = True
                        else:
                            self.output_csv_page_org_org_list_state["text"] = "Cannot output from 'assets/OrganizationList.dat'."
                            self.output_csv_page_org_org_list_bool = False
                    else:
                        self.output_csv_page_org_org_list_state["text"] = "Cannot read from 'assets/OrganizationList.dat'."
                        self.output_csv_page_org_org_list_bool = False
                else:
                    self.output_csv_page_org_org_list_state["text"] = "No *.dat file as 'assets/OrganizationList.dat'."
                    self.output_csv_page_org_org_list_bool = False
        else:
            self.output_csv_page_mem_radio.select()
    
    def output_csv_fun_scan(self):
        if not self.cur_progress_bool:
            if os.path.exists(self.cur_org_file_name):
                with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                    read_text = read_file.read()
                    self.cur_org = self.reading_str_text_org(read_text)
                if not self.cur_org is None:
                    temp_num_0 = -1
                    for n in range(len(self.cur_org[2])):
                        if self.cur_org[2][n] == self.cur_mani_num:
                            temp_num_0 = n
                            break
                    if temp_num_0 >= 0:
                        temp_bool_0 = self.cur_org[3][temp_num_0]
                    else:
                        temp_bool_0 = False
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
            if not temp_bool_0:
                showerror(title = "Error", 
                          message = "No privilege to do so.") 
            else:
                answer = askyesno(title="Scan",
                                  message="Are you sure that you want to start the scanning?")
                if answer:
                    self.cur_progress_bool = True
                    self.output_csv_page_cur_process_vari = "scan"
                    self.output_csv_page_mem_scan_progressbar["value"] = 0
                    self.output_csv_page_mem_scan_state["text"] = ""
                    self.output_csv_page_mem_copy_progressbar["value"] = 0
                    self.output_csv_page_mem_copy_state["text"] = ""
                    temp_file_list = os.scandir(self.basic_parameter[4][0])
                    temp_file_name_list = []
                    temp_file_type_if_iden_list = []
                    temp_bool_0 = True
                    for e in temp_file_list:
                        if self.cur_progress_bool:
                            temp_str_0 = e.name
                            temp_len_0 = len(temp_str_0)
                            if temp_len_0 > 4:
                                if temp_str_0[-4:].upper() == ".TXT":
                                    temp_file_name_list.append(temp_str_0)
                                    temp_file_type_if_iden_list.append(False)
                                elif temp_len_0 > 5:
                                    if temp_str_0[-5:].upper() == ".IDEN":
                                        temp_file_name_list.append(temp_str_0)
                                        temp_file_type_if_iden_list.append(True)
                            self.update()
                            if len(temp_file_type_if_iden_list) > 20000:
                                temp_bool_0 = False
                                showerror(title = "Error", 
                                          message = "There are more than 20 000 *.txt or *.iden files.")
                                break
                        else:
                            break
                    temp_bool_2 = False
                    if self.cur_progress_bool:
                        if temp_bool_0:
                            temp_len_0 = len(temp_file_name_list)
                            if temp_len_0 > 0:
                                self.output_csv_mem_name_copy_from_list = []
                                self.output_csv_mem_name_copy_list = []
                                self.output_csv_mem_content_list = []
                                temp_path_0 = self.basic_parameter[4][0]+"/"+"Report_scan.csv"
                                temp_str_0 = chr(65279)
                                temp_str_0 = temp_str_0+'"'+"index"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"valid"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"if duplicate with previous"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"file name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"mixed number"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"member number"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"given name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"middle name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"family name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"type of another name / virtual name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"another name / virtual name"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"addition (@ or #)"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"date"+'"'+","
                                temp_str_0 = temp_str_0+'"'+"time"+'"'
                                with open(temp_path_0, "w", encoding = "utf-8") as save_file:
                                    save_file.write(temp_str_0)
                                    save_file.close()
                                for n in range(temp_len_0):
                                    if self.cur_progress_bool:
                                        temp_bool_1 = True
                                        with open(self.basic_parameter[4][0]+"/"+temp_file_name_list[n], "r", encoding = "utf-8") as read_file:
                                            read_text = read_file.read()
                                        if temp_file_type_if_iden_list[n]:
                                            temp_list_0 = self.reading_str_text_mem(read_text)
                                        else:
                                            temp_list_0 = self.reading_str_text_member_lang(read_text)
                                        if not temp_list_0 is None:
                                            if temp_list_0[0][0][0:3].upper() == self.cur_org[0][0][0:3].upper():
                                                temp_str_0 = self.forming_str_text_member(temp_list_0[0], temp_list_0[1], 
                                                                                          temp_list_0[2], temp_list_0[3], 
                                                                                          temp_list_0[4])
                                                temp_bool_1 = (not temp_str_0 is None)
                                            else:
                                                temp_bool_1 = False
                                        else:
                                            temp_bool_1 = False
                                        if temp_bool_1:
                                            temp_str_1 = self.num_mix_64_2_8(temp_list_0[0][0])
                                            if not temp_str_1 in self.output_csv_mem_name_copy_list:
                                                self.output_csv_mem_name_copy_from_list.append(temp_file_name_list[n])
                                                self.output_csv_mem_name_copy_list.append(temp_str_1)
                                                self.output_csv_mem_content_list.append(temp_str_0)
                                                if not temp_bool_2:
                                                    temp_bool_2 = True
                                                temp_str_1 = "\n"
                                                temp_str_1 = temp_str_1+str(n+1)
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+"1"
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+"0"
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+temp_file_name_list[n]
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+"'"+temp_list_0[0][0]+"'"
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+"'"+temp_list_0[0][1]+"'"
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[1][0]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[1][1]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[1][2]+'"'
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[2][0]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[2][1]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[2][2]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[3][0]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[3][1]+'"'
                                                with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                                    save_file.write(temp_str_1)
                                                    save_file.close()
                                            else:
                                                temp_str_1 = "\n"
                                                temp_str_1 = temp_str_1+str(n+1)
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+"1"
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+"1"
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+temp_file_name_list[n]
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+"'"+temp_list_0[0][0]+"'"
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+"'"+temp_list_0[0][1]+"'"
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[1][0]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[1][1]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[1][2]+'"'
                                                temp_str_1 = temp_str_1+","
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[2][0]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[2][1]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[2][2]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[3][0]+'"'
                                                temp_str_1 = temp_str_1+","                                            
                                                temp_str_1 = temp_str_1+'"'+temp_list_0[3][1]+'"'
                                                with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                                    save_file.write(temp_str_1)
                                                    save_file.close()
                                        else:
                                            temp_str_1 = "\n"
                                            temp_str_1 = temp_str_1+str(n+1)
                                            temp_str_1 = temp_str_1+","
                                            temp_str_1 = temp_str_1+"0"
                                            temp_str_1 = temp_str_1+","
                                            temp_str_1 = temp_str_1+""
                                            temp_str_1 = temp_str_1+","
                                            temp_str_1 = temp_str_1+temp_file_name_list[n]
                                            for n1 in range(10):
                                                temp_str_1 = temp_str_1+","
                                            with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                                save_file.write(temp_str_1)
                                                save_file.close()
                                    else:
                                        break
                                    temp_num_1 = n+1
                                    temp_float_0 = (temp_num_1/temp_len_0)*100
                                    self.output_csv_page_mem_scan_state["text"] = str(round(temp_float_0, 2))+"%"
                                    self.output_csv_page_mem_scan_progressbar["value"] = int(temp_float_0)
                                    temp_str_1 = str(temp_num_1)+"/"+str(temp_len_0)
                                    temp_str_1 = temp_str_1+" scanned from database, '"
                                    temp_str_1 = temp_str_1+self.basic_parameter[4][0]+"/'."
                                    self.output_csv_page_mem_state["text"] = temp_str_1
                                    self.update()
                            else:
                                showerror(title = "Error", 
                                          message = "There is no *.txt or *.iden files.")
                    if self.cur_progress_bool:
                        self.cur_progress_bool = False
                        self.output_csv_page_cur_process_vari = ""
                        if temp_bool_2:
                            self.output_csv_page_mem_scan_state["text"] = "Finished. "
                            self.output_csv_page_mem_state["text"] = "'"+temp_path_0+"' is output, with "+str(len(self.output_csv_mem_name_copy_list))+" valid results."
                        else:
                            self.output_csv_mem_name_copy_from_list = None
                            self.output_csv_mem_name_copy_list = None
                            self.output_csv_mem_content_list = None
                            self.output_csv_page_mem_state["text"] = "No valid result."
                    else:
                        if temp_bool_2:
                            self.output_csv_page_mem_state["text"] = "'"+temp_path_0+"' is output."
                        else:
                            self.output_csv_mem_name_copy_from_list = None
                            self.output_csv_mem_name_copy_list = None
                            self.output_csv_mem_content_list = None      
                            self.output_csv_page_mem_state["text"] = "No valid result."                  
                        self.output_csv_page_cur_process_vari = ""
    
    def output_csv_fun_copy(self, in_num):
        if not self.cur_progress_bool:
            if os.path.exists(self.cur_org_file_name):
                with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                    read_text = read_file.read()
                    self.cur_org = self.reading_str_text_org(read_text)
                if not self.cur_org is None:
                    temp_num_0 = -1
                    for n in range(len(self.cur_org[2])):
                        if self.cur_org[2][n] == self.cur_mani_num:
                            temp_num_0 = n
                            break
                    if temp_num_0 >= 0:
                        temp_bool_0 = self.cur_org[3][temp_num_0]
                    else:
                        temp_bool_0 = False
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
            if not temp_bool_0:
                showerror(title = "Error", 
                          message = "No privilege to do so.") 
            else:
                temp_str_0 = "Slot-"+str(in_num+1)
                temp_str_1 = "Are you sure that you want to start the copying to "
                temp_str_1 = temp_str_1+temp_str_0+"?"
                answer = askyesno(title="Copy",
                                  message=temp_str_1)
                if answer:
                    if self.output_csv_mem_content_list is None:
                        showerror(title = "Error", 
                                  message = "There is no scanned result.")                         
                    else:
                        self.cur_progress_bool = True
                        self.output_csv_page_cur_process_vari = "copy"
                        temp_path_0 = self.basic_parameter[4][0]+"/"+"Report_copy_to_"+temp_str_0+".csv"
                        temp_str_1 = chr(65279)
                        temp_str_1 = temp_str_1+'"'+"index"+'"'+","
                        temp_str_1 = temp_str_1+'"'+"if successfully copied"+'"'+","
                        temp_str_1 = temp_str_1+'"'+"original file name in database"+'"'+","
                        temp_str_1 = temp_str_1+'"'+"file name in "+temp_str_0+'"'
                        with open(temp_path_0, "w", encoding = "utf-8") as save_file:
                            save_file.write(temp_str_1)
                            save_file.close()
                        temp_len_0 = len(self.output_csv_mem_content_list)
                        for n in range(temp_len_0):
                            if self.cur_progress_bool:
                                temp_str_3 = self.output_csv_mem_name_copy_list[n]+".iden"
                                temp_path_1 = self.basic_parameter[4][1][in_num]+"/"+temp_str_3
                                if os.path.exists(temp_path_1):
                                    temp_str_2 = "\n"
                                    temp_str_2 = temp_str_2+str(n+1)
                                    temp_str_2 = temp_str_2+","
                                    temp_str_2 = temp_str_2+"0"
                                    temp_str_2 = temp_str_2+","
                                    temp_str_2 = temp_str_2+self.output_csv_mem_name_copy_from_list[n]
                                    temp_str_2 = temp_str_2+","
                                    temp_str_2 = temp_str_2+temp_str_3
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_2)
                                        save_file.close()
                                else:
                                    with open(temp_path_1, "w", encoding = "utf-8") as save_file:
                                        save_file.write(self.output_csv_mem_content_list[n])
                                        save_file.close()
                                    temp_str_2 = "\n"
                                    temp_str_2 = temp_str_2+str(n+1)
                                    temp_str_2 = temp_str_2+","
                                    temp_str_2 = temp_str_2+"1"
                                    temp_str_2 = temp_str_2+","
                                    temp_str_2 = temp_str_2+self.output_csv_mem_name_copy_from_list[n]
                                    temp_str_2 = temp_str_2+","
                                    temp_str_2 = temp_str_2+temp_str_3
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_2)
                                        save_file.close()
                                temp_num_1 = n+1
                                temp_float_0 = (temp_num_1/temp_len_0)*100
                                self.output_csv_page_mem_copy_state["text"] = str(round(temp_float_0, 2))+"%"
                                self.output_csv_page_mem_copy_progressbar["value"] = int(temp_float_0)
                                temp_str_2 = str(temp_num_1)+"/"+str(temp_len_0)
                                temp_str_2 = temp_str_2+" copied to "+temp_str_0
                                temp_str_2 = temp_str_2+", '"+self.basic_parameter[4][1][in_num]+"/'."
                                self.output_csv_page_mem_state["text"] = temp_str_2
                                self.update()
                            else:
                                break
                        if self.cur_progress_bool:
                            self.cur_progress_bool = False
                            self.output_csv_page_cur_process_vari = ""
                            self.output_csv_page_mem_copy_state["text"] = "Finished. "
                            self.output_csv_page_mem_state["text"] = "'"+temp_path_0+"' is output."
                        else:
                            self.output_csv_page_cur_process_vari = ""
                    
    def output_csv_fun_output(self, in_num):
        if not self.cur_progress_bool:
            if os.path.exists(self.cur_org_file_name):
                with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                    read_text = read_file.read()
                    self.cur_org = self.reading_str_text_org(read_text)
                if not self.cur_org is None:
                    temp_num_0 = -1
                    for n in range(len(self.cur_org[2])):
                        if self.cur_org[2][n] == self.cur_mani_num:
                            temp_num_0 = n
                            break
                    if temp_num_0 >= 0:
                        temp_bool_0 = self.cur_org[3][temp_num_0]
                    else:
                        temp_bool_0 = False
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
            if not temp_bool_0:
                showerror(title = "Error", 
                          message = "No privilege to do so.") 
            else:
                temp_str_0 = "Slot-"+str(in_num+1)
                temp_str_1 = "Are you sure that you want to start to output *.csv from "
                temp_str_1 = temp_str_1+temp_str_0+"?"
                answer = askyesno(title="Output",
                                  message=temp_str_1)
                if answer:
                    temp_file_list = os.scandir(self.basic_parameter[4][1][in_num])
                    temp_file_name_list = []
                    for e in temp_file_list:
                        temp_file_name_list.append(e.name)
                    temp_len_0 = len(temp_file_name_list)
                    if temp_len_0 < 1:
                        temp_str_1 = "There is no file in "
                        temp_str_1 = temp_str_1+temp_str_0
                        temp_str_1 = temp_str_1+", '"+self.basic_parameter[4][1][in_num]
                        temp_str_1 = temp_str_1+"/'."
                        showerror(title = "Error", 
                                  message = temp_str_1)
                    else:
                        self.cur_progress_bool = True
                        self.output_csv_page_cur_process_vari = "output"
                        temp_num_0 = 0
                        temp_num_1 = 1
                        temp_success_num = 0
                        temp_fail_num = 0
                        temp_path_0 = self.basic_parameter[3][1][in_num]+"/"
                        temp_path_0 = temp_path_0+"Report_failure_files.txt"
                        with open(temp_path_0, "w", encoding = "utf-8") as save_file:
                            save_file.write("")
                            save_file.close()
                        temp_path_1 = self.basic_parameter[3][1][in_num]+"/"
                        temp_path_1 = temp_path_1+"Report_amount.txt"
                        with open(temp_path_1, "w", encoding = "utf-8") as save_file:
                            save_file.write("")
                            save_file.close()
                        for n in range(temp_len_0):
                            if self.cur_progress_bool:
                                temp_bool_1 = True
                                temp_path_3 = self.basic_parameter[4][1][in_num]+"/"+temp_file_name_list[n]
                                if len(temp_file_name_list[n]) == 47:
                                    if temp_file_name_list[n][-5:].upper() == ".IDEN":
                                        with open(temp_path_3, "r", encoding = "utf-8") as read_file:
                                            read_text = read_file.read()
                                        temp_list_0 = self.reading_str_text_mem(read_text)
                                        if not temp_list_0 is None:
                                            if temp_list_0[0][0][0:3].upper() == self.cur_org[0][0][0:3].upper():
                                                temp_str_2 = self.num_mix_64_2_8(temp_list_0[0][0])
                                                if temp_file_name_list[n][:42] == temp_str_2:
                                                    temp_str_2 = "\n"
                                                    temp_str_2 = temp_str_2+str(temp_num_0+1)
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+"'"+temp_list_0[0][0]+"'"
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+"'"+temp_list_0[0][1]+"'"
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+"'"+temp_list_0[3][0]+"'"
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+"'"+temp_list_0[3][1]+"'"
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+'"'+temp_list_0[1][0]+'"'
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+'"'+temp_list_0[1][1]+'"'
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+'"'+temp_list_0[1][2]+'"'
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+'"'+temp_list_0[2][0]+'"'
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+'"'+temp_list_0[2][1]+'"'
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+'"'+temp_list_0[2][2]+'"'
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+"'"+temp_list_0[4][3]+"'"
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+"'"+temp_list_0[4][0]+"'"
                                                    temp_str_2 = temp_str_2+","
                                                    if not self.basic_org_list is None:
                                                        temp_num_2 = -1
                                                        for n1 in range(len(self.basic_org_list[1])):
                                                            if self.basic_org_list[1][n1][0] == temp_list_0[4][0]:
                                                                temp_num_2 = n1
                                                                break
                                                        if temp_num_2 >= 0:
                                                            temp_str_2 = temp_str_2+'"'+self.basic_org_list[1][temp_num_2][1]+'"'
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+"'"+temp_list_0[4][1]+"'"
                                                    temp_str_2 = temp_str_2+","
                                                    temp_str_2 = temp_str_2+"'"+temp_list_0[4][2]+"'"
                                                else:
                                                    temp_bool_1 = False                                            
                                            else:
                                                temp_bool_1 = False
                                        else:
                                            temp_bool_1 = False
                                    else:
                                        temp_bool_1 = False
                                else:
                                    temp_bool_1 = False
                                if temp_bool_1:
                                    temp_path_2 = self.basic_parameter[3][1][in_num]+"/"
                                    temp_path_2 = temp_path_2+"Table_"
                                    temp_path_2 = temp_path_2+str(temp_num_1)+".csv"
                                    if temp_num_0 == 0:
                                        temp_str_3 = chr(65279)
                                        temp_str_3 = temp_str_3+'"'+"index"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"mixed number"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"member number"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"issued date"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"issued time"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"English given name"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"English middle name"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"English family name"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"type of another name / virtual name"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"another name / virtual name"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"addition (@ or #) of another name / virtual name"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"issuer's manipulation number"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"issuer's organization number"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"issuer's organization name"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"created date of the organization"+'"'+","
                                        temp_str_3 = temp_str_3+'"'+"created time of the organization"+'"'
                                        with open(temp_path_2, "w", encoding = "utf-8") as save_file:
                                            save_file.write(temp_str_3)
                                            save_file.close()
                                    with open(temp_path_2, "a", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_2)
                                        save_file.close()
                                    temp_success_num += 1
                                    temp_str_4 = "Successful: "
                                    temp_str_4 = temp_str_4+str(temp_success_num)
                                    temp_str_4 = temp_str_4+"\nFailure: "
                                    temp_str_4 = temp_str_4+str(temp_fail_num)
                                    temp_str_4 = temp_str_4+"\nTotal file number in '"+self.basic_parameter[4][1][in_num]+"/': "
                                    temp_str_4 = temp_str_4+str(temp_success_num+temp_fail_num)
                                    temp_str_4 = temp_str_4+"\nTotal table number in '"+self.basic_parameter[3][1][in_num]+"/': "
                                    temp_str_4 = temp_str_4+str(temp_num_1)
                                    with open(temp_path_1, "w", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_4)
                                        save_file.close()
                                    temp_num_0 += 1
                                    if temp_num_0 >= 50000:
                                        temp_num_0 = 0
                                        temp_num_1 += 1
                                else:
                                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                                        save_file.write("\n"+temp_path_3)
                                        save_file.close()
                                    temp_fail_num += 1
                                    temp_str_4 = "Successful: "
                                    temp_str_4 = temp_str_4+str(temp_success_num)
                                    temp_str_4 = temp_str_4+"\nFailure: "
                                    temp_str_4 = temp_str_4+str(temp_fail_num)
                                    temp_str_4 = temp_str_4+"\nTotal file number in '"+self.basic_parameter[4][1][in_num]+"/': "
                                    temp_str_4 = temp_str_4+str(temp_success_num+temp_fail_num)
                                    temp_str_4 = temp_str_4+"\nTotal table number in '"+self.basic_parameter[3][1][in_num]+"/': "
                                    temp_str_4 = temp_str_4+str(temp_num_1)
                                    with open(temp_path_1, "w", encoding = "utf-8") as save_file:
                                        save_file.write(temp_str_4)
                                        save_file.close()
                                temp_num_2 = n+1
                                temp_float_0 = (temp_num_2/temp_len_0)*100
                                self.output_csv_page_mem_output_state["text"] = str(round(temp_float_0, 2))+"%"
                                self.output_csv_page_mem_output_progressbar["value"] = int(temp_float_0)
                                temp_str_3 = str(temp_num_2)+"/"+str(temp_len_0)
                                temp_str_3 = temp_str_3+", in which "+str(temp_success_num)
                                temp_str_3 = temp_str_3+" are output into the table in '"+self.basic_parameter[3][1][in_num]+"/'."
                                self.output_csv_page_mem_state["text"] = temp_str_3
                                self.update()
                            else:
                                break
                        if self.cur_progress_bool:
                            self.cur_progress_bool = False
                            self.output_csv_page_cur_process_vari = ""
                            self.output_csv_page_mem_output_state["text"] = "Finished. "
                            self.output_csv_page_mem_state["text"] = "'"+temp_path_1+"' is output."
                        else:
                            self.output_csv_page_cur_process_vari = ""
    
    def output_csv_fun_mem_stop(self, in_str):
        if self.cur_progress_bool:
            if in_str == self.output_csv_page_cur_process_vari:
                answer = askyesno(title="Stop current process",
                                  message="Are you sure that you want to stop the current process?")
                if answer:  
                    self.cur_progress_bool = False
                    self.output_csv_page_cur_process_vari = ""
                    if in_str == "scan":
                        self.output_csv_page_mem_scan_state["text"] = "Stopped. "
                    elif in_str == "copy":
                        self.output_csv_page_mem_copy_state["text"] = "Stopped. "
                    elif in_str == "output":
                        self.output_csv_page_mem_output_state["text"] = "Stopped. "
    
    def output_csv_fun_mani(self):
        if self.output_csv_page_org_mani_list_bool: 
            if os.path.exists(self.cur_org_file_name):
                with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                    read_text = read_file.read()
                    self.cur_org = self.reading_str_text_org(read_text)
                if not self.cur_org is None:
                    temp_num_0 = -1
                    for n in range(len(self.cur_org[2])):
                        if self.cur_org[2][n] == self.cur_mani_num:
                            temp_num_0 = n
                            break
                    if temp_num_0 >= 0:
                        temp_bool_0 = self.cur_org[3][temp_num_0]
                    else:
                        temp_bool_0 = False
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
            if not temp_bool_0:
                showerror(title = "Error", 
                          message = "No privilege to do so.") 
            else:
                temp_str_0 = chr(65279)
                temp_str_0 = temp_str_0+'"'+"index"+'"'+","
                temp_str_0 = temp_str_0+'"'+"if enabled"+'"'+","
                temp_str_0 = temp_str_0+'"'+"manipulation number"+'"'+","
                temp_str_0 = temp_str_0+'"'+"current organization number"+'"'+","
                temp_str_0 = temp_str_0+'"'+"current organization name"+'"'+","
                temp_str_0 = temp_str_0+'"'+"if creator"+'"'+","
                temp_str_0 = temp_str_0+'"'+"created date"+'"'+","
                temp_str_0 = temp_str_0+'"'+"created time"+'"'+","
                temp_str_0 = temp_str_0+'"'+"if administrator"+'"'+","
                temp_str_0 = temp_str_0+'"'+"member number"+'"'+","
                temp_str_0 = temp_str_0+'"'+"name type"+'"'+","
                temp_str_0 = temp_str_0+'"'+"English given name"+'"'+","
                temp_str_0 = temp_str_0+'"'+"English middle name"+'"'+","
                temp_str_0 = temp_str_0+'"'+"English family name"+'"'+","
                temp_str_0 = temp_str_0+'"'+"type of another name / virtual name"+'"'+","
                temp_str_0 = temp_str_0+'"'+"another name / virtual name"+'"'+","
                temp_str_0 = temp_str_0+'"'+"addition (@ or #) of another name / virtual name"+'"'+","
                temp_str_0 = temp_str_0+'"'+"issuer's organization number"+'"'+","
                temp_str_0 = temp_str_0+'"'+"issuer's created date"+'"'+","
                temp_str_0 = temp_str_0+'"'+"issuer's created time"+'"'
                temp_path_0 = self.basic_parameter[3][0]+"/"+"ManipulationList_"+self.cur_org[0][1]+".csv"
                with open(temp_path_0, "w", encoding = "utf-8") as save_file:
                    save_file.write(temp_str_0)
                    save_file.close()
                if_admin = False
                if_creator = False
                for n in range(len(self.cur_org[1])):
                    temp_str_1 = "\n"
                    temp_str_1 = temp_str_1+str(n+1)
                    temp_str_1 = temp_str_1+","
                    if self.cur_org[1][n][1]:
                        temp_str_1 = temp_str_1+"1"
                    else:
                        temp_str_1 = temp_str_1+"0"
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+"'"+self.cur_org[1][n][0]+"'"
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+"'"+self.cur_org[0][0]+"'"
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+'"'+self.cur_org[0][2]+'"'
                    temp_str_1 = temp_str_1+","
                    if not if_creator:
                        if self.cur_org[1][n][0] == self.cur_org[0][5][0]:
                            temp_str_1 = temp_str_1+"1"
                            temp_str_1 = temp_str_1+","
                            temp_str_1 = temp_str_1+"'"+self.cur_org[0][5][1]+"'"
                            temp_str_1 = temp_str_1+","
                            temp_str_1 = temp_str_1+"'"+self.cur_org[0][5][2]+"'"
                            if_creator = True
                        else:
                            temp_str_1 = temp_str_1+","
                            temp_str_1 = temp_str_1+","
                    else:
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+","
                    if not if_admin:
                        if self.cur_org[1][n][0] == self.cur_org[0][4]:
                            temp_str_1 = temp_str_1+"1"
                            if_admin = True
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+"'"+self.cur_org[1][n][2]+"'"
                    temp_str_1 = temp_str_1+","
                    if self.cur_org[1][n][3] == "en":
                        temp_str_1 = temp_str_1+"English name"
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+'"'+self.cur_org[1][n][4]+'"'
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+'"'+self.cur_org[1][n][5]+'"'
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+'"'+self.cur_org[1][n][6]+'"'
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                    elif self.cur_org[1][n][3] == "vn":
                        temp_str_1 = temp_str_1+"another name / virtual name"
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+'"'+self.cur_org[1][n][4]+'"'
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+'"'+self.cur_org[1][n][5]+'"'
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+'"'+self.cur_org[1][n][6]+'"'
                    else:
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                        temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+"'"+self.cur_org[1][n][7]+"'"
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+"'"+self.cur_org[1][n][8]+"'"
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+"'"+self.cur_org[1][n][9]+"'"
                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                        save_file.write(temp_str_1)
                        save_file.close()
                showinfo(title = "The *.csv file is output", 
                         message = "The *.csv file with path '"+temp_path_0+"' is output.")
    
    def output_csv_fun_org(self):
        if self.output_csv_page_org_org_list_bool: 
            if os.path.exists(self.cur_org_file_name):
                with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                    read_text = read_file.read()
                    self.cur_org = self.reading_str_text_org(read_text)
                if not self.cur_org is None:
                    temp_num_0 = -1
                    for n in range(len(self.cur_org[2])):
                        if self.cur_org[2][n] == self.cur_mani_num:
                            temp_num_0 = n
                            break
                    if temp_num_0 >= 0:
                        temp_bool_0 = self.cur_org[3][temp_num_0]
                    else:
                        temp_bool_0 = False
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
            if not temp_bool_0:
                showerror(title = "Error", 
                          message = "No privilege to do so.") 
            else:
                temp_str_0 = chr(65279)
                temp_str_0 = temp_str_0+'"'+"index"+'"'+","
                temp_str_0 = temp_str_0+'"'+"organization number"+'"'+","
                temp_str_0 = temp_str_0+'"'+"organization name"+'"'+","
                temp_str_0 = temp_str_0+'"'+"created date"+'"'+","
                temp_str_0 = temp_str_0+'"'+"created time"+'"'+","
                temp_str_0 = temp_str_0+'"'+"creator's manipulation number"+'"'
                temp_path_0 = self.basic_parameter[3][0]+"/"+"OrganizationList.csv"
                with open(temp_path_0, "w", encoding = "utf-8") as save_file:
                    save_file.write(temp_str_0)
                    save_file.close()
                for n in range(len(self.basic_org_list[1])):
                    temp_str_1 = "\n"
                    temp_str_1 = temp_str_1+str(n+1)
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+"'"+self.basic_org_list[1][n][0]+"'"
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+'"'+self.basic_org_list[1][n][1]+'"'
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+"'"+self.basic_org_list[1][n][2]+"'"
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+"'"+self.basic_org_list[1][n][3]+"'"
                    temp_str_1 = temp_str_1+","
                    temp_str_1 = temp_str_1+"'"+self.basic_org_list[1][n][4]+"'"
                    with open(temp_path_0, "a", encoding = "utf-8") as save_file:
                        save_file.write(temp_str_1)
                        save_file.close()
                showinfo(title = "The *.csv file is output", 
                         message = "The *.csv file with path '"+temp_path_0+"' is output.")
    
    def setting_page(self):    
        # setting_page_frame
        self.setting_page_frame.grid(row = 1, column = 0,
                                     padx = 5, pady = 5,
                                     sticky = tk.W)
        setting_page_radio_frame = tk.LabelFrame(self.setting_page_frame, 
                                                 text = "Setting: select a function", 
                                                 font = self.fonsize_s)
        setting_page_radio_frame.grid(row = 0, column = 0,
                                      padx = 5, pady = 5,
                                      sticky = tk.W)
        setting_page_radio_line_0 = tk.Frame(setting_page_radio_frame)
        setting_page_radio_line_0.grid(row = 0, column = 0,
                                       sticky = tk.W)
        setting_page_radio_line_1 = tk.Frame(setting_page_radio_frame)
        setting_page_radio_line_1.grid(row = 1, column = 0,
                                       sticky = tk.W)
        self.setting_page_radio_vari = tk.StringVar()
        self.setting_page_mani_num_radio = tk.Radiobutton(setting_page_radio_line_0, 
                                                          variable = self.setting_page_radio_vari, 
                                                          text = "Input a manipulation number", 
                                                          value = "mani_num", 
                                                          font = self.fonsize_s)
        self.setting_page_mani_num_radio.grid(row = 0, column = 0,
                                              padx = 2, pady = 2, 
                                              sticky = tk.W)
        self.setting_page_gene_org_radio = tk.Radiobutton(setting_page_radio_line_0, 
                                                          variable = self.setting_page_radio_vari, 
                                                          text = "Generate a new <organization.dat> file", 
                                                          value = "gene_org", 
                                                          font = self.fonsize_s)
        self.setting_page_gene_org_radio.grid(row = 0, column = 1,
                                              padx = 2, pady = 2, 
                                              sticky = tk.W)
        self.setting_page_direct_radio = tk.Radiobutton(setting_page_radio_line_1, 
                                                        variable = self.setting_page_radio_vari, 
                                                        text = "Set directories", 
                                                        value = "direct", 
                                                        font = self.fonsize_s)
        self.setting_page_direct_radio.grid(row = 0, column = 0,
                                            padx = 2, pady = 2, 
                                            sticky = tk.W)
        self.setting_page_my_org_radio = tk.Radiobutton(setting_page_radio_line_1, 
                                                        variable = self.setting_page_radio_vari, 
                                                        text = "My organization", 
                                                        value = "my_org", 
                                                        font = self.fonsize_s)
        self.setting_page_my_org_radio.grid(row = 0, column = 1,
                                            padx = 2, pady = 2, 
                                            sticky = tk.W)
        self.setting_page_org_list_radio = tk.Radiobutton(setting_page_radio_line_1, 
                                                          variable = self.setting_page_radio_vari, 
                                                          text = "Organization list", 
                                                          value = "org_list", 
                                                          font = self.fonsize_s)
        self.setting_page_org_list_radio.grid(row = 0, column = 2,
                                              padx = 2, pady = 2, 
                                              sticky = tk.W)
        ## command
        self.setting_page_mani_num_radio["command"] = self.setting_fun_select
        self.setting_page_gene_org_radio["command"] = self.setting_fun_select
        self.setting_page_direct_radio["command"] = self.setting_fun_select
        self.setting_page_my_org_radio["command"] = self.setting_fun_select
        self.setting_page_org_list_radio["command"] = self.setting_fun_select
        
        # mani_num
        self.setting_mani_num_frame = tk.Frame(self.setting_page_frame)
        self.setting_mani_num_frame.grid(row = 1, column = 0,
                                         padx = 5, pady = 5, 
                                         sticky = tk.NW)
        setting_org_file_is = ttk.Label(self.setting_mani_num_frame, 
                                        text = "Current organization files: ",                          
                                        font = self.fonsize_m)
        setting_org_file_is.grid(row = 0, column = 0,
                                 sticky = tk.W)
        self.setting_org_file_combo_vari = tk.StringVar()
        self.setting_org_file_combo = ttk.Combobox(self.setting_mani_num_frame, 
                                                   textvariable = self.setting_org_file_combo_vari, 
                                                   values = [], 
                                                   width = 50, 
                                                   state = "readonly",
                                                   font = self.fonsize_s)
        self.setting_org_file_combo.grid(row = 1, column = 0, 
                                         sticky = tk.E)
        setting_mani_num_is = ttk.Label(self.setting_mani_num_frame, 
                                       text = "Selected organization number: ",                          
                                       font = self.fonsize_m)
        setting_mani_num_is.grid(row = 2, column = 0,
                                sticky = tk.W)
        self.setting_org_num = ttk.Label(self.setting_mani_num_frame, 
                                         text = "",    
                                         wraplength = 1000,                       
                                         font = self.fonsize_s)
        self.setting_org_num.grid(row = 3, column = 0,
                                  sticky = tk.E)
        setting_org_name_is = ttk.Label(self.setting_mani_num_frame, 
                                        text = "Selected organization name: ",                          
                                        font = self.fonsize_m)
        setting_org_name_is.grid(row = 4, column = 0,
                                 sticky = tk.W)
        self.setting_org_name = ttk.Label(self.setting_mani_num_frame, 
                                          text = "",   
                                          wraplength = 1000, 
                                          font = self.fonsize_s)
        self.setting_org_name.grid(row = 5, column = 0,
                                   sticky = tk.E)
        setting_mani_num_is = ttk.Label(self.setting_mani_num_frame, 
                                        text = "Input manipulation number: ",                          
                                        font = self.fonsize_m)
        setting_mani_num_is.grid(row = 6, column = 0,
                                 sticky = tk.W)
        setting_mani_num_line = tk.Frame(self.setting_mani_num_frame)
        setting_mani_num_line.grid(row = 7, column = 0,
                                   sticky = tk.E)
        self.setting_mani_num_entry_vari = tk.StringVar()
        self.setting_mani_num_entry = tk.Entry(setting_mani_num_line, 
                                               textvariable = self.setting_mani_num_entry_vari, 
                                               width = 9, 
                                               font = self.fonsize_m)
        self.setting_mani_num_entry.grid(row = 0, column = 0,
                                         sticky = tk.E)
        self.setting_mani_num_confirm_button = tk.Button(setting_mani_num_line, 
                                                         text = "Confirm", 
                                                         width = 9, 
                                                         font = self.fonsize_m, 
                                                         foreground = "green", 
                                                         activeforeground = "green")
        self.setting_mani_num_confirm_button.grid(row = 0, column = 1,
                                                  sticky = tk.W)
        ## command
        self.setting_org_file_combo.bind("<<ComboboxSelected>>", self.setting_fun_org_select)
        self.setting_mani_num_confirm_button["command"] = self.setting_fun_org_confirm
        self.setting_mani_num_entry.bind("<Escape>", self.setting_fun_org_escqpe)
        self.setting_mani_num_entry.bind("<Return>", self.setting_fun_org_return)
        
        # gene_org
        self.setting_gene_org_frame_0 = tk.Frame(self.setting_page_frame)
        self.setting_gene_org_frame_0.grid_forget()
        setting_gene_org_frame_0_line_0 = tk.Frame(self.setting_gene_org_frame_0)
        setting_gene_org_frame_0_line_0.grid(row = 0, column = 0,
                                             sticky = tk.W)
        setting_gene_org_frame_0_line_0_left = tk.Frame(setting_gene_org_frame_0_line_0)
        setting_gene_org_frame_0_line_0_left.grid(row = 0, column = 0,
                                                  sticky = tk.W)
        setting_new_org_name_is = ttk.Label(setting_gene_org_frame_0_line_0_left, 
                                            text = "Input English name of the new organization: ",                          
                                            font = self.fonsize_m)
        setting_new_org_name_is.grid(row = 0, column = 0,
                                     sticky = tk.W)
        self.setting_new_org_name_entry_vari = tk.StringVar()
        self.setting_new_org_name_entry = tk.Entry(setting_gene_org_frame_0_line_0_left, 
                                                   textvariable = self.setting_new_org_name_entry_vari, 
                                                   width = 35, 
                                                   font = self.fonsize_s)
        self.setting_new_org_name_entry.grid(row = 1, column = 0,
                                             sticky = tk.N)
        setting_gene_org_frame_0_line_0_right = tk.Frame(setting_gene_org_frame_0_line_0)
        setting_gene_org_frame_0_line_0_right.grid(row = 0, column = 1,
                                                   sticky = tk.W)
        setting_new_org_init_is = ttk.Label(setting_gene_org_frame_0_line_0_right, 
                                            text = "The initial 3 digits of the numbers: ",                          
                                            font = self.fonsize_m)
        setting_new_org_init_is.grid(row = 0, column = 0,
                                     sticky = tk.W)
        setting_gene_org_frame_0_line_0_right_line_1 = tk.Frame(setting_gene_org_frame_0_line_0_right)
        setting_gene_org_frame_0_line_0_right_line_1.grid(row = 1, column = 0,
                                                          sticky = tk.N)
        self.setting_new_org_init_0_entry_vari = tk.StringVar()
        self.setting_new_org_init_0_entry = tk.Entry(setting_gene_org_frame_0_line_0_right_line_1, 
                                                     textvariable = self.setting_new_org_init_0_entry_vari, 
                                                     width = 3, 
                                                     font = self.fonsize_s)
        self.setting_new_org_init_0_entry.grid(row = 0, column = 0,
                                               padx = 4, 
                                               sticky = tk.N)
        self.setting_new_org_init_1_entry_vari = tk.StringVar()
        self.setting_new_org_init_1_entry = tk.Entry(setting_gene_org_frame_0_line_0_right_line_1, 
                                                     textvariable = self.setting_new_org_init_1_entry_vari, 
                                                     width = 3, 
                                                     font = self.fonsize_s)
        self.setting_new_org_init_1_entry.grid(row = 0, column = 1,
                                               padx = 4, 
                                               sticky = tk.N)
        self.setting_new_org_init_2_entry_vari = tk.StringVar()
        self.setting_new_org_init_2_entry = tk.Entry(setting_gene_org_frame_0_line_0_right_line_1, 
                                                     textvariable = self.setting_new_org_init_2_entry_vari, 
                                                     width = 3, 
                                                     font = self.fonsize_s)
        self.setting_new_org_init_2_entry.grid(row = 0, column = 2,
                                               padx = 4, 
                                               sticky = tk.N)
        setting_page_new_org_note_frame = tk.Frame(self.setting_gene_org_frame_0)
        setting_page_new_org_note_frame.grid(row = 2, column = 0,
                                             sticky = tk.W)
        temp_str_0 = "Notes. "
        ttk.Label(setting_page_new_org_note_frame, 
                  text = temp_str_0,                          
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        temp_str_0 = "    (1) The initial character of the English name must be from 26 English capital letters and number 0-9."
        ttk.Label(setting_page_new_org_note_frame, 
                  text = temp_str_0,    
                  wraplength = 1000,                       
                  font = self.fonsize_s).grid(row = 1, column = 0,
                                              sticky = tk.W)
        temp_str_0 = "    (2) The other characters of the English name are from: "
        temp_str_0 = temp_str_0+"(i) 26 English capital letters, "
        temp_str_0 = temp_str_0+"(ii) 26 English small letters, "
        temp_str_0 = temp_str_0+"(iii) number 0-9, "
        temp_str_0 = temp_str_0+"(iv) space \" \", "
        temp_str_0 = temp_str_0+"(v) hyphen \"-\", "
        temp_str_0 = temp_str_0+"(vi) and \"&\", "
        temp_str_0 = temp_str_0+"(vii) or \"/\", "
        temp_str_0 = temp_str_0+"(iix) single quotation mark \"'\" and \"‘\" and \"’\", "
        temp_str_0 = temp_str_0+"(ix) dot \".\", "
        temp_str_0 = temp_str_0+"(x) colon \":\", "
        temp_str_0 = temp_str_0+"(xi) parenthesis \"(\" and \")\"."
        ttk.Label(setting_page_new_org_note_frame, 
                  text = temp_str_0,     
                  wraplength = 1000,                       
                  font = self.fonsize_s).grid(row = 2, column = 0,
                                              sticky = tk.W)
        temp_str_0 = "    (3) The max length of the English name is "+str(self.org_name_max_len)+"."
        ttk.Label(setting_page_new_org_note_frame, 
                  text = temp_str_0,  
                  wraplength = 1000,                        
                  font = self.fonsize_s).grid(row = 3, column = 0,
                                              sticky = tk.W)
        temp_str_0 = "    (4) The 3 initial digits must be from 26 English letters, regardless capital or small letters."
        ttk.Label(setting_page_new_org_note_frame, 
                  text = temp_str_0,  
                  wraplength = 1000,                        
                  font = self.fonsize_s).grid(row = 4, column = 0,
                                              sticky = tk.W)
        setting_page_new_org_button_frame_0 = tk.Frame(self.setting_gene_org_frame_0)
        setting_page_new_org_button_frame_0.grid(row = 3, column = 0,
                                                 sticky = tk.W)
        
        self.setting_org_num_prev_button_0 = tk.Button(setting_page_new_org_button_frame_0, 
                                                       text = "Previous", 
                                                       state = "disabled", 
                                                       width = 10, 
                                                       font = self.fonsize_m)
        self.setting_org_num_prev_button_0.grid(row = 0, column = 0,
                                                padx = 2, pady = 2,
                                                sticky = tk.W)
        self.setting_org_num_next_button_0 = tk.Button(setting_page_new_org_button_frame_0, 
                                                       text = "Next", 
                                                       width = 10, 
                                                       font = self.fonsize_m)
        self.setting_org_num_next_button_0.grid(row = 0, column = 1,
                                                padx = 2, pady = 2,
                                                sticky = tk.W)
        self.setting_gene_org_frame_1 = tk.Frame(self.setting_page_frame)
        self.setting_gene_org_frame_1.grid_forget()
        setting_gene_org_frame_1_line_0 = tk.Frame(self.setting_gene_org_frame_1)
        setting_gene_org_frame_1_line_0.grid(row = 0, column = 0,
                                             padx = 2, pady = 2,
                                             sticky = tk.W)
        self.setting_gene_org_1_radio_vari = tk.StringVar()
        self.setting_gene_org_1_new_radio = tk.Radiobutton(setting_gene_org_frame_1_line_0, 
                                                           variable = self.setting_gene_org_1_radio_vari, 
                                                           text = "Generate a new member number as administrator", 
                                                           value = "new", 
                                                           font = self.fonsize_s)
        self.setting_gene_org_1_new_radio.grid(row = 0, column = 0,
                                               sticky = tk.W)
        self.setting_gene_org_1_exist_radio = tk.Radiobutton(setting_gene_org_frame_1_line_0, 
                                                             variable = self.setting_gene_org_1_radio_vari, 
                                                             text = "Set an existing member number as administrator", 
                                                             value = "exist", 
                                                             font = self.fonsize_s)
        self.setting_gene_org_1_exist_radio.grid(row = 1, column = 0,
                                                 sticky = tk.W)
        ttk.Separator(setting_gene_org_frame_1_line_0, 
                      orient="horizontal").grid(row = 2, column = 0,
                                                sticky = tk.EW)
        self.setting_gene_org_frame_1_new_frame = tk.Frame(self.setting_gene_org_frame_1)
        self.setting_gene_org_frame_1_new_frame.grid_forget()
        ttk.Label(self.setting_gene_org_frame_1_new_frame, 
                  text = "(1) English name: ",                     
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        setting_gene_org_frame_1_new_frame_line_0 = tk.Frame(self.setting_gene_org_frame_1_new_frame)
        setting_gene_org_frame_1_new_frame_line_0.grid(row = 1, column = 0,
                                                       padx = 2, pady = 2,
                                                       sticky = tk.N)
        ttk.Label(setting_gene_org_frame_1_new_frame_line_0, 
                  text = "Given Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_gene_org_new_gn_entry_vari = tk.StringVar()
        self.setting_gene_org_new_gn_entry = tk.Entry(setting_gene_org_frame_1_new_frame_line_0, 
                                                      textvariable = self.setting_gene_org_new_gn_entry_vari, 
                                                      width = 14, 
                                                      font = self.fonsize_s)
        self.setting_gene_org_new_gn_entry.grid(row = 1, column = 0,
                                                sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_new_frame_line_0, 
                  text = "Middle Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 1,
                                              sticky = tk.W)
        self.setting_gene_org_new_mn_entry_vari = tk.StringVar()
        self.setting_gene_org_new_mn_entry = tk.Entry(setting_gene_org_frame_1_new_frame_line_0, 
                                                      textvariable = self.setting_gene_org_new_mn_entry_vari, 
                                                      width = 14, 
                                                      font = self.fonsize_s)
        self.setting_gene_org_new_mn_entry.grid(row = 1, column = 1,
                                                sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_new_frame_line_0, 
                  text = "Family Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        self.setting_gene_org_new_fn_entry_vari = tk.StringVar()
        self.setting_gene_org_new_fn_entry = tk.Entry(setting_gene_org_frame_1_new_frame_line_0, 
                                                      textvariable = self.setting_gene_org_new_fn_entry_vari, 
                                                      width = 14, 
                                                      font = self.fonsize_s)
        self.setting_gene_org_new_fn_entry.grid(row = 1, column = 2,
                                                sticky = tk.W)
        ttk.Separator(self.setting_gene_org_frame_1_new_frame, 
                      orient="horizontal").grid(row = 2, column = 0, 
                                                sticky = tk.EW)
        ttk.Label(self.setting_gene_org_frame_1_new_frame, 
                  text = "(2) Another name / virtual name: ",                     
                  font = self.fonsize_s).grid(row = 3, column = 0,
                                              sticky = tk.W)
        setting_gene_org_frame_1_new_frame_line_1 = tk.Frame(self.setting_gene_org_frame_1_new_frame)
        setting_gene_org_frame_1_new_frame_line_1.grid(row = 4, column = 0,
                                                       padx = 2, pady = 2,
                                                       sticky = tk.W)
        setting_gene_org_frame_1_new_frame_line_1_line_0 = tk.Frame(setting_gene_org_frame_1_new_frame_line_1)
        setting_gene_org_frame_1_new_frame_line_1_line_0.grid(row = 0, column = 0,
                                                              sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_new_frame_line_1_line_0, 
                  text = "Name type ",        
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_gene_org_new_vt_combo_vari = tk.StringVar()
        self.setting_gene_org_new_vt_combo = ttk.Combobox(setting_gene_org_frame_1_new_frame_line_1_line_0, 
                                                          textvariable = self.setting_gene_org_new_vt_combo_vari, 
                                                          values = self.virtual_type, 
                                                          width = 35, 
                                                          state = "readonly",
                                                          font = self.fonsize_s)
        self.setting_gene_org_new_vt_combo.grid(row = 0, column = 1, 
                                                sticky = tk.W)
        self.setting_gene_org_new_vt_combo.set("Other")
        setting_gene_org_frame_1_new_frame_line_1_line_1 = tk.Frame(setting_gene_org_frame_1_new_frame_line_1)
        setting_gene_org_frame_1_new_frame_line_1_line_1.grid(row = 1, column = 0,
                                                              sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_new_frame_line_1_line_1, 
                  text = "Name ",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_gene_org_new_vn_entry_vari = tk.StringVar()
        self.setting_gene_org_new_vn_entry = tk.Entry(setting_gene_org_frame_1_new_frame_line_1_line_1, 
                                                      textvariable = self.setting_gene_org_new_vn_entry_vari, 
                                                      width = 14, 
                                                      font = self.fonsize_s)
        self.setting_gene_org_new_vn_entry.grid(row = 0, column = 1,
                                                sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_new_frame_line_1_line_1, 
                  text = ", Addition (@ or #) ",
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        self.setting_gene_org_new_va_entry_vari = tk.StringVar()
        self.setting_gene_org_new_va_entry = tk.Entry(setting_gene_org_frame_1_new_frame_line_1_line_1, 
                                                      textvariable = self.setting_gene_org_new_va_entry_vari, 
                                                      width = 14, 
                                                      font = self.fonsize_s)
        self.setting_gene_org_new_va_entry.grid(row = 0, column = 3,
                                                sticky = tk.W)
        ttk.Separator(self.setting_gene_org_frame_1_new_frame, 
                      orient="horizontal").grid(row = 5, column = 0, 
                                                sticky = tk.EW)
        setting_gene_org_frame_1_new_frame_line_2 = tk.Frame(self.setting_gene_org_frame_1_new_frame)
        setting_gene_org_frame_1_new_frame_line_2.grid(row = 6, column = 0,
                                                       padx = 2, pady = 2,
                                                       sticky = tk.N)
        ttk.Label(setting_gene_org_frame_1_new_frame_line_2, 
                  text = "(3) Set ",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        setting_gene_org_frame_1_new_frame_line_2_radio_frame = tk.Frame(setting_gene_org_frame_1_new_frame_line_2)
        setting_gene_org_frame_1_new_frame_line_2_radio_frame.grid(row = 0, column = 1,
                                                                   sticky = tk.W)
        self.setting_gene_org_frame_1_new_admin_radio_vari = tk.StringVar()
        self.setting_gene_org_frame_1_new_admin_en_radio = tk.Radiobutton(setting_gene_org_frame_1_new_frame_line_2_radio_frame, 
                                                                          variable = self.setting_gene_org_frame_1_new_admin_radio_vari, 
                                                                          text = "English name", 
                                                                          value = "en", 
                                                                          font = self.fonsize_s)
        self.setting_gene_org_frame_1_new_admin_en_radio.grid(row = 0, column = 0,
                                                              sticky = tk.W)
        self.setting_gene_org_frame_1_new_admin_vn_radio = tk.Radiobutton(setting_gene_org_frame_1_new_frame_line_2_radio_frame, 
                                                                          variable = self.setting_gene_org_frame_1_new_admin_radio_vari, 
                                                                          text = "another name / virtual name", 
                                                                          value = "vn", 
                                                                          font = self.fonsize_s)
        self.setting_gene_org_frame_1_new_admin_vn_radio.grid(row = 1, column = 0,
                                                              sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_new_frame_line_2, 
                  text = " as the name of administrator.",
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        ttk.Separator(self.setting_gene_org_frame_1_new_frame, 
                      orient="horizontal").grid(row = 7, column = 0,
                                                sticky = tk.EW)
        self.setting_gene_org_frame_1_exist_frame = tk.Frame(self.setting_gene_org_frame_1)
        self.setting_gene_org_frame_1_exist_frame.grid_forget()
        ttk.Label(self.setting_gene_org_frame_1_exist_frame, 
                  text = "(1) Member: ", 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        setting_gene_org_frame_1_exist_frame_line_0 = tk.Frame(self.setting_gene_org_frame_1_exist_frame)
        setting_gene_org_frame_1_exist_frame_line_0.grid(row = 1, column = 0,
                                                         padx = 2, pady = 2,
                                                         sticky = tk.W)
        setting_gene_org_frame_1_exist_frame_line_0_line_0 = tk.Frame(setting_gene_org_frame_1_exist_frame_line_0)
        setting_gene_org_frame_1_exist_frame_line_0_line_0.grid(row = 0, column = 0,
                                                                sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_0_line_0, 
                  text = "    Member number (14 digits): ",                     
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)        
        self.setting_gene_org_exist_mem_num_entry_vari = tk.StringVar()
        self.setting_gene_org_exist_mem_num_entry = tk.Entry(setting_gene_org_frame_1_exist_frame_line_0_line_0, 
                                                             textvariable = self.setting_gene_org_exist_mem_num_entry_vari, 
                                                             width = 16, 
                                                             font = self.fonsize_s)
        self.setting_gene_org_exist_mem_num_entry.grid(row = 0, column = 1,
                                                       sticky = tk.W)
        setting_gene_org_frame_1_exist_frame_line_0_line_1 = tk.Frame(setting_gene_org_frame_1_exist_frame_line_0)
        setting_gene_org_frame_1_exist_frame_line_0_line_1.grid(row = 1, column = 0,
                                                                sticky = tk.W)
        self.setting_gene_org_frame_1_exist_admin_radio_vari = tk.StringVar()
        self.setting_gene_org_frame_1_exist_admin_en_radio = tk.Radiobutton(setting_gene_org_frame_1_exist_frame_line_0_line_1, 
                                                                            variable = self.setting_gene_org_frame_1_exist_admin_radio_vari, 
                                                                            text = "English name", 
                                                                            value = "en", 
                                                                            font = self.fonsize_s)
        self.setting_gene_org_frame_1_exist_admin_en_radio.grid(row = 0, column = 0,
                                                                padx = 5, 
                                                                sticky = tk.W)
        self.setting_gene_org_frame_1_exist_admin_vn_radio = tk.Radiobutton(setting_gene_org_frame_1_exist_frame_line_0_line_1, 
                                                                            variable = self.setting_gene_org_frame_1_exist_admin_radio_vari, 
                                                                            text = "another name / virtual name", 
                                                                            value = "vn", 
                                                                            font = self.fonsize_s)
        self.setting_gene_org_frame_1_exist_admin_vn_radio.grid(row = 0, column = 1,
                                                                padx = 5, 
                                                                sticky = tk.W)
        self.setting_gene_org_frame_1_exist_frame_line_0_en = tk.Frame(setting_gene_org_frame_1_exist_frame_line_0)
        self.setting_gene_org_frame_1_exist_frame_line_0_en.grid(row = 2, column = 0,
                                                                 sticky = tk.W)
        ttk.Label(self.setting_gene_org_frame_1_exist_frame_line_0_en, 
                  text = "Given Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_gene_org_exist_gn_entry_vari = tk.StringVar()
        self.setting_gene_org_exist_gn_entry = tk.Entry(self.setting_gene_org_frame_1_exist_frame_line_0_en, 
                                                        textvariable = self.setting_gene_org_exist_gn_entry_vari, 
                                                        width = 14, 
                                                        font = self.fonsize_s)
        self.setting_gene_org_exist_gn_entry.grid(row = 1, column = 0,
                                                  sticky = tk.W)
        ttk.Label(self.setting_gene_org_frame_1_exist_frame_line_0_en, 
                  text = "Middle Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 1,
                                              sticky = tk.W)
        self.setting_gene_org_exist_mn_entry_vari = tk.StringVar()
        self.setting_gene_org_exist_mn_entry = tk.Entry(self.setting_gene_org_frame_1_exist_frame_line_0_en, 
                                                        textvariable = self.setting_gene_org_exist_mn_entry_vari, 
                                                        width = 14, 
                                                        font = self.fonsize_s)
        self.setting_gene_org_exist_mn_entry.grid(row = 1, column = 1,
                                                  sticky = tk.W)
        ttk.Label(self.setting_gene_org_frame_1_exist_frame_line_0_en, 
                  text = "Family Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        self.setting_gene_org_exist_fn_entry_vari = tk.StringVar()
        self.setting_gene_org_exist_fn_entry = tk.Entry(self.setting_gene_org_frame_1_exist_frame_line_0_en, 
                                                        textvariable = self.setting_gene_org_exist_fn_entry_vari, 
                                                        width = 14, 
                                                        font = self.fonsize_s)
        self.setting_gene_org_exist_fn_entry.grid(row = 1, column = 2,
                                                  sticky = tk.W)
        self.setting_gene_org_frame_1_exist_frame_line_0_vn = tk.Frame(setting_gene_org_frame_1_exist_frame_line_0)
        self.setting_gene_org_frame_1_exist_frame_line_0_vn.grid(row = 2, column = 0,
                                                                 sticky = tk.W)
        setting_gene_org_frame_1_exist_frame_line_0_vn_line_0 = tk.Frame(self.setting_gene_org_frame_1_exist_frame_line_0_vn)
        setting_gene_org_frame_1_exist_frame_line_0_vn_line_0.grid(row = 0, column = 0,
                                                                   sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_0_vn_line_0, 
                  text = "Name type ",        
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_gene_org_exist_vt_combo_vari = tk.StringVar()
        self.setting_gene_org_exist_vt_combo = ttk.Combobox(setting_gene_org_frame_1_exist_frame_line_0_vn_line_0, 
                                                            textvariable = self.setting_gene_org_exist_vt_combo_vari, 
                                                            values = self.virtual_type, 
                                                            width = 35, 
                                                            state = "readonly",
                                                            font = self.fonsize_s)
        self.setting_gene_org_exist_vt_combo.grid(row = 0, column = 1, 
                                                  sticky = tk.W)
        self.setting_gene_org_exist_vt_combo.set("Other")
        setting_gene_org_frame_1_exist_frame_line_0_vn_line_1 = tk.Frame(self.setting_gene_org_frame_1_exist_frame_line_0_vn)
        setting_gene_org_frame_1_exist_frame_line_0_vn_line_1.grid(row = 1, column = 0,
                                                                   sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_0_vn_line_1, 
                  text = "Name ",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_gene_org_exist_vn_entry_vari = tk.StringVar()
        self.setting_gene_org_exist_vn_entry = tk.Entry(setting_gene_org_frame_1_exist_frame_line_0_vn_line_1, 
                                                        textvariable = self.setting_gene_org_exist_vn_entry_vari, 
                                                        width = 14, 
                                                        font = self.fonsize_s)
        self.setting_gene_org_exist_vn_entry.grid(row = 0, column = 1,
                                                  sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_0_vn_line_1, 
                  text = ", Addition (@ or #) ",
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        self.setting_gene_org_exist_va_entry_vari = tk.StringVar()
        self.setting_gene_org_exist_va_entry = tk.Entry(setting_gene_org_frame_1_exist_frame_line_0_vn_line_1, 
                                                        textvariable = self.setting_gene_org_exist_va_entry_vari, 
                                                        width = 14, 
                                                        font = self.fonsize_s)
        self.setting_gene_org_exist_va_entry.grid(row = 0, column = 3,
                                                  sticky = tk.W)
        ttk.Separator(self.setting_gene_org_frame_1_exist_frame, 
                      orient="horizontal").grid(row = 2, column = 0, 
                                                sticky = tk.EW)
        ttk.Label(self.setting_gene_org_frame_1_exist_frame, 
                  text = "(2) Issuer of the member: ",                     
                  font = self.fonsize_s).grid(row = 3, column = 0,
                                              sticky = tk.W)
        setting_gene_org_frame_1_exist_frame_line_0
                                              
        setting_gene_org_frame_1_exist_frame_line_1 = tk.Frame(self.setting_gene_org_frame_1_exist_frame)
        setting_gene_org_frame_1_exist_frame_line_1.grid(row = 4, column = 0,
                                                         sticky = tk.W)
        setting_gene_org_frame_1_exist_frame_line_1_line_0 = tk.Frame(setting_gene_org_frame_1_exist_frame_line_1)
        setting_gene_org_frame_1_exist_frame_line_1_line_0.grid(row = 0, column = 0,
                                                                sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_0, 
                  text = "    Organization number (14 digits): ",                     
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)        
        self.setting_gene_org_exist_org_num_entry_vari = tk.StringVar()
        self.setting_gene_org_exist_org_num_entry = tk.Entry(setting_gene_org_frame_1_exist_frame_line_1_line_0, 
                                                             textvariable = self.setting_gene_org_exist_org_num_entry_vari, 
                                                             width = 16, 
                                                             font = self.fonsize_s)
        self.setting_gene_org_exist_org_num_entry.grid(row = 0, column = 1,
                                                       sticky = tk.W)
        setting_gene_org_frame_1_exist_frame_line_1_line_1 = tk.Frame(setting_gene_org_frame_1_exist_frame_line_1)
        setting_gene_org_frame_1_exist_frame_line_1_line_1.grid(row = 1, column = 0,
                                                                sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_1, 
                  text = "    Organization's created date (UTC): ",                     
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        setting_gene_org_frame_1_exist_frame_line_1_line_1_date = tk.Frame(setting_gene_org_frame_1_exist_frame_line_1_line_1)
        setting_gene_org_frame_1_exist_frame_line_1_line_1_date.grid(row = 0, column = 1,
                                                                     sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_1_date, 
                  text = "Year",
                  width = 6, 
                  font = self.fonsize_s).grid(row = 0, column = 0)
        self.setting_gene_org_exist_org_date_year_spinbox_vari = tk.StringVar()
        self.setting_gene_org_exist_org_date_year_spinbox = tk.Spinbox(setting_gene_org_frame_1_exist_frame_line_1_line_1_date, 
                                                                       textvariable = self.setting_gene_org_exist_org_date_year_spinbox_vari, 
                                                                       width = 5, 
                                                                       from_ = 0, 
                                                                       to = 9999, 
                                                                       font = self.fonsize_s)
        self.setting_gene_org_exist_org_date_year_spinbox.grid(row = 1, column = 0,
                                                               sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_1_date, 
                  text = "-",
                  font = self.fonsize_s).grid(row = 1, column = 1)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_1_date, 
                  text = "Month",
                  width = 6, 
                  font = self.fonsize_s).grid(row = 0, column = 2)
        self.setting_gene_org_exist_org_date_month_spinbox_vari = tk.StringVar()
        self.setting_gene_org_exist_org_date_month_spinbox = tk.Spinbox(setting_gene_org_frame_1_exist_frame_line_1_line_1_date, 
                                                                        textvariable = self.setting_gene_org_exist_org_date_month_spinbox_vari, 
                                                                        width = 3, 
                                                                        from_ = 1, 
                                                                        to = 12, 
                                                                        font = self.fonsize_s)
        self.setting_gene_org_exist_org_date_month_spinbox.grid(row = 1, column = 2,
                                                                sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_1_date, 
                  text = "-",
                  font = self.fonsize_s).grid(row = 1, column = 3)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_1_date, 
                  text = "Day",
                  width = 4, 
                  font = self.fonsize_s).grid(row = 0, column = 4)
        self.setting_gene_org_exist_org_date_day_spinbox_vari = tk.StringVar()
        self.setting_gene_org_exist_org_date_day_spinbox = tk.Spinbox(setting_gene_org_frame_1_exist_frame_line_1_line_1_date, 
                                                                      textvariable = self.setting_gene_org_exist_org_date_day_spinbox_vari, 
                                                                      width = 3, 
                                                                      from_ = 1, 
                                                                      to = 31, 
                                                                      font = self.fonsize_s)
        self.setting_gene_org_exist_org_date_day_spinbox.grid(row = 1, column = 4,
                                                              sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_1, 
                  text = ", time (UTC): ",                     
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        setting_gene_org_frame_1_exist_frame_line_1_line_1_time = tk.Frame(setting_gene_org_frame_1_exist_frame_line_1_line_1)
        setting_gene_org_frame_1_exist_frame_line_1_line_1_time.grid(row = 0, column = 3,
                                                                     sticky = tk.W)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_1_time, 
                  text = "Hour",
                  width = 5, 
                  font = self.fonsize_s).grid(row = 0, column = 0)
        self.setting_gene_org_exist_org_time_hour_spinbox_vari = tk.StringVar()
        self.setting_gene_org_exist_org_time_hour_spinbox = tk.Spinbox(setting_gene_org_frame_1_exist_frame_line_1_line_1_time, 
                                                                       textvariable = self.setting_gene_org_exist_org_time_hour_spinbox_vari, 
                                                                       width = 3, 
                                                                       from_ = 0, 
                                                                       to = 23, 
                                                                       font = self.fonsize_s)
        self.setting_gene_org_exist_org_time_hour_spinbox.grid(row = 1, column = 0,
                                                              sticky = tk.W)    
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_1_time, 
                  text = ":",
                  font = self.fonsize_s).grid(row = 1, column = 1)
        ttk.Label(setting_gene_org_frame_1_exist_frame_line_1_line_1_time, 
                  text = "Minute",
                  width = 7, 
                  font = self.fonsize_s).grid(row = 0, column = 2)
        self.setting_gene_org_exist_org_time_minute_spinbox_vari = tk.StringVar()
        self.setting_gene_org_exist_org_time_minute_spinbox = tk.Spinbox(setting_gene_org_frame_1_exist_frame_line_1_line_1_time, 
                                                                         textvariable = self.setting_gene_org_exist_org_time_minute_spinbox_vari, 
                                                                         width = 3, 
                                                                         from_ = 0, 
                                                                         to = 59, 
                                                                         font = self.fonsize_s)
        self.setting_gene_org_exist_org_time_minute_spinbox.grid(row = 1, column = 2,
                                                              sticky = tk.W)
        setting_page_new_org_button_frame_1 = tk.Frame(self.setting_gene_org_frame_1)
        setting_page_new_org_button_frame_1.grid(row = 2, column = 0,
                                                 sticky = tk.W)
        self.setting_org_num_prev_button_1 = tk.Button(setting_page_new_org_button_frame_1, 
                                                       text = "Previous", 
                                                       width = 10, 
                                                       font = self.fonsize_m)
        self.setting_org_num_prev_button_1.grid(row = 0, column = 0,
                                                padx = 2, pady = 2,
                                                sticky = tk.W)
        self.setting_org_num_gene_button_1 = tk.Button(setting_page_new_org_button_frame_1, 
                                                       text = "Generate", 
                                                       width = 10, 
                                                       font = self.fonsize_m, 
                                                       foreground = "green", 
                                                       activeforeground = "green")
        self.setting_org_num_gene_button_1.grid(row = 0, column = 1,
                                                padx = 2, pady = 2,
                                                sticky = tk.W)
        ## command
        self.setting_org_num_next_button_0["command"] = self.setting_fun_generate_org_next_0
        self.setting_org_num_prev_button_1["command"] = self.setting_fun_generate_org_prev_1
        self.setting_gene_org_1_new_radio["command"] = self.setting_fun_generate_org_new_exist_switch_1
        self.setting_gene_org_1_exist_radio["command"] = self.setting_fun_generate_org_new_exist_switch_1
        self.setting_gene_org_frame_1_exist_admin_en_radio["command"] = self.setting_fun_generate_org_exist_member_switch_1
        self.setting_gene_org_frame_1_exist_admin_vn_radio["command"] = self.setting_fun_generate_org_exist_member_switch_1
        self.setting_org_num_gene_button_1["command"] = self.setting_fun_generate_org_gene_1
        
        # direct
        self.setting_direct_frame = tk.Frame(self.setting_page_frame)
        self.setting_direct_frame.grid_forget()    
        setting_direct_new_member_frame = tk.LabelFrame(self.setting_direct_frame, 
                                                        text = "Output new member numbers", 
                                                        font = self.fonsize_s)
        setting_direct_new_member_frame.grid(row = 0, column = 0,
                                             padx = 2, pady = 2,
                                             sticky = tk.W)
        setting_direct_new_member_line_0 = tk.Frame(setting_direct_new_member_frame)
        setting_direct_new_member_line_0.grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_direct_new_member_button = tk.Button(setting_direct_new_member_line_0, 
                                                          text = "Change", 
                                                          width = 8, 
                                                          font = self.fonsize_s)
        self.setting_direct_new_member_button.grid(row = 0, column = 0,
                                                   padx = 1, pady = 1,
                                                   sticky = tk.W)
        self.setting_direct_new_member_vari = ""
        self.setting_direct_new_member = ttk.Label(setting_direct_new_member_line_0, 
                                                   text = "",                          
                                                   font = self.fonsize_s)
        self.setting_direct_new_member.grid(row = 0, column = 1,
                                            padx = 1, pady = 1,
                                            sticky = tk.W)
        setting_direct_new_member_line_1 = tk.Frame(setting_direct_new_member_frame)
        setting_direct_new_member_line_1.grid(row = 1, column = 0,
                                              sticky = tk.W)
        ttk.Label(setting_direct_new_member_line_1, 
                  text = "Also output *.txt in: ",
                  font = self.fonsize_s).grid(row = 0, column = 0)
        self.setting_direct_new_member_en_check_vari = tk.BooleanVar()
        self.setting_direct_new_member_en_check = tk.Checkbutton(setting_direct_new_member_line_1, 
                                                                 variable = self.setting_direct_new_member_en_check_vari, 
                                                                 text = "English  ", 
                                                                 font = self.fonsize_s, 
                                                                 onvalue = True, 
                                                                 offvalue = False)
        self.setting_direct_new_member_en_check.grid(row = 0, column = 1,
                                                     padx = 1, pady = 1,
                                                     sticky = tk.W)
        self.setting_direct_new_member_zhs_check_vari = tk.BooleanVar()
        self.setting_direct_new_member_zhs_check = tk.Checkbutton(setting_direct_new_member_line_1, 
                                                                 variable = self.setting_direct_new_member_zhs_check_vari, 
                                                                 text = "简体中文  ", 
                                                                 font = self.fonsize_s, 
                                                                 onvalue = True, 
                                                                 offvalue = False)
        self.setting_direct_new_member_zhs_check.grid(row = 0, column = 2,
                                                      padx = 1, pady = 1,
                                                      sticky = tk.W)
        self.setting_direct_new_member_zht_check_vari = tk.BooleanVar()
        self.setting_direct_new_member_zht_check = tk.Checkbutton(setting_direct_new_member_line_1, 
                                                                 variable = self.setting_direct_new_member_zht_check_vari, 
                                                                 text = "正體中文  ", 
                                                                 font = self.fonsize_s, 
                                                                 onvalue = True, 
                                                                 offvalue = False)
        self.setting_direct_new_member_zht_check.grid(row = 0, column = 3,
                                                      padx = 1, pady = 1,
                                                      sticky = tk.W)
        setting_direct_output_conf_frame = tk.LabelFrame(self.setting_direct_frame, 
                                                         text = "Output configuration", 
                                                         font = self.fonsize_s)
        setting_direct_output_conf_frame.grid(row = 1, column = 0,
                                              padx = 2, pady = 2,
                                              sticky = tk.W)
        self.setting_direct_output_conf_button = tk.Button(setting_direct_output_conf_frame, 
                                                           text = "Change", 
                                                           width = 8, 
                                                           font = self.fonsize_s)
        self.setting_direct_output_conf_button.grid(row = 0, column = 0,
                                                    padx = 1, pady = 1,
                                                    sticky = tk.W)
        self.setting_direct_output_conf_vari = ""
        self.setting_direct_output_conf = ttk.Label(setting_direct_output_conf_frame, 
                                                    text = "",                          
                                                    font = self.fonsize_s)
        self.setting_direct_output_conf.grid(row = 0, column = 1,
                                             padx = 1, pady = 1,
                                             sticky = tk.W)
        setting_direct_output_csv_frame = tk.LabelFrame(self.setting_direct_frame, 
                                                        text = "Output *.csv", 
                                                        font = self.fonsize_s)
        setting_direct_output_csv_frame.grid(row = 2, column = 0,
                                             padx = 2, pady = 2,
                                             sticky = tk.W)
        self.setting_direct_output_csv_button = tk.Button(setting_direct_output_csv_frame, 
                                                          text = "Change", 
                                                          width = 8, 
                                                          font = self.fonsize_s)
        self.setting_direct_output_csv_button.grid(row = 0, column = 0,
                                                  padx = 1, pady = 1,
                                                  sticky = tk.W)    
        self.setting_direct_output_csv_vari = ""
        self.setting_direct_output_csv = ttk.Label(setting_direct_output_csv_frame, 
                                                   text = "",                          
                                                   font = self.fonsize_s)
        self.setting_direct_output_csv.grid(row = 0, column = 1,
                                            padx = 1, pady = 1,
                                            sticky = tk.W)
        setting_direct_database_frame = tk.LabelFrame(self.setting_direct_frame, 
                                                      text = "Database", 
                                                      font = self.fonsize_s)
        setting_direct_database_frame.grid(row = 3, column = 0,
                                           padx = 2, pady = 2,
                                           sticky = tk.W)
        self.setting_direct_database_button = tk.Button(setting_direct_database_frame, 
                                                        text = "Change", 
                                                        width = 8, 
                                                        font = self.fonsize_s)
        self.setting_direct_database_button.grid(row = 0, column = 0,
                                                 padx = 1, pady = 1,
                                                 sticky = tk.W)   
        self.setting_direct_database_vari = ""
        self.setting_direct_database = ttk.Label(setting_direct_database_frame, 
                                                 text = "",                          
                                                 font = self.fonsize_s)
        self.setting_direct_database.grid(row = 0, column = 1,
                                          padx = 1, pady = 1,
                                          sticky = tk.W)
        self.setting_direct_confirm_button = tk.Button(self.setting_direct_frame, 
                                                       text = "Confirm", 
                                                       width = 9, 
                                                       font = self.fonsize_s, 
                                                       foreground = "green", 
                                                       activeforeground = "green")
        self.setting_direct_confirm_button.grid(row = 4, column = 0,
                                                padx = 1, pady = 1,
                                                sticky = tk.W)  
        ## command
        self.setting_direct_new_member_button["command"] = lambda in_str = "new_member": self.setting_fun_change_direct(in_str)
        self.setting_direct_output_conf_button["command"] = lambda in_str = "output_conf": self.setting_fun_change_direct(in_str)
        self.setting_direct_output_csv_button["command"] = lambda in_str = "output_csv": self.setting_fun_change_direct(in_str)
        self.setting_direct_database_button["command"] = lambda in_str = "database": self.setting_fun_change_direct(in_str)
        self.setting_direct_confirm_button["command"] = self.setting_fun_confirm_direct
        
        # my_org
        self.setting_my_org_frame = tk.Frame(self.setting_page_frame)
        self.setting_my_org_frame.grid_forget()          
        setting_my_org_frame_line_0 = tk.Frame(self.setting_my_org_frame)
        setting_my_org_frame_line_0.grid(row = 0, column = 0,
                                         padx = 2, pady = 2,
                                         sticky = tk.W)         
        self.setting_my_org_output_button = tk.Button(setting_my_org_frame_line_0, 
                                                      text = "Output organization.dat", 
                                                      width = 25, 
                                                      font = self.fonsize_m)
        self.setting_my_org_output_button.grid(row = 0, column = 0,
                                               padx = 2, pady = 2,
                                               sticky = tk.W)
        self.setting_my_org_page_radio_vari = tk.StringVar()
        self.setting_my_org_basic_info_radio = tk.Radiobutton(setting_my_org_frame_line_0, 
                                                              variable = self.setting_my_org_page_radio_vari, 
                                                              text = "Basic info", 
                                                              value = "info", 
                                                              font = self.fonsize_s)
        self.setting_my_org_basic_info_radio.grid(row = 0, column = 1,
                                                  padx = 2, pady = 2,
                                                  sticky = tk.W)
        self.setting_my_org_mani_list_radio = tk.Radiobutton(setting_my_org_frame_line_0, 
                                                             variable = self.setting_my_org_page_radio_vari, 
                                                             text = "Manipulation list", 
                                                             value = "mani", 
                                                             font = self.fonsize_s)
        self.setting_my_org_mani_list_radio.grid(row = 0, column = 2,
                                                 padx = 2, pady = 2,
                                                 sticky = tk.W)
        ttk.Separator(setting_my_org_frame_line_0, 
                      orient="horizontal").grid(row = 1, column = 0,
                                                columnspan = 3,
                                                sticky = tk.EW)
        self.setting_my_org_basic_info_frame = tk.Frame(self.setting_my_org_frame)
        self.setting_my_org_basic_info_frame.grid(row = 1, column = 0,
                                                  padx = 2, pady = 2,
                                                  sticky = tk.W) 
        setting_my_org_basic_info_frame_line_0 = tk.Frame(self.setting_my_org_basic_info_frame)
        setting_my_org_basic_info_frame_line_0.grid(row = 0, column = 0,
                                                    padx = 2, pady = 2,
                                                    sticky = tk.W) 
        ttk.Label(setting_my_org_basic_info_frame_line_0, 
                  text = "Organization number",
                  font = self.fonsize_s).grid(row = 0, column = 0, 
                                              pady = 2, 
                                              sticky = tk.N)
        setting_my_org_basic_info_frame_line_0_org_num_frame = tk.Frame(setting_my_org_basic_info_frame_line_0)
        setting_my_org_basic_info_frame_line_0_org_num_frame.grid(row = 1, column = 0,
                                                       padx = 2, pady = 2, 
                                                       sticky = tk.N) 
        self.setting_my_org_org_num_vari = ""
        self.setting_my_org_org_num = ttk.Label(setting_my_org_basic_info_frame_line_0_org_num_frame, 
                                                text = self.setting_my_org_org_num_vari,
                                                width = 16, 
                                                font = self.fonsize_s)
        self.setting_my_org_org_num.grid(row = 0, column = 0, 
                                         sticky = tk.W) 
        self.setting_my_org_org_num_copy_button = tk.Button(setting_my_org_basic_info_frame_line_0_org_num_frame, 
                                                            text = "Copy", 
                                                            width = 8, 
                                                            font = self.fonsize_s)
        self.setting_my_org_org_num_copy_button.grid(row = 0, column = 1,
                                                     sticky = tk.W) 
        ttk.Separator(setting_my_org_basic_info_frame_line_0, 
                      orient="vertical").grid(row = 0, column = 1,
                                              rowspan = 2, 
                                              sticky = tk.NS)
        ttk.Label(setting_my_org_basic_info_frame_line_0, 
                  text = "Initial 3 digits",
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              padx = 2, pady = 2)
        setting_my_org_basic_info_frame_line_0_initial_frame = tk.Frame(setting_my_org_basic_info_frame_line_0)
        setting_my_org_basic_info_frame_line_0_initial_frame.grid(row = 1, column = 2, 
                                                       padx = 2, pady = 2) 
        self.setting_my_org_org_num_initial_0 = ttk.Label(setting_my_org_basic_info_frame_line_0_initial_frame, 
                                                          text = "",
                                                          font = self.fonsize_s)
        self.setting_my_org_org_num_initial_0.grid(row = 0, column = 0, 
                                                   padx = 4)  
        self.setting_my_org_org_num_initial_1 = ttk.Label(setting_my_org_basic_info_frame_line_0_initial_frame, 
                                                          text = "",
                                                          font = self.fonsize_s)
        self.setting_my_org_org_num_initial_1.grid(row = 0, column = 1, 
                                                   padx = 4)  
        self.setting_my_org_org_num_initial_2 = ttk.Label(setting_my_org_basic_info_frame_line_0_initial_frame, 
                                                          text = "",
                                                          font = self.fonsize_s)
        self.setting_my_org_org_num_initial_2.grid(row = 0, column = 2, 
                                                   padx = 4) 
        ttk.Separator(setting_my_org_basic_info_frame_line_0, 
                      orient="vertical").grid(row = 0, column = 3,
                                              rowspan = 2, 
                                              sticky = tk.NS)
        ttk.Label(setting_my_org_basic_info_frame_line_0, 
                  text = "Manipulation number of Administrator",
                  font = self.fonsize_s).grid(row = 0, column = 4,
                                              padx = 2, pady = 2)
        setting_my_org_basic_info_frame_line_0_admin_frame = tk.Frame(setting_my_org_basic_info_frame_line_0)
        setting_my_org_basic_info_frame_line_0_admin_frame.grid(row = 1, column = 4,
                                                     padx = 2, pady = 2, 
                                                     sticky = tk.N) 
        self.setting_my_org_admin_num_vari = ""
        self.setting_my_org_admin_num = ttk.Label(setting_my_org_basic_info_frame_line_0_admin_frame, 
                                                  text = self.setting_my_org_admin_num_vari,
                                                  width = 9, 
                                                  font = self.fonsize_s)
        self.setting_my_org_admin_num.grid(row = 0, column = 0,
                                           sticky = tk.W) 
        self.setting_my_org_admin_num_copy_button = tk.Button(setting_my_org_basic_info_frame_line_0_admin_frame, 
                                                              text = "Copy", 
                                                              width = 8, 
                                                              font = self.fonsize_s)
        self.setting_my_org_admin_num_copy_button.grid(row = 0, column = 1,
                                                       sticky = tk.W) 
        self.setting_my_org_admin_num_change_button = tk.Button(setting_my_org_basic_info_frame_line_0_admin_frame, 
                                                                text = "Change Admin.", 
                                                                width = 15, 
                                                                font = self.fonsize_s, 
                                                                foreground = "blue", 
                                                                activeforeground = "blue")
        self.setting_my_org_admin_num_change_button.grid(row = 0, column = 2,
                                                         sticky = tk.W) 
        ttk.Separator(self.setting_my_org_basic_info_frame, 
                      orient="horizontal").grid(row = 1, column = 0,
                                                sticky = tk.EW)
        setting_my_org_basic_info_frame_line_1 = tk.Frame(self.setting_my_org_basic_info_frame)
        setting_my_org_basic_info_frame_line_1.grid(row = 2, column = 0,
                                                    padx = 2, pady = 2,
                                                    sticky = tk.W) 
        ttk.Label(setting_my_org_basic_info_frame_line_1, 
                  text = "(1) Organization name: ",
                  font = self.fonsize_m).grid(row = 0, column = 0,
                                              padx = 2, pady = 2)
        self.setting_my_org_org_name_vari = ""
        self.setting_my_org_org_name = ttk.Label(setting_my_org_basic_info_frame_line_1, 
                                                 text = self.setting_my_org_org_name_vari,
                                                 width = 35, 
                                                 font = self.fonsize_s)
        self.setting_my_org_org_name.grid(row = 0, column = 1,
                                          sticky = tk.W)
        self.setting_my_org_org_name_entry_vari = tk.StringVar()
        self.setting_my_org_org_name_entry = tk.Entry(setting_my_org_basic_info_frame_line_1, 
                                                      textvariable = self.setting_my_org_org_name_entry_vari, 
                                                      width = 35, 
                                                      font = self.fonsize_s)
        self.setting_my_org_org_name_entry.grid_forget()
        self.setting_my_org_org_name_edit_button = tk.Button(setting_my_org_basic_info_frame_line_1, 
                                                             text = "Edit", 
                                                             width = 8, 
                                                             font = self.fonsize_s, 
                                                             foreground = "blue", 
                                                             activeforeground = "blue")
        self.setting_my_org_org_name_edit_button.grid(row = 0, column = 2,
                                                      sticky = tk.W) 
        self.setting_my_org_org_name_copy_button = tk.Button(setting_my_org_basic_info_frame_line_1, 
                                                             text = "Copy", 
                                                             width = 8, 
                                                             font = self.fonsize_s)
        self.setting_my_org_org_name_copy_button.grid(row = 0, column = 3,
                                                      sticky = tk.W) 
        self.setting_my_org_org_name_cancel_button = tk.Button(setting_my_org_basic_info_frame_line_1, 
                                                               text = "Cancel", 
                                                               width = 8, 
                                                               font = self.fonsize_s, 
                                                               foreground = "red", 
                                                               activeforeground = "red")
        self.setting_my_org_org_name_cancel_button.grid_forget()
        self.setting_my_org_org_name_confirm_button = tk.Button(setting_my_org_basic_info_frame_line_1, 
                                                                text = "Confirm", 
                                                                width = 8, 
                                                                font = self.fonsize_s, 
                                                                foreground = "green", 
                                                                activeforeground = "green")
        self.setting_my_org_org_name_confirm_button.grid_forget()
        ttk.Separator(self.setting_my_org_basic_info_frame, 
                      orient="horizontal").grid(row = 3, column = 0,
                                                sticky = tk.EW)
        setting_my_org_frame_line_2 = tk.Frame(self.setting_my_org_basic_info_frame)
        setting_my_org_frame_line_2.grid(row = 4, column = 0,
                                         padx = 2, pady = 2,
                                         sticky = tk.W) 
        ttk.Label(setting_my_org_frame_line_2, 
                  text = "(2) City: ",
                  font = self.fonsize_m).grid(row = 0, column = 0,
                                              padx = 2, pady = 2)
        self.setting_my_org_city_vari = ""
        self.setting_my_org_city = ttk.Label(setting_my_org_frame_line_2, 
                                             text = self.setting_my_org_city_vari,
                                             width = 35, 
                                             font = self.fonsize_s)
        self.setting_my_org_city.grid(row = 0, column = 1,
                                      sticky = tk.W)
        self.setting_my_org_city_entry_vari = tk.StringVar()
        self.setting_my_org_city_entry = tk.Entry(setting_my_org_frame_line_2, 
                                                  textvariable = self.setting_my_org_city_entry_vari, 
                                                  width = 35, 
                                                  font = self.fonsize_s)
        self.setting_my_org_city_entry.grid_forget()
        self.setting_my_org_city.grid(row = 0, column = 1,
                                          sticky = tk.W) 
        self.setting_my_org_city_edit_button = tk.Button(setting_my_org_frame_line_2, 
                                                         text = "Edit", 
                                                         width = 8, 
                                                         font = self.fonsize_s, 
                                                         foreground = "blue", 
                                                         activeforeground = "blue")
        self.setting_my_org_city_edit_button.grid(row = 0, column = 2,
                                                  sticky = tk.W) 
        self.setting_my_org_city_copy_button = tk.Button(setting_my_org_frame_line_2, 
                                                         text = "Copy", 
                                                         width = 8, 
                                                         font = self.fonsize_s)
        self.setting_my_org_city_copy_button.grid(row = 0, column = 3,
                                                  sticky = tk.W) 
        self.setting_my_org_city_cancel_button = tk.Button(setting_my_org_frame_line_2, 
                                                           text = "Cancel", 
                                                           width = 8, 
                                                           font = self.fonsize_s, 
                                                           foreground = "red", 
                                                           activeforeground = "red")
        self.setting_my_org_city_cancel_button.grid_forget()
        self.setting_my_org_city_confirm_button = tk.Button(setting_my_org_frame_line_2, 
                                                            text = "Confirm", 
                                                            width = 8, 
                                                            font = self.fonsize_s, 
                                                            foreground = "green", 
                                                            activeforeground = "green")
        self.setting_my_org_city_confirm_button.grid_forget()        
        setting_my_org_frame_line_3 = tk.Frame(self.setting_my_org_basic_info_frame)
        setting_my_org_frame_line_3.grid(row = 5, column = 0,
                                         padx = 2, pady = 2,
                                         sticky = tk.W) 
        ttk.Label(setting_my_org_frame_line_3, 
                  text = "(3) Region: ",
                  font = self.fonsize_m).grid(row = 0, column = 0,
                                              padx = 2, pady = 2)
        self.setting_my_org_region_vari = ""
        self.setting_my_org_region_combo_vari = tk.StringVar()
        self.setting_my_org_region_combo = ttk.Combobox(setting_my_org_frame_line_3, 
                                                        textvariable = self.setting_my_org_region_combo_vari, 
                                                        values = self.regions_vec, 
                                                        width = 33, 
                                                        state = "readonly",
                                                        font = self.fonsize_s)
        self.setting_my_org_region_combo.grid(row = 0, column = 1, 
                                              padx = 2, pady = 2, 
                                              sticky = tk.N)
        self.setting_my_org_region_combo.current(0)
        self.setting_my_org_region_edit_button = tk.Button(setting_my_org_frame_line_3, 
                                                           text = "Edit", 
                                                           width = 8, 
                                                           font = self.fonsize_s, 
                                                           foreground = "blue", 
                                                           activeforeground = "blue")
        self.setting_my_org_region_edit_button.grid(row = 0, column = 2,
                                                    sticky = tk.W) 
        self.setting_my_org_region_cancel_button = tk.Button(setting_my_org_frame_line_3, 
                                                             text = "Cancel", 
                                                             width = 8, 
                                                             font = self.fonsize_s, 
                                                             foreground = "red", 
                                                             activeforeground = "red")
        self.setting_my_org_region_cancel_button.grid_forget()
        self.setting_my_org_region_confirm_button = tk.Button(setting_my_org_frame_line_3, 
                                                              text = "Confirm", 
                                                              width = 8, 
                                                              font = self.fonsize_s, 
                                                              foreground = "green", 
                                                              activeforeground = "green")
        self.setting_my_org_region_confirm_button.grid_forget()  
        ttk.Separator(self.setting_my_org_basic_info_frame, 
                      orient="horizontal").grid(row = 6, column = 0,
                                                sticky = tk.EW)
        setting_my_org_frame_line_4 = tk.Frame(self.setting_my_org_basic_info_frame)
        setting_my_org_frame_line_4.grid(row = 7, column = 0,
                                         padx = 2, pady = 2,
                                         sticky = tk.W) 
        ttk.Label(setting_my_org_frame_line_4, 
                  text = "Created by ",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              padx = 2, pady = 2)
        self.setting_my_org_generate_mani_num = ttk.Label(setting_my_org_frame_line_4, 
                                                          text = "",
                                                          font = self.fonsize_s)
        self.setting_my_org_generate_mani_num.grid(row = 0, column = 1, 
                                                   padx = 2) 
        ttk.Label(setting_my_org_frame_line_4, 
                  text = ", on (UTC) ",
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              padx = 2, pady = 2)
        self.setting_my_org_generate_date = ttk.Label(setting_my_org_frame_line_4, 
                                                      text = "",
                                                      font = self.fonsize_s)
        self.setting_my_org_generate_date.grid(row = 0, column = 3, 
                                               padx = 2) 
        ttk.Label(setting_my_org_frame_line_4, 
                  text = ", at (UTC) ",
                  font = self.fonsize_s).grid(row = 0, column = 4,
                                              padx = 2, pady = 2)
        self.setting_my_org_generate_time = ttk.Label(setting_my_org_frame_line_4, 
                                                      text = "",
                                                      font = self.fonsize_s)
        self.setting_my_org_generate_time.grid(row = 0, column = 5, 
                                               padx = 2) 
        setting_my_org_frame_line_5 = tk.Frame(self.setting_my_org_basic_info_frame)
        setting_my_org_frame_line_5.grid(row = 8, column = 0,
                                         padx = 2, pady = 2,
                                         sticky = tk.W) 
        ttk.Label(setting_my_org_frame_line_5, 
                  text = "Last-edited by ",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              padx = 2, pady = 2)
        self.setting_my_org_lastedit_mani_num = ttk.Label(setting_my_org_frame_line_5, 
                                                          text = "",
                                                          font = self.fonsize_s)
        self.setting_my_org_lastedit_mani_num.grid(row = 0, column = 1, 
                                                   padx = 2) 
        ttk.Label(setting_my_org_frame_line_5, 
                  text = ", on (UTC) ",
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              padx = 2, pady = 2)
        self.setting_my_org_lastedit_date = ttk.Label(setting_my_org_frame_line_5, 
                                                      text = "",
                                                      font = self.fonsize_s)
        self.setting_my_org_lastedit_date.grid(row = 0, column = 3, 
                                               padx = 2) 
        ttk.Label(setting_my_org_frame_line_5, 
                  text = ", at (UTC) ",
                  font = self.fonsize_s).grid(row = 0, column = 4,
                                              padx = 2, pady = 2)
        self.setting_my_org_lastedit_time = ttk.Label(setting_my_org_frame_line_5, 
                                                      text = "",
                                                      font = self.fonsize_s)
        self.setting_my_org_lastedit_time.grid(row = 0, column = 5, 
                                               padx = 2) 
        ttk.Separator(self.setting_my_org_basic_info_frame, 
                      orient="horizontal").grid(row = 9, column = 0,
                                                sticky = tk.EW)
        self.setting_my_org_mani_list_frame = tk.Frame(self.setting_my_org_frame)
        self.setting_my_org_mani_list_frame.grid_forget()
        setting_my_org_mani_list_frame_line_0 = tk.Frame(self.setting_my_org_mani_list_frame)
        setting_my_org_mani_list_frame_line_0.grid(row = 0, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        setting_my_org_mani_list_frame_line_0_left = tk.Frame(setting_my_org_mani_list_frame_line_0)
        setting_my_org_mani_list_frame_line_0_left.grid(row = 0, column = 0,
                                                        sticky = tk.W)        
        self.setting_my_org_mani_listbox_select = ttk.Label(setting_my_org_mani_list_frame_line_0_left, 
                                                            text = "Currently select: -", 
                                                            width = 28, 
                                                            font = self.fonsize_s)
        self.setting_my_org_mani_listbox_select.grid(row = 0, column = 0)
        setting_my_org_mani_list_frame_line_0_left_listbox_frame = tk.Frame(setting_my_org_mani_list_frame_line_0_left)
        setting_my_org_mani_list_frame_line_0_left_listbox_frame.grid(row = 1, column = 0)
        self.setting_my_org_mani_list_listbox_vari = tk.StringVar(value = [])
        self.setting_my_org_mani_list_listbox = tk.Listbox(setting_my_org_mani_list_frame_line_0_left_listbox_frame, 
                                                           listvariable = self.setting_my_org_mani_list_listbox_vari, 
                                                           width = 24, height = 5, 
                                                           font = self.fonsize_s, 
                                                           selectmode = "single")
        self.setting_my_org_mani_list_listbox.grid(row = 0, column = 0, 
                                                   sticky = tk.W)
        setting_my_org_mani_list_listbox_x_scrollbar = ttk.Scrollbar(setting_my_org_mani_list_frame_line_0_left_listbox_frame, 
                                                                     orient = "horizontal", 
                                                                     command = self.setting_my_org_mani_list_listbox.xview)
        self.setting_my_org_mani_list_listbox["xscrollcommand"] = setting_my_org_mani_list_listbox_x_scrollbar.set
        setting_my_org_mani_list_listbox_x_scrollbar.grid(row = 1, column = 0, 
                                                          sticky = tk.EW)
        setting_my_org_mani_list_listbox_y_scrollbar = ttk.Scrollbar(setting_my_org_mani_list_frame_line_0_left_listbox_frame, 
                                                                     orient = "vertical", 
                                                                     command = self.setting_my_org_mani_list_listbox.yview)
        self.setting_my_org_mani_list_listbox["yscrollcommand"] = setting_my_org_mani_list_listbox_y_scrollbar.set
        setting_my_org_mani_list_listbox_y_scrollbar.grid(row = 0, column = 1, 
                                                          sticky = tk.NS)
        setting_my_org_mani_list_frame_line_0_left_button_frame = tk.Frame(setting_my_org_mani_list_frame_line_0_left)
        setting_my_org_mani_list_frame_line_0_left_button_frame.grid(row = 2, column = 0)
        self.setting_my_org_mani_list_add_button = tk.Button(setting_my_org_mani_list_frame_line_0_left_button_frame, 
                                                             text = "✚", 
                                                             width = 3, 
                                                             font = self.fonsize_s, 
                                                             foreground = "green", 
                                                             activeforeground = "green")
        self.setting_my_org_mani_list_add_button.grid(row = 0, column = 0,
                                                      sticky = tk.W)        
        self.setting_my_org_mani_list_up_button = tk.Button(setting_my_org_mani_list_frame_line_0_left_button_frame, 
                                                            text = "▲", 
                                                            width = 3, 
                                                            font = self.fonsize_s, 
                                                            foreground = "blue", 
                                                            activeforeground = "blue")
        self.setting_my_org_mani_list_up_button.grid(row = 0, column = 1,
                                                     sticky = tk.W)
        self.setting_my_org_mani_list_down_button = tk.Button(setting_my_org_mani_list_frame_line_0_left_button_frame, 
                                                              text = "▼", 
                                                              width = 3, 
                                                              font = self.fonsize_s, 
                                                              foreground = "blue", 
                                                              activeforeground = "blue")
        self.setting_my_org_mani_list_down_button.grid(row = 0, column = 2,
                                                       sticky = tk.W)
        self.setting_my_org_mani_list_remove_button = tk.Button(setting_my_org_mani_list_frame_line_0_left_button_frame, 
                                                                text = "✖",  
                                                                width = 3, 
                                                                font = self.fonsize_s, 
                                                                foreground = "red", 
                                                                activeforeground = "red")
        self.setting_my_org_mani_list_remove_button.grid(row = 0, column = 3,
                                                         sticky = tk.W)        
        self.setting_my_org_mani_list_frame_line_0_Right = tk.Frame(setting_my_org_mani_list_frame_line_0)
        self.setting_my_org_mani_list_frame_line_0_Right.grid(row = 0, column = 1,
                                                              sticky = tk.W)
        setting_my_org_mani_list_frame_line_0_Right_line_0 = tk.Frame(self.setting_my_org_mani_list_frame_line_0_Right)
        setting_my_org_mani_list_frame_line_0_Right_line_0.grid(row = 0, column = 0,
                                                                padx = 2, pady = 2,
                                                                sticky = tk.W)
        ttk.Label(setting_my_org_mani_list_frame_line_0_Right_line_0, 
                  text = "(1) Manipulation Number (7 digits): ", 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_my_org_mani_new_frame = tk.Frame(setting_my_org_mani_list_frame_line_0_Right_line_0)
        self.setting_my_org_mani_new_frame.grid(row = 1, column = 0,
                                                sticky = tk.W)
        self.setting_my_org_mani_new_entry_vari = tk.StringVar()
        self.setting_my_org_mani_new_entry = tk.Entry(self.setting_my_org_mani_new_frame, 
                                                      textvariable = self.setting_my_org_mani_new_entry_vari, 
                                                      width = 9, 
                                                      font = self.fonsize_s)
        self.setting_my_org_mani_new_entry.grid(row = 0, column = 0,
                                                sticky = tk.W)
        self.setting_my_org_mani_new_confirm_button = tk.Button(self.setting_my_org_mani_new_frame,
                                                                text = "Confirm", 
                                                                width = 8, 
                                                                font = self.fonsize_s)
        self.setting_my_org_mani_new_confirm_button.grid(row = 0, column = 1,
                                                         sticky = tk.W)
        self.setting_my_org_mani_new_gene_button = tk.Button(self.setting_my_org_mani_new_frame,
                                                             text = "Randomly generate", 
                                                             width = 28, 
                                                             font = self.fonsize_s, 
                                                             foreground = "green", 
                                                             activeforeground = "green")
        self.setting_my_org_mani_new_gene_button.grid(row = 0, column = 2,
                                                      padx = 2, 
                                                      sticky = tk.W) 
        self.setting_my_org_mani_old_frame = tk.Frame(setting_my_org_mani_list_frame_line_0_Right_line_0)
        self.setting_my_org_mani_old_frame.grid(row = 1, column = 0,
                                                sticky = tk.W)
        self.setting_my_org_mani_old_num_vari = ""
        self.setting_my_org_mani_old_num = ttk.Label(self.setting_my_org_mani_old_frame, 
                                                     text = self.setting_my_org_mani_old_num_vari, 
                                                     width = 9, 
                                                     font = self.fonsize_s)
        self.setting_my_org_mani_old_num.grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_my_org_mani_old_copy_button = tk.Button(self.setting_my_org_mani_old_frame,
                                                             text = "Copy", 
                                                             width = 8, 
                                                             font = self.fonsize_s)
        self.setting_my_org_mani_old_copy_button.grid(row = 0, column = 1,
                                                      sticky = tk.W)
        self.setting_my_org_mani_old_check_vari = tk.BooleanVar()
        self.setting_my_org_mani_old_check = tk.Checkbutton(self.setting_my_org_mani_old_frame, 
                                                            variable = self.setting_my_org_mani_old_check_vari, 
                                                            text = "This number is enabled.", 
                                                            width = 28, 
                                                            font = self.fonsize_s, 
                                                            onvalue = True, 
                                                            offvalue = False)
        self.setting_my_org_mani_old_check.grid(row = 0, column = 2,
                                                padx = 2, 
                                                sticky = tk.W)
        self.setting_my_org_mani_confirm_all_button = tk.Button(self.setting_my_org_mani_old_frame,
                                                                text = "Confirm", 
                                                                width = 8, 
                                                                font = self.fonsize_m, 
                                                                foreground = "green", 
                                                                activeforeground = "green")
        self.setting_my_org_mani_confirm_all_button.grid(row = 0, column = 3,
                                                         sticky = tk.W)
        ttk.Separator(self.setting_my_org_mani_list_frame_line_0_Right, 
                      orient="horizontal").grid(row = 1, column = 0,
                                                sticky = tk.EW)
        self.setting_my_org_mani_name_frame = tk.Frame(self.setting_my_org_mani_list_frame_line_0_Right)
        self.setting_my_org_mani_name_frame.grid(row = 2, column = 0,
                                                 padx = 2, pady = 2,
                                                 sticky = tk.W)
        setting_my_org_mani_name_frame_line_0 = tk.Frame(self.setting_my_org_mani_name_frame)
        setting_my_org_mani_name_frame_line_0.grid(row = 0, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(setting_my_org_mani_name_frame_line_0, 
                  text = "(2) Member: ", 
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_my_org_mani_name_radio_vari = tk.StringVar()
        self.setting_my_org_mani_name_en_radio = tk.Radiobutton(setting_my_org_mani_name_frame_line_0, 
                                                                variable = self.setting_my_org_mani_name_radio_vari, 
                                                                text = "English name", 
                                                                value = "en", 
                                                                font = self.fonsize_s)
        self.setting_my_org_mani_name_en_radio.grid(row = 0, column = 1,
                                                    padx = 5, 
                                                    sticky = tk.W)
        self.setting_my_org_mani_name_vn_radio = tk.Radiobutton(setting_my_org_mani_name_frame_line_0, 
                                                                variable = self.setting_my_org_mani_name_radio_vari, 
                                                                text = "another name / virtual name", 
                                                                value = "vn", 
                                                                font = self.fonsize_s)
        self.setting_my_org_mani_name_vn_radio.grid(row = 0, column = 2,
                                                    padx = 5, 
                                                    sticky = tk.W)
        setting_my_org_mani_name_frame_line_1 = tk.Frame(self.setting_my_org_mani_name_frame)
        setting_my_org_mani_name_frame_line_1.grid(row = 1, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        ttk.Label(setting_my_org_mani_name_frame_line_1, 
                  text = "Member number (14 digits): ",                     
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)   
        self.setting_my_org_mani_mem_num_entry_vari = tk.StringVar()
        self.setting_my_org_mani_mem_num_entry = tk.Entry(setting_my_org_mani_name_frame_line_1, 
                                                          textvariable = self.setting_my_org_mani_mem_num_entry_vari, 
                                                          width = 16, 
                                                          font = self.fonsize_s)
        self.setting_my_org_mani_mem_num_entry.grid(row = 0, column = 1,
                                                    sticky = tk.W)
        self.setting_my_org_mani_name_en_frame = tk.Frame(self.setting_my_org_mani_name_frame)
        self.setting_my_org_mani_name_en_frame.grid(row = 2, column = 0,
                                                    sticky = tk.W)        
        ttk.Label(self.setting_my_org_mani_name_en_frame, 
                  text = "Given Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_my_org_mani_name_gn_entry_vari = tk.StringVar()
        self.setting_my_org_mani_name_gn_entry = tk.Entry(self.setting_my_org_mani_name_en_frame, 
                                                          textvariable = self.setting_my_org_mani_name_gn_entry_vari, 
                                                          width = 14, 
                                                          font = self.fonsize_s)
        self.setting_my_org_mani_name_gn_entry.grid(row = 1, column = 0,
                                                    sticky = tk.W)
        ttk.Label(self.setting_my_org_mani_name_en_frame, 
                  text = "Middle Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 1,
                                              sticky = tk.W)
        self.setting_my_org_mani_name_mn_entry_vari = tk.StringVar()
        self.setting_my_org_mani_name_mn_entry = tk.Entry(self.setting_my_org_mani_name_en_frame, 
                                                          textvariable = self.setting_my_org_mani_name_mn_entry_vari, 
                                                          width = 14, 
                                                          font = self.fonsize_s)
        self.setting_my_org_mani_name_mn_entry.grid(row = 1, column = 1,
                                                    sticky = tk.W)
        ttk.Label(self.setting_my_org_mani_name_en_frame, 
                  text = "Family Name",
                  width = 14,
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        self.setting_my_org_mani_name_fn_entry_vari = tk.StringVar()
        self.setting_my_org_mani_name_fn_entry = tk.Entry(self.setting_my_org_mani_name_en_frame, 
                                                          textvariable = self.setting_my_org_mani_name_fn_entry_vari, 
                                                          width = 14, 
                                                          font = self.fonsize_s)
        self.setting_my_org_mani_name_fn_entry.grid(row = 1, column = 2,
                                                    sticky = tk.W)
        self.setting_my_org_mani_name_vn_frame = tk.Frame(self.setting_my_org_mani_name_frame)
        self.setting_my_org_mani_name_vn_frame.grid(row = 2, column = 0,
                                                    sticky = tk.W)
        setting_my_org_mani_name_vn_frame_line_0 = tk.Frame(self.setting_my_org_mani_name_vn_frame)
        setting_my_org_mani_name_vn_frame_line_0.grid(row = 0, column = 0,
                                                      sticky = tk.W)
        ttk.Label(setting_my_org_mani_name_vn_frame_line_0, 
                  text = "Name type ",        
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_my_org_mani_name_vt_combo_vari = tk.StringVar()
        self.setting_my_org_mani_name_vt_combo = ttk.Combobox(setting_my_org_mani_name_vn_frame_line_0, 
                                                              textvariable = self.setting_my_org_mani_name_vt_combo_vari, 
                                                              values = self.virtual_type, 
                                                              width = 35, 
                                                              state = "readonly",
                                                              font = self.fonsize_s)
        self.setting_my_org_mani_name_vt_combo.grid(row = 0, column = 1, 
                                                    sticky = tk.W)
        self.setting_my_org_mani_name_vt_combo.set("Other")
        setting_my_org_mani_name_vn_frame_line_1 = tk.Frame(self.setting_my_org_mani_name_vn_frame)
        setting_my_org_mani_name_vn_frame_line_1.grid(row = 1, column = 0,
                                                      sticky = tk.W)
        ttk.Label(setting_my_org_mani_name_vn_frame_line_1, 
                  text = "Name ",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_my_org_mani_name_vn_entry_vari = tk.StringVar()
        self.setting_my_org_mani_name_vn_entry = tk.Entry(setting_my_org_mani_name_vn_frame_line_1, 
                                                          textvariable = self.setting_my_org_mani_name_vn_entry_vari, 
                                                          width = 14, 
                                                          font = self.fonsize_s)
        self.setting_my_org_mani_name_vn_entry.grid(row = 0, column = 1,
                                                  sticky = tk.W)
        ttk.Label(setting_my_org_mani_name_vn_frame_line_1, 
                  text = ", Addition (@ or #) ",
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        self.setting_my_org_mani_name_va_entry_vari = tk.StringVar()
        self.setting_my_org_mani_name_va_entry = tk.Entry(setting_my_org_mani_name_vn_frame_line_1, 
                                                          textvariable = self.setting_my_org_mani_name_va_entry_vari, 
                                                          width = 14, 
                                                          font = self.fonsize_s)
        self.setting_my_org_mani_name_va_entry.grid(row = 0, column = 3,
                                                    sticky = tk.W)
        ttk.Separator(self.setting_my_org_mani_list_frame, 
                      orient="horizontal").grid(row = 1, column = 0,
                                                sticky = tk.EW)
        self.setting_my_org_mani_org_frame = tk.Frame(self.setting_my_org_mani_list_frame)
        self.setting_my_org_mani_org_frame.grid(row = 2, column = 0,
                                                padx = 2, pady = 2,
                                                sticky = tk.W)
        ttk.Label(self.setting_my_org_mani_org_frame, 
                  text = "(3) Issuer of the member: ",                     
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        setting_my_org_mani_org_frame_line_1 = tk.Frame(self.setting_my_org_mani_org_frame)
        setting_my_org_mani_org_frame_line_1.grid(row = 1, column = 0,
                                                  sticky = tk.W)
        ttk.Label(setting_my_org_mani_org_frame_line_1, 
                  text = "Organization number (14 digits): ",                     
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)        
        self.setting_my_org_mani_org_num_entry_vari = tk.StringVar()
        self.setting_my_org_mani_org_num_entry = tk.Entry(setting_my_org_mani_org_frame_line_1, 
                                                          textvariable = self.setting_my_org_mani_org_num_entry_vari, 
                                                          width = 16, 
                                                          font = self.fonsize_s)
        self.setting_my_org_mani_org_num_entry.grid(row = 0, column = 1,
                                                    sticky = tk.W)
        setting_my_org_mani_org_frame_line_2 = tk.Frame(self.setting_my_org_mani_org_frame)
        setting_my_org_mani_org_frame_line_2.grid(row = 2, column = 0,
                                                  sticky = tk.W)
        ttk.Label(setting_my_org_mani_org_frame_line_2, 
                  text = "Organization's created date (UTC): ",                     
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        setting_my_org_mani_org_frame_line_2_date = tk.Frame(setting_my_org_mani_org_frame_line_2)
        setting_my_org_mani_org_frame_line_2_date.grid(row = 0, column = 1,
                                                       sticky = tk.W)
        ttk.Label(setting_my_org_mani_org_frame_line_2_date, 
                  text = "Year",
                  width = 6, 
                  font = self.fonsize_s).grid(row = 0, column = 0)
        self.setting_my_org_mani_org_date_year_spinbox_vari = tk.StringVar()
        self.setting_my_org_mani_org_date_year_spinbox = tk.Spinbox(setting_my_org_mani_org_frame_line_2_date, 
                                                                    textvariable = self.setting_my_org_mani_org_date_year_spinbox_vari, 
                                                                    width = 5, 
                                                                    from_ = 0, 
                                                                    to = 9999, 
                                                                    font = self.fonsize_s)
        self.setting_my_org_mani_org_date_year_spinbox.grid(row = 1, column = 0,
                                                                sticky = tk.W)
        ttk.Label(setting_my_org_mani_org_frame_line_2_date, 
                  text = "-",
                  font = self.fonsize_s).grid(row = 1, column = 1)
        ttk.Label(setting_my_org_mani_org_frame_line_2_date, 
                  text = "Month",
                  width = 6, 
                  font = self.fonsize_s).grid(row = 0, column = 2)
        self.setting_my_org_mani_org_date_month_spinbox_vari = tk.StringVar()
        self.setting_my_org_mani_org_date_month_spinbox = tk.Spinbox(setting_my_org_mani_org_frame_line_2_date, 
                                                                     textvariable = self.setting_my_org_mani_org_date_month_spinbox_vari, 
                                                                     width = 3, 
                                                                     from_ = 1, 
                                                                     to = 12, 
                                                                     font = self.fonsize_s)
        self.setting_my_org_mani_org_date_month_spinbox.grid(row = 1, column = 2,
                                                             sticky = tk.W)
        ttk.Label(setting_my_org_mani_org_frame_line_2_date, 
                  text = "-",
                  font = self.fonsize_s).grid(row = 1, column = 3)
        ttk.Label(setting_my_org_mani_org_frame_line_2_date, 
                  text = "Day",
                  width = 4, 
                  font = self.fonsize_s).grid(row = 0, column = 4)
        self.setting_my_org_mani_org_date_day_spinbox_vari = tk.StringVar()
        self.setting_my_org_mani_org_date_day_spinbox = tk.Spinbox(setting_my_org_mani_org_frame_line_2_date, 
                                                                   textvariable = self.setting_my_org_mani_org_date_day_spinbox_vari, 
                                                                   width = 3, 
                                                                   from_ = 1, 
                                                                   to = 31, 
                                                                   font = self.fonsize_s)
        self.setting_my_org_mani_org_date_day_spinbox.grid(row = 1, column = 4,
                                                           sticky = tk.W)
        ttk.Label(setting_my_org_mani_org_frame_line_2, 
                  text = ", time (UTC): ",                     
                  font = self.fonsize_s).grid(row = 0, column = 2,
                                              sticky = tk.W)
        setting_my_org_mani_org_frame_line_2_time = tk.Frame(setting_my_org_mani_org_frame_line_2)
        setting_my_org_mani_org_frame_line_2_time.grid(row = 0, column = 3,
                                                       sticky = tk.W)
        ttk.Label(setting_my_org_mani_org_frame_line_2_time, 
                  text = "Hour",
                  width = 5, 
                  font = self.fonsize_s).grid(row = 0, column = 0)
        self.setting_my_org_mani_org_time_hour_spinbox_vari = tk.StringVar()
        self.setting_my_org_mani_org_time_hour_spinbox = tk.Spinbox(setting_my_org_mani_org_frame_line_2_time, 
                                                                    textvariable = self.setting_my_org_mani_org_time_hour_spinbox_vari, 
                                                                    width = 3, 
                                                                    from_ = 0, 
                                                                    to = 23, 
                                                                    font = self.fonsize_s)
        self.setting_my_org_mani_org_time_hour_spinbox.grid(row = 1, column = 0,
                                                            sticky = tk.W)    
        ttk.Label(setting_my_org_mani_org_frame_line_2_time, 
                  text = ":",
                  font = self.fonsize_s).grid(row = 1, column = 1)
        ttk.Label(setting_my_org_mani_org_frame_line_2_time, 
                  text = "Minute",
                  width = 7, 
                  font = self.fonsize_s).grid(row = 0, column = 2)
        self.setting_my_org_mani_org_time_minute_spinbox_vari = tk.StringVar()
        self.setting_my_org_mani_org_time_minute_spinbox = tk.Spinbox(setting_my_org_mani_org_frame_line_2_time, 
                                                                      textvariable = self.setting_my_org_mani_org_time_minute_spinbox_vari, 
                                                                      width = 3, 
                                                                      from_ = 0, 
                                                                      to = 59, 
                                                                      font = self.fonsize_s)
        self.setting_my_org_mani_org_time_minute_spinbox.grid(row = 1, column = 2,
                                                              sticky = tk.W)
        ## command
        self.setting_my_org_basic_info_radio["command"] = self.setting_fun_my_org_switch_page
        self.setting_my_org_mani_list_radio["command"] = self.setting_fun_my_org_switch_page
        self.setting_my_org_org_num_copy_button["command"] = self.setting_fun_my_org_copy_org_num
        self.setting_my_org_admin_num_copy_button["command"] = self.setting_fun_my_org_copy_admin_num
        self.setting_my_org_admin_num_change_button["command"] = self.setting_fun_my_org_admin_change
        self.setting_my_org_org_name_edit_button["command"] = self.setting_fun_my_org_edit_org_name
        self.setting_my_org_org_name_copy_button["command"] = self.setting_fun_my_org_copy_org_name
        self.setting_my_org_org_name_cancel_button["command"] = self.setting_fun_my_org_cancel_org_name
        self.setting_my_org_org_name_entry.bind("<Escape>", self.setting_fun_my_org_escape_org_name)
        self.setting_my_org_org_name_confirm_button["command"] = self.setting_fun_my_org_confirm_org_name
        self.setting_my_org_org_name_entry.bind("<Return>", self.setting_fun_my_org_return_org_name)
        self.setting_my_org_city_edit_button["command"] = self.setting_fun_my_org_edit_city
        self.setting_my_org_city_copy_button["command"] = self.setting_fun_my_org_copy_city
        self.setting_my_org_city_cancel_button["command"] = self.setting_fun_my_org_cancel_city
        self.setting_my_org_city_entry.bind("<Escape>", self.setting_fun_my_org_escape_city)
        self.setting_my_org_city_confirm_button["command"] = self.setting_fun_my_org_confirm_city
        self.setting_my_org_city_entry.bind("<Return>", self.setting_fun_my_org_return_city)
        self.setting_my_org_region_edit_button["command"] = self.setting_fun_my_org_edit_region
        self.setting_my_org_region_cancel_button["command"] = self.setting_fun_my_org_cancel_region
        self.setting_my_org_region_confirm_button["command"] = self.setting_fun_my_org_confirm_region
        self.setting_my_org_mani_list_listbox.bind("<<ListboxSelect>>", self.setting_fun_my_org_listbox_select)
        self.setting_my_org_mani_list_add_button["command"] = self.setting_fun_my_org_listbox_add
        self.setting_my_org_mani_list_up_button["command"] = self.setting_fun_my_org_listbox_up
        self.setting_my_org_mani_list_down_button["command"] = self.setting_fun_my_org_listbox_down
        self.setting_my_org_mani_list_remove_button["command"] = self.setting_fun_my_org_listbox_remove
        self.setting_my_org_mani_new_gene_button["command"] = self.setting_fun_my_org_new_mani_gene
        self.setting_my_org_mani_new_confirm_button["command"] = self.setting_fun_my_org_new_mani_confirm
        self.setting_my_org_mani_old_copy_button["command"] = self.setting_fun_my_org_copy_mani
        self.setting_my_org_mani_name_en_radio["command"] = self.setting_fun_my_org_mani_name_switch
        self.setting_my_org_mani_name_vn_radio["command"] = self.setting_fun_my_org_mani_name_switch
        self.setting_my_org_mani_confirm_all_button["command"] = self.setting_fun_my_org_mani_confirm
        self.setting_my_org_output_button["command"] = self.setting_fun_my_org_output
        
        # org_list
        self.setting_org_list_frame = tk.Frame(self.setting_page_frame)
        self.setting_org_list_frame.grid_forget()        
        setting_org_list_frame_line_0 = tk.Frame(self.setting_org_list_frame)
        setting_org_list_frame_line_0.grid(row = 0, column = 0,
                                           padx = 2, pady = 2, 
                                           sticky = tk.W)
        setting_org_list_left_frame = tk.Frame(setting_org_list_frame_line_0)
        setting_org_list_left_frame.grid(row = 0, column = 0,
                                         padx = 5, pady = 5, 
                                         sticky = tk.NW)
        self.setting_org_list_listbox_select = ttk.Label(setting_org_list_left_frame, 
                                                         text = "Currently select: -", 
                                                         width = 28, 
                                                         font = self.fonsize_s)
        self.setting_org_list_listbox_select.grid(row = 0, column = 0)        
        setting_org_list_listbox_frame = tk.Frame(setting_org_list_left_frame)
        setting_org_list_listbox_frame.grid(row = 1, column = 0)
        self.setting_org_list_listbox_vari = tk.StringVar(value = [])
        self.setting_org_list_listbox = tk.Listbox(setting_org_list_listbox_frame, 
                                                   listvariable = self.setting_org_list_listbox_vari, 
                                                   width = 24, height = 9, 
                                                   font = self.fonsize_s, 
                                                   selectmode = "single")
        self.setting_org_list_listbox.grid(row = 0, column = 0, 
                                           sticky = tk.W)
        setting_org_list_listbox_x_scrollbar = ttk.Scrollbar(setting_org_list_listbox_frame, 
                                                             orient = "horizontal", 
                                                             command = self.setting_org_list_listbox.xview)
        self.setting_org_list_listbox["xscrollcommand"] = setting_org_list_listbox_x_scrollbar.set
        setting_org_list_listbox_x_scrollbar.grid(row = 1, column = 0, 
                                                  sticky = tk.EW)
        setting_org_list_listbox_y_scrollbar = ttk.Scrollbar(setting_org_list_listbox_frame, 
                                                             orient = "vertical", 
                                                             command = self.setting_org_list_listbox.yview)
        self.setting_org_list_listbox["yscrollcommand"] = setting_org_list_listbox_y_scrollbar.set
        setting_org_list_listbox_y_scrollbar.grid(row = 0, column = 1, 
                                                  sticky = tk.NS)
        setting_org_list_listbox_upper_button_frame = tk.Frame(setting_org_list_left_frame)
        setting_org_list_listbox_upper_button_frame.grid(row = 2, column = 0)
        self.setting_org_list_add_button = tk.Button(setting_org_list_listbox_upper_button_frame, 
                                                     text = "✚", 
                                                     width = 3, 
                                                     font = self.fonsize_s, 
                                                     foreground = "green", 
                                                     activeforeground = "green")
        self.setting_org_list_add_button.grid(row = 0, column = 0,
                                              sticky = tk.W)        
        self.setting_org_list_up_button = tk.Button(setting_org_list_listbox_upper_button_frame, 
                                                    text = "▲", 
                                                    width = 3, 
                                                    font = self.fonsize_s, 
                                                    foreground = "blue", 
                                                    activeforeground = "blue")
        self.setting_org_list_up_button.grid(row = 0, column = 1,
                                             sticky = tk.W)
        self.setting_org_list_down_button = tk.Button(setting_org_list_listbox_upper_button_frame, 
                                                      text = "▼", 
                                                      width = 3, 
                                                      font = self.fonsize_s, 
                                                      foreground = "blue", 
                                                      activeforeground = "blue")
        self.setting_org_list_down_button.grid(row = 0, column = 2,
                                               sticky = tk.W)
        self.setting_org_list_remove_button = tk.Button(setting_org_list_listbox_upper_button_frame, 
                                                        text = "✖",  
                                                        width = 3, 
                                                        font = self.fonsize_s, 
                                                        foreground = "red", 
                                                        activeforeground = "red")
        self.setting_org_list_remove_button.grid(row = 0, column = 3,
                                                 sticky = tk.W)        
        setting_org_list_listbox_bottom_button_frame = tk.Frame(setting_org_list_left_frame)
        setting_org_list_listbox_bottom_button_frame.grid(row = 3, column = 0, 
                                                          padx = 2, pady = 2)
        self.setting_org_list_output_button = tk.Button(setting_org_list_listbox_bottom_button_frame, 
                                                        text = "Output OrganizationList.dat", 
                                                        width = 29, 
                                                        font = self.fonsize_s)
        self.setting_org_list_output_button.grid(row = 0, column = 0,
                                                 sticky = tk.W)
        self.setting_org_list_right_frame = tk.Frame(setting_org_list_frame_line_0)
        self.setting_org_list_right_frame.grid(row = 0, column = 1,
                                               padx = 5, pady = 5, 
                                               sticky = tk.NW)
        setting_org_list_right_frame_line_0 = tk.Frame(self.setting_org_list_right_frame)
        setting_org_list_right_frame_line_0.grid(row = 0, column = 0,
                                                 padx = 2, pady = 2, 
                                                 sticky = tk.NW)
        ttk.Label(setting_org_list_right_frame_line_0, 
                  text = "(1) Organization number:",
                  font = self.fonsize_s).grid(row = 0, column = 0, 
                                              sticky = tk.W)
        self.setting_org_list_org_num_entry_vari = tk.StringVar()
        self.setting_org_list_org_num_entry = tk.Entry(setting_org_list_right_frame_line_0, 
                                                       textvariable = self.setting_org_list_org_num_entry_vari, 
                                                       width = 16, 
                                                       font = self.fonsize_s)
        self.setting_org_list_org_num_entry.grid(row = 1, column = 0,
                                                 sticky = tk.W)   
        ttk.Separator(self.setting_org_list_right_frame, 
                      orient="horizontal").grid(row = 1, column = 0,
                                                sticky = tk.EW)
        setting_org_list_right_frame_line_1 = tk.Frame(self.setting_org_list_right_frame)
        setting_org_list_right_frame_line_1.grid(row = 2, column = 0,
                                                 padx = 2, pady = 2, 
                                                 sticky = tk.NW)                                           
        ttk.Label(setting_org_list_right_frame_line_1, 
                  text = "(2) Organization name:",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        self.setting_org_list_org_name_entry_vari = tk.StringVar()
        self.setting_org_list_org_name_entry = tk.Entry(setting_org_list_right_frame_line_1, 
                                                        textvariable = self.setting_org_list_org_name_entry_vari, 
                                                        width = 35, 
                                                        font = self.fonsize_s)
        self.setting_org_list_org_name_entry.grid(row = 1, column = 0,
                                                  sticky = tk.W) 
        ttk.Separator(self.setting_org_list_right_frame, 
                      orient="horizontal").grid(row = 3, column = 0,
                                                sticky = tk.EW)
        setting_org_list_right_frame_line_2 = tk.Frame(self.setting_org_list_right_frame)
        setting_org_list_right_frame_line_2.grid(row = 4, column = 0,
                                                 padx = 2, pady = 2, 
                                                 sticky = tk.NW) 
        ttk.Label(setting_org_list_right_frame_line_2, 
                  text = "(3) Created date (UTC):",
                  font = self.fonsize_s).grid(row = 0, column = 0,
                                              sticky = tk.W)
        setting_org_list_right_frame_line_2_date = tk.Frame(setting_org_list_right_frame_line_2)
        setting_org_list_right_frame_line_2_date.grid(row = 1, column = 0,
                                                      sticky = tk.N)
        ttk.Label(setting_org_list_right_frame_line_2_date, 
                  text = "Year",
                  width = 6, 
                  font = self.fonsize_s).grid(row = 0, column = 0)
        self.setting_org_list_line_2_date_year_spinbox_vari = tk.StringVar()
        self.setting_org_list_line_2_date_year_spinbox = tk.Spinbox(setting_org_list_right_frame_line_2_date, 
                                                                    textvariable = self.setting_org_list_line_2_date_year_spinbox_vari, 
                                                                    width = 5, 
                                                                    from_ = 0, 
                                                                    to = 9999, 
                                                                    font = self.fonsize_s)
        self.setting_org_list_line_2_date_year_spinbox.grid(row = 1, column = 0,
                                                            sticky = tk.W)
        ttk.Label(setting_org_list_right_frame_line_2_date, 
                  text = "-",
                  font = self.fonsize_s).grid(row = 1, column = 1)
        ttk.Label(setting_org_list_right_frame_line_2_date, 
                  text = "Month",
                  width = 6, 
                  font = self.fonsize_s).grid(row = 0, column = 2)
        self.setting_org_list_line_2_date_month_spinbox_vari = tk.StringVar()
        self.setting_org_list_line_2_date_month_spinbox = tk.Spinbox(setting_org_list_right_frame_line_2_date, 
                                                                     textvariable = self.setting_org_list_line_2_date_month_spinbox_vari, 
                                                                     width = 3, 
                                                                     from_ = 1, 
                                                                     to = 12, 
                                                                     font = self.fonsize_s)
        self.setting_org_list_line_2_date_month_spinbox.grid(row = 1, column = 2,
                                                             sticky = tk.W)
        ttk.Label(setting_org_list_right_frame_line_2_date, 
                  text = "-",
                  font = self.fonsize_s).grid(row = 1, column = 3)
        ttk.Label(setting_org_list_right_frame_line_2_date, 
                  text = "Day",
                  width = 4, 
                  font = self.fonsize_s).grid(row = 0, column = 4)
        self.setting_org_list_line_2_date_day_spinbox_vari = tk.StringVar()
        self.setting_org_list_line_2_date_day_spinbox = tk.Spinbox(setting_org_list_right_frame_line_2_date, 
                                                                   textvariable = self.setting_org_list_line_2_date_day_spinbox_vari, 
                                                                   width = 3, 
                                                                   from_ = 1, 
                                                                   to = 31, 
                                                                   font = self.fonsize_s)
        self.setting_org_list_line_2_date_day_spinbox.grid(row = 1, column = 4,
                                                           sticky = tk.W)
        ttk.Separator(setting_org_list_right_frame_line_2, 
                      orient="vertical").grid(row = 0, column = 1,
                                              rowspan = 2, 
                                              sticky = tk.NS)
        ttk.Label(setting_org_list_right_frame_line_2, 
                  text = "(4) Created time (UTC):",
                  font = self.fonsize_s).grid(row = 0, column = 2, 
                                              sticky = tk.W)
        setting_org_list_right_frame_line_2_time = tk.Frame(setting_org_list_right_frame_line_2)
        setting_org_list_right_frame_line_2_time.grid(row = 1, column = 2,
                                                      sticky = tk.N)
        ttk.Label(setting_org_list_right_frame_line_2_time, 
                  text = "Hour",
                  width = 5, 
                  font = self.fonsize_s).grid(row = 0, column = 0)
        self.setting_org_list_line_2_time_hour_spinbox_vari = tk.StringVar()
        self.setting_org_list_line_2_time_hour_spinbox = tk.Spinbox(setting_org_list_right_frame_line_2_time, 
                                                                    textvariable = self.setting_org_list_line_2_time_hour_spinbox_vari, 
                                                                    width = 3, 
                                                                    from_ = 0, 
                                                                    to = 23, 
                                                                    font = self.fonsize_s)
        self.setting_org_list_line_2_time_hour_spinbox.grid(row = 1, column = 0,
                                                            sticky = tk.W)    
        ttk.Label(setting_org_list_right_frame_line_2_time, 
                  text = ":",
                  font = self.fonsize_s).grid(row = 1, column = 1)
        ttk.Label(setting_org_list_right_frame_line_2_time, 
                  text = "Minute",
                  width = 7, 
                  font = self.fonsize_s).grid(row = 0, column = 2)
        self.setting_org_list_line_2_time_minute_spinbox_vari = tk.StringVar()
        self.setting_org_list_line_2_time_minute_spinbox = tk.Spinbox(setting_org_list_right_frame_line_2_time, 
                                                                      textvariable = self.setting_org_list_line_2_time_minute_spinbox_vari, 
                                                                      width = 3, 
                                                                      from_ = 0, 
                                                                      to = 59, 
                                                                      font = self.fonsize_s)
        self.setting_org_list_line_2_time_minute_spinbox.grid(row = 1, column = 2,
                                                              sticky = tk.W)
        ttk.Separator(self.setting_org_list_right_frame, 
                      orient="horizontal").grid(row = 5, column = 0,
                                                sticky = tk.EW)
        setting_org_list_right_frame_line_3 = tk.Frame(self.setting_org_list_right_frame)
        setting_org_list_right_frame_line_3.grid(row = 6, column = 0,
                                                 padx = 2, pady = 2, 
                                                 sticky = tk.NW) 
        ttk.Label(setting_org_list_right_frame_line_3, 
                  text = "(5) Manipulation number of the organization's creator:",
                  font = self.fonsize_s).grid(row = 0, column = 0, 
                                              sticky = tk.W)
        self.setting_org_list_org_gene_num_entry_vari = tk.StringVar()
        self.setting_org_list_org_gene_num_entry = tk.Entry(setting_org_list_right_frame_line_3, 
                                                            textvariable = self.setting_org_list_org_gene_num_entry_vari, 
                                                            width = 9, 
                                                            font = self.fonsize_s)
        self.setting_org_list_org_gene_num_entry.grid(row = 1, column = 0,
                                                      sticky = tk.W) 
        ttk.Separator(self.setting_org_list_right_frame, 
                      orient="horizontal").grid(row = 7, column = 0,
                                                sticky = tk.EW)
        self.setting_org_list_confirm_button = tk.Button(self.setting_org_list_right_frame,
                                                         text = "Confirm", 
                                                         width = 8, 
                                                         font = self.fonsize_m, 
                                                         foreground = "green", 
                                                         activeforeground = "green")
        self.setting_org_list_confirm_button.grid(row = 8, column = 0,
                                                  padx = 2, pady = 2, 
                                                  sticky = tk.NE)
        self.setting_org_list_cur_sel = -1
        
        self.setting_org_list_frame_line_1 = tk.Frame(self.setting_org_list_frame)
        self.setting_org_list_frame_line_1.grid(row = 1, column = 0,
                                                padx = 2, pady = 2, 
                                                sticky = tk.W)
        self.setting_org_list_frame_line_1_not = ttk.Label(self.setting_org_list_frame, 
                                                           text = "The file 'assets/OrganizationList.dat' is not existing.",
                                                           foreground = "red", 
                                                           font = self.fonsize_s)
        self.setting_org_list_frame_line_1_not.grid_forget()
        self.setting_org_list_frame_line_1_broken = ttk.Label(self.setting_org_list_frame, 
                                                              text = "The file 'assets/OrganizationList.dat' is broken.",
                                                              foreground = "red", 
                                                              font = self.fonsize_s)
        self.setting_org_list_frame_line_1_broken.grid_forget()
        ttk.Label(self.setting_org_list_frame_line_1, 
                  text = "The OrganizationList.dat is created by ",
                  font = self.fonsize_s).grid(row = 0, column = 0)
        self.setting_org_list_frame_line_1_mani_num = ttk.Label(self.setting_org_list_frame_line_1, 
                                                                text = "",
                                                                font = self.fonsize_s)
        self.setting_org_list_frame_line_1_mani_num.grid(row = 0, column = 1)
        ttk.Label(self.setting_org_list_frame_line_1, 
                  text = " of ",
                  font = self.fonsize_s).grid(row = 0, column = 2)
        self.setting_org_list_frame_line_1_org_num = ttk.Label(self.setting_org_list_frame_line_1, 
                                                               text = "",
                                                               font = self.fonsize_s)
        self.setting_org_list_frame_line_1_org_num.grid(row = 0, column = 3)
        ttk.Label(self.setting_org_list_frame_line_1, 
                  text = ", on ",
                  font = self.fonsize_s).grid(row = 0, column = 4)
        self.setting_org_list_frame_line_1_date = ttk.Label(self.setting_org_list_frame_line_1, 
                                                            text = "",
                                                            font = self.fonsize_s)
        self.setting_org_list_frame_line_1_date.grid(row = 0, column = 5)
        ttk.Label(self.setting_org_list_frame_line_1, 
                  text = " at ",
                  font = self.fonsize_s).grid(row = 0, column = 6)
        self.setting_org_list_frame_line_1_time = ttk.Label(self.setting_org_list_frame_line_1, 
                                                            text = "",
                                                            font = self.fonsize_s)
        self.setting_org_list_frame_line_1_time.grid(row = 0, column = 7)
        ## command
        self.setting_org_list_listbox.bind("<<ListboxSelect>>", self.setting_fun_org_list_listbox_select)
        self.setting_org_list_add_button["command"] = self.setting_fun_org_list_listbox_add
        self.setting_org_list_up_button["command"] = self.setting_fun_org_list_listbox_up
        self.setting_org_list_down_button["command"] = self.setting_fun_org_list_listbox_down
        self.setting_org_list_remove_button["command"] = self.setting_fun_org_list_listbox_remove
        self.setting_org_list_confirm_button["command"] = self.setting_fun_org_list_confirm
        self.setting_org_list_output_button["command"] = self.setting_fun_org_list_output
    
    def setting_fun_select(self):
        temp_str = self.setting_page_radio_vari.get()
        if temp_str == "mani_num":
            self.setting_mani_num_frame.grid(row = 1, column = 0,
                                             padx = 5, pady = 5, 
                                             sticky = tk.NW)
            self.setting_fun_org_scan()
            self.setting_mani_num_entry.delete(0, "end")
            self.setting_gene_org_frame_0.grid_forget()
            self.setting_gene_org_frame_1.grid_forget()
            self.setting_direct_frame.grid_forget()
            self.setting_my_org_frame.grid_forget()
            self.setting_org_list_frame.grid_forget()
        elif temp_str == "gene_org":
            self.setting_mani_num_frame.grid_forget()
            self.setting_gene_org_frame_0.grid(row = 1, column = 0,
                                               padx = 5, pady = 5, 
                                               sticky = tk.NW)
            self.setting_gene_org_frame_1.grid_forget()            
            self.setting_new_org_name_entry.delete(0, "end")   
            self.setting_new_org_init_0_entry.delete(0, "end")   
            self.setting_new_org_init_1_entry.delete(0, "end")   
            self.setting_new_org_init_2_entry.delete(0, "end")
            self.setting_direct_frame.grid_forget()
            self.setting_my_org_frame.grid_forget()
            self.setting_org_list_frame.grid_forget()
        elif temp_str == "direct":
            self.setting_mani_num_frame.grid_forget()
            self.setting_gene_org_frame_0.grid_forget()
            self.setting_gene_org_frame_1.grid_forget()
            self.setting_direct_frame.grid(row = 1, column = 0,
                                           padx = 5, pady = 5, 
                                           sticky = tk.NW)
            self.setting_fun_read_direct()
            self.setting_my_org_frame.grid_forget()
            self.setting_org_list_frame.grid_forget()
        elif temp_str == "my_org":
            self.setting_mani_num_frame.grid_forget()
            self.setting_gene_org_frame_0.grid_forget()
            self.setting_gene_org_frame_1.grid_forget()
            self.setting_direct_frame.grid_forget()
            if self.login_state:
                self.setting_my_org_frame.grid(row = 1, column = 0,
                                               padx = 5, pady = 5, 
                                               sticky = tk.NW)
                if os.path.exists(self.cur_org_file_name):
                    with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                        read_text = read_file.read()
                        self.cur_org = self.reading_str_text_org(read_text)
                    if not self.cur_org is None:
                        self.setting_my_org_basic_info_radio.select()
                        self.setting_fun_my_org_switch_page()
                    else:
                        self.setting_my_org_frame.grid_forget()
                else:
                    self.setting_my_org_frame.grid_forget()
            else:
                self.setting_my_org_frame.grid_forget()
            self.setting_org_list_frame.grid_forget()
        elif temp_str == "org_list":
            self.setting_mani_num_frame.grid_forget()
            self.setting_gene_org_frame_0.grid_forget()
            self.setting_gene_org_frame_1.grid_forget()
            self.setting_direct_frame.grid_forget()
            self.setting_my_org_frame.grid_forget()
            if self.login_state:
                self.setting_org_list_frame.grid(row = 1, column = 0,
                                                 padx = 5, pady = 5, 
                                                 sticky = tk.NW)
                self.setting_fun_org_list_read()
            else:
                self.setting_org_list_frame.grid_forget()
    
    def setting_fun_org_scan(self):
        temp_file_list = os.scandir("assets")
        temp_file_name_list = []
        for e in temp_file_list:
            temp_str_0 = e.name
            temp_file_name_list.append(temp_str_0)
        temp_select_name_list = []
        for n in range(len(temp_file_name_list)):
            temp_str_0 = temp_file_name_list[n]
            if len(temp_str_0) == 42:
                if temp_str_0[0:4].upper() == "ORG_":
                    temp_bool = True
                    for n1 in range(4, 16):
                        if not temp_str_0[n1] in self.numeric_digits:
                            temp_bool = False
                            break
                    if temp_bool:
                        if temp_str_0[16] == "_":
                            for n1 in range(17, 38):
                                if not temp_str_0[n1].upper() in self.numeric_hex_digits:
                                    temp_bool = False
                                    break
                            if temp_bool:
                                if temp_str_0[38:42].upper() == ".DAT":
                                    temp_select_name_list.append(temp_str_0)
        self.setting_org_file_combo["values"] = temp_select_name_list
        if self.basic_parameter[0] in temp_select_name_list:
            self.setting_org_file_combo.set(self.basic_parameter[0])
            with open("assets/"+self.basic_parameter[0], "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.sel_org = self.reading_str_text_org(read_text)
                read_file.close()
            temp_bool = True
            if not self.sel_org is None:
                temp_str_1 = self.basic_parameter[0][4:8]
                temp_str_1 = temp_str_1+"-"
                temp_str_1 = temp_str_1+self.basic_parameter[0][8:10]
                temp_str_1 = temp_str_1+"-"
                temp_str_1 = temp_str_1+self.basic_parameter[0][10:12]
                temp_str_2 = self.basic_parameter[0][12:14]
                temp_str_2 = temp_str_2+":"
                temp_str_2 = temp_str_2+self.basic_parameter[0][14:16]
                temp_str_3 = self.basic_parameter[0][17:38].upper()
                if self.sel_org[0][1] != temp_str_3:
                    temp_bool = False
                elif self.sel_org[0][5][1] != temp_str_1:
                    temp_bool = False
                elif self.sel_org[0][5][2] != temp_str_2:
                    temp_bool = False
            else:
                temp_bool = False
            if temp_bool:
                self.setting_org_num["text"] = self.sel_org[0][0]
                self.setting_org_name["text"] = self.sel_org[0][2]
            else:
                self.sel_org = None            
        else:
            self.setting_org_file_combo.set("")
    
    def setting_fun_org_select(self, event):
        temp_str_0 = self.setting_org_file_combo_vari.get().strip()
        if len(temp_str_0) > 0:
            with open("assets/"+temp_str_0, "r", encoding = "utf-8") as read_file:
                read_text = read_file.read()
                self.sel_org = self.reading_str_text_org(read_text)
                read_file.close()
            temp_bool = True
            if not self.sel_org is None:
                temp_str_1 = temp_str_0[4:8]
                temp_str_1 = temp_str_1+"-"
                temp_str_1 = temp_str_1+temp_str_0[8:10]
                temp_str_1 = temp_str_1+"-"
                temp_str_1 = temp_str_1+temp_str_0[10:12]
                temp_str_2 = temp_str_0[12:14]
                temp_str_2 = temp_str_2+":"
                temp_str_2 = temp_str_2+temp_str_0[14:16]
                temp_str_3 = temp_str_0[17:38].upper()
                if self.sel_org[0][1] != temp_str_3:
                    temp_bool = False
                elif self.sel_org[0][5][1] != temp_str_1:
                    temp_bool = False
                elif self.sel_org[0][5][2] != temp_str_2:
                    temp_bool = False
            else:
                temp_bool = False
            if not temp_bool:
                self.sel_org = None
                showerror(title = "Error", 
                          message = "The organization.dat file is not readable.") 
        else:
            self.sel_org = None
        if self.sel_org is None:
            self.setting_org_num["text"] = ""
            self.setting_org_name["text"] = ""
        else:
            self.setting_org_num["text"] = self.sel_org[0][0]
            self.setting_org_name["text"] = self.sel_org[0][2]
    
    def setting_fun_org_confirm(self):
        temp_str_0 = self.setting_mani_num_entry_vari.get().strip().upper()
        if not self.sel_org is None:
            if temp_str_0 in self.sel_org[2]:
                self.cur_org_file_name = self.setting_org_file_combo_vari.get().strip()
                self.cur_org_file_name = "assets/"+self.cur_org_file_name
                self.cur_mani_num = temp_str_0
                with open(self.cur_org_file_name, "r", encoding = "utf-8") as read_file:
                    read_text = read_file.read()
                    self.cur_org = self.reading_str_text_org(read_text)
                self.label_org_num["text"] = self.cur_org[0][0]
                self.label_mani_num["text"] = self.cur_mani_num 
                self.basic_parameter[0] = self.setting_org_file_combo_vari.get().strip()
                temp_str_1 = self.basic_parameter[0]
                temp_str_1 = temp_str_1+self.dat_file_sep
                temp_str_1 = temp_str_1+self.basic_parameter[1][0]
                temp_str_1 = temp_str_1+self.dat_file_sep
                if self.basic_parameter[1][2][1]:
                    temp_str_1 = temp_str_1+"1"
                else:
                    temp_str_1 = temp_str_1+"0"
                temp_str_1 = temp_str_1+self.dat_file_sub_sep
                if self.basic_parameter[1][2][2]:
                    temp_str_1 = temp_str_1+"1"
                else:
                    temp_str_1 = temp_str_1+"0"
                temp_str_1 = temp_str_1+self.dat_file_sub_sep
                if self.basic_parameter[1][2][3]:
                    temp_str_1 = temp_str_1+"1"
                else:
                    temp_str_1 = temp_str_1+"0"
                temp_str_1 = temp_str_1+self.dat_file_sep
                temp_str_1 = temp_str_1+self.basic_parameter[2][0]
                temp_str_1 = temp_str_1+self.dat_file_sep
                temp_str_1 = temp_str_1+self.dat_file_sep
                temp_str_1 = temp_str_1+self.basic_parameter[3][0]
                temp_str_1 = temp_str_1+self.dat_file_sep
                temp_str_1 = temp_str_1+self.dat_file_sep
                temp_str_1 = temp_str_1+self.basic_parameter[4][0]
                temp_str_1 = temp_str_1+self.dat_file_sep
                with open("assets/NumGene.dat", "w", encoding = "utf-8") as save_file:
                    save_file.write(temp_str_1)
                    save_file.close()
                showinfo(title = "The manipulation number is set", 
                         message = "Organization number: "+self.cur_org[0][0]+"\nManipulation number:"+self.cur_mani_num+"\nis set.")
                self.setting_mani_num_entry.delete(0, "end")
                self.login_state = True
            else:
                showerror(title = "Error", 
                          message = "The manipulation number is not in the organization.dat file.") 
        else:
            showerror(title = "Error", 
                      message = "The organization.dat file is not readable.") 
    
    def setting_fun_org_escqpe(self, event):
        self.setting_mani_num_entry.delete(0, "end")
    
    def setting_fun_org_return(self, event):
        self.setting_fun_org_confirm()
    
    def setting_fun_generate_org_next_0(self):
        temp_str_0 = self.setting_new_org_name_entry_vari.get().strip()
        temp_str_1 = self.setting_new_org_init_0_entry_vari.get().strip()
        temp_str_2 = self.setting_new_org_init_1_entry_vari.get().strip()
        temp_str_3 = self.setting_new_org_init_2_entry_vari.get().strip()
        temp_num_0 = len(temp_str_0)
        if (temp_num_0 > 0) & (temp_num_0 <= self.org_name_max_len):
            if (len(temp_str_1) == 1) & (len(temp_str_2) == 1) & (len(temp_str_3) == 1):
                temp_str_1 = temp_str_1.upper()
                temp_str_2 = temp_str_2.upper()
                temp_str_3 = temp_str_3.upper()
                English_name_capital = ("A", "B", "C", "D", "E", "F", "G", 
                                        "H", "I", "J", "K", "L", "M", "N", 
                                        "O", "P", "Q", "R", "S", "T", 
                                        "U", "V", "W", "X", "Y", "Z")
                if ((temp_str_1 in English_name_capital) & (temp_str_1 in English_name_capital) & 
                    (temp_str_1 in English_name_capital)):
                    self.setting_new_org_init_list = [temp_str_1, temp_str_2, temp_str_3]
                    self.cur_progress_bool = True
                    out_list = self.number_organization_generate([temp_str_0], self.setting_new_org_init_list)
                    self.cur_progress_bool = False
                    out_list = out_list[0]
                    if not out_list is None:
                        temp_str_1 = self.num_organization_64_2_16(out_list[0])
                        temp_str_2 = self.number_manipulation_generate(out_list[0])
                        self.setting_new_org_tuple = out_list
                        self.setting_new_org_str_0 = temp_str_1
                        self.setting_new_org_str_1 = temp_str_2
                        self.setting_gene_org_frame_0.grid_forget()
                        self.setting_gene_org_frame_1.grid(row = 1, column = 0,
                                                           padx = 5, pady = 5, 
                                                           sticky = tk.NW)
                        self.setting_gene_org_1_new_radio.select()
                        self.setting_fun_generate_org_new_exist_switch_1()
                        self.setting_gene_org_new_gn_entry.delete(0, "end")
                        self.setting_gene_org_new_mn_entry.delete(0, "end")
                        self.setting_gene_org_new_fn_entry.delete(0, "end")
                        self.setting_gene_org_new_vt_combo.set("Other")
                        self.setting_gene_org_new_vn_entry.delete(0, "end")
                        self.setting_gene_org_new_va_entry.delete(0, "end")
                        self.setting_gene_org_frame_1_new_admin_en_radio.select()
                        self.setting_gene_org_exist_mem_num_entry.delete(0, "end")
                        self.setting_gene_org_exist_gn_entry.delete(0, "end")
                        self.setting_gene_org_exist_mn_entry.delete(0, "end")
                        self.setting_gene_org_exist_fn_entry.delete(0, "end")
                        self.setting_gene_org_exist_vt_combo.set("Other")
                        self.setting_gene_org_exist_vn_entry.delete(0, "end")
                        self.setting_gene_org_exist_va_entry.delete(0, "end")
                        self.setting_gene_org_exist_org_num_entry.delete(0, "end")
                        self.setting_gene_org_exist_org_date_year_spinbox.delete(0, "end")
                        self.setting_gene_org_exist_org_date_year_spinbox.insert(0, "2020")
                        self.setting_gene_org_exist_org_date_month_spinbox.delete(0, "end")
                        self.setting_gene_org_exist_org_date_month_spinbox.insert(0, "1")
                        self.setting_gene_org_exist_org_date_day_spinbox.delete(0, "end")
                        self.setting_gene_org_exist_org_date_day_spinbox.insert(0, "1")
                        self.setting_gene_org_exist_org_time_hour_spinbox.delete(0, "end")
                        self.setting_gene_org_exist_org_time_hour_spinbox.insert(0, "0")
                        self.setting_gene_org_exist_org_time_minute_spinbox.delete(0, "end")
                        self.setting_gene_org_exist_org_time_minute_spinbox.insert(0, "0")                
                    else:
                        showerror(title = "Error", 
                                  message = "The name is not valie.")  
                else:
                    showerror(title = "Error", 
                              message = "The initial(s) is not valie.") 
            else:
                showerror(title = "Error", 
                          message = "The initial(s) is not valie.")   
        else:
            showerror(title = "Error", 
                      message = "The name is not valie.")   
    
    def setting_fun_generate_org_prev_1(self):
        self.setting_new_org_name_entry.delete(0, "end")
        self.setting_new_org_name_entry.insert(0, self.setting_new_org_tuple[1])
        self.setting_gene_org_frame_0.grid(row = 1, column = 0,
                                           padx = 5, pady = 5, 
                                           sticky = tk.NW)
        self.setting_gene_org_frame_1.grid_forget()
    
    def setting_fun_generate_org_new_exist_switch_1(self):
        temp_str_0 = self.setting_gene_org_1_radio_vari.get()
        if temp_str_0 == "new":
            self.setting_gene_org_frame_1_new_frame.grid(row = 1, column = 0,
                                                         padx = 2, pady = 2,
                                                         sticky = tk.W)
            self.setting_gene_org_frame_1_exist_frame.grid_forget()
        elif temp_str_0 == "exist":
            self.setting_gene_org_frame_1_new_frame.grid_forget()
            self.setting_gene_org_frame_1_exist_frame.grid(row = 1, column = 0,
                                                           padx = 2, pady = 2,
                                                           sticky = tk.W)
            self.setting_gene_org_frame_1_exist_admin_en_radio.select()
            self.setting_fun_generate_org_exist_member_switch_1()
    
    def setting_fun_generate_org_exist_member_switch_1(self):
        temp_str_0 = self.setting_gene_org_frame_1_exist_admin_radio_vari.get()
        if temp_str_0 == "en":
            self.setting_gene_org_frame_1_exist_frame_line_0_en.grid(row = 2, column = 0,
                                                                     sticky = tk.W)
            self.setting_gene_org_frame_1_exist_frame_line_0_vn.grid_forget()
        elif temp_str_0 == "vn":
            self.setting_gene_org_frame_1_exist_frame_line_0_en.grid_forget()
            self.setting_gene_org_frame_1_exist_frame_line_0_vn.grid(row = 2, column = 0,
                                                                     sticky = tk.W)
    
    def setting_fun_generate_org_gene_1(self):
        temp_str_0 = self.setting_gene_org_1_radio_vari.get()
        if temp_str_0 == "new":
            temp_list_1 = [self.setting_gene_org_new_gn_entry_vari.get().strip(), 
                           self.setting_gene_org_new_mn_entry_vari.get().strip(), 
                           self.setting_gene_org_new_fn_entry_vari.get().strip()]
            temp_list_1 = self.English_name_change_quotation_mark(temp_list_1)
            if not temp_list_1 is None: 
                self.cur_progress_bool = True
                temp_list_2 = self.number_mix_generate([[temp_list_1[0], temp_list_1[2]]], self.setting_new_org_init_list)
                self.cur_progress_bool = False
                temp_list_2 = temp_list_2[0]
                if not temp_list_2 is None:
                    temp_list_3 = [self.setting_gene_org_new_vt_combo_vari.get().strip(), 
                                   self.setting_gene_org_new_vn_entry_vari.get().strip(), 
                                   self.setting_gene_org_new_va_entry_vari.get().strip()]
                    temp_list_3 = self.virtual_name_change_quotation_mark(temp_list_3)
                    if not temp_list_3 is None:
                        self.cur_progress_bool = True
                        temp_list_4 = self.number_member_generate([[temp_list_2[0], temp_list_1[0], temp_list_1[2], 
                                                                    temp_list_3[1], self.setting_new_org_tuple[0], 
                                                                    temp_list_2[4], temp_list_2[5]]])
                        self.cur_progress_bool = False
                        temp_list_4 = temp_list_4[0]
                        if not temp_list_4 is None:
                            temp_str_1 = self.setting_new_org_init_list[0]+self.setting_new_org_init_list[1]+self.setting_new_org_init_list[2]
                            temp_str_2 = self.setting_gene_org_frame_1_new_admin_radio_vari.get().strip()
                            temp_list_5 = [self.setting_new_org_str_1, self.setting_new_org_tuple[2], self.setting_new_org_tuple[3]]
                            temp_list_6 = ["", self.regions_vec[-1]]
                            if temp_str_2 == "en":
                                temp_list_7 = [self.setting_new_org_str_1, True, temp_list_4[0], 
                                               temp_str_2, temp_list_1[0], temp_list_1[1], temp_list_1[2], 
                                               self.setting_new_org_tuple[0], 
                                               self.setting_new_org_tuple[2], 
                                               self.setting_new_org_tuple[3]]
                            elif temp_str_2 == "vn":
                                temp_list_7 = [self.setting_new_org_str_1, True, temp_list_4[0], 
                                               temp_str_2, temp_list_3[0], temp_list_3[1], temp_list_3[2], 
                                               self.setting_new_org_tuple[0], 
                                               self.setting_new_org_tuple[2], 
                                               self.setting_new_org_tuple[3]]
                            else:
                                temp_list_7 = []                            
                            out_str_0 = self.forming_str_text_org(self.setting_new_org_tuple[0], 
                                                                  self.setting_new_org_tuple[1], 
                                                                  temp_str_1, 
                                                                  self.setting_new_org_str_1, 
                                                                  temp_list_5, 
                                                                  self.setting_new_org_str_1, 
                                                                  temp_list_6, 
                                                                  [temp_list_7])
                            if not out_str_0 is None:
                                temp_list_8 = [temp_list_4[1], temp_list_4[0]]
                                temp_list_9 = [temp_list_2[4], temp_list_2[5]]
                                temp_list_10 = [self.setting_new_org_tuple[0], self.setting_new_org_tuple[2], 
                                                self.setting_new_org_tuple[3], self.setting_new_org_str_1]
                                out_str_list_1 = self.forming_str_text_member_lang(temp_list_8, temp_list_1, 
                                                                                   temp_list_3, temp_list_9, 
                                                                                   temp_list_10, 
                                                                                   self.basic_parameter[1][2][1], 
                                                                                   self.basic_parameter[1][2][2], 
                                                                                   self.basic_parameter[1][2][3])
                                if not out_str_list_1 is None:  
                                    temp_bool_0 = True
                                    temp_file_list = os.scandir(self.basic_parameter[1][0])
                                    for e in temp_file_list:
                                        temp_str_0 = e.name
                                        if len(temp_str_0) > 4:
                                            temp_str_1 = temp_str_0[-4:].upper()
                                            if (temp_str_1 == ".CSV") | (temp_str_1 == ".TXT"):
                                                temp_bool_0 = False
                                            if temp_bool_0:
                                                if len(temp_str_0) > 5:
                                                    temp_str_1 = temp_str_0[-5:].upper()
                                                    if temp_str_1 == ".IDEN":
                                                        temp_bool_0 = False
                                        if not temp_bool_0:
                                            break
                                    if temp_bool_0:
                                        for n in range(len(self.basic_parameter[1][1])):
                                            temp_file_list = os.scandir(self.basic_parameter[1][1][n])
                                            for e in temp_file_list:
                                                temp_str_0 = e.name
                                                if len(temp_str_0) > 4:
                                                    temp_str_1 = temp_str_0[-4:].upper()
                                                    if (temp_str_1 == ".CSV") | (temp_str_1 == ".TXT"):
                                                        temp_bool_0 = False
                                                    if temp_bool_0:
                                                        if len(temp_str_0) > 5:
                                                            temp_str_1 = temp_str_0[-5:].upper()
                                                            if temp_str_1 == ".IDEN":
                                                                temp_bool_0 = False
                                                if not temp_bool_0:
                                                    break
                                            if not temp_bool_0:
                                                break
                                    if temp_bool_0:
                                        temp_str_1 = "Mem_"
                                        temp_str_1 = temp_str_1+temp_list_2[4][0]
                                        temp_str_1 = temp_str_1+temp_list_2[4][1]
                                        temp_str_1 = temp_str_1+temp_list_2[4][2]
                                        temp_str_1 = temp_str_1+temp_list_2[4][3]
                                        temp_str_1 = temp_str_1+temp_list_2[4][5]
                                        temp_str_1 = temp_str_1+temp_list_2[4][6]
                                        temp_str_1 = temp_str_1+temp_list_2[4][8]
                                        temp_str_1 = temp_str_1+temp_list_2[4][9]
                                        temp_str_1 = temp_str_1+temp_list_2[5][0]
                                        temp_str_1 = temp_str_1+temp_list_2[5][1]
                                        temp_str_1 = temp_str_1+temp_list_2[5][3]
                                        temp_str_1 = temp_str_1+temp_list_2[5][4]
                                        temp_str_1 = temp_str_1+"_"
                                        temp_str_1 = temp_str_1+temp_list_1[0]
                                        temp_str_1 = temp_str_1+"_"
                                        temp_str_1 = temp_str_1+temp_list_1[1]
                                        temp_str_1 = temp_str_1+"_"
                                        temp_str_1 = temp_str_1+temp_list_1[2]
                                        temp_str_1 = temp_str_1+"_"
                                        temp_str_1 = temp_str_1+temp_list_4[0]
                                        temp_str_1_0 = temp_str_1+".iden"
                                        temp_str_1_0 = self.basic_parameter[1][1][0]+"/"+temp_str_1_0
                                        with open(temp_str_1_0, "w", encoding = "utf-8") as save_file:
                                            save_file.write(out_str_list_1[0])
                                            save_file.close()
                                        temp_str_2 = "The file with path '"+temp_str_1_0+"' is output."
                                        if self.basic_parameter[1][2][1]:
                                            temp_str_1_0 = temp_str_1+"_English.txt"
                                            temp_str_1_0 = self.basic_parameter[1][1][1]+"/"+temp_str_1_0
                                            temp_str_2 = temp_str_2+"\n"
                                            temp_str_2 = temp_str_2+"The file with path '"+temp_str_1_0+"' is output."
                                            with open(temp_str_1_0, "w", encoding = "utf-8") as save_file:
                                                save_file.write(out_str_list_1[1])
                                                save_file.close()
                                        if self.basic_parameter[1][2][2]:
                                            temp_str_1_0 = temp_str_1+"_简体中文.txt"
                                            temp_str_1_0 = self.basic_parameter[1][1][2]+"/"+temp_str_1_0
                                            temp_str_2 = temp_str_2+"\n"
                                            temp_str_2 = temp_str_2+"The file with path '"+temp_str_1_0+"' is output."
                                            with open(temp_str_1_0, "w", encoding = "utf-8") as save_file:
                                                save_file.write(out_str_list_1[2])
                                                save_file.close()
                                        if self.basic_parameter[1][2][3]:
                                            temp_str_1_0 = temp_str_1+"_正體中文.txt"
                                            temp_str_1_0 = self.basic_parameter[1][1][3]+"/"+temp_str_1_0
                                            temp_str_2 = temp_str_2+"\n"
                                            temp_str_2 = temp_str_2+"The file with path '"+temp_str_1_0+"' is output."
                                            with open(temp_str_1_0, "w", encoding = "utf-8") as save_file:
                                                save_file.write(out_str_list_1[3])
                                                save_file.close()
                                        showinfo(title = "output *.iden (and *txt) file", 
                                                 message = temp_str_2) 
                                        temp_str_2 = "Org_"
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][0]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][1]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][2]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][3]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][5]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][6]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][8]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][9]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[3][0]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[3][1]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[3][3]
                                        temp_str_2 = temp_str_2+self.setting_new_org_tuple[3][4]
                                        temp_str_2 = temp_str_2+"_"
                                        temp_str_2 = temp_str_2+self.setting_new_org_str_0
                                        temp_str_2 = temp_str_2+".dat"
                                        temp_str_2 = self.basic_parameter[2][0]+"/"+temp_str_2
                                        with open(temp_str_2, "w", encoding = "utf-8") as save_file:
                                            save_file.write(out_str_0)
                                            save_file.close()
                                            showinfo(title = "output *.dat File", 
                                                     message = "The file with path '"+temp_str_2+"' is output.\nThe manipulation number of the administrator is '"+self.setting_new_org_str_1+"'.")
                                        self.setting_gene_org_frame_0.grid(row = 1, column = 0,
                                                                           padx = 5, pady = 5, 
                                                                           sticky = tk.NW)
                                        self.setting_gene_org_frame_1.grid_forget()            
                                        self.setting_new_org_name_entry.delete(0, "end")   
                                        self.setting_new_org_init_0_entry.delete(0, "end")   
                                        self.setting_new_org_init_1_entry.delete(0, "end")   
                                        self.setting_new_org_init_2_entry.delete(0, "end")
                                    else:
                                        showerror(title = "Error", 
                                                  message = "There exists other *.iden or *.txt, *.csv in '"+self.basic_parameter[1][0]+"/', or its sub-folders.")
                                else:
                                    showerror(title = "Error", 
                                              message = "Error in forming files.")
                            else:
                                showerror(title = "Error", 
                                          message = "Error in forming files.")
                        else:
                            showerror(title = "Error", 
                                      message = "Another name / virtual is in wrong format.")
                    else:
                        showerror(title = "Error", 
                                  message = "Another name / virtual is in wrong format.")
                else:
                    showerror(title = "Error", 
                              message = "The English name is in wrong format.")
            else:
                showerror(title = "Error", 
                          message = "The English name is in wrong format.")
        elif temp_str_0 == "exist":
            temp_str_0 = self.setting_gene_org_frame_1_exist_admin_radio_vari.get()
            if temp_str_0 == "en":
                temp_list_0 = [self.setting_gene_org_exist_gn_entry_vari.get().strip(), 
                               self.setting_gene_org_exist_mn_entry_vari.get().strip(), 
                               self.setting_gene_org_exist_fn_entry_vari.get().strip()]
                temp_list_0 = self.English_name_change_quotation_mark(temp_list_0)
            elif temp_str_0 == "vn":
                temp_list_0 = [self.setting_gene_org_exist_vt_combo_vari.get().strip(), 
                               self.setting_gene_org_exist_vn_entry_vari.get().strip(), 
                               self.setting_gene_org_exist_va_entry_vari.get().strip()]
                temp_list_0 = self.virtual_name_change_quotation_mark(temp_list_0)
            temp_str_1 = self.setting_gene_org_exist_org_num_entry_vari.get().strip()
            temp_list_1 = [self.setting_gene_org_exist_org_date_year_spinbox_vari.get().strip(), 
                           self.setting_gene_org_exist_org_date_month_spinbox_vari.get().strip(), 
                           self.setting_gene_org_exist_org_date_day_spinbox_vari.get().strip()]
            temp_list_2 = [self.setting_gene_org_exist_org_time_hour_spinbox_vari.get().strip(), 
                           self.setting_gene_org_exist_org_time_minute_spinbox_vari.get().strip()]
            numeric_digits = ("0", "1", "2", "3", "4", 
                              "5", "6", "7", "8", "9")
            temp_bool_0 =True
            temp_num_0 = len(temp_list_1[0])
            if (temp_num_0 > 0) & (temp_num_0 <= 4):
                for n in range(temp_num_0):
                    if not temp_list_1[0][n] in numeric_digits:
                        temp_bool_0 = False
                        break
            if temp_bool_0:
                temp_num_1 = int(temp_list_1[0])
                temp_num_0 = len(temp_list_1[1])
                if (temp_num_0 > 0) & (temp_num_0 <= 2):
                    for n in range(temp_num_0):
                        if not temp_list_1[1][n] in numeric_digits:
                            temp_bool_0 = False
                            break
            if temp_bool_0:
                temp_num_2 = int(temp_list_1[1])
                temp_num_0 = len(temp_list_1[2])
                if (temp_num_0 > 0) & (temp_num_0 <= 2):
                    for n in range(temp_num_0):
                        if not temp_list_1[2][n] in numeric_digits:
                            temp_bool_0 = False
                            break
            if temp_bool_0:
                temp_num_3 = int(temp_list_1[2])
                temp_num_0 = len(temp_list_2[0])
                if (temp_num_0 > 0) & (temp_num_0 <= 2):
                    for n in range(temp_num_0):
                        if not temp_list_2[0][n] in numeric_digits:
                            temp_bool_0 = False
                            break
            if temp_bool_0:
                temp_num_4 = int(temp_list_2[0])
                temp_num_0 = len(temp_list_2[1])
                if (temp_num_0 > 0) & (temp_num_0 <= 2):
                    for n in range(temp_num_0):
                        if not temp_list_2[1][n] in numeric_digits:
                            temp_bool_0 = False
                            break
            if temp_bool_0:
                if len(temp_str_1) == 14:
                    if temp_str_1[0].upper() != self.setting_new_org_init_list[0]:
                        temp_bool_0 = False
                    elif temp_str_1[1].upper() != self.setting_new_org_init_list[1]:
                        temp_bool_0 = False
                    elif temp_str_1[2].upper() != self.setting_new_org_init_list[2]:
                        temp_bool_0 = False
                else:
                    temp_bool_0 = False
            if temp_bool_0:
                temp_num_5 = int(temp_list_2[1])
                if self.num_organization_valid(temp_str_1, 
                                               temp_num_1, temp_num_2, temp_num_3, 
                                               temp_num_4, temp_num_5):
                    temp_str_2 = self.setting_gene_org_exist_mem_num_entry_vari.get().strip()    
                    if temp_str_0 == "en":
                        if not temp_list_0 is None:
                            temp_bool_0 = self.num_member_valid(temp_str_2, 
                                                                organization_number = temp_str_1)
                        else:
                            temp_bool_0 = False
                            showerror(title = "Error", 
                                      message = "The English name is in wrong format.")
                    elif temp_str_0 == "vn":
                        if not temp_list_0 is None:
                            temp_bool_0 = self.num_member_valid(temp_str_2, 
                                                                virtual_name = temp_list_0[1], 
                                                                organization_number = temp_str_1)
                        else:
                            temp_bool_0 = False
                            showerror(title = "Error", 
                                      message = "Another name / virtual name is in wrong format.")
                    else:
                        temp_bool_0 = False
                        showerror(title = "Error", 
                                  message = "Error in forming files.")
                    if temp_bool_0:
                        temp_str_3 = self.setting_new_org_init_list[0]+self.setting_new_org_init_list[1]+self.setting_new_org_init_list[2]
                        temp_list_5 = [self.setting_new_org_str_1, self.setting_new_org_tuple[2], self.setting_new_org_tuple[3]]
                        temp_list_6 = ["", self.regions_vec[-1]]
                        temp_str_4 = ""
                        if temp_num_1 < 10:
                            temp_str_4 = temp_str_4+"000"+str(temp_num_1)
                        elif temp_num_1 < 100:
                            temp_str_4 = temp_str_4+"00"+str(temp_num_1)
                        elif temp_num_1 < 1000:
                            temp_str_4 = temp_str_4+"0"+str(temp_num_1)
                        elif temp_num_1 < 10000:
                            temp_str_4 = temp_str_4+str(temp_num_1)
                        temp_str_4 = temp_str_4+"-"                        
                        if temp_num_2 < 10:
                            temp_str_4 = temp_str_4+"0"+str(temp_num_2)
                        elif temp_num_2 < 100:
                            temp_str_4 = temp_str_4+str(temp_num_2)
                        temp_str_4 = temp_str_4+"-"                        
                        if temp_num_3 < 10:
                            temp_str_4 = temp_str_4+"0"+str(temp_num_3)
                        elif temp_num_3 < 100:
                            temp_str_4 = temp_str_4+str(temp_num_3)
                        temp_str_5 = ""     
                        if temp_num_4 < 10:
                            temp_str_5 = temp_str_5+"0"+str(temp_num_4)
                        elif temp_num_4 < 100:
                            temp_str_5 = temp_str_5+str(temp_num_4)
                        temp_str_5 = temp_str_5+":"                        
                        if temp_num_5 < 10:
                            temp_str_5 = temp_str_5+"0"+str(temp_num_5)
                        elif temp_num_3 < 100:
                            temp_str_5 = temp_str_5+str(temp_num_5)
                        temp_list_7 = [self.setting_new_org_str_1, True, temp_str_2, 
                                       temp_str_0, temp_list_0[0], temp_list_0[1], temp_list_0[2], 
                                       temp_str_1, temp_str_4, temp_str_5]                      
                        out_str_0 = self.forming_str_text_org(self.setting_new_org_tuple[0], 
                                                              self.setting_new_org_tuple[1], 
                                                              temp_str_3, 
                                                              self.setting_new_org_str_1, 
                                                              temp_list_5, 
                                                              self.setting_new_org_str_1, 
                                                              temp_list_6, 
                                                              [temp_list_7])
                        if not out_str_0 is None:
                            temp_str_2 = "Org_"
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][0]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][1]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][2]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][3]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][5]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][6]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][8]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[2][9]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[3][0]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[3][1]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[3][3]
                            temp_str_2 = temp_str_2+self.setting_new_org_tuple[3][4]
                            temp_str_2 = temp_str_2+"_"
                            temp_str_2 = temp_str_2+self.setting_new_org_str_0
                            temp_str_2 = temp_str_2+".dat"
                            temp_str_2 = self.basic_parameter[2][0]+"/"+temp_str_2
                            with open(temp_str_2, "w", encoding = "utf-8") as save_file:
                                save_file.write(out_str_0)
                                save_file.close()
                                showinfo(title = "output *.dat File", 
                                         message = "The file with path '"+temp_str_2+"' is output.\nThe manipulation number of the administrator is '"+self.setting_new_org_str_1+"'.")
                            self.setting_gene_org_frame_0.grid(row = 1, column = 0,
                                                               padx = 5, pady = 5, 
                                                               sticky = tk.NW)
                            self.setting_gene_org_frame_1.grid_forget()            
                            self.setting_new_org_name_entry.delete(0, "end")   
                            self.setting_new_org_init_0_entry.delete(0, "end")   
                            self.setting_new_org_init_1_entry.delete(0, "end")   
                            self.setting_new_org_init_2_entry.delete(0, "end")
                        else:
                            showerror(title = "Error", 
                                      message = "Error in forming files.")                        
                    else:
                        temp_bool_0 = False
                else:
                    showerror(title = "Error", 
                              message = "The issuer's information is in wrong format.")
            else:
                showerror(title = "Error", 
                          message = "The issuer's information is in wrong format.")
    
    def setting_fun_read_direct(self):
        self.setting_direct_new_member_vari = self.basic_parameter[1][0]
        self.setting_direct_new_member["text"] = self.setting_direct_new_member_vari+"/"
        if self.basic_parameter[1][2][1]:
            self.setting_direct_new_member_en_check.select()
        else:
            self.setting_direct_new_member_en_check.deselect()
        if self.basic_parameter[1][2][2]:
            self.setting_direct_new_member_zhs_check.select()
        else:
            self.setting_direct_new_member_zhs_check.deselect()
        if self.basic_parameter[1][2][3]:
            self.setting_direct_new_member_zht_check.select()
        else:
            self.setting_direct_new_member_zht_check.deselect()
        self.setting_direct_output_conf_vari = self.basic_parameter[2][0]
        self.setting_direct_output_conf["text"] = self.setting_direct_output_conf_vari+"/"
        self.setting_direct_output_csv_vari = self.basic_parameter[3][0]
        self.setting_direct_output_csv["text"] = self.setting_direct_output_csv_vari+"/"
        self.setting_direct_database_vari = self.basic_parameter[4][0]
        self.setting_direct_database["text"] = self.setting_direct_database_vari+"/"
    
    def setting_fun_change_direct(self, in_str):
        if in_str == "new_member":
            path = askdirectory(initialdir = self.basic_parameter[1][0])
        elif in_str == "output_conf":
            path = askdirectory(initialdir = self.basic_parameter[2][0])
        elif in_str == "output_csv":
            path = askdirectory(initialdir = self.basic_parameter[3][0])
        elif in_str == "database":
            path = askdirectory(initialdir = self.basic_parameter[4][0])
        if path:
            path = str(path)
            if in_str == "new_member":
                self.setting_direct_new_member_vari = path
                self.setting_direct_new_member["text"] = self.setting_direct_new_member_vari+"/"
            elif in_str == "output_conf":
                self.setting_direct_output_conf_vari = path
                self.setting_direct_output_conf["text"] = self.setting_direct_output_conf_vari+"/"
            elif in_str == "output_csv":
                self.setting_direct_output_csv_vari = path
                self.setting_direct_output_csv["text"] = self.setting_direct_output_csv_vari+"/"
            elif in_str == "database":
                self.setting_direct_database_vari = path
                self.setting_direct_database["text"] = self.setting_direct_database_vari+"/"
    
    def setting_fun_confirm_direct(self):
        temp_bool_0 = True
        if not os.path.exists(self.setting_direct_new_member_vari):
            temp_bool_0 = False
        elif not os.path.exists(self.setting_direct_output_conf_vari):
            temp_bool_0 = False
        elif not os.path.exists(self.setting_direct_output_csv_vari):
            temp_bool_0 = False
        elif not os.path.exists(self.setting_direct_database_vari):
            temp_bool_0 = False
        if temp_bool_0:
            temp_list_0 = [self.basic_parameter[0]]
            temp_str_0 = self.basic_parameter[0]
            temp_str_1 = self.setting_direct_new_member_vari
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_str_0 = temp_str_0+temp_str_1
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_list_1 = [temp_str_1]
            temp_list_1.append([temp_str_1+"/iden", 
                                temp_str_1+"/English", 
                                temp_str_1+"/简体中文", 
                                temp_str_1+"/正體中文"])
            temp_bool_1 = self.setting_direct_new_member_en_check_vari.get()
            temp_bool_2 = self.setting_direct_new_member_zhs_check_vari.get()
            temp_bool_3 = self.setting_direct_new_member_zht_check_vari.get()
            temp_list_1.append([True, 
                                temp_bool_1, 
                                temp_bool_2, 
                                temp_bool_3])
            if temp_bool_1:
                temp_str_0 = temp_str_0+"1"
            else:
                temp_str_0 = temp_str_0+"0"
            temp_str_0 = temp_str_0+self.dat_file_sub_sep
            if temp_bool_2:
                temp_str_0 = temp_str_0+"1"
            else:
                temp_str_0 = temp_str_0+"0"
            temp_str_0 = temp_str_0+self.dat_file_sub_sep
            if temp_bool_3:
                temp_str_0 = temp_str_0+"1"
            else:
                temp_str_0 = temp_str_0+"0"
            if not os.path.exists(temp_list_1[0]):
                os.mkdir(temp_list_1[0])
            if not os.path.exists(temp_list_1[1][0]):
                os.mkdir(temp_list_1[1][0])
            if not os.path.exists(temp_list_1[1][1]):
                os.mkdir(temp_list_1[1][1])
            if not os.path.exists(temp_list_1[1][2]):
                os.mkdir(temp_list_1[1][2])
            if not os.path.exists(temp_list_1[1][3]):
                os.mkdir(temp_list_1[1][3])
            temp_list_0.append(temp_list_1)
            temp_str_1 = self.setting_direct_output_conf_vari         
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_str_0 = temp_str_0+temp_str_1
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_list_1 = [temp_str_1]
            temp_list_0.append(temp_list_1) 
            if not os.path.exists(temp_list_1[0]):
                os.mkdir(temp_list_1[0])
            temp_str_1 = self.setting_direct_output_csv_vari           
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_str_0 = temp_str_0+temp_str_1
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_list_1 = [temp_str_1]
            temp_list_1.append([temp_str_1+"/Slot-1", 
                                temp_str_1+"/Slot-2", 
                                temp_str_1+"/Slot-3", 
                                temp_str_1+"/Slot-4", 
                                temp_str_1+"/Slot-5", 
                                temp_str_1+"/Slot-6", 
                                temp_str_1+"/Slot-7", 
                                temp_str_1+"/Slot-8"])
            temp_list_0.append(temp_list_1)  
            if not os.path.exists(temp_list_1[0]):
                os.mkdir(temp_list_1[0])
            if not os.path.exists(temp_list_1[1][0]):
                os.mkdir(temp_list_1[1][0])
            if not os.path.exists(temp_list_1[1][1]):
                os.mkdir(temp_list_1[1][1])
            if not os.path.exists(temp_list_1[1][2]):
                os.mkdir(temp_list_1[1][2])
            if not os.path.exists(temp_list_1[1][3]):
                os.mkdir(temp_list_1[1][3])  
            if not os.path.exists(temp_list_1[1][4]):
                os.mkdir(temp_list_1[1][4])
            if not os.path.exists(temp_list_1[1][5]):
                os.mkdir(temp_list_1[1][5])
            if not os.path.exists(temp_list_1[1][6]):
                os.mkdir(temp_list_1[1][6])       
            if not os.path.exists(temp_list_1[1][7]):
                os.mkdir(temp_list_1[1][7])              
            temp_str_1 = self.setting_direct_database_vari           
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_str_0 = temp_str_0+temp_str_1
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_list_1 = [temp_str_1]
            temp_list_1.append([temp_str_1+"/Slot-1", 
                                temp_str_1+"/Slot-2", 
                                temp_str_1+"/Slot-3", 
                                temp_str_1+"/Slot-4", 
                                temp_str_1+"/Slot-5", 
                                temp_str_1+"/Slot-6", 
                                temp_str_1+"/Slot-7", 
                                temp_str_1+"/Slot-8"])
            temp_list_0.append(temp_list_1)   
            if not os.path.exists(temp_list_1[0]):
                os.mkdir(temp_list_1[0])
            if not os.path.exists(temp_list_1[1][0]):
                os.mkdir(temp_list_1[1][0])
            if not os.path.exists(temp_list_1[1][1]):
                os.mkdir(temp_list_1[1][1])
            if not os.path.exists(temp_list_1[1][2]):
                os.mkdir(temp_list_1[1][2])
            if not os.path.exists(temp_list_1[1][3]):
                os.mkdir(temp_list_1[1][3])  
            if not os.path.exists(temp_list_1[1][4]):
                os.mkdir(temp_list_1[1][4])
            if not os.path.exists(temp_list_1[1][5]):
                os.mkdir(temp_list_1[1][5])
            if not os.path.exists(temp_list_1[1][6]):
                os.mkdir(temp_list_1[1][6]) 
            if not os.path.exists(temp_list_1[1][7]):
                os.mkdir(temp_list_1[1][7])     
            self.basic_parameter = temp_list_0
            with open("assets/NumGene.dat", "w", encoding = "utf-8") as save_file:
                save_file.write(temp_str_0)
                save_file.close()
                showinfo(title = "Directories saved", 
                         message = "The change of directoried has been saved.") 
        else:
            showerror(title = "Error", 
                      message = "Fail to change the configuration of the directories.")  
    
    def setting_fun_my_org_switch_page(self):
        if not self.cur_org is None:
            temp_str = self.setting_my_org_page_radio_vari.get()
            if temp_str == "info":
                self.setting_my_org_basic_info_frame.grid(row = 1, column = 0,
                                                          padx = 2, pady = 2,
                                                          sticky = tk.W) 
                self.setting_my_org_mani_list_frame.grid_forget()
                self.setting_my_org_org_num_vari = self.cur_org[0][0]
                self.setting_my_org_org_num["text"] = self.setting_my_org_org_num_vari
                self.setting_my_org_org_num_initial_0["text"] = self.cur_org[0][3][0]
                self.setting_my_org_org_num_initial_1["text"] = self.cur_org[0][3][1]
                self.setting_my_org_org_num_initial_2["text"] = self.cur_org[0][3][2]
                self.setting_my_org_admin_num_vari = self.cur_org[0][4]
                self.setting_my_org_admin_num["text"] = self.setting_my_org_admin_num_vari
                self.setting_my_org_org_name_vari = self.cur_org[0][2]
                self.setting_my_org_org_name["text"] = self.setting_my_org_org_name_vari
                self.setting_my_org_org_name.grid(row = 0, column = 1,
                                                  sticky = tk.W) 
                self.setting_my_org_org_name_entry.grid_forget()
                self.setting_my_org_org_name_edit_button.grid(row = 0, column = 2,
                                                              sticky = tk.W)
                self.setting_my_org_org_name_copy_button.grid(row = 0, column = 3,
                                                              sticky = tk.W) 
                self.setting_my_org_org_name_cancel_button.grid_forget()
                self.setting_my_org_org_name_confirm_button.grid_forget()
                self.setting_my_org_city_vari = self.cur_org[0][7][0]
                self.setting_my_org_city["text"] = self.setting_my_org_city_vari
                self.setting_my_org_city.grid(row = 0, column = 1,
                                              sticky = tk.W) 
                self.setting_my_org_city_entry.grid_forget()
                self.setting_my_org_city_edit_button.grid(row = 0, column = 2,
                                                          sticky = tk.W) 
                self.setting_my_org_city_copy_button.grid(row = 0, column = 3,
                                                          sticky = tk.W) 
                self.setting_my_org_city_cancel_button.grid_forget()
                self.setting_my_org_city_confirm_button.grid_forget()
                self.setting_my_org_region_vari = self.cur_org[0][7][1]
                self.setting_my_org_region_combo["state"] = "readonly"
                self.setting_my_org_region_combo.set(self.setting_my_org_region_vari)
                self.setting_my_org_region_combo["state"] = "disabled"
                self.setting_my_org_region_edit_button.grid(row = 0, column = 2,
                                                                    sticky = tk.W) 
                self.setting_my_org_region_cancel_button.grid_forget()
                self.setting_my_org_region_confirm_button.grid_forget()
                self.setting_my_org_generate_mani_num["text"] = self.cur_org[0][5][0]
                self.setting_my_org_generate_date["text"] = self.cur_org[0][5][1]
                self.setting_my_org_generate_time["text"] = self.cur_org[0][5][2]       
                self.setting_my_org_lastedit_mani_num["text"] = self.cur_org[0][6][0]
                self.setting_my_org_lastedit_date["text"] = self.cur_org[0][6][1]
                self.setting_my_org_lastedit_time["text"] = self.cur_org[0][6][2]
            elif temp_str == "mani":
                self.setting_my_org_basic_info_frame.grid_forget()
                self.setting_my_org_mani_list_frame.grid(row = 1, column = 0,
                                                         padx = 2, pady = 2,
                                                         sticky = tk.W) 
                self.setting_fun_my_org_scan_mani()
                for n in range(len(self.cur_org[1])):
                    self.setting_my_org_mani_list_listbox.select_clear(n)
                self.setting_my_org_mani_listbox_select["text"] = "Currently select: -"
                self.setting_my_org_mani_list_frame_line_0_Right.grid_forget()
                self.setting_my_org_mani_org_frame.grid_forget()
                self.setting_my_org_mani_cur_sel = -1
            else:
                self.setting_my_org_basic_info_frame.grid_forget()
                self.setting_my_org_mani_list_frame.grid_forget()
    
    def setting_fun_my_org_copy_org_num(self):
        if not self.cur_org is None:
            self.clipboard_clear()
            self.clipboard_append(self.setting_my_org_org_num_vari)
    
    def setting_fun_my_org_copy_admin_num(self):
        if not self.cur_org is None:
            self.clipboard_clear()
            self.clipboard_append(self.setting_my_org_admin_num_vari)
    
    def setting_fun_my_org_admin_change(self):
        if not self.cur_org is None:
            temp_num = -1
            for n in range(len(self.cur_org[2])):
                if self.cur_mani_num == self.cur_org[2][n]:
                    temp_num = n
                    break
            if temp_num >= 0:
                if self.cur_org[3][temp_num]:
                    temp_str = "Are you sure that you want to change the administrator from '"
                    temp_str = temp_str+self.setting_my_org_admin_num_vari
                    temp_str = temp_str+"' to '"
                    temp_str = temp_str+self.cur_mani_num
                    temp_str = temp_str+"'?"
                    answer = askyesno(title="Change administrator",
                                      message=temp_str)
                    if answer:  
                        self.setting_my_org_admin_num_vari = self.cur_mani_num
                        self.setting_my_org_admin_num["text"] = self.setting_my_org_admin_num_vari
                else:
                    showerror(title = "Error", 
                              message = "Your manipulation number is disabled.") 
            else:
                showerror(title = "Error", 
                          message = "Your manipulation number is not in the manipulation list.") 
                
    
    def setting_fun_my_org_copy_org_name(self):
        if not self.cur_org is None:
            self.clipboard_clear()
            self.clipboard_append(self.setting_my_org_org_name_vari)
    
    def setting_fun_my_org_edit_org_name(self):
        if not self.cur_org is None:
            self.setting_my_org_org_name_entry.delete(0, "end")
            self.setting_my_org_org_name_entry.insert(0, self.setting_my_org_org_name_vari)
            self.setting_my_org_org_name.grid_forget()
            self.setting_my_org_org_name_entry.grid(row = 0, column = 1,
                                                    sticky = tk.W) 
            self.setting_my_org_org_name_edit_button.grid_forget()
            self.setting_my_org_org_name_copy_button.grid_forget()
            self.setting_my_org_org_name_cancel_button.grid(row = 0, column = 2,
                                                            sticky = tk.W)
            self.setting_my_org_org_name_confirm_button.grid(row = 0, column = 3,
                                                             sticky = tk.W)
    
    def setting_fun_my_org_cancel_org_name(self):
        if not self.cur_org is None:
            self.setting_my_org_org_name["text"] = self.setting_my_org_org_name_vari
            self.setting_my_org_org_name.grid(row = 0, column = 1,
                                              sticky = tk.W) 
            self.setting_my_org_org_name_entry.grid_forget()
            self.setting_my_org_org_name_edit_button.grid(row = 0, column = 2,
                                                          sticky = tk.W)
            self.setting_my_org_org_name_copy_button.grid(row = 0, column = 3,
                                                          sticky = tk.W)
            self.setting_my_org_org_name_cancel_button.grid_forget()
            self.setting_my_org_org_name_confirm_button.grid_forget()
    
    def setting_fun_my_org_escape_org_name(self, event):
        if not self.cur_org is None:
            self.setting_fun_my_org_cancel_org_name()
    
    def setting_fun_my_org_confirm_org_name(self):
        if not self.cur_org is None:
            temp_str = self.setting_my_org_org_name_entry_vari.get().strip()
            temp_len = len(temp_str)
            temp_bool = True
            if temp_len < 1:
                temp_bool = False
            if temp_len == 1:
                temp_str_0 = temp_str[0]
                if (not temp_str_0 in self.English_name_capital) & (not temp_str_0 in self.numeric_digits):
                    temp_bool = False
            elif temp_len <= self.org_name_max_len:
                temp_str_0 = temp_str[0]
                if (temp_str_0 in self.English_name_capital) | (temp_str_0 in self.numeric_digits):
                    for n in range(1, temp_len):
                        temp_str_0 = temp_str[n].upper()
                        if ((not temp_str_0 in self.English_name_capital) & 
                            (not temp_str_0 in self.numeric_digits) & 
                            (not temp_str_0 in self.English_name_other_1)):
                            temp_bool = False
                            break
                else:
                    temp_bool = False
            else:
                temp_bool = False
            if temp_bool:
                self.cur_org[0][2] = temp_str
                self.setting_my_org_org_name_vari = self.cur_org[0][2]
                self.setting_my_org_org_name["text"] = self.setting_my_org_org_name_vari
                self.setting_my_org_org_name.grid(row = 0, column = 1,
                                                  sticky = tk.W) 
                self.setting_my_org_org_name_entry.grid_forget()
                self.setting_my_org_org_name_edit_button.grid(row = 0, column = 2,
                                                              sticky = tk.W)
                self.setting_my_org_org_name_copy_button.grid(row = 0, column = 3,
                                                              sticky = tk.W)
                self.setting_my_org_org_name_cancel_button.grid_forget()
                self.setting_my_org_org_name_confirm_button.grid_forget()
            else:
                temp_str = "(1) The initial character must be from 26 English capital letters and number 0-9."
                temp_str = temp_str+"\n\n"
                temp_str = temp_str+"(2) The other characters are from: "
                temp_str = temp_str+"(i) 26 English capital letters, "
                temp_str = temp_str+"(ii) 26 English small letters, "
                temp_str = temp_str+"(iii) number 0-9, "
                temp_str = temp_str+"(iv) space \" \", "
                temp_str = temp_str+"(v) hypen \"-\", "
                temp_str = temp_str+"(vi) and \"&\", "
                temp_str = temp_str+"(vii) or \"/\", "
                temp_str = temp_str+"(iix) single quotation mark \"'\" and \"‘\" and \"’\", "
                temp_str = temp_str+"(ix) dot \".\", "
                temp_str = temp_str+"(x) colon \":\", "
                temp_str = temp_str+"(xi) parenthesis \"(\" and \")\"."
                temp_str = temp_str+"\n\n"
                temp_str = temp_str+"(3) The max length is "+str(self.org_name_max_len)+"."
                showerror(title = "Error", 
                          message = temp_str) 
    
    def setting_fun_my_org_return_org_name(self, event):
        if not self.cur_org is None:
            self.setting_fun_my_org_confirm_org_name()
    
    def setting_fun_my_org_copy_city(self):
        if not self.cur_org is None:
            self.clipboard_clear()
            self.clipboard_append(self.setting_my_org_city_vari)
    
    def setting_fun_my_org_edit_city(self):
        if not self.cur_org is None:
            self.setting_my_org_city_entry.delete(0, "end")
            self.setting_my_org_city_entry.insert(0, self.setting_my_org_city_vari)
            self.setting_my_org_city.grid_forget()
            self.setting_my_org_city_entry.grid(row = 0, column = 1,
                                                sticky = tk.W) 
            self.setting_my_org_city_edit_button.grid_forget()
            self.setting_my_org_city_copy_button.grid_forget()
            self.setting_my_org_city_cancel_button.grid(row = 0, column = 2,
                                                        sticky = tk.W)
            self.setting_my_org_city_confirm_button.grid(row = 0, column = 3,
                                                         sticky = tk.W)
    
    def setting_fun_my_org_cancel_city(self):
        if not self.cur_org is None:
            self.setting_my_org_city["text"] = self.setting_my_org_city_vari
            self.setting_my_org_city.grid(row = 0, column = 1,
                                              sticky = tk.W) 
            self.setting_my_org_city_entry.grid_forget()
            self.setting_my_org_city_edit_button.grid(row = 0, column = 2,
                                                      sticky = tk.W)
            self.setting_my_org_city_copy_button.grid(row = 0, column = 3,
                                                      sticky = tk.W)
            self.setting_my_org_city_cancel_button.grid_forget()
            self.setting_my_org_city_confirm_button.grid_forget()
    
    def setting_fun_my_org_escape_city(self, event):
        if not self.cur_org is None:
            self.setting_fun_my_org_cancel_city()
    
    def setting_fun_my_org_confirm_city(self):
        if not self.cur_org is None:
            temp_str = self.setting_my_org_city_entry_vari.get().strip()
            temp_len = len(temp_str)
            temp_bool = True
            if temp_len == 1:
                temp_str_0 = temp_str[0]
                if (not temp_str_0 in self.English_name_capital) & (not temp_str_0 in self.numeric_digits):
                    temp_bool = False
            elif temp_len > 1:
                temp_str_0 = temp_str[0]
                if (temp_str_0 in self.English_name_capital) | (temp_str_0 in self.numeric_digits):
                    for n in range(1, temp_len):
                        temp_str_0 = temp_str[n].upper()
                        if ((not temp_str_0 in self.English_name_capital) & 
                            (not temp_str_0 in self.numeric_digits) & 
                            (not temp_str_0 in self.English_name_other_1)):
                            temp_bool = False
                            break
                else:
                    temp_bool = False
            if temp_bool:
                self.cur_org[0][7][0] = temp_str
                self.setting_my_org_city_vari = self.cur_org[0][7][0]
                self.setting_my_org_city["text"] = self.setting_my_org_city_vari
                self.setting_my_org_city.grid(row = 0, column = 1,
                                              sticky = tk.W) 
                self.setting_my_org_city_entry.grid_forget()
                self.setting_my_org_city_edit_button.grid(row = 0, column = 2,
                                                          sticky = tk.W)
                self.setting_my_org_city_copy_button.grid(row = 0, column = 3,
                                                          sticky = tk.W)
                self.setting_my_org_city_cancel_button.grid_forget()
                self.setting_my_org_city_confirm_button.grid_forget()
            else:
                temp_str = "(1) The initial character must be from 26 English capital letters and number 0-9."
                temp_str = temp_str+"\n\n"
                temp_str = temp_str+"(2) The other characters are from: "
                temp_str = temp_str+"(i) 26 English capital letters, "
                temp_str = temp_str+"(ii) 26 English small letters, "
                temp_str = temp_str+"(iii) number 0-9, "
                temp_str = temp_str+"(iv) space \" \", "
                temp_str = temp_str+"(v) hypen \"-\", "
                temp_str = temp_str+"(vi) and \"&\", "
                temp_str = temp_str+"(vii) or \"/\", "
                temp_str = temp_str+"(iix) single quotation mark \"'\" and \"‘\" and \"’\", "
                temp_str = temp_str+"(ix) dot \".\", "
                temp_str = temp_str+"(x) colon \":\", "
                temp_str = temp_str+"(xi) parenthesis \"(\" and \")\"."
                temp_str = temp_str+"\n\n"
                temp_str = temp_str+"(3) There is no limitations of the length, even it can be 0."
                showerror(title = "Error", 
                          message = temp_str) 
    
    def setting_fun_my_org_return_city(self, event):
        if not self.cur_org is None:
            self.setting_fun_my_org_confirm_city()
    
    def setting_fun_my_org_edit_region(self):
        if not self.cur_org is None:
            self.setting_my_org_region_combo["state"] = "readonly"
            self.setting_my_org_region_edit_button.grid_forget()
            self.setting_my_org_region_cancel_button.grid(row = 0, column = 2,
                                                          sticky = tk.W)
            self.setting_my_org_region_confirm_button.grid(row = 0, column = 3,
                                                           sticky = tk.W)
    
    def setting_fun_my_org_cancel_region(self):
        if not self.cur_org is None:
            self.setting_my_org_region_combo["state"] = "readonly"
            self.setting_my_org_region_combo.set(self.setting_my_org_region_vari)
            self.setting_my_org_region_combo["state"] = "disabled"
            self.setting_my_org_region_edit_button.grid(row = 0, column = 2,
                                                          sticky = tk.W)
            self.setting_my_org_region_cancel_button.grid_forget()
            self.setting_my_org_region_confirm_button.grid_forget()
    
    def setting_fun_my_org_confirm_region(self):
        if not self.cur_org is None:
            temp_str = self.setting_my_org_region_combo_vari.get().strip()
            if temp_str in self.regions_vec:    
                self.cur_org[0][7][1] = temp_str
                self.setting_my_org_region_vari = self.cur_org[0][7][1]
                self.setting_my_org_region_combo["state"] = "readonly"
                self.setting_my_org_region_combo.set(self.setting_my_org_region_vari)
                self.setting_my_org_region_combo["state"] = "disabled"
                self.setting_my_org_region_edit_button.grid(row = 0, column = 2,
                                                              sticky = tk.W)
                self.setting_my_org_region_cancel_button.grid_forget()
                self.setting_my_org_region_confirm_button.grid_forget()
    
    def setting_fun_my_org_scan_mani(self):
        if not self.cur_org is None:
            temp_len = len(self.cur_org[1])
            temp_name_list = []
            for n in range(temp_len):
                temp_tuple = self.cur_org[1][n]
                if not temp_tuple is None:
                    temp_str = ""
                    temp_str = str(n+1)+"/"+str(temp_len)+" - "
                    if temp_tuple[1]:
                        temp_str = temp_str+"enabled"
                    else:
                        temp_str = temp_str+"disabled"
                    temp_str = temp_str+" - "
                    temp_str = temp_str+temp_tuple[0]
                    temp_str = temp_str+" - "
                    if temp_tuple[3] == "en":
                        temp_str = temp_str+temp_tuple[4]
                        temp_str = temp_str+" "
                        temp_str = temp_str+temp_tuple[6]
                    elif temp_tuple[3] == "vn":
                        temp_str = temp_str+temp_tuple[5]
                else:
                    temp_str = ""
                    temp_str = str(n+1)+"/"+str(temp_len)+" - <empty>"
                temp_name_list.append(temp_str)
            self.setting_my_org_mani_list_listbox_vari = tk.StringVar(value = temp_name_list)
            self.setting_my_org_mani_list_listbox["listvariable"] = self.setting_my_org_mani_list_listbox_vari
    
    def setting_fun_my_org_listbox_select(self, event):
        if not self.cur_org is None:
            temp_tuple_0 = self.setting_my_org_mani_list_listbox.curselection()
            if len(temp_tuple_0) > 0:
                if self.setting_my_org_mani_cur_sel != temp_tuple_0[0]:                
                    self.setting_my_org_mani_cur_sel = temp_tuple_0[0]
                    temp_tuple_1 = self.cur_org[1][self.setting_my_org_mani_cur_sel]
                    temp_str_0 = "Currently select: "
                    temp_str_0 = temp_str_0+str(self.setting_my_org_mani_cur_sel+1)
                    temp_str_0 = temp_str_0+"/"
                    temp_str_0 = temp_str_0+str(len(self.cur_org[1]))
                    self.setting_my_org_mani_listbox_select["text"] = temp_str_0
                    if not temp_tuple_1 is None:
                        self.setting_my_org_mani_list_frame_line_0_Right.grid(row = 0, column = 1,
                                                                              sticky = tk.W)
                        self.setting_my_org_mani_new_frame.grid_forget()
                        self.setting_my_org_mani_old_frame.grid(row = 1, column = 0,
                                                                sticky = tk.W)
                        self.setting_my_org_mani_name_frame.grid(row = 2, column = 0,
                                                                 padx = 2, pady = 2,
                                                                 sticky = tk.W)
                        self.setting_my_org_mani_org_frame.grid(row = 2, column = 0,
                                                                padx = 2, pady = 2,
                                                                sticky = tk.W)
                        self.setting_my_org_mani_old_num_vari = temp_tuple_1[0]
                        self.setting_my_org_mani_old_num["text"] = self.setting_my_org_mani_old_num_vari
                        if  temp_tuple_1[1]:
                            self.setting_my_org_mani_old_check.select()
                        else:
                            self.setting_my_org_mani_old_check.deselect()
                        self.setting_my_org_mani_mem_num_entry.delete(0, "end")
                        self.setting_my_org_mani_mem_num_entry.insert(0, temp_tuple_1[2])
                        if temp_tuple_1[3] == "en":
                            self.setting_my_org_mani_name_en_radio.select()
                            self.setting_my_org_mani_name_en_frame.grid(row = 2, column = 0,
                                                                        sticky = tk.W)
                            self.setting_my_org_mani_name_gn_entry.delete(0, "end")
                            self.setting_my_org_mani_name_gn_entry.insert(0, temp_tuple_1[4])
                            self.setting_my_org_mani_name_mn_entry.delete(0, "end")
                            self.setting_my_org_mani_name_mn_entry.insert(0, temp_tuple_1[5])
                            self.setting_my_org_mani_name_fn_entry.delete(0, "end")
                            self.setting_my_org_mani_name_fn_entry.insert(0, temp_tuple_1[6])
                            self.setting_my_org_mani_name_vn_frame.grid_forget()
                            self.setting_my_org_mani_name_vt_combo.set("Other")
                            self.setting_my_org_mani_name_vn_entry.delete(0, "end")
                            self.setting_my_org_mani_name_va_entry.delete(0, "end")
                        elif temp_tuple_1[3] == "vn":
                            self.setting_my_org_mani_name_vn_radio.select()
                            self.setting_my_org_mani_name_en_frame.grid_forget()
                            self.setting_my_org_mani_name_gn_entry.delete(0, "end")
                            self.setting_my_org_mani_name_mn_entry.delete(0, "end")
                            self.setting_my_org_mani_name_fn_entry.delete(0, "end")
                            self.setting_my_org_mani_name_vn_frame.grid(row = 2, column = 0,
                                                                        sticky = tk.W)
                            self.setting_my_org_mani_name_vt_combo.set(temp_tuple_1[4])
                            self.setting_my_org_mani_name_vn_entry.delete(0, "end")
                            self.setting_my_org_mani_name_vn_entry.insert(0, temp_tuple_1[5])
                            self.setting_my_org_mani_name_va_entry.delete(0, "end")
                            self.setting_my_org_mani_name_va_entry.insert(0, temp_tuple_1[6])
                        self.setting_my_org_mani_org_num_entry.delete(0, "end")
                        self.setting_my_org_mani_org_num_entry.insert(0, temp_tuple_1[7])
                        self.setting_my_org_mani_org_date_year_spinbox.delete(0, "end")
                        temp_str_0 = str(int(str(temp_tuple_1[8][0:4])))
                        self.setting_my_org_mani_org_date_year_spinbox.insert(0, temp_str_0)
                        self.setting_my_org_mani_org_date_month_spinbox.delete(0, "end")
                        temp_str_0 = str(int(str(temp_tuple_1[8][5:7])))
                        self.setting_my_org_mani_org_date_month_spinbox.insert(0, temp_str_0)                        
                        self.setting_my_org_mani_org_date_day_spinbox.delete(0, "end")
                        temp_str_0 = str(int(str(temp_tuple_1[8][8:10])))
                        self.setting_my_org_mani_org_date_day_spinbox.insert(0, temp_str_0)                        
                        self.setting_my_org_mani_org_time_hour_spinbox.delete(0, "end")
                        temp_str_0 = str(int(str(temp_tuple_1[9][0:2])))
                        self.setting_my_org_mani_org_time_hour_spinbox.insert(0, temp_str_0)                        
                        self.setting_my_org_mani_org_time_minute_spinbox.delete(0, "end")
                        temp_str_0 = str(int(str(temp_tuple_1[9][3:5])))
                        self.setting_my_org_mani_org_time_minute_spinbox.insert(0, temp_str_0)                        
                    else:
                        self.setting_my_org_mani_list_frame_line_0_Right.grid(row = 0, column = 1,
                                                                              sticky = tk.W)
                        self.setting_my_org_mani_new_frame.grid(row = 1, column = 0,
                                                                sticky = tk.W)
                        self.setting_my_org_mani_new_entry.delete(0, "end")
                        self.setting_my_org_mani_old_frame.grid_forget()
                        self.setting_my_org_mani_name_frame.grid_forget()
                        self.setting_my_org_mani_org_frame.grid_forget()
                        
    def setting_fun_my_org_listbox_add(self):
        if not self.cur_org is None:
            self.cur_org[1].append(None)
            self.cur_org[2].append("")
            self.cur_org[3].append(False)
            self.setting_fun_my_org_scan_mani()
            if self.setting_my_org_mani_cur_sel >= 0:
                temp_str_0 = "Currently select: "
                temp_str_0 = temp_str_0+str(self.setting_my_org_mani_cur_sel+1)
                temp_str_0 = temp_str_0+"/"
                temp_str_0 = temp_str_0+str(len(self.cur_org[1]))
                self.setting_my_org_mani_listbox_select["text"] = temp_str_0
        
    def setting_fun_my_org_listbox_up(self):
        if not self.cur_org is None:
            if (self.setting_my_org_mani_cur_sel > 0) & (self.setting_my_org_mani_cur_sel < len(self.cur_org[1])):
                temp_tuple = self.cur_org[1][self.setting_my_org_mani_cur_sel]
                self.cur_org[1][self.setting_my_org_mani_cur_sel] = self.cur_org[1][self.setting_my_org_mani_cur_sel-1]
                self.cur_org[1][self.setting_my_org_mani_cur_sel-1] = temp_tuple
                temp_str = self.cur_org[2][self.setting_my_org_mani_cur_sel]
                self.cur_org[2][self.setting_my_org_mani_cur_sel] = self.cur_org[2][self.setting_my_org_mani_cur_sel-1]
                self.cur_org[2][self.setting_my_org_mani_cur_sel-1] = temp_str
                temp_bool = self.cur_org[3][self.setting_my_org_mani_cur_sel]
                self.cur_org[3][self.setting_my_org_mani_cur_sel] = self.cur_org[3][self.setting_my_org_mani_cur_sel-1]
                self.cur_org[3][self.setting_my_org_mani_cur_sel-1] = temp_bool
                self.setting_fun_my_org_scan_mani()
                self.setting_my_org_mani_list_listbox.select_clear(self.setting_my_org_mani_cur_sel)
                self.setting_my_org_mani_cur_sel -= 1
                self.setting_my_org_mani_list_listbox.select_set(self.setting_my_org_mani_cur_sel)
                self.setting_my_org_mani_list_listbox.activate(self.setting_my_org_mani_cur_sel)
                temp_str_0 = "Currently select: "
                temp_str_0 = temp_str_0+str(self.setting_my_org_mani_cur_sel+1)
                temp_str_0 = temp_str_0+"/"
                temp_str_0 = temp_str_0+str(len(self.cur_org[1]))
                self.setting_my_org_mani_listbox_select["text"] = temp_str_0
    
    def setting_fun_my_org_listbox_down(self):
        if not self.cur_org is None:
            if (self.setting_my_org_mani_cur_sel >= 0) & (self.setting_my_org_mani_cur_sel < len(self.cur_org[1])-1):
                temp_tuple = self.cur_org[1][self.setting_my_org_mani_cur_sel]
                self.cur_org[1][self.setting_my_org_mani_cur_sel] = self.cur_org[1][self.setting_my_org_mani_cur_sel+1]
                self.cur_org[1][self.setting_my_org_mani_cur_sel+1] = temp_tuple
                temp_str = self.cur_org[2][self.setting_my_org_mani_cur_sel]
                self.cur_org[2][self.setting_my_org_mani_cur_sel] = self.cur_org[2][self.setting_my_org_mani_cur_sel+1]
                self.cur_org[2][self.setting_my_org_mani_cur_sel+1] = temp_str
                temp_bool = self.cur_org[3][self.setting_my_org_mani_cur_sel]
                self.cur_org[3][self.setting_my_org_mani_cur_sel] = self.cur_org[3][self.setting_my_org_mani_cur_sel+1]
                self.cur_org[3][self.setting_my_org_mani_cur_sel+1] = temp_bool
                self.setting_fun_my_org_scan_mani()
                self.setting_my_org_mani_list_listbox.select_clear(self.setting_my_org_mani_cur_sel)
                self.setting_my_org_mani_cur_sel += 1
                self.setting_my_org_mani_list_listbox.select_set(self.setting_my_org_mani_cur_sel)
                self.setting_my_org_mani_list_listbox.activate(self.setting_my_org_mani_cur_sel)
                temp_str_0 = "Currently select: "
                temp_str_0 = temp_str_0+str(self.setting_my_org_mani_cur_sel+1)
                temp_str_0 = temp_str_0+"/"
                temp_str_0 = temp_str_0+str(len(self.cur_org[1]))
                self.setting_my_org_mani_listbox_select["text"] = temp_str_0        
    
    def setting_fun_my_org_listbox_remove(self):
        if not self.cur_org is None:
            if self.setting_my_org_mani_cur_sel >= 0:
                temp_tuple = self.cur_org[1][self.setting_my_org_mani_cur_sel]
                temp_bool = True
                if not temp_tuple is None:
                    if temp_tuple[0] == self.cur_org[0][4]:
                        temp_bool = False
                        showerror(title = "Error", 
                                  message = "The administrator cannot be removed.")
                    elif temp_tuple[0] == self.cur_org[0][5][0]:
                        temp_bool = False
                        showerror(title = "Error", 
                                  message = "The founder cannot be removed.")
                    elif temp_tuple[0] == self.cur_org[0][6][0]:
                        temp_bool = False
                        showerror(title = "Error", 
                                  message = "The last editor cannot be removed.")
                if temp_bool:
                    answer = askyesno(title="Remove",
                                      message="Are you sure that you want to remove item "+str(1+self.setting_my_org_mani_cur_sel)+"?")
                    if answer:  
                        self.setting_my_org_mani_list_listbox.select_clear(self.setting_my_org_mani_cur_sel)
                        del(self.cur_org[1][self.setting_my_org_mani_cur_sel])
                        del(self.cur_org[2][self.setting_my_org_mani_cur_sel])
                        del(self.cur_org[3][self.setting_my_org_mani_cur_sel])
                        self.setting_fun_my_org_scan_mani()
                        self.setting_my_org_mani_cur_sel = -1
                        self.setting_my_org_mani_listbox_select["text"] = "Currently select: -"       
                        self.setting_my_org_mani_list_frame_line_0_Right.grid_forget()
                        self.setting_my_org_mani_org_frame.grid_forget()
    
    def setting_fun_my_org_new_mani_gene(self):
        if not self.cur_org is None:
            if self.setting_my_org_mani_cur_sel >= 0:
                if len(self.cur_org[1]) < 777:
                    temp_bool = True
                    while temp_bool:
                        temp_str = self.number_manipulation_generate(self.cur_org[0][0])
                        if not temp_str in self.cur_org[2]:
                            temp_bool = False
                    self.setting_my_org_mani_new_entry.delete(0, "end")
                    self.setting_my_org_mani_new_entry.insert(0, temp_str)
                else:
                    showerror(title = "Error", 
                              message = "There are 777 manipulation numbers, which reaches the limitation.")
    
    def setting_fun_my_org_new_mani_confirm(self):
        if not self.cur_org is None:
            if self.setting_my_org_mani_cur_sel >= 0:
                temp_str = self.setting_my_org_mani_new_entry_vari.get().strip()
                temp_str = temp_str.upper()
                if self.number_manipulation_valid(temp_str, self.cur_org[0][0]):
                    if not temp_str in self.cur_org[2]:
                        self.setting_my_org_mani_old_num_vari = temp_str
                        self.setting_my_org_mani_old_num["text"] = self.setting_my_org_mani_old_num_vari
                        self.setting_my_org_mani_old_check.deselect()
                        self.setting_my_org_mani_old_frame.grid(row = 1, column = 0,
                                                                sticky = tk.W)
                        self.setting_my_org_mani_mem_num_entry.delete(0, "end")
                        self.setting_my_org_mani_name_frame.grid(row = 2, column = 0,
                                                                 padx = 2, pady = 2,
                                                                 sticky = tk.W)
                        self.setting_my_org_mani_name_en_radio.select()
                        self.setting_my_org_mani_name_en_frame.grid(row = 2, column = 0,
                                                                    sticky = tk.W)
                        self.setting_my_org_mani_name_gn_entry.delete(0, "end")
                        self.setting_my_org_mani_name_mn_entry.delete(0, "end")
                        self.setting_my_org_mani_name_fn_entry.delete(0, "end")
                        self.setting_my_org_mani_name_vn_frame.grid_forget()
                        self.setting_my_org_mani_name_vt_combo.set("Other")
                        self.setting_my_org_mani_name_vn_entry.delete(0, "end")
                        self.setting_my_org_mani_name_va_entry.delete(0, "end")
                        self.setting_my_org_mani_org_frame.grid(row = 2, column = 0,
                                                                padx = 2, pady = 2,
                                                                sticky = tk.W)
                        self.setting_my_org_mani_org_num_entry.delete(0, "end")
                        self.setting_my_org_mani_org_date_year_spinbox.delete(0, "end")
                        self.setting_my_org_mani_org_date_year_spinbox.insert(0, "2020")
                        self.setting_my_org_mani_org_date_month_spinbox.delete(0, "end")
                        self.setting_my_org_mani_org_date_month_spinbox.insert(0, "1")
                        self.setting_my_org_mani_org_date_day_spinbox.delete(0, "end")
                        self.setting_my_org_mani_org_date_day_spinbox.insert(0, "1")
                        self.setting_my_org_mani_org_time_hour_spinbox.delete(0, "end")
                        self.setting_my_org_mani_org_time_hour_spinbox.insert(0, "0")
                        self.setting_my_org_mani_org_time_minute_spinbox.delete(0, "end")
                        self.setting_my_org_mani_org_time_minute_spinbox.insert(0, "0")
                    else:
                        showerror(title = "Error", 
                                  message = "The manipulation number is duplicate.")
                else:
                    showerror(title = "Error", 
                              message = "The manipulation number is invalid.")
        
    def setting_fun_my_org_copy_mani(self):
        if not self.cur_org is None:
            if self.setting_my_org_mani_cur_sel >= 0:
                self.clipboard_clear()
                self.clipboard_append(self.setting_my_org_mani_old_num_vari)
    
    def setting_fun_my_org_mani_name_switch(self):
        if not self.cur_org is None:
            if self.setting_my_org_mani_cur_sel >= 0:
                temp_str_0 = self.setting_my_org_mani_name_radio_vari.get()
                if temp_str_0 == "en":
                    self.setting_my_org_mani_name_en_frame.grid(row = 2, column = 0,
                                                                sticky = tk.W)
                    self.setting_my_org_mani_name_vn_frame.grid_forget()
                elif temp_str_0 == "vn":
                    self.setting_my_org_mani_name_en_frame.grid_forget()
                    self.setting_my_org_mani_name_vn_frame.grid(row = 2, column = 0,
                                                                sticky = tk.W)
    
    def setting_fun_my_org_mani_confirm(self):
        if not self.cur_org is None:
            if self.setting_my_org_mani_cur_sel >= 0:
                temp_list_0 = []
                temp_str_0 = self.setting_my_org_mani_old_num_vari.strip().upper()
                temp_bool = True
                if self.number_manipulation_valid(temp_str_0, self.cur_org[0][0]):
                    temp_list_0.append(temp_str_0)
                    temp_list_0.append(self.setting_my_org_mani_old_check_vari.get())
                    temp_str_0 = self.setting_my_org_mani_name_radio_vari.get()
                    if temp_str_0 == "en":
                        temp_list_1 = [self.setting_my_org_mani_name_gn_entry_vari.get().strip(), 
                                       self.setting_my_org_mani_name_mn_entry_vari.get().strip(), 
                                       self.setting_my_org_mani_name_fn_entry_vari.get().strip()]
                        temp_list_1 = self.English_name_change_quotation_mark(temp_list_1)
                        if not temp_list_1 is None:
                            if len(temp_list_1[0]) > 0:
                                temp_str_1 = self.setting_my_org_mani_mem_num_entry_vari.get().strip()
                                temp_str_1 = temp_str_1.upper()
                                temp_str_2 = self.setting_my_org_mani_org_num_entry_vari.get().strip()
                                if self.num_member_valid(temp_str_1, 
                                                         organization_number = temp_str_2):
                                    if ((temp_str_2[0].upper() == self.cur_org[0][3][0]) & 
                                        (temp_str_2[1].upper() == self.cur_org[0][3][1]) & 
                                        (temp_str_2[2].upper() == self.cur_org[0][3][2])):
                                        temp_list_0.append(temp_str_1)
                                        temp_list_0.append(temp_str_0)
                                        temp_list_0.extend(temp_list_1)
                                        temp_list_0.append(temp_str_2)
                                    else:
                                        temp_bool = False 
                                else:
                                    temp_bool = False 
                            else:
                                temp_bool = False 
                        else:
                            temp_bool = False 
                    elif temp_str_0 == "vn":
                        temp_list_1 = [self.setting_my_org_mani_name_vt_combo_vari.get().strip(), 
                                       self.setting_my_org_mani_name_vn_entry_vari.get().strip(), 
                                       self.setting_my_org_mani_name_va_entry_vari.get().strip()]
                        temp_list_1 = self.virtual_name_change_quotation_mark(temp_list_1)
                        if not temp_list_1 is None:
                            if len(temp_list_1[1]) > 0:
                                temp_str_1 = self.setting_my_org_mani_mem_num_entry_vari.get().strip()
                                temp_str_1 = temp_str_1.upper()
                                temp_str_2 = self.setting_my_org_mani_org_num_entry_vari.get().strip()
                                if self.num_member_valid(temp_str_1, 
                                                         virtual_name = temp_list_1[1], 
                                                         organization_number = temp_str_2):
                                    if ((temp_str_2[0].upper() == self.cur_org[0][3][0]) & 
                                        (temp_str_2[1].upper() == self.cur_org[0][3][1]) & 
                                        (temp_str_2[2].upper() == self.cur_org[0][3][2])):
                                        temp_list_0.append(temp_str_1)
                                        temp_list_0.append(temp_str_0)
                                        temp_list_0.extend(temp_list_1)
                                        temp_list_0.append(temp_str_2)
                                    else:
                                        temp_bool = False 
                                else:
                                    temp_bool = False 
                            else:
                                temp_bool = False 
                        else:
                            temp_bool = False 
                    else:
                        temp_bool = False 
                else:
                    temp_bool = False
                if temp_bool:
                    temp_str_1 = self.setting_my_org_mani_org_date_year_spinbox_vari.get().strip()
                    temp_num_1 = len(temp_str_1)
                    if (temp_num_1 > 0) & (temp_num_1 <= 4):
                        for n in range(temp_num_1):
                            if not temp_str_1[n] in self.numeric_digits:
                                temp_bool = False
                                break
                    if temp_bool:
                        temp_num_1 = int(temp_str_1)
                        temp_str_2 = self.setting_my_org_mani_org_date_month_spinbox_vari.get().strip()
                        temp_num_2 = len(temp_str_2)
                        if (temp_num_2 > 0) & (temp_num_2 <= 2):
                            for n in range(temp_num_2):
                                if not temp_str_2[n] in self.numeric_digits:
                                    temp_bool = False
                                    break
                        if temp_bool:
                            temp_num_2 = int(temp_str_2)
                            temp_str_3 = self.setting_my_org_mani_org_date_day_spinbox_vari.get().strip()
                            temp_num_3 = len(temp_str_3)
                            if (temp_num_3 > 0) & (temp_num_3 <= 2):
                                for n in range(temp_num_3):
                                    if not temp_str_3[n] in self.numeric_digits:
                                        temp_bool = False
                                        break
                            if temp_bool:
                                temp_num_3 = int(temp_str_3)
                                temp_str_4 = self.setting_my_org_mani_org_time_hour_spinbox_vari.get().strip()
                                temp_num_4 = len(temp_str_4)
                                if (temp_num_4 > 0) & (temp_num_4 <= 2):
                                    for n in range(temp_num_4):
                                        if not temp_str_4[n] in self.numeric_digits:
                                            temp_bool = False
                                            break
                                if temp_bool:
                                    temp_num_4 = int(temp_str_4)
                                    temp_str_5 = self.setting_my_org_mani_org_time_minute_spinbox_vari.get().strip()
                                    temp_num_5 = len(temp_str_5)
                                    if (temp_num_5 > 0) & (temp_num_5 <= 2):
                                        for n in range(temp_num_5):
                                            if not temp_str_5[n] in self.numeric_digits:
                                                temp_bool = False
                                                break
                                    if temp_bool:
                                        temp_num_5 = int(temp_str_5)
                    if temp_bool:
                        if self.num_organization_valid(temp_list_0[-1],  
                                                       temp_num_1, temp_num_2, temp_num_3, 
                                                       temp_num_4, temp_num_5):
                            temp_str_0 = ""
                            if temp_num_1 < 10:
                                temp_str_0 = temp_str_0+"000"+str(temp_num_1)
                            elif temp_num_1 < 100:
                                temp_str_0 = temp_str_0+"00"+str(temp_num_1)
                            elif temp_num_1 < 1000:
                                temp_str_0 = temp_str_0+"0"+str(temp_num_1)
                            else:
                                temp_str_0 = temp_str_0+str(temp_num_1)
                            temp_str_0 = temp_str_0+"-"
                            if temp_num_2 < 10:
                                temp_str_0 = temp_str_0+"0"+str(temp_num_2)
                            else:
                                temp_str_0 = temp_str_0+str(temp_num_2)
                            temp_str_0 = temp_str_0+"-"
                            if temp_num_3 < 10:
                                temp_str_0 = temp_str_0+"0"+str(temp_num_3)
                            else:
                                temp_str_0 = temp_str_0+str(temp_num_3)
                            temp_list_0.append(temp_str_0)
                            temp_str_0 = ""
                            if temp_num_4 < 10:
                                temp_str_0 = temp_str_0+"0"+str(temp_num_4)
                            else:
                                temp_str_0 = temp_str_0+str(temp_num_4)
                            temp_str_0 = temp_str_0+":"
                            if temp_num_5 < 10:
                                temp_str_0 = temp_str_0+"0"+str(temp_num_5)
                            else:
                                temp_str_0 = temp_str_0+str(temp_num_5)
                            temp_list_0.append(temp_str_0)
                        else:
                            temp_bool = False
                if temp_bool:
                    self.cur_org[1][self.setting_my_org_mani_cur_sel] = tuple(temp_list_0)
                    self.cur_org[2][self.setting_my_org_mani_cur_sel] = temp_list_0[0]
                    self.cur_org[3][self.setting_my_org_mani_cur_sel] = temp_list_0[1]
                    self.setting_fun_my_org_scan_mani()
                    for n in range(len(self.cur_org[1])):
                        self.setting_my_org_mani_list_listbox.select_clear(n)
                    temp_str = str(self.setting_my_org_mani_cur_sel+1)
                    temp_str = temp_str+"/"
                    temp_str = temp_str+str(len(self.cur_org[1]))
                    self.setting_my_org_mani_listbox_select["text"] = temp_str+" is modified."
                    self.setting_my_org_mani_list_frame_line_0_Right.grid_forget()
                    self.setting_my_org_mani_org_frame.grid_forget()
                    self.setting_my_org_mani_cur_sel = -1
                else:
                    showerror(title = "Error", 
                              message = "The content is in wrong format.")
    
    def setting_fun_my_org_output(self):
        if not self.cur_org is None:
            temp_str_1 = self.cur_org[0][3][0]+self.cur_org[0][3][1]+self.cur_org[0][3][2]
            out_str_0 = self.forming_str_text_org(self.cur_org[0][0], self.cur_org[0][2], temp_str_1, 
                                                  self.cur_org[0][4], self.cur_org[0][5], self.cur_mani_num, 
                                                  self.cur_org[0][7], self.cur_org[1])
            if not out_str_0 is None:
                temp_str_2 = "Org_"
                temp_str_2 = temp_str_2+self.cur_org[0][5][1][0]
                temp_str_2 = temp_str_2+self.cur_org[0][5][1][1]
                temp_str_2 = temp_str_2+self.cur_org[0][5][1][2]
                temp_str_2 = temp_str_2+self.cur_org[0][5][1][3]
                temp_str_2 = temp_str_2+self.cur_org[0][5][1][5]
                temp_str_2 = temp_str_2+self.cur_org[0][5][1][6]
                temp_str_2 = temp_str_2+self.cur_org[0][5][1][8]
                temp_str_2 = temp_str_2+self.cur_org[0][5][1][9]
                temp_str_2 = temp_str_2+self.cur_org[0][5][2][0]
                temp_str_2 = temp_str_2+self.cur_org[0][5][2][1]
                temp_str_2 = temp_str_2+self.cur_org[0][5][2][3]
                temp_str_2 = temp_str_2+self.cur_org[0][5][2][4]
                temp_str_2 = temp_str_2+"_"
                temp_str_2 = temp_str_2+self.cur_org[0][1]
                temp_str_2 = temp_str_2+".dat"
                temp_str_2 = self.basic_parameter[2][0]+"/"+temp_str_2
                with open(temp_str_2, "w", encoding = "utf-8") as save_file:
                    save_file.write(out_str_0)
                    save_file.close()
                    showinfo(title = "output *.dat File", 
                             message = "The file with path '"+temp_str_2+"' is output.\nThe manipulation number of the administrator is '"+self.cur_org[0][4]+"'.")
            else:
                showerror(title = "Error", 
                          message = "The content is in wrong format, and the file cannot output.")
    
    def setting_fun_org_list_read(self):
        if not self.basic_org_list is None:
            temp_bool = True
            if not self.basic_org_list[0] is None:
                self.cur_org_list = []
                temp_str_0 = self.basic_org_list[0][0].strip()
                temp_str_1 = self.basic_org_list[0][1].strip()
                temp_str_2 = self.basic_org_list[0][2].strip()
                temp_str_3 = self.basic_org_list[0][3].strip()
                temp_list_1 = []
            else:
                temp_bool = False
            if temp_bool:            
                if len(temp_str_1) == 10:
                    if len(temp_str_2) == 5:
                        if not temp_str_1[0] in self.numeric_digits:
                            temp_bool = False
                        elif not temp_str_1[1] in self.numeric_digits:
                            temp_bool = False
                        elif not temp_str_1[2] in self.numeric_digits:
                            temp_bool = False
                        elif not temp_str_1[3] in self.numeric_digits:
                            temp_bool = False
                        elif temp_str_1[4] != "-":
                            temp_bool = False
                        elif not temp_str_1[5] in self.numeric_digits:
                            temp_bool = False
                        elif not temp_str_1[6] in self.numeric_digits:
                            temp_bool = False
                        elif temp_str_1[7] != "-":
                            temp_bool = False
                        elif not temp_str_1[8] in self.numeric_digits:
                            temp_bool = False
                        elif not temp_str_1[9] in self.numeric_digits:
                            temp_bool = False
                        if temp_bool:
                            temp_num_0 = int(temp_str_1[0:4])
                            temp_num_1 = int(temp_str_1[5:7])
                            temp_num_2 = int(temp_str_1[8:10])
                            if not temp_str_2[0] in self.numeric_digits:
                                temp_bool = False
                            elif not temp_str_2[1] in self.numeric_digits:
                                temp_bool = False
                            elif temp_str_2[2] != ":":
                                temp_bool = False
                            elif not temp_str_2[3] in self.numeric_digits:
                                temp_bool = False
                            elif not temp_str_2[4] in self.numeric_digits:
                                temp_bool = False
                            if temp_bool:
                                temp_num_3 = int(temp_str_2[0:2])
                                temp_num_4 = int(temp_str_2[3:5])
                                temp_bool = self.number_manipulation_valid(temp_str_3, temp_str_0)
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
                if temp_bool:
                    self.setting_org_list_frame_line_1_mani_num["text"] = temp_str_3
                    self.setting_org_list_frame_line_1_org_num["text"] = temp_str_0
                    self.setting_org_list_frame_line_1_date["text"] = temp_str_1
                    self.setting_org_list_frame_line_1_time["text"] = temp_str_2
                    temp_str_9 = temp_str_0[0:3].upper()
                    for n in range(len(self.basic_org_list[1])):
                        temp_str_4 = self.basic_org_list[1][n][0].strip()
                        if not temp_str_4 in temp_list_1:
                            temp_list_1.append(temp_str_4)
                            temp_str_5 = self.basic_org_list[1][n][1].strip()
                            temp_str_6 = self.basic_org_list[1][n][2].strip()
                            temp_str_7 = self.basic_org_list[1][n][3].strip()
                            temp_str_8 = self.basic_org_list[1][n][4].strip()
                            temp_list_0 = []
                            if len(temp_str_6) == 10:
                                if len(temp_str_7) == 5:
                                    if not temp_str_6[0] in self.numeric_digits:
                                        temp_bool = False
                                    elif not temp_str_6[1] in self.numeric_digits:
                                        temp_bool = False
                                    elif not temp_str_6[2] in self.numeric_digits:
                                        temp_bool = False
                                    elif not temp_str_6[3] in self.numeric_digits:
                                        temp_bool = False
                                    elif temp_str_6[4] != "-":
                                        temp_bool = False
                                    elif not temp_str_6[5] in self.numeric_digits:
                                        temp_bool = False
                                    elif not temp_str_6[6] in self.numeric_digits:
                                        temp_bool = False
                                    elif temp_str_6[7] != "-":
                                        temp_bool = False
                                    elif not temp_str_6[8] in self.numeric_digits:
                                        temp_bool = False
                                    elif not temp_str_6[9] in self.numeric_digits:
                                        temp_bool = False
                                    if temp_bool:
                                        temp_num_5 = int(temp_str_6[0:4])
                                        temp_num_6 = int(temp_str_6[5:7])
                                        temp_num_7 = int(temp_str_6[8:10])
                                        if not temp_str_7[0] in self.numeric_digits:
                                            temp_bool = False
                                        elif not temp_str_7[1] in self.numeric_digits:
                                            temp_bool = False
                                        elif temp_str_7[2] != ":":
                                            temp_bool = False
                                        elif not temp_str_7[3] in self.numeric_digits:
                                            temp_bool = False
                                        elif not temp_str_7[4] in self.numeric_digits:
                                            temp_bool = False
                                        if temp_bool:
                                            temp_num_8 = int(temp_str_7[0:2])
                                            temp_num_9 = int(temp_str_7[3:5])
                                            if temp_num_5 > temp_num_0:
                                                temp_bool = False
                                            elif temp_num_5 == temp_num_0:
                                                if temp_num_6 > temp_num_1:
                                                    temp_bool = False
                                                elif temp_num_6 == temp_num_1:
                                                    if temp_num_7 > temp_num_2:
                                                        temp_bool = False
                                                    elif temp_num_7 == temp_num_2:
                                                        if temp_num_8 > temp_num_3:
                                                            temp_bool = False
                                                        elif temp_num_8 == temp_num_3:
                                                            if temp_num_9 > temp_num_4:
                                                                temp_bool = False
                                            if temp_bool:
                                                if self.number_manipulation_valid(temp_str_8, temp_str_4):
                                                    temp_bool = self.num_organization_valid(temp_str_4, 
                                                                                            temp_num_5, temp_num_6, temp_num_7, 
                                                                                            temp_num_8, temp_num_9)
                                                else:
                                                    temp_bool = False
                                    if temp_bool:
                                        if temp_str_4[0:3].upper() == temp_str_9:
                                            temp_len = len(temp_str_5)
                                            if temp_len < 1:
                                                temp_bool = False
                                            elif temp_len == 1:
                                                temp_str_10 = temp_str_5[0]
                                                if ((not temp_str_10 in self.English_name_capital) & 
                                                    (not temp_str_10 in self.numeric_digits)):
                                                    temp_bool = False
                                            elif temp_len <= self.org_name_max_len:
                                                temp_str_10 = temp_str_5[0]
                                                if ((not temp_str_10 in self.English_name_capital) & 
                                                    (not temp_str_10 in self.numeric_digits)):
                                                    temp_bool = False
                                                for n1 in range(1, temp_len):
                                                    temp_str_10 = temp_str_5[n1].upper()
                                                    if ((not temp_str_10 in self.English_name_capital) & 
                                                        (not temp_str_10 in self.numeric_digits) & 
                                                        (not temp_str_10 in self.English_name_other_1)):
                                                        temp_bool = False
                                                        break
                                            else:
                                                temp_bool = False
                                            if temp_bool:
                                                temp_list_0.append(temp_str_4)
                                                temp_list_0.append(temp_str_5)
                                                temp_list_0.append(temp_str_6)
                                                temp_list_0.append((temp_num_5, temp_num_6, temp_num_7))
                                                temp_list_0.append(temp_str_7)
                                                temp_list_0.append((temp_num_8, temp_num_9))  
                                                temp_list_0.append(temp_str_8)
                                        else:
                                            temp_bool = False
                                else:
                                    temp_bool = False
                            else:
                                temp_bool = False
                        else:
                            temp_bool = False
                        if temp_bool:
                            self.cur_org_list.append(tuple(temp_list_0))
                        else:
                            break
            if temp_bool:
                self.setting_org_list_frame_line_1.grid(row = 1, column = 0,
                                                        padx = 2, pady = 2, 
                                                        sticky = tk.W)
                self.setting_org_list_frame_line_1_not.grid_forget()
                self.setting_org_list_frame_line_1_broken.grid_forget()
            else:
                self.cur_org_list = []
                self.setting_org_list_frame_line_1.grid_forget()
                self.setting_org_list_frame_line_1_not.grid_forget()
                self.setting_org_list_frame_line_1_broken.grid(row = 1, column = 0,
                                                               padx = 2, pady = 2, 
                                                               sticky = tk.W)
        else:
            self.setting_org_list_frame_line_1.grid_forget()
            self.setting_org_list_frame_line_1_not.grid(row = 1, column = 0,
                                                        padx = 2, pady = 2, 
                                                        sticky = tk.W)
            self.setting_org_list_frame_line_1_broken.grid_forget()
            self.cur_org_list = []
        self.setting_fun_org_list_scan()
        self.setting_org_list_cur_sel = -1
        self.setting_org_list_listbox_select["text"] = "Currently select: -"
        self.setting_org_list_right_frame.grid_forget()        
    
    def setting_fun_org_list_scan(self):
        if not self.cur_org_list is None:
            temp_len = len(self.cur_org_list)
            temp_name_list = []
            for n in range(temp_len):
                temp_tuple = self.cur_org_list[n]
                if not temp_tuple is None:
                    temp_str = ""
                    temp_str = str(n+1)+"/"+str(temp_len)+" - " 
                    temp_str = temp_str+temp_tuple[0]
                    temp_str = temp_str+" - "
                    temp_str = temp_str+temp_tuple[1]
                else:
                    temp_str = ""
                    temp_str = str(n+1)+"/"+str(temp_len)+" - <empty>"
                temp_name_list.append(temp_str)
            self.setting_org_list_listbox_vari = tk.StringVar(value = temp_name_list)
            self.setting_org_list_listbox["listvariable"] = self.setting_org_list_listbox_vari
    
    def setting_fun_org_list_listbox_select(self, event):
        if not self.cur_org_list is None:
            temp_tuple_0 = self.setting_org_list_listbox.curselection()
            if len(temp_tuple_0) > 0:
                if self.setting_org_list_cur_sel != temp_tuple_0[0]:                
                    self.setting_org_list_cur_sel = temp_tuple_0[0]
                    temp_tuple_1 = self.cur_org_list[self.setting_org_list_cur_sel]
                    temp_str_0 = "Currently select: "
                    temp_str_0 = temp_str_0+str(self.setting_org_list_cur_sel+1)
                    temp_str_0 = temp_str_0+"/"
                    temp_str_0 = temp_str_0+str(len(self.cur_org_list))
                    self.setting_org_list_listbox_select["text"] = temp_str_0
                    self.setting_org_list_right_frame.grid(row = 0, column = 1,
                                                           padx = 5, pady = 5, 
                                                           sticky = tk.NW)
                    if not temp_tuple_1 is None:
                        self.setting_org_list_org_num_entry.delete(0, "end")
                        self.setting_org_list_org_num_entry.insert(0, temp_tuple_1[0])
                        self.setting_org_list_org_name_entry.delete(0, "end")
                        self.setting_org_list_org_name_entry.insert(0, temp_tuple_1[1])
                        self.setting_org_list_line_2_date_year_spinbox.delete(0, "end")
                        self.setting_org_list_line_2_date_year_spinbox.insert(0, str(temp_tuple_1[3][0]))
                        self.setting_org_list_line_2_date_month_spinbox.delete(0, "end")
                        self.setting_org_list_line_2_date_month_spinbox.insert(0, str(temp_tuple_1[3][1]))
                        self.setting_org_list_line_2_date_day_spinbox.delete(0, "end")
                        self.setting_org_list_line_2_date_day_spinbox.insert(0, str(temp_tuple_1[3][2]))
                        self.setting_org_list_line_2_time_hour_spinbox.delete(0, "end")
                        self.setting_org_list_line_2_time_hour_spinbox.insert(0, str(temp_tuple_1[5][0]))
                        self.setting_org_list_line_2_time_minute_spinbox.delete(0, "end")
                        self.setting_org_list_line_2_time_minute_spinbox.insert(0, str(temp_tuple_1[5][1]))   
                        self.setting_org_list_org_gene_num_entry.delete(0, "end")
                        self.setting_org_list_org_gene_num_entry.insert(0, temp_tuple_1[6])
                    else:
                        self.setting_org_list_org_num_entry.delete(0, "end")
                        self.setting_org_list_org_name_entry.delete(0, "end")
                        self.setting_org_list_line_2_date_year_spinbox.delete(0, "end")
                        self.setting_org_list_line_2_date_year_spinbox.insert(0, "2020")
                        self.setting_org_list_line_2_date_month_spinbox.delete(0, "end")
                        self.setting_org_list_line_2_date_month_spinbox.insert(0, "1")
                        self.setting_org_list_line_2_date_day_spinbox.delete(0, "end")
                        self.setting_org_list_line_2_date_day_spinbox.insert(0, "1")
                        self.setting_org_list_line_2_time_hour_spinbox.delete(0, "end")
                        self.setting_org_list_line_2_time_hour_spinbox.insert(0, "0")
                        self.setting_org_list_line_2_time_minute_spinbox.delete(0, "end")
                        self.setting_org_list_line_2_time_minute_spinbox.insert(0, "0")
                        self.setting_org_list_org_gene_num_entry.delete(0, "end")
    
    def setting_fun_org_list_listbox_add(self):
        if not self.cur_org_list is None:
            self.cur_org_list.append(None)
            self.setting_fun_org_list_scan()
            if self.setting_org_list_cur_sel >= 0:
                temp_str_0 = "Currently select: "
                temp_str_0 = temp_str_0+str(self.setting_org_list_cur_sel+1)
                temp_str_0 = temp_str_0+"/"
                temp_str_0 = temp_str_0+str(len(self.cur_org_list))
                self.setting_org_list_listbox_select["text"] = temp_str_0
    
    def setting_fun_org_list_listbox_up(self):
        if not self.cur_org_list is None:
            if (self.setting_org_list_cur_sel > 0) & (self.setting_org_list_cur_sel < len(self.cur_org_list)):
                temp_tuple = self.cur_org_list[self.setting_org_list_cur_sel]
                self.cur_org_list[self.setting_org_list_cur_sel] = self.cur_org_list[self.setting_org_list_cur_sel-1]
                self.cur_org_list[self.setting_org_list_cur_sel-1] = temp_tuple
                self.setting_fun_org_list_scan()
                self.setting_org_list_listbox.select_clear(self.setting_org_list_cur_sel)
                self.setting_org_list_cur_sel -= 1
                self.setting_org_list_listbox.select_set(self.setting_org_list_cur_sel)
                self.setting_org_list_listbox.activate(self.setting_org_list_cur_sel)
                temp_str_0 = "Currently select: "
                temp_str_0 = temp_str_0+str(self.setting_org_list_cur_sel+1)
                temp_str_0 = temp_str_0+"/"
                temp_str_0 = temp_str_0+str(len(self.cur_org_list))
                self.setting_org_list_listbox_select["text"] = temp_str_0
    
    def setting_fun_org_list_listbox_down(self):
        if not self.cur_org_list is None:
            if (self.setting_org_list_cur_sel >= 0) & (self.setting_org_list_cur_sel < len(self.cur_org_list)-1):
                temp_tuple = self.cur_org_list[self.setting_org_list_cur_sel]
                self.cur_org_list[self.setting_org_list_cur_sel] = self.cur_org_list[self.setting_org_list_cur_sel+1]
                self.cur_org_list[self.setting_org_list_cur_sel+1] = temp_tuple
                self.setting_fun_org_list_scan()
                self.setting_org_list_listbox.select_clear(self.setting_org_list_cur_sel)
                self.setting_org_list_cur_sel += 1
                self.setting_org_list_listbox.select_set(self.setting_org_list_cur_sel)
                self.setting_org_list_listbox.activate(self.setting_org_list_cur_sel)
                temp_str_0 = "Currently select: "
                temp_str_0 = temp_str_0+str(self.setting_org_list_cur_sel+1)
                temp_str_0 = temp_str_0+"/"
                temp_str_0 = temp_str_0+str(len(self.cur_org_list))
                self.setting_org_list_listbox_select["text"] = temp_str_0
    
    def setting_fun_org_list_listbox_remove(self):
        if not self.cur_org_list is None:
            if self.setting_org_list_cur_sel >= 0:              
                answer = askyesno(title="Remove",
                                  message="Are you sure that you want to remove item "+str(1+self.setting_org_list_cur_sel)+"?")
                if answer:  
                    self.setting_org_list_listbox.select_clear(self.setting_org_list_cur_sel)
                    del(self.cur_org_list[self.setting_org_list_cur_sel])
                    self.setting_fun_org_list_scan()
                    self.setting_org_list_cur_sel = -1
                    self.setting_org_list_listbox_select["text"] = "Currently select: -"       
                    self.setting_org_list_right_frame.grid_forget()
    
    def setting_fun_org_list_confirm(self):
        if not self.cur_org_list is None:
            if self.setting_org_list_cur_sel >= 0:
                temp_str_0 = self.setting_org_list_org_num_entry_vari.get().strip()
                temp_str_1 = self.setting_org_list_org_name_entry_vari.get().strip()
                temp_num_1 = len(temp_str_1)
                temp_str_2_0 = self.setting_org_list_line_2_date_year_spinbox_vari.get().strip()
                temp_num_2_0 = len(temp_str_2_0)
                temp_str_2_1 = self.setting_org_list_line_2_date_month_spinbox_vari.get().strip()
                temp_num_2_1 = len(temp_str_2_1)
                temp_str_2_2 = self.setting_org_list_line_2_date_day_spinbox_vari.get().strip()
                temp_num_2_2 = len(temp_str_2_2)
                temp_str_3_0 = self.setting_org_list_line_2_time_hour_spinbox_vari.get().strip()
                temp_num_3_0 = len(temp_str_3_0)
                temp_str_3_1 = self.setting_org_list_line_2_time_minute_spinbox_vari.get().strip()
                temp_num_3_1 = len(temp_str_3_1)
                temp_str_4 = self.setting_org_list_org_gene_num_entry_vari.get().strip()
                temp_bool = True
                if (temp_num_2_0 > 0) & (temp_num_2_0 <= 4):
                    for n in range(temp_num_2_0):
                        if not temp_str_2_0[n] in self.numeric_digits:
                            temp_bool = False
                            break
                    if temp_bool:
                        temp_num_2_0 = int(temp_str_2_0)
                else:
                    temp_bool = False
                if temp_bool:
                    if (temp_num_2_1 > 0) & (temp_num_2_1 <= 4):
                        for n in range(temp_num_2_1):
                            if not temp_str_2_1[n] in self.numeric_digits:
                                temp_bool = False
                                break
                        if temp_bool:
                            temp_num_2_1 = int(temp_str_2_1)
                    else:
                        temp_bool = False
                if temp_bool:
                    if (temp_num_2_2 > 0) & (temp_num_2_2 <= 4):
                        for n in range(temp_num_2_2):
                            if not temp_str_2_2[n] in self.numeric_digits:
                                temp_bool = False
                                break
                        if temp_bool:
                            temp_num_2_2 = int(temp_str_2_2)
                    else:
                        temp_bool = False
                if temp_bool:
                    if (temp_num_3_0 > 0) & (temp_num_3_0 <= 4):
                        for n in range(temp_num_3_0):
                            if not temp_str_3_0[n] in self.numeric_digits:
                                temp_bool = False
                                break
                        if temp_bool:
                            temp_num_3_0 = int(temp_str_3_0)
                    else:
                        temp_bool = False
                if temp_bool:
                    if (temp_num_3_1 > 0) & (temp_num_3_1 <= 4):
                        for n in range(temp_num_3_1):
                            if not temp_str_3_1[n] in self.numeric_digits:
                                temp_bool = False
                                break
                        if temp_bool:
                            temp_num_3_1 = int(temp_str_3_1)
                    else:
                        temp_bool = False
                if temp_bool:
                    if self.number_manipulation_valid(temp_str_4, temp_str_0):
                        temp_bool = self.num_organization_valid(temp_str_0, 
                                                                temp_num_2_0, temp_num_2_1, temp_num_2_2, 
                                                                temp_num_3_0, temp_num_3_1)
                    else:
                        temp_bool = False
                    if temp_bool:
                        if temp_num_1 < 1:
                            temp_bool = False
                        elif temp_num_1 == 1:
                            temp_str_5 = temp_str_1[0]
                            if ((not temp_str_5 in self.English_name_capital) & 
                                (not temp_str_5 in self.numeric_digits)):
                                temp_bool = False
                        elif temp_num_1 <= self.org_name_max_len:
                            temp_str_5 = temp_str_1[0]
                            if ((not temp_str_5 in self.English_name_capital) & 
                                (not temp_str_5 in self.numeric_digits)):
                                temp_bool = False
                            for n1 in range(1, temp_num_1):
                                temp_str_5 = temp_str_1[n1].upper()
                                if ((not temp_str_5 in self.English_name_capital) & 
                                    (not temp_str_5 in self.numeric_digits) & 
                                    (not temp_str_5 in self.English_name_other_1)):
                                    temp_bool = False
                                    break
                        else:
                            temp_bool = False
                if temp_bool:                    
                    temp_str_6 = ""
                    if temp_num_2_0 < 10:
                        temp_str_6 = temp_str_6+"000"+str(temp_num_2_0)
                    elif temp_num_2_0 < 100:
                        temp_str_6 = temp_str_6+"00"+str(temp_num_2_0)
                    elif temp_num_2_0 < 1000:
                        temp_str_6 = temp_str_6+"0"+str(temp_num_2_0)
                    else:
                        temp_str_6 = temp_str_6+str(temp_num_2_0)
                    temp_str_6 = temp_str_6+"-"
                    if temp_num_2_1 < 10:
                        temp_str_6 = temp_str_6+"0"+str(temp_num_2_1)
                    else:
                        temp_str_6 = temp_str_6+str(temp_num_2_1)
                    temp_str_6 = temp_str_6+"-"
                    if temp_num_2_2 < 10:
                        temp_str_6 = temp_str_6+"0"+str(temp_num_2_2)
                    else:
                        temp_str_6 = temp_str_6+str(temp_num_2_2)
                    temp_str_7 = ""
                    if temp_num_3_0 < 10:
                        temp_str_7 = temp_str_7+"0"+str(temp_num_3_0)
                    else:
                        temp_str_7 = temp_str_7+str(temp_num_3_0)
                    temp_str_7 = temp_str_7+":"
                    if temp_num_3_1 < 10:
                        temp_str_7 = temp_str_7+"0"+str(temp_num_3_1)
                    else:
                        temp_str_7 = temp_str_7+str(temp_num_3_1)                    
                    temp_list_0 = []
                    temp_list_0.append(temp_str_0)
                    temp_list_0.append(temp_str_1)
                    temp_list_0.append(temp_str_6)
                    temp_list_0.append((temp_num_2_0, temp_num_2_1, temp_num_2_2))
                    temp_list_0.append(temp_str_7)
                    temp_list_0.append((temp_num_3_0, temp_num_3_1))
                    temp_list_0.append(temp_str_4)
                    self.cur_org_list[self.setting_org_list_cur_sel] = tuple(temp_list_0)
                    self.setting_fun_org_list_scan()
                    temp_str = str(self.setting_org_list_cur_sel+1)
                    temp_str = temp_str+"/"
                    temp_str = temp_str+str(len(self.cur_org[1]))
                    self.setting_org_list_listbox_select["text"] = temp_str+" is modified."
                    self.setting_org_list_right_frame.grid_forget()  
                    self.setting_org_list_cur_sel = -1
                else:
                    showerror(title = "Error", 
                              message = "The content is in wrong format.") 
    
    def setting_fun_org_list_output(self):
        if not self.cur_org_list is None:
            temp_len = len(self.cur_org_list)
            if temp_len > 0:
                temp_bool = True
                temp_time_now = datetime.utcnow()
                temp_num_0 = temp_time_now.year
                temp_num_1 = temp_time_now.month
                temp_num_2 = temp_time_now.day
                temp_num_3 = temp_time_now.hour
                temp_num_4 = temp_time_now.minute
                out_str_0 = ""
                temp_str_0 = self.cur_mani_num.strip()
                temp_str_1 = self.cur_org[0][0].strip()
                if self.number_manipulation_valid(temp_str_0, temp_str_1):
                    out_str_0 = out_str_0+temp_str_1
                    temp_str_2 = ""
                    if temp_num_0 < 10:
                        temp_str_2 = temp_str_2+"000"+str(temp_num_0)
                    elif temp_num_0 < 100:
                        temp_str_2 = temp_str_2+"00"+str(temp_num_0)
                    elif temp_num_0 < 1000:
                        temp_str_2 = temp_str_2+"0"+str(temp_num_0)
                    else:
                        temp_str_2 = temp_str_2+str(temp_num_0)
                    temp_str_2 = temp_str_2+"-"
                    if temp_num_1 < 10:
                        temp_str_2 = temp_str_2+"0"+str(temp_num_1)
                    else:
                        temp_str_2 = temp_str_2+str(temp_num_1)
                    temp_str_2 = temp_str_2+"-"
                    if temp_num_2 < 10:
                        temp_str_2 = temp_str_2+"0"+str(temp_num_2)
                    else:
                        temp_str_2 = temp_str_2+str(temp_num_2)
                    temp_str_3 = ""
                    if temp_num_3 < 10:
                        temp_str_3 = temp_str_3+"0"+str(temp_num_3)
                    else:
                        temp_str_3 = temp_str_3+str(temp_num_3)
                    temp_str_3 = temp_str_3+":"
                    if temp_num_4 < 10:
                        temp_str_3 = temp_str_3+"0"+str(temp_num_4)
                    else:
                        temp_str_3 = temp_str_3+str(temp_num_4)
                    out_str_0 = out_str_0+self.dat_file_sub_sep
                    out_str_0 = out_str_0+temp_str_2
                    out_str_0 = out_str_0+self.dat_file_sub_sep
                    out_str_0 = out_str_0+temp_str_3
                    out_str_0 = out_str_0+self.dat_file_sub_sep
                    out_str_0 = out_str_0+temp_str_0
                    out_str_0 = out_str_0+self.dat_file_sep
                else:
                    temp_bool = False
                if temp_bool:
                    temp_list_0 = []
                    out_str_1 = ""
                    temp_str_5 = temp_str_1[0:3].upper()
                    for n in range(temp_len):
                        temp_tuple_1 = self.cur_org_list[n]
                        if not temp_tuple_1 is None:
                            if len(temp_tuple_1) == 7:
                                temp_str_0 = temp_tuple_1[0].strip()
                                temp_str_1 = temp_tuple_1[1].strip()
                                temp_str_2 = temp_tuple_1[2].strip()
                                temp_str_3 = temp_tuple_1[4].strip()
                                temp_str_4 = temp_tuple_1[6].strip()
                                temp_bool = temp_str_0[0:3].upper() == temp_str_5
                                if temp_bool:
                                    if len(temp_str_2) == 10:
                                        if len(temp_str_3) == 5:
                                            if not temp_str_2[0] in self.numeric_digits:
                                                temp_bool = False
                                            elif not temp_str_2[1] in self.numeric_digits:
                                                temp_bool = False
                                            elif not temp_str_2[2] in self.numeric_digits:
                                                temp_bool = False
                                            elif not temp_str_2[3] in self.numeric_digits:
                                                temp_bool = False
                                            elif temp_str_2[4] != "-":
                                                temp_bool = False
                                            elif not temp_str_2[5] in self.numeric_digits:
                                                temp_bool = False
                                            elif not temp_str_2[6] in self.numeric_digits:
                                                temp_bool = False
                                            elif temp_str_2[7] != "-":
                                                temp_bool = False
                                            elif not temp_str_2[8] in self.numeric_digits:
                                                temp_bool = False
                                            elif not temp_str_2[9] in self.numeric_digits:
                                                temp_bool = False
                                            if temp_bool:
                                                temp_num_5 = int(temp_str_2[0:4])
                                                temp_num_6 = int(temp_str_2[5:7])
                                                temp_num_7 = int(temp_str_2[8:10])
                                                if not temp_str_3[0] in self.numeric_digits:
                                                    temp_bool = False
                                                elif not temp_str_3[1] in self.numeric_digits:
                                                    temp_bool = False
                                                elif temp_str_3[2] != ":":
                                                    temp_bool = False
                                                elif not temp_str_3[3] in self.numeric_digits:
                                                    temp_bool = False
                                                elif not temp_str_3[4] in self.numeric_digits:
                                                    temp_bool = False
                                                if temp_bool:
                                                    temp_num_8 = int(temp_str_3[0:2])
                                                    temp_num_9 = int(temp_str_3[3:5])
                                                    if temp_num_5 > temp_num_0:
                                                        temp_bool = False
                                                    elif temp_num_5 == temp_num_0:
                                                        if temp_num_6 > temp_num_1:
                                                            temp_bool = False
                                                        elif temp_num_6 == temp_num_1:
                                                            if temp_num_7 > temp_num_2:
                                                                temp_bool = False
                                                            elif temp_num_7 == temp_num_2:
                                                                if temp_num_8 > temp_num_3:
                                                                    temp_bool = False
                                                                elif temp_num_8 == temp_num_3:
                                                                    if temp_num_9 > temp_num_4:
                                                                        temp_bool = False
                                                    if temp_bool:
                                                        if self.number_manipulation_valid(temp_str_4, temp_str_0):
                                                            temp_bool = self.num_organization_valid(temp_str_0, 
                                                                                                    temp_num_5, temp_num_6, temp_num_7, 
                                                                                                    temp_num_8, temp_num_9)
                                                        else:
                                                            temp_bool = False
                                        else:
                                            temp_bool = False
                                    else:
                                        temp_bool = False
                                    if temp_bool:
                                        if not temp_str_0 in temp_list_0:
                                            temp_len_1 = len(temp_str_1)
                                            if temp_len_1 < 1:
                                                temp_bool = False
                                            elif temp_len_1 == 1:
                                                temp_str_6 = temp_str_1[0]
                                                if ((not temp_str_6 in self.English_name_capital) & 
                                                    (not temp_str_6 in self.numeric_digits)):
                                                    temp_bool = False
                                            elif temp_len_1 <= self.org_name_max_len:
                                                temp_str_6 = temp_str_1[0]
                                                if ((not temp_str_6 in self.English_name_capital) & 
                                                    (not temp_str_6 in self.numeric_digits)):
                                                    temp_bool = False
                                                for n1 in range(1, temp_len):
                                                    temp_str_6 = temp_str_1[n1].upper()
                                                    if ((not temp_str_6 in self.English_name_capital) & 
                                                        (not temp_str_6 in self.numeric_digits) & 
                                                        (not temp_str_6 in self.English_name_other_1)):
                                                        temp_bool = False
                                                        break
                                            else:
                                                temp_bool = False  
                                        else:
                                            temp_bool = False                    
                            else:
                                temp_bool = False
                            if temp_bool:
                                temp_list_0.append(temp_str_0)
                                out_str_1 = out_str_1+self.dat_file_sep
                                out_str_1 = out_str_1+temp_str_0
                                out_str_1 = out_str_1+self.dat_file_sub_sep
                                out_str_1 = out_str_1+temp_str_1
                                out_str_1 = out_str_1+self.dat_file_sub_sep
                                out_str_1 = out_str_1+temp_str_2
                                out_str_1 = out_str_1+self.dat_file_sub_sep
                                out_str_1 = out_str_1+temp_str_3
                                out_str_1 = out_str_1+self.dat_file_sub_sep
                                out_str_1 = out_str_1+temp_str_4
                            else:
                                break
                    if temp_bool:
                        if self.cur_org[0][0].strip() in temp_list_0:
                            temp_len = len(temp_list_0)
                            out_str_0 = out_str_0+str(temp_len)+out_str_1
                        else:
                            temp_bool = False
                if temp_bool:
                    temp_str_0 = "OrganizationList.dat"
                    temp_str_0 = self.basic_parameter[2][0]+"/"+temp_str_0
                    with open(temp_str_0, "w", encoding = "utf-8") as save_file:
                        save_file.write(out_str_0)
                        save_file.close()
                        showinfo(title = "output *.dat File", 
                                 message = "The file with path '"+temp_str_0+"' is output.")
                else:
                    showerror(title = "Error", 
                              message = "The content is in wrong format.") 
            else:
                showerror(title = "Error", 
                          message = "There is no items to be output.") 
        else:
            showerror(title = "Error", 
                      message = "There is no items to be output.") 
    
    def other_page(self):
        other_page_radio_frame = tk.LabelFrame(self.other_page_frame, 
                                               text = "Other: select a function", 
                                               font = self.fonsize_s)
        other_page_radio_frame.grid(row = 0, column = 0,
                                    padx = 5, pady = 5,
                                    sticky = tk.W)
        other_page_radio_line_0 = tk.Frame(other_page_radio_frame)
        other_page_radio_line_0.grid(row = 0, column = 0,
                                     sticky = tk.W)
        other_page_radio_line_1 = tk.Frame(other_page_radio_frame)
        other_page_radio_line_1.grid(row = 1, column = 0,
                                     sticky = tk.W)
        self.other_page_radio_vari = tk.StringVar()
        self.other_page_scan_validity_radio = tk.Radiobutton(other_page_radio_line_0, 
                                                             variable = self.other_page_radio_vari, 
                                                             text = "Scan a *.iden or *.txt file whether it is a valid file of member's info", 
                                                             value = "valid", 
                                                             font = self.fonsize_s)
        self.other_page_scan_validity_radio.grid(row = 0, column = 0,
                                                 padx = 2, pady = 2, 
                                                 sticky = tk.W)
        self.other_page_number_rule_radio = tk.Radiobutton(other_page_radio_line_1, 
                                                        variable = self.other_page_radio_vari, 
                                                        text = "Simplified rules of generating numbers", 
                                                        value = "rule", 
                                                        font = self.fonsize_s)
        self.other_page_number_rule_radio.grid(row = 0, column = 0,
                                               padx = 2, pady = 2, 
                                               sticky = tk.W)
        self.other_page_about_radio = tk.Radiobutton(other_page_radio_line_1, 
                                                     variable = self.other_page_radio_vari, 
                                                     text = "About", 
                                                     value = "about", 
                                                     font = self.fonsize_s)
        self.other_page_about_radio.grid(row = 0, column = 1,
                                         padx = 2, pady = 2, 
                                         sticky = tk.W)
        ## command
        self.other_page_scan_validity_radio["command"] = self.other_fun_select
        self.other_page_number_rule_radio["command"] = self.other_fun_select
        self.other_page_about_radio["command"] = self.other_fun_select
        
        # scan_valid
        self.other_scan_valid_frame = tk.Frame(self.other_page_frame)
        self.other_scan_valid_frame.grid_forget()   
        self.cur_scan_file_info = None
        self.other_scan_valid_open_button = tk.Button(self.other_scan_valid_frame, 
                                                      text = "Open a *.iden or *.txt file", 
                                                      width = 29, 
                                                      font = self.fonsize_l)
        self.other_scan_valid_open_button.grid(row = 0, column = 0,
                                               padx = 2, pady = 2,
                                               sticky = tk.W)
        other_scan_valid_line_1 = tk.Frame(self.other_scan_valid_frame)
        other_scan_valid_line_1.grid(row = 1, column = 0,
                                     sticky = tk.W)
        self.other_scan_valid_result_pad = ScrolledText(other_scan_valid_line_1, 
                                                        width = 49, 
                                                        height = 12, 
                                                        wrap = tk.WORD, 
                                                        font = self.fonsize_s)
        self.other_scan_valid_result_pad.grid(row = 0, column = 0,
                                              padx = 2, pady = 2,
                                              sticky = tk.W)
        self.other_scan_valid_result_pad["state"] = "normal"
        self.other_scan_valid_result_pad.delete("1.0", "end")
        self.other_scan_valid_result_pad["state"] = "disabled"
        other_scan_valid_save_as_frame = tk.Frame(other_scan_valid_line_1)
        other_scan_valid_save_as_frame.grid(row = 0, column = 1,
                                            padx = 2, pady = 2,
                                            sticky = tk.NW)
        self.other_scan_valid_save_iden_button = tk.Button(other_scan_valid_save_as_frame, 
                                                           text = "Save as *.iden of UTF-8", 
                                                           width = 28, 
                                                           font = self.fonsize_s)
        self.other_scan_valid_save_iden_button.grid(row = 0, column = 0,
                                                    padx = 2, pady = 2,
                                                    sticky = tk.W)
        self.other_scan_valid_save_en_button = tk.Button(other_scan_valid_save_as_frame, 
                                                         text = "Save as *.txt in English of UTF-8", 
                                                         width = 35, 
                                                         font = self.fonsize_s)
        self.other_scan_valid_save_en_button.grid(row = 1, column = 0,
                                                  padx = 2, pady = 2,
                                                  sticky = tk.W)
        self.other_scan_valid_save_zhs_button = tk.Button(other_scan_valid_save_as_frame, 
                                                          text = "Save as *.iden in 简体中文 of UTF-8", 
                                                          width = 35, 
                                                          font = self.fonsize_s)
        self.other_scan_valid_save_zhs_button.grid(row = 2, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        self.other_scan_valid_save_zht_button = tk.Button(other_scan_valid_save_as_frame, 
                                                          text = "Save as *.iden 正體中文 of UTF-8", 
                                                          width = 35, 
                                                          font = self.fonsize_s)
        self.other_scan_valid_save_zht_button.grid(row = 3, column = 0,
                                                   padx = 2, pady = 2,
                                                   sticky = tk.W)
        self.other_scan_valid_save_iden_button["state"] = "disabled"
        self.other_scan_valid_save_en_button["state"] = "disabled"
        self.other_scan_valid_save_zhs_button["state"] = "disabled"
        self.other_scan_valid_save_zht_button["state"] = "disabled"
        ## command
        self.other_scan_valid_open_button["command"] = self.other_fun_scan_valid_open
        self.other_scan_valid_save_iden_button["command"] = lambda in_type = "iden": self.other_fun_scan_valid_save(in_type)
        self.other_scan_valid_save_en_button["command"] = lambda in_type = "en": self.other_fun_scan_valid_save(in_type)
        self.other_scan_valid_save_zhs_button["command"] = lambda in_type = "zhs": self.other_fun_scan_valid_save(in_type)
        self.other_scan_valid_save_zht_button["command"] = lambda in_type = "zht": self.other_fun_scan_valid_save(in_type)
        
        # num_rule
        self.other_num_rule_frame = tk.Frame(self.other_page_frame)
        self.other_num_rule_frame.grid_forget()   
        self.other_rule_pad = ScrolledText(self.other_num_rule_frame, 
                                           width = 63, 
                                           height = 14, 
                                           wrap = tk.WORD, 
                                           font = self.fonsize_s)
        self.other_rule_pad.grid(row = 0, column = 0,
                                 padx = 2, pady = 2,
                                 sticky = tk.W)
        self.other_rule_pad["state"] = "normal"
        self.other_rule_pad.delete("1.0", "end")
        temp_str_0 = "Simplified Rules of Generating Numbers in this Application"
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"1. There are 4 kinds of numbers:"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) Mixed number, which belongs to person, and is of 21 digits, and each digit has 64 different values;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) Member number, which belongs to person, and is of 14 digits, and each digit has 16 different values;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) Organization number, which belongs to organization, and is of 14 digits, and each digit has 64 different values;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) Manipulation number, which belongs to organization, and is of 7 digits, and each digit has 16 different values."
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    Among these 4 kinds:"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) The number, of which each digit has 16 values, is a hexadecimal number, and each digit is from number 0-9 and {'A', 'B', 'C', 'D', 'E', 'F'} (regardless capital or small letter); "
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) For the digit of 16 values, the map is from {'5', 'B', '7', 'F', '0', 'C', '2', 'D', 'E', '9', '3', '1', '4', '8', '6', 'A'} to 0-15;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) The number, of which each digit has 64 values, is a mixture of some characters, and each digit is from 26 English capital letters, 26 English small letters, number 0-9 and {'+', '-'}; "
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) For the digit of 64 values, the map is from {'G', 'B', 'l', 'A', 'r', 's', '6', 'X', 'c', 'K', 'R', 'Q', 'I', 'x', 'h', 'b', "
        temp_str_0 = temp_str_0+"'i', 'f', 'o', 'a', 'M', 'S', 'w', '0', 'P', 'v', '3', 'N', 't', 'g', '8', '2', '+', '-', '4', 'k', '7', 'e', 'n', 'D', "
        temp_str_0 = temp_str_0+"'V', 'y', 'U', 'W', 'F', 'L', 'd', 'T', '1', 'J', 'u', 'Z', 'z', 'C', 'Y', '9', 'm', 'H', 'O', 'E', '5', 'p', 'j', 'q'} to 0-63."
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"2. Mixed number"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) The mixed number is designed with the large amount of possible numbers for the purpose that if the issuers are separated, they can issue different numbers in probability;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) The first 3 digits are from a combination of English letters (according to the issuer's first 3 digits) in capital and/or small cases, totally 8 different kinds;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) The last digit is the remainder of the sum of the other 20 digits divided by 64;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) The combination from 4th digit to the 20th digit encodes issuing date, issuing time, the first 2 letters of English given name, the first 2 letters of English family name;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (5) For each case of first 2 letters of English given name, first 2 letters of English family name, there are possibly 1.405669E+16 different mixed numbers in the same minute;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (6) For 2 persons, if their first 2 letters of English given name and first 2 letters of English family name are not the same, their mixed number must be different;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (7) For 2 persons, if their mixed numbers are issued in different minute (UTC), their mixed number must be different;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (8) If the English name is empty, the mixed number can also be output."
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"3. Member number"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) The member number is designed with the smaller amount of possible numbers than the mixed number, for the purpose that persons can memorize the member numbers;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) The combination of the first 4 digits encodes some digits of the mixed number;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) The combination of the 5th and 6th digits encodes some digits of the issuer's organization number;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) The combination of the 7th and 8th digits encodes some digits of the person's first 2 characters of another name / virtual name in Unicode;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (5) The combination from the 9th to 13th digits encodes issuing date, issuing time;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (6) If the member's English name is not empty, the last digit is the remainder of the sum of the other 13 digits divided by 15;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (7) If the member's English name is empty, the last digit is fixed to 'A', which is 15 as the map;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (8) It is possible that the member numbers of 2 persons are the same in probability."
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"4. Organization number"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) The organization number is designed with the large amount of possible numbers for the purpose that if the issuers in the same league/country are separated, some other issuers can come out with the different organization numbers in probability;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) The first 3 digits are from a combination of English letters (showing that which league/country these organizations belong to) in capital and/or small cases, totally 8 different kinds;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) The last digit is the remainder of the sum of the other 13 digits divided by 64;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) The combination from 4th digit to the 13th digit encodes creating date, creating time;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (5) In every minute, there are possibly 1.662640E+9 different organization numbers;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (6) For 2 organizations, if their organization numbers are created in different minute (UTC), their organization number must be different."
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"5. Manipulation number"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) The manipulation number is designed for manipulators to memorize, and for other organizations to search the exact issuers of mixed numbers and/or member numbers;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) All the 7 digits as a combination encodes some digits of the organization number;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) Within an organization, there are only 1271 are valid."
        temp_str_0 = temp_str_0+"\n\n\n\n"        
        self.rule_str_en = temp_str_0
        self.other_rule_pad.insert("insert", temp_str_0)
        self.other_rule_pad["state"] = "disabled"
        
        # about
        self.other_about_frame = tk.Frame(self.other_page_frame)
        self.other_about_frame.grid_forget()   
        self.other_about_pad = ScrolledText(self.other_about_frame, 
                                            width = 63, 
                                            height = 14, 
                                            wrap = tk.WORD, 
                                            font = self.fonsize_s)
        self.other_about_pad.grid(row = 0, column = 0,
                                  padx = 2, pady = 2,
                                  sticky = tk.W)
        self.other_about_pad["state"] = "normal"
        self.other_about_pad.delete("1.0", "end")
        temp_str_0 = ""
        temp_str_0 = temp_str_0+"Number Generator"
        temp_str_0 = temp_str_0+"\n\n"
        temp_str_0 = temp_str_0+"version "+str(self.version[0])+"."+str(self.version[1])+"."+str(self.version[2])
        temp_str_0 = temp_str_0+"\n\n"
        temp_str_0 = temp_str_0+"March 15, 2022"
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"1. Originally, because there was no designed electronic number system in the New Federal State of China (NFSC), "
        temp_str_0 = temp_str_0+"the idea of generating numbers for identities came out in my brain in October to November 2021. "
        temp_str_0 = temp_str_0+"\n\n"
        temp_str_0 = temp_str_0+"2. In December 2021, the idea of 4 numbers, mixed number, member number, organization number, manipulation number, was formed as the framework of the number generating system. "
        temp_str_0 = temp_str_0+"\n\n"
        temp_str_0 = temp_str_0+"3. In January 2022, to strengthen the avoidance of duplications, I set issuing or creating date and time as factors to be encoded in the numbers. "
        temp_str_0 = temp_str_0+"\n\n"
        temp_str_0 = temp_str_0+"4. In February 2022, because the old algorithm cannot support at least one billion different numbers in probability, I modified it into the other algorithm. "
        temp_str_0 = temp_str_0+"On February 24, 2022, when Russia invaded Ukraine, I noticed that 'the wars are not far from us' and, I decided to continue the modified algorithm, to re-write the whole application as this one. "
        temp_str_0 = temp_str_0+"\n\n"
        temp_str_0 = temp_str_0+"5. In the first half of March 2022, the Chinese Communist Party (CCP) interrupted the Ukraine rescue of the NFSC, "
        temp_str_0 = temp_str_0+"particularly the CCP tried to halt the spreads of rescue information in Chinese from the NFSC, "
        temp_str_0 = temp_str_0+"while there are still many Chinese people in Ukraine."
        temp_str_0 = temp_str_0+"\n\n"
        temp_str_0 = temp_str_0+"As I am a human, to end communism, totalitarianism, dictatorship is not referring to political views, but to termination of antihuman actions. "
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"As I am a Chinese person, to end the ruling of the CCP over Chinese people, to end the threats of the CCP towards Chinese people, "
        temp_str_0 = temp_str_0+"and to bring freedom, democracy, rule-of-law to Chinese people is one of my goals. "
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"As I am a scientist, even though I don't know how to end the wars between Ukraine and Russia, I don't know how to avoid the wars between Mainland China and Taiwan, "
        temp_str_0 = temp_str_0+"my hope is still that I can apply my knowledge to help more people."
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"The algorithm is designed by Hao Jiang."
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"The Python script is written in Python 3.9 by Hao Jiang."
        self.other_about_pad.insert("insert", temp_str_0)
        self.other_about_pad["state"] = "disabled"
    
    def other_fun_select(self):
        temp_str = self.other_page_radio_vari.get()
        if temp_str == "valid":
            self.other_scan_valid_frame.grid(row = 1, column = 0,
                                             padx = 5, pady = 5, 
                                             sticky = tk.NW)
            self.other_scan_valid_result_pad["state"] = "normal"
            self.other_scan_valid_result_pad.delete("1.0", "end")
            self.other_scan_valid_result_pad["state"] = "disabled"
            self.other_scan_valid_save_iden_button["state"] = "disabled"
            self.other_scan_valid_save_en_button["state"] = "disabled"
            self.other_scan_valid_save_zhs_button["state"] = "disabled"
            self.other_scan_valid_save_zht_button["state"] = "disabled"
            self.other_num_rule_frame.grid_forget()
            self.other_about_frame.grid_forget()
        elif temp_str == "rule":
            self.other_scan_valid_frame.grid_forget()
            self.other_num_rule_frame.grid(row = 1, column = 0,
                                           padx = 5, pady = 5, 
                                           sticky = tk.NW)
            self.other_about_frame.grid_forget()
        elif temp_str == "about":
            self.other_scan_valid_frame.grid_forget()
            self.other_num_rule_frame.grid_forget()
            self.other_about_frame.grid(row = 1, column = 0,
                                        padx = 5, pady = 5, 
                                        sticky = tk.NW)
    
    def other_fun_scan_valid_open(self):
        file = askopenfile(mode = "r", 
                           filetypes=[("Identity file / Text file", ("*.iden", "*.txt")), 
                                      ("Identity file", "*.iden"), 
                                      ("Text file",  "*.txt")])  
        if file:
            file_path = file.name
            with open(file_path, "r", encoding = "utf-8") as open_file:
                temp_str_0 = open_file.read()
                temp_bool = True
                if len(file_path) > 4:
                    if file_path[-4:].upper() == ".TXT":
                        self.cur_scan_file_info = self.reading_str_text_member_lang(temp_str_0)
                    else:
                        if len(file_path) > 5:
                            if file_path[-5:].upper() == ".IDEN":
                                self.cur_scan_file_info = self.reading_str_text_mem(temp_str_0)
                            else:
                                temp_bool = False
                        else:
                            temp_bool = False
                else:
                    temp_bool = False
                if not temp_bool:
                    self.cur_scan_file_info = None
                if not self.cur_scan_file_info is None:
                    self.other_scan_valid_result_pad["state"] = "normal"
                    self.other_scan_valid_result_pad.delete("1.0", "end")
                    temp_str_0 = file_path
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"This is a valid file with initial 3 digits '"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[0][0][:3].upper()
                    temp_str_0 = temp_str_0+"'."
                    temp_str_0 = temp_str_0+"\n\n\n\n"
                    temp_str_0 = temp_str_0+"Mixed number (21 digits): "
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[0][0]
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Member number (14 digits): "
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[0][1]
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Issued on "
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[3][0]
                    temp_str_0 = temp_str_0+", at "
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[3][1]
                    temp_str_0 = temp_str_0+"."
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+"UTC (Coordinated Universal Time)"
                    temp_str_0 = temp_str_0+"\n\n\n"
                    temp_str_0 = temp_str_0+"Member's English name: "
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Given name, "
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[1][0]
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Middle name, "
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[1][1]
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Family name, "
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[1][2]
                    temp_str_0 = temp_str_0+"\n\n\n"
                    temp_str_0 = temp_str_0+"Member's another name / virtual name: "
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Type, "
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[2][0]
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Name, "
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[2][1]
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Addition (@ or #), "
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[2][2]
                    temp_str_0 = temp_str_0+"\n\n\n"
                    temp_str_0 = temp_str_0+"Issuer: "
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Manipulation number (7 digits), "
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[4][3]
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Organization number (14 digits), "
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[4][0]
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"Organization name, "
                    temp_str_0 = temp_str_0+"\n"
                    if not self.basic_org_list is None:
                        if not self.basic_org_list[1] is None:
                            temp_num_1 = -1
                            for n in range(len(self.basic_org_list[1])):
                                if self.basic_org_list[1][n][0] == self.cur_scan_file_info[4][0]:
                                    temp_num_1 = n
                                    break
                            if temp_num_1 >= 0:
                                temp_str_0 = temp_str_0+self.basic_org_list[1][n][1]
                            else:
                                temp_str_0 = temp_str_0+"no result"
                        else:
                            temp_str_0 = temp_str_0+"Because the file 'assets/OrganizationList.dat' is broken, the organization number cannot be used in searching."
                    else:
                        temp_str_0 = temp_str_0+"Because the file 'assets/OrganizationList.dat' is not existing, the organization number cannot be used in searching."
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"The organization is created on "
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[4][1]
                    temp_str_0 = temp_str_0+", at "
                    temp_str_0 = temp_str_0+self.cur_scan_file_info[4][2]
                    temp_str_0 = temp_str_0+"."
                    temp_str_0 = temp_str_0+"\n"
                    temp_str_0 = temp_str_0+"UTC (Coordinated Universal Time)"
                    temp_str_0 = temp_str_0+"\n\n\n\n"
                    self.other_scan_valid_result_pad.insert("insert", temp_str_0)
                    self.other_scan_valid_result_pad["state"] = "disabled"
                    self.other_scan_valid_save_iden_button["state"] = "normal"
                    self.other_scan_valid_save_en_button["state"] = "normal"
                    self.other_scan_valid_save_zhs_button["state"] = "normal"
                    self.other_scan_valid_save_zht_button["state"] = "normal"
                else:
                    self.other_scan_valid_result_pad["state"] = "normal"
                    self.other_scan_valid_result_pad.delete("1.0", "end")
                    temp_str_0 = file_path
                    temp_str_0 = temp_str_0+"\n\n"
                    temp_str_0 = temp_str_0+"This is not a valid file."
                    temp_str_0 = temp_str_0+"\n\n\n\n"
                    self.other_scan_valid_result_pad.insert("insert", temp_str_0)
                    self.other_scan_valid_result_pad["state"] = "disabled"
                    self.other_scan_valid_save_iden_button["state"] = "disabled"
                    self.other_scan_valid_save_en_button["state"] = "disabled"
                    self.other_scan_valid_save_zhs_button["state"] = "disabled"
                    self.other_scan_valid_save_zht_button["state"] = "disabled"
                    showerror(title = "Error", 
                              message = "The file is not readable.") 
    
    def other_fun_scan_valid_save(self, in_type):
        if not self.cur_scan_file_info is None:
            temp_str_0 = "Mem_"
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][0][0]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][0][1]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][0][2]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][0][3]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][0][5]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][0][6]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][0][8]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][0][9]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][1][0]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][1][1]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][1][3]
            temp_str_0 = temp_str_0+self.cur_scan_file_info[3][1][4]
            temp_str_0 = temp_str_0+"_"
            temp_str_0 = temp_str_0+self.cur_scan_file_info[1][0]
            temp_str_0 = temp_str_0+"_"
            temp_str_0 = temp_str_0+self.cur_scan_file_info[1][1]
            temp_str_0 = temp_str_0+"_"
            temp_str_0 = temp_str_0+self.cur_scan_file_info[1][2]
            temp_str_0 = temp_str_0+"_"
            temp_str_0 = temp_str_0+self.cur_scan_file_info[0][1]
            if in_type == "iden":
                temp_list_1 = self.forming_str_text_member_lang(self.cur_scan_file_info[0], 
                                                                self.cur_scan_file_info[1], 
                                                                self.cur_scan_file_info[2], 
                                                                self.cur_scan_file_info[3], 
                                                                self.cur_scan_file_info[4])
                file = asksaveasfile(initialfile = temp_str_0+".iden",
                                     defaultextension=".iden",
                                     filetypes=[("Identity file", "*.iden")])
                if file:
                    file_path = file.name
                    with open(file_path, "w", encoding = "utf-8") as save_file:
                        save_file.write(temp_list_1[0])
                        save_file.close()
                        showinfo(title = "Saved", 
                                 message = "The file with path '"+file_path+"' is saved.")                
            if in_type == "en":
                temp_list_1 = self.forming_str_text_member_lang(self.cur_scan_file_info[0], 
                                                                self.cur_scan_file_info[1], 
                                                                self.cur_scan_file_info[2], 
                                                                self.cur_scan_file_info[3], 
                                                                self.cur_scan_file_info[4], 
                                                                if_out_en = True)
                file = asksaveasfile(initialfile = temp_str_0+"_English.txt",
                                     defaultextension=".txt",
                                     filetypes=[("Text file", "*.txt")])
                if file:
                    file_path = file.name
                    with open(file_path, "w", encoding = "utf-8") as save_file:
                        save_file.write(temp_list_1[1])
                        save_file.close()
                        showinfo(title = "Saved", 
                                 message = "The file with path '"+file_path+"' is saved.")   
            if in_type == "zhs":
                temp_list_1 = self.forming_str_text_member_lang(self.cur_scan_file_info[0], 
                                                                self.cur_scan_file_info[1], 
                                                                self.cur_scan_file_info[2], 
                                                                self.cur_scan_file_info[3], 
                                                                self.cur_scan_file_info[4], 
                                                                if_out_zhs = True)
                file = asksaveasfile(initialfile = temp_str_0+"_简体中文.txt",
                                     defaultextension=".txt",
                                     filetypes=[("Text file", "*.txt")])
                if file:
                    file_path = file.name
                    with open(file_path, "w", encoding = "utf-8") as save_file:
                        save_file.write(temp_list_1[2])
                        save_file.close()
                        showinfo(title = "Saved", 
                                 message = "The file with path '"+file_path+"' is saved.")                 
            if in_type == "zht":
                temp_list_1 = self.forming_str_text_member_lang(self.cur_scan_file_info[0], 
                                                                self.cur_scan_file_info[1], 
                                                                self.cur_scan_file_info[2], 
                                                                self.cur_scan_file_info[3], 
                                                                self.cur_scan_file_info[4], 
                                                                if_out_zht = True)
                file = asksaveasfile(initialfile = temp_str_0+"_正體中文.txt",
                                     defaultextension=".txt",
                                     filetypes=[("Text file", "*.txt")])
                if file:
                    file_path = file.name
                    with open(file_path, "w", encoding = "utf-8") as save_file:
                        save_file.write(temp_list_1[3])
                        save_file.close()
                        showinfo(title = "Saved", 
                                 message = "The file with path '"+file_path+"' is saved.") 







    

    def preread(self):
        # basic parameter
        file_bool = os.path.exists("assets/NumGene.dat")
        if file_bool:
            with open("assets/NumGene.dat", "r", encoding = "utf-8") as ini_file:
                self.basic_parameter = ini_file.read()
                ini_file.close()
        else:
            self.basic_parameter = None
        if not self.basic_parameter is None:    
            temp_list_0 = []
            temp_bool_0 = True
            temp_str_list = self.basic_parameter.split(self.dat_file_read_sep)
            if len(temp_str_list) == 9:
                temp_list_0.append(temp_str_list[0].strip())
                temp_str_0 = temp_str_list[1].strip()
                if os.path.exists(temp_str_0):
                    temp_list_1 = [temp_str_0]
                    temp_str_0_0 = temp_str_0+"/iden"
                    temp_str_0_1 = temp_str_0+"/English"
                    temp_str_0_2 = temp_str_0+"/简体中文"
                    temp_str_0_3 = temp_str_0+"/正體中文"
                    if not os.path.exists(temp_str_0_0):
                        temp_bool_0 = False
                    elif not os.path.exists(temp_str_0_1):
                        temp_bool_0 = False
                    elif not os.path.exists(temp_str_0_2):
                        temp_bool_0 = False
                    elif not os.path.exists(temp_str_0_3):
                        temp_bool_0 = False
                    else:
                        temp_list_1.append([temp_str_0_0, temp_str_0_1, temp_str_0_2, temp_str_0_3])
                        temp_str_list_1 = temp_str_list[2].split(self.dat_file_sub_sep)
                        if len(temp_str_list_1) >= 3:
                            temp_list_2 = [True]
                            for n in range(3):
                                temp_bool_str = temp_str_list_1[n].strip()
                                if temp_bool_str == "1":
                                    temp_list_2.append(True)
                                elif temp_bool_str == "0":
                                    temp_list_2.append(False)
                                else:
                                    temp_bool_0 = False
                                    break
                            if temp_bool_0:
                                temp_list_1.append(temp_list_2)
                                temp_list_0.append(temp_list_1)
                        else:
                            temp_bool_0 = False
                else:
                    temp_bool_0 = False                    
                if temp_bool_0:
                    temp_str_1 = temp_str_list[3].strip()
                    if os.path.exists(temp_str_1):
                        temp_list_1 = [temp_str_1]
                        temp_list_0.append(temp_list_1)
                    else:
                        temp_bool_0 = False
                if temp_bool_0:
                    temp_str_2 = temp_str_list[5].strip()
                    if os.path.exists(temp_str_2):
                        temp_list_1 = [temp_str_2]
                        temp_str_2_0 = temp_str_2+"/Slot-1"
                        temp_str_2_1 = temp_str_2+"/Slot-2"
                        temp_str_2_2 = temp_str_2+"/Slot-3"
                        temp_str_2_3 = temp_str_2+"/Slot-4"
                        temp_str_2_4 = temp_str_2+"/Slot-5"
                        temp_str_2_5 = temp_str_2+"/Slot-6"
                        temp_str_2_6 = temp_str_2+"/Slot-7"
                        temp_str_2_7 = temp_str_2+"/Slot-8"
                        if not os.path.exists(temp_str_2_0):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_2_1):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_2_2):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_2_3):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_2_4):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_2_5):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_2_6):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_2_7):
                            temp_bool_0 = False
                        else:
                            temp_list_1.append([temp_str_2_0, temp_str_2_1, temp_str_2_2, 
                                                temp_str_2_3, temp_str_2_4, temp_str_2_5, 
                                                temp_str_2_6, temp_str_2_7])
                            temp_list_0.append(temp_list_1)
                    else:
                        temp_bool_0 = False  
                if temp_bool_0:
                    temp_str_3 = temp_str_list[7].strip()
                    if os.path.exists(temp_str_3):
                        temp_list_1 = [temp_str_3]
                        temp_str_3_0 = temp_str_3+"/Slot-1"
                        temp_str_3_1 = temp_str_3+"/Slot-2"
                        temp_str_3_2 = temp_str_3+"/Slot-3"
                        temp_str_3_3 = temp_str_3+"/Slot-4"
                        temp_str_3_4 = temp_str_3+"/Slot-5"
                        temp_str_3_5 = temp_str_3+"/Slot-6"
                        temp_str_3_6 = temp_str_3+"/Slot-7"
                        temp_str_3_7 = temp_str_3+"/Slot-8"
                        if not os.path.exists(temp_str_3_0):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_3_1):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_3_2):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_3_3):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_3_4):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_3_5):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_3_6):
                            temp_bool_0 = False
                        elif not os.path.exists(temp_str_3_7):
                            temp_bool_0 = False
                        else:
                            temp_list_1.append([temp_str_3_0, temp_str_3_1, temp_str_3_2, 
                                                temp_str_3_3, temp_str_3_4, temp_str_3_5, 
                                                temp_str_3_6, temp_str_3_7])
                            temp_list_0.append(temp_list_1)
                    else:
                        temp_bool_0 = False 
            else:
                temp_bool_0 = False
            if temp_bool_0:
                self.basic_parameter = temp_list_0
            else:
                self.basic_parameter = None
        if self.basic_parameter is None:    
            temp_list_0 = [""]
            temp_str_1 = "NewMember"
            temp_str_0 = self.dat_file_sep
            temp_str_0 = temp_str_0+temp_str_1
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_list_1 = [temp_str_1]
            temp_list_1.append([temp_str_1+"/iden", 
                                temp_str_1+"/English", 
                                temp_str_1+"/简体中文", 
                                temp_str_1+"/正體中文"])
            temp_list_1.append([True, 
                                True, 
                                False, 
                                False])
            temp_str_0 = temp_str_0+"1"
            temp_str_0 = temp_str_0+self.dat_file_sub_sep
            temp_str_0 = temp_str_0+"0"
            temp_str_0 = temp_str_0+self.dat_file_sub_sep
            temp_str_0 = temp_str_0+"0"
            if not os.path.exists(temp_list_1[0]):
                os.mkdir(temp_list_1[0])
            if not os.path.exists(temp_list_1[1][0]):
                os.mkdir(temp_list_1[1][0])
            if not os.path.exists(temp_list_1[1][1]):
                os.mkdir(temp_list_1[1][1])
            if not os.path.exists(temp_list_1[1][2]):
                os.mkdir(temp_list_1[1][2])
            if not os.path.exists(temp_list_1[1][3]):
                os.mkdir(temp_list_1[1][3])
            temp_list_0.append(temp_list_1)
            temp_str_1 = "OutputConfiguration"            
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_str_0 = temp_str_0+temp_str_1
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_list_1 = [temp_str_1]
            temp_list_0.append(temp_list_1) 
            if not os.path.exists(temp_list_1[0]):
                os.mkdir(temp_list_1[0])
            temp_str_1 = "OutputCSV"            
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_str_0 = temp_str_0+temp_str_1
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_list_1 = [temp_str_1]
            temp_list_1.append([temp_str_1+"/Slot-1", 
                                temp_str_1+"/Slot-2", 
                                temp_str_1+"/Slot-3", 
                                temp_str_1+"/Slot-4", 
                                temp_str_1+"/Slot-5", 
                                temp_str_1+"/Slot-6", 
                                temp_str_1+"/Slot-7", 
                                temp_str_1+"/Slot-8"])
            temp_list_0.append(temp_list_1)  
            if not os.path.exists(temp_list_1[0]):
                os.mkdir(temp_list_1[0])
            if not os.path.exists(temp_list_1[1][0]):
                os.mkdir(temp_list_1[1][0])
            if not os.path.exists(temp_list_1[1][1]):
                os.mkdir(temp_list_1[1][1])
            if not os.path.exists(temp_list_1[1][2]):
                os.mkdir(temp_list_1[1][2])
            if not os.path.exists(temp_list_1[1][3]):
                os.mkdir(temp_list_1[1][3])  
            if not os.path.exists(temp_list_1[1][4]):
                os.mkdir(temp_list_1[1][4])
            if not os.path.exists(temp_list_1[1][5]):
                os.mkdir(temp_list_1[1][5])
            if not os.path.exists(temp_list_1[1][6]):
                os.mkdir(temp_list_1[1][6])    
            if not os.path.exists(temp_list_1[1][7]):
                os.mkdir(temp_list_1[1][7])          
            temp_str_1 = "Database"            
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_str_0 = temp_str_0+temp_str_1
            temp_str_0 = temp_str_0+self.dat_file_sep
            temp_list_1 = [temp_str_1]
            temp_list_1.append([temp_str_1+"/Slot-1", 
                                temp_str_1+"/Slot-2", 
                                temp_str_1+"/Slot-3", 
                                temp_str_1+"/Slot-4", 
                                temp_str_1+"/Slot-5", 
                                temp_str_1+"/Slot-6", 
                                temp_str_1+"/Slot-7", 
                                temp_str_1+"/Slot-8"])
            temp_list_0.append(temp_list_1)   
            if not os.path.exists(temp_list_1[0]):
                os.mkdir(temp_list_1[0])
            if not os.path.exists(temp_list_1[1][0]):
                os.mkdir(temp_list_1[1][0])
            if not os.path.exists(temp_list_1[1][1]):
                os.mkdir(temp_list_1[1][1])
            if not os.path.exists(temp_list_1[1][2]):
                os.mkdir(temp_list_1[1][2])
            if not os.path.exists(temp_list_1[1][3]):
                os.mkdir(temp_list_1[1][3])  
            if not os.path.exists(temp_list_1[1][4]):
                os.mkdir(temp_list_1[1][4])
            if not os.path.exists(temp_list_1[1][5]):
                os.mkdir(temp_list_1[1][5])
            if not os.path.exists(temp_list_1[1][6]):
                os.mkdir(temp_list_1[1][6])   
            if not os.path.exists(temp_list_1[1][7]):
                os.mkdir(temp_list_1[1][7])   
            self.basic_parameter = temp_list_0
            with open("assets/NumGene.dat", "w", encoding = "utf-8") as save_file:
                save_file.write(temp_str_0)
                save_file.close()
        
        # organization list
        file_bool = os.path.exists("assets/OrganizationList.dat")
        if file_bool:
            with open("assets/OrganizationList.dat", "r", encoding = "utf-8") as ini_file:
                self.basic_org_list = ini_file.read()
                ini_file.close()
        else:
            self.basic_org_list = None
        if not self.basic_org_list is None:
            temp_bool_0 = True
            temp_str_list_0 = self.basic_org_list.split(self.dat_file_read_sep)
            temp_len_0 = len(temp_str_list_0)
            if temp_len_0 >= 3:
                temp_str_0 = temp_str_list_0[1].strip()
                temp_len_1 = len(temp_str_0)
                if temp_len_1 > 0:
                    for n1 in range(temp_len_1):
                        if not temp_str_0[n1] in self.numeric_digits:
                            temp_bool_0 = False  
                            break
                else:
                    temp_bool_0 = False   
                if temp_bool_0:
                    temp_len_1 = int(temp_str_0)
                    temp_bool_0 = temp_len_1 + 2 == temp_len_0
                    if temp_bool_0:
                        temp_str_list_1 = temp_str_list_0[0].split(self.dat_file_sub_sep)
                        if len(temp_str_list_1) == 4:
                            temp_str_0 = temp_str_list_1[0].strip()
                            temp_str_1 = temp_str_list_1[1].strip()
                            temp_str_2 = temp_str_list_1[2].strip()
                            temp_str_3 = temp_str_list_1[3].strip()                            
                            if len(temp_str_1) == 10:
                                if len(temp_str_2) == 5:
                                    if not temp_str_1[0] in self.numeric_digits:
                                        temp_bool_0 = False
                                    elif not temp_str_1[1] in self.numeric_digits:
                                        temp_bool_0 = False
                                    elif not temp_str_1[2] in self.numeric_digits:
                                        temp_bool_0 = False
                                    elif not temp_str_1[3] in self.numeric_digits:
                                        temp_bool_0 = False
                                    elif temp_str_1[4] != "-":
                                        temp_bool_0 = False
                                    elif not temp_str_1[5] in self.numeric_digits:
                                        temp_bool_0 = False
                                    elif not temp_str_1[6] in self.numeric_digits:
                                        temp_bool_0 = False
                                    elif temp_str_1[7] != "-":
                                        temp_bool_0 = False
                                    elif not temp_str_1[8] in self.numeric_digits:
                                        temp_bool_0 = False
                                    elif not temp_str_1[9] in self.numeric_digits:
                                        temp_bool_0 = False
                                    if temp_bool_0:
                                        temp_num_0 = int(temp_str_1[0:4])
                                        temp_num_1 = int(temp_str_1[5:7])
                                        temp_num_2 = int(temp_str_1[8:10])
                                        if not temp_str_2[0] in self.numeric_digits:
                                            temp_bool_0 = False
                                        elif not temp_str_2[1] in self.numeric_digits:
                                            temp_bool_0 = False
                                        elif temp_str_2[2] != ":":
                                            temp_bool_0 = False
                                        elif not temp_str_2[3] in self.numeric_digits:
                                            temp_bool_0 = False
                                        elif not temp_str_2[4] in self.numeric_digits:
                                            temp_bool_0 = False
                                        if temp_bool_0:
                                            temp_num_3 = int(temp_str_2[0:2])
                                            temp_num_4 = int(temp_str_2[3:5])
                                            temp_bool_0 = self.number_manipulation_valid(temp_str_3, temp_str_0)
                                else:
                                    temp_bool_0 = False 
                            else:
                                temp_bool_0 = False
                        else:
                            temp_bool_0 = False  
                if temp_bool_0:
                    temp_tuple_0 = (temp_str_0, temp_str_1, temp_str_2, temp_str_3)
                    temp_str_9 = temp_str_0[0:3].upper()
                    temp_list_0 = []
                    temp_list_1 = []
                    for n in range(2, temp_len_0):
                        temp_str_list_1 = temp_str_list_0[n].split(self.dat_file_sub_sep)
                        if len(temp_str_list_1) == 5:
                            temp_str_4 = temp_str_list_1[0].strip()
                            if not temp_str_4 in temp_list_1:
                                temp_list_1.append(temp_str_0)
                                temp_str_5 = temp_str_list_1[1].strip()
                                temp_str_6 = temp_str_list_1[2].strip()
                                temp_str_7 = temp_str_list_1[3].strip()
                                temp_str_8 = temp_str_list_1[4].strip()
                                if len(temp_str_6) == 10:
                                    if len(temp_str_7) == 5:
                                        if not temp_str_6[0] in self.numeric_digits:
                                            temp_bool_0 = False
                                        elif not temp_str_6[1] in self.numeric_digits:
                                            temp_bool_0 = False
                                        elif not temp_str_6[2] in self.numeric_digits:
                                            temp_bool_0 = False
                                        elif not temp_str_6[3] in self.numeric_digits:
                                            temp_bool_0 = False
                                        elif temp_str_6[4] != "-":
                                            temp_bool_0 = False
                                        elif not temp_str_6[5] in self.numeric_digits:
                                            temp_bool_0 = False
                                        elif not temp_str_6[6] in self.numeric_digits:
                                            temp_bool_0 = False
                                        elif temp_str_6[7] != "-":
                                            temp_bool_0 = False
                                        elif not temp_str_6[8] in self.numeric_digits:
                                            temp_bool_0 = False
                                        elif not temp_str_6[9] in self.numeric_digits:
                                            temp_bool_0 = False
                                        if temp_bool_0:
                                            temp_num_5 = int(temp_str_6[0:4])
                                            temp_num_6 = int(temp_str_6[5:7])
                                            temp_num_7 = int(temp_str_6[8:10])
                                            if not temp_str_7[0] in self.numeric_digits:
                                                temp_bool_0 = False
                                            elif not temp_str_7[1] in self.numeric_digits:
                                                temp_bool_0 = False
                                            elif temp_str_7[2] != ":":
                                                temp_bool_0 = False
                                            elif not temp_str_7[3] in self.numeric_digits:
                                                temp_bool_0 = False
                                            elif not temp_str_7[4] in self.numeric_digits:
                                                temp_bool_0 = False
                                            if temp_bool_0:
                                                temp_num_8 = int(temp_str_7[0:2])
                                                temp_num_9 = int(temp_str_7[3:5])
                                                if temp_num_5 > temp_num_0:
                                                    temp_bool_0 = False
                                                elif temp_num_5 == temp_num_0:
                                                    if temp_num_6 > temp_num_1:
                                                        temp_bool_0 = False
                                                    elif temp_num_6 == temp_num_1:
                                                        if temp_num_7 > temp_num_2:
                                                            temp_bool_0 = False
                                                        elif temp_num_7 == temp_num_2:
                                                            if temp_num_8 > temp_num_3:
                                                                temp_bool_0 = False
                                                            elif temp_num_8 == temp_num_3:
                                                                if temp_num_9 > temp_num_4:
                                                                    temp_bool_0 = False
                                                if temp_bool_0:
                                                    if self.number_manipulation_valid(temp_str_8, temp_str_4):
                                                        temp_bool_0 = self.num_organization_valid(temp_str_4, 
                                                                                                  temp_num_5, temp_num_6, temp_num_7, 
                                                                                                  temp_num_8, temp_num_9)
                                                    else:
                                                        temp_bool_0 = False
                                                if temp_bool_0:
                                                    if temp_str_4[0:3].upper() == temp_str_9:
                                                        temp_len = len(temp_str_5)
                                                        if temp_len < 1:
                                                            temp_bool_0 = False
                                                        elif temp_len == 1:
                                                            temp_str_10 = temp_str_5[0]
                                                            if ((not temp_str_10 in self.English_name_capital) & 
                                                                (not temp_str_10 in self.numeric_digits)):
                                                                temp_bool_0 = False
                                                        elif temp_len <= self.org_name_max_len:
                                                            temp_str_10 = temp_str_5[0]
                                                            if ((not temp_str_10 in self.English_name_capital) & 
                                                                (not temp_str_10 in self.numeric_digits)):
                                                                temp_bool_0 = False
                                                            for n1 in range(1, temp_len):
                                                                temp_str_10 = temp_str_5[n1].upper()
                                                                if ((not temp_str_10 in self.English_name_capital) & 
                                                                    (not temp_str_10 in self.numeric_digits) & 
                                                                    (not temp_str_10 in self.English_name_other_1)):
                                                                    temp_bool_0 = False
                                                                    break
                                                        else:
                                                            temp_bool_0 = False
                            else:
                                temp_bool_0 = False
                        else:
                            temp_bool_0 = False
                        if temp_bool_0:
                            temp_list_0.append((temp_str_4, temp_str_5, temp_str_6, 
                                                temp_str_7, temp_str_8))
                        else:
                            break
                    if temp_bool_0:
                        temp_bool_0 = temp_tuple_0[0] in temp_list_1
            else:
                temp_bool_0 = False
            if temp_bool_0:
                self.basic_org_list = (temp_tuple_0, tuple(temp_list_0))
            else:
                self.basic_org_list = (None, None)
    
    def English_name_change_quotation_mark(self, in_list):
        temp_bool = True
        temp_str_0 = in_list[0].strip()
        temp_len_0 = len(temp_str_0)
        temp_str_1 = in_list[1].strip()
        temp_len_1 = len(temp_str_1)
        temp_str_2 = in_list[2].strip()
        temp_len_2 = len(temp_str_2)
        if temp_len_0 < 1:
            temp_bool = (temp_len_1 < 1) & (temp_len_2 < 1)
        else:
            temp_str_3 = ""
            if temp_len_0 == 1:
                temp_str_4 = temp_str_0[0].upper()
                if temp_str_4 in self.English_name_capital:
                    temp_str_3 = temp_str_3+temp_str_4
                    temp_str_0 = temp_str_3
                else:
                    temp_bool = False
            else:
                temp_str_4 = temp_str_0[0].upper()
                if temp_str_4 in self.English_name_capital:
                    temp_str_3 = temp_str_3+temp_str_4
                    for n in range(1, temp_len_0):
                        temp_str_4 = temp_str_0[n]
                        if (temp_str_4 == "‘") | (temp_str_4 == "’") | (temp_str_4 == "`"):
                            temp_str_4 = "'"
                        if ((temp_str_4.upper() in self.English_name_capital) | 
                            (temp_str_4 in self.English_name_other)):
                            temp_str_3 = temp_str_3+temp_str_4
                        else:
                            temp_bool = False
                            break
                    if temp_bool:
                        temp_str_0 = temp_str_3
                else:
                    temp_bool = False
            if temp_bool:
                temp_str_3 = ""
                if temp_len_1 == 1:
                    temp_str_4 = temp_str_1[0].upper()
                    if temp_str_4 in self.English_name_capital:
                        temp_str_3 = temp_str_3+temp_str_4
                        temp_str_1 = temp_str_3
                    else:
                        temp_bool = False
                elif temp_len_1 > 1:
                    temp_str_4 = temp_str_1[0].upper()
                    if temp_str_4 in self.English_name_capital:
                        temp_str_3 = temp_str_3+temp_str_4
                        for n in range(1, temp_len_1):
                            temp_str_4 = temp_str_1[n]
                            if (temp_str_4 == "‘") |(temp_str_4 == "’") | (temp_str_4 == "`"):
                                temp_str_4 = "'"
                            if ((temp_str_4.upper() in self.English_name_capital) | 
                                (temp_str_4 in self.English_name_other)):
                                temp_str_3 = temp_str_3+temp_str_4
                            else:
                                temp_bool = False
                                break
                        if temp_bool:
                            temp_str_1 = temp_str_3
                    else:
                        temp_bool = False
            if temp_bool:
                temp_str_3 = ""
                if temp_len_2 == 1:
                    temp_str_4 = temp_str_2[0].upper()
                    if temp_str_4 in self.English_name_capital:
                        temp_str_3 = temp_str_3+temp_str_4
                        temp_str_2 = temp_str_3
                    else:
                        temp_bool = False
                elif temp_len_2 > 1:
                    temp_str_4 = temp_str_2[0].upper()
                    if temp_str_4 in self.English_name_capital:
                        temp_str_3 = temp_str_3+temp_str_4
                        for n in range(1, temp_len_2):
                            temp_str_4 = temp_str_2[n]
                            if (temp_str_4 == "‘") | (temp_str_4 == "’") | (temp_str_4 == "`"):
                                temp_str_4 = "'"
                            if ((temp_str_4.upper() in self.English_name_capital) | 
                                (temp_str_4 in self.English_name_other)):
                                temp_str_3 = temp_str_3+temp_str_4
                            else:
                                temp_bool = False
                                break
                        if temp_bool:
                            temp_str_2 = temp_str_3
                    else:
                        temp_bool = False
        if temp_bool:
            out_list = [temp_str_0, temp_str_1, temp_str_2]
        else:
            out_list = None
        return out_list
    
    def English_name_valid(self, in_list):
        out_bool = True
        temp_len_0 = len(in_list[0])
        temp_len_1 = len(in_list[1])
        temp_len_2 = len(in_list[2])
        if temp_len_0 < 1:
            out_bool = (temp_len_1 < 1) & (temp_len_2 < 1)
        else:
            if temp_len_0 == 1:
                out_bool = in_list[0][0] in self.English_name_capital
            else:
                if in_list[0][0] in self.English_name_capital:
                    for n in range(1, temp_len_0):
                        temp_str_0 = in_list[0][n].upper()
                        if ((not temp_str_0 in self.English_name_capital) & 
                            (not temp_str_0 in self.English_name_other)):
                            out_bool = False
                            break
                else:
                    out_bool = False
            if out_bool:
                if temp_len_1 > 0:
                    if temp_len_1 == 1:
                        out_bool = in_list[1][0] in self.English_name_capital
                    else:
                        if in_list[1][0] in self.English_name_capital:
                            for n in range(1, temp_len_1):
                                temp_str_0 = in_list[1][n].upper()
                                if ((not temp_str_0 in self.English_name_capital) & 
                                    (not temp_str_0 in self.English_name_other)):
                                    out_bool = False
                                    break
                        else:
                            out_bool = False
            if out_bool:
                if temp_len_2 > 0:
                    if temp_len_2 == 1:
                        out_bool = in_list[2][0] in self.English_name_capital
                    else:
                        if in_list[2][0] in self.English_name_capital:
                            for n in range(1, temp_len_2):
                                temp_str_0 = in_list[2][n].upper()
                                if ((not temp_str_0 in self.English_name_capital) & 
                                    (not temp_str_0 in self.English_name_other)):
                                    out_bool = False
                                    break
                        else:
                            out_bool = False
        return out_bool
    
    def virtual_name_change_quotation_mark(self, in_list):
        temp_bool = True
        temp_str_0 = in_list[0]
        temp_len_1 = len(in_list[1])
        temp_len_2 = len(in_list[2])
        if temp_str_0 in self.virtual_type:
            if temp_str_0 == self.virtual_type[0]:
                temp_str_1 = ""
                temp_str_2 = ""
            elif temp_len_1 < 1:
                if temp_len_2 < 1:
                    temp_str_0 = self.virtual_type[0]
                    temp_str_1 = ""
                    temp_str_2 = ""
                else:
                    temp_bool = False
            else:
                temp_str_1 = ""
                for n in range(temp_len_1):
                    temp_str_3 = in_list[1][n]
                    temp_num_0 = ord(temp_str_3)
                    if (temp_num_0 >= 32) & (temp_num_0 < 65536):
                        if not temp_str_1 in ("'", '"'):
                            temp_str_1 = temp_str_1+temp_str_3
                        else:
                            temp_str_1 = temp_str_1+"?"
                    else:
                        temp_bool = False
                        break
                if temp_bool:
                    temp_str_2 = ""
                    for n in range(temp_len_2):
                        temp_str_3 = in_list[2][n]
                        temp_num_0 = ord(temp_str_3)
                        if (temp_num_0 >= 32) & (temp_num_0 < 65536):
                            if not temp_str_1 in ("'", '"'):
                                temp_str_2 = temp_str_2+temp_str_3
                            else:
                                temp_str_2 = temp_str_2+"?"
                        else:
                            temp_bool = False
                            break
        else:
            temp_bool = False
        if temp_bool:
            out_list = [temp_str_0, temp_str_1, temp_str_2]
        else:
            out_list = None
        return out_list
    
    def virtual_name_valid(self, in_list):
        out_bool = True
        temp_len_1 = len(in_list[1])
        temp_len_2 = len(in_list[2])
        if in_list[0] in self.virtual_type:
            if in_list[0].upper() in ("NONE", "NULL", "NA"):
                out_bool = (temp_len_1 < 1) & (temp_len_2 < 1)
            else:
                if temp_len_1 > 0:
                    for n in range(temp_len_1):
                        temp_str_0 = in_list[1][n]
                        temp_num_0 = ord(temp_str_0)
                        if (temp_num_0 >= 32) & (temp_num_0 < 65536):
                            if temp_str_0 in ("'", '"'):
                               out_bool = False
                               break
                        else:
                            out_bool = False
                            break
                    if out_bool:
                        for n in range(temp_len_2):
                            temp_str_0 = in_list[2][n]
                            temp_num_0 = ord(temp_str_0)
                            if (temp_num_0 >= 32) & (temp_num_0 < 65536):
                                if temp_str_0 in ("'", '"'):
                                   out_bool = False
                                   break
                            else:
                                out_bool = False
                                break    
                else:
                    out_bool = False
        else:
            out_bool = False
        return out_bool
    
    def number_mix_generate(self, in_list_name, in_initial_list):
        # to generate mixed number, 21 digits
        
        # input:
        # in_list_name = [[given name 0, family name 0] / None, 
        #                 [given name 1, family name 1] / None, 
        #                 [given name 2, family name 2] / None, ...]
        # in_initial_list = [*, *, *]
        #                   each of the *s is from 26 letters
        
        # output:
        # out_result = [[out number 0, given name 0, family name 0, 
        #                if exists English name 0, Date-UTC 0, Time-UTC 0] / None,
        #               [out number 1, given name 1, family name 1, 
        #                if exists English name 1, Date-UTC 1, Time-UTC 1] / None,
        #               [out number 2, given name 2, family name 2, 
        #                if exists English name 2, Date-UTC 2, Time-UTC 2] / None, ...]
            
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        English_name_capital = ("A", "B", "C", "D", "E", "F", "G", 
                                "H", "I", "J", "K", "L", "M", "N", 
                                "O", "P", "Q", "R", "S", "T", 
                                "U", "V", "W", "X", "Y", "Z")
        English_name_other = (" ", "-", "'")
        out_result = []
        temp_bool_0 = True
        if isinstance(in_initial_list, list) | isinstance(in_initial_list, tuple):
            if len(in_initial_list) == 3:
                init_char_0 = in_initial_list[0]
                init_char_1 = in_initial_list[1]
                init_char_2 = in_initial_list[2]
                if (isinstance(init_char_0, str) & isinstance(init_char_1, str) &
                    isinstance(init_char_2, str)):
                    init_char_0 = init_char_0.strip().upper()
                    init_char_1 = init_char_1.strip().upper()
                    init_char_2 = init_char_2.strip().upper()
                    if ((init_char_0 in English_name_capital) & (init_char_1 in English_name_capital) & 
                        (init_char_2 in English_name_capital)):
                        first_3_digits = (init_char_0.lower()+init_char_1.lower()+init_char_2.lower(), 
                                          init_char_0.lower()+init_char_1.lower()+init_char_2, 
                                          init_char_0.lower()+init_char_1+init_char_2.lower(), 
                                          init_char_0.lower()+init_char_1+init_char_2, 
                                          init_char_0+init_char_1.lower()+init_char_2.lower(), 
                                          init_char_0+init_char_1.lower()+init_char_2, 
                                          init_char_0+init_char_1+init_char_2.lower(), 
                                          init_char_0+init_char_1+init_char_2)
                        
                    else:
                        temp_bool_0 = False
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        if temp_bool_0:
            if isinstance(in_list_name, list) | isinstance(in_list_name, tuple):
                temp_len = len(in_list_name)
                if temp_len > 0:
                    temp_time_now = datetime.utcnow()
                    temp_num_0 = temp_time_now.microsecond
                    temp_num_0 = temp_num_0*60+temp_time_now.second
                    temp_num_0 = temp_num_0*60+temp_time_now.minute
                    temp_num_0 = temp_num_0*24+temp_time_now.hour
                    seed(temp_num_0)
                    for n in range(temp_len):
                        if self.cur_progress_bool:
                            temp_bool_1 = True
                            if in_list_name[n] is None:
                                out_result.append(None)
                            elif isinstance(in_list_name[n], list) | isinstance(in_list_name[n], tuple):
                                if len(in_list_name[n]) == 2:
                                    if isinstance(in_list_name[n][0], str) & isinstance(in_list_name[n][1], str):
                                        temp_gn_str = in_list_name[n][0].strip()
                                        temp_len_1 = len(temp_gn_str)
                                        temp_fn_str = in_list_name[n][1].strip()
                                        temp_len_2 = len(temp_fn_str)
                                        if temp_len_1 == 0:
                                            if temp_len_2 == 0:
                                                temp_gn_1 = 0
                                                temp_gn_2 = 0
                                            else:
                                                temp_bool_1 = False
                                        elif temp_len_1 == 1:
                                            temp_str_1 = temp_gn_str[0]
                                            temp_gn_1 = 0                                
                                            for n2 in range(26):
                                                if English_name_capital[n2] == temp_str_1:
                                                    temp_gn_1 = n2+1
                                                    break
                                            if temp_gn_1 > 0:
                                                temp_gn_2 = 0
                                            else:
                                                temp_bool_1 = False
                                        else:
                                            temp_str_1 = temp_gn_str[0]
                                            temp_gn_1 = 0                                
                                            for n2 in range(26):
                                                if English_name_capital[n2] == temp_str_1:
                                                    temp_gn_1 = n2+1
                                                    break
                                            if temp_gn_1 > 0:
                                                temp_str_2 = temp_gn_str[1].upper()
                                                temp_gn_2 = 0                                
                                                for n2 in range(26):
                                                    if English_name_capital[n2] == temp_str_2:
                                                        temp_gn_2 = n2+1
                                                        break
                                                if temp_gn_2 < 1:
                                                    temp_bool_1 = temp_str_2 in English_name_other
                                            else:
                                                temp_bool_1 = False
                                        if temp_bool_1:
                                            if temp_len_2 == 0:
                                                temp_fn_1 = 0
                                                temp_fn_2 = 0
                                            elif temp_len_2 == 1:
                                                temp_str_1 = temp_fn_str[0]
                                                temp_fn_1 = 0                                
                                                for n2 in range(26):
                                                    if English_name_capital[n2] == temp_str_1:
                                                        temp_fn_1 = n2+1
                                                        break
                                                if temp_fn_1 > 0:
                                                    temp_fn_2 = 0
                                                else:
                                                    temp_bool_1 = False
                                            else:
                                                temp_str_1 = temp_fn_str[0]
                                                temp_fn_1 = 0                                
                                                for n2 in range(26):
                                                    if English_name_capital[n2] == temp_str_1:
                                                        temp_fn_1 = n2+1
                                                        break
                                                if temp_fn_1 > 0:
                                                    temp_str_2 = temp_fn_str[1].upper()
                                                    temp_fn_2 = 0                                
                                                    for n2 in range(26):
                                                        if English_name_capital[n2] == temp_str_2:
                                                            temp_fn_2 = n2+1
                                                            break
                                                    if temp_fn_2 < 1:
                                                        temp_bool_1 = temp_str_2 in English_name_other
                                                else:
                                                    temp_bool_1 = False
                                        if temp_bool_1:
                                            temp_time_now = datetime.utcnow()
                                            temp_year = temp_time_now.year
                                            temp_year_3 = temp_year%10
                                            temp_year_0 = int((temp_year-temp_year_3)/10)
                                            temp_year_2 = temp_year_0%10
                                            temp_year_0 = int((temp_year_0-temp_year_2)/10)
                                            temp_year_1 = temp_year_0%10
                                            temp_year_0 = int((temp_year_0-temp_year_1)/10)
                                            temp_month = temp_time_now.month
                                            temp_day = temp_time_now.day
                                            temp_hour = temp_time_now.hour
                                            temp_minute = temp_time_now.minute
                                            temp_num_0 = 0
                                            temp_runif = 1.0
                                            while temp_runif == 1.0:
                                                temp_runif = uniform(0.0, 1.0)
                                            temp_num_1_0 = int(temp_runif*8)
                                            if temp_num_1_0 == 8:
                                                temp_num_1_0 -= 1
                                            out_num_str = first_3_digits[temp_num_1_0]
                                            temp_str_3 = out_num_str[0]
                                            temp_num_1_1 = -1
                                            for n2 in range(64):
                                                if long_digits[n2] == temp_str_3:
                                                    temp_num_1_1 = n2
                                                    break
                                            init_num_0 = temp_num_1_1
                                            temp_num_0 += temp_num_1_1
                                            temp_str_3 = out_num_str[1]
                                            temp_num_1_1 = -1
                                            for n2 in range(64):
                                                if long_digits[n2] == temp_str_3:
                                                    temp_num_1_1 = n2
                                                    break
                                            init_num_1 = temp_num_1_1
                                            temp_num_0 += temp_num_1_1
                                            temp_str_3 = out_num_str[2]
                                            temp_num_1_1 = -1
                                            for n2 in range(64):
                                                if long_digits[n2] == temp_str_3:
                                                    temp_num_1_1 = n2
                                                    break
                                            init_num_2 = temp_num_1_1
                                            temp_num_0 += temp_num_1_1 
                                            temp_runif = 1.0
                                            while temp_runif == 1.0:
                                                temp_runif = uniform(0.0, 1.0)
                                            temp_num_2_1 = int(temp_runif*2297)
                                            if temp_num_2_1 == 2297:
                                                temp_num_2_1 -= 1
                                            temp_num_2_2 = temp_year_2
                                            temp_num_2_2 = temp_num_2_2*27+temp_fn_2
                                            temp_num_2_2 = temp_num_2_2*27+temp_gn_2
                                            temp_num_2 = temp_num_2_2+temp_num_2_1*7297
                                            temp_num_2_3 = temp_num_2%64
                                            temp_num_2_0 = int((temp_num_2-temp_num_2_3)/64)
                                            temp_num_2_2 = temp_num_2_0%64
                                            temp_num_2_0 = int((temp_num_2_0-temp_num_2_2)/64)
                                            temp_num_2_1 = temp_num_2_0%64
                                            temp_num_2_0 = int((temp_num_2_0-temp_num_2_1)/64)
                                            temp_num_2_0 = (temp_num_2_0+init_num_0)%64
                                            temp_num_0 += temp_num_2_0
                                            out_num_str = out_num_str+long_digits[temp_num_2_0]
                                            temp_num_2_1 = (temp_num_2_1-init_num_1)%64
                                            temp_num_0 += temp_num_2_1
                                            out_num_str = out_num_str+long_digits[temp_num_2_1]
                                            temp_num_2_2 = (temp_num_2_2+init_num_2)%64
                                            temp_num_0 += temp_num_2_2
                                            out_num_str = out_num_str+long_digits[temp_num_2_2]
                                            temp_num_2_3 = (temp_num_2_3-init_num_0)%64
                                            temp_num_0 += temp_num_2_3
                                            out_num_str = out_num_str+long_digits[temp_num_2_3]
                                            temp_runif = 1.0
                                            while temp_runif == 1.0:
                                                temp_runif = uniform(0.0, 1.0)
                                            temp_num_2_1 = int(temp_runif*2579)
                                            if temp_num_2_1 == 2579:
                                                temp_num_2_1 -= 1
                                            temp_num_2_2 = temp_hour
                                            temp_num_2_2 = temp_num_2_2*27+temp_gn_1
                                            temp_num_2_2 = temp_num_2_2*10+temp_year_0
                                            temp_num_2 = temp_num_2_2+temp_num_2_1*6481
                                            temp_num_2_3 = temp_num_2%64
                                            temp_num_2_0 = int((temp_num_2-temp_num_2_3)/64)
                                            temp_num_2_2 = temp_num_2_0%64
                                            temp_num_2_0 = int((temp_num_2_0-temp_num_2_2)/64)
                                            temp_num_2_1 = temp_num_2_0%64
                                            temp_num_2_0 = int((temp_num_2_0-temp_num_2_1)/64)
                                            temp_num_2_0 = (temp_num_2_0+init_num_1)%64
                                            temp_num_0 += temp_num_2_0
                                            out_num_str = out_num_str+long_digits[temp_num_2_0]
                                            temp_num_2_1 = (temp_num_2_1-init_num_2)%64
                                            temp_num_0 += temp_num_2_1
                                            out_num_str = out_num_str+long_digits[temp_num_2_1]
                                            temp_num_2_2 = (temp_num_2_2+init_num_0)%64
                                            temp_num_0 += temp_num_2_2
                                            out_num_str = out_num_str+long_digits[temp_num_2_2]
                                            temp_num_2_3 = (temp_num_2_3-init_num_1)%64
                                            temp_num_0 += temp_num_2_3
                                            out_num_str = out_num_str+long_digits[temp_num_2_3]
                                            temp_runif = 1.0
                                            while temp_runif == 1.0:
                                                temp_runif = uniform(0.0, 1.0)
                                            temp_num_2_1 = int(temp_runif*6173)
                                            if temp_num_2_1 == 6173:
                                                temp_num_2_1 -= 1
                                            temp_num_2_2 = temp_year_3
                                            temp_num_2_2 = temp_num_2_2*10+temp_year_1
                                            temp_num_2_2 = temp_num_2_2*27+temp_fn_1
                                            temp_num_2 = temp_num_2_2+temp_num_2_1*2707
                                            temp_num_2_3 = temp_num_2%64
                                            temp_num_2_0 = int((temp_num_2-temp_num_2_3)/64)
                                            temp_num_2_2 = temp_num_2_0%64
                                            temp_num_2_0 = int((temp_num_2_0-temp_num_2_2)/64)
                                            temp_num_2_1 = temp_num_2_0%64
                                            temp_num_2_0 = int((temp_num_2_0-temp_num_2_1)/64)
                                            temp_num_2_0 = (temp_num_2_0+init_num_2)%64
                                            temp_num_0 += temp_num_2_0
                                            out_num_str = out_num_str+long_digits[temp_num_2_0]
                                            temp_num_2_1 = (temp_num_2_1-init_num_0)%64
                                            temp_num_0 += temp_num_2_1
                                            out_num_str = out_num_str+long_digits[temp_num_2_1]
                                            temp_num_2_2 = (temp_num_2_2+init_num_1)%64
                                            temp_num_0 += temp_num_2_2
                                            out_num_str = out_num_str+long_digits[temp_num_2_2]
                                            temp_num_2_3 = (temp_num_2_3-init_num_2)%64
                                            temp_num_0 += temp_num_2_3
                                            out_num_str = out_num_str+long_digits[temp_num_2_3]
                                            temp_runif = 1.0
                                            while temp_runif == 1.0:
                                                temp_runif = uniform(0.0, 1.0)
                                            temp_num_2_1 = int(temp_runif*48049)
                                            if temp_num_2_1 == 48049:
                                                temp_num_2_1 -= 1
                                            temp_num_2_2 = (temp_month-1)
                                            temp_num_2_2 = temp_num_2_2*31+(temp_day-1)
                                            temp_num_2_2 = temp_num_2_2*60+temp_minute
                                            temp_num_2 = temp_num_2_2+temp_num_2_1*22343
                                            temp_num_2_4 = temp_num_2%64
                                            temp_num_2_0 = int((temp_num_2-temp_num_2_4)/64)
                                            temp_num_2_3 = temp_num_2_0%64
                                            temp_num_2_0 = int((temp_num_2_0-temp_num_2_3)/64)
                                            temp_num_2_2 = temp_num_2_0%64
                                            temp_num_2_0 = int((temp_num_2_0-temp_num_2_2)/64)
                                            temp_num_2_1 = temp_num_2_0%64
                                            temp_num_2_0 = int((temp_num_2_0-temp_num_2_1)/64)
                                            temp_num_2_0 = (temp_num_2_0+init_num_0)%64
                                            temp_num_0 += temp_num_2_0
                                            out_num_str = out_num_str+long_digits[temp_num_2_0]
                                            temp_num_2_1 = (temp_num_2_1-init_num_1)%64
                                            temp_num_0 += temp_num_2_1
                                            out_num_str = out_num_str+long_digits[temp_num_2_1]
                                            temp_num_2_2 = (temp_num_2_2+init_num_2)%64
                                            temp_num_0 += temp_num_2_2
                                            out_num_str = out_num_str+long_digits[temp_num_2_2]
                                            temp_num_2_3 = (temp_num_2_3-init_num_0)%64
                                            temp_num_0 += temp_num_2_3
                                            out_num_str = out_num_str+long_digits[temp_num_2_3]
                                            temp_num_2_4 = (temp_num_2_4+init_num_1)%64
                                            temp_num_0 += temp_num_2_4
                                            out_num_str = out_num_str+long_digits[temp_num_2_4]
                                            out_num_str = out_num_str+long_digits[temp_num_0%64]
                                            temp_str_4 = str(temp_year_0)+str(temp_year_1)+str(temp_year_2)+str(temp_year_3)
                                            temp_str_4 = temp_str_4+"-"
                                            if temp_month < 10:
                                                temp_str_4 = temp_str_4+"0"+str(temp_month)
                                            else:
                                                temp_str_4 = temp_str_4+str(temp_month)
                                            temp_str_4 = temp_str_4+"-"
                                            if temp_day < 10:
                                                temp_str_4 = temp_str_4+"0"+str(temp_day)
                                            else:
                                                temp_str_4 = temp_str_4+str(temp_day)
                                            temp_str_5 = ""
                                            if temp_hour < 10:
                                                temp_str_5 = temp_str_5+"0"+str(temp_hour)
                                            else:
                                                temp_str_5 = temp_str_5+str(temp_hour)
                                            temp_str_5 = temp_str_5+":"
                                            if temp_minute < 10:
                                                temp_str_5 = temp_str_5+"0"+str(temp_minute)
                                            else:
                                                temp_str_5 = temp_str_5+str(temp_minute)
                                            out_result.append([out_num_str, temp_gn_str, temp_fn_str, temp_gn_1 != 0, temp_str_4, temp_str_5])                            
                                        else:
                                            out_result.append(None)
                                    else:
                                        out_result.append(None)
                                else:
                                    out_result.append(None)
                            else:
                                out_result.append(None)
                            if self.cur_multi_gene_bool:
                                temp_show_num = n+1
                                temp_show_float = (temp_show_num/temp_len)*100
                                temp_show_str_0 = str(temp_show_num)+"/"+str(temp_len)
                                temp_show_str_1 = str(round(temp_show_float, 2))+"%"
                                self.gene_multiple_gene_state_1_0["text"] = temp_show_str_0
                                self.gene_multiple_gene_state_1_1["text"] = temp_show_str_1
                                self.gene_multiple_gene_progressbar_1["value"] = int(temp_show_float)
                                self.update()
                        else:
                            break
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        if not temp_bool_0:
            out_result = None
        return out_result
    
    def num_mix_valid(self, 
                      mix_number, given_name = None, family_name = None, 
                      year = None, month = None, day = None, 
                      hour = None, minute = None):
        # check validation of mixed number
        
        # input: mix_number, string of length 21
        #        given_name, string
        #        family_name, string
        #        year, integer
        #        month, integer
        #        day, integer
        #        hour, integer
        #        minute, integer
        
        # output: bool
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        English_name_capital = ("A", "B", "C", "D", "E", "F", "G", 
                                "H", "I", "J", "K", "L", "M", "N", 
                                "O", "P", "Q", "R", "S", "T", 
                                "U", "V", "W", "X", "Y", "Z")
        English_name_other = (" ", "-", "'")
        out_bool = True
        if isinstance(mix_number, str):
            mix_number = mix_number.strip()
            if len(mix_number) == 21:
                init_str_0 = mix_number[0]
                init_str_1 = mix_number[1]
                init_str_2 = mix_number[2]
                if ((init_str_0.upper() in English_name_capital) & 
                    (init_str_1.upper() in English_name_capital) & 
                    (init_str_2.upper() in English_name_capital)):
                    temp_number_list = []
                    temp_num_1 = 0
                    temp_num_0 = -1
                    for n1 in range(64):
                        if long_digits[n1] == init_str_0:
                            temp_num_0 = n1
                            break
                    init_num_0 = temp_num_0
                    temp_num_1 += temp_num_0
                    temp_number_list.append(temp_num_0)
                    temp_num_0 = -1
                    for n1 in range(64):
                        if long_digits[n1] == init_str_1:
                            temp_num_0 = n1
                            break
                    init_num_1 = temp_num_0
                    temp_num_1 += temp_num_0
                    temp_number_list.append(temp_num_0)
                    temp_num_0 = -1
                    for n1 in range(64):
                        if long_digits[n1] == init_str_2:
                            temp_num_0 = n1
                            break
                    init_num_2 = temp_num_0
                    temp_num_1 += temp_num_0
                    temp_number_list.append(temp_num_0)
                    temp_num_2 = 0
                    for n in range(3, 21):
                        temp_num_0 = -1
                        temp_str_0 = mix_number[n]
                        for n1 in range(64):
                            if long_digits[n1] == temp_str_0:
                                temp_num_0 = n1
                                break
                        if temp_num_0 >= 0:
                            temp_number_list.append(temp_num_0)
                            if n < 20:                            
                                temp_num_1 += temp_num_0
                            else:
                                temp_num_2 += temp_num_0
                        else:
                            out_bool = False
                            break
                    if out_bool:
                        out_bool = temp_num_1%64 == temp_num_2
                else:
                    out_bool = False
            else:
                out_bool = False
        else:
            out_bool = False    
        if out_bool:
            temp_num_0 = (temp_number_list[3]-init_num_0)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[4]+init_num_1)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[5]-init_num_2)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[6]+init_num_0)%64
            temp_num_0 = temp_num_0%7297
            temp_num_1_2 = temp_num_0%27
            temp_num_1_0 = int((temp_num_0-temp_num_1_2)/27)
            temp_num_1_1 = temp_num_1_0%27
            temp_num_1_0 = int((temp_num_1_0-temp_num_1_1)/27)
            temp_num_0 = (temp_number_list[7]-init_num_1)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[8]+init_num_2)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[9]-init_num_0)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[10]+init_num_1)%64
            temp_num_0 = temp_num_0%6481
            temp_num_2_2 = temp_num_0%10
            temp_num_2_0 = int((temp_num_0-temp_num_2_2)/10)
            temp_num_2_1 = temp_num_2_0%27
            temp_num_2_0 = int((temp_num_2_0-temp_num_2_1)/27)
            temp_num_0 = (temp_number_list[11]-init_num_2)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[12]+init_num_0)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[13]-init_num_1)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[14]+init_num_2)%64
            temp_num_0 = temp_num_0%2707
            temp_num_3_2 = temp_num_0%27
            temp_num_3_0 = int((temp_num_0-temp_num_3_2)/27)
            temp_num_3_1 = temp_num_3_0%10
            temp_num_3_0 = int((temp_num_3_0-temp_num_3_1)/10)
            temp_num_0 = (temp_number_list[15]-init_num_0)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[16]+init_num_1)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[17]-init_num_2)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[18]+init_num_0)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[19]-init_num_1)%64
            temp_num_0 = temp_num_0%22343
            temp_num_4_2 = temp_num_0%60
            temp_num_4_0 = int((temp_num_0-temp_num_4_2)/60)
            temp_num_4_1 = temp_num_4_0%31
            temp_num_4_0 = int((temp_num_4_0-temp_num_4_1)/31)
            if (temp_num_2_0 >= 0) & (temp_num_2_0 < 24):
                if (temp_num_4_2 >= 0) & (temp_num_4_2 < 60):
                    if ((temp_num_1_0 >= 0) & (temp_num_1_0 <= 9) & 
                        (temp_num_2_2 >= 0) & (temp_num_2_2 <= 9) & 
                        (temp_num_3_0 >= 0) & (temp_num_3_0 <= 9) & 
                        (temp_num_3_1 >= 0) & (temp_num_3_1 <= 9)):
                        temp_num_1 = temp_num_2_2
                        temp_num_1 = temp_num_1*10+temp_num_3_1
                        temp_num_1 = temp_num_1*10+temp_num_1_0
                        temp_num_1 = temp_num_1*10+temp_num_3_0
                        temp_num_2 = temp_num_4_0+1
                        if (temp_num_2 > 0) & (temp_num_2 <= 12):
                            temp_num_3 = temp_num_4_1+1
                            if temp_num_2 in (1, 3, 5, 7, 8, 10, 12):
                                out_bool = (temp_num_3 > 0) & (temp_num_3 <= 31)
                            elif temp_num_2 in (4, 6, 9, 11):
                                out_bool = (temp_num_3 > 0) & (temp_num_3 <= 30)
                            else:
                                if temp_num_1%400 == 0:
                                    out_bool = (temp_num_3 > 0) & (temp_num_3 <= 29)
                                elif temp_num_1%100 == 0:
                                    out_bool = (temp_num_3 > 0) & (temp_num_3 <= 28)
                                elif temp_num_1%4 == 0:
                                    out_bool = (temp_num_3 > 0) & (temp_num_3 <= 29)
                                else:
                                    out_bool = (temp_num_3 > 0) & (temp_num_3 <= 28)
                        else:
                            out_bool = False
                    else:
                        out_bool = False
                else:
                    out_bool = False
            else:
                out_bool = False
        if out_bool:
            if not year is None:
                out_bool = year == temp_num_1
        if out_bool:
            if not month is None:
                out_bool = month == temp_num_2
        if out_bool:
            if not day is None:
                out_bool = day == temp_num_3
        if out_bool:
            if not hour is None:
                out_bool = hour == temp_num_2_0
        if out_bool:
            if not minute is None:
                out_bool = minute == temp_num_4_2
        if out_bool:
            if not given_name is None:
                if isinstance(given_name, str):
                    given_name = given_name.strip()
                    temp_len = len(given_name)
                    if temp_len == 0:
                        out_bool = (temp_num_1_2 == 0) & (temp_num_2_1 == 0)
                    elif temp_len == 1:
                        temp_num_1 = 0
                        temp_str_1 = given_name[0]
                        for n in range(26):
                            if temp_str_1 == English_name_capital[n]:
                                temp_num_1 = n+1
                                break
                        if temp_num_1 > 0:
                            if temp_num_1 == temp_num_2_1:
                                out_bool = temp_num_1_2 == 0
                            else:
                                out_bool = False
                        else:
                            out_bool = False
                    else:
                        temp_num_1 = 0
                        temp_str_1 = given_name[0]
                        for n in range(26):
                            if temp_str_1 == English_name_capital[n]:
                                temp_num_1 = n+1
                                break
                        if temp_num_1 > 0:
                            if temp_num_1 == temp_num_2_1:
                                temp_num_2 = 0
                                temp_str_2 = given_name[1].upper()
                                for n in range(26):
                                    if temp_str_2 == English_name_capital[n]:
                                        temp_num_2 = n+1
                                        break
                                if temp_num_2 > 0:
                                    out_bool = temp_num_1_2 == temp_num_2
                                elif temp_str_2 in English_name_other:
                                    out_bool = temp_num_1_2 == 0
                                else:
                                    out_bool = False
                            else:
                                out_bool = False
                        else:
                            out_bool = False
                else:
                    out_bool = False
        if out_bool:
            if not family_name is None:
                if isinstance(family_name, str):
                    family_name = family_name.strip()
                    temp_len = len(family_name)
                    if temp_len == 0:
                        out_bool = (temp_num_1_1 == 0) & (temp_num_3_2 == 0)
                    elif temp_len == 1:
                        temp_num_1 = 0
                        temp_str_1 = family_name[0]
                        for n in range(26):
                            if temp_str_1 == English_name_capital[n]:
                                temp_num_1 = n+1
                                break
                        if temp_num_1 > 0:
                            if temp_num_1 == temp_num_3_2:
                                out_bool = temp_num_1_1 == 0
                            else:
                                out_bool = False
                        else:
                            out_bool = False
                    else:
                        temp_num_1 = 0
                        temp_str_1 = family_name[0]
                        for n in range(26):
                            if temp_str_1 == English_name_capital[n]:
                                temp_num_1 = n+1
                                break
                        if temp_num_1 > 0:
                            if temp_num_1 == temp_num_3_2:
                                temp_num_2 = 0
                                temp_str_2 = family_name[1].upper()
                                for n in range(26):
                                    if temp_str_2 == English_name_capital[n]:
                                        temp_num_2 = n+1
                                        break
                                if temp_num_2 > 0:
                                    out_bool = temp_num_1_1 == temp_num_2
                                elif temp_str_2 in English_name_other:
                                    out_bool = temp_num_1_1 == 0
                                else:
                                    out_bool = False
                            else:
                                out_bool = False
                        else:
                            out_bool = False
                else:
                    out_bool = False
        return out_bool
    
    def num_mix_64_2_8(self, mix_number):
        # input: mix_number, string of length 21
        
        # output: mix_number, string of length 42
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        oct_digits = ("0", "1", "2", "3", "4", "5", "6", "7")
        out_str = ""
        if isinstance(mix_number, str):
            mix_number = mix_number.strip()
            if len(mix_number) == 21:
                temp_bool_0 = True
                temp_number_list = []
                for n in range(21):
                    temp_num_0 = -1
                    temp_str_0 = mix_number[n]
                    for n1 in range(64):
                        if long_digits[n1] == temp_str_0:
                            temp_num_0 = n1
                            break
                    if temp_num_0 >= 0:
                        temp_number_list.append(temp_num_0)
                    else:
                        temp_bool_0 = False
                if temp_bool_0:
                    temp_number_list_1 = []
                    for n in range(21):
                        temp_num_1 = temp_number_list[n]%8
                        temp_num_0 = int((temp_number_list[n]-temp_num_1)/8)
                        temp_number_list_1.append(temp_num_0)
                        temp_number_list_1.append(temp_num_1)
                    for n in range(len(temp_number_list_1)):
                        out_str = out_str+oct_digits[temp_number_list_1[n]]
                else:
                    out_str = None
            else:
                out_str = None
        else:
            out_str = None
        return out_str
    
    def num_mix_8_2_64(self, mix_number):
        # input: mix_number, string of length 42
        
        # output: mix_number, string of length 21
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        oct_digits = ("0", "1", "2", "3", "4", "5", "6", "7")
        out_str = ""
        if isinstance(mix_number, str):
            mix_number = mix_number.strip()
            if len(mix_number) == 42:
                temp_bool_0 = True
                temp_number_list = []
                for n in range(42):
                    temp_num_0 = -1
                    temp_str_0 = mix_number[n]
                    for n1 in range(8):
                        if oct_digits[n1] == temp_str_0:
                            temp_num_0 = n1
                            break
                    if temp_num_0 >= 0:
                        temp_number_list.append(temp_num_0)
                    else:
                        temp_bool_0 = False
                if temp_bool_0:
                    temp_number_list_1 = []
                    for n in range(21):
                        temp_num_0 = temp_number_list[2*n]*8+temp_number_list[2*n+1]
                        temp_number_list_1.append(temp_num_0)
                    for n in range(len(temp_number_list_1)):
                        out_str = out_str+long_digits[temp_number_list_1[n]]
                else:
                    out_str = None
            else:
                out_str = None
        else:
            out_str = None
        return out_str
    
    def number_organization_generate(self, in_list_name, in_initial_list):
        # to generate organization number, 14 digits
        
        # input:
        # in_list_name = [organization name 0 (str) / None, 
        #                 organization name 1 (str) / None, 
        #                 organization name 2 (str) / None, ...]
        # in_initial_list = [*, *, *]
        #                   each of the *s is from 26 letters
        
        # output:
        # out_result = [(out number 0, organization name 0, 
        #                Date-UTC 0, Time-UTC 0) / None,
        #               (out number 1, organization name 1, 
        #                Date-UTC 1, Time-UTC 1) / None,
        #               (out number 2, organization name 2, 
        #                Date-UTC 2, Time-UTC 2) / None, ...]
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        English_name_capital = ("A", "B", "C", "D", "E", "F", "G", 
                                "H", "I", "J", "K", "L", "M", "N", 
                                "O", "P", "Q", "R", "S", "T", 
                                "U", "V", "W", "X", "Y", "Z")
        English_name_capital_1 = ("A", "B", "C", "D", "E", "F", "G", 
                                  "H", "I", "J", "K", "L", "M", "N", 
                                  "O", "P", "Q", "R", "S", "T", 
                                  "U", "V", "W", "X", "Y", "Z", 
                                  "0", "1", "2", "3", "4", 
                                  "5", "6", "7", "8", "9")
        English_name_other = (" ", "-", "'", "‘", "’", "&", 
                              "/", ".", ":", "(", ")")
        temp_bool_0 = True
        if isinstance(in_initial_list, list) | isinstance(in_initial_list, tuple):
            if len(in_initial_list) == 3:
                init_char_0 = in_initial_list[0]
                init_char_1 = in_initial_list[1]
                init_char_2 = in_initial_list[2]
                if (isinstance(init_char_0, str) & isinstance(init_char_1, str) &
                    isinstance(init_char_2, str)):
                    init_char_0 = init_char_0.strip().upper()
                    init_char_1 = init_char_1.strip().upper()
                    init_char_2 = init_char_2.strip().upper()
                    if ((init_char_0 in English_name_capital) & (init_char_1 in English_name_capital) & 
                        (init_char_2 in English_name_capital)):
                        first_3_digits = (init_char_0.lower()+init_char_1.lower()+init_char_2.lower(), 
                                          init_char_0.lower()+init_char_1.lower()+init_char_2, 
                                          init_char_0.lower()+init_char_1+init_char_2.lower(), 
                                          init_char_0.lower()+init_char_1+init_char_2, 
                                          init_char_0+init_char_1.lower()+init_char_2.lower(), 
                                          init_char_0+init_char_1.lower()+init_char_2, 
                                          init_char_0+init_char_1+init_char_2.lower(), 
                                          init_char_0+init_char_1+init_char_2)
                    else:
                        temp_bool_0 = False
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
        out_result = []
        if temp_bool_0:
            if isinstance(in_list_name, list) | isinstance(in_list_name, tuple):
                temp_len = len(in_list_name)
                if temp_len > 0:
                    temp_time_now = datetime.utcnow()
                    temp_num_0 = temp_time_now.microsecond
                    temp_num_0 = temp_num_0*60+temp_time_now.second
                    temp_num_0 = temp_num_0*60+temp_time_now.minute
                    temp_num_0 = temp_num_0*24+temp_time_now.hour
                    seed(temp_num_0)
                    for n in range(temp_len):
                        if self.cur_progress_bool:
                            temp_bool_1 = True
                            if in_list_name[n] is None:
                                out_result.append(None)
                            elif isinstance(in_list_name[n], str):
                                temp_on_str = in_list_name[n].strip()
                                temp_len = len(temp_on_str)
                                if temp_len == 0:
                                    temp_bool_1 = False
                                elif temp_len == 1:  
                                    temp_num_1 = 0
                                    temp_str_1 = in_list_name[n][0]
                                    for n2 in range(36):
                                        if English_name_capital_1[n2] == temp_str_1:
                                            temp_num_1 = n2+1
                                            break
                                    if temp_num_1 < 1:
                                        temp_bool_1 = False
                                else:
                                    temp_num_1 = 0
                                    temp_str_1 = in_list_name[n][0]
                                    for n2 in range(36):
                                        if English_name_capital_1[n2] == temp_str_1:
                                            temp_num_1 = n2+1
                                            break
                                    if temp_num_1 > 0:
                                        for n1 in range(1, temp_len):
                                            temp_num_2 = 0
                                            temp_str_2 = in_list_name[n][n1].upper()
                                            for n2 in range(36):
                                                if English_name_capital_1[n2] == temp_str_2:
                                                    temp_num_2 = n2+1
                                                    break
                                            if temp_num_2 < 1:
                                                if not temp_str_2 in English_name_other:
                                                    temp_bool_1 = False
                                                    break
                                    else:
                                        temp_bool_1 = False
                                if temp_bool_1:
                                    temp_time_now = datetime.utcnow()
                                    temp_year = temp_time_now.year
                                    temp_year_3 = temp_year%10
                                    temp_year_0 = int((temp_year-temp_year_3)/10)
                                    temp_year_2 = temp_year_0%10
                                    temp_year_0 = int((temp_year_0-temp_year_2)/10)
                                    temp_year_1 = temp_year_0%10
                                    temp_year_0 = int((temp_year_0-temp_year_1)/10)
                                    temp_month = temp_time_now.month
                                    temp_day = temp_time_now.day
                                    temp_hour = temp_time_now.hour
                                    temp_minute = temp_time_now.minute
                                    temp_num_0 = 0
                                    temp_runif = 1.0
                                    while temp_runif == 1.0:
                                        temp_runif = uniform(0.0, 1.0)
                                    temp_num_1_0 = int(temp_runif*8)
                                    if temp_num_1_0 == 8:
                                        temp_num_1_0 -= 1
                                    out_num_str = first_3_digits[temp_num_1_0]
                                    temp_str_3 = out_num_str[0]
                                    temp_num_1_1 = -1
                                    for n2 in range(64):
                                        if long_digits[n2] == temp_str_3:
                                            temp_num_1_1 = n2
                                            break
                                    init_num_0 = temp_num_1_1
                                    temp_num_0 += temp_num_1_1
                                    temp_str_3 = out_num_str[1]
                                    temp_num_1_1 = -1
                                    for n2 in range(64):
                                        if long_digits[n2] == temp_str_3:
                                            temp_num_1_1 = n2
                                            break
                                    init_num_1 = temp_num_1_1
                                    temp_num_0 += temp_num_1_1
                                    temp_str_3 = out_num_str[2]
                                    temp_num_1_1 = -1
                                    for n2 in range(64):
                                        if long_digits[n2] == temp_str_3:
                                            temp_num_1_1 = n2
                                            break
                                    init_num_2 = temp_num_1_1
                                    temp_num_0 += temp_num_1_1 
                                    temp_runif = 1.0
                                    while temp_runif == 1.0:
                                        temp_runif = uniform(0.0, 1.0)
                                    temp_num_2_1 = int(temp_runif*89)
                                    if temp_num_2_1 == 89:
                                        temp_num_2_1 -= 1
                                    temp_num_2_2 = temp_year_1
                                    temp_num_2_2 = temp_num_2_2*24+temp_hour
                                    temp_num_2_2 = temp_num_2_2*12+(temp_month-1)
                                    temp_num_2 = temp_num_2_2+temp_num_2_1*2887
                                    temp_num_2_2 = temp_num_2%64
                                    temp_num_2_0 = int((temp_num_2-temp_num_2_2)/64)
                                    temp_num_2_1 = temp_num_2_0%64
                                    temp_num_2_0 = int((temp_num_2_0-temp_num_2_1)/64)
                                    temp_num_2_0 = (temp_num_2_0+init_num_0)%64
                                    temp_num_0 += temp_num_2_0
                                    out_num_str = out_num_str+long_digits[temp_num_2_0]
                                    temp_num_2_1 = (temp_num_2_1-init_num_1)%64
                                    temp_num_0 += temp_num_2_1
                                    out_num_str = out_num_str+long_digits[temp_num_2_1]
                                    temp_num_2_2 = (temp_num_2_2+init_num_2)%64
                                    temp_num_0 += temp_num_2_2
                                    out_num_str = out_num_str+long_digits[temp_num_2_2]
                                    temp_runif = 1.0
                                    while temp_runif == 1.0:
                                        temp_runif = uniform(0.0, 1.0)
                                    temp_num_2_1 = int(temp_runif*5393)
                                    if temp_num_2_1 == 5393:
                                        temp_num_2_1 -= 1
                                    temp_num_2_2 = temp_day-1
                                    temp_num_2_2 = temp_num_2_2*10+temp_year_0
                                    temp_num_2_2 = temp_num_2_2*10+temp_year_2
                                    temp_num_2 = temp_num_2_2+temp_num_2_1*3109
                                    temp_num_2_3 = temp_num_2%64
                                    temp_num_2_0 = int((temp_num_2-temp_num_2_3)/64)
                                    temp_num_2_2 = temp_num_2_0%64
                                    temp_num_2_0 = int((temp_num_2_0-temp_num_2_2)/64)
                                    temp_num_2_1 = temp_num_2_0%64
                                    temp_num_2_0 = int((temp_num_2_0-temp_num_2_1)/64)
                                    temp_num_2_0 = (temp_num_2_0-init_num_0)%64
                                    temp_num_0 += temp_num_2_0
                                    out_num_str = out_num_str+long_digits[temp_num_2_0]
                                    temp_num_2_1 = (temp_num_2_1+init_num_1)%64
                                    temp_num_0 += temp_num_2_1
                                    out_num_str = out_num_str+long_digits[temp_num_2_1]
                                    temp_num_2_2 = (temp_num_2_2-init_num_2)%64
                                    temp_num_0 += temp_num_2_2
                                    out_num_str = out_num_str+long_digits[temp_num_2_2]
                                    temp_num_2_3 = (temp_num_2_3+init_num_0)%64
                                    temp_num_0 += temp_num_2_3
                                    out_num_str = out_num_str+long_digits[temp_num_2_3]
                                    temp_runif = 1.0
                                    while temp_runif == 1.0:
                                        temp_runif = uniform(0.0, 1.0)
                                    temp_num_2_1 = int(temp_runif*433)
                                    if temp_num_2_1 == 433:
                                        temp_num_2_1 -= 1
                                    temp_num_2_2 = temp_minute
                                    temp_num_2_2 = temp_num_2_2*10+temp_year_3
                                    temp_num_2 = temp_num_2_2+temp_num_2_1*601
                                    temp_num_2_2 = temp_num_2%64
                                    temp_num_2_0 = int((temp_num_2-temp_num_2_2)/64)
                                    temp_num_2_1 = temp_num_2_0%64
                                    temp_num_2_0 = int((temp_num_2_0-temp_num_2_1)/64)
                                    temp_num_2_0 = (temp_num_2_0-init_num_1)%64
                                    temp_num_0 += temp_num_2_0
                                    out_num_str = out_num_str+long_digits[temp_num_2_0]
                                    temp_num_2_1 = (temp_num_2_1+init_num_2)%64
                                    temp_num_0 += temp_num_2_1
                                    out_num_str = out_num_str+long_digits[temp_num_2_1]
                                    temp_num_2_2 = (temp_num_2_2-init_num_0)%64
                                    temp_num_0 += temp_num_2_2
                                    out_num_str = out_num_str+long_digits[temp_num_2_2]
                                    out_num_str = out_num_str+long_digits[temp_num_0%64]
                                    temp_runif = 1.0
                                    temp_str_4 = str(temp_year_0)+str(temp_year_1)+str(temp_year_2)+str(temp_year_3)
                                    temp_str_4 = temp_str_4+"-"
                                    if temp_month < 10:
                                        temp_str_4 = temp_str_4+"0"+str(temp_month)
                                    else:
                                        temp_str_4 = temp_str_4+str(temp_month)
                                    temp_str_4 = temp_str_4+"-"
                                    if temp_day < 10:
                                        temp_str_4 = temp_str_4+"0"+str(temp_day)
                                    else:
                                        temp_str_4 = temp_str_4+str(temp_day)
                                    temp_str_5 = ""
                                    if temp_hour < 10:
                                        temp_str_5 = temp_str_5+"0"+str(temp_hour)
                                    else:
                                        temp_str_5 = temp_str_5+str(temp_hour)
                                    temp_str_5 = temp_str_5+":"
                                    if temp_minute < 10:
                                        temp_str_5 = temp_str_5+"0"+str(temp_minute)
                                    else:
                                        temp_str_5 = temp_str_5+str(temp_minute)
                                    out_result.append((out_num_str, temp_on_str, temp_str_4, temp_str_5))                            
                                else:
                                    out_result.append(None)
                            else:
                                out_result.append(None)
                        else:
                            break
                else:
                    temp_bool_0 = False
            else:
                temp_bool_0 = False
        if not temp_bool_0:
            out_result = None
        return out_result
    
    def num_organization_valid(self, 
                               organization_number, 
                               year = None, month = None, day = None, 
                               hour = None, minute = None):
        # check validation of mixed number
        
        # input: organization_number, string of length 14
        #        year, integer
        #        month, integer
        #        day, integer
        #        hour, integer
        #        minute, integer
        
        # output: bool
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        English_name_capital = ("A", "B", "C", "D", "E", "F", "G", 
                                "H", "I", "J", "K", "L", "M", "N", 
                                "O", "P", "Q", "R", "S", "T", 
                                "U", "V", "W", "X", "Y", "Z")        
        out_bool = True
        if isinstance(organization_number, str):
            organization_number = organization_number.strip()
            if len(organization_number) == 14:
                init_str_0 = organization_number[0]
                init_str_1 = organization_number[1]
                init_str_2 = organization_number[2]
                if ((init_str_0.upper() in English_name_capital) & 
                    (init_str_1.upper() in English_name_capital) & 
                    (init_str_2.upper() in English_name_capital)):
                    temp_number_list = []
                    temp_num_1 = 0
                    temp_num_0 = -1
                    for n1 in range(64):
                        if long_digits[n1] == init_str_0:
                            temp_num_0 = n1
                            break
                    init_num_0 = temp_num_0
                    temp_num_1 += temp_num_0
                    temp_number_list.append(temp_num_0)
                    temp_num_0 = -1
                    for n1 in range(64):
                        if long_digits[n1] == init_str_1:
                            temp_num_0 = n1
                            break
                    init_num_1 = temp_num_0
                    temp_num_1 += temp_num_0
                    temp_number_list.append(temp_num_0)
                    temp_num_0 = -1
                    for n1 in range(64):
                        if long_digits[n1] == init_str_2:
                            temp_num_0 = n1
                            break
                    init_num_2 = temp_num_0
                    temp_num_1 += temp_num_0
                    temp_number_list.append(temp_num_0)
                    temp_num_2 = 0
                    for n in range(3, 14):
                        temp_num_0 = -1
                        temp_str_0 = organization_number[n]
                        for n1 in range(64):
                            if long_digits[n1] == temp_str_0:
                                temp_num_0 = n1
                                break
                        if temp_num_0 >= 0:
                            temp_number_list.append(temp_num_0)
                            if n < 13:                            
                                temp_num_1 += temp_num_0
                            else:
                                temp_num_2 += temp_num_0
                        else:
                            out_bool = False
                            break
                    if out_bool:
                        out_bool = temp_num_1%64 == temp_num_2
                else:
                    out_bool = False
            else:
                out_bool = False
        else:
            out_bool = False  
        if out_bool:
            temp_num_0 = (temp_number_list[3]-init_num_0)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[4]+init_num_1)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[5]-init_num_2)%64
            temp_num_0 = temp_num_0%2887
            temp_num_1_2 = temp_num_0%12
            temp_num_1_0 = int((temp_num_0-temp_num_1_2)/12)
            temp_num_1_1 = temp_num_1_0%24
            temp_num_1_0 = int((temp_num_1_0-temp_num_1_1)/24)
            temp_num_0 = (temp_number_list[6]+init_num_0)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[7]-init_num_1)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[8]+init_num_2)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[9]-init_num_0)%64
            temp_num_0 = temp_num_0%3109
            temp_num_2_2 = temp_num_0%10
            temp_num_2_0 = int((temp_num_0-temp_num_2_2)/10)
            temp_num_2_1 = temp_num_2_0%10
            temp_num_2_0 = int((temp_num_2_0-temp_num_2_1)/10)
            temp_num_0 = (temp_number_list[10]+init_num_1)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[11]-init_num_2)%64
            temp_num_0 = temp_num_0*64+(temp_number_list[12]+init_num_0)%64
            temp_num_0 = temp_num_0%601
            temp_num_3_1 = temp_num_0%10
            temp_num_3_0 = int((temp_num_0-temp_num_3_1)/10)    
            if (temp_num_1_1 >= 0) & (temp_num_1_1 < 24):
                if (temp_num_3_0 >= 0) & (temp_num_3_0 < 60):
                    if ((temp_num_1_0 >= 0) & (temp_num_1_0 <= 9) & 
                        (temp_num_2_1 >= 0) & (temp_num_2_1 <= 9) & 
                        (temp_num_2_2 >= 0) & (temp_num_2_2 <= 9) & 
                        (temp_num_3_1 >= 0) & (temp_num_3_1 <= 9)):
                        temp_num_1 = temp_num_2_1
                        temp_num_1 = temp_num_1*10+temp_num_1_0
                        temp_num_1 = temp_num_1*10+temp_num_2_2
                        temp_num_1 = temp_num_1*10+temp_num_3_1
                        temp_num_2 = temp_num_1_2+1
                        if (temp_num_2 > 0) & (temp_num_2 <= 12):
                            temp_num_3 = temp_num_2_0+1
                            if temp_num_2 in (1, 3, 5, 7, 8, 10, 12):
                                out_bool = (temp_num_3 > 0) & (temp_num_3 <= 31)
                            elif temp_num_2 in (4, 6, 9, 11):
                                out_bool = (temp_num_3 > 0) & (temp_num_3 <= 30)
                            else:
                                if temp_num_1%400 == 0:
                                    out_bool = (temp_num_3 > 0) & (temp_num_3 <= 29)
                                elif temp_num_1%100 == 0:
                                    out_bool = (temp_num_3 > 0) & (temp_num_3 <= 28)
                                elif temp_num_1%4 == 0:
                                    out_bool = (temp_num_3 > 0) & (temp_num_3 <= 29)
                                else:
                                    out_bool = (temp_num_3 > 0) & (temp_num_3 <= 28)
                        else:
                            out_bool = False
                    else:
                        out_bool = False
                else:
                    out_bool = False
            else:
                out_bool = False
        if out_bool:
            if not year is None:
                out_bool = year == temp_num_1
        if out_bool:
            if not month is None:
                out_bool = month == temp_num_2
        if out_bool:
            if not day is None:
                out_bool = day == temp_num_3
        if out_bool:
            if not hour is None:
                out_bool = hour == temp_num_1_1
        if out_bool:
            if not minute is None:
                out_bool = minute == temp_num_3_0
        return out_bool
    
    def num_organization_64_2_16(self, organization_number):
        # input: organization_number, string of length 14
        
        # output: organization_number, string of length 21
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        hex_digits = ("0", "1", "2", "3", "4", "5", "6", "7", 
                      "8", "9", "A", "B", "C", "D", "E", "F")
        out_str = ""
        if isinstance(organization_number, str):
            organization_number = organization_number.strip()
            if len(organization_number) == 14:
                temp_bool_0 = True
                temp_number_list = []
                for n in range(14):
                    temp_num_0 = -1
                    temp_str_0 = organization_number[n]
                    for n1 in range(64):
                        if long_digits[n1] == temp_str_0:
                            temp_num_0 = n1
                            break
                    if temp_num_0 >= 0:
                        temp_number_list.append(temp_num_0)
                    else:
                        temp_bool_0 = False
                if temp_bool_0:
                    temp_number_list_1 = []
                    for n in range(7):
                        temp_num_0 = temp_number_list[2*n]*64+temp_number_list[2*n+1]
                        temp_num_3 = temp_num_0%16
                        temp_num_0 = int((temp_num_0-temp_num_3)/16)
                        temp_num_2 = temp_num_0%16
                        temp_num_1 = int((temp_num_0-temp_num_2)/16)
                        temp_number_list_1.append(temp_num_1)
                        temp_number_list_1.append(temp_num_2)
                        temp_number_list_1.append(temp_num_3)
                    for n in range(len(temp_number_list_1)):
                        out_str = out_str+hex_digits[temp_number_list_1[n]]
                else:
                    out_str = None
            else:
                out_str = None
        else:
            out_str = None
        return out_str
    
    def num_organization_16_2_64(self, organization_number):
        # input: organization_number, string of length 21
        
        # output: organization_number, string of length 14
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        hex_digits = ("0", "1", "2", "3", "4", "5", "6", "7", 
                      "8", "9", "A", "B", "C", "D", "E", "F")
        out_str = ""
        if isinstance(organization_number, str):
            organization_number = organization_number.strip()
            if len(organization_number) == 21:
                temp_bool_0 = True
                temp_number_list = []
                for n in range(21):
                    temp_num_0 = -1
                    temp_str_0 = organization_number[n].upper()
                    for n1 in range(16):
                        if hex_digits[n1] == temp_str_0:
                            temp_num_0 = n1
                            break
                    if temp_num_0 >= 0:
                        temp_number_list.append(temp_num_0)
                    else:
                        temp_bool_0 = False
                if temp_bool_0:
                    temp_number_list_1 = []
                    for n in range(7):
                        temp_num_0 = temp_number_list[3*n]*256+temp_number_list[3*n+1]*16+temp_number_list[3*n+2]
                        temp_num_1 = temp_num_0%64
                        temp_num_0 = int((temp_num_0-temp_num_1)/64)
                        temp_number_list_1.append(temp_num_0)
                        temp_number_list_1.append(temp_num_1)
                    for n in range(len(temp_number_list_1)):
                        out_str = out_str+long_digits[temp_number_list_1[n]]
                else:
                    out_str = None
            else:
                out_str = None
        else:
            out_str = None
        return out_str
    
    def number_manipulation_generate(self, organization_number):
        # to generate manipulation number, 7 digits
        
        # input: organization_number, string of length 14    
        
        # output:
        # out_number, string of length 7
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        series_digits = ("5", "B", "7", "F", "0", "C", "2", "D", 
                         "E", "9", "3", "1", "4", "8", "6", "A")
        organization_number = organization_number.strip()    
        temp_bool = self.num_organization_valid(organization_number)
        if temp_bool:
            temp_number_list = []
            for n in range(14):
                temp_num_0 = -1
                temp_str_0 = organization_number[n]
                for n1 in range(64):
                    if long_digits[n1] == temp_str_0:
                        temp_num_0 = n1
                        break
                temp_number_list.append(temp_num_0)
            temp_num_1 = temp_number_list[0]+temp_number_list[4]+temp_number_list[8]
            temp_num_2 = temp_number_list[1]+temp_number_list[5]+temp_number_list[9]
            temp_num_3 = (temp_num_1+temp_num_2)%16
            out_num_str = series_digits[temp_num_3]
            temp_runif = 1.0
            while temp_runif == 1.0:
                temp_runif = uniform(0.0, 1.0)
            temp_num_1_0 = int(temp_runif*41)
            if temp_num_1_0 == 41:
                temp_num_1_0 -= 1
            temp_num_1_0 *= 97
            temp_num_3 = temp_num_1%5
            temp_num_4 = temp_num_2%19
            temp_num_5 = temp_num_3*19+temp_num_4+temp_num_1_0
            temp_num_3 = temp_num_5%16
            out_num_str = out_num_str+series_digits[temp_num_3]
            temp_num_5 = int((temp_num_5-temp_num_3)/16)
            temp_num_4 = temp_num_5%16
            out_num_str = out_num_str+series_digits[temp_num_4]
            temp_num_5 = int((temp_num_5-temp_num_4)/16)
            out_num_str = out_num_str+series_digits[temp_num_5]        
            temp_runif = 1.0
            while temp_runif == 1.0:
                temp_runif = uniform(0.0, 1.0)
            temp_num_1_0 = int(temp_runif*31)
            if temp_num_1_0 == 31:
                temp_num_1_0 -= 1
            temp_num_1_0*= 127
            temp_num_3 = temp_num_2%17
            temp_num_4 = temp_num_1%7
            temp_num_5 = temp_num_3*7+temp_num_4+temp_num_1_0
            temp_num_3 = temp_num_5%16
            out_num_str = out_num_str+series_digits[temp_num_3]
            temp_num_5 = int((temp_num_5-temp_num_3)/16)
            temp_num_4 = temp_num_5%16
            out_num_str = out_num_str+series_digits[temp_num_4]
            temp_num_5 = int((temp_num_5-temp_num_4)/16)
            out_num_str = out_num_str+series_digits[temp_num_5]
        else:
            out_num_str = None
        return out_num_str
    
    def number_manipulation_valid(self, manipulation_number, organization_number):
        # to generate manipulation number, 7 digits
        
        # input: manipulation_number, string of length 7
        #        organization_number, string of length 14
        
        # output: bool
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        series_digits = ("5", "B", "7", "F", "0", "C", "2", "D", 
                         "E", "9", "3", "1", "4", "8", "6", "A")
        if isinstance(manipulation_number, str) & isinstance(organization_number, str):
            manipulation_number = manipulation_number.strip()
            organization_number = organization_number.strip()
            out_bool = self.num_organization_valid(organization_number)
        else:
            out_bool = False
        if out_bool:
            if len(manipulation_number) == 7:
                temp_number_list_0 = []
                for n in range(7):
                    temp_num_0 = -1
                    temp_str_0 = manipulation_number[n]
                    for n1 in range(16):
                        if series_digits[n1] == temp_str_0:
                            temp_num_0 = n1
                            break
                    if temp_num_0 >= 0:                    
                        temp_number_list_0.append(temp_num_0)
                    else:
                        out_bool = False
                        break
                if out_bool: 
                    temp_number_list_1 = []
                    for n in range(14):
                        temp_num_0 = -1
                        temp_str_0 = organization_number[n]
                        for n1 in range(64):
                            if long_digits[n1] == temp_str_0:
                                temp_num_0 = n1
                                break
                        if temp_num_0 >= 0:                    
                            temp_number_list_1.append(temp_num_0)
                        else:
                            out_bool = False
                            break           
                if out_bool: 
                    temp_num_1 = temp_number_list_1[0]+temp_number_list_1[4]+temp_number_list_1[8]
                    temp_num_2 = temp_number_list_1[1]+temp_number_list_1[5]+temp_number_list_1[9]
                    if (temp_num_1+temp_num_2)%16 == temp_number_list_0[0]:
                        temp_num_3 = temp_number_list_0[3]
                        temp_num_3 = temp_num_3*16+temp_number_list_0[2]
                        temp_num_3 = temp_num_3*16+temp_number_list_0[1]
                        temp_num_3 = temp_num_3%97
                        temp_num_4 = temp_num_3%19
                        temp_num_3 = int((temp_num_3-temp_num_4)/19)
                        if (temp_num_1%5 == temp_num_3) & (temp_num_2%19 == temp_num_4):
                            temp_num_3 = temp_number_list_0[6]
                            temp_num_3 = temp_num_3*16+temp_number_list_0[5]
                            temp_num_3 = temp_num_3*16+temp_number_list_0[4]
                            temp_num_3 = temp_num_3%127
                            temp_num_4 = temp_num_3%7
                            temp_num_3 = int((temp_num_3-temp_num_4)/7)
                            out_bool = (temp_num_2%17 == temp_num_3) & (temp_num_1%7 == temp_num_4)
                        else:
                            out_bool = False
                    else:
                        out_bool = False
            else:
                out_bool = False
        return out_bool
    
    def number_member_generate(self, in_list_name):
        # to generate member number, 14 digits
        
        # input:
        # in_list_name = [[mixed number 0, 
        #                  given name 0, family name 0, 
        #                  virtual name 0, 
        #                  organization number 0, 
        #                  date 0, time 0] / None, 
        #                 [mixed number 1, 
        #                  given name 1, family name 1, 
        #                  virtual name 1, 
        #                  organization number 1, 
        #                  date 1, time 1] / None, 
        #                 [mixed number 2, 
        #                  given name 2, family name 2, 
        #                  virtual name 2, 
        #                  organization number 2, 
        #                  date 2, time 2] / None, ...]
        
        # output:
        # out_result = [(out number 0, mixed number 0, virtual name 0, organization number) / None,
        #               (out number 1, mixed number 1, virtual name 1, organization number) / None,
        #               (out number 2, mixed number 2, virtual name 2, organization number) / None, ...]
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        series_digits = ("5", "B", "7", "F", "0", "C", "2", "D", 
                         "E", "9", "3", "1", "4", "8", "6", "A")
        numeric_digits = ("0", "1", "2", "3", "4", 
                          "5", "6", "7", "8", "9")
        out_result = []
        if isinstance(in_list_name, list) | isinstance(in_list_name, tuple):
            temp_len = len(in_list_name)
            if temp_len > 0:
                temp_time_now = datetime.utcnow()
                temp_num_0 = temp_time_now.microsecond
                temp_num_0 = temp_num_0*60+temp_time_now.second
                temp_num_0 = temp_num_0*60+temp_time_now.minute
                temp_num_0 = temp_num_0*24+temp_time_now.hour
                seed(temp_num_0)
                for n in range(temp_len):
                    if self.cur_progress_bool:
                        temp_bool = True
                        if in_list_name[n] is None:
                            temp_bool = False
                        elif isinstance(in_list_name[n], list) | isinstance(in_list_name[n], tuple):
                            if len(in_list_name[n]) == 7:
                                if (isinstance(in_list_name[n][0], str) & isinstance(in_list_name[n][1], str) & 
                                    isinstance(in_list_name[n][2], str) & isinstance(in_list_name[n][3], str) & 
                                    isinstance(in_list_name[n][4], str) & isinstance(in_list_name[n][5], str) & 
                                    isinstance(in_list_name[n][6], str)):
                                    temp_list_0 = []
                                    for n1 in range(7):
                                        temp_list_0.append(in_list_name[n][n1].strip())
                                    if len(temp_list_0[5]) == 10:
                                        if ((temp_list_0[5][0] in numeric_digits) & (temp_list_0[5][1] in numeric_digits) & 
                                            (temp_list_0[5][2] in numeric_digits) & (temp_list_0[5][3] in numeric_digits) & 
                                            (temp_list_0[5][4] == "-") & (temp_list_0[5][5] in numeric_digits) & 
                                            (temp_list_0[5][6] in numeric_digits) & (temp_list_0[5][7] == "-") & 
                                            (temp_list_0[5][8] in numeric_digits) & (temp_list_0[5][9] in numeric_digits)):
                                            temp_num_1_0 = int(temp_list_0[5][0:4])
                                            temp_num_1_1 = int(temp_list_0[5][5:7])
                                            temp_num_1_2 = int(temp_list_0[5][8:10])          
                                        else:
                                            temp_bool = False
                                    else:
                                        temp_bool = False
                                    if temp_bool:
                                        if len(temp_list_0[6]) == 5:
                                            if ((temp_list_0[6][0] in numeric_digits) & (temp_list_0[6][1] in numeric_digits) & 
                                                (temp_list_0[6][2] == ":") & (temp_list_0[6][3] in numeric_digits) & 
                                                (temp_list_0[6][4] in numeric_digits)):
                                                temp_num_2_0 = int(temp_list_0[6][0:2])
                                                temp_num_2_1 = int(temp_list_0[6][3:5])        
                                            else:
                                                temp_bool = False
                                        else:
                                            temp_bool = False
                                    if temp_bool:
                                        if temp_list_0[0][:3].upper() == temp_list_0[4][:3].upper():
                                            if self.num_mix_valid(temp_list_0[0], temp_list_0[1], temp_list_0[2], 
                                                                  year = temp_num_1_0, month = temp_num_1_1, day = temp_num_1_2, 
                                                                  hour = temp_num_2_0, minute = temp_num_2_1):
                                                temp_bool = self.num_organization_valid(temp_list_0[4])                                             
                                            else:                                    
                                                temp_bool = False
                                        else:                                    
                                            temp_bool = False
                                    if temp_bool:
                                        temp_number_list_0 = []
                                        for n1 in range(21):
                                            temp_num_0 = -1
                                            temp_str_0 = temp_list_0[0][n1]
                                            for n2 in range(64):
                                                if long_digits[n2] == temp_str_0:
                                                    temp_num_0 = n2
                                                    break                  
                                            temp_number_list_0.append(temp_num_0)
                                        temp_number_list_1 = []
                                        for n1 in range(14):
                                            temp_num_0 = -1
                                            temp_str_0 = temp_list_0[4][n1]
                                            for n2 in range(64):
                                                if long_digits[n2] == temp_str_0:
                                                    temp_num_0 = n2
                                                    break                  
                                            temp_number_list_1.append(temp_num_0)
                                        temp_len_1 = len(temp_list_0[3])
                                        if temp_len_1 == 0:                                        
                                            if len(temp_list_0[1]) > 0:
                                                temp_str_vn = ""
                                                temp_num_1 = 0
                                                temp_num_2 = 0
                                            else:
                                                temp_bool = False
                                        else:
                                            temp_str_vn = ""
                                            for n1 in range(temp_len_1):
                                                temp_str_1 = temp_list_0[3][n1]
                                                temp_num_3 = ord(temp_str_1)
                                                if (temp_num_3 >= 32) & (temp_num_3 < 65536):
                                                    if not temp_str_1 in ("'", '"'):
                                                        temp_str_vn = temp_str_vn+temp_str_1
                                                    else:
                                                        temp_str_vn = temp_str_vn+"?"
                                                else:
                                                    temp_bool = False
                                                    break
                                            if temp_bool:                                            
                                                if temp_len_1 == 1:
                                                    temp_str_1 = temp_str_vn[0]
                                                    temp_num_3 = ord(temp_str_1)
                                                    temp_num_1 = temp_num_3%16
                                                    temp_num_3 = int((temp_num_3-temp_num_1)/16)
                                                    temp_num_1 = temp_num_3%16
                                                    temp_num_2 = 0
                                                else:
                                                    temp_str_1 = temp_str_vn[0]
                                                    temp_num_3 = ord(temp_str_1)
                                                    temp_num_1 = temp_num_3%16
                                                    temp_num_3 = int((temp_num_3-temp_num_1)/16)
                                                    temp_num_1 = temp_num_3%16
                                                    temp_str_2 = temp_str_vn[1]
                                                    temp_num_4 = ord(temp_str_2)
                                                    temp_num_2 = temp_num_4%16
                                        if temp_bool:
                                            temp_num_0 = 0
                                            out_num_str = ""
                                            temp_num_3 = (temp_number_list_0[0]+temp_number_list_0[4]+temp_number_list_0[8])%16
                                            temp_num_0 += temp_num_3
                                            out_num_str = out_num_str+series_digits[temp_num_3]
                                            temp_num_3 = (temp_number_list_0[1]+temp_number_list_0[5]+temp_number_list_0[9])%16
                                            temp_num_0 += temp_num_3
                                            out_num_str = out_num_str+series_digits[temp_num_3]
                                            temp_num_3 = (temp_number_list_0[2]+temp_number_list_0[6]+temp_number_list_0[10])%16
                                            temp_num_0 += temp_num_3
                                            out_num_str = out_num_str+series_digits[temp_num_3]
                                            temp_num_3 = (temp_number_list_0[3]+temp_number_list_0[7]+temp_number_list_0[11])%16
                                            temp_num_0 += temp_num_3
                                            out_num_str = out_num_str+series_digits[temp_num_3]
                                            temp_num_3 = (temp_number_list_1[3]+temp_number_list_1[7]+temp_number_list_1[11])%16
                                            temp_num_0 += temp_num_3
                                            out_num_str = out_num_str+series_digits[temp_num_3]
                                            temp_num_3 = (temp_number_list_1[2]+temp_number_list_1[6]+temp_number_list_1[10])%16
                                            temp_num_0 += temp_num_3
                                            out_num_str = out_num_str+series_digits[temp_num_3]
                                            temp_num_0 += temp_num_1
                                            out_num_str = out_num_str+series_digits[temp_num_1]
                                            temp_num_0 += temp_num_2
                                            out_num_str = out_num_str+series_digits[temp_num_2]
                                            temp_num_1 = (temp_num_2_0+temp_number_list_0[12])%29
                                            temp_num_2 = (temp_num_1_1-temp_number_list_0[14])%17
                                            temp_num_1 = temp_num_1*17+temp_num_2
                                            temp_num_2 = (temp_num_1_0%10+temp_number_list_0[15])%11
                                            temp_num_1 = temp_num_1*11+temp_num_2
                                            temp_num_2 = (temp_num_1_2-temp_number_list_0[13])%31
                                            temp_num_1 = temp_num_1*31+temp_num_2
                                            temp_runif = 1.0
                                            while temp_runif == 1.0:
                                                temp_runif = uniform(0.0, 1.0)
                                            temp_num_2 = int(temp_runif*6)
                                            if temp_num_2 == 6:
                                                temp_num_2 -= 1
                                            temp_num_2 *= 168127
                                            temp_num_1 += temp_num_2
                                            temp_num_5 = temp_num_1%16
                                            temp_num_1 = int((temp_num_1-temp_num_5)/16)
                                            temp_num_4 = temp_num_1%16
                                            temp_num_1 = int((temp_num_1-temp_num_4)/16)
                                            temp_num_3 = temp_num_1%16
                                            temp_num_1 = int((temp_num_1-temp_num_3)/16)
                                            temp_num_2 = temp_num_1%16
                                            temp_num_1 = int((temp_num_1-temp_num_2)/16)
                                            temp_num_0 += temp_num_1
                                            out_num_str = out_num_str+series_digits[temp_num_1]
                                            temp_num_0 += temp_num_2
                                            out_num_str = out_num_str+series_digits[temp_num_2]
                                            temp_num_0 += temp_num_3
                                            out_num_str = out_num_str+series_digits[temp_num_3]
                                            temp_num_0 += temp_num_4
                                            out_num_str = out_num_str+series_digits[temp_num_4]
                                            temp_num_0 += temp_num_5
                                            out_num_str = out_num_str+series_digits[temp_num_5]
                                            if len(temp_list_0[1]) > 0:
                                                out_num_str = out_num_str+series_digits[temp_num_0%15]
                                            else:
                                                out_num_str = out_num_str+series_digits[15]
                                else:
                                    temp_bool = False
                            else:
                                temp_bool = False
                        else:
                            temp_bool = False                
                        if temp_bool:
                            out_result.append([out_num_str, temp_list_0[0], temp_str_vn, temp_list_0[4]])
                        else:
                            out_result.append(None)
                        if self.cur_multi_gene_bool:
                            temp_show_num = n+1
                            temp_show_float = (temp_show_num/temp_len)*100
                            temp_show_str_0 = str(temp_show_num)+"/"+str(temp_len)
                            temp_show_str_1 = str(round(temp_show_float, 2))+"%"
                            self.gene_multiple_gene_state_2_0["text"] = temp_show_str_0
                            self.gene_multiple_gene_state_2_1["text"] = temp_show_str_1
                            self.gene_multiple_gene_progressbar_2["value"] = int(temp_show_float)
                            self.update()
                    else:
                        break
            else:
                out_result = None
        else:
            out_result = None
        return out_result    
    
    def num_member_valid(self, 
                         member_number, mix_number = None, 
                         virtual_name = None, organization_number = None):
        # check validation of mixed number
        
        # input: member_number, string of length 14
        #        mix_number, string of length 21
        #        virtual_name, string
        #        organization_number, string of length 14
        
        # output: bool
        
        long_digits = ("G", "B", "l", "A", "r", "s", "6", "X", 
                        "c", "K", "R", "Q", "I", "x", "h", "b", 
                        "i", "f", "o", "a", "M", "S", "w", "0", 
                        "P", "v", "3", "N", "t", "g", "8", "2",
                        "+", "-", "4", "k", "7", "e", "n", "D", 
                        "V", "y", "U", "W", "F", "L", "d", "T", 
                        "1", "J", "u", "Z", "z", "C", "Y", "9", 
                        "m", "H", "O", "E", "5", "p", "j", "q")
        series_digits = ("5", "B", "7", "F", "0", "C", "2", "D", 
                         "E", "9", "3", "1", "4", "8", "6", "A")
        out_bool = True
        if isinstance(member_number, str):
            member_number = member_number.strip()
            if len(member_number) == 14:
                temp_number_list = []
                temp_num_1 = 0
                temp_num_2 = 0
                for n in range(14):
                    temp_num_0 = -1
                    temp_str_0 = member_number[n]
                    for n1 in range(16):
                        if series_digits[n1] == temp_str_0:
                            temp_num_0 = n1
                            break
                    if temp_num_0 >= 0:
                        temp_number_list.append(temp_num_0)
                        if n < 13:                            
                            temp_num_1 += temp_num_0
                        else:
                            temp_num_2 += temp_num_0
                    else:
                        out_bool = False
                        break
                if out_bool:
                    if temp_number_list[13] != 15: 
                        out_bool = temp_num_1%15 == temp_num_2                
            else:
                out_bool = False
        else:
            out_bool = False
        if out_bool:
            if not mix_number is None:
                if self.num_mix_valid(mix_number):
                    mix_number = mix_number.strip()
                    temp_number_list_1 = []
                    for n in range(21):
                        temp_num_0 = -1
                        temp_str_0 = mix_number[n]
                        for n1 in range(64):
                            if long_digits[n1] == temp_str_0:
                                temp_num_0 = n1
                                break
                        temp_number_list_1.append(temp_num_0)
                    if (temp_number_list_1[0]+temp_number_list_1[4]+
                        temp_number_list_1[8])%16 != temp_number_list[0]:
                        out_bool = False
                    elif (temp_number_list_1[1]+temp_number_list_1[5]+
                          temp_number_list_1[9])%16 != temp_number_list[1]:
                        out_bool = False
                    elif (temp_number_list_1[2]+temp_number_list_1[6]+
                          temp_number_list_1[10])%16 != temp_number_list[2]:
                        out_bool = False
                    elif (temp_number_list_1[3]+temp_number_list_1[7]+
                          temp_number_list_1[11])%16 != temp_number_list[3]:
                        out_bool = False
                    else:
                        temp_num_0 = (temp_number_list_1[7]-temp_number_list_1[1])%64
                        temp_num_0 = temp_num_0*64+(temp_number_list_1[8]+temp_number_list_1[2])%64
                        temp_num_0 = temp_num_0*64+(temp_number_list_1[9]-temp_number_list_1[0])%64
                        temp_num_0 = temp_num_0*64+(temp_number_list_1[10]+temp_number_list_1[1])%64
                        temp_num_0 = temp_num_0%6481
                        temp_num_1 = int(temp_num_0/270)
                        temp_num_0 = (temp_number_list_1[11]-temp_number_list_1[2])%64
                        temp_num_0 = temp_num_0*64+(temp_number_list_1[12]+temp_number_list_1[0])%64
                        temp_num_0 = temp_num_0*64+(temp_number_list_1[13]-temp_number_list_1[1])%64
                        temp_num_0 = temp_num_0*64+(temp_number_list_1[14]+temp_number_list_1[2])%64
                        temp_num_0 = temp_num_0%2707
                        temp_num_2 = int(temp_num_0/270)
                        temp_num_0 = (temp_number_list_1[15]-temp_number_list_1[0])%64
                        temp_num_0 = temp_num_0*64+(temp_number_list_1[16]+temp_number_list_1[1])%64
                        temp_num_0 = temp_num_0*64+(temp_number_list_1[17]-temp_number_list_1[2])%64
                        temp_num_0 = temp_num_0*64+(temp_number_list_1[18]+temp_number_list_1[0])%64
                        temp_num_0 = temp_num_0*64+(temp_number_list_1[19]-temp_number_list_1[1])%64
                        temp_num_0 = temp_num_0%22343
                        temp_num_3 = int(temp_num_0/60)
                        temp_num_4 = temp_num_3%31
                        temp_num_3 = int((temp_num_3-temp_num_4)/31)
                        temp_num_1 = (temp_num_1+temp_number_list_1[12])%29
                        temp_num_2 = (temp_num_2+temp_number_list_1[15])%11
                        temp_num_3 = (temp_num_3+1-temp_number_list_1[14])%17
                        temp_num_4 = (temp_num_4+1-temp_number_list_1[13])%31
                        temp_num_5 = temp_number_list[8]
                        temp_num_5 = temp_num_5*16+temp_number_list[9]
                        temp_num_5 = temp_num_5*16+temp_number_list[10]
                        temp_num_5 = temp_num_5*16+temp_number_list[11]
                        temp_num_5 = temp_num_5*16+temp_number_list[12]
                        temp_num_5 = temp_num_5%168127
                        temp_num_6 = temp_num_5%31
                        if temp_num_6 == temp_num_4:                        
                            temp_num_5 = int((temp_num_5-temp_num_6)/31)
                            temp_num_6 = temp_num_5%11
                            if temp_num_6 == temp_num_2:
                                temp_num_5 = int((temp_num_5-temp_num_6)/11)
                                temp_num_6 = temp_num_5%17
                                if temp_num_6 == temp_num_3:
                                    temp_num_5 = int((temp_num_5-temp_num_6)/17)
                                    out_bool = temp_num_5 == temp_num_1
                                else:
                                    out_bool = False
                            else:
                                out_bool = False
                        else:
                            out_bool = False
                else:
                    out_bool = False
        if out_bool:
            if not virtual_name is None:
                if isinstance(virtual_name, str):
                    virtual_name = virtual_name.strip()
                    temp_len = len(virtual_name)
                    for n in range(temp_len):
                        temp_str_0 = virtual_name[0]
                        temp_num_0 = ord(temp_str_0)
                        if (temp_num_0 >= 32) & (temp_num_0 < 65536):                        
                            if temp_str_0 in ("'", '"'):
                                out_bool = False
                                break
                        else:
                            out_bool = False
                            break                
                    if out_bool:
                        if temp_len == 0:
                            if (temp_number_list[6] != 0) | (temp_number_list[7] != 0):
                                out_bool = False
                            elif temp_number_list[13] == 15:
                                out_bool = False
                        elif temp_len == 1:
                            temp_num_0 = ord(virtual_name[0])    
                            temp_num_1 = temp_num_0%16
                            temp_num_0 = int((temp_num_0-temp_num_1)/16)
                            temp_num_1 = temp_num_0%16
                            if temp_number_list[6] == temp_num_1:
                                out_bool =temp_number_list[7] == 0
                            else:
                                out_bool = False
                        else:
                            temp_num_0 = ord(virtual_name[0])    
                            temp_num_1 = temp_num_0%16
                            temp_num_0 = int((temp_num_0-temp_num_1)/16)
                            temp_num_1 = temp_num_0%16
                            if temp_number_list[6] == temp_num_1:
                                temp_num_0 = ord(virtual_name[1])    
                                temp_num_1 = temp_num_0%16
                                out_bool = temp_number_list[7] == temp_num_1
                            else:
                                out_bool = False
                else:
                    out_bool = False
        if out_bool:
            if not organization_number is None:
                if self.num_organization_valid(organization_number):
                    organization_number = organization_number.strip()
                    if not mix_number is None:
                        out_bool = mix_number[:3].upper() == organization_number[:3].upper()
                    if out_bool:
                        temp_number_list_2 = []
                        for n in range(14):
                            temp_num_0 = -1
                            temp_str_0 = organization_number[n]
                            for n1 in range(64):
                                if long_digits[n1] == temp_str_0:
                                    temp_num_0 = n1
                                    break
                            temp_number_list_2.append(temp_num_0)
                        if ((temp_number_list_2[3]+temp_number_list_2[7]+
                             temp_number_list_2[11]) % 16 != temp_number_list[4]):
                            out_bool = False
                        elif ((temp_number_list_2[2]+temp_number_list_2[6]+
                             temp_number_list_2[10]) % 16 != temp_number_list[5]):
                            out_bool = False
                else:
                    out_bool = False
        return out_bool
    
    def forming_str_text_org(self, 
                             in_org_num, in_org_name, in_org_init_num, 
                             in_org_admin, in_gene_list, in_editor, 
                             in_loc_list, in_member_of_org_list):
        # forming string text of organization
        
        # input: in_org_num, organization number, string of length 14
        #        in_org_name, organization name, string 
        #        in_org_init_num, string of 3 initial numbers
        #        in_org_admin, administrator, string of length 7
        #        in_gene_list, generator of the organization, ["manipulation", "date", "time"]
        #        in_editor, current editor, string of length 7
        #        in_loc_list, location, ["city", "region"]
        #        in_member_of_org_list= [[mani_num 0, enabled or not (1/0), member_num, 
        #                                 En_name or A/V name (0/1), name-0, name-1, name-2, 
        #                                 issuer's org_num, org's date, org's time]. 
        #                                [mani_num 1, enabled or not (1/0), member_num, 
        #                                 En_name or A/V name (0/1), name-0, name-1, name-2, 
        #                                 issuer's org_num, org's date, org's time]. 
        #                                [mani_num 2, enabled or not (1/0), member_num, 
        #                                 En_name or A/V name (0/1), name-0, name-1, name-2, 
        #                                 issuer's org_num, org's date, org's time].  ...]
        #                               length 10 per each    
        
        # output: string
        
        file_sep = ";"+"\u0009"+"\u000a"
        file_sub_sep = ","+"\u0009" 
        English_name_capital = ("A", "B", "C", "D", "E", "F", "G", 
                                "H", "I", "J", "K", "L", "M", "N", 
                                "O", "P", "Q", "R", "S", "T", 
                                "U", "V", "W", "X", "Y", "Z")
        English_name_capital_1 = ("A", "B", "C", "D", "E", "F", "G", 
                                  "H", "I", "J", "K", "L", "M", "N", 
                                  "O", "P", "Q", "R", "S", "T", 
                                  "U", "V", "W", "X", "Y", "Z", 
                                  "0", "1", "2", "3", "4", 
                                  "5", "6", "7", "8", "9")
        English_org_name_other = (" ", "-", "'", "‘", "’", "&", 
                                  "/", ".", ":", "(", ")")
        numeric_digits = ("0", "1", "2", "3", "4", 
                          "5", "6", "7", "8", "9")
        regions_short = ('nam', 'cam', 'car', 'sam', 'weu', 
                         'seu', 'neu', 'eeu', 'naf', 'eaf', 
                         'maf', 'saf', 'waf', 'eas', 'sea', 
                         'nas', 'cas', 'sas', 'me', 'omi', 
                         'ome', 'opo', 'oau', 'int', 'other')
        regions = ("nam - Northern America", 
                   "cam - Central America", 
                   "car - Caribbean", 
                   "sam - South America", 
                   "weu - Western Europe", 
                   "seu - Southern Europe", 
                   "neu - Northern Europe", 
                   "eeu - Eastern Europe", 
                   "naf - North Africa", 
                   "eaf - East Africa", 
                   "maf - Middle Africa", 
                   "saf - Southern Africa", 
                   "waf - West Africa",
                   "eas - East Asia", 
                   "sea - Southeast Asia", 
                   "nas - North Asia / Siberia", 
                   "cas - Central Asia", 
                   "sas - South Asia", 
                   "me - Western Asia / Middle East", 
                   "omi - Micronesia", 
                   "ome - Melanesia", 
                   "opo - Polynesia", 
                   "oau - Australasia", 
                   "int - Internation", 
                   "other - Other")
        out_str = ""
        temp_bool = True
        if isinstance(in_org_num, str):
            if isinstance(in_gene_list, list) | isinstance(in_gene_list, tuple):
                if len(in_gene_list) == 3:
                    if (isinstance(in_gene_list[0], str) & isinstance(in_gene_list[1], str) & 
                        isinstance(in_gene_list[2], str)):
                        temp_str_0 = in_gene_list[1].strip()
                        if len(temp_str_0) == 10:
                            if not temp_str_0[0] in numeric_digits:
                                temp_bool = False 
                            elif not temp_str_0[1] in numeric_digits:
                                temp_bool = False  
                            elif not temp_str_0[2] in numeric_digits:
                                temp_bool = False  
                            elif not temp_str_0[3] in numeric_digits:
                                temp_bool = False 
                            elif temp_str_0[4] != "-":
                                temp_bool = False   
                            elif not temp_str_0[5] in numeric_digits:
                                temp_bool = False  
                            elif not temp_str_0[6] in numeric_digits:
                                temp_bool = False  
                            elif temp_str_0[7] != "-":
                                temp_bool = False   
                            elif not temp_str_0[8] in numeric_digits:
                                temp_bool = False  
                            elif not temp_str_0[9] in numeric_digits:
                                temp_bool = False 
                            if temp_bool:
                                temp_num_0 = int(temp_str_0[0:4])
                                temp_num_1 = int(temp_str_0[5:7])
                                temp_num_2 = int(temp_str_0[8:10])
                        else:
                            temp_bool = False 
                        if temp_bool:
                            temp_str_1 = in_gene_list[2].strip()
                            if len(temp_str_1) == 5:
                                if not temp_str_1[0] in numeric_digits:
                                    temp_bool = False  
                                elif not temp_str_1[1] in numeric_digits:
                                    temp_bool = False 
                                elif temp_str_1[2] != ":":
                                    temp_bool = False   
                                elif not temp_str_1[3] in numeric_digits:
                                    temp_bool = False  
                                elif not temp_str_1[4] in numeric_digits:
                                    temp_bool = False  
                                if temp_bool:
                                    temp_num_3 = int(temp_str_1[0:2])
                                    temp_num_4 = int(temp_str_1[3:5])
                            else:
                                temp_bool = False  
                    if temp_bool:
                        in_org_num = in_org_num.strip()
                        temp_bool = self.num_organization_valid(in_org_num, 
                                                                temp_num_0, temp_num_1, temp_num_2, 
                                                                temp_num_3, temp_num_4)
                else:
                    temp_bool = False
            else:
                temp_bool = False
        else:
            temp_bool = False
        if temp_bool:
            out_str = out_str+in_org_num
            out_str = out_str+file_sub_sep
            out_str = out_str+self.num_organization_64_2_16(in_org_num)
        if temp_bool:
            if isinstance(in_org_num, str):
                in_org_name = in_org_name.strip()
                temp_num_0 = len(in_org_name)
                if temp_num_0 == 0:
                    temp_bool = False
                if temp_num_0 == 1:
                    temp_str_2 = in_org_name[0].upper()
                    if not temp_str_2 in English_name_capital_1:
                        temp_bool = False
                else:
                    temp_str_2 = in_org_name[0].upper()
                    if temp_str_2 in English_name_capital_1:
                        for n in range(1, temp_num_0):
                            temp_str_2 = in_org_name[n].upper()
                            if ((not temp_str_2 in English_name_capital_1) & 
                                (not temp_str_2 in English_org_name_other)):
                                temp_bool = False
                                break
                    else:
                        temp_bool = False
                if temp_bool:
                    if isinstance(in_org_init_num, str):
                        in_org_init_num = in_org_init_num.strip()
                        if len(in_org_init_num) == 3:
                            temp_str_2 = ""
                            for n in range(3):
                                temp_str_3 = in_org_init_num[n].upper()
                                if temp_str_3 in English_name_capital:
                                    temp_str_2 = temp_str_2+temp_str_3
                                else:
                                    temp_bool = False
                                    break
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
            else:
                temp_bool = False
        if temp_bool:
            in_org_init_num = temp_str_2
            if in_org_num[0:3].upper() == in_org_init_num:
                out_str = out_str+file_sep
                out_str = out_str+in_org_name
                out_str = out_str+file_sub_sep
                out_str = out_str+in_org_init_num
            else:
                temp_bool = False
        if temp_bool:
            if isinstance(in_org_admin, str):
                in_org_admin = in_org_admin.strip()
                if len(in_org_admin) == 7:
                    out_str = out_str+file_sep
                    out_str = out_str+in_org_admin
                    temp_str_2 = in_gene_list[0].strip()
                    if len(temp_str_2) == 7:
                        out_str = out_str+file_sep
                        out_str = out_str+temp_str_2
                        out_str = out_str+file_sub_sep
                        out_str = out_str+temp_str_0
                        out_str = out_str+file_sub_sep
                        out_str = out_str+temp_str_1
                        in_editor = in_editor.strip()
                        out_str = out_str+file_sep
                        out_str = out_str+in_editor
                        if len(in_editor) == 7:
                            temp_time_now = datetime.utcnow()
                            temp_num_0 = temp_time_now.year
                            temp_str_0 = ""
                            if temp_num_0 < 10:
                                temp_str_0 = temp_str_0+"000"+str(temp_num_0)
                            elif temp_num_0 < 100:
                                temp_str_0 = temp_str_0+"00"+str(temp_num_0)
                            elif temp_num_0 < 1000:
                                temp_str_0 = temp_str_0+"0"+str(temp_num_0)
                            elif temp_num_0 < 10000:
                                temp_str_0 = temp_str_0+str(temp_num_0)
                            temp_str_0 = temp_str_0+"-"
                            temp_num_0 = temp_time_now.month
                            if temp_num_0 < 10:
                                temp_str_0 = temp_str_0+"0"+str(temp_num_0)
                            elif temp_num_0 < 100:
                                temp_str_0 = temp_str_0+str(temp_num_0)
                            temp_str_0 = temp_str_0+"-"
                            temp_num_0 = temp_time_now.day
                            if temp_num_0 < 10:
                                temp_str_0 = temp_str_0+"0"+str(temp_num_0)
                            elif temp_num_0 < 100:
                                temp_str_0 = temp_str_0+str(temp_num_0)
                            out_str = out_str+file_sub_sep
                            out_str = out_str+temp_str_0
                            temp_str_0 = ""
                            temp_num_0 = temp_time_now.hour
                            if temp_num_0 < 10:
                                temp_str_0 = temp_str_0+"0"+str(temp_num_0)
                            elif temp_num_0 < 100:
                                temp_str_0 = temp_str_0+str(temp_num_0)
                            temp_str_0 = temp_str_0+":"
                            temp_num_0 = temp_time_now.minute
                            if temp_num_0 < 10:
                                temp_str_0 = temp_str_0+"0"+str(temp_num_0)
                            elif temp_num_0 < 100:
                                temp_str_0 = temp_str_0+str(temp_num_0)
                            out_str = out_str+file_sub_sep
                            out_str = out_str+temp_str_0
                        else:
                            temp_bool = False      
                    else:
                        temp_bool = False   
                else:
                    temp_bool = False   
            else:
                temp_bool = False
        if temp_bool:
            if isinstance(in_loc_list, list) | isinstance(in_loc_list, tuple):
                if len(in_loc_list) == 2:
                    if isinstance(in_loc_list[0], str) & isinstance(in_loc_list[1], str):
                        temp_str_0 = in_loc_list[0].strip()
                        temp_str_1 = in_loc_list[1].strip()
                        temp_num_0 = -1
                        for n in range(25):
                            if regions[n] == temp_str_1:
                                temp_num_0 = n
                                break
                        if temp_num_0 >= 0:
                            temp_num_1 = len(temp_str_0)                    
                            if temp_num_1 == 1:
                                temp_str_2 = temp_str_0[0].upper()
                                if not temp_str_2 in English_name_capital_1:
                                    temp_bool = False
                            elif temp_num_1 > 1:
                                temp_str_2 = temp_str_0[0].upper()
                                if temp_str_2 in English_name_capital_1:
                                    for n in range(1, temp_num_1):
                                        temp_str_2 = in_org_name[n].upper()
                                        if ((not temp_str_2 in English_name_capital_1) & 
                                            (not temp_str_2 in English_org_name_other)):
                                            temp_bool = False
                                            break
                                else:
                                    temp_bool = False
                            if temp_bool:
                                out_str = out_str+file_sep
                                out_str = out_str+temp_str_0
                                out_str = out_str+file_sub_sep
                                out_str = out_str+regions_short[temp_num_0]
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
            else:
                temp_bool = False
        if temp_bool:
            if isinstance(in_member_of_org_list, list) | isinstance(in_member_of_org_list, tuple):
                temp_num_0 = len(in_member_of_org_list)
                if (temp_num_0 > 0) & (temp_num_0 <= 777):
                    temp_mani_str_list = []
                    temp_mani_num_list = []
                    temp_mani_num_enable_list = [] 
                    for n in range(temp_num_0):
                        temp_list_1 = in_member_of_org_list[n]
                        if not temp_list_1 is None: 
                            temp_bool_1 = True  
                            if isinstance(temp_list_1, list) | isinstance(temp_list_1, tuple):
                                if len(temp_list_1) == 10:
                                    temp_str_0 = ""
                                    if isinstance(temp_list_1[0], str):
                                        temp_str_1 = temp_list_1[0].strip()
                                        if not temp_str_1 in temp_mani_str_list:
                                            if self.number_manipulation_valid(temp_str_1, in_org_num):
                                                temp_str_0 = temp_str_0+temp_str_1
                                                temp_mani_num_list.append(temp_str_1)
                                            else:
                                                temp_bool_1 = False
                                        else:
                                            temp_bool_1 = False
                                    else:
                                        temp_bool_1 = False
                                    if temp_bool_1:
                                        if isinstance(temp_list_1[1], bool):
                                            temp_str_0 = temp_str_0+file_sub_sep
                                            if temp_list_1[1]:
                                                temp_str_0 = temp_str_0+"1"
                                            else:
                                                temp_str_0 = temp_str_0+"0"
                                            temp_mani_num_enable_list.append(temp_list_1[1])
                                        else:
                                            temp_bool_1 = False
                                    if temp_bool_1:
                                        if isinstance(temp_list_1[2], str):
                                            temp_str_1 = temp_list_1[2].strip()
                                            if len(temp_str_1) == 14:
                                                temp_str_0 = temp_str_0+file_sub_sep
                                                temp_str_0 = temp_str_0+temp_str_1
                                            else:
                                                temp_bool_1 = False
                                        else:
                                            temp_bool_1 = False
                                    if temp_bool_1:
                                        if isinstance(temp_list_1[3], str):
                                            temp_str_2 = temp_list_1[3].strip()
                                            if temp_str_2 == "en":
                                                temp_str_0 = temp_str_0+file_sub_sep
                                                temp_str_0 = temp_str_0+"0"
                                            elif temp_str_2 == "vn":
                                                temp_str_0 = temp_str_0+file_sub_sep
                                                temp_str_0 = temp_str_0+"1"
                                            else:
                                                temp_bool_1 = False
                                        else:
                                            temp_bool_1 = False
                                    if temp_bool_1:
                                        if (isinstance(temp_list_1[4], str) & isinstance(temp_list_1[5], str) & 
                                            isinstance(temp_list_1[6], str)):
                                            temp_str_3 = temp_list_1[4].strip()
                                            temp_str_4 = temp_list_1[5].strip()
                                            temp_str_5 = temp_list_1[6].strip()
                                            if temp_str_2 == "en":
                                                if len(temp_str_3) > 0:
                                                    if self.English_name_valid([temp_str_3, temp_str_4, temp_str_5]):
                                                        temp_str_0 = temp_str_0+file_sub_sep
                                                        temp_str_0 = temp_str_0+temp_str_3
                                                        temp_str_0 = temp_str_0+file_sub_sep
                                                        temp_str_0 = temp_str_0+temp_str_4
                                                        temp_str_0 = temp_str_0+file_sub_sep
                                                        temp_str_0 = temp_str_0+temp_str_5
                                                    else:
                                                        temp_bool_1 = False
                                                else:
                                                    temp_bool_1 = False
                                            else:
                                                if len(temp_str_4) > 0:
                                                    if self.virtual_name_valid([temp_str_3, temp_str_4, temp_str_5]):
                                                        temp_str_0 = temp_str_0+file_sub_sep
                                                        temp_str_0 = temp_str_0+temp_str_3
                                                        temp_str_0 = temp_str_0+file_sub_sep
                                                        temp_str_0 = temp_str_0+temp_str_4
                                                        temp_str_0 = temp_str_0+file_sub_sep
                                                        temp_str_0 = temp_str_0+temp_str_5
                                                        temp_str_3 = temp_str_4
                                                    else:
                                                        temp_bool_1 = False
                                                else:
                                                    temp_bool_1 = False 
                                        else:
                                            temp_bool_1 = False
                                    if temp_bool_1:
                                        if (isinstance(temp_list_1[7], str) & isinstance(temp_list_1[8], str) & 
                                            isinstance(temp_list_1[9], str)):
                                            temp_str_4 = temp_list_1[7].strip()
                                            temp_str_5 = temp_list_1[8].strip()
                                            temp_str_6 = temp_list_1[9].strip()
                                            if len(temp_str_4) == 14:
                                                temp_bool_1 = temp_str_4[0:3].upper() == in_org_init_num
                                            else:
                                                temp_bool_1 = False
                                            if temp_bool_1:
                                                if len(temp_str_5) == 10:
                                                    if not temp_str_5[0] in numeric_digits:
                                                        temp_bool_1 = False 
                                                    elif not temp_str_5[1] in numeric_digits:
                                                        temp_bool_1 = False  
                                                    elif not temp_str_5[2] in numeric_digits:
                                                        temp_bool_1 = False  
                                                    elif not temp_str_5[3] in numeric_digits:
                                                        temp_bool_1 = False 
                                                    elif temp_str_5[4] != "-":
                                                        temp_bool_1 = False   
                                                    elif not temp_str_5[5] in numeric_digits:
                                                        temp_bool_1 = False  
                                                    elif not temp_str_5[6] in numeric_digits:
                                                        temp_bool_1 = False  
                                                    elif temp_str_5[7] != "-":
                                                        temp_bool_1 = False   
                                                    elif not temp_str_5[8] in numeric_digits:
                                                        temp_bool_1 = False  
                                                    elif not temp_str_5[9] in numeric_digits:
                                                        temp_bool_1 = False 
                                                    if temp_bool_1:
                                                        temp_num_1 = int(temp_str_5[0:4])
                                                        temp_num_2 = int(temp_str_5[5:7])
                                                        temp_num_3 = int(temp_str_5[8:10])
                                                else:
                                                    temp_bool_1 = False 
                                            if temp_bool_1:
                                                if len(temp_str_6) == 5:
                                                    if not temp_str_6[0] in numeric_digits:
                                                        temp_bool_1 = False  
                                                    elif not temp_str_6[1] in numeric_digits:
                                                        temp_bool_1 = False 
                                                    elif temp_str_6[2] != ":":
                                                        temp_bool_1 = False   
                                                    elif not temp_str_6[3] in numeric_digits:
                                                        temp_bool_1 = False  
                                                    elif not temp_str_6[4] in numeric_digits:
                                                        temp_bool_1 = False  
                                                    if temp_bool_1:
                                                        temp_num_4 = int(temp_str_6[0:2])
                                                        temp_num_5 = int(temp_str_6[3:5])
                                                else:
                                                    temp_bool_1 = False  
                                            if temp_bool_1:
                                                if self.num_organization_valid(temp_str_4, 
                                                                               temp_num_1, temp_num_2, temp_num_3, 
                                                                               temp_num_4, temp_num_5):
                                                    if temp_str_2 == "en":
                                                        temp_bool_1 = self.num_member_valid(temp_str_1, 
                                                                                            organization_number = temp_str_4)
                                                    else:
                                                        temp_bool_1 = self.num_member_valid(temp_str_1, 
                                                                                            virtual_name = temp_str_3, 
                                                                                            organization_number = temp_str_4)
                                                    if temp_bool_1:
                                                        temp_str_0 = temp_str_0+file_sub_sep
                                                        temp_str_0 = temp_str_0+temp_str_4
                                                        temp_str_0 = temp_str_0+file_sub_sep
                                                        temp_str_0 = temp_str_0+temp_str_5
                                                        temp_str_0 = temp_str_0+file_sub_sep
                                                        temp_str_0 = temp_str_0+temp_str_6
                                                else:
                                                    temp_bool_1 = False 
                                        else:
                                            temp_bool_1 = False
                                else:
                                    temp_bool_1 = False
                            else:
                                temp_bool_1 = False
                            if temp_bool_1:
                                temp_mani_str_list.append(temp_str_0)    
                            else:
                                temp_bool = False
                                break
                else:
                    temp_bool = False
            else:
                temp_bool = False
        if temp_bool:        
            temp_num_0 = len(temp_mani_str_list)
            temp_num_1 = -1
            temp_str_1 = in_org_admin.strip()
            temp_num_2 = -1
            temp_str_2 = in_editor.strip()
            temp_num_3 = -1
            temp_str_3 = in_gene_list[0].strip()
            for n in range(temp_num_0):
                if temp_num_1 < 0:
                    if temp_mani_num_list[n] == temp_str_1:
                        temp_num_1 = n
                if temp_num_2 < 0:
                    if temp_mani_num_list[n] == temp_str_2:
                        temp_num_2 = n
                if temp_num_3 < 0:
                    if temp_mani_num_list[n] == temp_str_3:
                        temp_num_3 = n 
                if (temp_num_1 >= 0) & (temp_num_2 >= 0) & (temp_num_3 >= 0):
                    break
            if (temp_num_1 >= 0) & (temp_num_2 >= 0) & (temp_num_3 >= 0):
                if (temp_mani_num_enable_list[temp_num_1]) & (temp_mani_num_enable_list[temp_num_2]):
                    out_str = out_str+file_sep
                    out_str = out_str+str(temp_num_0)
                    for n in range(temp_num_0):
                        out_str = out_str+file_sep
                        out_str = out_str+temp_mani_str_list[n]
                else:
                    temp_bool = False 
            else:
                temp_bool = False 
        if not temp_bool:
            out_str = None
        return out_str
    
    def reading_str_text_org(self, in_str):
        # reading string text of organization
        
        # input: in_str, string   
        
        # output: [organization info list, 
        #          manipulation info list, 
        #          manipulation number list, 
        #          enabled number list]
        
        file_read_sep = ";"+"\u0009"
        file_sub_sep = ","+"\u0009" 
        English_name_capital = ("A", "B", "C", "D", "E", "F", "G", 
                                "H", "I", "J", "K", "L", "M", "N", 
                                "O", "P", "Q", "R", "S", "T", 
                                "U", "V", "W", "X", "Y", "Z")
        English_name_capital_1 = ("A", "B", "C", "D", "E", "F", "G", 
                                  "H", "I", "J", "K", "L", "M", "N", 
                                  "O", "P", "Q", "R", "S", "T", 
                                  "U", "V", "W", "X", "Y", "Z", 
                                  "0", "1", "2", "3", "4", 
                                  "5", "6", "7", "8", "9")
        English_org_name_other = (" ", "-", "'", "‘", "’", "&", 
                                  "/", ".", ":", "(", ")")
        numeric_digits = ("0", "1", "2", "3", "4", 
                          "5", "6", "7", "8", "9")
        regions_short = ('nam', 'cam', 'car', 'sam', 'weu', 
                        'seu', 'neu', 'eeu', 'naf', 'eaf', 
                        'maf', 'saf', 'waf', 'eas', 'sea', 
                        'nas', 'cas', 'sas', 'me', 'omi', 
                        'ome', 'opo', 'oau', 'int', 'other')
        regions = ("nam - Northern America", 
                   "cam - Central America", 
                   "car - Caribbean", 
                   "sam - South America", 
                   "weu - Western Europe", 
                   "seu - Southern Europe", 
                   "neu - Northern Europe", 
                   "eeu - Eastern Europe", 
                   "naf - North Africa", 
                   "eaf - East Africa", 
                   "maf - Middle Africa", 
                   "saf - Southern Africa", 
                   "waf - West Africa",
                   "eas - East Asia", 
                   "sea - Southeast Asia", 
                   "nas - North Asia / Siberia", 
                   "cas - Central Asia", 
                   "sas - South Asia", 
                   "me - Western Asia / Middle East", 
                   "omi - Micronesia", 
                   "ome - Melanesia", 
                   "opo - Polynesia", 
                   "oau - Australasia", 
                   "int - Internation", 
                   "other - Other")
        org_info_list = []
        mani_info_list = []
        mani_num_list = []
        mani_enabled_list = []
        temp_bool = True
        if isinstance(in_str, str):
            temp_str_list_0 = in_str.split(file_read_sep)
            temp_len_0 = len(temp_str_list_0)
            if temp_len_0 >= 8:
                temp_str_0 = temp_str_list_0[6].strip()
                temp_len_1 = len(temp_str_0)
                if temp_len_1 > 0:
                    for n in range(temp_len_1):
                        if not temp_str_0[n] in numeric_digits:
                            temp_bool = False
                            break
                    if temp_bool:
                        temp_len_1 = int(temp_str_0)
                        temp_bool = temp_len_1+7 == temp_len_0
                else:
                    temp_bool = False
            else:
                temp_bool = False
        else:
            temp_bool = False
        if temp_bool:
            temp_str_list_1 = temp_str_list_0[0].split(file_sub_sep)
            if len(temp_str_list_1) == 2:
                temp_str_0 = temp_str_list_1[0].strip()
                temp_str_1 = temp_str_list_1[1].strip()
                if (len(temp_str_0) == 14) & (len(temp_str_1) == 21):
                    org_info_list.append(temp_str_0)
                    org_info_list.append(temp_str_1)
                else:
                    temp_bool = False
            else:
                temp_bool = False
            if temp_bool:
                temp_str_list_1 = temp_str_list_0[1].split(file_sub_sep)
                if len(temp_str_list_1) == 2:
                    temp_str_0 = temp_str_list_1[0].strip()
                    temp_str_1 = temp_str_list_1[1].strip()
                    org_init_num = temp_str_1
                    if len(temp_str_1) == 3:
                        temp_str_2 = temp_str_1[1]
                        temp_str_3 = temp_str_1[2]
                        temp_str_1 = temp_str_1[0]
                        if ((temp_str_1 in English_name_capital) & (temp_str_2 in English_name_capital) & 
                            (temp_str_3 in English_name_capital)):
                            if org_info_list[0][0:3].upper() == org_init_num:
                                temp_len_2 = len(temp_str_0)
                                if temp_len_2 < 1:
                                    temp_bool = False
                                elif temp_len_2 == 1:
                                    temp_bool = temp_str_0[0] in English_name_capital_1
                                else:
                                    if temp_str_0[0] in English_name_capital_1:
                                        for n in range(1, temp_len_2):
                                            if ((not temp_str_0[n].upper() in English_name_capital_1) & 
                                                (not temp_str_0[n] in English_org_name_other)):
                                                temp_bool = False
                                                break
                                        if temp_bool:
                                            org_info_list.append(temp_str_0)
                                            org_info_list.append((temp_str_1, temp_str_2, temp_str_3))
                                    else:
                                        temp_bool = False
                            else:
                                temp_bool = False
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
            if temp_bool:
                temp_str_0 = temp_str_list_0[2].strip()
                if len(temp_str_0) == 7:
                    org_info_list.append(temp_str_0)
                else:
                    temp_bool = False       
            if temp_bool:
                temp_str_list_1 = temp_str_list_0[3].split(file_sub_sep)
                if len(temp_str_list_1) == 3:
                    temp_str_0 = temp_str_list_1[0].strip()
                    temp_str_1 = temp_str_list_1[1].strip()
                    temp_str_2 = temp_str_list_1[2].strip()
                    if len(temp_str_0) == 7:
                        if len(temp_str_1) == 10:
                            if not temp_str_1[0] in numeric_digits:
                                temp_bool = False
                            elif not temp_str_1[1] in numeric_digits:
                                temp_bool = False
                            elif not temp_str_1[2] in numeric_digits:
                                temp_bool = False
                            elif not temp_str_1[3] in numeric_digits:
                                temp_bool = False
                            elif temp_str_1[4] != "-":
                                temp_bool = False
                            elif not temp_str_1[5] in numeric_digits:
                                temp_bool = False
                            elif not temp_str_1[6] in numeric_digits:
                                temp_bool = False
                            elif temp_str_1[7] != "-":
                                temp_bool = False
                            elif not temp_str_1[8] in numeric_digits:
                                temp_bool = False
                            elif not temp_str_1[9] in numeric_digits:
                                temp_bool = False
                            if temp_bool:
                                temp_num_0 = int(temp_str_1[0:4])
                                temp_num_1 = int(temp_str_1[5:7])
                                temp_num_2 = int(temp_str_1[8:10])
                                if not temp_str_2[0] in numeric_digits:
                                    temp_bool = False
                                elif not temp_str_2[1] in numeric_digits:
                                    temp_bool = False
                                elif temp_str_2[2] != ":":
                                    temp_bool = False
                                elif not temp_str_2[3] in numeric_digits:
                                    temp_bool = False
                                elif not temp_str_2[4] in numeric_digits:
                                    temp_bool = False
                                if temp_bool:
                                    temp_num_3 = int(temp_str_2[0:2])
                                    temp_num_4 = int(temp_str_2[3:5])
                                    if self.num_organization_valid(org_info_list[0], 
                                                                   temp_num_0, temp_num_1, temp_num_2, 
                                                                   temp_num_3, temp_num_4):
                                        org_info_list.append((temp_str_0, temp_str_1, temp_str_2))
                                    else:
                                        temp_bool = False
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
            if temp_bool:
                temp_str_list_1 = temp_str_list_0[4].split(file_sub_sep)
                if len(temp_str_list_1) == 3:
                    temp_str_0 = temp_str_list_1[0].strip()
                    temp_str_1 = temp_str_list_1[1].strip()
                    temp_str_2 = temp_str_list_1[2].strip()
                    if len(temp_str_0) == 7:
                        if len(temp_str_1) == 10:
                            if not temp_str_1[0] in numeric_digits:
                                temp_bool = False
                            elif not temp_str_1[1] in numeric_digits:
                                temp_bool = False
                            elif not temp_str_1[2] in numeric_digits:
                                temp_bool = False
                            elif not temp_str_1[3] in numeric_digits:
                                temp_bool = False
                            elif temp_str_1[4] != "-":
                                temp_bool = False
                            elif not temp_str_1[5] in numeric_digits:
                                temp_bool = False
                            elif not temp_str_1[6] in numeric_digits:
                                temp_bool = False
                            elif temp_str_1[7] != "-":
                                temp_bool = False
                            elif not temp_str_1[8] in numeric_digits:
                                temp_bool = False
                            elif not temp_str_1[9] in numeric_digits:
                                temp_bool = False
                            if temp_bool:
                                temp_num_5 = int(temp_str_1[0:4])
                                temp_num_6 = int(temp_str_1[5:7])
                                temp_num_7 = int(temp_str_1[8:10])
                                if not temp_str_2[0] in numeric_digits:
                                    temp_bool = False
                                elif not temp_str_2[1] in numeric_digits:
                                    temp_bool = False
                                elif temp_str_2[2] != ":":
                                    temp_bool = False
                                elif not temp_str_2[3] in numeric_digits:
                                    temp_bool = False
                                elif not temp_str_2[4] in numeric_digits:
                                    temp_bool = False
                                if temp_bool:
                                    temp_num_8 = int(temp_str_2[0:2])
                                    temp_num_9 = int(temp_str_2[3:5])
                                    if temp_num_5 < temp_num_0:
                                        temp_bool = False
                                    elif temp_num_5 == temp_num_0:
                                        if temp_num_6 < temp_num_1:
                                            temp_bool = False
                                        elif temp_num_6 == temp_num_1:
                                            if temp_num_7 < temp_num_2:
                                                temp_bool = False
                                            elif temp_num_7 == temp_num_2:
                                                if temp_num_8 < temp_num_3:
                                                    temp_bool = False
                                                elif temp_num_8 == temp_num_3:
                                                    if temp_num_9 < temp_num_4:
                                                        temp_bool = False
                                    if temp_bool:
                                        if (temp_num_8 >= 0) & (temp_num_8 < 24):
                                            if (temp_num_9 >= 0) & (temp_num_9 < 60):
                                                if temp_num_6 in (4, 6, 9, 11):
                                                    if (temp_num_7 < 1) | (temp_num_7 > 30):
                                                        temp_bool = False
                                                elif temp_num_6 in (1, 3, 5, 7, 8, 10, 12):
                                                    if (temp_num_7 < 1) | (temp_num_7 > 31):
                                                        temp_bool = False
                                                elif temp_num_6 == 2:
                                                    if temp_num_5%400 == 0:
                                                        if (temp_num_7 < 1) | (temp_num_7 > 29):
                                                            temp_bool = False
                                                    elif temp_num_5%100 == 0:
                                                        if (temp_num_7 < 1) | (temp_num_7 > 28):
                                                            temp_bool = False
                                                    elif temp_num_5%4 == 0:
                                                        if (temp_num_7 < 1) | (temp_num_7 > 29):
                                                            temp_bool = False
                                                    else:
                                                        if (temp_num_7 < 1) | (temp_num_7 > 28):
                                                            temp_bool = False
                                                else:
                                                    temp_bool = False
                                            else:
                                                temp_bool = False
                                        else:
                                            temp_bool = False
                                        if temp_bool:
                                            org_info_list.append((temp_str_0, temp_str_1, temp_str_2))
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
            if temp_bool:
                temp_str_list_1 = temp_str_list_0[5].split(file_sub_sep)
                if len(temp_str_list_1) == 2:
                    temp_str_0 = temp_str_list_1[0].strip()
                    temp_str_1 = temp_str_list_1[1].strip()
                    temp_num_0 = -1
                    for n in range(25):
                        if regions_short[n] == temp_str_1:
                            temp_num_0 = n
                            break
                    if temp_num_0 >= 0:
                        temp_len_2 = len(temp_str_0)
                        if temp_len_2 == 1:
                            if not temp_str_0[0] in English_name_capital_1:
                                temp_bool = False
                        elif temp_len_2 > 1:
                            if temp_str_0[0] in English_name_capital_1:
                                for n in range(1, temp_len_2):
                                    if ((not temp_str_0[n].upper() in English_name_capital_1) & 
                                        (not temp_str_0[n] in English_org_name_other)):
                                        temp_bool = False
                                        break
                            else:
                                temp_bool = False
                        if temp_bool:
                            org_info_list.append([temp_str_0, regions[temp_num_0]])
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
        if temp_bool:
            for n in range(7, temp_len_0):
                temp_str_list_1 = temp_str_list_0[n].split(file_sub_sep)
                if len(temp_str_list_1) == 10:
                    temp_str_list_2 = []
                    for n1 in range(10):
                        temp_str_list_2.append(temp_str_list_1[n1].strip())
                    temp_str_list_3 = []
                    if not temp_str_list_2[0] in mani_num_list:                    
                        if self.number_manipulation_valid(temp_str_list_2[0], org_info_list[0]):
                            temp_str_list_3.append(temp_str_list_2[0])
                            mani_num_list.append(temp_str_list_2[0])
                            if temp_str_list_2[1] == "0":
                                temp_str_list_3.append(False)
                                mani_enabled_list.append(False)
                            elif temp_str_list_2[1] == "1":
                                temp_str_list_3.append(True)
                                mani_enabled_list.append(True)
                            else:
                                temp_bool = False
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
                if temp_bool:
                    if len(temp_str_list_2[2]) == 14:
                        temp_str_list_3.append(temp_str_list_2[2])
                        if temp_str_list_2[3] == "0":
                            temp_str_list_3.append("en")
                            temp_str_list_4 = [temp_str_list_2[4], 
                                               temp_str_list_2[5], 
                                               temp_str_list_2[6]]
                            if self.English_name_valid(temp_str_list_4):
                                if self.num_member_valid(temp_str_list_2[2], 
                                                         organization_number = temp_str_list_2[7]):
                                    temp_str_list_3.append(temp_str_list_2[4])
                                    temp_str_list_3.append(temp_str_list_2[5])
                                    temp_str_list_3.append(temp_str_list_2[6])
                                else:
                                    temp_bool = False
                            else:
                                temp_bool = False
                        elif temp_str_list_2[3] == "1":
                            temp_str_list_3.append("vn")
                            temp_str_list_4 = [temp_str_list_2[4], 
                                               temp_str_list_2[5], 
                                               temp_str_list_2[6]]
                            if self.virtual_name_valid(temp_str_list_4):
                                if self.num_member_valid(temp_str_list_2[2], 
                                                         virtual_name = temp_str_list_2[5], 
                                                         organization_number = temp_str_list_2[7]):
                                    temp_str_list_3.append(temp_str_list_2[4])
                                    temp_str_list_3.append(temp_str_list_2[5])
                                    temp_str_list_3.append(temp_str_list_2[6])
                                else:
                                    temp_bool = False
                            else:
                                temp_bool = False
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
                if temp_bool:
                    if len(temp_str_list_2[7]) == 14:
                        temp_bool = temp_str_list_2[7][0:3].upper() == org_init_num
                    else:
                        temp_bool = False
                    if temp_bool:
                        if not temp_str_list_2[8][0] in numeric_digits:
                            temp_bool = False
                        elif not temp_str_list_2[8][1] in numeric_digits:
                            temp_bool = False
                        elif not temp_str_list_2[8][2] in numeric_digits:
                            temp_bool = False
                        elif not temp_str_list_2[8][3] in numeric_digits:
                            temp_bool = False
                        elif temp_str_list_2[8][4] != "-":
                            temp_bool = False
                        elif not temp_str_list_2[8][5] in numeric_digits:
                            temp_bool = False
                        elif not temp_str_list_2[8][6] in numeric_digits:
                            temp_bool = False
                        elif temp_str_list_2[8][7] != "-":
                            temp_bool = False
                        elif not temp_str_list_2[8][8] in numeric_digits:
                            temp_bool = False
                        elif not temp_str_list_2[8][9] in numeric_digits:
                            temp_bool = False
                    if temp_bool:
                        temp_num_0 = int(temp_str_list_2[8][0:4])
                        temp_num_1 = int(temp_str_list_2[8][5:7])
                        temp_num_2 = int(temp_str_list_2[8][8:10])
                        if not temp_str_list_2[9][0] in numeric_digits:
                            temp_bool = False
                        elif not temp_str_list_2[9][1] in numeric_digits:
                            temp_bool = False
                        elif temp_str_list_2[9][2] != ":":
                            temp_bool = False
                        elif not temp_str_list_2[9][3] in numeric_digits:
                            temp_bool = False
                        elif not temp_str_list_2[9][4] in numeric_digits:
                            temp_bool = False
                        if temp_bool:
                            temp_num_3 = int(temp_str_list_2[9][0:2])
                            temp_num_4 = int(temp_str_list_2[9][3:5])
                            if self.num_organization_valid(temp_str_list_2[7], 
                                                           temp_num_0, temp_num_1, temp_num_2, 
                                                           temp_num_3, temp_num_4):
                                temp_str_list_3.append(temp_str_list_2[7])
                                temp_str_list_3.append(temp_str_list_2[8])
                                temp_str_list_3.append(temp_str_list_2[9])
                            else:
                                temp_bool = False
                if temp_bool:
                    mani_info_list.append(tuple(temp_str_list_3))
                else:
                    break
        if temp_bool:
            temp_num_0 = -1
            temp_str_0 = org_info_list[4]
            temp_num_1 = -1
            temp_str_1 = org_info_list[5][0]
            temp_num_2 = -1
            temp_str_2 = org_info_list[6][0]
            for n in range(temp_len_1):
                if temp_num_0 < 0:
                    if mani_num_list[n] == temp_str_0:
                        temp_num_0 = n
                if temp_num_1 < 0:
                    if mani_num_list[n] == temp_str_1:
                        temp_num_1 = n
                if temp_num_2 < 0:
                    if mani_num_list[n] == temp_str_2:
                        temp_num_2 = n 
                if (temp_num_0 >= 0) & (temp_num_1 >= 0) & (temp_num_2 >= 0):
                    break
            if (temp_num_0 >= 0) & (temp_num_1 >= 0) & (temp_num_2 >= 0):
                temp_bool = (mani_enabled_list[temp_num_0]) & (mani_enabled_list[temp_num_1])            
            else:
                temp_bool = False 
        if temp_bool:
            out_tuple = (org_info_list, mani_info_list, mani_num_list, mani_enabled_list)
        else:
            out_tuple = None
        return out_tuple
    
    def forming_str_text_member(self, 
                                in_num_list, in_en_name_list, 
                                in_vn_name_list, in_date_list, 
                                in_org_list):
        # forming string text of member
        
        # input: in_num_list, numbers, [mixed number, member number]
        #        in_en_name_list, English name, [given, middle, family]
        #        in_vn_name_list, another name / virtual name, [type, name, addition]
        #        in_date_list, issued date of member, [date, time]
        #        in_org_list, issuing organization, [organization number, date, time, manipulation number]
            
        # output: string
        
        file_sep = ";"+"\u0009"+"\u000a"
        file_sub_sep = ","+"\u0009" 
        numeric_digits = ("0", "1", "2", "3", "4", 
                          "5", "6", "7", "8", "9")
        out_str = "member_info.iden"
        temp_bool = True    
        if isinstance(in_num_list, list) | isinstance(in_num_list, tuple):
            if len(in_num_list) == 2:
                if isinstance(in_num_list[0], str) & isinstance(in_num_list[1], str):
                    temp_str_0 = in_num_list[0].strip()
                    temp_str_1 = in_num_list[1].strip()
                    if (len(temp_str_0) == 21) & (len(temp_str_1) == 14):
                        out_str = out_str+file_sep
                        out_str = out_str+temp_str_0
                        out_str = out_str+file_sub_sep
                        out_str = out_str+temp_str_1   
                    else:
                        temp_bool = False              
                else:
                    temp_bool = False
            else:
                temp_bool = False
        else:
            temp_bool = False
        if temp_bool:
            if isinstance(in_en_name_list, list) | isinstance(in_en_name_list, tuple):
                if len(in_en_name_list) == 3:
                    if (isinstance(in_en_name_list[0], str) & isinstance(in_en_name_list[1], str) &
                        isinstance(in_en_name_list[2], str)):
                        temp_list_0 = [in_en_name_list[0].strip(), 
                                       in_en_name_list[1].strip(), 
                                       in_en_name_list[2].strip()]
                        if self.English_name_valid(temp_list_0):
                            out_str = out_str+file_sep
                            out_str = out_str+temp_list_0[0]
                            out_str = out_str+file_sub_sep
                            out_str = out_str+temp_list_0[1]  
                            out_str = out_str+file_sub_sep
                            out_str = out_str+temp_list_0[2]   
                            temp_str_2 = temp_list_0[0]
                            temp_str_3 = temp_list_0[2]
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
            else:
                temp_bool = False
        if temp_bool:
            if isinstance(in_vn_name_list, list) | isinstance(in_vn_name_list, tuple):
                if len(in_vn_name_list) == 3:
                    if (isinstance(in_vn_name_list[0], str) & isinstance(in_vn_name_list[1], str) &
                        isinstance(in_vn_name_list[2], str)):
                        temp_list_0 = [in_vn_name_list[0].strip(), 
                                       in_vn_name_list[1].strip(), 
                                       in_vn_name_list[2].strip()]
                        if self.virtual_name_valid(temp_list_0):
                            temp_str_4 = temp_list_0[1] 
                            if (len(temp_str_2) > 0) | (len(temp_str_4) > 0):
                                out_str = out_str+file_sep
                                out_str = out_str+temp_list_0[0]
                                out_str = out_str+file_sub_sep
                                out_str = out_str+temp_list_0[1]  
                                out_str = out_str+file_sub_sep
                                out_str = out_str+temp_list_0[2]      
                            else:
                                temp_bool = False
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
            else:
                temp_bool = False
        if temp_bool:
            if isinstance(in_date_list, list) | isinstance(in_date_list, tuple):
                if len(in_date_list) == 2:
                    if isinstance(in_date_list[0], str) & isinstance(in_date_list[1], str):
                        temp_str_5 = in_date_list[0].strip()
                        if len(temp_str_5) == 10:
                            if not temp_str_5[0] in numeric_digits:
                                temp_bool = False 
                            elif not temp_str_5[1] in numeric_digits:
                                temp_bool = False  
                            elif not temp_str_5[2] in numeric_digits:
                                temp_bool = False  
                            elif not temp_str_5[3] in numeric_digits:
                                temp_bool = False 
                            elif temp_str_5[4] != "-":
                                temp_bool = False   
                            elif not temp_str_5[5] in numeric_digits:
                                temp_bool = False  
                            elif not temp_str_5[6] in numeric_digits:
                                temp_bool = False  
                            elif temp_str_5[7] != "-":
                                temp_bool = False   
                            elif not temp_str_5[8] in numeric_digits:
                                temp_bool = False  
                            elif not temp_str_5[9] in numeric_digits:
                                temp_bool = False 
                            if temp_bool:
                                temp_num_0 = int(temp_str_5[0:4])
                                temp_num_1 = int(temp_str_5[5:7])
                                temp_num_2 = int(temp_str_5[8:10])
                        else:
                            temp_bool = False
                        if temp_bool:
                            temp_str_6 = in_date_list[1].strip()
                            if len(temp_str_6) == 5:
                                if not temp_str_6[0] in numeric_digits:
                                    temp_bool = False  
                                elif not temp_str_6[1] in numeric_digits:
                                    temp_bool = False 
                                elif temp_str_6[2] != ":":
                                    temp_bool = False   
                                elif not temp_str_6[3] in numeric_digits:
                                    temp_bool = False  
                                elif not temp_str_6[4] in numeric_digits:
                                    temp_bool = False  
                                if temp_bool:
                                    temp_num_3 = int(temp_str_6[0:2])
                                    temp_num_4 = int(temp_str_6[3:5])
                            else:
                                temp_bool = False  
                        if temp_bool:
                            if self.num_mix_valid(temp_str_0, temp_str_2, temp_str_3, 
                                                  temp_num_0, temp_num_1, temp_num_2, 
                                                  temp_num_3, temp_num_4):
                                out_str = out_str+file_sep
                                out_str = out_str+temp_str_5
                                out_str = out_str+file_sub_sep
                                out_str = out_str+temp_str_6
                            else:
                                temp_bool = False
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
            else:
                temp_bool = False
        if temp_bool:
            if isinstance(in_org_list, list) | isinstance(in_org_list, tuple):
                if len(in_org_list) == 4:
                    if (isinstance(in_org_list[0], str) & isinstance(in_org_list[1], str) &
                        isinstance(in_org_list[2], str) & isinstance(in_org_list[3], str)):
                        temp_str_2 = in_org_list[0].strip()
                        if self.num_member_valid(temp_str_1, temp_str_0, 
                                                 temp_str_4, temp_str_2):
                            temp_str_5 = in_org_list[1].strip()
                            if len(temp_str_5) == 10:
                                if not temp_str_5[0] in numeric_digits:
                                    temp_bool = False 
                                elif not temp_str_5[1] in numeric_digits:
                                    temp_bool = False  
                                elif not temp_str_5[2] in numeric_digits:
                                    temp_bool = False  
                                elif not temp_str_5[3] in numeric_digits:
                                    temp_bool = False 
                                elif temp_str_5[4] != "-":
                                    temp_bool = False   
                                elif not temp_str_5[5] in numeric_digits:
                                    temp_bool = False  
                                elif not temp_str_5[6] in numeric_digits:
                                    temp_bool = False  
                                elif temp_str_5[7] != "-":
                                    temp_bool = False   
                                elif not temp_str_5[8] in numeric_digits:
                                    temp_bool = False  
                                elif not temp_str_5[9] in numeric_digits:
                                    temp_bool = False 
                                if temp_bool:
                                    temp_num_5 = int(temp_str_5[0:4])
                                    temp_num_6 = int(temp_str_5[5:7])
                                    temp_num_7 = int(temp_str_5[8:10])
                            else:
                                temp_bool = False
                            if temp_bool:
                                temp_str_6 = in_org_list[2].strip()
                                if len(temp_str_6) == 5:
                                    if not temp_str_6[0] in numeric_digits:
                                        temp_bool = False  
                                    elif not temp_str_6[1] in numeric_digits:
                                        temp_bool = False 
                                    elif temp_str_6[2] != ":":
                                        temp_bool = False   
                                    elif not temp_str_6[3] in numeric_digits:
                                        temp_bool = False  
                                    elif not temp_str_6[4] in numeric_digits:
                                        temp_bool = False  
                                    if temp_bool:
                                        temp_num_8 = int(temp_str_6[0:2])
                                        temp_num_9 = int(temp_str_6[3:5])
                                        if temp_num_5 > temp_num_0:
                                            temp_bool = False
                                        elif temp_num_5 == temp_num_0:
                                            if temp_num_6 > temp_num_1:
                                                temp_bool = False
                                            elif temp_num_6 == temp_num_1:
                                                if temp_num_7 > temp_num_2:
                                                    temp_bool = False
                                                elif temp_num_7 == temp_num_2:
                                                    if temp_num_8 > temp_num_3:
                                                        temp_bool = False
                                                    elif temp_num_8 == temp_num_3:
                                                        if temp_num_9 > temp_num_4:
                                                            temp_bool = False
                                else:
                                    temp_bool = False  
                            if temp_bool:
                                if self.num_organization_valid(temp_str_2,  
                                                               temp_num_5, temp_num_6, temp_num_7, 
                                                               temp_num_8, temp_num_9):
                                    temp_str_3 = in_org_list[3].strip()
                                    if self.number_manipulation_valid(temp_str_3, temp_str_2):
                                        out_str = out_str+file_sep
                                        out_str = out_str+temp_str_2
                                        out_str = out_str+file_sub_sep
                                        out_str = out_str+temp_str_5
                                        out_str = out_str+file_sub_sep
                                        out_str = out_str+temp_str_6
                                        out_str = out_str+file_sub_sep
                                        out_str = out_str+temp_str_3
                                    else:
                                        temp_bool = False
                                else:
                                    temp_bool = False
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
            else:
                temp_bool = False
        if not temp_bool:
            out_str = None
        return out_str
    
    def reading_str_text_mem(self, in_str):
        # reading string text of organization
        
        # input: in_str, string   
        
        # output: out_list = [out_num_list, 
        #                     out_en_name_list, 
        #                     out_vn_name_list, 
        #                     out_date_list, 
        #                     out_org_list]
        
        file_read_sep = ";"+"\u0009"
        file_sub_sep = ","+"\u0009" 
        numeric_digits = ("0", "1", "2", "3", "4", 
                          "5", "6", "7", "8", "9")
        title_str = "member_info.iden"
        temp_bool = True   
        out_list = []
        if isinstance(in_str, str):
            temp_str_list_0 = in_str.split(file_read_sep)
            temp_len_0 = len(temp_str_list_0)
            if temp_len_0 == 6:
                temp_str_0 = temp_str_list_0[0].strip()
                if temp_str_0 == title_str:
                    temp_str_list_1 = temp_str_list_0[1].split(file_sub_sep)
                    if len(temp_str_list_1) == 2:
                        temp_str_1 = temp_str_list_1[0].strip()
                        temp_str_2 = temp_str_list_1[1].strip()
                        if (len(temp_str_1) == 21) & (len(temp_str_2) == 14):
                            out_list.append((temp_str_1, temp_str_2))
                            temp_str_list_1 = temp_str_list_0[2].split(file_sub_sep)
                            if len(temp_str_list_1) == 3:
                                temp_str_1 = temp_str_list_1[0].strip()
                                temp_str_2 = temp_str_list_1[1].strip()
                                temp_str_3 = temp_str_list_1[2].strip()
                                temp_tuple_0 = (temp_str_1, temp_str_2, temp_str_3)
                                if self.English_name_valid(temp_tuple_0):
                                    out_list.append(temp_tuple_0)
                                    temp_str_list_1 = temp_str_list_0[3].split(file_sub_sep)
                                    if len(temp_str_list_1) == 3:
                                        temp_str_1 = temp_str_list_1[0].strip()
                                        temp_str_2 = temp_str_list_1[1].strip()
                                        temp_str_3 = temp_str_list_1[2].strip()
                                        temp_tuple_0 = (temp_str_1, temp_str_2, temp_str_3)
                                        if self.virtual_name_valid(temp_tuple_0):
                                            out_list.append(temp_tuple_0)
                                            temp_str_list_1 = temp_str_list_0[4].split(file_sub_sep)
                                            if len(temp_str_list_1) == 2:
                                                temp_str_1 = temp_str_list_1[0].strip()
                                                if len(temp_str_1) == 10:
                                                    if not temp_str_1[0] in numeric_digits:
                                                        temp_bool = False 
                                                    elif not temp_str_1[1] in numeric_digits:
                                                        temp_bool = False  
                                                    elif not temp_str_1[2] in numeric_digits:
                                                        temp_bool = False  
                                                    elif not temp_str_1[3] in numeric_digits:
                                                        temp_bool = False 
                                                    elif temp_str_1[4] != "-":
                                                        temp_bool = False   
                                                    elif not temp_str_1[5] in numeric_digits:
                                                        temp_bool = False  
                                                    elif not temp_str_1[6] in numeric_digits:
                                                        temp_bool = False  
                                                    elif temp_str_1[7] != "-":
                                                        temp_bool = False   
                                                    elif not temp_str_1[8] in numeric_digits:
                                                        temp_bool = False  
                                                    elif not temp_str_1[9] in numeric_digits:
                                                        temp_bool = False 
                                                    if temp_bool:
                                                        temp_num_0 = int(temp_str_1[0:4])
                                                        temp_num_1 = int(temp_str_1[5:7])
                                                        temp_num_2 = int(temp_str_1[8:10])
                                                else:
                                                    temp_bool = False
                                                if temp_bool:
                                                    temp_str_2 = temp_str_list_1[1].strip()
                                                    if len(temp_str_2) == 5:
                                                        if not temp_str_2[0] in numeric_digits:
                                                            temp_bool = False  
                                                        elif not temp_str_2[1] in numeric_digits:
                                                            temp_bool = False 
                                                        elif temp_str_2[2] != ":":
                                                            temp_bool = False   
                                                        elif not temp_str_2[3] in numeric_digits:
                                                            temp_bool = False  
                                                        elif not temp_str_2[4] in numeric_digits:
                                                            temp_bool = False  
                                                        if temp_bool:
                                                            temp_num_3 = int(temp_str_2[0:2])
                                                            temp_num_4 = int(temp_str_2[3:5])
                                                    else:
                                                        temp_bool = False  
                                                if temp_bool:
                                                    if self.num_mix_valid(out_list[0][0], out_list[1][0], out_list[1][2], 
                                                                          temp_num_0, temp_num_1, temp_num_2, 
                                                                          temp_num_3, temp_num_4):
                                                        out_list.append((temp_str_1, temp_str_2))
                                                    else:
                                                        temp_bool = False
                                                if temp_bool:
                                                    temp_str_list_1 = temp_str_list_0[5].split(file_sub_sep)
                                                    if len(temp_str_list_1) == 4:
                                                        temp_str_1 = temp_str_list_1[1].strip()
                                                        if len(temp_str_1) == 10:
                                                            if not temp_str_1[0] in numeric_digits:
                                                                temp_bool = False 
                                                            elif not temp_str_1[1] in numeric_digits:
                                                                temp_bool = False  
                                                            elif not temp_str_1[2] in numeric_digits:
                                                                temp_bool = False  
                                                            elif not temp_str_1[3] in numeric_digits:
                                                                temp_bool = False 
                                                            elif temp_str_1[4] != "-":
                                                                temp_bool = False   
                                                            elif not temp_str_1[5] in numeric_digits:
                                                                temp_bool = False  
                                                            elif not temp_str_1[6] in numeric_digits:
                                                                temp_bool = False  
                                                            elif temp_str_1[7] != "-":
                                                                temp_bool = False   
                                                            elif not temp_str_1[8] in numeric_digits:
                                                                temp_bool = False  
                                                            elif not temp_str_1[9] in numeric_digits:
                                                                temp_bool = False 
                                                            if temp_bool:
                                                                temp_num_5 = int(temp_str_1[0:4])
                                                                temp_num_6 = int(temp_str_1[5:7])
                                                                temp_num_7 = int(temp_str_1[8:10])
                                                        else:
                                                            temp_bool = False
                                                        if temp_bool:
                                                            temp_str_2 = temp_str_list_1[2].strip()
                                                            if len(temp_str_2) == 5:
                                                                if not temp_str_2[0] in numeric_digits:
                                                                    temp_bool = False  
                                                                elif not temp_str_2[1] in numeric_digits:
                                                                    temp_bool = False 
                                                                elif temp_str_2[2] != ":":
                                                                    temp_bool = False   
                                                                elif not temp_str_2[3] in numeric_digits:
                                                                    temp_bool = False  
                                                                elif not temp_str_2[4] in numeric_digits:
                                                                    temp_bool = False  
                                                                if temp_bool:
                                                                    temp_num_8 = int(temp_str_2[0:2])
                                                                    temp_num_9 = int(temp_str_2[3:5])
                                                                    if temp_num_5 > temp_num_0:
                                                                        temp_bool = False
                                                                    elif temp_num_5 == temp_num_0:
                                                                        if temp_num_6 > temp_num_1:
                                                                            temp_bool = False
                                                                        elif temp_num_6 == temp_num_1:
                                                                            if temp_num_7 > temp_num_2:
                                                                                temp_bool = False
                                                                            elif temp_num_7 == temp_num_2:
                                                                                if temp_num_8 > temp_num_3:
                                                                                    temp_bool = False
                                                                                elif temp_num_8 == temp_num_3:
                                                                                    if temp_num_9 > temp_num_4:
                                                                                        temp_bool = False
                                                            else:
                                                                temp_bool = False  
                                                        if temp_bool:
                                                            temp_str_3 = temp_str_list_1[0].strip()
                                                            temp_str_4 = temp_str_list_1[3].strip()
                                                            if self.number_manipulation_valid(temp_str_4, temp_str_3):
                                                                if self.num_organization_valid(temp_str_3,  
                                                                                               temp_num_5, temp_num_6, temp_num_7, 
                                                                                               temp_num_8, temp_num_9):
                                                                    if self.num_member_valid(out_list[0][1], out_list[0][0], 
                                                                                             out_list[2][1], temp_str_3):
                                                                        out_list.append((temp_str_3, temp_str_1, 
                                                                                         temp_str_2, temp_str_4))
                                                                    else:
                                                                        temp_bool = False
                                                                else:
                                                                    temp_bool = False
                                                            else:
                                                                temp_bool = False
                                                    else:
                                                        temp_bool = False
                                            else:
                                                temp_bool = False
                                        else:
                                            temp_bool = False
                                    else:
                                        temp_bool = False
                                else:
                                    temp_bool = False
                            else:
                                temp_bool = False
                        else:
                            temp_bool = False
                    else:
                        temp_bool = False
                else:
                    temp_bool = False
            else:
                temp_bool = False
        else:
            temp_bool = False
        if not temp_bool:
            out_list = None
        return out_list
    
    def forming_str_text_member_lang(self, 
                                     in_num_list, in_en_name_list, 
                                     in_vn_name_list, in_date_list, 
                                     in_org_list, 
                                     if_out_en = False, 
                                     if_out_zhs = False, 
                                     if_out_zht = False):
        temp_bool = True
        temp_str_0 = self.forming_str_text_member(in_num_list, in_en_name_list, 
                                                  in_vn_name_list, in_date_list, 
                                                  in_org_list)
        if not temp_str_0 is None:
            temp_list_0 = self.reading_str_text_mem(temp_str_0)
            if not temp_list_0 is None:
                out_list = [temp_str_0]
                if if_out_en:
                    temp_str_en = ""
                    temp_str_en = temp_str_en+"1. The number: "
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"1.1 The initial 3 digits, "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[0][0][:3].upper()
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"1.2 Mixed number (21 digits), "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[0][0]
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"1.3 Member number (14 digits), "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[0][1]
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"1.4 Issued date (UTC, Coordinated Universal Time) (YYYY-MM-DD), "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[3][0]
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"1.5 Issued time (UTC, Coordinated Universal Time) (hh:mm, 24-hour), "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[3][1]
                    temp_str_en = temp_str_en+"\n\n\n\n"
                    temp_str_en = temp_str_en+"2. English name:"
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"2.1 Given name, "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[1][0]
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"2.2 Middle name, "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[1][1]
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"2.3 Family name, "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[1][2]
                    temp_str_en = temp_str_en+"\n\n\n\n"
                    temp_str_en = temp_str_en+"3. Another name / virtual name:"
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"3.1 type, "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[2][0]
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"3.2 Name, "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[2][1]
                    temp_str_en = temp_str_en+"\n\n"
                    temp_str_en = temp_str_en+"3.3 Addition (@ or #), "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[2][2]
                    temp_str_en = temp_str_en+"\n\n\n\n"
                    temp_str_en = temp_str_en+"4. Issuer:"
                    temp_str_en = temp_str_en+"\n\n"                    
                    temp_str_en = temp_str_en+"4.1 Manipulation number (7 digits), "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[4][3]
                    temp_str_en = temp_str_en+"\n\n"                    
                    temp_str_en = temp_str_en+"4.2 Organization number (14 digits), "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[4][0]
                    temp_str_en = temp_str_en+"\n\n"                    
                    temp_str_en = temp_str_en+"4.3 Created date of the organization (UTC, Coordinated Universal Time) (YYYY-MM-DD), "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[4][1]
                    temp_str_en = temp_str_en+"\n\n"                    
                    temp_str_en = temp_str_en+"4.4 Created time of the organization (UTC, Coordinated Universal Time) (hh:mm, 24-hour), "
                    temp_str_en = temp_str_en+"\n"
                    temp_str_en = temp_str_en+temp_list_0[4][2]
                    temp_str_en = temp_str_en+"\n\n\n"
                    temp_str_en = temp_str_en+"-------Do not modify anything before this line, or the *.txt file cannot be identified by the Application.-------"
                    temp_str_en = temp_str_en+"\n\n\n"
                    temp_str_en = temp_str_en+self.rule_str_en
                    out_list.append(temp_str_en)
                else:
                    out_list.append(None)
                if if_out_zhs:
                    temp_str_zhs = ""                    
                    temp_str_zhs = temp_str_zhs+"1. 编号："
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"1.1 初始3个数位，"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[0][0][:3].upper()
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"1.2 混合编号（mixed number，21个数位），"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[0][0]
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"1.3 成员编号（member number，14个数位），"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[0][1]
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"1.4 发行日期（UTC，世界协调时间）（年-月-日），"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[3][0]
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"1.5 发行时间（UTC，世界协调时间）（时:分，24小时制），"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[3][1]
                    temp_str_zhs = temp_str_zhs+"\n\n\n\n"
                    temp_str_zhs = temp_str_zhs+"2. 英文名字："
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"2.1 名，"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[1][0]
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"2.2 中间名，"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[1][1]
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"2.3 姓，"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[1][2]
                    temp_str_zhs = temp_str_zhs+"\n\n\n\n"
                    temp_str_zhs = temp_str_zhs+"3. 其他名字 / 虚拟名字："
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"3.1 类型，"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[2][0]
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"3.2 名字，"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[2][1]
                    temp_str_zhs = temp_str_zhs+"\n\n"
                    temp_str_zhs = temp_str_zhs+"3.3 附加（@或#），"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[2][2]
                    temp_str_zhs = temp_str_zhs+"\n\n\n\n"
                    temp_str_zhs = temp_str_zhs+"4. 发行方："
                    temp_str_zhs = temp_str_zhs+"\n\n"                    
                    temp_str_zhs = temp_str_zhs+"4.1 操作编号（manipulation number，7个数位），"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[4][3]
                    temp_str_zhs = temp_str_zhs+"\n\n"                    
                    temp_str_zhs = temp_str_zhs+"4.2 组织编号（organization number，14个数位），"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[4][0]
                    temp_str_zhs = temp_str_zhs+"\n\n"                    
                    temp_str_zhs = temp_str_zhs+"4.3 该组织的创建日期（UTC，世界协调时间）（年-月-日），"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[4][1]
                    temp_str_zhs = temp_str_zhs+"\n\n"                    
                    temp_str_zhs = temp_str_zhs+"4.4 该组织的创建时间（UTC，世界协调时间）（时:分，24小时制），"
                    temp_str_zhs = temp_str_zhs+"\n"
                    temp_str_zhs = temp_str_zhs+temp_list_0[4][2]
                    temp_str_zhs = temp_str_zhs+"\n\n\n"
                    temp_str_zhs = temp_str_zhs+"-------请勿修改此行之前的任何内容，否则应用程序无法识别该*。txt文件。-------"
                    temp_str_zhs = temp_str_zhs+"\n\n\n"
                    temp_str_zhs = temp_str_zhs+self.forming_rule_str_zhs()
                    out_list.append(temp_str_zhs)
                else:
                    out_list.append(None)
                if if_out_zht:
                    temp_str_zht = ""
                    temp_str_zht = temp_str_zht+"1. 編號："
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"1.1 初始3個數位，"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[0][0][:3].upper()
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"1.2 混合編號（mixed number，21個數位），"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[0][0]
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"1.3 成員編號（member number，14個數位），"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[0][1]
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"1.4 發行日期（UTC，世界協調時間）（年-月-日），"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[3][0]
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"1.5 發行時間（UTC，世界協調時間）（時:分，24小時制），"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[3][1]
                    temp_str_zht = temp_str_zht+"\n\n\n\n"
                    temp_str_zht = temp_str_zht+"2. 英文名字："
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"2.1 名，"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[1][0]
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"2.2 中間名，"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[1][1]
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"2.3 姓，"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[1][2]
                    temp_str_zht = temp_str_zht+"\n\n\n\n"
                    temp_str_zht = temp_str_zht+"3. 其他名字 / 虛擬名字："
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"3.1 類型，"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[2][0]
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"3.2 名字，"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[2][1]
                    temp_str_zht = temp_str_zht+"\n\n"
                    temp_str_zht = temp_str_zht+"3.3 附加（@或#），"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[2][2]
                    temp_str_zht = temp_str_zht+"\n\n\n\n"
                    temp_str_zht = temp_str_zht+"4. 發行方："
                    temp_str_zht = temp_str_zht+"\n\n"                    
                    temp_str_zht = temp_str_zht+"4.1 操作編號（manipulation number，7個數位），"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[4][3]
                    temp_str_zht = temp_str_zht+"\n\n"                    
                    temp_str_zht = temp_str_zht+"4.2 組織編號（organization number，14個數位），"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[4][0]
                    temp_str_zht = temp_str_zht+"\n\n"                    
                    temp_str_zht = temp_str_zht+"4.3 該組織的創建日期（UTC，世界協調時間）（年-月-日），"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[4][1]
                    temp_str_zht = temp_str_zht+"\n\n"                    
                    temp_str_zht = temp_str_zht+"4.4 該組織的創建時間（UTC，世界協調時間）（時:分，24小時制），"
                    temp_str_zht = temp_str_zht+"\n"
                    temp_str_zht = temp_str_zht+temp_list_0[4][2]
                    temp_str_zht = temp_str_zht+"\n\n\n"
                    temp_str_zht = temp_str_zht+"-------請勿修改此行之前的任何內容，否則應用程式無法識別該*.txt檔。-------"
                    temp_str_zht = temp_str_zht+"\n\n\n"
                    temp_str_zht = temp_str_zht+self.forming_rule_str_zht()
                    out_list.append(temp_str_zht)
                else:
                    out_list.append(None)
            else:
                temp_bool = False
        else:
            temp_bool = False
        if not temp_bool:
            out_list = None
        return out_list
    
    def forming_rule_str_zhs(self):
        temp_str_0 = "在此应用程序中生成编号的简化规则"
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"1. 有4种编号："
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 混合编号（Mixed number），属于人的编号，并且有21个数位，每个数位有64个不同的值；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 成员编号（Member number），属于人的编号，并且有14个数位，每个数位有16个不同的值；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 组织编号（Organization number），属于组织的编号，并且有14个数位，每个数位有64个不同的值；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) 操作编号（Manipulation number），属于组织的编号，并且有7个数位，每个数位有16个不同的值。"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    在这4种类型中："
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 每个数位有16个值的编号是一个十六进制数，每个数位来自数字0-9和{'A'，'B'，'C'，'D'，'E'，'F'}（不区分大写或小写字母）；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 对于16个值的数位，映射是从{'5', 'B', '7', 'F', '0', 'C', '2', 'D', 'E', '9', '3', '1', '4', '8', '6', 'A'}至0-15；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 每个数位有64个值的编号是一些字符的混合体，每个数位来自26个英文大写字母、26个英文小写字母、数字0-9和{'+', '-'}；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) 对于64个值的数位，映射是从{'G', 'B', 'l', 'A', 'r', 's', '6', 'X', 'c', 'K', 'R', 'Q', 'I', 'x', 'h', 'b', "
        temp_str_0 = temp_str_0+"'i', 'f', 'o', 'a', 'M', 'S', 'w', '0', 'P', 'v', '3', 'N', 't', 'g', '8', '2', '+', '-', '4', 'k', '7', 'e', 'n', 'D', "
        temp_str_0 = temp_str_0+"'V', 'y', 'U', 'W', 'F', 'L', 'd', 'T', '1', 'J', 'u', 'Z', 'z', 'C', 'Y', '9', 'm', 'H', 'O', 'E', '5', 'p', 'j', 'q'}至0-63。"
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"2. 混合编号（Mixed number）"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 混合编号的设计中含有大量的可能编号，目的是如果发行方被分开，那么他们可以在概率上发行不同的编号；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 前3个数位来自英文字母的组合（根据发行方的前3个数位），并根据大写和/或小写的不同有8种；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 最后一个数位是其他20个数位之和除以64的余数；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) 从第4个数位至第20个数位的组合编码了发行日期、发行时间、英文名的前2个字母、英文姓的前2个字母；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (5) 对于英文名的前2个字母、英文姓的前2个字母的每一种情况，在同一分钟内有1.405669E+16个不同的混合编号；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (6) 对于2个人，如果他们的英文名的前2个字母和英文姓的前2个字母不相同，他们的混合编号必然是不同的；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (7) 对于2个人，如果他们的混合编号是在不同的分钟（UTC）发行出来的，他们的混合编号必然是不同的；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (8) 如果英文名字为空，这样也可以输出混合编号。"
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"3. 成员编号（Member number）"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 成员编号的设计具有比混合编号更少的可能数量，以便人们可以记住成员编号；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 前4个数位的组合编码了混合编号的一些数位；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 第5个和第6个数位的组合对发行方的组织编号的一些数位进行编码；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) 第7个和第8个数位的组合对其他名字/虚拟名字的前2个字符的Unicode的一些数位进行编码；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (5) 从第8个数位至第13个数位的组合编码了发行日期、发行时间；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (6) 如果成员的英文名字不为空，则最后一个数位是其他13个数位之和除以15的余数；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (7) 如果成员的英文名字为空，则最后一个数位固定为'A'，根据映射也就是15;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (8) 2个人的成员编号在概率上可能相同。"
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"4. 组织编号（Organization number）"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 组织编号的设计中含有大量的可能编号，目的是如果同一联盟/国家的发行方被分开，则其他一些发行方也能够产生并且会在概率上得到不同的组织编号;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 前3个数位来自英文字母的组合（用来显示这些组织属于哪个联盟/国家），并根据大写和/或小写的不同有8种；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 最后一个数位是其他13个数位之和除以64的余数；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) 从第4个数位至第13个数位的组合编码了创建日期、创建时间；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (5) 在每分钟内有1.662640E+9个不同的组织编号；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (6) 对于2个组织，如果他们的组织编号是在不同的分钟（UTC）创建出来的，他们的组织编号必然是不同的。"
        temp_str_0 = temp_str_0+"\n\n\n\n"        
        temp_str_0 = temp_str_0+"5. 操作编号（Manipulation number）"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 操作编号是便利于操作者记忆而设计的，也是为了让其他组织搜索混合编号和/或成员编号的确切发行者而设计的；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 所有7个数位作为组合编码了组织编号的一些数位；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 在一个组织内，只有1271个是有效的。"
        temp_str_0 = temp_str_0+"\n\n\n\n" 
        return temp_str_0
    
    def forming_rule_str_zht(self):
        temp_str_0 = "在此應用程式中生成編號的簡化規則"
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"1. 有4種編號："
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 混合編號（Mixed number），屬於人的編號，並且有21個數位，每個數位有64個不同的值；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 成員編號（Member number），屬於人的編號，並且有14個數位，每個數位有16個不同的值；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 組織編號（Organization number），屬於組織的編號，並且有14個數位，每個數位有64個不同的值；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) 操作編號（Manipulation number），屬於組織的編號，並且有7個數位，每個數位有16個不同的值。"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    在這4種類型中："
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 每個數位有16個值的編號是一個十六進位數，每個數位來自數字0-9和{'A'，'B'，'C'，'D'，'E'，'F'}（不區分大寫或小寫字母）；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 對於16個值的數位，映射是從{'5', 'B', '7', 'F', '0', 'C', '2', 'D', 'E', '9', '3', '1', '4', '8', '6', 'A'}至0-15；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 每個數位有64個值的編號是一些字元的混合體，每個數位來自26個英文大寫字母、26個英文小寫字母、數字0-9和{'+', '-'}；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) 對於64個值的數位，映射是從{'G', 'B', 'l', 'A', 'r', 's', '6', 'X', 'c', 'K', 'R', 'Q', 'I', 'x', 'h', 'b', "
        temp_str_0 = temp_str_0+"'i', 'f', 'o', 'a', 'M', 'S', 'w', '0', 'P', 'v', '3', 'N', 't', 'g', '8', '2', '+', '-', '4', 'k', '7', 'e', 'n', 'D', "
        temp_str_0 = temp_str_0+"'V', 'y', 'U', 'W', 'F', 'L', 'd', 'T', '1', 'J', 'u', 'Z', 'z', 'C', 'Y', '9', 'm', 'H', 'O', 'E', '5', 'p', 'j', 'q'}至0-63。"
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"2. 混合編號（Mixed number）"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 混合編號的設計中含有大量的可能編號，目的是如果發行方被分開，那麼他們可以在概率上發行不同的編號；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 前3個數位來自英文字母的組合（根據發行方的前3個數位），並根據大寫和/或小寫的不同有8種；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 最後一個數位是其他20個數位之和除以64的餘數；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) 從第4個數位至第20個數位的組合編碼了發行日期、發行時間、英文名的前2個字母、英文姓的前2個字母；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (5) 對於英文名的前2個字母、英文姓的前2個字母中的每一種情況，在同一分鐘內有1.405669E+16個不同的混合編號；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (6) 對於2個人，如果他們的英文名的前2個字母和英文姓的前2個字母不相同，他們的混合編號必然是不同的;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (7) 對於2個人，如果他們的混合編號是在不同的分鐘（UTC）發行出來的，他們的混合編號必然是不同的;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (8) 如果英文名字為空，這樣也可以輸出混合編號。"
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"3. 成員編號（Member number）"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 成員編號的設計具有比混合編號更少的可能數量，以便人們可以記住成員編號；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 前4個數位的組合編碼了混合編號的一些數位；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 第5個和第6個數位的組合對發行方的組織編號的一些數位進行編碼；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) 第7個和第8個數位的組合對其他名字/虛擬名字的前2個字元的Unicode的一些數位進行編碼；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (5) 從第9個數位至第13個數位的組合編碼了發行日期、發行時間；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (6) 如果成員的英文名字不為空，則最後一個數位是其他13個數位之和除以15的餘數;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (7) 如果成員的英文名字為空，則最後一個數位固定為'A'，根據映射也就是15;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (8) 2個人的成員編號在概率上可能相同。"
        temp_str_0 = temp_str_0+"\n\n\n\n"
        temp_str_0 = temp_str_0+"4. 組織編號（Organization number）"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 組織編號的設計中含有大量的可能編號，目的是如果同一聯盟/國家的發行方被分開，則其他一些發行方也能夠產生並且會在概率上得到不同的組織編號;"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 前3個數位來自英文字母的組合（用來顯示這些組織屬於哪個聯盟/國家），並根據大寫和/或小寫的不同有8種；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 最後一個數位是其他13個數位之和除以64的餘數；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (4) 從第4個數位至第13個數位的組合編碼了創建日期、創建時間；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (5) 在每分鐘內有1.662640E+9個不同的組織編號；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (6) 對於2個組織，如果他們的組織編號是在不同的分鐘（UTC）創建出來的，他們的組織編號必然是不同的。"
        temp_str_0 = temp_str_0+"\n\n\n\n"        
        temp_str_0 = temp_str_0+"5. 操作編號（Manipulation number）"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (1) 操作號碼是便利於操縱者記憶而設計的，也是為了讓其他組織搜索混合編號和/或成員編號的確切發行者而設計的；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (2) 所有7個數位作為組合編碼了組織編號的一些數位；"
        temp_str_0 = temp_str_0+"\n"
        temp_str_0 = temp_str_0+"    (3) 在一個組織內，只有1271個是有效的。"
        temp_str_0 = temp_str_0+"\n\n\n\n"  
        return temp_str_0
    
    def reading_str_text_member_lang(self, in_str):
        temp_bool = True
        temp_str_list_0 = in_str.split("\n")
        temp_len_0 = len(temp_str_list_0)
        if temp_len_0 >= 58:
            temp_str_list_1 = []
            for n in range(temp_len_0):
                temp_str_0 = temp_str_list_0[n].strip()
                temp_str_list_1.append(temp_str_0)
            if len(temp_str_list_1) >= 58:
                temp_str_0 = "member_info.iden"
                temp_str_0 = temp_str_0+self.dat_file_sep
                temp_str_0 = temp_str_0+temp_str_list_1[6]
                temp_str_0 = temp_str_0+self.dat_file_sub_sep
                temp_str_0 = temp_str_0+temp_str_list_1[9]
                temp_str_0 = temp_str_0+self.dat_file_sep
                temp_str_0 = temp_str_0+temp_str_list_1[22]
                temp_str_0 = temp_str_0+self.dat_file_sub_sep
                temp_str_0 = temp_str_0+temp_str_list_1[25]
                temp_str_0 = temp_str_0+self.dat_file_sub_sep
                temp_str_0 = temp_str_0+temp_str_list_1[28]
                temp_str_0 = temp_str_0+self.dat_file_sep
                temp_str_0 = temp_str_0+temp_str_list_1[35]
                temp_str_0 = temp_str_0+self.dat_file_sub_sep
                temp_str_0 = temp_str_0+temp_str_list_1[38]
                temp_str_0 = temp_str_0+self.dat_file_sub_sep
                temp_str_0 = temp_str_0+temp_str_list_1[41]
                temp_str_0 = temp_str_0+self.dat_file_sep
                temp_str_0 = temp_str_0+temp_str_list_1[12]
                temp_str_0 = temp_str_0+self.dat_file_sub_sep
                temp_str_0 = temp_str_0+temp_str_list_1[15]
                temp_str_0 = temp_str_0+self.dat_file_sep
                temp_str_0 = temp_str_0+temp_str_list_1[51]
                temp_str_0 = temp_str_0+self.dat_file_sub_sep
                temp_str_0 = temp_str_0+temp_str_list_1[54]
                temp_str_0 = temp_str_0+self.dat_file_sub_sep
                temp_str_0 = temp_str_0+temp_str_list_1[57]
                temp_str_0 = temp_str_0+self.dat_file_sub_sep
                temp_str_0 = temp_str_0+temp_str_list_1[48]
            else:
                temp_bool = False
        else:
            temp_bool = False
        if temp_bool:
            out_list = self.reading_str_text_mem(temp_str_0)
        else:
            out_list = None
        return out_list
    
    def csv_row_read(self, in_str):
        in_str = in_str.strip()
        temp_len = len(in_str)
        if temp_len > 0:
            temp_list_0 = []
            temp_str_0 = ""
            temp_bool_0 = True
            for n in range(temp_len):
                temp_str_1 = in_str[n]
                temp_num_1 = ord(temp_str_1)
                if (temp_num_1 >= 32) & (temp_num_1 < 65536):
                    if temp_bool_0:
                        if temp_str_1 == ",":
                            temp_list_0.append(temp_str_0)
                            temp_list_0.append("\t")
                            temp_str_0 = ""
                        elif temp_str_1 == '"':
                            temp_list_0.append(temp_str_0)
                            temp_str_0 = ""
                            temp_bool_0 = False
                        else:
                            temp_str_0 = temp_str_0+temp_str_1
                    else:
                        if temp_str_1 == '"':
                            temp_list_0.append(temp_str_0)
                            temp_str_0 = ""
                            temp_bool_0 = True
                        else:
                            temp_str_0 = temp_str_0+temp_str_1
            temp_list_0.append(temp_str_0)
            temp_len = len(temp_list_0)
            temp_list_1 = [temp_list_0[0]]
            temp_num_0 = 0
            for n in range(1, temp_len):
                if temp_list_0[n] != "\t":
                    temp_list_1[temp_num_0] = temp_list_1[temp_num_0]+temp_list_0[n]
                else:
                    temp_list_1.append("")
                    temp_num_0 += 1
            temp_len = len(temp_list_1)
            for n in range(temp_len):
                temp_str_0 = temp_list_1[n].strip()
                temp_bool_1 = True
                while temp_bool_1:
                    temp_num_1 = len(temp_str_0)
                    if temp_num_1 >= 2:
                        if (temp_str_0[0] == '"') & (temp_str_0[temp_num_1-1] == '"'):
                            temp_str_0 = temp_str_0[1:(temp_num_1-1)]
                        elif (temp_str_0[0] == "'") & (temp_str_0[temp_num_1-1] == "'"):
                            temp_str_0 = temp_str_0[1:(temp_num_1-1)]
                        else:
                            temp_bool_1 = False
                    else:
                        temp_bool_1 = False
                temp_list_1[n] = temp_str_0.strip()
            out_list = temp_list_1
        else:
            out_list = [""]
        return(out_list)





if __name__ == "__main__":
    App = app()    
    App.mainloop()