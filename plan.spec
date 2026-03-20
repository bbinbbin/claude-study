# Plan Spec: 가족 소개 웹사이트 — family.html 리팩토링

## 1. 프로젝트 개요

| 항목         | 내용                                          |
|-------------|----------------------------------------------|
| 서비스 유형   | 가족 소개 웹사이트 (단일 HTML 파일)               |
| 대상 파일     | `family.html`                                 |
| 배포 방식     | 로컬/브라우저 전용 (빌드 없음, 의존성 없음)         |
| 디자인 톤     | 파스텔 톤 (기존 유지)                            |

## 2. 인터뷰 결과 요약

| 항목           | 결정                                           |
|---------------|-----------------------------------------------|
| 데이터 관리     | JS 데이터 객체 분리 (HTML에서 분리)                |
| 기능 범위      | Hero, 멤버카드, 메시지, 가치관, D-day, 푸터        |
| 프로젝트 구조   | 단일 HTML 파일 (인라인 CSS/JS)                   |
| 애니메이션      | 미니멀 (hover + scroll fade-in)                |
| 기존 코드 처리  | family.html 직접 리팩토링 (새 파일 생성 아님)       |
| 우려사항       | 없음                                           |

## 3. 리팩토링 목표

- 모든 가족 데이터를 `FAMILY_DATA` JS 객체로 분리
- 데이터만 수정하면 UI가 자동 반영되는 구조
- 디자인(CSS)과 기능(D-day, fade-in)은 100% 유지
- HTML 본문의 하드코딩 텍스트 및 TODO 주석 제거

## 4. 데이터 구조 (`FAMILY_DATA`)

```js
const FAMILY_DATA = {
  familyName: string,     // 가족 이름 (Hero 제목, 푸터에 사용)
  slogan: string,         // Hero 슬로건 (HTML 허용)
  motto: string,          // 푸터 모토
  year: string,           // 푸터 연도 표시
  dueDate: string,        // 출산 예정일 (YYYY-MM-DD, D-day 계산용)

  members: [              // 가족 구성원 배열
    {
      emoji: string,      // 카드 이모지
      name: string,       // 이름/호칭
      role: string,       // 역할 배지
      desc: string,       // 소개 문장 (HTML 허용)
      tags: string[],     // 취미/특기 태그 (빈 배열 가능)
      type: 'normal'|'baby'  // baby이면 D-day 박스 포함
    }
  ],

  message: {
    title: string,        // 섹션 제목
    subtitle: string,     // 섹션 부제
    text: string          // 본문 (HTML 허용)
  },

  values: [               // 가치관 배열
    {
      icon: string,       // 이모지 아이콘
      title: string,      // 가치관 제목
      desc: string        // 설명
    }
  ]
};
```

## 5. 아키텍처 변경

### Before (기존)
```
family.html
├── <style>  ... CSS 전체
├── <body>   ... 하드코딩된 HTML 콘텐츠
└── <script> ... D-day 계산 + IntersectionObserver
```

### After (리팩토링)
```
family.html
├── <style>  ... CSS 전체 (변경 없음)
├── <body>   ... 빈 시맨틱 컨테이너 (id로 식별)
└── <script>
    ├── FAMILY_DATA 객체 (데이터 소스)
    ├── renderHero()
    ├── renderMembers()
    ├── renderMessage()
    ├── renderValues()
    ├── renderFooter()
    ├── updateDday()
    └── init()  (렌더링 → D-day → Observer)
```

### HTML 컨테이너 구조
```html
<section class="hero"><div class="container" id="hero-root"></div></section>
<section class="members"><div class="container" id="members-root"></div></section>
<section class="message-section"><div class="container" id="message-root"></div></section>
<section class="values-section"><div class="container" id="values-root"></div></section>
<footer id="footer-root"></footer>
```

## 6. 렌더링 함수 명세

| 함수              | 입력 데이터                    | 출력 대상        | 역할                              |
|------------------|-------------------------------|-----------------|----------------------------------|
| `renderHero()`   | familyName, slogan            | #hero-root      | Hero 배지 + 제목 + 슬로건          |
| `renderMembers()`| members[]                     | #members-root   | 섹션 헤더 + 카드 그리드 (baby → D-day) |
| `renderMessage()`| message                       | #message-root   | 섹션 헤더 + 메시지 카드             |
| `renderValues()` | values[]                      | #values-root    | 섹션 헤더 + 가치관 그리드           |
| `renderFooter()` | motto, familyName, year       | #footer-root    | 모토 + 가족명/연도                 |
| `updateDday()`   | dueDate                       | #dday-number/sub| D-day 카운트다운 계산 및 표시        |
| `init()`         | -                             | -               | 모든 렌더 + D-day + Observer 설정  |

## 7. 유지 항목 (변경 없음)

- **CSS 전체**: 색상 토큰, 레이아웃, 그리드, hover 효과, 반응형, 배경 orbs
- **폰트**: Noto Sans KR (Google Fonts CDN)
- **@keyframes**: bounce (스크롤 힌트), sparkle (아기 카드)
- **D-day 계산 로직**: diff 기반 D-N / D-Day / D+N 분기
- **IntersectionObserver**: threshold 0.15, data-delay 기반 fade-in

## 8. 제거 항목

- HTML 본문의 하드코딩된 텍스트 콘텐츠
- `<!-- TODO: -->` 주석 (데이터 객체에서 직접 수정 가능하므로 불필요)
- 기존 `DUE_DATE` 상수 (→ `FAMILY_DATA.dueDate`로 통합)

## 9. 트레이드오프

| 장점                                    | 단점                                      |
|-----------------------------------------|------------------------------------------|
| 데이터 수정 시 HTML 구조를 건드릴 필요 없음   | JS 비활성화 시 빈 페이지 (기존엔 정적 표시)     |
| 구성원 추가/삭제가 배열 조작만으로 가능       | innerHTML 사용으로 XSS 가능성 (로컬 전용이라 무관) |
| 단일 파일 유지 (배포 단순)                  | 대규모 확장 시 프레임워크 필요                  |

## 10. 검증 체크리스트

- [ ] 브라우저에서 `family.html` 직접 열기
- [ ] 리팩토링 전후 시각적으로 동일한지 비교
- [ ] `FAMILY_DATA` 값 변경 후 새로고침 → UI 반영 확인
- [ ] D-day 카운트다운 정상 동작
- [ ] 카드 hover 효과 (translateY -8px + box-shadow)
- [ ] 스크롤 fade-in 애니메이션 (IntersectionObserver)
- [ ] 모바일(375px) 반응형
- [ ] 데스크탑(1280px) 반응형

## 11. 구현 순서

1. `FAMILY_DATA` 객체를 `<script>` 상단에 작성
2. HTML 본문을 빈 컨테이너 구조로 교체
3. 렌더링 함수 작성 (renderHero → renderMembers → renderMessage → renderValues → renderFooter)
4. `init()` 함수에서 렌더링 + D-day + IntersectionObserver 통합
5. 기존 CSS 그대로 유지 (클래스명 변경 없음)
