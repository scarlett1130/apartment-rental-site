<script setup lang="ts">
import 'leaflet/dist/leaflet.css'
import L from 'leaflet';

const props = defineProps<{
    mapHeight?: string;
}>()

const mapContainer = ref<HTMLElement | null>(null);


watch(mapContainer, (container) => {
    if (container) {
        const map = L.map(container).setView([51.505, -0.09], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
        L.marker([51.5, -0.09]).addTo(map)
            .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
            .openPopup();
    }
});
</script>

<template>
    <div ref="mapContainer" id="map" class="map"></div>
</template>

<style scoped>
    .map {
        height: calc(100vh - 80px);
    }
</style>
