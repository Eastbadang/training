# error, 2022/01/23 ; after python 3.9.7/anaconda upgrade
# http://blog.naver.com/PostView.nhn?blogId=chandong83&logNo=221886840586&categoryNo=81&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView

# pip install pycryptodome

#from Crypto.Cipher import AES
from Crypto.Cipher import AES

# 바이트 어레이 표시함수
def print_hex_bytes(name, byte_array):
    print('{} len[{}]: '.format(name, len(byte_array)), end='')
    for idx, c in enumerate(byte_array):
        print("{:02x}".format(int(c)), end='')
    print("")

# 암호화 함수
def enc(key, aad, nonce, plain_data):
    print('\nenter enc function ---------------------------------')
    # AES GCM으로 암호화 라이브러리 생성
    cipher = AES.new(key, AES.MODE_GCM, nonce)

    # aad(Associated Data) 추가
    cipher.update(aad)

    # 암호!!!
    cipher_data = cipher.encrypt(plain_data)
    mac = cipher.digest()

    # 암호화된 데이터 와 MAC Tag(Message Authentication Codes tag) 출력
    print_hex_bytes('cipher_data', cipher_data)
    print_hex_bytes('mac', mac)
    print('exit enc function ---------------------------------')
    # 암호 데이터와 mac 리턴
    return cipher_data, mac

# 복호화 함수
def dec(key, aad, nonce, cipher_data, mac):
    print('\nenter dec function ---------------------------------')
    # 암호화 라이브러리 생성
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    # aad(Associated Data) 추가
    cipher.update(aad)

    try:
        # 복호화!!!
        plain_data = cipher.decrypt_and_verify(cipher_data, mac)
        # 암호화된 데이터 출력
        print_hex_bytes('plain_data', plain_data)
        print('exit dec function ---------------------------------')
        # 복호화 된 값 리턴
        return plain_data

    except ValueError:
        # MAC Tag가 틀리다면, 즉, 훼손된 데이터
        print ("Key incorrect")
        print('exit dec function ---------------------------------')
        # 복호화 실패
        return None

if __name__ == "__main__":
    # 각종 키 정보
    key   = bytes([0x00,0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99,0xAA,0xBB,0xCC,0xDD,0xEE,0xFF])
    aad   = bytes([0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E]) #
    nonce = bytes([0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99,0xAA,0xBB,0xCC]) # 기본 12(96bit)byte이며 길이 변경 가능.
    # 원본 데이터
    plain_data  = bytes([0x42, 0x43 ,0x45 ,0x47 ,0x48 ,0x49 ,0x4A,0x4B,0x4C,0x4D,0x4E])


    # 각각의 키 정보 출력
    print_hex_bytes('key', key)
    print_hex_bytes('aad', aad)
    print_hex_bytes('nonce', nonce)
    print_hex_bytes('plain_data', plain_data)

    # 암호화 시작
    cipher_data, mac = enc(key, aad, nonce, plain_data)

    print('\nEncrypted value:')
    # 암호 데이터와 MAC 데이터 출력
    print_hex_bytes('\tcipher_data', cipher_data)
    print_hex_bytes('\tmac', mac)

    # 복호화
    result = dec(key, aad, nonce, cipher_data, mac)
    if result is not None:
        print('\nDecrypted value:')
        print_hex_bytes('\tresult(plain data)', result)