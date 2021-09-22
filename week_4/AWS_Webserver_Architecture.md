# AWS 웹서버 아키텍쳐

쇼핑몰 사이트를 구현하기 위한 아키텍쳐를 그려봅시다.

요건
- 3tier : WEB - WAS - DB로 구성
- Auto scaling, ELB, Cloudfront 등 확장성이 지원되는 구조
- 리전간 복제가 가능, 계정간 API 통신이 있는 구조

## Web Server와 WAS(Web Appliccation Server)의 차이점
=> https://gmlwjd9405.github.io/2018/10/27/webserver-vs-was.html

![image](https://user-images.githubusercontent.com/43658658/134292603-e8baad08-1f77-43b8-ba57-4beb6d04c3e3.png)

> <h3>Web Server</h3>

- Web Server의 개념
  - 소프트웨어와 하드웨어로 구분된다.
  1) 하드웨어
    - Web 서버가 설치되어 있는 컴퓨터
  2) 소프트웨어
    - 웹 브라우저 클라이언트로부터 HTTP 요청을 받아 정적인 컨텐츠(.html .jpeg .css 등)를 제공하는 컴퓨터 프로그램
- Web Server의 기능
  - HTTP 프로토콜을 기반으로 하여 클라이언트(웹 브라우저 또는 웹 크롤러)의 요청을 서비스 하는 기능을 담당한다.
  - 요청에 따라 아래의 두 가지 기능 중 적절하게 선택하여 수행한다.
  1. 기능 1
    - 정적인 컨텐츠 제공
    - WAS를 거치지 않고 바로 자원을 제공한다.
  2. 기능 2
    - 동적인 컨텐츠 제공을 위한 요청 전달
    - 클라이언트의 요청(Request)을 WAS에 보내고, WAS가 처리한 결과를 클라이언트에게 전달(응답, Response)한다.
    - 클라이언트는 일반적으로 웹 브라우저를 의미한다.
- Web Server의 예
  - Ex) Apache Server, Nginx, IIS(Windows 전용 Web 서버) 등

> <h3>WAS(Web Application Server)</h3>

- `WAS`의 개념
  - DB 조회나 다양한 로직 처리를 요구하는 동적인 컨텐츠를 제공하기 위해 만들어진 Application Server
  - HTTP를 통해 컴퓨터나 장치에 애플리케이션을 수행해주는 미들웨어(소프트웨어 엔진)이다.
  - “웹 컨테이너(Web Container)” 혹은 “서블릿 컨테이너(Servlet Container)”라고도 불린다.
  - Container란 JSP, Servlet을 실행시킬 수 있는 소프트웨어를 말한다.
  - 즉, WAS는 JSP, Servlet 구동 환경을 제공한다.
- `WAS`의 역할
  - `WAS = Web Server + Web Container`
  - Web Server 기능들을 구조적으로 분리하여 처리하고자하는 목적으로 제시되었다.
  - 분산 트랜잭션, 보안, 메시징, 쓰레드 처리 등의 기능을 처리하는 분산 환경에서 사용된다.
  - 주로 DB 서버와 같이 수행된다.
  - 현재는 WAS가 가지고 있는 Web Server도 정적인 컨텐츠를 처리하는 데 있어서 성능상 큰 차이가 없다.
- `WAS`의 주요 기능
  - 프로그램 실행 환경과 DB 접속 기능 제공
  - 여러 개의 트랜잭션(논리적인 작업 단위) 관리 기능
  - 업무를 처리하는 비즈니스 로직 수행
- `WAS`의 예
  - Ex) Tomcat, JBoss, Jeus, Web Sphere 등

> <h3>Web Server와 WAS를 구분하는 이유</h3>

- `Web Server`가 필요한 이유?
  - 클라이언트(웹 브라우저)에 이미지 파일(정적 컨텐츠)을 보내는 과정을 생각해보자.
  - 이미지 파일과 같은 정적인 파일들은 웹 문서(HTML 문서)가 클라이언트로 보내질 때 함께 가는 것이 아니다.
  - 클라이언트는 HTML 문서를 먼저 받고 그에 맞게 필요한 이미지 파일들을 다시 서버로 요청하면 그때서야 이미지 파일을 받아온다.
  - Web Server를 통해 정적인 파일들을 Application Server까지 가지 않고 앞단에서 빠르게 보내줄 수 있다.
  - 따라서 Web Server에서는 정적 컨텐츠만 처리하도록 기능을 분배하여 서버의 부담을 줄일 수 있다.
