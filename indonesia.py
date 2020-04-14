id_dictionaries = [
    [r'Aku ingin  (.*)',
     ["kenapa kamu ingin %?",
      "Lalu apa?",
      "Kamu yakin ingin %?"]],

    [r'Aku butuh (.*)',
     ["kenapa kamu butuh %?",
      "Lalu apa ?",
      "Apakah aku bisa membantu ?",
      "Kamu yakin butuh %?"]],

    [r'Kenapa (kamu|lo|elo|lu) ([^\?]*)\??',
     ["Kamu yakin aku %?",
      "Kamu ingin aku untuk %?"]],

    [r'Kenapa (aku|gw|saya) ([^\?]*)\??',
        ["Kamu yakin, kamu %?",
         "Aku tidak tahu, kenapa kamu %?",
         "Kenapa kamu berpikir begitu ?"]],

    [r'Kenapa sih (aku|gw|saya) ([^\?]*)\??',
        ["Kamu yakin, kamu %?",
         "Aku tidak tahu, kenapa kamu %?",
         "Kenapa kamu berpikir begitu ?"]],

    [r'Aku (gabisa|ngga bisa|tidak bisa) (.*)',
        ["Darimana kamu bisa tahu, kamuu gabisa %?",
         "Mungkin kamu bisa % jika kamu berusaha.",
         "Yuk bisa yuk wkwkwk",
         "Kamu pasti %?"]],

    [r'Aku (.*)',
        ["Kamu ngobrol sama aku karena %?",
         "Sudah berapa lama kamu %?",
         "Apakah kamu menikmatinya ?",
         "Apakah menyenangkan ?",
         "Apakah menyedihkan ?",
         "Kenapa kamu berpikir seperti itu ?",
         "Apa yang kamu rasakan ketika kamu %?"]],

    [r'Apakah kamu ([^\?]*)\??',
        ["Gapapa kan kalo aku %?",
         "Apa kamu lebih suka jika aku tidak %?",
         "Kenapa kamu berpikir begitu ?",
         "Hmm... aku tidak yakin",
         "Sepertinya tidak"]],

    [r'(Apa|bagaimana) (kabar|kabarmu)?',
        ["Baik, kamu?",
         "Baik.",
         "Baik, tentu saja.",
         "Menurut kamu?"]],

    [r'(.*) maaf (.*)',
        ["Tak apa.",
         "Engga papa.",
         "Kenapa :( ?"]],

    [r'(Hello|Hai|Hi|Halo|Hallo)(.*)',
        ["Hai",
         "Hi?",
         "Halo, Apa kabarmu?"]],

    [r'(.*) (temen|teman|temenku|temanku) (.*)',
        ["Ceritain temanmu dong.",
         "Bisa kamu ceritakan?",
         "Kamu punya banyak teman ya?"]],

    [r'Iya',
        ["Hmm, iya.",
         "Sudah kuduga"]],

    [r'(Baik|Alhamdulillah)',
        ["Alhamdulillah",
         "Semoga tetap baik saja.",
         "Aku juga baik"]],

    [r'Bisakah kamu ([^\?]*)\??',
        ["Apa akmu berpikir saya tidak bisa %?",
         "Kalo aku bisa %, Lalu apa ?",
         "Entahlah."]],

    [r'Bisa (ngga|tidak|nga) (kamu|lo|elo|lu) ([^\?]*)\??',
        ["Apa akmu berpikir saya tidak bisa %?",
         "Kalo aku bisa %, Lalu apa ?",
         "Entahlah."]],

    [r'(aku|gw|saya) (pengen|ingin|kepengen) bisa ([^\?]*)\??',
        ["Kenapa kamu ingin bisa %.",
         "Aku yakin kamu pasti bisa %",
         "Yuk bisa yuk wkwkw...."]],

    [r'(kamu|lo|elo|lu) (.*)',
        ["Kenapa kamu berpikir aku %?",
         "Kenapa begitu ?",
         "Kenapa kamu berpikir seperti itu?",
         "Kamu yakin aku %?"]],

    [r'(aku|gw|saya) punya (.*)',
        ["Kenapa kamu memberitahuku kamu punya %?",
         "Setelah punya %, kamu akan melakukan apa?", ]
     ],

    [r'(aku|gw|saya) akan (.*)',
        ["Kenapa kamu harus %?",
         "Kenapa kamu %?",
         "Apakah aku harus % juga?"]],

    [r'(aku|gw|saya) (pengen|ingin|kepengen) (.*)',
        ["Kenapa kamu ingin %?",
         "Setelah %, apa yang kamu lakukan?",
         "Kenapa %?",
         "Apakah aku bisa membantu?"]],

    [r'(.*)\?',
        ["Kenapa kamu bertanya itu?",
         "Kenapa?",
         "Hmmm... Aku tidak yakin."
         ]],

    [r'Selamat malam (.*)',
        ["Malam.",
         "Selamat malam.",
         "Iya?"]],

    [r'Selamat pagi (.*)',
        ["pagi.",
         "Selamat pagi.",
         "Pagi yang cerah",
         "Iya?"]],

    [r'(developer|pengembang)',
        ["Bot ini diciptakan oleh https://github.com/raisoturu"]],
    [r'(tentang|about)',
        ["Eliza merupakan pertama yang dibuat pada tahun 1964 sampai 1966 oleh Professor Joseph Weizenbaum di MIT (Massachusetts Institute of Technology), dengan tujuan untuk mempelajari komunikasi natural language antara manusia dengan mesin.",
         "Baca lebih lanjut disini https://en.wikipedia.org/wiki/ELIZA",
         "Baca lebih lanjut disini https://github.com/raisoturu/eliza-line-chatbot"]],

    [r'(quit|keluar|exit)',
        ["Dadah.",
         "Good-bye.",
         "Terima kasih sudah mengobrol"]],
]
id_default_responses = [
    "Menarik.",
    "Aku tidak yakin",
    "Aku tidak mengerti",
    "Iya?",
    "Lalu?",
    "Hmm...",
]
