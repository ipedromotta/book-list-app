<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <Books/>
  </div>
</template>

<script>
// @ is an alias to /src
import Books from '@/components/Books.vue';

export default {
  name: 'BooksView',
  components: {
    Books,
  },
};
</script>
