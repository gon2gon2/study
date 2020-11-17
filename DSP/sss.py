# 맞는 문자 타입이 아니라고 반환해주는 오류 클래스
class InvalidIntException(Exception):
    def __init__(self,arg):
        super().__init__('정수가 아닙니다.: {0}'.format(arg))

# text를 integer로 반환해주는 함수
def convert_to_integer(text):
    f = text[0]
    if f == '-':
        return float(text) 
    elif text.isdigit(): # 부호(+, -)처리 못함
        return float(text)
    else:
        raise InvalidIntException(text)

if __name__ =='__main__':
    try:
        print('숫자를 입력하세요:')
        text = input()
        number = convert_to_integer(text)
        print('3', number)
    except InvalidIntException as err:
        print('예외가 발생했습니다({0})'.format(err))
        
    else:
        print('정수 형식으로 변환되었습니다 : {0}{1}'.format(number, type(number)))