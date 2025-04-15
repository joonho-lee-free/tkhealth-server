# TKHealth Render 배포용 서버

## 구성 파일
- app.py: Flask 서버
- requirements.txt: 필요한 라이브러리
- .env 예시 (Render에서 환경변수로 등록)

## Render 배포 방법
1. Render 가입 및 GitHub 연동
2. 해당 ZIP을 GitHub 리포지토리로 업로드
3. Render에서 새 Web Service 생성
   - Build Command: pip install -r requirements.txt
   - Start Command: python app.py
   - Environment Variables:
     - KEY: FIREBASE_KEY_JSON
     - VALUE: firebase-key.json 파일 내용 전체를 복사하여 JSON 문자열로 입력
4. URL로 배포된 서버 접근 가능 (/upload)

## 테스트 예시
POST https://yourapp.onrender.com/upload
{
  "filename": "tk_cough_0415.m4a",
  "filetype": "audio/m4a",
  "base64": "(base64 encoded audio)"
}