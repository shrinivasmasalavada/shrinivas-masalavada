<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eco Spice | Future of Cooking</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Poppins', sans-serif; }
        .hero-bg {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                        url('https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&q=80&w=2070');
            background-size: cover;
            background-position: center;
            height: 100vh;
        }
        .spice-float { animation: float 6s ease-in-out infinite; }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
    </style>
</head>
<body class="bg-stone-50 text-stone-900">

    <nav class="fixed w-full z-50 flex justify-between items-center px-10 py-6 text-white bg-transparent">
        <h1 class="text-3xl font-bold tracking-tighter">ECO <span class="text-green-400">SPICE</span></h1>
        <div class="space-x-8 font-medium">
            <a href="#" class="hover:text-green-400 transition">ನಮ್ಮ ಬಗ್ಗೆ</a>
            <a href="#" class="hover:text-green-400 transition">ಉತ್ಪನ್ನಗಳು</a>
            <a href="#" class="bg-green-600 px-6 py-2 rounded-full hover:bg-green-700 transition">ಈಗಲೇ ಖರೀದಿಸಿ</a>
        </div>
    </nav>

    <header class="hero-bg flex items-center justify-center text-center">
        <div class="max-w-4xl px-4">
            <h2 class="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight spice-float">
                ಪ್ಲಾಸ್ಟಿಕ್ ಮುಕ್ತ ಅಡುಗೆಗೆ <br> ನೈಸರ್ಗಿಕ ಸ್ಪರ್ಶ
            </h2>
            <p class="text-xl text-stone-200 mb-10">ಅಕ್ಕಿ ಹಾಳೆ ಮತ್ತು ನೈಸರ್ಗಿಕ ನಾರಿನಿಂದ ಮಾಡಿದ ಭಾರತದ ಮೊದಲ "Drop & Cook" ಮಸಾಲೆ ಕ್ಯಾಪ್ಸುಲ್‌ಗಳು.</p>
            <button class="bg-white text-green-800 px-10 py-4 rounded-full font-bold text-lg hover:shadow-2xl transition-all duration-300">
                ಕಿಟ್ ಎಕ್ಸ್‌ಪ್ಲೋರ್ ಮಾಡಿ
            </button>
        </div>
    </header>

    <section class="py-24 px-10">
        <h3 class="text-4xl font-bold text-center mb-16 italic">"ಒಂದೇ ಒಂದು ಕ್ಯಾಪ್ಸುಲ್, ಪರಿಪೂರ್ಣ ರುಚಿ"</h3>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div class="bg-white p-6 rounded-3xl shadow-lg border border-stone-200 hover:-translate-y-2 transition-all">
                <img src="YOUR_TURMERIC_POD_IMAGE_URL" alt="Turmeric Pod" class="rounded-2xl mb-6 w-full h-64 object-cover">
                <h4 class="text-2xl font-bold mb-2">Heritage ಅರಿಶಿಣ</h4>
                <p class="text-stone-600">100% ಎಡಿಬಲ್ ರೈಸ್ ಪೇಪರ್ ಕವರ್.</p>
            </div>

            <div class="bg-white p-6 rounded-3xl shadow-lg border border-stone-200 hover:-translate-y-2 transition-all">
                <img src="YOUR_CHILLI_POD_IMAGE_URL" alt="Chilli Pod" class="rounded-2xl mb-6 w-full h-64 object-cover">
                <h4 class="text-2xl font-bold mb-2">Fire ಕೆಂಪು ಮೆಣಸು</h4>
                <p class="text-stone-600">ಪ್ರೀಮಿಯಂ ಗುಂಟೂರು ಮೆಣಸಿನ ಪುಡಿ.</p>
            </div>

            <div class="bg-white p-6 rounded-3xl shadow-lg border border-stone-200 hover:-translate-y-2 transition-all">
                <img src="YOUR_COMBO_KIT_IMAGE_URL" alt="Combo Kit" class="rounded-2xl mb-6 w-full h-64 object-cover">
                <h4 class="text-2xl font-bold mb-2">Premium Combo Kit</h4>
                <p class="text-stone-600">40 ಮ್ಯಾಜಿಕ್ ಕ್ಯಾಪ್ಸುಲ್‌ಗಳ ಸಂಕಲನ.</p>
            </div>
        </div>
    </section>

    <footer class="bg-stone-900 text-white py-20 text-center">
        <p class="text-stone-400 mb-4">© 2026 Eco Spice Start-up. All Rights Reserved.</p>
        <div class="flex justify-center space-x-6">
            <span>Instagram</span>
            <span>LinkedIn</span>
            <span>WhatsApp</span>
        </div>
    </footer>

</body>
</html>
