<template>
    <div class="alert alert-success alert-dismissible fade show" role="alert">
      {{ message }}
    </div>
  </template>
  
<script setup>
const props = defineProps({
    message: String
})
</script>