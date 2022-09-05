# 프로젝트명
> 스마트홈

# IoT 프로젝트
> Arduino, Raspberry Pi 각종 센서를 이용해 Web/App로 집 내부의 상황을 확인하고 관리/제어가 가능한 스마트홈 시스템 구축  
<img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white"/> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/> <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=white"/> <img src="https://img.shields.io/badge/Arduino-00979D?style=flat-square&logo=Arduino&logoColor=white"/> <img src="https://img.shields.io/badge/Raspberry Pi-A22846?style=flat-square&logo=Raspberry Pi&logoColor=white"/> <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=Android&logoColor=white"/> <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=Kotlin&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/>

# 아키텍처
- RFID 카드 추가/삭제
> RFID (RC522) 사용  
> RFID 등록 버튼을 누르면 JSON 파일로 카드가 등록 됨.  
> 이미 등록되어 있다면 등록되어 있다고 뜬다.  
> RFID 삭제 버튼을 누르면 JSON 파일에 조회 후 삭제 됨.  
> 없는 카드면 없는 카드라고 뜬다.
- RFID 외출/보안
> RFID 등록하면 JSON 파일에 0 : 외출, 1 : 집에 있는 상태 등록
<img width="60%" src="https://user-images.githubusercontent.com/12439450/188371995-9742adfd-2f4f-401e-9c27-ebc32a253a44.png">
> 외출/복귀시 JSON 파일에 집에 있는 사람 수를 저장 후 Web과 App에 알림이 뜬다.
<img width="591" src="https://user-images.githubusercontent.com/12439450/188372487-ee3cdd57-9c1b-42a6-bfc5-ce1f5df5e0b9.png">
