def solution(amountText):
    answer = True  # return : boolean

    # 옳은 금액 : ','으로만 이루어져 있는 문자, 구분자 없어도 옳은 문자,
    #   오른쪽에서 시작햇을 때 세자리 구분자가 성립해야함
    # 옳지 않은 금액 : '원', '왼쪽에 0 없어야',

    def is_valid_amount_basic(amount):
        if set(amount) == {','}:
            return False

        if '원' in amount:
            return False

        if amount.startswith('0'):
            return False

        if amount.startswith(','):
            return False

        if amount.endswith(','):
            return False

        return True

    def is_valid_amount_three_sep(amount):
        flag = False
        if ',' in amount:
            if len(amount) < 5:
                return False
            # flag = True # , 가 포함되어 있는 amount
            for i in range(-1, -len(amount) - 1, -1):
                if amount[i] == ',':
                    if ((-1 * i) % 4 != 0):
                        return False
                if ((-1 * i) % 4) == 0:
                    if amount[i] != ',':
                        return False

        return True

    def is_valid_chracters(amount):
        valid_characters = set('0123456789,')
        for c in amount:
            if c not in valid_characters:
                return False
        return True

    if amountText == "0":
        return True
    if is_valid_amount_three_sep(amountText) == False or is_valid_amount_basic(
            amountText) == False or is_valid_chracters(amountText) == False:
        answer = False

    return answer