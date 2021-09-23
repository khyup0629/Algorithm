# ★ aws-study ★

## Week 1

- [AWS 계정 생성](https://github.com/khyup0629/aws-study/blob/main/week_1/AWS%EA%B3%84%EC%A0%95%EC%83%9D%EC%84%B1_%EB%B9%84%EC%9A%A9%EC%98%88%EC%82%B0%EC%84%A4%EC%A0%95.md#aws-%EA%B3%84%EC%A0%95-%EC%83%9D%EC%84%B1)
- [비용 예산 설정](https://github.com/khyup0629/aws-study/blob/main/week_1/AWS%EA%B3%84%EC%A0%95%EC%83%9D%EC%84%B1_%EB%B9%84%EC%9A%A9%EC%98%88%EC%82%B0%EC%84%A4%EC%A0%95.md#%EB%B9%84%EC%9A%A9-%EC%98%88%EC%82%B0-%EC%84%A4%EC%A0%95) 
  - $10 청구서 비용 초과 알림 설정
- [네트워크 구축](https://github.com/khyup0629/aws-study/blob/main/week_1/%EC%9B%B9%EC%84%9C%EB%B2%84_%EB%A7%8C%EB%93%A4%EA%B8%B0.md#%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EA%B5%AC%EC%B6%95---vpc-%EC%84%9C%EB%B8%8C%EB%84%B7-%EC%9D%B8%ED%84%B0%EB%84%B7-%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4-%EB%9D%BC%EC%9A%B0%ED%8C%85-%ED%85%8C%EC%9D%B4%EB%B8%94-%EC%83%9D%EC%84%B1)
  - VPC, 서브넷, 인터넷 게이트웨이, 라우팅 테이블 생성 및 설정
- [EC2 웹서버 만들기](https://github.com/khyup0629/aws-study/blob/main/week_1/%EC%9B%B9%EC%84%9C%EB%B2%84_%EB%A7%8C%EB%93%A4%EA%B8%B0.md#ec2-%EC%9B%B9%EC%84%9C%EB%B2%84-%EC%83%9D%EC%84%B1) 
  - 인스턴스 시작, PuTTy, Apache 설치
- [추가 기능 설정](https://github.com/khyup0629/aws-study/blob/main/week_1/%EC%9B%B9%EC%84%9C%EB%B2%84_%EB%A7%8C%EB%93%A4%EA%B8%B0.md#ec2-%EC%B6%94%EA%B0%80-%EA%B4%80%EB%A6%AC-%EA%B8%B0%EB%8A%A5) 
  - 탄력적 IP 할당
  - 서버 백업(AMI, 스냅샷)
- [삭제하는 방법](https://github.com/khyup0629/aws-study/blob/main/week_1/%EC%9B%B9%EC%84%9C%EB%B2%84_%EB%A7%8C%EB%93%A4%EA%B8%B0.md#%EC%82%AD%EC%A0%9C%ED%95%98%EA%B8%B0---%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%9B%B9%EC%84%9C%EB%B2%84-%EC%B6%94%EA%B0%80-%EA%B4%80%EB%A6%AC-%EA%B8%B0%EB%8A%A5)
  - 인스턴스, AMI 및 스냅샷, 보안 그룹, 탄력젹 IP, VPC 삭제하기

## Week 4

- [성능 테스트](https://github.com/khyup0629/aws-study/blob/main/week_4/%EC%84%B1%EB%8A%A5_%ED%85%8C%EC%8A%A4%ED%8A%B8.md#%EC%84%B1%EB%8A%A5-%ED%85%8C%EC%8A%A4%ED%8A%B8)
	- `Jmeter`, Java 설치
	- 퍼블릭 액세스 허용 `DB 생성`, MySQL 설치(자신의 OS)
	- Jmeter를 이용한 `성능 테스트
- [람다 만들기](https://github.com/khyup0629/aws-study/blob/main/week_4/AWS_lambda.md#aws-lambda)
	- 람다 함수 만들기, 테스트 이벤트
	- API 게이트웨이 구축(리소스, 메서드, 스테이지, 배포)
	- POST 방식 테스트
- [웹서버 아키텍쳐 만들기](https://github.com/khyup0629/aws-study/blob/main/week_4/AWS_Webserver_Architecture.md#aws-%EC%9B%B9%EC%84%9C%EB%B2%84-%EC%95%84%ED%82%A4%ED%85%8D%EC%B3%90)
	- 주제 : 쇼핑몰
	- 3tier(WEB-WAS-DB)로 구성
	- Auto scaling, ELB, Cloudfront, SES, DynamoDB 등 확장성 지원
	- 고객 맞춤형 서비스 추천 아키텍쳐(SQS, SNS, Glue, Personalize)
	- 계정간 API 통신, 리전간 복제가 가능한 구조
