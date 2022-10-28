# git 수업

## Undo

### Restore

git init

vi touch.md

insert -> hello

`esc` `:` `wq`

git add .

git commit -m'aaf'

git restore filename

### staging area에서 되돌리기

















`git add .`

`git commit -m'00'`

`git commit --amend`

commmit message 수정





## reset - 특정 커밋 상태로 되돌리기

백섭

soft -돌아간 시점 이후의 파일들 staging area에올라감

mixed - 돌아간 시점 이후의 파일드를 working directory로 돌려노음

hard - 돌아간 시점 이후 파일들 삭제

---

reflog -  하드리셋 복구

### soft



git reflog

git log --oneline

git reset --soft commitnum



### mixed



### hard

git reset --hard commitnumber

git log --oneline

복구하기

git checkout commitnumber



## revert

reset과 차이점 : reset은 커밋 내용 삭제, revert - commit 새로 쌓기

git revert {commitnumber}

git log  --oneline





## branch

`git branch {branch_name}` : 브렌치만들기,  이미 있는 브렌치 이름 안됨 새로운이름 필수

`git branch {브렌치 이름} {커밋ID}` : 특정 기준으로 브랜치 생성

`git branch -d`:  merge해야만 삭제가능

`git branch -D`:  강제삭제

`git checkout {브렌치 이름}`: 다른 브렌치로 이동

`git switch {브렌치이름}`:  다른 브렌치로 이동

`git switch -c {브렌치이름}`:  생성하고 바로 다른 브렌치로 이동

`git switch -c {브렌치이름} {commit_id}`:  특정 커밋 기준으로 다른 브렌치로 이동





`git branch -r`  : 원격 저장소(github)의 브랜치 목록 확인

`git branch` : 로컬 저장소의 브랜치 목록 확인



`git merge {합칠 브렌치 이름}`:

1. Fast Forward
2.  3 Way Merge
3.  Merge Conflict





