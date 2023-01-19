def solution(s):
    p_num = 0
    y_num = 0
    
    for i in s:
        if ('p' is i or 'P' is i):
            p_num += 1
        elif ('y' is i or 'Y' is i):
            y_num += 1
            
            
    return p_num is y_num