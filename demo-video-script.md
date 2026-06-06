# Demo Video Script — Saxiy Makler TikTok Submission

> **Maqsad:** TikTok app review reviewer'i talab qilgan **end-to-end** flow ni real ko'rinishda (flowchart EMAS) ko'rsatish. Eski demo'da flowchart bor edi va shu sababli rad qilindi.
>
> **Davomiyligi:** 60-90 sekund (optimal 75)
> **Format:** Screen recording (1920×1080 horizontal yoki 1080×1920 vertical — TikTok Portal'da yuklash uchun MP4)
> **Audio:** Voice-over (inglizcha) + ekran tovushi
> **Yozish vositasi:** OBS Studio, ScreenToGif, yoki Windows Game Bar (Win+G)

---

## Reviewer talablari (yodda tutish)

Reviewer xabaridan to'g'ridan-to'g'ri:

> "The demo video should show the **complete end-to-end flow** of the integrations with TikTok (Please demonstrate with sandbox or provide a mockup demo). The demo video is **not related to the website** provided. Please demonstrate the user experience & how you use TikTok for Developers' capabilities inside your app & **not flowchart inside Demo Video**. Demo video does not provide enough clarity and context as to show the website functions."

**Demak demo MAJBURIY ko'rsatishi kerak:**
1. ✅ Website (`https://amir4874.github.io/saxiy-makler-legal/`) — favicon va header logo bilan
2. ✅ Botning real (yoki mockup) ishlashi — UX
3. ✅ TikTok auth dialogu (sandbox yoki mockup)
4. ✅ Video upload progress
5. ✅ TikTok'da publish bo'lganini ko'rsatish
6. ❌ Flowchart YO'Q — har qadam jonli ko'rsatilsin

---

## Storyboard (kadr-kadr)

### Kadr 1: Website intro (0:00 – 0:08, 8 sek)

**Ekran:** Browser ochilib `https://amir4874.github.io/saxiy-makler-legal/` ga o'tadi.

**Diqqat markazi:**
- **Browser tab'ida** Saxiy Makler favicon ko'rinishi (kursorni tab'ga yaqinlashtir)
- Sahifa **header'idagi 48×48 logo + "Saxiy Makler" matn**

**Voice-over (en):**
> "This is Saxiy Makler — a real estate video publisher for the Uzbekistan market. You can see the official website with our app icon in the browser tab and in the page header."

**Tip:** Cursor'ni favicon'ga ko'rsat, keyin header'dagi logo'ga ko'rsat.

---

### Kadr 2: Privacy Policy ko'rsatish (0:08 – 0:16, 8 sek)

**Ekran:** Header'dagi "Privacy" link bosiladi. `privacy.html` ochiladi.

**Diqqat markazi:**
- **Header'da yana logo** (yangi sahifa, lekin xuddi shu icon)
- **Browser tab favicon'da yana logo** (ramka qilib ko'rsat)
- Scroll qilib "TikTok-Specific Data Use" bo'limini ko'rsat

**Voice-over (en):**
> "Our Privacy Policy clearly documents how we use TikTok's video.publish scope — and the app icon is consistently displayed in the page header and browser tab."

---

### Kadr 3: Telegram bot — listing yuborish (0:16 – 0:30, 14 sek)

**Ekran:** Telegram Desktop ochilib `@Saxiy_makler` bot bilan suhbat oynasi.

**Action ketma-ketligi:**
1. `/start` yuborish (yoki "Yangi e'lon" tugmasini bosish)
2. Listing matnini yopishtir:
   ```
   3-xonali kvartira, Yunusobod tumani
   Maydon: 85 m²
   Narx: $95,000
   Yangi binoda, 2-qavat
   ```
3. 3-4 ta kvartira fotosurati yuborish (faqat mockup uchun internetdan tasodifiy bo'lsa ham bo'ladi)
4. Bot javob beradi: "✅ Qabul qilindi. Tarjima va video tayyorlanmoqda..."

**Voice-over (en):**
> "A real estate agent submits a property listing — text and photos — to our Telegram bot. The bot accepts only whitelisted users."

---

### Kadr 4: Video tayyorlanish (0:30 – 0:42, 12 sek)

**Ekran:** Bot suhbatida progress xabarlari ko'rinadi:
- "🌐 Translating to Uzbek..."
- "🎙️ Generating voiceover..."
- "📱 Rendering video (1080×1920)..."

Keyin **video preview** keladi (bot generated video).

**Voice-over (en):**
> "The bot translates the listing into Uzbek, generates AI voiceover with ElevenLabs, and renders a vertical short-form video using FFmpeg. The user then previews the result before publishing."

---

### Kadr 5: TikTok auth (0:42 – 0:55, 13 sek) — **ENG MUHIM**

**Ekran:** Bot'da "Publish to TikTok" tugmasi bosiladi.

**Variant A — Sandbox auth (afzal):**
1. Brauzer ochiladi, TikTok login sahifasi
2. Sandbox account bilan login
3. Permission dialog: "Saxiy Makler wants access to: video.publish"
4. "Allow" tugmasini bos
5. Brauzer yopiladi, bot'ga "✅ Authorized" keladi

**Variant B — Mockup (sandbox account yo'q bo'lsa):**
1. Bot suhbatida static screenshot/animation: "TikTok permission requested"
2. Screenshot — TikTok OAuth dialog (test environment)
3. "✅ User authorized the video.publish scope"

**Voice-over (en):**
> "The user authorizes our app via TikTok's standard OAuth flow, granting only the video.publish scope — no read access to profile, comments, or analytics."

---

### Kadr 6: Upload va publish (0:55 – 1:08, 13 sek)

**Ekran:** Bot suhbatida:
- "📤 Uploading to TikTok... 23%"
- "📤 Uploading to TikTok... 67%"
- "📤 Uploading to TikTok... 100%"
- "✅ Published. publish_id: v12345abc..."

**Diqqat markazi:** Real API chaqiruvi (network tab'da `open.tiktokapis.com/v2/post/publish/video/init/` ko'rinsa zo'r) yoki bot logini DevTools'da ko'rsat.

**Voice-over (en):**
> "The video is uploaded to TikTok's Content Posting API endpoint and published as PUBLIC_TO_EVERYONE. Saxiy Makler receives the publish_id confirming success."

---

### Kadr 7: TikTok'da natija (1:08 – 1:20, 12 sek)

**Ekran:** Brauzerda TikTok mobile view yoki TikTok app — sandbox account profili. Yangi video ko'rinadi.

**Diqqat markazi:**
- Video thumbnail
- "Saxiy Makler" caption va watermark
- Real publish vaqti

**Voice-over (en):**
> "Here you can see the published video on TikTok — fully end-to-end, from listing submission to the live video, all within one minute."

---

### Kadr 8: Yakuniy ekran (1:20 – 1:25, 5 sek)

**Ekran:** Website'ning bosh sahifasi (qaytib keladi). Logo, brand nomi, "Made for the Uzbekistan real estate market".

**Voice-over (en):**
> "Saxiy Makler — built for Uzbekistan real estate agents who want professional video output in under a minute."

---

## Voice-over to'liq matni (copy-paste)

> This is Saxiy Makler — a real estate video publisher for the Uzbekistan market. You can see the official website with our app icon in the browser tab and in the page header.
>
> Our Privacy Policy clearly documents how we use TikTok's video.publish scope — and the app icon is consistently displayed in the page header and browser tab.
>
> A real estate agent submits a property listing — text and photos — to our Telegram bot. The bot accepts only whitelisted users.
>
> The bot translates the listing into Uzbek, generates AI voiceover with ElevenLabs, and renders a vertical short-form video using FFmpeg. The user then previews the result before publishing.
>
> The user authorizes our app via TikTok's standard OAuth flow, granting only the video.publish scope — no read access to profile, comments, or analytics.
>
> The video is uploaded to TikTok's Content Posting API endpoint and published as PUBLIC_TO_EVERYONE. Saxiy Makler receives the publish_id confirming success.
>
> Here you can see the published video on TikTok — fully end-to-end, from listing submission to the live video, all within one minute.
>
> Saxiy Makler — built for Uzbekistan real estate agents who want professional video output in under a minute.

**Davomiyligi:** ~75 sekund (180 word @ 150 wpm)

---

## Tayyorlash qadamlari

### 1. Tayyorgarlik (15 daq)

- [ ] Website yangilangan va GitHub Pages'da deploy bo'lgan (favicon + header logo ko'rinmoqda)
- [ ] Brauzer cache tozalangan — `Ctrl+Shift+R` (favicon eski versiyasini ko'rsatmasin)
- [ ] Telegram Desktop ochilgan, `@Saxiy_makler` bot bilan toza suhbat
- [ ] OBS Studio yoki Win+G screen recorder tayyor
- [ ] Mikrofon test qilingan (yoki voice-over keyin alohida yoziladi)
- [ ] Sandbox TikTok account login ma'lumotlari tayyor (Variant A)
- [ ] Mockup screenshotlar tayyor (Variant B)

### 2. Yozish (30-45 daq)

- [ ] Birinchi yozuv (1 dublyaj)
- [ ] Agar 90 sek dan oshsa — kesib qisqartir
- [ ] Voice-over: live yozish yoki post-production'da qo'shish
- [ ] Subtitle (en) qo'shish — TikTok review favoritlardan biri

### 3. Post-production (15 daq)

- [ ] DaVinci Resolve, CapCut yoki Premiere'da kesish
- [ ] Voice-over qo'shish (agar live qilmagan bo'lsangiz)
- [ ] Eng birinchi 10 sekundda website + favicon ko'rinishi — **majburiy** (reviewer talabi)
- [ ] Last frame: "Saxiy Makler — saxiy-makler-legal.github.io" yoki shunga o'xshash text
- [ ] Export: MP4, 1080p, H.264

### 4. Upload (5 daq)

- [ ] TikTok Developer Portal → My Apps → Saxiy Makler → Submit Materials
- [ ] Demo Video field'ga MP4 yuklash
- [ ] "Notes for reviewer" maydonida:
  ```
  Scopes mismatch resolved: removed the unused user.info.basic (Login Kit)
  and video.upload scopes. The app now requests only video.publish and uses
  the Content Posting API Direct Post endpoint. The demo video is recorded in
  the TikTok sandbox and shows the complete end-to-end flow for video.publish
  only (no flowchart). Privacy Policy and website scope lists were updated to
  match — they now reference video.publish exclusively.
  ```
- [ ] Resubmit

---

## Reviewer checkmark — bizning demo bularni qondiradimi?

| Reviewer talabi | Demo'da javob |
|---|---|
| Favicon ko'rinishi | ✅ Kadr 1, 2 — browser tab focus |
| Header app icon | ✅ Kadr 1, 2 — header logo focus |
| End-to-end TikTok flow | ✅ Kadr 3-7 — listing → auth → upload → published |
| Flowchart EMAS, real UX | ✅ Hech qaerda flowchart yo'q — faqat real ekran |
| Website demo'da ko'rinadi | ✅ Kadr 1, 2, 8 — uchchala bo'limda ko'rsatildi |
| Sandbox yoki mockup | ✅ Variant A (sandbox) yoki Variant B (mockup) tanlanadi |
| Website'da ko'rsatilgan = TikTok'ga submit qilingan | ✅ Demo da `https://amir4874.github.io/saxiy-makler-legal/` ko'rsatiladi — bu TikTok'ga submit qilinadigan aniq URL |

---

## Variant tanlash

**⚠️ 2026-06 rad izohi:** Reviewer bu safar aniq yozdi: *"You are required to use **sandbox** to demonstrate the integration."* Demak mockup endi yetarli emas — **Variant A (sandbox) majburiy**.

- **Variant A — sandbox (MAJBURIY):** TikTok Portal'da Sandbox muhitini yoqib, test account bilan real OAuth (`video.publish`) → publish flow yoziladi. Eng ishonchli reviewer signal.
- **Variant B — mockup (faqat zaxira):** sandbox sozlash imkoni bo'lmasa. Lekin joriy raundda reviewer aniq sandbox so'ragani uchun yana rad bo'lish xavfi bor.

Sandbox sozlash ~1-2 soat. Bu raundda uni o'tkazib bo'lmaydi.
