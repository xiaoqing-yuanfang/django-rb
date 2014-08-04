def values_copy(buf):
    import copy
    b = copy.deepcopy(buf)
    return b
def yes_or_not(prompt=None):
    try:
        prompt = prompt + "' yes or not':"
        s = raw_input(prompt)
        if(s == 'y' or 
           s == 'yes' or 
           s == 'Y' or 
           s == 'YES'):
            return True
        else:
            return False
    except:
        return False
 
def open_dir():
    import platform
    flag = yes_or_not(prompt="do you want to open the cur dir")
    if(flag == True):
        if(platform.system() == "Linux"):
            import os
            os.system("nautilus .")
        elif(platform.system() == "Windows"):
            import os
            os.system("start .")
def user_interface():
    import fenxi
    import search
    
    try:
        flag_gen_chart = yes_or_not("do you want to gen chart data")
        if(flag_gen_chart == 'y' or 
           flag_gen_chart == 'yes' or 
           flag_gen_chart == 'Y' or 
           flag_gen_chart == 'YES'):
            flag_gen_chart = True
        else:
            pass

    except:
        flag_gen_chart = False
        print("Don't gen  chart in default")
    
        
    i_from,i_to,i_len = search.from_and_to()
    print("all %d from %d to %d" %(i_len,i_from,i_to))
    
    
    fenxi.fenxi_from_to_cycle_rates(n=i_len,
                                    periods_from=i_from,
                                    periods_to=i_to,
                                    hits_rate_of_34=0.8, #here we consume it is 0.8
                                    flag_gen_chart=flag_gen_chart)
    print("all results have gen ok")
    open_dir()
    fenxi.fenxi_from_to_cycle_rates(n=13,
                                    periods_from=2013058,
                                    periods_to=2013049,
                                    hits_rate_of_34=0.8,
                                    flag_gen_chart=flag_gen_chart)
    
    if(flag_gen_chart == True):
        import chart_pdf_modified
        chart_pdf_modified.modify_pdf()
if(__name__ == '__main__'):
    user_interface()