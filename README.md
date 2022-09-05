# 프로젝트명
> 스마트홈

# IoT 프로젝트
> Arduino, Raspberry Pi 각종 센서를 이용해 Web/App로 집 내부의 상황을 확인하고 관리/제어가 가능한 스마트홈 시스템 구축  
<img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white"/> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/> <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=white"/> <img src="https://img.shields.io/badge/Arduino-00979D?style=flat-square&logo=Arduino&logoColor=white"/> <img src="https://img.shields.io/badge/Raspberry Pi-A22846?style=flat-square&logo=Raspberry Pi&logoColor=white"/> <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=Android&logoColor=white"/> <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=Kotlin&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/>
# 아키텍처
- 온도 습도(DHT11), 미세먼지(PM2008)
> 5분마다 체크를 해 수치가 높으면 자동 환기  
> 웹(차트로 표시), 안드로이드앱(숫자 표시)  
- 파이카메라
> 집 내부 CCTV 촬영  
> 웹, 안드로이드 앱 표시  
- 조명(LED), 커튼(서보모터), 푸쉬버튼
> 서보모터로 전등 스위치 작동  
> 기상시간이 되면 전등 On/Off, 커튼 올리기/내리기(DC모터)
