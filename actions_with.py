import calculate as cal



def action(act_num_1, act_num_2, act_op):
    if act_op == '+':
        return cal.my_sum(act_num_1, act_num_2)
    elif act_op == '-':
        return cal.my_dif(act_num_1, act_num_2)
    elif act_op == '*':
        return cal.my_multiply(act_num_1, act_num_2)
    elif act_op == '/':
        return cal.my_div(act_num_1, act_num_2)