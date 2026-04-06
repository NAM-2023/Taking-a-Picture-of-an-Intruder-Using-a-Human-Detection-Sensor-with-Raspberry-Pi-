from gpiozero import MotionSensor                           # gpiozero 라이브러리에서 MotionSensor 클래스 가져오기 (PIR 센서 제어)
import time                                                 # 시간 지연을 위한 time 라이브러리
from picamera2 import Picamera2                             # picamera2 라이브러리에서 카메라 제어 클래스 가져오기
import datetime                                             # 날짜 및 시간 처리를 위한 datetime 라이브러리
 
pirPin = MotionSensor(16)                                   # GPIO 16번 핀을 PIR 인체 감지 센서 입력으로 설정

picam2 = Picamera2()                                        # Picamera2 객체 생성 (카메라 사용 준비)
camera_config = picam2.create_preview_configuration()       # 카메라 미리보기 설정 생성
picam2.configure(camera_config)                             # 생성한 설정을 카메라에 적용
picam2.start()                                              # 카메라 동작 시작

try:
    
    while True:                                              # 무한 반복문 시작 (계속 감지 수행)
        try:    
            sensorValue = pirPin.value                       # PIR 센서의 현재 값 읽기 (0 또는 1)

            if sensorValue ==1:                              # 센서 값이 1이면 움직임이 감지된 상태
                now = datetime.datetime.now()                # 현재 날짜 및 시간 가져오기
                print(now)                                   # 감지된 시간 출력

                fileName = now.strftime('%y-%m-%d %H:%M:%S') #현재 시간을 문자열로 변환하여 파일 이름으로 사용 
                                                                

                picam2.capture_file(fileName + '.jpg')       # 해당 파일 이름으로 사진 촬영 후 저장
                                                           

                time.sleep(0.5)                              # 0.5초 대기 (연속 촬영 방지)

        except:                                              # 내부 try문에서 오류 발생 시 무시하고 계속 실행
            pass

except KeyboardInterrupt:                                    # 키보드 인터럽트(Ctrl+C) 발생 시 루프 종료
    pass