- `WAS`가 필요한 이유?
  1. 웹 페이지는 `정적 컨텐츠`와 `동적 컨텐츠`가 모두 존재한다.
    - 사용자의 요청에 맞게 적절한 동적 컨텐츠를 만들어서 제공해야 한다.
    - 이때, Web Server만을 이용한다면 사용자가 원하는 요청에 대한 결과값을 모두 미리 만들어 놓고 서비스를 해야 한다.
    - 하지만 이렇게 수행하기에는 `자원이 절대적으로 부족`하다.
  2. 따라서 WAS를 통해 요청에 맞는 데이터를 DB에서 가져와서 비즈니스 로직에 맞게 그때 그때 결과를 만들어서 제공함으로써 자원을 효율적으로 사용할 수 있다.
- 그렇다면 WAS가 Web Server의 기능도 모두 수행하면 되지 않을까?
  1. 기능을 분리하여 `서버 부하 방지`
    - WAS는 DB 조회나 다양한 로직을 처리하느라 바쁘기 때문에 단순한 정적 컨텐츠는 `Web Server에서 빠르게 클라이언트에 제공하는 것이 좋다.`
    - `WAS`는 `기본적으로 동적 컨텐츠를 제공하기 위해 존재하는 서버`이다.
    - 만약 정적 컨텐츠 요청까지 WAS가 처리한다면 정적 데이터 처리로 인해 `부하가 커지게` 되고, 동적 컨텐츠의 처리가 지연됨에 따라 수행 속도가 느려진다.
    - 즉, 이로 인해 페이지 노출 시간이 늘어나게 될 것이다.
  2. 물리적으로 분리하여 `보안 강화`
    - SSL에 대한 `암복호화 처리에 Web Server를 사용`
  3. `여러 대`의 WAS를 연결 가능
    - `Load Balancing`을 위해서 `Web Server를 사용`
    - fail over(장애 극복), fail back 처리에 유리
    - 특히 대용량 웹 어플리케이션의 경우(여러 개의 서버 사용) `Web Server와 WAS를 분리하여 무중단 운영을 위한 장애 극복에 쉽게 대응`할 수 있다.
    - 예를 들어, 앞 단의 Web Server에서 오류가 발생한 WAS를 이용하지 못하도록 한 후 WAS를 재시작함으로써 사용자는 오류를 느끼지 못하고 이용할 수 있다.
  4. `여러 웹 어플리케이션 서비스` 가능
    - 예를 들어, `하나의 서버`에서 `PHP Application`과 `Java Application`을 함께 사용하는 경우
  5. 기타
    - 접근 허용 IP 관리, 2대 이상의 서버에서의 세션 관리 등도 Web Server에서 처리하면 효율적이다.
- 즉, `자원 이용의 효율성` 및 `장애 극복`, `배포 및 유지보수의 편의성` 을 위해 **Web Server와 WAS를 분리**한다.
- Web Server를 WAS 앞에 두고 필요한 WAS들을 Web Server에 플러그인 형태로 설정하면 더욱 효율적인 분산 처리가 가능하다.

> <h3>Web Service Architecture</h3>

- 다양한 구조를 가질 수 있다.
  1. Client -> Web Server -> DB
  2. Client -> WAS -> DB
  3. Client -> Web Server -> WAS -> DB

