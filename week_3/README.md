# 2tier 구축

이번 시간에는 DB와 연동되어 사용하는 `2-tier`를 구축해보겠습니다.

`2-tier`란 웹서버-DB로 연동되는 구조로, 트래픽이 많지 않은 경우 자주 사용되는 구조입니다.   
또한 웹서버를 안정적으로 구동시키기 위해 2대의 웹서버가 하나의 도메인을 사용하도록 구성해보겠습니다.

## VPC 생성

> <h3>VPC 마법사</h3>

이번 시간에는 VPC 마법사를 통해 VPC를 생성해보겠습니다.

그 전에 먼저 `EIP(탄력적 IP)`를 생성해야 합니다.   
VPC 마법사를 이용해 VPC를 생성할 때 필요하기 때문입니다.   
다른 설정없이 `EIP`를 할당해줍니다.

이제 [VPC 대시보드] 탭으로 들어가서 [VPC 마법사 시작] 버튼을 눌러줍니다.

![image](https://user-images.githubusercontent.com/43658658/133917873-0f90ece4-dd7f-4d20-ab40-5448e6d7f48d.png)

1단계에서는 [퍼블릭 및 프라이빗 서브넷이 있는 VPC]를 선택합니다.

![image](https://user-images.githubusercontent.com/43658658/133917904-f72947f6-ef7e-4fb2-8ccc-55b8d7ce9e99.png)

2단계에서는 위와 같이 IP를 할당합니다.   
퍼블릭 서브넷과 프라이빗 서브넷의 가용 영역은 '2a, 2c, 2d' 중 하나로 설정합니다.   
'2b'의 경우 프리티어가 사용할 수 없는 영역입니다.

탄력적 IP는 방금 생성한 EIP로 설정합니다.

> <h3>서브넷 추가 생성</h3>

[서브넷] 탭에 들어가면 VPC 마법사를 통해 생성한 퍼블릭 서브넷과 프라이빗 서브넷이 생성되어 있습니다.   
적절히 이름을 바꿔주고 우측 상단의 [서브넷 생성] 버튼을 클릭합니다.

DB를 안정적으로 운영하기 위해서 2개 이상의 서브넷을 사용하는 것이 좋습니다.   
다른 존에 있는 서브넷에 복제본을 두기 위함입니다.   

![image](https://user-images.githubusercontent.com/43658658/133918204-617b01b9-8f56-40bc-ace4-e26942a3b725.png)

VPC는 방금 생성한 VPC로 지정합니다.   
가용영역은 VPC를 생성할 때 지정한 영역과 다른 영역으로 하나 지정해줍니다.   
(만약 전에 '2a'로 생성했다면, '2b, 2c, 2d'중 하나로 지정합니다)   
IP는 `10.13.3.0/24`로 지정합니다.

[생성] 버튼을 눌러 서브넷을 생성합니다.

> <h3>NAT 게이트웨이, EIP 제거</h3>

VPC 마법사를 통해 VPC를 만들면 자동적으로 `NAT 게이트웨이`가 생성되는데, 나중에 비용이 청구될 수 있는 원인이 됩니다.   
당장 사용하지 않는 기능이므로 비용이 발생하지 않도록 삭제를 해야 합니다.

[NAT 게이트웨이] 탭으로 들어가서 해당 NAT 게이트웨이를 삭제합니다.

![image](https://user-images.githubusercontent.com/43658658/133918347-9b6de6dd-39f3-4670-9751-b713fb2f1718.png)

마찬가지로 EIP 역시 당장 사용하지 않으므로, 비용이 청구됩니다.   
[탄력적 IP] 탭으로 들어가 EIP를 삭제합니다.

![image](https://user-images.githubusercontent.com/43658658/133918451-9fc3f33e-c828-47fc-9404-4b63d5c84ca5.png)

> <h3>라우팅 테이블 확인</h3>

VPC 마법사를 통해 VPC를 만들면, 자동으로 `인터넷 게이트웨이`, `NAT 게이트웨이`, 그리고 이와 연결된 `라우터`들을 자동으로 만들어줍니다.

[라우팅 테이블] 탭으로 들어가면, 앞서 만들었던 VPC와 연결된 라우팅 테이블이 2개가 있을 것입니다.   
하나는 `인터넷 게이트웨이`, 다른 하나는 `NAT 게이트웨이`에 연결되어 있습니다.

![image](https://user-images.githubusercontent.com/43658658/133918577-b27077df-17b1-43a6-a756-a2a502118ab0.png)

우리는 앞서 NAT 게이트웨이를 제거했으므로 NAT와 연결되는 라우터는 필요가 없습니다.   
라우팅 테이블 ID를 클릭해서 위와 같이 라우팅이 nat와 연결되어 있는 라우터인지 확인합니다.

![image](https://user-images.githubusercontent.com/43658658/133918669-53032e25-deae-403a-ab19-8259558bc3e9.png)

인터넷 게이트웨이와 연결된 라우터를 찾아 적절한 이름을 부여합니다.

## EC2 인스턴스 생성

> <h3>웹서버 in 퍼블릭 서브넷</h3>

퍼블릭 서브넷에 웹서버를 만들어 보겠습니다.   
EC2 서비스에서 [인스턴스] 탭으로 들어가 인스턴스를 생성합니다.

![image](https://user-images.githubusercontent.com/43658658/133918801-cf28ffaa-40bc-4b33-8cf2-92bbed40f788.png)

서브넷은 퍼블릭 서브넷으로 지정합니다.

![image](https://user-images.githubusercontent.com/43658658/133918856-fd4d85f0-a0ff-45e8-a5f3-a41fab5bb970.png)

보안 그룹은 위와 같이 생성합니다.   
22번 포트는 `내 IP`로, 80번 포트는 '0.0.0.0/0`으로 개방합니다.

키페어 파일을 받고 인스턴스를 생성합니다.

## Wordpress, Apache, PHP, MySQL 설치

window OS 사용자의 경우 `PuTTy`를 이용해 생성한 EC2 서버에 접속합니다.

> <h3>Wordpress 유저 생성</h3>

`Wordpress`는 인터넷 웹페이지를 제작하기 쉽게 만들어주는 도구입니다.   
(전세계 웹사이트의 30%가 이걸로 만들어졌다고 합니다)   
웹페이지 언어는 PHP 기반이고, MySQL DB를 사용하게 되어 있습니다.

```
// 유저 생성
sudo useradd acwordpress
```

```
// 비밀번호 설정
sudo passwd acwordpress
```

![image](https://user-images.githubusercontent.com/43658658/133919156-cec0b4b8-491d-437f-b489-00c851e25423.png)

> <h3>Wordpress 유저 권한 부여</h3>

```
sudo vi /etc/sudoers
```

root ALL = (ALL) ALL을 찾아 그 밑에 아래와 같이 입력합니다.
(만약 위의 문구를 찾지 못하겠으면 아무곳에나 입력해도 무방합니다)

![image](https://user-images.githubusercontent.com/43658658/133919206-688535b9-3b4f-4e3e-84b1-348cb09ffacc.png)

> <h3>Apache, MySQL, PHP 설치</h3>

```
// Apache 설치
sudo yum install -y httpd
```

```
// MySQL 설치
sudo yum install -y mysql
```

```
// PHP 설치
sudo amazon-linux-extras install -y php7.3
```

> <h3>Wordpress 설치</h3>

먼저 압축파일과 관련된 프로그램인 `wget`을 설치합니다.

```
sudo yum install wget
```

Wordpress의 가장 최신 설치 압축 파일을 다운로드 받습니다.

```
sudo wget https://wordpress.org/latest.tar.gz
```

받은 설치파일의 압축을 풉니다.

```
sudo tar zxvf latest.tar.gz
```

wordpress 폴더로 들어가 폴더의 파일들을 강제로 `/var/www/html`로 복사합니다.

```
cd wordpress
sudo cp -rf * /var/www/html
```

마지막으로 Apache를 실행시키고, EC2를 재부팅했을 때 자동으로 Apache가 실행되도록 설정합니다.

```
sudo service httpd start
sudo chkconfig httpd on
```

## RDS 생성

RDS는 AWS에서 관계형 DB를 사용할 수 있도록 하는 플랫폼 서비스입니다.   
wordpress에서 사용할 수 있는 MySQL을 무료버전으로 만들어보겠습니다.

> <h3>서브넷 그룹 생성</h3>







