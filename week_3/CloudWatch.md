# CloudWatch 사용법

`CloudWatch`는 AWS의 모든 서비스를 모니터링 할 수 있는 기본 서비스입니다.

우리는 AWS의 서비스 중 RDS 모니터링 대시보드를 만들어 보겠습니다.

## CloudWatch 모니터링

> <h3>로그 파일 설정</h3>

CloudWatch로 모니터링 하기 위해선 RDS의 로그들을 CloudWatch로 보내지도록 설정해주어야 합니다.

![image](https://user-images.githubusercontent.com/43658658/134881863-4ddba81b-ab29-4316-829a-30b51c51b1c8.png)

[RDS] > [데이터베이스] > [수정] 버튼을 눌러줍니다.

![image](https://user-images.githubusercontent.com/43658658/134881999-4588e02d-9ccc-4d62-a948-12016b25dce1.png)

`로그 내보내기` 항목에 `에러 로그`와 `느린 쿼리 로그`를 체크해줍니다.   
`일반 로그`는 DB의 모든 로그를 남기는 옵션으로 DB에 부하를 주기 때문에 체크해 주지 않습니다.    
`에러 로그`는 에러가 발생했을 때 로그를 남기는 옵션이고,   
`느린 쿼리 로그`는 쿼리가 느릴 때 로그를 남기는 옵션입니다.

> <h3>모니터링 하는 간단한 방법</h3>

모니터링을 하는 방법은 2가지가 있습니다.   
그 중 첫 번째는 간편한 방법으로 RDS의 데이터베이스의 모니터링 정보를 통해 확인하는 방법입니다.

![image](https://user-images.githubusercontent.com/43658658/134882545-9a76b16c-c167-4473-bb7b-320d6e1bfa10.png)

해당 DB를 클릭해서 [모니터링] 탭으로 들어가서 확인하는 방법입니다.   
이 방법은 간편하고 빠르게 확인이 가능하지만 자세한 지표를 보기에는 한계가 있습니다.

> <h3>모니터링 대시보드</h3>

두 번째 방법은 CloudWatch 서비스로 들어가 모니터링 대시보드를 만드는 방법입니다.   
상단의 검색창에 `Cloudwatch`를 입력해서 접속합니다.

![image](https://user-images.githubusercontent.com/43658658/134883101-f04ee928-2340-41d8-a61a-765459902f77.png)

[대시보드] > [대시보드 생성] 버튼을 누릅니다.

![image](https://user-images.githubusercontent.com/43658658/134883234-51b07b03-09c3-4fe6-8428-e0c7fa2b5eed.png)

적절한 대시보드 이름을 작성합니다.

![image](https://user-images.githubusercontent.com/43658658/134883397-6a31a8ff-0f09-49c9-8497-7a7acc51cb17.png)

[행] > [지표]로 위젯을 하나 생성해보겠습니다.

![image](https://user-images.githubusercontent.com/43658658/134883645-14ea3f9f-b027-47c4-95ff-283624efc57f.png)

검색 창에 `RDS`, `DB이름`의 키워드를 각각 적고 엔터를 누릅니다.   
그럼 해당 키워드에 맞는 지표들이 필터링됩니다.

![image](https://user-images.githubusercontent.com/43658658/134884198-f1c64f54-c24f-4eff-94c0-ac5b3837e962.png)

RDS에서 클라우드로 보내주는 로그지표와 RDS를 만들면 자동으로 구성되는 데이터베이스 지표가 있습니다.   
`RDS에서 클라우드로 보내는 로그지표`가 바로 우리가 앞서 `에러 로그`와 `느린 쿼리 로그`를 체크해주었던 것이 반영된 것입니다.   
이곳을 클릭해서 `에러 로그`를 선택해 위젯을 생성해봅시다.

![image](https://user-images.githubusercontent.com/43658658/134884707-0482e6ec-786c-4d62-9f31-b3aeccce44c9.png)

[위젯 생성] 버튼을 눌러 위젯을 하나 생성합니다.

![image](https://user-images.githubusercontent.com/43658658/134884952-36d590ab-8640-4b8e-8b50-fee64aca919b.png)

위젯이 하나 생성되었습니다.   
다시 [위젯 추가] 버튼을 누르고 이번에는 CPU 사용량에 대한 위젯을 만들어보겠습니다.

![image](https://user-images.githubusercontent.com/43658658/134885353-3cd5c813-3ffb-4a3a-8d3d-847921e6e269.png)

마찬가지로 [행] > [지표]를 선택하고 검색 창에 `CPUUtilization`을 추가합니다.

![image](https://user-images.githubusercontent.com/43658658/134885825-ae1ad13a-ed2b-4389-b4da-d96212a0e242.png)

이렇게 원하는 지표들을 위젯을 만들어 대시보드에 추가할 수 있습니다.   
- freeablememory : 사용 가능한 메모리를 나타내는 지표입니다.
- Read IOPS : 초당 읽고 있는 숫자를 나타냅니다.
- Write IOPS : 초당 쓰고 있는 숫자를 나타냅니다.
- Latency : 지연시간을 표기합니다.

![image](https://user-images.githubusercontent.com/43658658/134886381-0a1537f1-1712-4033-815f-ce7359018818.png)

[위젯 추가] > [로그 테이블]를 누르면 `클라우드 인사이트`를 활용할 수 있습니다.   
로그를 쿼리해서 해당 로그를 볼 수 있습니다. `error로그`를 살펴보기에 좋습니다.

![image](https://user-images.githubusercontent.com/43658658/134886862-c98cbd11-25d3-4e5f-898d-12ff7c7f2dd9.png)

[로그 그룹 선택]에서 에러 로그와 관련된 항목을 체크합니다.   
날짜 범위를 설정합니다.

![image](https://user-images.githubusercontent.com/43658658/134887354-1498610c-03c5-4cf4-b87a-84a12d35fa67.png)

위와 같이 입력해서 [쿼리 실행] 버튼을 누르면 [로그] 탭에서 에러 로그가 나타납니다.   
(에러 로그가 없다면 아무것도 표시되지 않습니다)

상단의 [위젯 생성] 버트을 눌러 로그 데이터 위젯을 생성합니다.

![image](https://user-images.githubusercontent.com/43658658/134887613-02aaf6fb-d5da-4bf9-b6be-e463d0bce8bd.png)

로그 지표 위젯이 생성된 것을 확인할 수 있습니다.   
모니터링 대시보드는 반드시 상단의 [대시보드 저장] 버튼을 눌러줘야 저장이 됩니다.

---
