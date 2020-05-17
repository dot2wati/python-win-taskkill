import os, time

def check_process():
   
    # 
    result = os.popen('tasklist /V /fi "IMAGENAME eq iexplore.exe" /fi "STATUS eq Not Responding"')

    # strip 함수는 문자열의 맨앞과 맨뒤의 whitespace 제거 (중간문자는 제거 안됨)
    # split("\n")으로 결과 row 수 확인
    result_text = result.read().strip()
    resRows = result_text.split("\n")
    kill_len = (len(resRows))

    for resRow in resRows:
        print("*" * 50)
        print(resRow)

    if kill_len >= 3:
        print("kill")
        os.popen('taskKILL /f /im iexplore.exe')
        
while True:
    check_process()
    time.sleep(10)

    
 