from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Ta'lim Neon")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ta'lim Neon Dashboard</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
            body { background: #0b0f19; color: #f3f4f6; min-height: 100vh; display: flex; flex-direction: column; }
            
            /* Header */
            header { background: #111827; border-bottom: 1px solid #1f2937; padding: 16px 24px; display: flex; justify-content: space-between; align-items: center; }
            .logo { font-size: 20px; font-weight: 700; color: #38bdf8; display: flex; align-items: center; gap: 8px; }
            .badge { background: #1e293b; color: #94a3b8; padding: 4px 10px; border-radius: 9999px; font-size: 12px; border: 1px solid #334155; }
            
            /* Container */
            .container { flex: 1; padding: 24px; max-width: 1000px; margin: 0 auto; width: 100%; }
            .role-title { font-size: 24px; font-weight: 700; margin-bottom: 8px; color: #fff; }
            .role-subtitle { color: #9ca3af; font-size: 14px; margin-bottom: 24px; }
            
            /* Grid Cards */
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 28px; }
            .card { background: #1f2937; border: 1px solid #374151; border-radius: 12px; padding: 20px; }
            .card h3 { font-size: 13px; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }
            .card .value { font-size: 24px; font-weight: 700; color: #38bdf8; }
            
            /* Table/Details section */
            .content-box { background: #1f2937; border: 1px solid #374151; border-radius: 12px; padding: 20px; }
            .content-box h2 { font-size: 16px; margin-bottom: 16px; color: #e5e7eb; }
            .item-list { list-style: none; }
            .item-list li { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #374151; font-size: 14px; }
            .item-list li:last-child { border-bottom: none; }
            .status-tag { padding: 3px 8px; border-radius: 6px; font-size: 12px; font-weight: 600; background: #064e3b; color: #34d399; }
            
            /* Pastdagi Test Rejimi (Floating Bar) */
            .floating-bar {
                position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);
                background: rgba(31, 41, 55, 0.95); backdrop-filter: blur(10px);
                border: 1px solid #4b5563; border-radius: 50px; padding: 6px 10px;
                display: flex; gap: 8px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5); z-index: 9999;
            }
            .bar-label { display: flex; align-items: center; font-size: 12px; color: #9ca3af; padding-left: 10px; padding-right: 4px; font-weight: 600; }
            .role-btn {
                background: transparent; border: none; color: #d1d5db; padding: 8px 16px;
                border-radius: 9999px; font-size: 13px; font-weight: 600; cursor: pointer; transition: 0.2s;
            }
            .role-btn.active { background: #38bdf8; color: #0b0f19; font-weight: 700; box-shadow: 0 0 12px rgba(56, 189, 248, 0.4); }
        </style>
    </head>
    <body>
        <header>
            <div class="logo">⚡ Ta'lim.Neon</div>
            <div class="badge" id="current-badge">Admin Paneli</div>
        </header>
        
        <div class="container" id="main-content">
            <!-- JavaScript orqali to'ldiriladi -->
        </div>

        <!-- PASTDAGI TEST REJIMI TUGMALARI -->
        <div class="floating-bar">
            <span class="bar-label">TEST REJIMI:</span>
            <button class="role-btn active" onclick="switchRole('admin')">Admin</button>
            <button class="role-btn" onclick="switchRole('teacher')">O'qituvchi</button>
            <button class="role-btn" onclick="switchRole('student')">O'quvchi</button>
        </div>

        <script>
            const data = {
                admin: {
                    badge: "Boshqaruv (Admin)",
                    title: "O'quv Markazi Umumiy Holati",
                    subtitle: "Barcha filiallar, to'lovlar va faollik ko'rsatkichlari",
                    cards: [
                        { label: "Jami O'quvchilar", value: "142 ta" },
                        { label: "Faol Guruhlar", value: "12 ta" },
                        { label: "Oylik Tushum", value: "18.5 mln UZS" },
                        { label: "Qarzdorlik", value: "8 kishi" }
                    ],
                    tableTitle: "So'nggi Yangi Guruhlar",
                    items: [
                        { name: "IELTS Intensive (Ertalabki)", status: "To'lgan" },
                        { name: "Ingliz tili B1 (Kechki)", status: "Qabul ochiq" },
                        { name: "Frontend Dasturlash", status: "Dars boshlangan" }
                    ]
                },
                teacher: {
                    badge: "O'qituvchi Kabineti",
                    title: "Salom, Olim Ustoz",
                    subtitle: "Bugungi dars jadvali va guruhlar davomati",
                    cards: [
                        { label: "Mening Guruhlarim", value: "4 ta" },
                        { label: "Bugungi Darslar", value: "3 ta" },
                        { label: "O'rtacha Davomat", value: "94%" },
                        { label: "Tekshirilmagan Vazifalar", value: "5 ta" }
                    ],
                    tableTitle: "Bugungi Dars Rejasi",
                    items: [
                        { name: "IELTS Speaking Mock (14:00 - 15:30)", status: "Navbatdagi" },
                        { name: "Grammar Intensive (16:00 - 17:30)", status: "Rejalashtirilgan" },
                        { name: "B2 Vocabulary Test (18:00 - 19:30)", status: "Rejalashtirilgan" }
                    ]
                },
                student: {
                    badge: "O'quvchi Profili",
                    title: "Salom, Akmaljon",
                    subtitle: "Shaxsiy o'quv ko'rsatkichlaringiz va jadvalingiz",
                    cards: [
                        { label: "Guruh", value: "IELTS 7+" },
                        { label: "O'zlashtirish", value: "8.5 / 10" },
                        { label: "To'lov Holati", value: "To'langan" },
                        { label: "Uyga Vazifa", value: "Yuborilgan" }
                    ],
                    tableTitle: "Yaqinlashayotgan Darslar",
                    items: [
                        { name: "Reading Strategy & Test Practice", status: "Ertaga 14:00" },
                        { name: "Mock Exam (Writing Task 2)", status: "Shanba 10:00" }
                    ]
                }
            };

            function switchRole(role) {
                // Tugmalarni faollashtirish
                document.querySelectorAll('.role-btn').forEach(btn => {
                    btn.classList.remove('active');
                    if (btn.innerText.toLowerCase().includes(role === 'teacher' ? 'o\'qituvchi' : role)) {
                        btn.classList.add('active');
                    }
                });

                const r = data[role];
                document.getElementById('current-badge').innerText = r.badge;

                let cardsHtml = r.cards.map(c => `
                    <div class="card">
                        <h3>${c.label}</h3>
                        <div class="value">${c.value}</div>
                    </div>
                `).join('');

                let itemsHtml = r.items.map(i => `
                    <li>
                        <span>${i.name}</span>
                        <span class="status-tag">${i.status}</span>
                    </li>
                `).join('');

                document.getElementById('main-content').innerHTML = `
                    <h1 class="role-title">${r.title}</h1>
                    <p class="role-subtitle">${r.subtitle}</p>
                    <div class="grid">${cardsHtml}</div>
                    <div class="content-box">
                        <h2>${r.tableTitle}</h2>
                        <ul class="item-list">${itemsHtml}</ul>
                    </div>
                `;
            }

            // Dastlabki admin ko'rinishini yuklash
            switchRole('admin');
        </script>
    </body>
    </html>
    """
