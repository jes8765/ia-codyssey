# AI 기반 브랜드 광고 패키지 기획서 (스토리보드)

---

## 1. 브랜드 아이덴티티 및 캠페인 정의

### 1) 브랜드 아이덴티티 (Brand Identity)
* **브랜드명:** 레고 (LEGO)
* **타겟:** 7~12세 자녀를 둔 부모 및 상상력과 모험을 좋아하는 아이들
* **톤앤매너:** 따뜻한 감성의 3D 픽사(Pixar) 애니메이션 스타일, 시네마틱 조명, 아늑하고 마법 같은 분위기
* **차별점 (USP):** "스케치북 속 평면의 낙서가 현실이 되듯, 아이들의 머릿속 상상을 손끝에서 완벽한 입체 현실로 구현하는 유일한 장난감."

### 2) 캠페인 목표 및 메시지
* **광고 목적:** 브랜드 인지(Awareness) 및 동심 자극을 통한 소장 욕구 전환(Conversion)
* **핵심 메시지 (한 문장):** **"네가 그리는 모든 상상, 레고가 현실로 만듭니다."**

---

## 2. 멀티모달 생성 도구 및 파이프라인 파악

| 미디어 타입 | 메인 도구 | 선택 이유 (강점) | 대체 도구 (접근성 대비) |
| :--- | :--- | :--- | :--- |
| **이미지** | Midjourney (v6) | 고품질 3D 애니메이션 질감 및 화풍 제어 탁월 | DALL-E 3, Adobe Firefly |
| **비디오** | Hailuo AI (MiniMax) | Image-to-Video 기능을 활용하여 정적인 이미지를 자연스러운 애니메이션 장면으로 변환하고, 캐릭터와 배경의 움직임을 효과적으로 구현할 수 있음 | Kling AI, PixVerse |
| **오디오** | Suno AI / ElevenLabs | 감성적인 배경음악 생성 및 정교한 효과음(SFX) 합성 강점 | Udio, Typecast |

> **일관성(Style/Character) 유지 전략:**
> 캐릭터 외모의 일관성을 위해 모든 이미지 프롬프트에 `8-year-old Korean boy, short dark hair, wearing cozy yellow pajamas, big innocent eyes`를 고정 탑재하고, 화풍 고정을 위해 `--sref` 파라미터 및 `3D Pixar-style animation, cinematic lighting` 키워드를 전 씬에 동일하게 적용함.

---

## 3. 씬별 상세 스토리보드 (Storyboard)

### 🎬 씬 1 (Intro)
* **씬 길이:** 5초
* **목표 메시지:** "모두가 잠든 밤, 진짜 모험이 시작됩니다."
* **화면 구성:** 어둡고 아늑한 아이 방. 침대에 이불을 덮고 누워 눈을 감고 있는 아이(노란 잠옷, 짧은 검은 머리). 방문이 살짝 열려 있고, 부모님의 실루엣이 복도의 따뜻한 불빛을 뒤로한 채 조용히 문을 닫고 나가는 뒷모습. (텍스트 없음)
* **사용 도구 및 목적:** 
  * 이미지: Midjourney (오프닝 키 비주얼 생성)
  * 비디오: Hailuo AI (문이 닫히고 실루엣이 움직이는 부드러운 모션 부여)
  * 오디오: Suno AI (잔잔하고 아늑한 자장가풍의 피아노 선율 레이어링)
* **입력 프롬프트 (원문):**
  > `A cinematic 3D Pixar-style animation, an 8-year-old Korean boy with short dark hair wearing yellow pajamas is lying in bed, eyes closed, pretending to sleep. A bedroom door is slowly closing, showing a soft warm light from the hallway and the blurred silhouette of parents leaving. Cozy and dark bedroom atmosphere, moonlight filtering through the window, highly detailed, 8k, photorealistic textures --ar 16:9`
* **출력 결과 요약:** 어두운 방안과 문틈 사이 조명의 대비가 뛰어난 3D 애니메이션 컷 확보.
* **결과 파일명:** `scene01_sleeping_boy.png` / `scene01_intro_motion.mp4` / `scene01_bgm.wav`

---

### 🎬 씬 2 (계기)
* **씬 길이:** 5초
* **목표 메시지:** "머릿속에 숨겨둔 비밀 스케치북을 펼치다."
* **화면 구성:** 문이 닫히자 아이가 눈을 번쩍 뜸. 침대에서 일어나 탁자의 은은한 노란색 스탠드 전등을 켬. 탁자 위에는 알록달록한 크레용들과 두꺼운 스케치북이 놓여 있고, 아이는 장난기 어린 설레는 표정으로 스케치북을 바라봄. (텍스트 없음)
* **사용 도구 및 목적:**
  * 이미지: Midjourney (스탠드 조명이 켜지는 순간의 극적 연출)
  * 비디오: Hailuo AI (아이가 눈을 뜨고 스탠드를 켜는 연출 제어)
  * 오디오: ElevenLabs (스탠드 스위치 켜지는 '딸칵' 효과음 삽입)
