# 프로젝트명
> 스마트홈

# IoT 프로젝트
> Arduino, Raspberry Pi 각종 센서를 이용해 Web/App로 집 내부의 상황을 확인하고 관리/제어가 가능한 스마트홈 시스템 구축  
<img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white"/> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/> <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=white"/> <img src="https://img.shields.io/badge/Arduino-00979D?style=flat-square&logo=Arduino&logoColor=white"/> <img src="https://img.shields.io/badge/Raspberry Pi-A22846?style=flat-square&logo=Raspberry Pi&logoColor=white"/> <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=Android&logoColor=white"/> <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=Kotlin&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/>

# App
<img width="593" src="https://user-images.githubusercontent.com/12439450/188380806-e4459c10-4073-44ad-a7ce-997b14558962.png">

# Web
<img width="901" src="https://user-images.githubusercontent.com/12439450/188381166-68636102-19e4-4f04-93c7-f64705131c31.png">

# 아키텍처
### MQTT 통신을 사용해 Web/App/Raspberry Pi 통신을 하였음.

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

> 집에 사람이 아무도 없을때 보안 기능
집에 사람이 아무도 없을 때 PIR센서에 움직임이 감지되면 부저로 소리가 울리고 LED가 깜빡깜빡 거린다.  
그리고 Web/App에 알림이 울리게 된다.
<img width="602" src="https://user-images.githubusercontent.com/12439450/188373005-c51f0aee-64fe-4608-836b-d99c378914d9.png">

- 온도, 습도, 미세먼지
> 라즈베리파이에서 온습도, 미세먼지를 체크 후 Web/App에 출력
<img width="995" src="https://user-images.githubusercontent.com/12439450/188373185-da8569ad-fc4c-4cc0-8f0f-623730ca5ebc.png">

- 파이카메라  
> 라즈베리파이에 파이 카메라를 연결 후 MQTT를 통하여 Web/App 모두 CCTV 제어 가능  

- 커튼 올리기/내리기, 전등 On/Off  
>  서보모터로 커튼 구현  
>  MQTT 통신으로 전등 On/Off 구현  

- 전자 시계  
> 4x세그먼트 캐소드 사용  
> 현재 시간을 출력  

- App 알람  
> Date/Time PickerDialog를 활용하여 알람 기능 구현  

- 반려동물 사료주기  
> 사료통에 서보모터를 달아서 사료 공급  
> Web/App에 사료시간을 설정해서 자동으로 사료 공급  
<img width="316" src="https://user-images.githubusercontent.com/12439450/188378326-cfeadc37-c295-4361-94fa-96963c37b1d5.png">

- 반려동물 물 주기  
> Raspberry Pi와 Arduino 연동  
> 물높이 센서(B75) 센서 사용  
> 물 높이를 실시간으로 측정해 자동으로 물 공급 가능  
> Web/App에 물 버튼 클릭 시 물 공급 가능  

- 큰 소리 감지  
> 사운드 소리 감지 센서 (LM393) 센서 사용  
> Raspberry Pi와 Arduino 연동  
> 실시간으로 큰 소리를 감지해 수준 이상이 되면 Web/App 알람 기능  

# 시행 영상 및 PPT  
시행 영상 : 
PPT : 
