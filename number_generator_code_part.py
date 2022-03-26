# number generator & identifier
# writer: Shobaku

from random import uniform
from random import seed
from datetime import datetime

def number_mix_generate(in_list_name, in_initial_list):
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
            else:
                temp_bool_0 = False
        else:
            temp_bool_0 = False
    if not temp_bool_0:
        out_result = None
    return out_result

def num_mix_valid(mix_number, given_name = None, family_name = None, 
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

def num_mix_64_2_8(mix_number):
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

def num_mix_8_2_64(mix_number):
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

def number_organization_generate(in_list_name, in_initial_list):
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
                temp_bool_0 = False
        else:
            temp_bool_0 = False
    if not temp_bool_0:
        out_result = None
    return out_result

def num_organization_valid(organization_number, 
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

def num_organization_64_2_16(organization_number):
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

def num_organization_16_2_64(organization_number):
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

def number_manipulation_generate(organization_number):
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
    temp_bool = num_organization_valid(organization_number)
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

def number_manipulation_valid(manipulation_number, organization_number):
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
        out_bool = num_organization_valid(organization_number)
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

def number_member_generate(in_list_name):
    # to generate member number, 14 digits
    
    # input:
    # in_list_name = [[mix number 0, 
    #                  given name 0, family name 0, 
    #                  virtual name 0, 
    #                  organization number 0, 
    #                  date 0, time 0] / None, 
    #                 [mix number 1, 
    #                  given name 1, family name 1, 
    #                  virtual name 1, 
    #                  organization number 1, 
    #                  date 1, time 1] / None, 
    #                 [mix number 2, 
    #                  given name 2, family name 2, 
    #                  virtual name 2, 
    #                  organization number 2, 
    #                  date 2, time 2] / None, ...]
    
    # output:
    # out_result = [(out number 0, mix number 0, virtual name 0, organization number) / None,
    #               (out number 1, mix number 1, virtual name 1, organization number) / None,
    #               (out number 2, mix number 2, virtual name 2, organization number) / None, ...]
    
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
                                    if num_mix_valid(temp_list_0[0], temp_list_0[1], temp_list_0[2], 
                                                     year = temp_num_1_0, month = temp_num_1_1, day = temp_num_1_2, 
                                                     hour = temp_num_2_0, minute = temp_num_2_1):
                                        temp_bool = num_organization_valid(temp_list_0[4])                                    
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
        else:
            out_result = None
    else:
        out_result = None
    return out_result    

def num_member_valid(member_number, mix_number = None, 
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
            if num_mix_valid(mix_number):
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
                    temp_num_1 = int(round(temp_num_0/270, 1))
                    temp_num_0 = (temp_number_list_1[11]-temp_number_list_1[2])%64
                    temp_num_0 = temp_num_0*64+(temp_number_list_1[12]+temp_number_list_1[0])%64
                    temp_num_0 = temp_num_0*64+(temp_number_list_1[13]-temp_number_list_1[1])%64
                    temp_num_0 = temp_num_0*64+(temp_number_list_1[14]+temp_number_list_1[2])%64
                    temp_num_0 = temp_num_0%2707
                    temp_num_2 = int(round(temp_num_0/270, 1))
                    temp_num_0 = (temp_number_list_1[15]-temp_number_list_1[0])%64
                    temp_num_0 = temp_num_0*64+(temp_number_list_1[16]+temp_number_list_1[1])%64
                    temp_num_0 = temp_num_0*64+(temp_number_list_1[17]-temp_number_list_1[2])%64
                    temp_num_0 = temp_num_0*64+(temp_number_list_1[18]+temp_number_list_1[0])%64
                    temp_num_0 = temp_num_0*64+(temp_number_list_1[19]-temp_number_list_1[1])%64
                    temp_num_0 = temp_num_0%22343
                    temp_num_3 = int(round(temp_num_0/60, 1))
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
            if num_organization_valid(organization_number):
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

def forming_str_text_org(in_org_num, in_org_name, in_org_init_num, 
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
                    temp_bool = num_organization_valid(in_org_num, 
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
        out_str = out_str+num_organization_64_2_16(in_org_num)
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
                                        if number_manipulation_valid(temp_str_1, in_org_num):
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
                                                if English_name_valid([temp_str_3, temp_str_4, temp_str_5]):
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
                                                if virtual_name_valid([temp_str_3, temp_str_4, temp_str_5]):
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
                                            if num_organization_valid(temp_str_4, 
                                                                      temp_num_1, temp_num_2, temp_num_3, 
                                                                      temp_num_4, temp_num_5):
                                                if temp_str_2 == "en":
                                                    temp_bool_1 = num_member_valid(temp_str_1, 
                                                                                   organization_number = temp_str_4)
                                                else:
                                                    temp_bool_1 = num_member_valid(temp_str_1, 
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

def reading_str_text_org(in_str):
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
                                if num_organization_valid(org_info_list[0], 
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
                    if number_manipulation_valid(temp_str_list_2[0], org_info_list[0]):
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
                        if English_name_valid(temp_str_list_4):
                            if num_member_valid(temp_str_list_2[2], 
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
                        if virtual_name_valid(temp_str_list_4):
                            if num_member_valid(temp_str_list_2[2], 
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
                        if num_organization_valid(temp_str_list_2[7], 
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

def forming_str_text_member(in_num_list, in_en_name_list, 
                            in_vn_name_list, in_date_list, 
                            in_org_list):
    # forming string text of member
    
    # input: in_num_list, numbers, [mix number, member number]
    #        in_en_name_list, English name, [given, middle, family]
    #        in_vn_name_list, another name / virtual name, [type, name, addition]
    #        in_date_list, issuing date of member, [date, time]
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
                    if English_name_valid(temp_list_0):
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
                    if virtual_name_valid(temp_list_0):
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
                        if num_mix_valid(temp_str_0, temp_str_2, temp_str_3, 
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
                    if num_member_valid(temp_str_1, temp_str_0, 
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
                            if num_organization_valid(temp_str_2,  
                                                      temp_num_5, temp_num_6, temp_num_7, 
                                                      temp_num_8, temp_num_9):
                                temp_str_3 = in_org_list[3].strip()
                                if number_manipulation_valid(temp_str_3, temp_str_2):
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

def reading_str_text_mem(in_str):
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
                            if English_name_valid(temp_tuple_0):
                                out_list.append(temp_tuple_0)
                                temp_str_list_1 = temp_str_list_0[3].split(file_sub_sep)
                                if len(temp_str_list_1) == 3:
                                    temp_str_1 = temp_str_list_1[0].strip()
                                    temp_str_2 = temp_str_list_1[1].strip()
                                    temp_str_3 = temp_str_list_1[2].strip()
                                    temp_tuple_0 = (temp_str_1, temp_str_2, temp_str_3)
                                    if virtual_name_valid(temp_tuple_0):
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
                                                if num_mix_valid(out_list[0][0], out_list[1][0], out_list[1][2], 
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
                                                        if number_manipulation_valid(temp_str_4, temp_str_3):
                                                            if num_organization_valid(temp_str_3,  
                                                                                      temp_num_5, temp_num_6, temp_num_7, 
                                                                                      temp_num_8, temp_num_9):
                                                                if num_member_valid(out_list[0][1], out_list[0][0], 
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

def English_name_valid(in_list):
    English_name_capital = ("A", "B", "C", "D", "E", "F", "G", 
                            "H", "I", "J", "K", "L", "M", "N", 
                            "O", "P", "Q", "R", "S", "T", 
                            "U", "V", "W", "X", "Y", "Z")
    English_name_other = (" ", "-", "'")
    out_bool = True
    temp_len_0 = len(in_list[0])
    temp_len_1 = len(in_list[1])
    temp_len_2 = len(in_list[2])
    if temp_len_0 < 1:
        out_bool = (temp_len_1 < 1) & (temp_len_2 < 1)
    else:
        if temp_len_0 == 1:
            out_bool = in_list[0][0] in English_name_capital
        else:
            if in_list[0][0] in English_name_capital:
                for n in range(1, temp_len_0):
                    temp_str_0 = in_list[0][n].upper()
                    if ((not temp_str_0 in English_name_capital) & 
                        (not temp_str_0 in English_name_other)):
                        out_bool = False
                        break
            else:
                out_bool = False
        if out_bool:
            if temp_len_1 > 0:
                if temp_len_1 == 1:
                    out_bool = in_list[1][0] in English_name_capital
                else:
                    if in_list[1][0] in English_name_capital:
                        for n in range(1, temp_len_1):
                            temp_str_0 = in_list[1][n].upper()
                            if ((not temp_str_0 in English_name_capital) & 
                                (not temp_str_0 in English_name_other)):
                                out_bool = False
                                break
                    else:
                        out_bool = False
        if out_bool:
            if temp_len_2 > 0:
                if temp_len_2 == 1:
                    out_bool = in_list[2][0] in English_name_capital
                else:
                    if in_list[2][0] in English_name_capital:
                        for n in range(1, temp_len_2):
                            temp_str_0 = in_list[2][n].upper()
                            if ((not temp_str_0 in English_name_capital) & 
                                (not temp_str_0 in English_name_other)):
                                out_bool = False
                                break
                    else:
                        out_bool = False
    return out_bool

def virtual_name_valid(in_list):
    out_bool = True
    temp_len_1 = len(in_list[1])
    temp_len_2 = len(in_list[2])
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
    return out_bool




