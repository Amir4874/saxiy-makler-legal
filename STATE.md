# STATE — poster-tiktok-legal (Saxiy Makler TikTok app review)

## Joriy faza
⏸ PAUSED — 2026-06-14 — TikTok "Scopes mismatch" rad tuzatish: legal + demo skript tayyor, demo VIDEO yozish bosqichida

## Pauza konteksti

- **Qayerda to'xtadik:** Demo video qanday yozilishini hal qilishda. Foydalanuvchi botning ishini aniqlashtirdi (quyida), men demo'ni shu arxitekturaga moslab qayta tushuntirdim. Helper skript yozish taklif qildim — **javob kutilmoqda**.
- **Sabab:** Foydalanuvchi `/pause` berdi.

### Kontekst — TikTok rad va yondashuv
- TikTok "Saxiy Makler" app **"Not approved → Scopes mismatch"**. Reviewer izohi aslida **demo video** haqida: *"all scopes must be demonstrated in the video... required to use sandbox."*
- **KRITIK kashfiyot:** 3 scope ham MAJBURIY, olib bo'lmaydi. Zanjir: `Content Posting API → Login Kit'ni talab qiladi → Login Kit user.info.basic'ni majburiy o'z ichiga oladi`. (Login Kit'ni o'chirishga urinish → "Cannot delete Login Kit". video.upload'da minus yo'q.)
- Shuning uchun yo'l: **olib tashlash EMAS → hammasini demo'da namoyish + legal'da halol tushuntirish** (`user.info.basic` faqat `open_id` uchun).

### Botning HAQIQIY ishi (foydalanuvchi aniqlashtirdi — kod bilan tasdiqlandi)
- Operator Telegram'ga e'lon (matn+rasm) yuboradi → bot tarjima+ovoz+video (FFmpeg) → "Publish" → **statik `TIKTOK_ACCESS_TOKEN`** bilan TikTok'ga post.
- **Bot'da user login / OAuth YO'Q.** Bitta operator akkaunti, oldindan olingan token (`publisher.py:454` Bearer static; refresh ham yo'q).
- Demak demo'da "user OAuth" ko'rsatish = bot featuresi emas. Lekin token bir martalik **operator akkaunt ulashidan** kelgan — o'sha consent'ni sandbox'da ko'rsatish kerak (TikTok majburiy qiladi).

### Demo reja (kelishilgan yo'nalish, hali yozilmagan)
- **Qism 1 (~10 sek):** sandbox authorize URL → consent 3 scope → Allow (Login Kit + scopes namoyishi)
- **Qism 2 (asosiy):** website → Telegram bot → e'lon → video → Publish → sandbox akkauntda chiqdi (post→video→publish)

## Bajarilgan (commit + push)
- `privacy.html`, `index.html` — 3 scope + `open_id`-only framing (commit `edde8f6`, push qilingan, live deploy tasdiqlangan)
- `demo-video-script.md` — Kadr 5 consent 3 scope, voice-over, Notes for reviewer; sandbox MAJBURIY
- Avvalgi noto'g'ri commit `4bdcb6c` ("video.publish only") → `edde8f6` bilan tuzatildi
- App review matni (~900 belgi, 3 scope justify) — **foydalanuvchi portalda almashtirgan** ✅
- Memory: `feedback_tiktok_app_review.md` > **Naqsh 7** qo'shildi (majburiy zanjir + demonstrate yo'li)
- Bot kodiga TEGILMADI (to'g'ri — Direct Post `video.publish`)

## Tekshirilmagan / kutilayotgan (davom bo'lganda)
- [ ] **QAROR:** `tiktok_sandbox_demo.py` helper skriptini yozaymi? (authorize URL → code→sandbox token → sandbox Direct Post → publish_id). Yoki avval portal sandbox sozlab authorize URL beraymi?
- [ ] Portal: Sandbox tab → "Target users" → o'z TikTok akkauntini qo'shish
- [ ] Authorize URL (client_key portaldan): `https://www.tiktok.com/v2/auth/authorize/?client_key=...&scope=user.info.basic,video.publish,video.upload&response_type=code&redirect_uri=https://amir4874.github.io/saxiy-makler-legal/oauth-callback.html&state=demo`
- [ ] Demo videoni yozish (2 qism), eski `2026-04-04...mp4` o'rniga yuklash
- [ ] **Submit for review** — FAQAT yangi sandbox demo tayyor bo'lgach (eski video bilan submit = yana rad)

## Eslatma
- Bu repo GitHub Pages legal sayt (`Amir4874/saxiy-makler-legal`, `main`). Push = live sayt.
- Plan fayli: `C:\Users\AMIR\.claude\plans\deep-snacking-orbit.md` (v2 — namoyish yo'li)