* **입력 프롬프트 (원문):**
  > `A cinematic 3D Pixar-style animation, the 8-year-old Korean boy with short dark hair and yellow pajamas excitedly opens his eyes in the dark. He sits up and turns on a small yellow bedside lamp. The warm light illuminates a thick sketchbook and colorful crayons on the wooden nightstand. He has a mischievous and excited smile, highly detailed, vivid colors, 8k --ar 16:9`
* **출력 결과 요약:** 아이의 생생한 표정과 따뜻한 스탠드 불빛의 퍼짐이 완벽히 조화된 컷 확보.
* **결과 파일명:** `scene02_turn_on_light.png` / `scene02_action_motion.mp4` / `scene02_click_sfx.wav`

---

### 🎬 씬 3 (전환 - 매개체)
* **씬 길이:** 6초
* **목표 메시지:** "그려둔 상상이 살아 숨 쉬며 깨어날 시간."
* **화면 구성:** 카메라가 탁자 위 스케치북으로 아주 가깝게 익스트림 줌인(Extreme Zoom-in). 거친 종이 질감 위로 파란색과 보라색 크레용으로 삐뚤빼뚤하게 그려진 '우주 고래' 그림이 화면 가득 채워짐. 그림 주변으로 은은하게 반짝이는 파스텔톤 입자들이 피어오름. (텍스트 없음)
* **사용 도구 및 목적:**
  * 이미지: Midjourney (크레용 마감 질감과 신비로운 stardust 이펙트 구현)
  * 비디오: Hailuo AI (정지된 크레용 그림에서 반짝이는 먼지들이 뿜어져 나오는 카메라 무브먼트 연출)
  * 오디오: ElevenLabs (지잉- 하는 신비로운 마법 상승 효과음)
* **입력 프롬프트 (원문):**
  > `A cinematic 3D Pixar-style animation, extreme close-up of a sketchbook page. A cute cosmic whale is drawn with blue and purple crayons on textured white paper. The drawing slowly begins to glow with faint magical stardust and pastel-colored glittering particles floating up from the paper, shallow depth of field, magical atmosphere, 8k --ar 16:9`
* **출력 결과 요약:** 평면 그림에서 입체적인 마법 효과로 넘어가는 몽환적인 비주얼 확보.
* **결과 파일명:** `scene03_whale_sketch.png` / `scene03_fadein_motion.mp4` / `scene03_magic_sfx.wav`

---

### 🎬 씬 4 (하이라이트 - 판타지)
* **씬 길이:** 8초
* **목표 메시지:** "방구석 작은 은하계가 눈앞에 펼쳐집니다."
* **화면 구성:** 스케치북을 뚫고 거대한 우주 고래가 공중으로 부드럽게 튀어나와 유영함. 고래의 궤적을 따라 방 전체 벽과 천장이 '야광 스티커'를 붙여놓은 것처럼 화려한 은하수, 별빛, 미니 행성 그래픽으로 채워지며 빛남. 아이는 침대 위에서 입을 벌린 채 감탄함. (텍스트 없음)
* **사용 도구 및 목적:**
  * 이미지: Midjourney (야광 스티커 테마의 우주 방과 생동감 넘치는 고래 구현)
  * 비디오: Hailuo AI (고래가 방 안을 크게 회전하며 날아다니는 다이내믹 모션 구현)
  * 오디오: Suno AI (음악이 오케스트라풍의 웅장하고 환상적인 분위기로 고조됨)
* **입력 프롬프트 (원문):**
  > `A cinematic 3D Pixar-style animation, a magical cosmic whale glowing in blue and purple neon tones flies out of the sketchbook into the air. The entire bedroom walls and ceiling transform, glowing vividly like cosmic glow-in-the-dark stickers, covered in mini planets and constellations. The 8-year-old Korean boy in yellow pajamas sits on his bed, looking up with wide eyes and open mouth in pure amazement, breathtaking cinematic lighting, 8k --ar 16:9`
* **출력 결과 요약:** 방 전체가 야광 우주로 변하는 압도적인 판타지 비주얼 완성.
* **결과 파일명:** `scene04_cosmic_room.png` / `scene04_flying_whale.mp4` / `scene04_orchestra_bgm.wav`

---

### 🎬 씬 5 (클라이맥스 - 해결)
* **씬 길이:** 8초
* **목표 메시지:** "네가 그리는 모든 상상, 레고가 현실로 만듭니다."
* **화면 구성:** 방 안을 돌던 우주 고래가 부드럽게 하강하여 아이가 내민 두 손 위로 착지함. 손에 닿는 순간 마법 같은 빛의 번쩍임과 함께 '달칵!' 소리가 나며 고래의 몸이 수 수만 개의 레고 블록으로 분해되었다가 정교한 **'레고 우주 고래 피규어'** 형태로 완벽히 조립됨. (텍스트 유: 하단 자막 코어 메시지 표출)
* **내레이션 / 카피:** (화면 자막 & 내레이션) "네가 그리는 모든 상상, 레고가 현실로 만듭니다."
* **사용 도구 및 목적:**
  * 이미지: Midjourney (실제 플라스틱 레고 브릭 질감의 고래 피규어와 아이 손 매칭)
  * 비디오: Hailuo AI (빛의 폭발과 함께 블록들이 맞물려 조립되는 모프/트랜지션 효과 연출)
  * 오디오: ElevenLabs (레고 브릭들이 연속으로 착착착- 달칵! 조립되는 시그니처 사운드 효과음)
