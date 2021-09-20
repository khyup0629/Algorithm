# AWS lambda

`AWS 람다(lambda)`는 서버리스 배치프로그램을 수행할 수 있게 해주는 서비스입니다.   

`람다`는 함수(Function)서비스의 일종입니다. 코드를 작성하고 백엔드에서 주로 사용합니다.   
람다를 사용하면 AWS내 다양한 서비스에 다양한 처리를 코드로 할 수 있습니다.

![image](https://user-images.githubusercontent.com/43658658/133957745-120ae481-c47b-433f-9999-0b2564128725.png)

람다의 비용 청구는 위와 같습니다.

이번에는 `API Gateway`도 함께 사용합니다.   
API 게이트웨이는 1년동안 100만건을 초과할 때에만 유료입니다.

## 람다 함수 만들기

> <h3>함수 생성</h3>

AWS 콘솔에서 `lambda`를 검색하여 서비스로 이동합니다.   
[함수 생성] 버튼을 누릅니다.   

![image](https://user-images.githubusercontent.com/43658658/133961112-d62a527b-7727-4e40-a967-e983c871edf4.png)

`새로 작성` 옵션을 선택합니다.   
적절한 이름을 지어주고, 런타임의 언어는 `Node.JS`로 선택하겠습니다.

![image](https://user-images.githubusercontent.com/43658658/133961226-b72384d0-4a7d-45a4-b457-3fb3bc094b7e.png)

기존에 만든 롤이 없으므로 새로 생성해줍니다.

[함수 생성] 버튼을 눌러 다음 단계로 갑니다.

![image](https://user-images.githubusercontent.com/43658658/133961305-24164694-5df4-4cce-89e9-52cee1050e78.png)

위 화면의 왼쪽 파트는 `디자이너`입니다.   
람다는 호출할 대상과 특정 조건에 맞춰 다른 서비스를 불러올 수 있도록 `트리거`와 `대상`이라는 추가객체가 주어집니다.   
람다가 단독으로 실행되게 하고 싶으면 그대로 두면 됩니다.   

우측 파트에는 람다의 고유 번호인 `ARN 주소`가 있습니다.   
이 람다에 권한을 주고 싶거나, 특정 객체만 연결되게 제어하고 싶을 때 `ARN`을 사용합니다.

> <h3>람다 테스트 설정</h3>

![image](https://user-images.githubusercontent.com/43658658/133961567-087bd437-3f51-4893-9be0-cea8e02ebb5c.png)

하단의 `테스트` 항목을 클릭합니다.   
`테스트`에서 코드를 짜고 중간에 코드가 잘 작동하는지 볼 수 있습니다.   
이름에 적절한 이름을 작성한 뒤 [변경 사항 저장] 버튼을 눌러 테스트 셋팅을 합니다.   

![image](https://user-images.githubusercontent.com/43658658/133961964-41dc8e25-4ede-4049-b591-3fce0b1101c5.png)

이어서 오른쪽에 [테스트] 버튼을 누르면 위의 화면과 같이 테스트 성공 여부와 함께 로그를 볼 수 있습니다.

`"statusCode": 200`은 정상적으로 실행되었다는 의미의 코드입니다.

로그 출력 부분은 람다가 `실제로 사용한 메모리`와 `수행시간`이 출력됩니다.   
서버가 없이 돌아가는 `서버리스 함수`이기 때문에 서버에서 관리해주지 않습니다.   
따라서, 각 람다마다 리소스 사용량이 어떤지 알아둘 필요가 있습니다.

> <h3>람다 코드 수정 후 테스트</h3>

``` node.js
exports.handler = (event, context, callback) => {
  const output = "success lambda api test: "+event.val01;
  callback(null, output);
};
```

`exports.handler`는 node.js가 실행될 때 가장 먼저 참조하는 부분입니다.
`(event, context, callback)`에서 
  - `event`는 사용자가 입력한 값입니다. 테스트 이벤트에서 입력값이 들어올 곳입니다.
  - `context`는 exports.handler의 시스템 상태값입니다.
  - `callback`은 콜백 함수를 의미합니다. 콜백 함수에서 처리된 값이 반환됩니다.
`output`에는 event.val01에 들어오는 입력값이 앞의 문자열인 "success lambda api test: "과 더해져 저장됩니다.
`callback(null, output)`은 오류가 없다면 output을 반환하는 콜백 함수입니다.
  
 node.js와 관련된 라이브러리 및 기본 속성과 관련된 설명은 아래 링크를 참조바랍니다.   
 => https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/nodejs-context.html
 
 ![image](https://user-images.githubusercontent.com/43658658/133962739-1db7ae47-0de0-4904-bf62-6a0a56c8eaa6.png)

람다의 `코드` 항목으로 가서 `index.js`의 코드를 위의 코드로 수정합니다.   
수정 후 우측의 [Deploy] 버튼을 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/133963058-a052900f-378d-40ad-8e03-cb3d26538878.png)

람다의 `테스트` 항목으로 가서 테스트 이벤트를 변경합니다.   
index.js에서 `event.val01`에 입력값으로 들어갈 값을 작성해줍니다.

[변경 사항 저장] 버튼을 눌러 저장하고 [테스트] 버튼을 눌러봅니다.

![image](https://user-images.githubusercontent.com/43658658/133963576-94ad7f21-eb9f-44f2-8f0c-94eaba7d64c7.png)

코드의 `output` 값이 정상적으로 출력되는 것을 확인할 수 있습니다.

실제로 `API에서 호출`되는 `람다`는 이러한 가벼운 코드를 가진 것이 많기 때문에   
간단하게 데이터를 반환해주는 경우도 많습니다.   

반면 람다의 로직이 무거워지는 경우도 있습니다.   
이 경우에는 API로 호출되지 않고, `특정 시간에 맞춰서 실행`되도록 하는 경우도 있습니다.   
AWS에서는 프로그램 라이브러리 `SDK`나, 커맨드 명령어 `CLI`를 통해 함수를 실행할 수 있습니다.   
이렇게 구성해서 `주기적으로 람다를 실행`시키도록 설정하는 것을 `서버배치`라고 부릅니다.

## API Gateway

이번에는 함수를 호출할 API 세팅을 해보겠습니다.   
람다는 혼자서만 존재한다면 테스트 버튼을 누르기 전까지 동작하지 않습니다.   
따라서 API를 통해 람다를 호출하여 함수를 실행시켜야 합니다.
(CloudWatch의 규칙 기능을 사용할 수도 있습니다)

백엔드 개발에서는 `API Gateway`를 이용하므로 API Gateway를 통해 방금 만든 람다를 호출해보겠습니다.

> <h3>API 구축</h3>

AWS 콘솔에서 `API Gateway`를 검색해 접속합니다.

![image](https://user-images.githubusercontent.com/43658658/133964488-928c6742-941c-4acd-a01f-81cf7f8e5047.png)

람다와 HTTP(프론트)를 쓸 수 있는 `REST API`를 구축합니다.

![image](https://user-images.githubusercontent.com/43658658/133964589-4fcd1677-87d9-40fc-90f5-370a1c4769ec.png)

엔드포인트는 `지역`으로 설정해야 인터넷망에서 자유롭게 쓸 수 있습니다.

[API 생성] 버튼을 눌러줍니다.
 
![image](https://user-images.githubusercontent.com/43658658/133964742-4c407f46-41f7-4edb-b93d-61b9d9629898.png)

가장 먼저 리소스를 생성해주어야 합니다.   
현재 기본 설정은 '/'로 되어 있습니다.    
이는 `홈`과 같은 의미인데, 리소스가 없어도 API에 접속만 하면 람다가 바로 실행이 되는 설정입니다.   
HTTP통신에서는 이러한 설정이 매우 위험하기 때문에 리소스가 없으면 람다가 실행이 되지 않도록 해야합니다.

![image](https://user-images.githubusercontent.com/43658658/133965074-48ad75d3-2026-40ba-813d-4c3197f9c2a6.png)

[작업] > [리소스 생성]을 누릅니다.

![image](https://user-images.githubusercontent.com/43658658/133965144-104c1195-128a-4789-b423-8567d4fffa39.png)

리소스의 이름을 작성해주면 '/' 뒤에 리소스 이름이 붙게 됩니다.   
[리소스 생성] 버튼을 클릭하여 리소스를 생성합니다.

![image](https://user-images.githubusercontent.com/43658658/133965254-901e79fc-85c1-41bf-be75-c68579cc47eb.png)

다음으로 API를 어떤 방식으로 호출할 지 정의하기 위해 메서드를 생성해야합니다.
생성한 리소스가 클릭된 채로 [작업] > [메서드 생성]을 누릅니다.

![image](https://user-images.githubusercontent.com/43658658/133965971-e6c2c8f8-bcd4-45f1-9ee6-4d2554f148b5.png)

메서드는 `POST`로 선택하고 체크버튼을 누릅니다.   
HTTP의 대표적인 통신 방법에는 `GET`과 `POST` 방식이 있습니다.
`GET`은 요청할 내용을 URL에 실어서 전달하는 방식이고, `POST`는 내부에 숨겨서 전달하는 방식입니다.

![image](https://user-images.githubusercontent.com/43658658/133966171-726d7b4b-e04c-44f9-810c-1dc7200e72a1.png)

통합 유형은 `Lambda 함수`를 선택하고 Lambda 함수에는 람다의 이름을 작성합니다.

![image](https://user-images.githubusercontent.com/43658658/133966282-cc5d2b5c-b5b8-4616-a476-2eb4b53d4546.png)

[저장] 버튼을 누르면 API Gateway에 권한을 줄 것인지 물어봅니다.   
[확인]을 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/133966378-a64fe5ee-783a-40c6-8058-8da75c43c623.png)

테스트 버튼을 눌러서 람다를 테스트 해 볼 수 있습니다.

![image](https://user-images.githubusercontent.com/43658658/133966635-974dd3e3-9f9b-4af1-b5d5-d99e142b6fa0.png)

요청 본문에 테스트 이벤트에서 작성했던 것과 똑같이 작성을 하고 [테스트]버튼을 누르면   

![image](https://user-images.githubusercontent.com/43658658/133966692-ffb4af29-c4fa-4f56-96a7-b8b1773aaa0b.png)

오른쪽에 이와 같이 출력 결과와 로그가 나타납니다.

> <h3>API 배포</h3>

API 구성을 마치기 위해서는 API를 저장해야 합니다.   
API를 저장하는 행위를 `배포`라고 부릅니다.

![image](https://user-images.githubusercontent.com/43658658/133966904-f8ede6c3-b04f-42ef-b80e-934afc8f5718.png)

`POST`를 클릭한 상태에서 [작업] > [API 배포]를 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/133966974-4d17ad51-64fa-4f7f-b41a-fceda6a13c85.png)

스테이지는 Workspace와 같습니다. 스테이지의 이름을 지어주고 [배포] 버튼을 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/133967095-3e9b374d-ce07-4f31-9b16-4de6b4b90ffb.png)

상단의 URL을 클릭합니다.   
접속을 시도해보면 오류가 납니다.   
단순 접속을 하게 되면 '/' 경로로 접속이 되고 리소스가 없기 때문에 오류가 나는 것입니다.   
뒤에 리소스 이름을 붙여주게 되면 람다가 호출됩니다.

`GET` 메서드 방식일 경우 리소스 이름을 붙여주게 되면 정상적으로 람다가 호출이 될 것이지만,
`POST` 메서드는 강화된 보안 기능으로 인해 여전히 람다가 호출되지 않습니다.   
이를 호출해주기 위해서는 URL 접근 방식이 아닌 정식으로 HTTP 요청을 해야합니다.

> <h3>POST 방식 테스트</h3>

API를 만들고 나서 테스트할 때 쓰이는 가장 유명한 도구는 `Postman`입니다.
유료/무료 버전이 있는데 간단한 테스트는 무료 버전으로 충분합니다.

Postman의 자세한 사용법은 아래의 링크를 참조해주세요.   
=> https://learning.postman.com/docs/writing-scripts/test-scripts/

Postman은 2가지 설치 방법이 있습니다. 크롬에서 설치하여 사용하는 방법, 프로그램 다운로드 방법입니다.

프로그램 다운로드의 경우 아래 링크에서 다운로드 받으시면 됩니다.   
=> https://www.postman.com/downloads/

크롬으로 설치하는 방법을 알아보겠습니다.

크롬 브라우저를 열고 아래의 링크로 접속합니다.   
=> https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=ko

![image](https://user-images.githubusercontent.com/43658658/133968401-d0161cbb-6105-435f-b206-ddf1a77b8e3f.png)

[Chrome에 추가] 버튼을 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/133968487-68308669-b1d8-44e5-a2a8-a46e15db3225.png)

위의 링크에서 `Postman`을 클릭합니다.

구글 계정 또는 다른 이메일을 통해 회원가입을 하고 유저 이름을 작성해주고 [Submit] 버튼을 눌러줍니다.

![image](https://user-images.githubusercontent.com/43658658/133968749-e849deff-5c1f-4ee5-af15-12f7a8f8ae80.png)

![image](https://user-images.githubusercontent.com/43658658/133969023-280b4b11-91d6-4478-b582-68456c7c0926.png)

`POST` 방식을 선택하고 리소스 이름까지 붙인 스테이지 URL을 작성하고 `Body` 항목에서 `row`를 선택한 뒤 테스트 이벤트를 작성합니다.   

![image](https://user-images.githubusercontent.com/43658658/133969140-8b353203-af98-4477-9a9d-0f335e796f5c.png)

[Send] 버튼을 누르고 결과를 확인합니다.

![image](https://user-images.githubusercontent.com/43658658/133969206-d5542b11-991a-405d-b7ff-6ebb4212f4da.png)

`API 대시보드`에 들어가면 각종 지표들을 확인해 볼 수 있습니다.   
특정 API만 과하게 호출되어 관련 서비스들이 먹통이 된다면   
과하게 호출되는 API를 모니터링하여 골라내 API를 나누거나, API에서 처리하는 로직을 다른 곳에서 처리하도록 분산합니다.





