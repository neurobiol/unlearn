const CACHE = 'unlearn-cache-v1';
const CORE = [
  './index.html',
  './styles.css',
  './manifest.webmanifest',
  './assets/icon.svg',
  './poster_overview.html',
  './poster_guide.html',
  './core_question.html',
  './methods_summary.html',
  './two_timescale_model.html',
  './parkinsons_wearables.html',
  './discussion_future_work.html',
  './glossary.html',
  './references.html',
  './further_reading.html'
];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(CORE)));
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(keys.map(k => k === CACHE ? null : caches.delete(k))))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cached => {
      return cached || fetch(event.request).then(resp => {
        const copy = resp.clone();
        caches.open(CACHE).then(cache => cache.put(event.request, copy));
        return resp;
      }).catch(() => cached);
    })
  );
});
