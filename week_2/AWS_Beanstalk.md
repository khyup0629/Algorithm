# AWS Beanstalk

## Beanstalk

Beanstalk는 네트워크 구축, EC2에 웹 서버 프로그램을 설치하지 않고도 웹 서버를 구축할 수 있는 방법입니다.   
HTML을 배포하기 위해 사전에 준비해야 할 것이 너무나도 많습니다. 이는 작은 조직이나 작은 프로젝트에 있어서는 비효율적일 수 있습니다.   
AWS Beanstalk는 소스만 배포하면 사이트를 만들어주는 도구입니다.   
하지만 자동화가 된 만큼 많은 제약이 존재합니다.

> <h3>Beanstalk로 웹 서버 구축</h3>

Beanstalk로 웹 서버를 구축하기 이전에 `기본 VPC`가 존재해야 합니다.   
기본 VPC는 AWS 계정을 생성하면 자동으로 생성되지만 임의로 삭제하였을 경우 다시 생성해주어야 합니다.

![image](https://user-images.githubusercontent.com/43658658/134847080-aae94ee8-805c-4a97-8831-bfc3e44e6557.png)

VPC 목록 중 `기본 VPC`가 `예`로 설정되어 있는 VPC가 있는지 확인합니다.   
있을 경우 기본 VPC가 있는 것이고 없다면 아래의 방법으로 생성해야 합니다.

![image](https://user-images.githubusercontent.com/43658658/134847022-448b98f1-eecd-49a4-b1c7-87b8d51821e3.png)

기본 VPC를 생성하는 방법은 간단합니다. [작업] > [기본 VPC 생성]을 눌러서 생성할 수 있습니다.

이제 본격적으로 Beanstalk를 이용해 웹 서버를 구축해봅시다.

![image](https://user-images.githubusercontent.com/43658658/134846174-ad6872ea-6250-4bbd-a7ef-8e69436b4f96.png)

AWS 페이지 상단의 검색 창에 `Beanstalk`를 입력해서 접속합니다.

![image](https://user-images.githubusercontent.com/43658658/134846291-b10a08c4-d667-4cb6-8407-e59e9e94a02b.png)

[환경] > [Create Application]을 누릅니다.

![image](https://user-images.githubusercontent.com/43658658/134847194-08e2c640-be9b-47f6-97c8-549282d7fb01.png)

적절한 이름을 작성해주시고, 플랫폼을 선택해줍니다.   
플랫폼은 자신이 가장 자신있는 언어를 선택하시면 됩니다.(저는 Python을 선택하겠습니다)   
애플리케이션 코드는 `샘플 애플리케이션`을 선택합니다.   
샘플 애플리케이션은 Beanstalk 환경을 구성하는 기초 파일을 직접 코딩하지 않고 자동으로 생성해주는 것을 의미합니다.

[추가 옵션 구성]을 클릭해봅니다.

![image](https://user-images.githubusercontent.com/43658658/134847454-7f617664-7c15-4f71-ae82-1c403318595e.png)

Beanstalk 자체는 무료이지만 Beanstalk에 의해 생성되는 리소스는 유료일 수 있습니다.   
우리는 단일 인스턴스 프리티어를 선택해줍니다.

마지막으로 [앱 생성] 버튼을 누릅니다.

앞서 `샘플 애플리케이션`을 선택해주었기 때문에 기초 파일이 샘플로 제공이 됩니다.   
이 샘플 파일을 확인하는 방법은 아래와 같습니다.   
먼저 구글에 `AWS Beanstalk`를 검색하고, `AWS Elastic Beanstalk란 무엇입니까?`라는 제목의 사이트로 접속합니다.

![image](https://user-images.githubusercontent.com/43658658/134847705-85d0bf02-ca32-44f9-b380-fb0e097db1dd.png)

[시작하기] > [3단계:새 버전 배포]로 들어가면 각 언어에 해당되는 샘플 코드 압축 파일들이 존재합니다.   
자신이 선택한 플랫폼의 언어를 다운로드 받습니다.

![image](https://user-images.githubusercontent.com/43658658/134847881-47bfe1e0-f696-4b34-b00a-e5a84d0a5527.png)

이렇게 소스를 살펴볼 수 있습니다.   
고급 작업을 하려면 이곳의 소스 파일을 수정한 후 Beanstalk에 배포하면 됩니다.

![image](https://user-images.githubusercontent.com/43658658/134848229-21f6329d-fb21-4504-b22c-37baec0d465e.png)

Beanstalk 생성이 완료되면 [환경] > 자신이 만든 Beanstalk 환경 이름을 클릭합니다.

![image](https://user-images.githubusercontent.com/43658658/134848366-f6193687-40e1-4f5d-86fe-64a0862c0722.png)

![image](https://user-images.githubusercontent.com/43658658/134848412-a44bc9c5-2228-4a2d-b7f4-c2eea979a679.png)

[환경으로 이동] 버튼을 클릭하면 웹 서버 화면이 나타납니다.

![image](https://user-images.githubusercontent.com/43658658/134848579-b07379c3-9606-4ecd-b4f4-6270309b7094.png)

샘플 소스를 수정해서 `업로드 및 배포` 버튼을 눌러 소스 파일을 재배포하여 홈페이지를 수정할 수 있습니다.

---
