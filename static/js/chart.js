var myChart1 = echarts.init(document.getElementById('chart1'));
                            var myChart2 = echarts.init(document.getElementById('chart2'));
                            var myChart3 = echarts.init(document.getElementById('chart3'));
                            //chart의 설정
                            var option1 = {
                              tooltip: {
                                trigger: 'axis',
                                axisPointer: {
                                  type: 'cross',
                                  label: {
                                    backgroundColor: '#283b56'
                                  }
                                }
                              },
                              dataZoom: {
                                show: false,
                                start: 0,
                                end: 100
                              },
                              xAxis: [
                                {
                                  type: 'category',
                                  boundaryGap: true,
                                  data: (function (){
                                    var now = new Date();
                                    var res = [];
                                    for(let i =0; i<dht_temp.length; i+=2) {
                                      res.unshift(dht_temp[i].replace(/\//g,":"));
                                      now = new Date(dht_temp[i]);
                                    }
                                    return res;
                                  })()
                                },
                              ],
                              yAxis: [
                                {
                                  type: 'value',
                                  scale: true,
                                  name: '온도',
                                  max: 50,
                                  min: 0,
                                  boundaryGap: [0.2, 0.2],
                                },

                              ],
                              series: [
                                {
                                  name: '온도',
                                  type: 'bar',
                                  lineStyle:{
                                    color:'#2A265C' //line차트 색상 변경
                                  },
                                  smooth: true, //부드러운 line 표현
                                  yAxisIndex: 0, //yAxis 0번째 사용
                                  data: (function(){
                                    var res = [];
                                    for(let i=0; i<dht_temp.length; i+=2) {
                                      res.push(dht_temp[i+1]);
                                    }
                                    return res;
                                  })()
                                },
                              ]
                            };

                            var option2 = {
                              tooltip: {
                                trigger: 'axis',
                                axisPointer: {
                                  type: 'cross',
                                  label: {
                                    backgroundColor: '#283b56'
                                  }
                                }
                              },
                              dataZoom: {
                                show: false,
                                start: 0,
                                end: 100
                              },
                              xAxis: [
                                {
                                  type: 'category',
                                  boundaryGap: true,
                                  data: (function (){
                                    var now = new Date();
                                    var res = [];
                                    for (let i=0; i<dht_humid.length; i+=2) {
                                      res.unshift(dht_humid[i].replace(/\//g,":"));
                                      now = new Date(dht_humid[i]);
                                    }
                                    return res;
                                  })()
                                },
                              ],
                              yAxis: [
                                {
                                  type: 'value',
                                  scale: true,
                                  name: '습도',
                                  max: 100,
                                  min: 0,
                                  boundaryGap: [0.2, 0.2],
                                },

                              ],
                              series: [
                                {
                                  name: '습도',
                                  type: 'bar',
                                  lineStyle:{
                                    color:'#2A265C' //line차트 색상 변경
                                  },
                                  smooth: true, //부드러운 line 표현
                                  yAxisIndex: 0, //yAxis 0번째 사용
                                  data: (function(){
                                    var res = [];
                                    for(let i=0; i<dht_humid.length; i+=2) {
                                      res.push(dht_humid[i+1]);
                                    }
                                    return res;
                                  })()
                                },
                              ]
                            };

                            var option3 = {
                              tooltip: {
                                trigger: 'axis',
                                axisPointer: {
                                  type: 'cross',
                                  label: {
                                    backgroundColor: '#283b56'
                                  }
                                }
                              },
                              dataZoom: {
                                show: false,
                                start: 0,
                                end: 100
                              },
                              xAxis: [
                                {
                                  type: 'category',
                                  boundaryGap: true,
                                  data: (function (){
                                    var now = new Date();
                                    var res = [];
                                    for (let i=0; i<dht_dust.length; i+=2) {
                                        res.unshift(dht_dust[i].replace(/\//g,":"));
                                        now = new Date(dht_dust[i])
                                    }
                                    return res;
                                  })()
                                },
                              ],
                              yAxis: [
                                {
                                  type: 'value',
                                  scale: true,
                                  name: '미세먼지',
                                  max: 300,
                                  min: 0,
                                  boundaryGap: [0.2, 0.2],
                                },

                              ],
                              series: [
                                {
                                  name: '미세먼지',
                                  type: 'bar',
                                  lineStyle:{
                                    color:'#2A265C' //line차트 색상 변경
                                  },
                                  smooth: true, //부드러운 line 표현
                                  yAxisIndex: 0, //yAxis 0번째 사용
                                  data: (function (){
                                    var res = [];
                                    for(let i=0; i<dht_dust.length; i+=2) {
                                        res.push(dht_dust[i+1])
                                    }
                                    return res;
                                  })()
                                },
                              ]
                            };

                            // 위에서 설정한 속성을 차트에 반영합니다.
                            myChart1.setOption(option1);
                            myChart2.setOption(option2);
                            myChart3.setOption(option3);

                            //데이터를 생성하고 삭제합니다.
                            setInterval(function setdata(value, time){
                                //x축에 실시간 데이터 생성
                                var axisData = (new Date()).toLocaleTimeString().replace(/^\D*/, '');

                                var data0 = option1.series[0].data; //온도 데이터
                                var data1 = option2.series[0].data; //습도 데이터
                                var data2 = option3.series[0].data; //미세먼지 데이터

                                //데이터의 가장 왼쪽 값을 제거
                                data0.shift();
                                data1.shift();
                                data2.shift();
                                //데이터의 가장 오른쪽 값을 추가
                                data0.push(temp);
                                data1.push(humid);
                                data2.push(dust);


                                //x축에 시간 데이터 추가
                                option1.xAxis[0].data.shift();
                                option1.xAxis[0].data.push(axisData);
                                option2.xAxis[0].data.shift();
                                option2.xAxis[0].data.push(axisData);
                                option3.xAxis[0].data.shift();
                                option3.xAxis[0].data.push(axisData);

                                //차트에 반영
                                myChart1.setOption(option1);
                                myChart2.setOption(option2);
                                myChart3.setOption(option3);
                            }, 5000);