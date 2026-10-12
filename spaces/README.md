# 공간 배치

`cafe_previs.html`이 여는 공간 배치 파일을 모아 둔 폴더입니다. 툴은 하나이고, 공간마다 배치 파일만 따로 둡니다.

- 여는 주소: `cafe_previs.html?space=dalbit` (머리말의 "공간" 목록에서도 고를 수 있습니다)
- `index.json`: 목록에 보일 공간. `id`는 주소에 쓰는 이름, `file`은 이 폴더 안의 배치 파일
- `royal_banquet.json`: 궁중 연회장 (12×18m, 천장 7m, 30초 5샷 동선). 여는 주소는 `cafe_previs.html?space=banquet`. 마찬가지로 `builtinSpaces`에도 들어 있습니다.
- `dalbit_pungryu.json`: 달빛풍류 주막 (5×7m, 30초 5샷 동선). 같은 내용이 `cafe_previs.html` 안(`builtinSpaces`)에도 들어 있어, 툴은 그쪽을 먼저 씁니다. 배치를 고치면 두 곳을 함께 바꿉니다.

## 새 공간 추가 (예: 화음스튜디오)

1. 툴에서 벽·가구·카메라를 배치하고 "프로젝트 저장"을 누릅니다.
2. 받은 JSON 파일을 이 폴더에 넣습니다. 파일 안 `space` 값(`id`, `title`, `prefix`, `place` 등)을 그 공간에 맞게 바꿉니다.
3. `index.json`에 한 줄을 추가합니다.
