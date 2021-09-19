# 성능 테스트

이번에는 성능테스트를 위한 툴을 설치해보고 DB부하 테스트에 사용해보겠습니다.

- [Jmeter 설치](#Jmeter-설치)
- [DB 생성](#DB-생성)
- [Jmeter를 이용한 성능테스트](#Jmeter를-이용한-성능테스트)

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

## DB 생성

DB를 만들기 위한 VPC, EC2를 모두 구성해준 뒤 RDS 서비스를 이용해 DB를 만들어줍니다.

![image](https://user-images.githubusercontent.com/43658658/133924423-e9dba1d1-be4f-42a7-b686-f527d10c8ccd.png)

DB는 Private 서브넷에 생성되어 있으면 접속할 수 없습니다.
따라서 public 서브넷에 DB를 만들어주어야 합니다.   
public 서브넷을 두 개 만든 다음 RDS에서 서브넷 그룹으로 묶어서 사용하거나,   
RDS 생성 메뉴에서 `default VPC`를 선택하고 서브넷 그룹을 `기본값`, 퍼블릭 액세스를 `예`로 선택하는 2가지 방법이 있습니다.   
저는 후자의 방법을 선택해서 DB를 생성해보겠습니다.

> <h3>인바운드 규칙 수정</h3>

생성한 DB의 VPC 보안 그룹을 클릭해서 인바운드 규칙 수정 버튼을 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/133924940-2f89109a-99a9-49b4-9ebf-ce8f327f9d82.png)

22번 포트를 내 IP로 개방하여 터미널, CMD에서 접근할 수 있도록 해줍니다.   
3306번 포트를 내 IP로 개방하여 MySQL에 접근 가능하도록 해줍니다.

규칙 저장 버튼을 누릅니다.

> <h3>자신의 OS에 MySQL 설치</h3>

앞서 22번, 3306번 포트를 개방하여 로컬(자신의 OS)에서 CMD를 통해 MySQL에 접속이 가능하도록 설정해 주었습니다.   
따라서, 로컬에 `MySQL`의 설치가 필요합니다.   
아래의 링크로 접속하여 `MySQL Community`를 다운로드 받습니다.   
=> https://dev.mysql.com/downloads/mysql/

![image](https://user-images.githubusercontent.com/43658658/133925803-d418d64e-3042-45c5-bfbe-fa5e9ee5382e.png)

MSI Installer, 400MB 이상으로 설치합니다.   
RDS에서 지원하는 최신 버전은 8.0입니다. 따라서 버전은 8.0버전 이상으로 다운로드 받습니다.   
마찬가지로 `No thanks, just start my download`를 눌러서 다운로드 받습니다.

![image](https://user-images.githubusercontent.com/43658658/133926396-ab12d63c-ad44-4950-8766-b7f7b83e2370.png)

자세한 사항은 아래의 링크에 접속하여 따라하며 수행해봅니다.   
=> https://goddaehee.tistory.com/277   
(MySQL Server 설치 과정에서 이전에 MariaDB가 설치되어있을 경우 3306번은 충돌이 날 수 있으므로 `3305번 포트`로 바꿀 수 있습니다)

이제 `C:\Program Files\MySQL\MySQL Server 8.0\bin` 경로로 들어가서 아래의 명령어를 입력해 MySQL이 정상적으로 설치되었는지 확인해봅시다.

```
mysql --version
```

![image](https://user-images.githubusercontent.com/43658658/133928993-e1a12474-a96e-4aff-b190-6cb45072fb7f.png)

앞서 생성한 DB의 MySQL로 접속해 보겠습니다.

```
mysql -u admin(DB를 생성할 당시 ID) -p -h DB엔드포인트
```

![image](https://user-images.githubusercontent.com/43658658/133929081-cf794d5e-0b8a-42ad-bae0-86108f10d7aa.png)

DB에 부하를 주기 위해 DB와 Table을 만들어보겠습니다.

```
create database bootcamp;
use bootcamp;
create table cmt_table (sn varchar(10));
```

## Jmeter를 이용한 성능테스트

Jmeter는 실행될 때 lib폴더를 참조합니다.   
앞서 lib폴더에 파일을 추가한 이력이 있으므로, Jmeter를 닫고 재실행합니다.

Jmeter는 크게 네 가지 구성으로 이루어져 있습니다.
- Connector     : 테스트 서버에 `접속정보`를 입력합니다.
- Thread Group  : 테스트 서버에 `접속량`과 `빈도`를 입력합니다.
- Request       : 실제 테스트할 `로직`을 입력합니다.
- Result View   : 테스트 `결과`를 보여줍니다.

초보자를 위해 Jmeter에서는 템플릿을 제공하고 있습니다.   
상단 메뉴의 [File] > [Templates]를 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/133929625-ebdf5783-a2a1-4fa7-b565-3f8e6137b6a6.png)

`JDBC Load Test`를 선택하고 `Create` 버튼을 눌러서 불러옵니다.

> <h3>Connector 설정</h3>

![image](https://user-images.githubusercontent.com/43658658/133929738-ffc77bca-2940-4aca-95cc-1e85bf72c782.png)

jdbcConfig가 이 커넥터의 이름입니다.   
Max Number of Connections에 10을 넣어서 최대 10개의 커넥션을 맺을 수 있게 설정했습니다.

각 옵션에 대한 설명은 아래의 링크로 접속해 [Ctrl] + [F]를 이용해 찾아봅시다.   
=> https://jmeter.apache.org/usermanual/component_reference.html

![image](https://user-images.githubusercontent.com/43658658/133930002-111179a1-ea65-4b59-8ba7-88ef3b24d6c7.png)

스크롤을 아래로 내려 나머지 DB 접속 정보를 기록해줍니다.

`Database URL`에는 단순히 DB의 엔드포인트만 적어주면 안돼고,   
`jdbc:mysql://DB엔드포인트:3306/DB이름`의 형식으로 적어주어야 합니다.   
`Driver class`도 위와 같이 선택해주시고, `username`과 `password`는 DB 생성 당시 ID와 비밀번호를 입력해줍니다.

> <h3>Thread Group 설정</h3>

좌측 메뉴의 `Thread Group`을 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/133930239-7a773981-3b40-42e0-bc10-b8fbf7f87776.png)

- Number of Threads (users) : 쓰레드(접속 부하)의 총 수
- Ramp-up period (seconds)  : 테스트에 걸리는 총 시간
- Loop Count                : 반복 횟수

위와 같이 설정하면 3초(30/10)에 한 번씩 쓰레드가 걸립니다.   
이 작업을 2번 반복하게 됩니다.   
따라서 60초 동안 3초에 한 번씩 쓰레드가 걸려서 총 20번의 접속 부하를 줍니다.

> <h3>JDBC Request 설정</h3>

좌측 메뉴의 'Thread Group`의 하위 메뉴에 `JDBC Request`가 있습니다.   
여기서 실제 테스트할 로직을 작성합니다.

![image](https://user-images.githubusercontent.com/43658658/133930670-b8296c74-8852-4212-8a77-8f9e821b6291.png)

- Variable Name of Pool declared in JDBC Connection Configuration : Connector 이름을 작성합니다.
- Query Type : insert, update 쿼리문을 작성할 경우 `Update Statement`로 선택합니다.
- insert into cmt_table values ('a') : cmt_table에 'a'라는 데이터를 입력합니다.

> <h3>Result View</h3>

결과는 View Results Tree로 확인할 수 있지만, 이걸로는 부족합니다.   
[JDBC Request]를 우클릭하여 [Add] > [Listener] > [Summary Report]를 선택합니다.

Summary Reports는 요청성공여부 통계를 냅니다.   
DB에 부하가 많이 걸려서 요청이 실패하게 될 경우, 대략 몇 건까지 요청이 성공했는지 파악할 수 있습니다.

> <h3>성능 테스트</h3>

![image](https://user-images.githubusercontent.com/43658658/133930951-ff08896f-022e-462e-ad9a-c7c3af7e1190.png)

[File] > [Save]를 눌러 저장하고, JDBC Request 화면을 띄웁니다.   
상단의 시작버튼을 눌러 성능 테스트를 시작합니다.

![image](https://user-images.githubusercontent.com/43658658/133930982-77759aa9-615e-4599-8fd4-18d7f55155c5.png)

우측 상단에서 실행 시간과 진행 상황을 볼 수 있습니다.

만약 오류가 발생했다면 View Results Tree에서 오류발생 로그를 확인할 수 있습니다.   
빨간글씨가 나오면 오류가 발생한 것입니다.

![image](https://user-images.githubusercontent.com/43658658/133931081-16f3eea0-df7e-4e47-aa4d-e1777d06e317.png)

정상적인 경우 위와 같은 그림으로 나타납니다.

DB에 데이터가 잘 들어갔는지 확인해 볼 수 있습니다.

```
use bootcamp;
select count(1) from cmt_table
```

![image](https://user-images.githubusercontent.com/43658658/133931337-d9994be0-8990-4d13-8282-4111bb0aa5fc.png)

첫 번째 칼럼의 개수를 셉니다.   
쓰레드가 한 번 걸릴 때마다 첫 번째 칼럼에 `a`라는 데이터가 insert됩니다.   
앞서 총 20번의 접속 부하를 지정해주었으므로, 결괏값으로 20이 나타납니다.

`Thread Group`을 조절해서 CPU가 높아지는 순간이 언제인지 테스트 해보면서 DB의 성능적 한계를 파악할 수 있습니다.

