# 성능 테스트

이번에는 성능테스트를 위한 툴을 설치해보고 DB부하 테스트에 사용해보겠습니다.

## Jmeter 설치

성능 테스트를 위한 툴은 여러가지가 있는데, 무료버전으로는 `Jmeter(Java)`와 `Locust(Python)`이 많이 사용됩니다.   
여기서는 만들어진지 가장 오래되어 웬만한 것을 모두 테스트 할 수 있는 `Jmeter`를 사용해보겠습니다.

Jmeter는 Apache 2.0 라이센스를 사용하고 있는데, 이는 오픈소스로 기업에서도 무료로 사용이 가능한 라이센스입니다.   
따라서 기업에서 Jmeter를 사용해도 무방합니다.

> <h3>Java 설치</h3>

Jmeter를 사용하려면 `자바8 버전 이상`이 필요합니다.

자바8 버전 이상이 없을 경우 아래 링크에서 OS에 맞는 버전을 다운로드 받아 설치합니다.   
=> https://www.oracle.com/java/technologies/downloads/#jdk17-windows

![image](https://user-images.githubusercontent.com/43658658/133916090-844dadc2-6ea1-4238-892e-53a872eb396a.png)

> <h3>Jmeter 설치</h3>

window OS를 사용하는 경우 Jmeter 툴은 아래의 링크에서 다운로드 받을 수 있습니다.   
=> https://jmeter.apache.org/download_jmeter.cgi

![image](https://user-images.githubusercontent.com/43658658/133916388-b2fcf033-17f1-4a2b-be01-0910c0bdfa3f.png)

`Binaries` 에서 `.zip`를 다운 받습니다.

![image](https://user-images.githubusercontent.com/43658658/133916457-04653200-b949-4bda-9d7f-696f1cecea34.png)

압축을 풀고 bin 폴더 내에 `jmeter.bat`을 실행합니다.   
(cmd창으로 로그 등을 볼 수 있으므로 닫지 않습니다)

접속을 하면 아래와 같은 화면이 나옵니다.

![image](https://user-images.githubusercontent.com/43658658/133916507-931a5020-8668-4418-819f-a98d00e10411.png)

Jmeter가 DB에 접속하기 위해서는 접속드라이버가 필요합니다.   
아래의 링크에 접속해서 필요한 접속드라이버를 다운로드합니다.   
=> https://dev.mysql.com/downloads/connector/j/

![image](https://user-images.githubusercontent.com/43658658/133916545-b8cfae75-8819-497a-b514-781694dbf066.png)

`platform independent` 메뉴에서 `zip`파일을 다운로드 받습니다.

![image](https://user-images.githubusercontent.com/43658658/133916568-b4880cb8-493f-4791-8226-a453c031ab09.png)

`No thanks, just start my download`를 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/133916656-d7898466-514a-437d-b415-05f877ff4177.png)

압축을 풀고 `압축(JAR)`파일을 Jmeter의 `lib`폴더에 복사합니다.

