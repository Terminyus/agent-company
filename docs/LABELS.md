# 🏷️ Label Standardı

GitHub label'ları issue'ları organize etmek, backlog'u manage etmek ve triage'ı hızlandırmak için kullanılır.

---

## Priority Labels (Jadwal)

Tüm issue'lar bir priority label'ı almalıdır.

### 🔴 `blocker`
- **Açıklama**: MVP'yi durduran kritik sorular
- **Kullanım**: Sistem down, kullanılamaz, no workaround
- **Action**: Hemen fix edilmelidir
- **SLA**: 24 saat içinde çalışılmalı

### 🟠 `high`
- **Açıklama**: Önemli ama blocking değil
- **Kullanım**: Kritik feature broken, iş yapılmıyor ama partial çözüm var
- **Action**: Sonraki sprint'e alınmalı
- **SLA**: 1 hafta

### 🟡 `medium`
- **Açıklama**: Standart issue'lar
- **Kullanım**: Normal feature request, minor bug
- **Action**: Backlog'a gidiyor
- **SLA**: 2-3 hafta

### 🟢 `low`
- **Açıklama**: Nice-to-have, cosmetic
- **Kullanım**: Typo, UI tweak, minor improvement
- **Action**: Backlog, veya hiç olmaz
- **SLA**: Belirsiz

---

## Type Labels (Tür)

Issue'nun ne olduğunu belirtir.

### 🐛 `bug`
- **Açıklama**: Hata raporu
- **Otomatik**: bug_report.yml açıldığında auto-assigned
- **Format**: "🐛 [BUG] Kısaca ne hata"

### ✨ `enhancement`
- **Açıklama**: Yeni feature veya improvement
- **Otomatik**: feature_request.yml açıldığında auto-assigned
- **Format**: "✨ [FEATURE] Kısaca ne isteniyor"

### 📚 `docs`
- **Açıklama**: Dokümanter, README, API docs
- **Otomatik**: El ile assign edilir
- **Format**: "[DOCS] Kısaca ne dokümante edilecek"

---

## Team/Area Labels (Takım)

Kimin sorumlu olduğunu gösterir.

### 💻 `pm`
- **Açıklama**: PM backlog issue'ları
- **Otomatik**: Başlık "PM Backlog:" içeriyorsa auto-assigned
- **Sorumlu**: Project Manager
- **Alt-label**: Genelde `enhancement` ve priority label'ı beraberdir

### 🎨 `frontend`
- **Açıklama**: UI/UX, React, CSS, etc.
- **Sorumlu**: Frontend Developer
- **Format**: "[FRONTEND] ..."

### ⚙️ `backend`
- **Açıklama**: API, Database, business logic
- **Sorumlu**: Backend Developer
- **Format**: "[BACKEND] ..."

### 🧪 `qa`
- **Açıklama**: QA/Testing, test plan, test case
- **Sorumlu**: QA Engineer
- **Format**: "[QA] ..."

---

## Severity Labels (Ciddilik - Bug için)

Sadece bug'lar için ek severity label'ı. Priority ile beraber çalışır.

| Label | Priority | Açıklama | Örnek |
|-------|----------|----------|-------|
| `severity/critical` | blocker | APP CRASH, veri kaybı | POST request fail, kullanıcı login yapamıyor |
| `severity/high` | high | Kullanıcı flow broken | Button click'lenmiyor, form submit fail |
| `severity/medium` | medium | Feature partially broken | Pagination broken, ama data gösteriyor |
| `severity/low` | low | Cosmetic bug | Yazı rengi yanlış, button 1px sağda |

**Kuralı**: 
```
bug + blocker => severity/critical (Otomatik)
bug + high => severity/high (Otomatik)
bug + medium => severity/medium (Otomatik)
bug + low => severity/low (Otomatik)
```

---

## Status Labels (Durum)

Mevcut durum (opsiyonel, GitHub Projects kullanılırsa gereksiz).

### ✅ `ready`
- **Açıklama**: Specification ready, development hazır
- **Kullanım**: Backlog → Sprint'e taşındığında

### 🚧 `in-progress`
- **Açıklama**: Birisi üzerinde çalışıyor
- **Kullanım**: PR açıldığında, issue assigned + started

### ⏳ `blocked`
- **Açıklama**: Başka issue'ya bağımlı
- **Kullanım**: Dependencies var, beklenemde

### 👀 `needs-review`
- **Açıklama**: Code review bekliyor
- **Kullanım**: PR açıldığında

### ✔️ `approved`
- **Açıklama**: Review passed, merge ready
- **Kullanım**: PR approved state

### 🔄 `rework`
- **Açıklama**: Changes requested, rework gerekli
- **Kullanım**: Review feedback gelince

---

## Meta Labels (Komut)

Automation ve tooling için.

### 🤖 `automated`
- **Açıklama**: Bot tarafından oluşturuldu
- **Kullanım**: seed_ideas.py, labeler, vs.

### 📌 `pinned`
- **Açıklama**: Önemli, herkese göster
- **Kullanım**: Kritik announcement

### ❓ `question`
- **Açıklama**: Soru/clarification gerekli
- **Kullanım**: İç tartışmalar

---

## Label Kombinasyon Kuralı

### Genel
```
[Type] + [Priority] + [Team] = Complete issue
```

Örnek:
- 🐛 bug + 🔴 blocker + ⚙️ backend = "API crash, PM'in şimdi fix etmesi gerek"
- ✨ enhancement + 🟡 medium + 🎨 frontend = "Nice UI feature, backlog'a gidiyor"

### Template Otomasyonu
```
bug_report.yml açıldığında:
  - label: "bug"
  - label: "severity/X" (severity dropdown'a göre)
  - label: "needs-review"

feature_request.yml açıldığında:
  - label: "enhancement"
  - label: "ready" (spec complete olma sayılıyor)
```

---

## Labeling Best Practices

1. **Her issue başlıkta tip olsun**:
   - ✅ "[BUG] Login button çalışmıyor"
   - ❌ "Button doesn't work"

2. **Her bug'ın priority'si olsun**:
   - ✅ Bug + blocker/high/medium/low
   - ❌ Bug ama priority yok

3. **Team label'ı clear olsun**:
   - ✅ Issue'da "pm" varsa PM'ye assign et
   - ❌ Issue'da team label yok, kim yapacak bilinmiyor

4. **Blocker'lar 24 saat içinde triage yapılsın**:
   - ⏰ Daily standup'da blocker'ları kontrol et

---

## Label Yönetimi

GitHub Settings → Labels sayfasından:

1. Tüm label'ları yukarıdaki listeye göre oluştur
2. Tanım (description) alanına açıklamayı yapıştır
3. Color: Consistency için type labels farklı renk
   - Bug = Red 🔴
   - Enhancement = Green 🟢
   - PM = Purple 🟣

---

**Last Updated**: 2026-02-13
