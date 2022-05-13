// 세그먼트 핀 번호
// 2   6  11 3   4   7
// D1  A  F  D2  D3  B


// E   D  dp  C  G  D4
// 10  9  13  8  12  5
// -----------------------

//a,b,c,d,e,f,g 상태값 (캐소드형 회로이기 때문에 1 : 끄기, 0 : 켜기)
const byte segValue[10][7] = {
   {1,1,1,1,1,1,0}, //0
   {0,1,1,0,0,0,0}, //1
   {1,1,0,1,1,0,1}, //2
   {1,1,1,1,0,0,1}, //3
   {0,1,1,0,0,1,1}, //4
   {1,0,1,1,0,1,1}, //5
   {1,0,1,1,1,1,1}, //6
   {1,1,1,0,0,0,0}, //7
   {1,1,1,1,1,1,1}, //8
   {1,1,1,1,0,1,1}  //9  
};

// 우선 dig들에게 신호를 주고 다음에 a~g까지 신호를 줘서 숫자 모양을 만듦
// const : 변경이 불가능한 상수
const byte segPin[8]={6,7,8,9,10,11,12,13}; //{a,b,c,d,e,f,g,dp} 순서대로
const byte digitPin[4] = {2,3,4,5}; //{d1,d2,d3,d4} 순서대로

boolean state = false;  // 시간 출력형식 지정
extern volatile unsigned long timer0_millis; // 타이머 변수
unsigned long readTime; // 현재타이머시간 변수 설정
int hour, min, sec;

void setup() {
  Serial.begin(9600);  

  for(int i=0;i<10;i++){
    pinMode(segPin[i], OUTPUT);
  }
  for(int j=0;j<4;j++){
    pinMode(digitPin[j], OUTPUT);    
    digitalWrite(digitPin[j], HIGH); 
  }  
}

void loop() {   
  if(Serial.available()){ // 사용자가 입력하는 시/분/초 읽기
    String inString = Serial.readStringUntil('\n'); // 입력한 모든 문자열을 반환해 inString에 저장   
    int index1 = inString.indexOf(':'); // indexOf는 split같은 기능 => indexOf(찾을 문자, 검색 시작 위치)
    int index2 = inString.indexOf(':',index1+1);  // 두 번째 세미콜론 위치
    int index3 = inString.length();  // 문자열 길이
    // 입력한 값을 각각 hour, min, sec 변수에 저장
    // substring(추출 시작 위치, 추출 끝 위치) <= 추출 끝 위치는 인덱스 번호가 아닌 실제 문자열의 자리수를 의미
    //  => ex) "222"를 추출하려면, substring(0,2)가 아니라 substring(0,3)이 되어야 한다.
    // "23:12:34"이면
    hour = inString.substring(0, index1).toInt(); // (0,2) => 23만 추출해서 hour에 저장
    min = inString.substring(index1+1,index2).toInt();  // (3,5) => 12만 추출해서 min에 저장
    sec = inString.substring(index2+1,index3).toInt();  // (6,8) => 34만 추출해서 sec에 저장

    // hour,min,sec 값을 초로 변환하여 timer0_millis 변수에 저장 => 입력된 시간을 기준으로 돌아가게 된다.
    timer0_millis = ((long)hour*3600+min*60+sec)*1000;   
    
  } 
  // 타이머 리셋
  // millis():아두이노의 동작이 시작된 후로부터 경과된 시간을 millisecond(1/1000)단위로 나타냄
  if(millis()>=86400000){  // 24시(24시간을 초로 바꾸면 86400000초)가 되면
     timer0_millis=0;      // 00:00:00으로 리셋되어 타이머는 24시간 단위로 처음부터 다시 돌게 된다.
  }
  readTime = millis()/1000; // millis()함수에서 읽은 타이머 시간값을 1000으로 나눈 몫 값을 readTime에 저장
  // 입력 시간을 기준으로 흐르는 시간 값을 hour, min, sec값으로 다시 바꾸면, 현재 시간을 구할 수 있다.
  sec = readTime%60;
  min = (readTime/60)%60;
  hour = (readTime/(60*60))%24;

  // segoutput()
  segOutput(3,min%10,0); //min 1의 자리
  segOutput(2,min/10,0); //min 10의 자리
  segOutput(1,hour%10,1); //hour 1의 자리
  segOutput(0,hour/10,0); //hour 10의 자리    
}

//LED 초기화
void segClear(){ 
  for(int i=0;i<8;i++){
    digitalWrite(segPin[i], LOW);        
  }
}
//LED 출력
void segOutput(int d, int Number, int dp){ 
  segClear();
  digitalWrite(digitPin[d], LOW);
  for(int i=0;i<7;i++){  // 0~6인 이유 => dp를 제외한 a,b,c,d,e,f,g까지만 이기 때문 
     digitalWrite(segPin[i], segValue[Number][i]); // b에 1에 들어옴      
  }
  digitalWrite(segPin[7], dp); 
  delayMicroseconds(1000);
  digitalWrite(digitPin[d], HIGH); 
}
