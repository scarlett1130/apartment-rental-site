<script setup lang="ts">
import { Apartment } from '~~/composables/types';

defineProps<{ apartment: Apartment }>()
</script>

<template>
    <div class="flex flex-col items-center mb-10">
        <NuxtLink :to="`/apartment/${apartment.id}`">
            <img :src="apartment.apartment_image ? apartment.apartment_image[0].image : `https://picsum.photos/200/300`"
                alt="Apartment" class="md:h-[15rem] h-[10rem] object-cover object-center">
        </NuxtLink>
        <div class="pt-2">
            <span class="text-xl">{{ apartment.name }}</span>
            <p class="">{{ apartment.location.city }}</p>
            <p class="">{{ apartment.price }}</p>
        </div>
    </div>
</template>