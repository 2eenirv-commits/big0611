# 홍길동 포트폴리오 웹사이트

빅데이터 전문가 홍길동의 개인 포트폴리오 웹사이트입니다.

## 📋 프로젝트 개요

- **기술 스택**: HTML5, CSS3, JavaScript
- **디자인**: 모던하고 세련된 라이트 테마
- **레이아웃**: 풀 페이지 방식 (헤더, 4개 섹션, 푸터)
- **반응형**: 모바일, 태블릿, 데스크톱 지원

## 🎨 섹션 구성

1. **프로필**: 개인 소개, 경력, 목표
2. **스킬**: 데이터 엔지니어링, 웹 개발, 데이터베이스, 클라우드 & 배포
3. **포트폴리오**: 3개의 실전 프로젝트
   - 지하철 데이터 분석 플랫폼 (https://subwaykr.onrender.com)
   - 영화 추천 시스템 (https://movieflowkr.onrender.com)
   - 레시피 추천 앱 (https://recipekr.onrender.com)
4. **연락처**: 이메일, 전화번호, 위치, 연락 폼

## 📁 파일 구조

```
my/
├── index.html          # 메인 HTML 파일
├── css/
│   └── style.css      # 스타일시트
├── js/
│   └── main.js        # 자바스크립트 파일
├── images/
│   ├── subway.jpg     # 지하철 프로젝트 이미지
│   ├── movie.jpg      # 영화 프로젝트 이미지
│   └── recipe.jpg     # 레시피 프로젝트 이미지
├── favicon.ico        # 파비콘
└── README.md          # 이 파일
```

## 🚀 배포 가이드

### 1. GitHub에 업로드

```bash
# Git 초기화
git init

# 모든 파일 추가
git add .

# 커밋
git commit -m "Initial commit: 포트폴리오 웹사이트"

# GitHub 리포지토리 생성 후 연결
git remote add origin https://github.com/USERNAME/REPOSITORY_NAME.git

# 푸시
git branch -M main
git push -u origin main
```

### 2. Netlify에 배포

1. [Netlify](https://www.netlify.com/)에 가입
2. "New site from Git" 클릭
3. GitHub 리포지토리 선택
4. Build settings:
   - **Build command**: (비워둠)
   - **Publish directory**: (비워둠 또는 `.`)
5. "Deploy site" 클릭

## 📧 연락 폼 설정 (Formspree)

연락 폼이 실제로 작동하려면 Formspree 설정이 필요합니다:

### Formspree 설정 방법

1. [Formspree](https://formspree.io/)에 가입
2. "New Form" 클릭
3. 폼 정보 입력:
   - **Form name**: Portfolio Contact
   - **Recipient email**: 본인의 이메일 주소
4. 생성된 Form ID 복사 (예: `xvngykwj`)

### HTML 파일 업데이트

`index.html` 파일의 283번 라인에서:

```html
<!-- 변경 전 -->
<form class="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">

<!-- 변경 후 (실제 Form ID로 교체) -->
<form class="contact-form" action="https://formspree.io/f/xvngykwj" method="POST">
```

`YOUR_FORM_ID`를 실제 Formspree Form ID로 교체하세요.

## 🎨 사용자 정의

### 개인 정보 변경

`index.html` 파일에서 다음 정보를 본인의 실제 정보로 변경하세요:

- **이름**: "홍길동" → 본인 이름
- **이메일**: "honggildong@email.com" → 본인 이메일
- **전화번호**: "010-1234-5678" → 본인 전화번호
- **소셜 링크**: GitHub, LinkedIn URL

### 색상 테마 변경

`css/style.css` 파일의 CSS 변수를 수정하여 색상을 변경할 수 있습니다:

```css
:root {
    --primary-color: #4a90a4;      /* 주 색상 */
    --secondary-color: #357a8c;    /* 보조 색상 */
    --accent-color: #e8f4f8;       /* 강조 색상 */
    /* ... */
}
```

### 이미지 교체

`images/` 폴더의 이미지 파일을 실제 프로젝트 스크린샷으로 교체하세요:

- `subway.jpg` → 지하철 프로젝트 스크린샷
- `movie.jpg` → 영화 추천 시스템 스크린샷
- `recipe.jpg` → 레시피 추천 앱 스크린샷

이미지 크기는 800x600 픽셀을 권장합니다.

## 📱 반응형 디자인

이 웹사이트는 다음 디바이스에 최적화되어 있습니다:

- **데스크톱**: 1200px 이상
- **태블릿**: 768px - 1199px
- **모바일**: 767px 이하

## 🔧 기능

- **부드러운 스크롤**: 네비게이션 클릭 시 부드럽게 이동
- **모바일 메뉴**: 햄버거 메뉴 지원
- **스크롤 애니메이션**: 섹션 진입 시 페이드인 효과
- **폼 유효성 검사**: 이메일 형식, 필수 필드 검사
- **전화번호 자동 포맷**: 010-1234-5678 형식 자동 변환
- **액티브 네비게이션**: 현재 섹션 하이라이트

## 📝 라이선스

이 프로젝트는 개인 포트폴리오 용도로 제작되었습니다.

---

**제작자**: 홍길동  
**완성일**: 2024년
