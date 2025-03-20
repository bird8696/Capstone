# GitHub에서 새로운 컴퓨터로 프로젝트 불러오기 및 푸쉬하기

팀원들과 GitHub 저장소를 공유하고, 새로운 컴퓨터에서 프로젝트를 불러와서 작업한 후 다시 푸쉬하는 방법을 설명합니다.

## 1. 새로운 컴퓨터에서 GitHub 저장소 클론하기

새로운 환경에서 프로젝트를 시작하려면, 먼저 Git이 설치되어 있는지 확인해야 합니다.

### Git 설치 확인
```sh
git --version
```
Git이 설치되지 않았다면, [Git 공식 사이트](https://git-scm.com/)에서 다운로드 후 설치하세요.

### GitHub 저장소 클론하기
1. 팀의 GitHub 저장소 URL을 확인합니다.
2. 터미널(또는 명령 프롬프트, Git Bash)에서 원하는 폴더로 이동한 후 다음 명령어 실행:
   ```sh
   git clone <저장소_URL>
   ```
   예시:
   ```sh
   git clone https://github.com/your-team/repository.git
   ```
3. 클론이 완료되면 해당 디렉토리로 이동합니다.
   ```sh
   cd repository
   ```

## 2. 작업 후 변경 사항 커밋하기
프로젝트를 수정하거나 파일을 추가한 후, 변경 사항을 저장소에 올립니다.

### 변경 사항 확인
```sh
git status
```
수정된 파일 목록을 확인할 수 있습니다.

### 변경된 파일 추가 (스테이징)
```sh
git add .
```
또는 특정 파일만 추가할 경우:
```sh
git add 파일이름
```

### 변경 사항 커밋
```sh
git commit -m "작업 내용 설명"
```
예시:
```sh
git commit -m "회원가입 페이지 UI 수정"
```

## 3. 변경 사항 푸쉬하기
팀의 저장소와 동기화하여 변경 사항을 올립니다.

### 최신 코드 가져오기 (충돌 방지)
```sh
git pull origin main
```
현재 `main` 브랜치의 최신 코드를 가져와 충돌을 방지합니다.

### 변경 사항 푸쉬
```sh
git push origin main
```
위 명령어를 실행하면 변경된 파일이 GitHub에 업로드됩니다.

## 4. 자주 사용하는 Git 명령어 정리
```sh
# 현재 브랜치 확인
git branch

# 새로운 브랜치 생성 및 이동
git checkout -b new-branch

# 브랜치 전환
git checkout main

# 원격 저장소 최신 내용 가져오기
git pull origin main

# 로컬에서 작업한 내용 푸쉬
git push origin main

# 변경 사항 취소
git reset --hard HEAD
```

이제 새로운 컴퓨터에서도 GitHub에서 파일을 불러와서 작업하고, 다시 푸쉬할 수 있습니다! 🚀


