# 웹 서버 정적 배포

이번 시간에는 웹 페이지를 웹 서버에 배포해보겠습니다.   
=> https://html5up.net/   
위의 사이트로 접속해 마음에 드는 html5 기본 소스를 하나 다운 받습니다.

웹 페이지를 개발할 수 있는 능력이 있으시다면, 적절히 소스를 수정해서 자신만의 웹 페이지로 만들어주시고   
프론트엔드 개발을 할 줄 모르신다면 그냥 있는 다운 받은 웹 페이지를 그대로 사용하시면 됩니다.

## 웹 서버 배포

먼저 네트워크를 구축하고 Apache 웹 서버를 만듭니다.   
=> [네트워크 및 웹 서버 구축하는 방법](https://github.com/khyup0629/aws-study/blob/main/week_1/%EC%9B%B9%EC%84%9C%EB%B2%84_%EB%A7%8C%EB%93%A4%EA%B8%B0.md#%EC%9B%B9%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0)

웹 서버까지 모두 구축하고 퍼블릭 IP 주소로 접속하면 Apache 테스트 페이지가 보입니다.   
이 페이지 대신 우리가 만든(다운 받은) 웹 페이지의 `index.html` 파일이 표시되어야 합니다.

웹 페이지가 표시되게 하려면 적절한 위치에 우리가 만든 HTML 파일이 위치해야 합니다.   
이렇게 서버에 파일을 넣는 것이 바로 `배포`입니다.   
경로는 `var/www/html`입니다.

파일을 옮기는 방법은 윈도우 사용자라면 AWS의 권고대로 Filezilar 프로그램을 통해 옮기는 것이 권장됩니다.   
맥 또는 리눅스 사용자는 SFTP 명령어를 통해 파일을 옮깁니다.   
(실무에서는 주로 맥 또는 리눅스로 SFTP 명령어를 이용합니다)

저는 윈도우 사용자이므로 FileZilla를 통해 배포를 해보겠습니다.
=> [FileZilla 다운로드 사이트](https://filezilla-project.org/)

![image](https://user-images.githubusercontent.com/43658658/134776984-a4fbea72-9104-49e9-806d-64061a336c66.png)

OS에 관계없이 왼쪽 클라이언트 버전으로 다운 받습니다.

![image](https://user-images.githubusercontent.com/43658658/134841652-54a7cbfd-067b-4652-a3fe-d0b7b6b0af3c.png)

`Filezilla`를 실행하고, 상단 탭에서 [편집] > [설정]으로 들어갑니다.

![image](https://user-images.githubusercontent.com/43658658/134841727-5fa34c37-fc50-42eb-91b5-b96b45fc303a.png)

왼쪽 탭에서 [SFTP] > [키 파일 추가] 버튼을 클릭하여 인스턴스에 해당되는 키 파일을 추가합니다.

![image](https://user-images.githubusercontent.com/43658658/134841811-853a2671-b1fa-4568-9d03-bc5b24071c65.png)

호스트에는 `퍼블릭 IP 주소`, 사용자명에는 `ec2-user`, 포트에는 `22`를 입력하고 [빠른 연결] 버튼을 누르면
서버와 연결되어 `서버의 디렉토리 구성을 가시화`시켜줍니다.

경우에 따라 22번 포트로 입력해도 21번 포트로 연결을 시도하는 경우가 있습니다.   
이 경우 인바운드 규칙에 21번 포트를 열지 않았다면 접속 에러가 발생합니다.   
21번 포트로 접속을 시도하려다 에러가 발생하는 경우 인스턴스의 [보안 규칙] > [인바운드 규칙 편집]으로 들어가 21번 포트를 개방합니다.

이제 우리가 만든 웹 페이지 파일을 배포해봅시다.

![image](https://user-images.githubusercontent.com/43658658/134842702-b656f097-9285-41c0-a6c3-ddf2598cfc2b.png)

왼쪽 파트에서 웹 페이지 파일(HTML, assets, images)을 찾아서 `드래그 앤 드롭`으로 오른쪽 파트로 옮깁니다.   
처음부터 바로 `/var/www/html` 경로를 찾아서 배포해도 됩니다.   
하지만 그럴 경우 파일이 깨질 우려가 있습니다.   
그래서 연결된 폴더 아무 곳에 넣어주고 터미널에서 `/var/www/html`로 옮겨줄 것입니다.

`pwd` 명령어로 현재 위치를 확인한 후 웹 페이지 파일이 위치한 폴더 경로를 찾아 `cd` 명령어로 들어갑니다.

![image](https://user-images.githubusercontent.com/43658658/134844781-727d1fa3-75a0-409c-92a4-42a715ea63b9.png)

`ll` 명령어로 알맞은 웹 페이지 파일들이 들어있는지 확인합니다.   
`mv` 명령어로 HTML 파일을 모두 /var/www/html로 옮겨줍시다.

```
// mv 옮길파일 옮길경로
sudo mv *.html /var/www/html
```

그리고 CSS, JS 파일인 `assets` 폴더와 이미지 폴더인 `images` 폴더를 옮겨줍니다.

![image](https://user-images.githubusercontent.com/43658658/134844935-aa53bd1e-42e4-4086-bbc1-e9b178f29107.png)

`/var/www/html` 경로로 들어가서 파일 리스트를 확인해 보면 정상적으로 파일이 옮겨진 것을 확인할 수 있습니다.

![image](https://user-images.githubusercontent.com/43658658/134845354-992c0196-2aef-44fd-a18b-f85a19bb02a0.png)

이제 퍼블릭 IP 주소로 접속을 해보면 배포된 웹 페이지가 띄워지는 것을 확인할 수 있습니다.
