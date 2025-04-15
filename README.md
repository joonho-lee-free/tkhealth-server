# TKHealth Upload Server (Python + Flask + Firebase)

## 구성 파일
- app.py: Flask 서버 본체
- requirements.txt: 필요한 파이썬 패키지 목록
- firebase-key.json: Firebase 서비스 계정 키 (직접 추가 필요)

## 실행 방법
1. 가상환경 생성 (선택):
   python3 -m venv venv && source venv/bin/activate

2. 패키지 설치:
   pip install -r requirements.txt

3. Firebase 키 파일 넣기:
   프로젝트 루트에 firebase-key.json 추가

4. 서버 실행:
   python app.py

## 사용 예시 (React Native 등에서 요청)
POST /upload
{
  "filename": "tk_cough_0415.m4a",
  "filetype": "audio/m4a",
  "base64": "(base64 문자열)"
}