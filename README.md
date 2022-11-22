## Jo-Ving

알고리즘 기반의 영화 추천 서비스

## tools

### Front

- vue

### Back

- Django

### 아이디어


## 구현 목표
1. signup 완료시 좋아하는 영화 pick 고고
2. 영화 추천(main: (고려 중...) // detail: 유사 장르, 이 영화를 본 다른 사람이 시청한..)
<!-- 3. 찜, 찜 목록 조회 -->
4. 리뷰(별점, 답글)
<!-- 5. 검색(최근 검색어, 인기검색어, 검색시 비동기로 바로 포스터 출력) -->


## ERD
![erd](https://user-images.githubusercontent.com/109322161/202946378-264f5050-76bb-45b7-a028-9c2e581d804f.png)


## 전체 일정
11.16 - 11.21 : 추천, 추가 기능 제외 기초 구현 완료하기
<br>
11.21 - : 추천 기능 및 css .. 시간이 된다면 욕심 나는 기능..

## 11.17
movie_list, user 기초 구현

front 스켈레톤 구성

## 11.18
back - review endpoint시작.. user도 보충 필요하다(프론트 axios해결되면)
front - 기본 스켈레톤 코드와 컴포넌트 제작.(css제외 back과 연결 전 상태 완성)

## 11.21
(주말 간 sign up, login 구현.)
 front : 토큰 처리, 라우팅
 back : review, 영화 찜 기능 구현

 ## 11.22
 back - 찜한 목록 완성, 답글 구현 및 추천 알고리즘 구현
 front - 검색(최근 검색어, 인기검색어, 검색시 비동기로 바로 포스터 출력), signup 완료시 좋아하는 영화 pick 고고
 과연 css 시작할 수 있을지..

  --- 22:46
  => 대댓글 모델 확인 해야함(교수님께 여쭤보기), 
  => movies.views.py에 신작 핫 완성(recommend1), 댓글 공감(모델 되면 되게 함수는 짜둠), pick&like 분리 끝
