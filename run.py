import os
from datetime import datetime
from spleeter.separator import Separator

def separate_audio():
    # 최상위 결과 디렉토리 경로 설정
    result_directory = 'result'
    
    # 현재 날짜와 시간을 기반으로 디렉토리 이름 생성
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_directory = os.path.join(result_directory, f'output_directory_{timestamp}')

    # 최상위 결과 디렉토리가 존재하지 않으면 생성
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)
        print(f"{result_directory} 디렉토리가 생성되었습니다.")

    # 출력 디렉토리가 존재하지 않으면 생성
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"{output_directory} 디렉토리가 생성되었습니다.")

    # Spleeter 초기화 (4스템 미세 조정 모델: 보컬, 드럼, 베이스, 기타)
    separator = Separator('spleeter:4stems')
    # 로컬 모델을 사용하려면 주석 해제: separator = Separator('pretrained_models/4stems_finetune/configuration.json')

    # 오디오 파일 분리
    separator.separate_to_file('day6.mp3', output_directory)

    print("오디오 파일이 성공적으로 분리되었습니다.")

if __name__ == '__main__':
    separate_audio()
