# HANDOFF.md — 가족 소개 웹사이트 리팩토링

## 프로젝트 요약
`family.html`(단일 파일 가족 소개 웹사이트)을 데이터-뷰 분리 구조로 리팩토링하는 작업.

## 완료된 작업

### 1. 인터뷰 → plan.spec 작성
- 사용자 인터뷰를 통해 요구사항 확정
- `plan.spec` 파일로 전체 계획 문서화 (데이터 구조, 아키텍처, 트레이드오프, 검증 체크리스트 포함)

### 2. family.html 리팩토링 (완료)
- **FAMILY_DATA 객체 도입**: 모든 하드코딩 텍스트를 JS 데이터 객체로 추출
- **HTML 본문 → 빈 컨테이너**: `#hero-root`, `#members-root`, `#message-root`, `#values-root`, `#footer-root`
- **렌더링 함수 5개 작성**: `renderHero()`, `renderMembers()`, `renderMessage()`, `renderValues()`, `renderFooter()`
- **init() 함수로 통합**: 렌더링 → D-day 업데이트 → IntersectionObserver 순서
- **CSS 100% 유지**: 클래스명, 디자인 토큰, 애니메이션, 반응형 전부 그대로
- **TODO 주석 제거**: 데이터 객체에서 직접 수정 가능하므로 불필요

## 시도했으나 실패한 것
- 없음. 리팩토링은 한 번에 성공.

## 알려진 이슈
- **브라우저 검증 미완료**: 리팩토링 후 실제 브라우저에서 시각적 동일성 확인을 사용자가 아직 하지 않음
- **JS 비활성화 시 빈 페이지**: innerHTML 기반 렌더링이므로 JS 꺼지면 아무것도 안 보임 (로컬 전용이라 수용 가능)

## 파일 구조
```
claude_test/
├── CLAUDE.md         # 프로젝트 지침 (한국어 응답, 단일 파일 구조)
├── plan.txt          # 원본 사용자 요청
├── plan.spec         # 상세 구현 계획서
├── family.html       # 리팩토링 완료된 가족 소개 웹사이트
└── calculator.html   # 별도 프로젝트 (무관)
```

## 다음 단계
1. **브라우저 검증** — `plan.spec` 10번 항목의 체크리스트 수행
2. **사용자 피드백 반영** — 데이터 값 수정, 구성원 추가/삭제 등 요청 시 `FAMILY_DATA`만 수정
3. **추가 기능** — 사용자가 요청할 경우에만 (사진 추가, 타임라인 등)
