---
name: changelog
description: 프로젝트 변경 이력을 생성하거나 업데이트합니다. CHANGELOG.md 파일을 Keep a Changelog 형식으로 관리합니다.
---

CHANGELOG.md 파일을 생성하거나 업데이트하세요.

## 절차

1. 기존 `CHANGELOG.md`가 있으면 읽어서 내용을 파악한다.
2. `git log`로 최근 커밋 이력을 가져온다. 인자($ARGUMENTS)가 있으면 해당 범위/버전만 대상으로 한다.
3. 변경사항을 아래 카테고리로 분류한다:
   - **Added** — 새로운 기능
   - **Changed** — 기존 기능 변경
   - **Fixed** — 버그 수정
   - **Removed** — 제거된 기능
   - **Breaking** — 호환성이 깨지는 변경
4. [Keep a Changelog](https://keepachangelog.com/ko/1.1.0/) 형식을 따른다.
5. 날짜 형식은 `YYYY-MM-DD`를 사용한다.
6. 최신 항목이 파일 상단에 오도록 정렬한다.
7. 한국어로 작성한다.
