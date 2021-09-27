# Wordpress

## Wordpress 설정

본격적으로 Wordpress를 설치하기 위해 설정 파일을 하나 만들겠습니다.   
설정 파일의 경로는 `/var/www/html`에 있습니다.   
(앞서 Wordpress 관련 압축 파일을 해제하고 파일들을 /var/www/html 경로로 옮겨주었습니다)

`wp-config.php` 파일을 만들텐데 파일 리스트를 보시면 `wp-config-sample.php`가 있습니다.   
이 파일을 복사해서 wp-config.php 파일로 만든 후 wordpress와 관련한 설정을 해보겠습니다.

```
cd /var/www/html
sudo cp wp-config-sample.php wp-config.php
```

sample 파일을 복사해 준 후, `wp-config.php` 파일을 생성해줍니다.

```
sudo vi wp-config.php
```

편집 모드로 `wp-config.php`를 편집해줍니다.

![image](https://user-images.githubusercontent.com/43658658/134874244-3225d133-1ce0-4ae2-99fb-86716c0b0338.png)

이 부분을 수정해줍니다.   
DB 이름은 RDS를 생성할 당시 초기 데이터베이스의 이름을 적어주시면 됩니다.   
사용자명과 패스워드 역시 RDS를 생성할 때 설정한 ID와 패스워드를 적어주시면 됩니다.   
호스트는 RDS의 엔드포인트를 입력해주시면 됩니다.

한 가지 더 설정을 해보겠습니다.   
wordpress에서 설치할 일부 테마나 응용 프로그램은 EC2 서버 내에 폴더를 만들고 데이터를 저장시키도록 동작합니다.   
wordpress가 동작하고 있는 Apache가 EC2내에 폴더를 자유롭게 만들 수 있도록 권한이 필요합니다.

```
sudo chown -R apache:apache /var/www/html
```

다음의 명령어로 apache에게 /var/www/html 폴더 전권을 주도록 합니다.

![image](https://user-images.githubusercontent.com/43658658/134875057-115320fd-f14b-4030-b4fc-1ed5656fa4e9.png)

`/var/www/` 경로에서 `ll`을 명령했을 때 html 라인에서 apache apache가 뜬다면 올바른 설정이 된 것입니다.

복제된 서버에도 위의 과정을 똑같이 수행해줍니다.

> <h3>쿠버네티스의 사용 이유</h3>

웹서버가 많을 수록 같은 작업을 번거롭게 반복해야 합니다.   
이런 과정을 줄이고 한 번의 배포로 관련된 서버에 동시에 반영되도록 하는 툴이 바로 `쿠버네티스`입니다.   
=> [쿠버네티스 스터디 자료](https://www.eksworkshop.com/)

> <h3>Wordpress 설치</h3>

이제 EC2 퍼블릭 IP 주소에 `/wp-admin/install.php`를 붙여서 접속합니다.

![image](https://user-images.githubusercontent.com/43658658/134876119-a250a1b3-3d47-4be8-a80a-11a2e1f8ef07.png)

`한국어`를 선택해줍니다.

![image](https://user-images.githubusercontent.com/43658658/134876354-6f15ed66-9297-4746-8cc8-c253d7e8c66f.png)

Wordpress 계정을 생성하고 [워드프레스 설치] 버튼을 눌러 설치합니다.

![image](https://user-images.githubusercontent.com/43658658/134876477-8ecfb28f-0db9-4869-bafd-f42996cc029d.png)

[로그인] 버튼을 눌러 접속합니다.

![image](https://user-images.githubusercontent.com/43658658/134876581-b6560683-03c9-49bd-b866-9629c0ca87b1.png)

계정 생성 당시 사용자명과 비밀번호를 입력하고 로그인합니다.

![image](https://user-images.githubusercontent.com/43658658/134876794-35208719-bc10-4cd6-994b-716049394a33.png)

[외모] > [테마] > [새로 추가] 버튼을 누릅니다.

![image](https://user-images.githubusercontent.com/43658658/134877051-8710fcc7-6858-4ffa-86f4-a427e6013ba3.png)

`oceanwp`를 검색해서 설치합니다.

![image](https://user-images.githubusercontent.com/43658658/134877486-37202e89-b5b1-4059-b150-61143d662bcf.png)

[테마] 밑에 [사용자 정의하기] 버튼을 눌러 웹 페이지를 수정할 수 있습니다.
수정한 후 [공개] 버튼을 클릭하여 반영할 수 있습니다.

![image](https://user-images.githubusercontent.com/43658658/134878156-72059849-b627-4166-bd9b-96bf0b35e0ed.png)

이제 ELB의 DNS 이름을 통해서 웹 사이트에 접속하면 Wordpress 홈페이지가 나타납니다.   
다시 `관리자 모드`로 들어가고 싶다면 `DNS이름 + /wp-admin`을 통해 접속이 가능합니다.

> <h3>MySQL 조회</h3>

Wordpress의 경우 동적 웹 페이지이기 때문에 우리가 만든 DB를 조회해서 데이터를 표시합니다.   
EC2에서 RDS의 MySQL로 접속하여 초기 DB로 생성한 `wordpress` 이름의 DB에 Table을 조회해 보겠습니다.

![image](https://user-images.githubusercontent.com/43658658/134879122-0c02ca30-dae0-486c-a278-9ab1a7043852.png)

`mysql -E` 옵션은 조회 결과를 세로 모드로 깔끔하게 보여줍니다.   
`use DB이름`은 MySQL 내에 DB들 중 해당 DB로 들어가겠다는 뜻입니다.

![image](https://user-images.githubusercontent.com/43658658/134879401-9151eb96-d642-46da-946d-e53fd8cb058a.png)

`show tables`는 DB 내에 table들을 조회해줍니다.   
여기서 table 이름을 확인 후 Select 명령어를 통해 테이블 내의 데이터를 5개까지 표시해보겠습니다.   

![image](https://user-images.githubusercontent.com/43658658/134879628-f4753f74-eec1-45d1-bfb9-839cd7fb3a9d.png)

wordpress의 경우 대부분 웹 페이지에서 작업이 이루어집니다.   
웹 페이지에서 이루어지는 작업이 아닌 경우는 직접 DB에서 쿼리문을 통해 데이터 조회, 입출력을 하는 작업입니다.

> <h3>Wordpress 웹 디자인</h3>

Wordpress 웹 디자인의 경우 그림판 보단 어렵고 포토샵 보다는 쉬운 정도의 난이도입니다.   
유튜브를 검색해보면 자료가 많이 나와 있으니 참고해서 웹 페이지를 꾸며보시기 바랍니다.   
=> [Wordpress 웹 디자인 추천 자료 영상](https://www.youtube.com/watch?v=N7NYQTih-2U)

---