* **입력 프롬프트 (원문):**
  > `A cinematic 3D Pixar-style animation, the glowing cosmic whale gently lands on the open hands of the 8-year-old Korean boy. At the moment of contact, a burst of magical light occurs, and the whale transforms with snapping plastic block textures into a highly detailed LEGO spaceship whale figure. Studio lighting on the hand-held LEGO object, vivid details, 8k --ar 16:9`
* **출력 결과 요약:** 판타지 생명체가 실제 장난감 레고 제품으로 치환되는 핵심 클라이맥스 연출 성공.
* **결과 파일명:** `scene05_lego_transform.png` / `scene05_assembly_motion.mp4` / `scene05_lego_brick_sfx.wav`

---

### 🎬 씬 6 (엔딩 및 CTA)
* **씬 길이:** 6초
* **목표 메시지:** "Imagine Anyting. LEGO" (브랜드 각인)
* **화면 구성:** 방 안의 야광 은하수 효과가 서서히 걷히고 원래의 아늑한 밤의 방으로 돌아옴. 아이는 완성된 레고 고래 피규어를 품에 꼭 껴안고 침대에 누워 행복하게 미소 짓고 있음. 마지막 3초간 화면 중심에 **LEGO 공식 로고**와 슬로건이 페이드인되며 마무리. (텍스트 유: 로고 및 슬로건)
* **내레이션 / 카피:** (내레이션) "Imagine Anyting. LEGO."
* **사용 도구 및 목적:**
  * 이미지: Midjourney (평온하고 행복한 엔딩 키 비주얼 확보)
  * 비디오: Hailuo AI (은은한 카메라 아웃포커싱 및 페이드아웃 처리)
  * 오디오: Suno AI (음악이 잔잔하게 페이드아웃되며 레고 특유의 브랜딩 사운드로 마무리)
* **입력 프롬프트 (원문):**
  > `A cinematic 3D Pixar-style animation, the 8-year-old Korean boy with short dark hair is lying back in his cozy bed, hugging the completed LEGO whale toy tightly to his chest. He has a peaceful and happy smile on his face. The bedroom is back to its quiet nighttime state with soft moonlight. Clean and heartwarming ending, 8k --ar 16:9`
* **출력 결과 요약:** 정서적 안정감과 여운을 주는 엔딩 컷 확보 후 편집기에서 로고 레이어 합성.
* **결과 파일명:** `scene06_ending_boy.png` / `scene06_fadeout_motion.mp4` / `scene06_logo_layer.png`

---

## 4. 프롬프트 개선 로그 (Prompt Improvement Log)

### 📌 씬 4 (하이라이트) 프롬프트 개선 내용
* **수정 전 의도:** 스케치북에서 고래가 나와 방을 날아다니는 판타지 연출.
* **초기 프롬프트:** `A cosmic whale flying in the kid's bedroom, 3D animation, fantasy`
* **문제점:** 레고 광고 특유의 '아이의 동심, 방구석 안에서의 아기자기한 놀이' 정서가 살지 않고 배경이 지나치게 이질적인 SF 우주 공간으로만 표현되어 화풍 일관성이 깨짐.
* **수정 후 변경:** 배경 설정을 아이들이 좋아하는 **'야광 스티커(glow-in-the-dark stickers)'** 테마로 구체화하고, 아이의 리액션(`looking up with wide eyes and open mouth in pure amazement`)을 추가하여 캐릭터 중심의 서사로 유도함. 또한 고정 스타일 키워드(`A cinematic 3D Pixar-style animation`)를 전면에 배치함.
* **결과 변화:** 인물과 화풍의 디테일 과장이 줄어들고 레고 브랜드 톤앤매너에 딱 맞는 따뜻하고 신비로운 스튜디오급 3D 애니메이션 톤 유지 성공.

---

## 5. 최종 영상 파일 정보 (Final Video Specification)

* **파일명:** `LEGO_CosmicWhale_Branding_Video_Final.mp4`
* **총 길이:** 35초
* **해상도:** 1920x1080 (16:9 Wide)
* **프레임레이트:** 30 fps
* **비디오 코덱:** H.264
* **오디오 코덱:** AAC
* **통합 편집 범위:** CapCut을 사용하여 AI 비디오 소스 컷 편집, 자막 추가, 각 씬별 오디오 볼륨 밸런싱(BGM 대비 SFX 효과음 부각) 및 최종 엔딩 3초 구간에 'LEGO 로고 프리셋 이미지' 디졸브 합성 진행.
