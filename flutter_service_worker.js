'use strict';
const CACHE_NAME = 'flutter-app-cache';
const RESOURCES = {
    "/trips/index.html": "ebdf9c1145644f18f149e9edac0972b5",
    "/trips/main.dart.js": "d6f2fafcbbc70b48244716742c9a6ca9",
    "/trips/manifest.json": "f39cf2390219532f935faf79ad92706f",
    "/trips/assets/fonts/MaterialIcons-Regular.ttf": "56d3ffdef7a25659eab6a68a3fbfaf16"
};

self.addEventListener('activate', function (event) {
    event.waitUntil(
        caches.keys().then(function (cacheName) {
            return caches.delete(cacheName);
        }).then(function (_) {
            return caches.open(CACHE_NAME);
        }).then(function (cache) {
            return cache.addAll(Object.keys(RESOURCES));
        })
    );
});

self.addEventListener('fetch', function (event) {
    event.respondWith(
        caches.match(event.request)
            .then(function (response) {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            })
    );
});