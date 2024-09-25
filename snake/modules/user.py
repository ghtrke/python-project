def read_direction(last_direction):
    while(True):
        # TODO: 感觉应该另开一个进程读取用户输入 
        direction = read_user_input();
        return direction if direction else last_direction

