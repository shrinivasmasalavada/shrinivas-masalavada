<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eco Spice | Multi-lingual Premium Brand</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .hero-section {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                        url('https://images.unsplash.com/photo-1506484334402-4d5b69385d57?auto=format&fit=crop&q=80&w=2070');
            background-size: cover;
            height: 90vh;
        }
        .lang-btn { @apply px-3 py-1 border border-white rounded hover:bg-white hover:text-black transition; }
    </style>
</head>
<body class="bg-[#fdfcf8]">

    <nav class="fixed w-full z-50 bg-black/30 backdrop-blur-md text-white px-8 py-4 flex justify-between items-center">
        <div class="text-2xl font-bold italic">ECO SPICE</div>
        <div class="flex items-center gap-4">
            <button class="lang-btn">ಕನ್ನಡ</button>
            <button class="lang-btn">English</button>
            <button class="lang-btn">हिन्दी</button>
            <a href="#" class="ml-6 bg-green-600 px-5 py-2 rounded-full font-bold shadow-lg">Shop Now</a>
        </div>
    </nav>

    <section class="hero-section flex items-center justify-center text-center text-white">
        <div class="max-w-5xl">
            <h1 class="text-6xl font-extrabold mb-6 drop-shadow-2xl">
                ರುಚಿಯ ಸಂಪ್ರದಾಯ, ಪ್ರಕೃತಿಯ ಸಂರಕ್ಷಣೆ
            </h1>
            <p class="text-2xl mb-8 opacity-90">Revolutionizing Kitchens with 100% Biodegradable Spice Pods.</p>
        </div>
    </section>

    <section class="py-20 px-10 bg-white">
        <div class="text-center mb-16">
            <h2 class="text-4xl font-bold text-stone-800 mb-4">ನಮ್ಮ ನೈಸರ್ಗಿಕ ಕವಚಗಳು (Our Sustainable Covers)</h2>
            <p class="text-stone-500">ಪ್ಲಾಸ್ಟಿಕ್ ಬದಲು ನಾವು ಬಳಸುವ ನೈಸರ್ಗಿಕ ಮೂಲಗಳು</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
            <div class="group overflow-hidden rounded-3xl relative">
                <img src="https://images.unsplash.com/photo-1622210332144-71cf007d05f6?auto=format&fit=crop&q=80" alt="Sugarcane Waste" class="w-full h-96 object-cover group-hover:scale-110 transition duration-500">
                <div class="absolute bottom-0 left-0 p-8 bg-gradient-to-t from-black text-white w-full">
                    <h3 class="text-2xl font-bold">ಶುಗರ್ ಕೇನ್ ವೇಸ್ಟ್ (Sugarcane Bagasse)</h3>
                    <p>ಕಬ್ಬಿನ ಸಿಪ್ಪೆಯಿಂದ ತಯಾರಿಸಿದ ಪರಿಸರ ಸ್ನೇಹಿ ಬಾಕ್ಸ್‌ಗಳು.</p>
                </div>
            </div>

            <div class="group overflow-hidden rounded-3xl relative">
                <img src="https://images.unsplash.com/photo-1599940859674-a7fef05b94ae?auto=format&fit=crop&q=80" alt="Spice Pods" class="w-full h-96 object-cover group-hover:scale-110 transition duration-500">
                <div class="absolute bottom-0 left-0 p-8 bg-gradient-to-t from-black text-white w-full">
                    <h3 class="text-2xl font-bold">ಅಕ್ಕಿ ಹಾಳೆ (Edible Rice Film)</h3>
                    <p>ನೀರಿನಲ್ಲಿ ಕರಗುವ, ವಿಷಕಾರಿ ಅಂಶವಿಲ್ಲದ ಮ್ಯಾಜಿಕ್ ಕ್ಯಾಪ್ಸುಲ್‌ಗಳು.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="py-16 bg-[#f7f4ed]">
        <div class="text-center mb-12">
            <h2 class="text-3xl font-bold">ನಮ್ಮ ಕಿಟ್‌ನಲ್ಲಿರುವ ಮಸಾಲೆಗಳು (Our Spice Range)</h2>
        </div>
        <div class="flex overflow-x-auto gap-8 px-10 pb-10">
            <div class="min-w-[300px] bg-white rounded-2xl p-4 shadow-md">
                <div class="h-48 bg-yellow-100 rounded-xl mb-4 flex items-center justify-center text-4xl">🌕</div>
                <h4 class="font-bold">ಅರಿಶಿಣ (Turmeric)</h4>
                <p class="text-sm text-gray-500">5 Pods per kit</p>
            </div>
            <div class="min-w-[300px] bg-white rounded-2xl p-4 shadow-md">
                <div class="h-48 bg-red-100 rounded-xl mb-4 flex items-center justify-center text-4xl">🌶️</div>
                <h4 class="font-bold">ಖಾರ (Chili)</h4>
                <p class="text-sm text-gray-500">10 Pods per kit</p>
            </div>
            <div class="min-w-[300px] bg-white rounded-2xl p-4 shadow-md">
                <div class="h-48 bg-orange-100 rounded-xl mb-4 flex items-center justify-center text-4xl">🥘</div>
                <h4 class="font-bold">ಸಾಂಬಾರ್ ಪುಡಿ</h4>
                <p class="text-sm text-gray-500">10 Pods per kit</p>
            </div>
        </div>
    </section>

    <footer class="bg-stone-900 text-white py-12 px-10">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-10 border-b border-stone-700 pb-10">
            <div>
                <h4 class="text-xl font-bold mb-4">ಕನ್ನಡ</h4>
                <p class="text-stone-400">ಪ್ಲಾಸ್ಟಿಕ್ ಮುಕ್ತ ಭಾರತದತ್ತ ನಮ್ಮ ಪುಟ್ಟ ಹೆಜ್ಜೆ.</p>
            </div>
            <div>
                <h4 class="text-xl font-bold mb-4">English</h4>
                <p class="text-stone-400">Small steps for a plastic-free sustainable future.</p>
            </div>
            <div>
                <h4 class="text-xl font-bold mb-4">हिन्दी</h4>
                <p class="text-stone-400">प्लास्टिक मुक्त भारत की ओर हमारा एक छोटा कदम।</p>
            </div>
        </div>
        <p class="text-center mt-8 text-stone-500">© 2026 Eco Spice Startup | Made with Love for Mother Earth</p>
    </footer>

</body>
</html>