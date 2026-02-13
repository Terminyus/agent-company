from datetime import datetime

TEMPLATE = """\n\n## Günlük Taslak ({date})
Aşağıdaki 10 fikri doldur:

### IDEA-{n1}
- Problem:
- Persona:
- Kanıt:
- Rakipler:
- Farkımız:
- Gelir modeli:
- MVP kapsamı:
- Riskler:
- Türkiye Uygulanabilirlik Puanı (1-10):

### IDEA-{n2}
- Problem:
- Persona:
- Kanıt:
- Rakipler:
- Farkımız:
- Gelir modeli:
- MVP kapsamı:
- Riskler:
- Türkiye Uygulanabilirlik Puanı (1-10):

### IDEA-{n3}
- Problem:
- Persona:
- Kanıt:
- Rakipler:
- Farkımız:
- Gelir modeli:
- MVP kapsamı:
- Riskler:
- Türkiye Uygulanabilirlik Puanı (1-10):

### IDEA-{n4}
- Problem:
- Persona:
- Kanıt:
- Rakipler:
- Farkımız:
- Gelir modeli:
- MVP kapsamı:
- Riskler:
- Türkiye Uygulanabilirlik Puanı (1-10):

### IDEA-{n5}
- Problem:
- Persona:
- Kanıt:
- Rakipler:
- Farkımız:
- Gelir modeli:
- MVP kapsamı:
- Riskler:
- Türkiye Uygulanabilirlik Puanı (1-10):

### IDEA-{n6}
- Problem:
- Persona:
- Kanıt:
- Rakipler:
- Farkımız:
- Gelir modeli:
- MVP kapsamı:
- Riskler:
- Türkiye Uygulanabilirlik Puanı (1-10):

### IDEA-{n7}
- Problem:
- Persona:
- Kanıt:
- Rakipler:
- Farkımız:
- Gelir modeli:
- MVP kapsamı:
- Riskler:
- Türkiye Uygulanabilirlik Puanı (1-10):

### IDEA-{n8}
- Problem:
- Persona:
- Kanıt:
- Rakipler:
- Farkımız:
- Gelir modeli:
- MVP kapsamı:
- Riskler:
- Türkiye Uygulanabilirlik Puanı (1-10):

### IDEA-{n9}
- Problem:
- Persona:
- Kanıt:
- Rakipler:
- Farkımız:
- Gelir modeli:
- MVP kapsamı:
- Riskler:
- Türkiye Uygulanabilirlik Puanı (1-10):

### IDEA-{n10}
- Problem:
- Persona:
- Kanıt:
- Rakipler:
- Farkımız:
- Gelir modeli:
- MVP kapsamı:
- Riskler:
- Türkiye Uygulanabilirlik Puanı (1-10):
"""

def main():
    # Basit numaralama: her gün 1-10 blok açıyoruz
    date = datetime.utcnow().strftime("%Y-%m-%d")
    block = TEMPLATE.format(
        date=date,
        n1=1, n2=2, n3=3, n4=4, n5=5, n6=6, n7=7, n8=8, n9=9, n10=10
    )

    path = "docs/IDEAS.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Aynı gün ekleme yapma
    if f"## Günlük Taslak ({date})" in content:
        return

    with open(path, "a", encoding="utf-8") as f:
        f.write(block)

if __name__ == "__main__":
    main()