![image](https://user-images.githubusercontent.com/43658658/134294932-ca6822a5-0abc-443b-8add-5b70cd43a11f.png)

- 3번 구조의 동작과정

  1. Web Server는 웹 브라우저 클라이언트로부터 HTTP 요청을 받는다.
  2. Web Server는 클라이언트의 요청(Request)을 WAS에 보낸다.
  3. WAS는 관련된 Servlet을 메모리에 올린다.
WAS는 web.xml을 참조하여 해당 Servlet에 대한 Thread를 생성한다. (Thread Pool 이용)
HttpServletRequest와 HttpServletResponse 객체를 생성하여 Servlet에 전달한다.
5-1. Thread는 Servlet의 service() 메서드를 호출한다.
5-2. service() 메서드는 요청에 맞게 doGet() 또는 doPost() 메서드를 호출한다.
protected doGet(HttpServletRequest request, HttpServletResponse response)
doGet() 또는 doPost() 메서드는 인자에 맞게 생성된 적절한 동적 페이지를 Response 객체에 담아 WAS에 전달한다.
WAS는 Response 객체를 HttpResponse 형태로 바꾸어 Web Server에 전달한다.
생성된 Thread를 종료하고, HttpServletRequest와 HttpServletResponse 객체를 제거한다.

- Servlet => https://gmlwjd9405.github.io/2018/10/28/servlet.html

## Auto Scaling

`Auto Scaling` 기능을 통해 필요에 따라 인스턴스 동적으로 늘리거나 줄일 수 있습니다.   

자세한 설명은 아래의 링크를 통해 예시를 확인해보시기 바랍니다.
=> https://docs.aws.amazon.com/ko_kr/autoscaling/ec2/userguide/auto-scaling-benefits.html

## CloudFront

`Amazon CloudFront`는 .html, .css, .js 및 이미지 파일과 같은 정적 및 동적 웹 콘텐츠를 사용자에게 더 빨리 배포하도록 지원하는 웹 서비스입니다.

CloudFront에는 `S3`, `Edge Location`이 존재합니다.
`S3`는 오리진 서버로 최종 원본 콘텐츠가 저장됩니다.   
`CloudFront`는 `S3`에서 콘텐츠를 가져와 전 세계 `Edge Location`에 배포합니다.   
클라이언트가 웹페이지의 콘텐츠를 요청할 때 지연 시간이 가장 낮은 `Edge Location`에 콘텐츠가 있을 경우   
`CloudFront`는 해당 `Edge Location`에서 콘텐츠를 가져옵니다.
해당 콘텐츠가 `Edge Location`에 없다면, `CloudFront`는 `S3`에서 최종 버전의 해당 콘텐츠를 검색합니다.

자세한 설명은 아래의 링크를 참조바랍니다.
=> https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/Introduction.html

## Dynamo DB

`DynamoDB`는 NoSQL 데이터베이스의 한 종류로 관계형 데이터베이스와 반대되는 개념의 데이터베이스입니다.   
=> [관계형 데이터베이스(RDS)와 NoSQL 데이터베이스의 차이점](https://aws.amazon.com/ko/nosql/)   
`DynamoDB`는 어떤 규모에서도 10밀리초 미만의 성능을 제공하는 키-값 및 문서 데이터베이스입니다. 완전관리형의 내구성이 뛰어난 다중 리전, 다중 활성 데이터베이스로서, 인터넷 규모 애플리케이션을 위한 보안, 백업 및 복원, 인 메모리 캐싱 기능을 기본적으로 제공합니다. `DynamoDB`는 하루에 10조 개 이상의 요청을 처리할 수 있고, 초당 2,000만 개 이상의 피크 요청을 지원할 수 있습니다.    
주로 모바일, 웹, 게임, 광고 기술, IoT 및 규모와 상관없이 `지연 시간이 짧은 데이터 액세스`가 필요한 기타 애플리케이션을 위한 키-값 및 문서 데이터베이스로 `DynamoDB`를 선택합니다.

## 고객 맞춤형 서비스 추천 아키텍쳐

[SQS](https://aws.amazon.com/ko/sqs/)   
[SNS](https://aws.amazon.com/ko/sns/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)   
[Glue](https://aws.amazon.com/ko/glue/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)   
[Personalize](https://aws.amazon.com/ko/personalize/)

## AWS 웹서버 아키텍처 - 쇼핑몰

![image](https://user-images.githubusercontent.com/43658658/134333004-ea914c15-e851-4c99-9a36-fccb5854f53d.png)





---
참고한 아키텍처   
- [UZEN G1 Commerce 플랫폼](https://aws.amazon.com/ko/partners/success/uzen/)
- [Brandi](https://aws.amazon.com/ko/solutions/case-studies/brandi/)
- [Trenbe](https://aws.amazon.com/ko/solutions/case-studies/trenbe/)



