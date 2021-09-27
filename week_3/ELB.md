# 로드밸런싱(Load Balancing)

서버를 두 대를 쓰게 되면 한 대에 문제가 발생해도 다른 서버에서 서비스를 하면 되므로 `가용성`이 좋아집니다.   
서버 자체가 무거운 로직을 가지고 있다면 스팩 좋은 서버 한 개를 두는게 유리하지만,   
보통 웹 서버 자체는 무겁지 않기 때문에 스팩이 상대적으로 낮은 서버를 2개 두는 것이 더 유리합니다.

AWS에는 ELB라는 로드 밸런싱 서비스가 있습니다.   
트래픽이 발생할 경우 ELB에 등록된 여러 개의 서버로 트래픽을 순서대로 분산시켜줍니다.

## 로드 밸런싱

> <h3>RDS 접속 확인</h3>

먼저 EC2에서 RDS로 접속 가능한지 알아보겠습니다.   
RDS의 주소를 알아야 EC2에서 해당 주소로 접속이 가능합니다.

![image](https://user-images.githubusercontent.com/43658658/134855333-aef141cd-a84e-48e3-9977-2a6e951a8e74.png)

생성한 RDS의 세부 정보에서 `엔드 포인트`의 주소가 바로 RDS의 주소입니다.   
이 주소를 통해 터미널에서 RDS에 접속이 가능합니다.

![image](https://user-images.githubusercontent.com/43658658/134855457-61bb8eeb-1bd0-4a36-b3a6-823b90bef543.png)

```
mysql -u DB생성당시ID -p -h RDS엔드포인트
```

위의 형식으로 입력했을 때 MySQL로 접속이 된다면 정상적으로 EC2에서 RDS로 접속이 가능하다는 의미입니다.   
`using password` 오류가 나면, DB에 접속은 가능하나 패스워드가 틀렸다는 의미입니다.   
`connection` 관련 오류가 나면, 방화벽 설정에 문제가 있는 것입니다.   보안그룹, VPC, 서브넷 등을 확인하세요.   
exit를 입력해 MySQL을 빠져나올 수 있습니다.

> <h3>인스턴스 복제</h3>

웹서버에서 RDS로 정상적인 접속이 가능하니 같은 스팩의 서버를 2개 만들어보겠습니다.

![image](https://user-images.githubusercontent.com/43658658/134856176-ed3bdea4-b6e0-4dcc-8f24-fc3654bd3d20.png)

생성한 인스턴스를 체크하고 [작업] > [이미지 및 템플릿] > [이미지 생성]을 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/134856527-687c1573-7cde-41c2-868e-216c9cb72c88.png)

적절한 이름을 작성해주고 [이미지 생성] 버튼을 눌러 이미지 파일을 생성합니다.

![image](https://user-images.githubusercontent.com/43658658/134858797-6b5d415d-1c59-4352-9007-67d9b2704acb.png)

이미지 파일의 상태가 `available`이 되면 해당 이미지 파일을 체크하고 [작업] > [시작하기]를 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/134859006-c1c43643-f7cc-4c0d-b435-a2abb905a25b.png)

3단계의 VPC, 서브넷, 퍼블릭 IP 활성화 여부를 선택해줍니다.

![image](https://user-images.githubusercontent.com/43658658/134859102-239ee83d-421a-432b-9b0b-cb1ea1b3d5ce.png)

6단계의 보안 그룹은 기존 보안 그룹 중 앞서 생성한 인스턴스의 보안 그룹과 같은 것을 체크합니다.   
키 페어 파일을 새로 받아주고 인스턴스를 시작합니다.

복제한 인스턴스 역시 RDS에 정상적으로 접속이 가능한지 살펴봅니다.   
PuTTy에 접속해서 복제한 인스턴스의 `퍼블릭 IP 주소`와 `키 페어 파일`로 EC2에 접속합니다.   

![image](https://user-images.githubusercontent.com/43658658/134859684-15df55bb-6760-4709-a8f1-7986f225f217.png)

앞의 방법과 동일한 방법으로 RDS 접속 가능 여부를 확인합니다.

> <h3>로드 밸런서 생성</h3>

![image](https://user-images.githubusercontent.com/43658658/134860506-3d013258-cd86-4350-aa11-3560e0c3bd2c.png)

[로드 밸런서] > [로드 밸런서 생성] 버튼을 눌러줍니다.

![image](https://user-images.githubusercontent.com/43658658/134860658-3a35bb5c-554b-4c57-af2f-398c3f499f27.png)

`ALB`를 생성합니다.

![image](https://user-images.githubusercontent.com/43658658/134861117-e09e4e9e-4da7-4e39-ab4d-0f3dc8f3b455.png)

적절한 이름을 작성합니다.
인터넷을 통해 접속하므로 `인터넷 경계`를 체크해주고, 서울 리전의 경우 `IPv4`를 이용하므로 체크해줍니다.

![image](https://user-images.githubusercontent.com/43658658/134861446-935b3c3e-d570-4db7-81d5-91b8ee7100dc.png)

생성한 VPC와 서브넷을 설정해줍니다.   
첫 번째 가용 영역에서 퍼블릭 서브넷을 선택해주고, 다른 가용 영역에서 그 영역에서 생성한 프라이빗 서브넷을 선택합니다.

![image](https://user-images.githubusercontent.com/43658658/134861740-6cb52387-96e2-4bb3-b52c-36bb2a027172.png)

3단계로 넘어가 `웹 서버의 보안 그룹`을 선택합니다.

![image](https://user-images.githubusercontent.com/43658658/134862579-d34f0080-c418-466a-a610-90a3863011bc.png)

4단계에서 ELB에 등록할 웹 서버를 위한 그룹을 생성하는 절차입니다.   
우리는 인스턴스 2개를 등록할 것이므로 인스턴스를 체크해줍니다.

![image](https://user-images.githubusercontent.com/43658658/134862961-09287f21-6a38-4eff-b97b-f6729626ee9e.png)

상태 검사의 경로는 Apache의 경우 `/var/www/html`로 바꾸어줍니다.

![image](https://user-images.githubusercontent.com/43658658/134863129-4a75398c-9225-4c25-9b53-9f90c14a48e1.png)

5단계로 넘어가서 등록할 2개의 인스턴스를 체크하고 [등록된 항목에 추가] 버튼을 눌러 ELB에 등록합니다.   
마지막으로 [검토] > [생성] 버튼을 눌러 로드밸런서를 생성합니다.

![image](https://user-images.githubusercontent.com/43658658/134864050-caaae289-1566-42a1-94b2-2a7e1b40a77c.png)

생성한 로드 밸런서의 상태가 `active(활성)` 상태가 되면 DNS 이름을 웹 브라우저의 링크 창에 복사-붙여넣기 하여 접속해봅니다.

![image](https://user-images.githubusercontent.com/43658658/134864265-bd140e7c-d178-42c4-8365-e22da8cd99ad.png)

앞서 wordpress를 설치했기 때문에 위의 화면이 떠야합니다.

> <h3>ELB 테스트</h3>

ELB가 정상적으로 작동하는지 테스트해보겠습니다.

```
cd /var/www/html
sudo vi index.html
```

먼저 첫 번째 인스턴스의 터미널로 접속해서 `/var/www/html` 경로에 `index.html` 파일을 하나 생성해서 아래의 내용을 작성하고 저장합니다.

```
<html><body><p> Web Server 1 </p></body></html>
```

두 번째 인스턴스의 터미널로 접속해서 마찬가지로 `/var/www/html` 경로에 `index.html` 파일을 생성하고 아래의 내용을 입력하고 저장합니다.

```
<html><body><p> Web Server 2 </p></body></html>
```

![image](https://user-images.githubusercontent.com/43658658/134865527-b593573e-a118-467e-979b-44d94fe7fb6e.png)

![image](https://user-images.githubusercontent.com/43658658/134865621-c8091d22-6daf-43d2-92c8-2f75b4e1d65f.png)

이제 로드밸런서의 DNS 이름으로 다시 접속해서 새로 고침을 누르면 한 번은 `Web Server 1`, 다른 한 번은 `Web Server 2`가 번갈아가면서 나타납니다.   
이것은 2개의 서버에 순서대로 접속이 이루어진다는 의미입니다.

이제 ELB도 정상적으로 작동하는 것을 확인했습니다.

---
