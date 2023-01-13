"""
날짜 : 2023-01-13
이름 : 박진휘
내용 : 파이썬 사용자관리 프로그램 실습
"""
import pymysql

#데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                user='root', 
                password='1234', 
                db='java1db', 
                charset='UTF8')

#관리 프로그램
while True:
    print('***************************************')
    print('0: 종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    
    try:
        answer = int(input('선택 : '))
    except Exception as e:
        print("숫자 0~4를 입력해주세요.", e)
        continue

    if answer == 0:
        break
    elif answer == 1:
        #등록
        print('등록할 정보를 입력하세요.')
        val = []
        val.append(input("아이디 : "))
        val.append(input("비밀번호 : "))
        val.append(input("이름 : "))
        val.append(input("전화번호 : "))
        val.append(input("나이 : "))
        cur = conn.cursor()
        sql = "insert into `user1` values (%s,%s,%s,%s,%s);"
        cur.execute(sql, val)
        conn.commit()
        print('등록 완료')
        continue 
    elif answer == 2:
        #조회
        cur = conn.cursor()
        sql = "select * from `user1`;"
        cur.execute(sql)
        conn.commit()
        for row in cur.fetchall():
            print('아이디 : ', row[0])
        print('조회 완료')
        continue 
    elif answer == 3:
        #검색
        print('검색할 아이디를 입력하세요.')
        uid = input()
        cur = conn.cursor()
        sql = "select * from `user1` where `uid`=(%s);"
        cur.execute(sql, uid)
        conn.commit()
        for i in cur.fetchall():
            print(i[0], i[1], i[2], i[3], i[4])
        print('검색 완료')
        continue 
    elif answer == 4:
        #삭제
        print('삭제할 아이디를 입력하세요.')
        uid = input()
        cur = conn.cursor()
        sql = "delete from `user1` where `uid`=(%s);"
        cur.execute(sql, uid)
        conn.commit()
        print('삭제 완료')
        continue 
    else:
        print("숫자 0~4를 입력해주세요.", e)
        continue 

#종료
conn.close()

#프로그램 종료
print("프로그램 종료")