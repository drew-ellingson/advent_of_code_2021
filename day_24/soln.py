# -------------------- Read File ----------------------


class Instruction:
    def __init__(self, instr_text):
        type, *params = instr_text.strip().split(" ")
        params = [int(x) if not x in "wxyz" else x for x in params]

        self.type = type
        self.params = params

    def __repr__(self):
        return f"{self.type} {self.params}"


class ArithmeticLogicUnit:
    def __init__(self, instructions):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0

        self.instructions = instructions
        self.instr_num = 0

    def __repr__(self):
        try:
            curr_instr = self.instructions[self.instr_num]
        except IndexError:
            curr_instr = 'None'
        msg = f"instr_num: {self.instr_num}\ncurr_instr: {curr_instr}\nw: {self.w}\nx: {self.x}\ny: {self.y}\nz: {self.z}"
        return msg

    def get_param_val(self, val):
        if type(val) == int:
            return val
        return getattr(self, val)

    def inp(self, params, input_val):
        setattr(self, params[0], input_val)

    def add(self, params):
        setattr(
            self,
            params[0],
            self.get_param_val(params[0]) + self.get_param_val(params[1]),
        )

    def mul(self, params):
        setattr(
            self,
            params[0],
            self.get_param_val(params[0]) * self.get_param_val(params[1]),
        )

    def div(self, params):
        setattr(
            self,
            params[0],
            self.get_param_val(params[0]) // self.get_param_val(params[1]),
        )

    def mod(self, params):
        setattr(
            self,
            params[0],
            self.get_param_val(params[0]) % self.get_param_val(params[1]),
        )

    def eql(self, params):
        setattr(
            self,
            params[0],
            1 if self.get_param_val(params[0]) == self.get_param_val(params[1]) else 0,
        )

    def test_model_num(self, model_num):
        model_num = str(model_num)
        for ins in self.instructions:
            ins_func = getattr(self, ins.type)
            if ins_func == self.inp:
                ins_func(ins.params, int(model_num[0]))
                model_num = model_num[1:]
            else:
                ins_func(ins.params)
            self.instr_num += 1
        return self.z == 0

    def reset(self):
        self.w == 0
        self.x == 0
        self.y == 0
        self.z == 0
        self.instr_num = 0


if __name__=="__main__":
    with open('day_24/input.txt') as in_file:
        instructions = [Instruction(line) for line in in_file.readlines()]

    max_num = 99_999_999_999_999
    max_num = 99_999_978_702_000
    # got through 99999978702000 with min_val 459 @ 99999985303046

    achieved_min_val = max_num
    min_val = 1e100

    while not (done := False):
        if max_num % 1000 == 0:
            print(f'Current Max Num: {max_num}\nCurrent Min Val: {min_val} achieved at: {achieved_min_val}\n')
        
        alu = ArithmeticLogicUnit(instructions)
        done = alu.test_model_num(max_num)
        
        if alu.z <= min_val:
            min_val = alu.z 
            achieved_min_val = max_num
        
        max_num -= 1

    print(f'P1 Soln: {max_num + 1}')    



# -------------------- P2 -----------------------------
