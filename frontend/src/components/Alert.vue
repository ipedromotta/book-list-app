<template>
  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
  </div>
</template>

<script>
  export default {
    name: 'AlertComponent',
    props: ['message'],
  };
</script>